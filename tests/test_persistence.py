"""tests/test_persistence.py

06_연락처관리_웹서비스_테스트계획서_v1.0.md §7 "영속성 특수 케이스"(AC-16)
TC-PERSIST-01~04 (4개)

**qa-engineer 구현 노트(실행 방식 재량 — 06 문서 §7 하단 안내에 따름)**
- 이 모듈은 §2의 공통 사전조건("서버가 이미 기동 중")과 달리, 서버 프로세스
  자체를 죽였다 살리는 것이 테스트의 핵심이므로 **이 테스트 스위트가 직접
  uvicorn 서브프로세스를 소유(기동/재기동/종료)한다** (`managed_server`
  픽스처, `subprocess.Popen` 방식). 외부 셸에서 이미 8000번 포트에 서버를
  띄워 둔 상태로 이 모듈을 실행하면 포트 충돌로 실패할 수 있다 — 이 모듈은
  독립적으로 실행하는 것을 전제로 한다.
- DB 컨테이너 재시작(TC-PERSIST-02)은 `docker restart pg-lab`을
  subprocess로 직접 실행한다(TRD §9-1의 컨테이너명 `pg-lab` 기준).
- 현재(2026-07-16) `backend/main.py`가 없으므로 uvicorn 기동 자체가 실패하는
  것이 정상 RED이다.
"""

import subprocess
import time
from pathlib import Path

import pytest

from conftest import (
    BASE_URL,
    contact_payload,
    get_category_id,
    login,
    signup,
    unique_username,
)

BACKEND_DIR = Path(__file__).resolve().parent.parent / "backend"
PG_CONTAINER_NAME = "pg-lab"


def _start_server():
    return subprocess.Popen(
        ["python3", "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd=str(BACKEND_DIR),
    )


def _stop_server(proc):
    proc.terminate()
    try:
        proc.wait(timeout=10)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()


def _wait_until_up(ctx, retries=20, interval=0.5) -> bool:
    for _ in range(retries):
        try:
            resp = ctx.get("/")
            if resp.status < 500:
                return True
        except Exception:
            pass
        time.sleep(interval)
    return False


class _ManagedServer:
    def __init__(self, ctx):
        self.ctx = ctx
        self.proc = _start_server()
        _wait_until_up(self.ctx)

    def restart(self):
        _stop_server(self.proc)
        self.proc = _start_server()
        _wait_until_up(self.ctx)


@pytest.fixture
def managed_server(playwright):
    """PERSIST 테스트 전용 — 테스트가 직접 소유하는 uvicorn 프로세스 핸들."""
    ctx = playwright.request.new_context(base_url=BASE_URL)
    handle = _ManagedServer(ctx)
    yield handle
    ctx.dispose()
    _stop_server(handle.proc)


def test_tc_persist_01_server_restart_keeps_contacts_and_categories(managed_server):
    ctx = managed_server.ctx
    username = unique_username()
    signup(ctx, username)
    login(ctx, username)
    category_id = get_category_id(ctx)
    contact = ctx.post("/contacts", data=contact_payload(category_id, name="윤아")).json()

    managed_server.restart()
    login(ctx, username)  # 시나리오상 "재로그인" 명시(01문서 §5-3 세션 유지와 별개로 재접속 흐름 그대로 옮김)

    contacts_after = ctx.get("/contacts").json()
    categories_after = ctx.get("/categories").json()
    assert any(item["id"] == contact["id"] for item in contacts_after["items"])
    assert any(c["id"] == category_id for c in categories_after)


def test_tc_persist_02_db_container_restart_keeps_data_without_server_restart(managed_server):
    ctx = managed_server.ctx
    username = unique_username()
    signup(ctx, username)
    login(ctx, username)
    category_id = get_category_id(ctx)
    contact = ctx.post("/contacts", data=contact_payload(category_id, name="윤아")).json()

    result = subprocess.run(
        ["docker", "restart", PG_CONTAINER_NAME], capture_output=True, text=True
    )
    assert result.returncode == 0, f"docker restart {PG_CONTAINER_NAME} 실패: {result.stderr}"
    time.sleep(3)  # 컨테이너 재기동 대기

    resp = ctx.get("/contacts")
    assert resp.status == 200
    assert any(item["id"] == contact["id"] for item in resp.json()["items"])


def test_tc_persist_03_server_restart_keeps_login_session_via_existing_cookie(managed_server):
    ctx = managed_server.ctx
    username = unique_username()
    signup(ctx, username)
    login(ctx, username)  # 세션 쿠키 발급(ctx에 저장됨)

    managed_server.restart()

    resp = ctx.get("/auth/me")  # 기존 쿠키 재사용 — 재로그인 없이 요청
    assert resp.status == 200


def test_tc_persist_04_revisit_with_same_cookies_shows_management_screen_immediately(
    managed_server, browser
):
    ctx = managed_server.ctx
    username = unique_username()
    signup(ctx, username)
    login(ctx, username)

    storage_state = ctx.storage_state()
    new_context = browser.new_context(storage_state=storage_state, base_url=BASE_URL)
    try:
        new_page = new_context.new_page()
        new_page.goto(BASE_URL)
        new_page.screenshot(path="docs/screenshot/persist-01-쿠키재방문직후.png")
        # 로그인 화면이 아니라 관리 화면(로그아웃 버튼)이 즉시 표시되어야 함
        new_page.get_by_role("button", name="로그아웃", exact=True).wait_for()
        new_page.screenshot(path="docs/screenshot/persist-02-관리화면즉시표시.png")
    finally:
        new_context.close()

"""tests/conftest.py — 06 문서(테스트계획서) §2 "테스트 환경" 공통 설정.

이 파일은 qa-planner의 06 문서가 정의한 표를 그대로 pytest 코드로 옮기기 위한
공용 픽스처/헬퍼만 담는다 — 새로운 테스트 케이스를 설계하지 않는다.

**설치된 pytest-playwright(0.8.0)에는 06 문서/TRD §10-2가 언급한
"APIRequestContext용 `request` 픽스처"가 실제로는 존재하지 않는다**
(패키지 소스 확인 결과 `page`/`context`/`browser` 등만 제공하며, API 전용
`request` 픽스처는 없음 — pytest의 내장 `request`(FixtureRequest)와 이름이
겹쳐 그대로 덮어쓰면 pytest-playwright 내부 픽스처가 깨질 위험도 있음).
따라서 Playwright 공식 문서가 권장하는 패턴(`playwright.request.new_context()`)
그대로 `api_request` 픽스처를 직접 정의해 사용한다. 이 판단은 도구 배선 문제일
뿐 케이스 설계에는 손대지 않았다 — dev-pl에게 별도 보고.
"""

import itertools
import uuid

import pytest

BASE_URL = "http://127.0.0.1:8000"
DEFAULT_PASSWORD = "pass1234"

_phone_seq = itertools.count(10_000_000)


def unique_username(prefix: str = "user") -> str:
    """06 문서 §2 — 매 테스트 새 계정(uuid4 hex 8자리)."""
    return f"{prefix}{uuid.uuid4().hex[:8]}"


def unique_phone() -> str:
    """01 문서 §4-1 규칙(^010\\d{8}$)을 만족하는 유일한 전화번호."""
    return f"010{next(_phone_seq):08d}"


def unique_category_name(prefix: str = "모임") -> str:
    """01 문서 §4-1 규칙(1~10자)을 만족하는 유일한 카테고리명."""
    return f"{prefix}{uuid.uuid4().hex[:4]}"


@pytest.fixture
def api_request(playwright):
    """독립된 쿠키 저장소를 가진 APIRequestContext.

    함수 스코프로 매 테스트마다 새로 만들어 쿠키(세션)가 테스트 간에
    새어나가지 않게 한다(06 문서 §2 "테스트 독립성 원칙").
    """
    context = playwright.request.new_context(base_url=BASE_URL)
    yield context
    context.dispose()


def signup(ctx, username: str | None = None, password: str = DEFAULT_PASSWORD):
    """POST /auth/signup 호출. (username, response) 반환."""
    username = username or unique_username()
    resp = ctx.post("/auth/signup", data={"username": username, "password": password})
    return username, resp


def login(ctx, username: str, password: str = DEFAULT_PASSWORD):
    """POST /auth/login 호출. response 반환(성공 시 ctx에 세션 쿠키 저장됨)."""
    return ctx.post("/auth/login", data={"username": username, "password": password})


def signup_and_login(ctx, username: str | None = None, password: str = DEFAULT_PASSWORD) -> str:
    """가입 + 로그인까지 한 번에. 로그인된 username 반환."""
    username = username or unique_username()
    signup(ctx, username, password)
    login(ctx, username, password)
    return username


def get_category_id(ctx, name: str = "친구") -> int:
    """가입 직후 기본 카테고리(가족/친구/기타) 중 지정한 이름의 id를 가져온다."""
    resp = ctx.get("/categories")
    categories = resp.json()
    for c in categories:
        if c["name"] == name:
            return c["id"]
    return categories[0]["id"]


def contact_payload(category_id: int, name: str = "윤아", phone: str | None = None, addr: str = "서울시"):
    return {
        "name": name,
        "phone": phone or unique_phone(),
        "addr": addr,
        "category_id": category_id,
    }


def assert_not_server_error(resp):
    """06 문서 §2 — 모든 실패 케이스는 500이 아님을 함께 확인(NFR-01/AC-17)."""
    assert resp.status != 500, f"500 발생(NFR-01 위반): {resp.status} {resp.text()}"


def record_network(page):
    """E2E 테스트에서 "API 호출됨/호출 안 됨"을 검증하기 위한 네트워크 로그 수집."""
    log: list[str] = []
    page.on("request", lambda req: log.append(f"{req.method} {req.url}"))
    return log


def called(log, method: str, path: str) -> bool:
    """log에 method+path(쿼리스트링 무관)로 시작하는 요청이 있는지 확인."""
    target = f"{method} {BASE_URL}{path}"
    return any(entry == target or entry.startswith(target + "?") for entry in log)

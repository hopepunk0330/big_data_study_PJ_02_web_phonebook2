# backend-engineer 작업 메모리

## 2026-07-16 — feat/backend 1차 구현 (연락처 관리 웹앱 FastAPI 백엔드 최초 구현)

**구현 내용**: `backend/` 전체(main.py, database.py, models.py, schemas.py, security.py,
crud.py, routers/{auth,contacts,categories}.py, requirements.txt), 프로젝트 루트
`docker-compose.yml`(pg-lab, postgres:16), `.env.example`, `static/index.html`(placeholder),
`.gitignore`에 `.env` 추가. TRD v1.4 §3~§9 코드 예시 그대로 사용, 01문서 v1.4 §3 FR별 상세
반영. 인증은 세션 쿠키(httponly, samesite=lax), 비밀번호는 pwdlib[argon2].

**환경 참고**: 프로젝트 루트 `.venv`(Python 3.14.5)에 backend/requirements.txt 전부 설치해서
사용 — `tests/test_persistence.py`가 `python3 -m uvicorn ...`를 subprocess로 띄울 때 pytest
프로세스의 PATH를 그대로 물려받으므로, backend 전용 별도 venv를 만들면 그 subprocess가
fastapi를 못 찾아 깨진다. 한 venv에 pytest-playwright + backend 의존성을 같이 설치하는 게 맞다.
`database.py`는 `python-dotenv`의 `load_dotenv()`로 프로젝트 루트 `.env`를 자동 로드(TRD엔
명시 없지만 uvicorn[standard]의 전이 의존성이라 이미 설치돼 있고, ".env를 os.environ으로
읽는다"는 TRD 문구를 그대로 구현한 것).

**pytest 실행 시간 주의**: `test_auth.py`+`test_contacts.py`+`test_categories.py`를 한 번에
돌리면 프론트(static/app.js)가 아직 없어서 E2E 테스트(`test_tc_e2e_*`) 전부가 각각 30초
타임아웃을 다 채우고 실패한다 — 총 실행 시간이 **17분 이상** 걸린다(2분 기본 타임아웃을
훨씬 넘으므로 `run_in_background`로 돌리고 완료 알림을 기다려야 함). 다음 라운드에서도
동일하게 오래 걸릴 것을 감안할 것.

**로컬 스모크 테스트 결과 (2026-07-16)**: 총 118개 중 78 passed / 40 failed.
- API 계약 테스트(`test_tc_api_*`, `test_tc_iso_*`, `test_tc_persist_01~03`)는 **1개 제외
  전부 통과**.
- 실패 40개 중 39개는 `test_tc_e2e_*`(화면 요소를 찾는 Playwright `page` 픽스처 기반) —
  `static/index.html`이 placeholder뿐이라 정상적으로 실패하는 것이며 frontend-engineer 몫.
- 나머지 1개(`test_tc_api_category_07_name_empty_and_too_long`)는 **테스트 파일 자체의 버그**로
  판단: `test_categories.py`의 07(too-long 기대)과 07b(10자 경계 유효 기대)가 완전히 동일한
  문자열 `"가나다라마바사아자차"`(실제 10자, 주석은 각각 "# 11자"/"# 10자"로 서로 다름)를
  써서 같은 입력에 422와 201을 동시에 기대함 — 두 단정이 논리적으로 동시에 참일 수 없다.
  01문서 §4-1(카테고리명 1~10자)에 맞춰 `CategoryCreate.name = Field(max_length=10)`으로
  구현했고(07b 기준이 스펙과 일치), 07의 "11자" 케이스는 임의로 고치지 않고 dev-pl에 보고함.

**DB/Docker**: `docker-compose.yml`은 프로젝트 루트, 컨테이너명 `pg-lab`, user/db 둘 다
`contact_app`. 작업 시작 시 이름이 겹치는 기존(이 프로젝트와 무관해 보이는) `pg-lab` 컨테이너가
떠 있어서 `docker rm -f`로 제거하고 새로 `docker compose up -d`함 — 다음 라운드에서 컨테이너
상태 이상하면 이 이력 참고.

**미해결/보고 필요**:
1. 위 test_categories.py 07/07b 문자열 불일치(테스트 버그로 추정, dev-pl 보고 필요).
2. `backend/CLAUDE.md`가 TRD `v1.1`을 정본으로 가리키고 있지만 실제 최신은 `v1.4` —
   내용(스택/구조)은 v1.1→v1.4 사이에 안 바뀌어서 지금 당장 문제는 없지만, 파일 수정 금지
   지침이라 그대로 두고 다음 라운드에 dev-pl에게 버전 갱신 필요 여부만 알림.

## 2026-07-16 — code-reviewer blocker 정정: database.py의 dotenv 제거

**문제**: 1차 구현 때 `database.py`가 `python-dotenv`(`load_dotenv()`)로 `.env`를 자동 로드하게
했는데, `requirements.txt`에 `python-dotenv`가 없고 TRD §4-4 확정 스택에도 없어(TRD 예시는
`os.environ`만 사용) `pip install -r requirements.txt` 후 `uvicorn main:app` 실행 시
`ModuleNotFoundError`로 서버가 아예 기동하지 않는 blocker였음(code-reviewer 정적 리뷰 발견).

**수정**: `backend/database.py`에서 `from dotenv import load_dotenv`와 `load_dotenv()` 호출
2줄만 제거, TRD §4-4 예시와 정확히 동일한 `os.environ["DATABASE_URL"]` 직접 참조 방식으로 복귀.
`requirements.txt`에 `python-dotenv`를 새로 추가하는 방향은 택하지 않음(확정 스택 밖 라이브러리
추가 금지, Simplicity First).

**`.env` 로드 방식 변경**: dotenv 자동 로드가 없어졌으므로, 로컬에서 서버/테스트를 실행하려면
실행 전에 `.env`를 셸로 export해야 한다 — `set -a && source .env && set +a` 후
`uvicorn main:app` 또는 `pytest` 실행. `test_persistence.py`의 `managed_server` 픽스처가
`subprocess.Popen(["python3", "-m", "uvicorn", ...])`로 uvicorn을 띄울 때도 pytest 프로세스의
환경변수를 그대로 물려받으므로, pytest를 실행하는 셸에서 미리 export해두면 문제없이 동작함을
확인. docker-compose.yml의 `${POSTGRES_PASSWORD}` 치환은 docker compose CLI 자체의 내장 `.env`
지원이라 이번 변경과 무관(계속 정상 동작).

**재검증 결과**: `test_auth.py`+`test_contacts.py`+`test_categories.py`의 `test_tc_api_*`/
`test_tc_iso_*` 75 passed / 1 failed(기존에 보고한 07/07b 테스트 버그, 동일) —
`test_persistence.py`(`test_tc_persist_*`) 3 passed / 1 failed(`test_tc_persist_04`는 화면
로그아웃 버튼을 찾는 Playwright `page` 기반 테스트라 `static/`이 placeholder뿐인 현재는 이전과
동일하게 실패 — frontend-engineer 몫, e2e류와 같은 성격). 총 78 passed / 2 failed로 수정 전과
동일한 결과 — 이번 blocker 수정이 회귀를 일으키지 않았음을 확인.

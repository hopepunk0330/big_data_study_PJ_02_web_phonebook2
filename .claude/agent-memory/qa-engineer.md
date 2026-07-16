# qa-engineer 작업 로그

로그가 5개를 넘으면 가장 오래된 항목부터 삭제한다(git 히스토리에 전체 이력 보존됨).

---

## 2026-07-16 — 연락처 관리 웹서비스: 06 테스트계획서 → pytest 최초 변환 (TDD red)

**배경**: `backend/`에 실제 구현 코드 전무(가이드 `CLAUDE.md`만 존재). qa-planner가 확정한
`docs/planning/06_연락처관리_웹서비스_테스트계획서_v1.0.md`의 케이스 표를 `tests/` 아래
pytest 코드로 최초 변환. TDD 순서상 구현 이전 호출 — 전부 실패(RED)가 정상 기대치.

**만든 파일과 테스트 함수 개수**
- `tests/conftest.py` — 공용 픽스처/헬퍼(신규, 테스트 함수 없음)
- `tests/test_auth.py` — 43개 (AUTH 15 + PW 9 + SCREEN 1 + E2E SCR001 7 + SCR004 6 + SCR900 5)
- `tests/test_contacts.py` — 46개 (CONTACT 28 + E2E SCR002 12 + ISO 6)
- `tests/test_categories.py` — 25개 (CATEGORY 17 + E2E SCR003 8)
- `tests/test_persistence.py` — 4개 (PERSIST 01~04)
- 합계 **118개** (기존 `tests/test_example.py`는 무관한 스캐폴딩이라 손대지 않음)

**06 문서와의 수치 불일치 발견(dev-pl 보고 필요, 아직 미해소)**
06 문서 §4-1 "API 그룹 소계" 줄은 총 69개(CATEGORY 16개로 계산)라 적었지만, 실제
§4-4 표에는 `TC-API-CATEGORY-07b`가 별도 행으로 존재해 CATEGORY가 17개다. 표 자체를
소스 오브 트루스로 보고 07b를 포함한 17개 전부를 옮겼다. 이 때문에 이번 라운드의
실제 총계는 문서가 스스로 계산한 117개가 아니라 **118개**다. 케이스를 새로 만든 것이
아니라 이미 표에 있던 행을 셈에서 빠뜨린 문서 자체의 산술 오류로 보인다 — 발명이 아님.

**도구 관련 판단(보고 필요)**: TRD §10-2/06 문서 §2가 언급한 "pytest-playwright의 `request`
픽스처(APIRequestContext)"는 설치된 `pytest-playwright==0.8.0`에 실제로 존재하지 않는다
(패키지 소스에 fixture 없음 — `page`/`context`/`browser`만 제공). pytest 내장 `request`
(FixtureRequest)와 이름이 겹쳐 그대로 덮어쓰면 내부 픽스처가 깨질 위험도 있어, Playwright
공식 권장 패턴대로 `tests/conftest.py`에 `api_request` 픽스처(`playwright.request.new_context()`
래핑, 함수 스코프)를 직접 정의해 사용했다. 케이스 설계는 손대지 않고 배선만 한 것.

**TC-PERSIST-01/02 실행 방식**: 이 스위트가 직접 uvicorn 서브프로세스를 소유(`subprocess.Popen`
으로 기동 → kill → 재기동)하는 구조로 구현(`test_persistence.py`의 `managed_server` 픽스처).
DB 컨테이너 재시작은 `subprocess.run(["docker","restart","pg-lab"])`로 직접 실행. 외부 셸에
서버가 이미 떠 있으면 포트 충돌 가능 — 이 모듈은 독립 실행 전제.

**TC-UNIT-* 12개**: 06 문서 §8이 스스로 "파일 구조 미확정, tech-architect/planning-pl 확인
필요"라 명시해 이번 라운드에서 제외(qa-planner도 임의 결정 권한 밖이라고 못 박음). `tests/unit/`
등 새 파일 구조를 임의로 만들지 않았다.

**실행 결과**: `python -m pytest tests/test_auth.py tests/test_contacts.py tests/test_categories.py
tests/test_persistence.py -q` → **118개 전부 실패(RED)**. 실패 원인 전수 확인 결과 전부
`ECONNREFUSED 127.0.0.1:8000`(APIRequestContext) 또는 `net::ERR_CONNECTION_REFUSED`(Page.goto)
— AttributeError/TypeError/NameError 등 테스트 코드 자체의 버그로 인한 실패는 0건(전량 grep
검증 완료). 의도한 정상 RED.

**다음 라운드(backend-engineer 구현 완료 후) 재호출 시 할 일**: 같은 4개 파일을 그대로
재실행해 RED→GREEN 전환 여부만 확인. 구현 코드는 건드리지 않는다.

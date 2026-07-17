# qa-engineer 작업 로그

로그가 5개를 넘으면 가장 오래된 항목부터 삭제한다(git 히스토리에 전체 이력 보존됨).

---

## 2026-07-17 — `test_tc_api_category_07` 실패 원인: backend 버그 아님, 테스트 데이터 오타

**배경**: `python -m pytest` 재실행 중 `test_tc_api_category_07_name_empty_and_too_long`이
422 기대·201 실제로 실패. `backend/schemas.py`의 `CategoryCreate/Update`엔 이미
`max_length=10`이 정확히 있어 backend 버그 아님을 확인. 원인은 89번 줄 "too_long" 테스트
데이터 문자열 `"가나다라마바사아자차"`가 실제로 10글자(11자가 아님)였던 것 — 바로 아래
07b(경계값 10자 유효 케이스)와 완전히 같은 문자열을 써서 두 테스트가 서로 모순된 기대치를
갖고 있었음. `tests/test_categories.py` 89번 줄만 11글자 문자열(`"가나다라마바사아자차카"`)로
교체(surgical fix, backend 코드는 미변경).

**실행 결과**: `tests/test_categories.py -q` → API 테스트 17개(CATEGORY 01~16 + 07b) 전부
GREEN. `test_tc_api_category_07`/`07b` 모두 통과 확인.

**새로 발견한 이슈(dev-pl 보고 필요, 이번 요청 범위 밖이라 손대지 않음)**: 같은 파일의 E2E
`test_tc_e2e_scr003_01~08`(chromium) 8개가 전부 실패. `_login_via_page`가
`page.get_by_placeholder("영문 소문자·숫자 4~20자")`를 30초 타임아웃까지 못 찾음(프론트
서버 미기동 또는 로그인 화면 placeholder 텍스트 불일치로 추정), `get_category_id`도
`ctx.get("/categories").json()`이 문자열 리스트를 반환해 `c["name"]`에서 TypeError 발생.
이번 요청은 API 카테고리 테스트(07번)에 한정된 surgical fix라 이 E2E 8건은 조사·수정하지
않고 그대로 보고만 함 — 프론트 서버 기동 여부/로그인 페이지 마크업 확인이 backend/frontend
담당 쪽에서 필요.

---

## 2026-07-17 — E2E 12곳 `api_request` 미로그인 버그 수정(dev-pl 지시, surgical fix)

**배경**: `signup(api_request)`만 호출하고 `page`는 `_login_via_page`로 별도 로그인시키면서,
`api_request`(독립 쿠키 저장소) 쪽은 로그인 없이 그대로 `/categories`·`/contacts` 등 인증
필요 엔드포인트를 호출하던 12개 E2E 테스트를 수정. `signup(...)` 바로 다음 줄에
`login(api_request, username)`을 추가(`page`용 `_login_via_page`는 그대로 유지 — 의도된
별개 로그인).

**수정한 12곳**: `test_auth.py`의 `test_tc_e2e_scr900_02`, `_04`(2곳, `login`은 이미 import돼
있었음) / `test_contacts.py`의 `test_tc_e2e_scr002_01`, `_04`, `_06`, `_07`, `_08`, `_09`,
`_10`(7곳, `login` import 추가) / `test_categories.py`의 `test_tc_e2e_scr003_03`, `_05`,
`_06`(3곳, `login` import 추가). 지시받은 12곳 모두 실제로 "signup만 하고 그 `api_request`로
곧바로/나중에 인증 필요 호출"하는 패턴임을 직접 확인 후 수정 — 오탐·누락 없었음.

**검증**: (1) 수정한 12개 테스트를 실제 실행 → 전부 `_login_via_page`의
`get_by_placeholder("영문 소문자·숫자 4~20자")` 30초 타임아웃(프론트 미기동)으로 실패
— 이전처럼 `get_category_id`의 `c["name"]` TypeError나 401로 죽는 케이스는 0건, 실패 지점이
전량 "프론트엔드 부재"로 이동한 것 확인. (2) 별도로 `requests`로 backend에 직접
signup→(로그인 전)`GET /categories`→login→(로그인 후)`GET /categories`를 재현해 login 유무에
따라 401→200으로 바뀜을 재확인(수정 논리 자체의 타당성 검증, `api_request`가 아닌 `requests`
사용은 순수 확인용이며 테스트 코드에는 미반영).

**주의**: 프론트엔드가 아직 없어 `page` 기반 어설션까지 GREEN 확인은 불가 — frontend-engineer
작업 완료 후 같은 12개(및 나머지 SCR900/SCR002/SCR003 E2E 전체)를 재실행해 RED→GREEN 전환만
확인하면 된다. 이번 라운드는 "api_request 인증 버그 제거"까지만 확인 범위.

---

## 2026-07-17 — 전역 CLAUDE.md 규칙 반영: E2E(`page` 기반) 테스트에 스크린샷 캡처 호출 추가

**배경**: 전역/프로젝트 `CLAUDE.md`의 "playwright 테스트는 스텝마다 `docs/screenshot/`에 캡처"
규칙을 `test_tc_e2e_*`(및 `test_persistence.py`에서 실제 `Page` 객체를 쓰는 TC-PERSIST-04)에
반영. **테스트 로직(어설션·API 호출·셀렉터)은 한 글자도 건드리지 않고** `page.screenshot(path=...)`
줄만 핵심 단계(입력 직후·클릭/제출 직후·결과 확인 직전 등) 사이에 삽입하는 surgical 작업만 수행.
`docs/screenshot/` 폴더 신규 생성.

**적용 범위와 파일명 컨벤션**: `test_auth.py` 17개 E2E(SCR-001→`login-01~13`, SCR-004→
`pwreset-01~13`, SCR-900→`alert-01~11`, 화면 흐름별로 번호를 이어감) / `test_contacts.py`
SCR-002 12개(`contacts-01~19`) / `test_categories.py` SCR-003 8개(`category-01~10`) /
`test_persistence.py`는 `browser.new_context().new_page()`로 실제 `Page`를 다루는
`test_tc_persist_04`만 해당(`persist-01~02`) — 나머지 PERSIST 01~03은 `APIRequestContext`만
쓰고 화면이 없어 스크린샷 대상에서 제외(함수명이 `test_tc_e2e_*`가 아니라 `test_tc_persist_*`인
것과 일치, 지시문의 "page 픽스처를 쓰는 E2E 테스트"라는 괄호 설명을 실제 기준으로 삼음).
전체 68개 `page.screenshot(...)` 호출 추가, 파일명 중복 없음(전수 `uniq -d` 확인).

**스팟체크(프론트가 부분적으로 존재해 실행 가능했음)**: (1) `test_tc_e2e_scr001_01`(초기 화면
1스텝) 실행 → GREEN, `docs/screenshot/login-01-초기화면.png`(297KB) 실제 저장 확인 — 캡처
메커니즘 정상 동작. (2) `test_tc_e2e_scr003_01`(카테고리 추가, 로그인 이후 단계 필요) 실행 →
`_login_via_page`의 로그아웃 버튼 대기에서 30초 타임아웃으로 실패 — 프론트엔드 로그인/카테고리
화면이 아직 미완성이라는 기존 알려진 사실과 일치, 스크린샷 코드 자체의 결함 아님. `python -m
py_compile`로 4개 파일 전부 구문 오류 없음도 확인.

**다음 라운드(frontend-engineer 구현 완료 후)**: 같은 4개 파일 전체를 재실행해 RED→GREEN 전환
여부 확인 + `docs/screenshot/`에 몇 장이 실제로 쌓였는지 정식 카운트해 보고.

---

## 2026-07-17 — frontend-engineer 구현 완료 후 잔여 11건 로케이터 정밀화(surgical, dev-pl 지시)

**배경**: 8개 화면 구현 완료 후 107/118 GREEN, 잔여 11건이 실제 DOM에 동일 텍스트/역할 요소가
여러 개 동시 존재해 Playwright strict mode violation을 일으키는 것으로 지목받아 재조사·수정.
직접 실행해 원인을 1건씩 재현 후 수정(추정이 아니라 실측 확인).

**1) "이름" placeholder 충돌(exact=True 추가)**: `#add-name`(placeholder="이름")과
`#search-name`이 동시 존재해 `get_by_placeholder("이름")`이 strict mode violation. `test_auth.py`
3곳(456/471/484번 함수 내부) + `test_contacts.py` 6곳(연락처 추가 폼 필드)에 `exact=True` 추가.

**2) "추가" 버튼 중복(지시받은 것보다 범위가 넓었음)**: 지시문은 `test_tc_e2e_scr002_05` 1건만
언급했으나, 실측 결과 `#btn-add-contact`/`#btn-add-category` 두 버튼이 항상 동시에 DOM에 존재해
**".click()"/".dblclick()"도 index 없이는 전부 strict violation**이었다(사전에 "이름" placeholder
에서 먼저 죽어 가려져 있던 잠재 실패). `test_auth.py` 3곳 + `test_contacts.py` 5곳(365/382/397/429/543
번 줄, scr002_01/02/03/05/12)에 연락처 추가 버튼이므로 전부 `.nth(0)` 추가(카테고리 버튼은
`test_categories.py`가 이미 일관되게 `.nth(1)` 사용 중이라 그대로 둠). 검증 도중 발견해 dev-pl
지시 범위보다 넓게 고쳤음 — 원래 report된 "1건"이 아니라 실제로는 8개 테스트 함수에 영향.

**2-1) 부수 발견 — 검색 placeholder 문구 변경**: `#search-name`의 실제 placeholder가 지시문의
"이름 검색"이 아니라 `"이름으로 검색 (예: 윤아)"`로 이미 바뀌어 있었음(지시문도 "frontend-engineer가
Figma 재확인 후 바뀔 수 있다"고 미리 경고한 부분). `test_contacts.py`의 `get_by_placeholder("이름
검색")` 2곳을 실제 문구로 교체(검색 대상 필드 자체는 동일, 텍스트만 동기화).

**3) 카테고리명 3곳 동시 노출**: 실측 결과 지시문이 말한 "카테고리 관리 목록"이 아니라 `#add-category`
(select option), `#category-nav`(사이드바), `#category-manage-list`(관리 목록, `li[aria-label]`
구조) 3곳이었음(관리 목록도 포함되지만 위치가 다름). `test_tc_e2e_scr003_01`/`_03`은 원래 어설션이
없는 순수 동기화용 `.wait_for()`라 `.first`를 시도했으나 DOM 순서상 `.first`가 항상 숨겨진
`<option>`을 집어 "hidden" 상태로 30초 타임아웃 — `<option>`은 Playwright 기준 절대 visible이
될 수 없으므로 `#category-nav` 스코프로 재수정(테스트 취지상 "카테고리 목록"에 반영됐는지 확인이
가장 적합). `test_tc_e2e_scr003_07`(삭제 취소 후 "친구" 유지 확인 — 실제 assert 존재)은 삭제
버튼을 클릭한 동일 영역인 `#category-manage-list`로 스코프.

**부수 이슈 — 외부 uvicorn이 테스트 도중 다운됨**: 처음 재실행 중 서버가 죽어 114개 전부 실패로
보였다가(테스트 코드 문제 아님, `curl`로 확인) 재기동 후 정상. `test_persistence.py`는 자체
`subprocess.Popen`으로 uvicorn을 띄우는데 `.env`를 source하지 않은 셸에서 실행하면
`KeyError: DATABASE_URL`로 스폰된 서브프로세스가 즉시 죽음 — 반드시 `set -a; source .env; set +a`
후 이 파일만 단독 실행해야 함(코드 버그 아님, 실행 환경 이슈).

**검증 결과**: `test_auth.py`+`test_contacts.py`+`test_categories.py` 114개 전부 GREEN(기존
107→114, 11건 전부 해소 확인). `test_persistence.py` 별도 실행 4개 전부 GREEN. 합계 **118/118
GREEN**. `docs/screenshot/`에 72장 존재(우리 68장 + frontend-engineer 쪽 별도 3장 `main-*`,
1장 `contacts-18-검색인풋아이콘수정확인.png` — 우리 테스트 파일 소관 아님, 그대로 둠).

**다음에 재호출 시 참고**: 화면 구조가 다시 바뀌면(placeholder 문구, 버튼/셀렉터 배치) 이 라운드처럼
"이름"류 부분일치·"추가" 버튼 인덱스·카테고리명 3중 노출 패턴이 재발할 수 있음 — 매번 실측(브라우저
DOM) 먼저 확인 후 스코핑할 것, 지시문의 추정 범위만 믿고 고치면 놓치는 케이스가 있다(이번에 "1건"으로
보고된 게 실제로는 8건).

---

## 2026-07-17 — 오늘 최종 라운드: 단위/통합 테스트 분리 실행 + 보고서 문서화 절차 최초 적용

**배경**: dev-pl 지시로 오늘부터 "단위 테스트와 통합 테스트를 각각 별도로 실행하고, 실행마다
`docs/test-reports/`에 문서를 남긴다"는 새 절차 최초 적용. 오늘 하루 backend 데이터 버그 수정,
frontend 8개 화면 신규 구현, 검색 인풋/빈 상태 UI, 로케이터 정밀화가 모두 끝난 뒤의 최종 검증.

**환경 이슈(실행 전 직접 확인·조치)**: 지시문은 "backend가 이미 127.0.0.1:8000에 떠 있다"고
했으나 실제로는 다운돼 있었음(`curl` 000, `lsof -i :8000` 빈 결과, `ps aux | grep uvicorn` 빈
결과). DB 컨테이너 `pg-lab`은 정상 기동 중이었음. 시스템 `python3`엔 `uvicorn`/`pytest-playwright`
가 없고, 프로젝트 루트에 이미 만들어진 `.venv/bin/uvicorn`·`.venv/bin/pytest`가 있어 이걸로
`cd backend && set -a && source ../.env && set +a && .venv/bin/uvicorn main:app --host 127.0.0.1
--port 8000`으로 직접 기동 후 전체 라운드 진행. 이후 모든 pytest 실행은 `.venv/bin/python -m
pytest`로 통일.

**스모크 체크**: Playwright로 회원가입(빈 입력 클릭 시 "String should have at least 4
characters" 검증 배너 정상 노출 확인 후 필드 채워 재시도)→로그인→연락처 추가("테스트"/010.../
서울시, "추가되었습니다" 토스트 확인)→카테고리 추가("스모크")→로그아웃까지 전부 정상, `pageerror`
콘솔 에러 0건. 눈에 띄는 화면 깨짐 없음.

**단위 테스트(`test_tc_api_*`)**: `pytest tests/test_auth.py tests/test_contacts.py
tests/test_categories.py -k "test_tc_api" -v` → **70개 전부 PASSED**, 12.87s.

**지시문 패턴 밖 발견(dev-pl 보고 필요)**: `test_contacts.py`에 `test_tc_iso_01~06`(6개, 타
사용자 데이터 격리 검증, `api_request`만 쓰고 `page` 없음 — 순수 API 단위 테스트 성격)가 있는데
이름이 `test_tc_api_*`도 `test_tc_e2e_*`도 아니라서 지시받은 `-k "test_tc_api"` 패턴으로는
잡히지 않는 사각지대였음. 케이스를 새로 만들지 않고, 성격상 단위 테스트에 속한다고 판단해 별도로
`-k "test_tc_iso"`로 추가 실행 → **6개 전부 PASSED**, 2.49s. 정정된 단위 테스트 실제 총계는
70+6=**76개**. 다음 라운드부터 `-k`를 확장하거나 이 6개를 `test_tc_api_*`로 개명하는 걸 dev-pl에
제안.

**통합 테스트(`test_tc_e2e_*`)**: `pytest tests/ -k "test_tc_e2e" -v` → **38개 전부 PASSED**,
33.12s(SCR-001 7·SCR-004 6·SCR-900 5·SCR-002 12·SCR-003 8). 지난 라운드까지 있었던 SCR-003 8건
실패·strict mode violation 11건은 전혀 재현되지 않음(frontend 구현+로케이터 정밀화 유지 확인).

**`test_persistence.py`(TC-PERSIST, 단독 실행 필수)**: `set -a; source .env; set +a; .venv/bin/
python -m pytest tests/test_persistence.py -v` → **4개 전부 PASSED**, 5.34s. TC-PERSIST-02(DB
컨테이너 재시작)가 `docker restart pg-lab` 실제 실행하므로 이 스위트가 끝난 뒤 `pg-lab`이 다시
"Up 9 seconds"로 재기동된 것 확인(정상 동작).

**스크린샷**: `docs/screenshot/` 총 74장(개수 불변) — 파일명이 "화면+스텝순번" 고정 컨벤션이라
재실행 시 새로 추가되는 게 아니라 기존 파일이 최신 캡처로 덮어써짐(`mtime`으로 이번 실행분임을
직접 확인). 신규 파일 0장, 이 자체는 정상(테스트 코드가 매번 같은 경로에 `page.screenshot`
호출하는 구조이기 때문).

**보고서**: `docs/test-reports/unit-2026-07-17.md`(단위 70+6개), `docs/test-reports/
integration-2026-07-17.md`(E2E 38 + PERSIST 4) 신규 작성 — 이 절차가 처음 적용된 라운드라
`docs/test-reports/` 폴더 자체도 신규 생성.

**최종 결과**: 오늘 목표였던 118/118(구버전 집계) 대비 실제로는 76(단위, ISO 6 포함)+38(E2E)+
4(PERSIST)=**118개 전부 GREEN**, 실패 0건. 화면 버그/테스트 코드 버그 모두 발견되지 않음.

**다음 라운드 참고**: (1) 지시문이 "서버가 이미 떠 있다"고 해도 매번 `curl`/`lsof`로 직접
확인 후 필요시 `.venv/bin/uvicorn`으로 재기동할 것(이번처럼 실제로 안 떠 있을 수 있음). (2)
`test_tc_iso_*` 6개를 단위 테스트 실행 패턴에 포함시키는 게 확정되면 이 로그의 "정정된 총계" 부분
업데이트.

# qa-engineer 작업 로그

로그가 5개를 넘으면 가장 오래된 항목부터 삭제한다(git 히스토리에 전체 이력 보존됨).

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

---

## 2026-07-17 — 카테고리 삭제확인/이름수정 모달(4/6번) 구현 완료 후 최종 재검증

**배경**: dev-pl 지시로 카테고리 삭제확인/이름수정 모달 구현 완료(`test_categories.py` 25
passed 확인됨) 후 오늘 최종 확인 라운드. 단위/통합 분리 절차(이전 라운드에서 최초 적용)를
그대로 반복 적용해 두 보고서를 갱신.

**환경 확인**: 지시문과 달리 백엔드가 실제로는 다운(`curl` 000)돼 있어 `.venv/bin/uvicorn`으로
재기동 후 진행(DB 컨테이너 `pg-lab`은 기동 중이었음) — 매 라운드 반복되는 패턴이라 앞으로도
"떠 있다"는 말을 그대로 믿지 않고 직접 확인할 것.

**단위 테스트**: `pytest tests/test_auth.py tests/test_contacts.py tests/test_categories.py -k
"test_tc_api or test_tc_iso" -v` → **76개 전부 PASSED**, 9.46s(AUTH 24 + CONTACT 27+ISO6=33 +
CATEGORY 19). 이전 라운드부터 `test_tc_iso_*`를 정식 단위 테스트 실행 패턴에 포함시키기로 한
제안이 이번 라운드에 실제로 반영됨(한 명령으로 통합 실행).

**통합 테스트**: `pytest tests/ -k "test_tc_e2e" -v` → **38개 전부 PASSED**, 28.51s. 특히
지시받은 대로 `test_categories.py`만 별도 재실행해 SCR-003 8개(scr003_01~08) 개별 PASSED를
확인 — 새 모달 패턴(이름수정 03/04, 삭제확인 05/06/07)으로 바뀐 뒤에도 회귀 없음을 명시적으로
검증(단순히 "38 passed" 총계만 보지 않고 개별 테스트명까지 grep으로 확인).

**`test_persistence.py`**: `.env` source 후 단독 실행 → **4개 전부 PASSED**, 4.51s. TC-PERSIST-02가
`pg-lab`을 재시작하므로 전체 스위트 종료 후 `docker ps`/`curl`로 서버·DB 정상 상태 재확인(둘 다
정상).

**최종 결과**: 단위 76 + 통합 42(E2E 38 + PERSIST 4) = **118개 전부 GREEN**, 실패 0건. 오늘
하루 전체 작업(backend 데이터 버그 수정, frontend 8개 화면, 검색 인풋, 빈 상태, 카테고리 모달
2개) 종합 회귀 없음 확인.

**스크린샷**: `docs/screenshot/` 총 74장(개수 불변, 파일명 고정 컨벤션이라 매 실행마다 덮어씀).
`category-01~10-*.png`(SCR-003, 신규 모달 스텝 포함) 10장 이번 실행분으로 갱신 확인.

**보고서**: `docs/test-reports/unit-2026-07-17.md`, `docs/test-reports/integration-2026-07-17.md`
둘 다 이번 실행 결과로 갱신(같은 날 재실행이라 덮어쓰되, 파일 내 "이력(같은 날 이전 실행)"
섹션에 이전 수치와 비교해 회귀 없음을 남겨 이력 보존).

**다음 라운드 참고**: `test_tc_iso_*`를 `-k "test_tc_api or test_tc_iso"`로 함께 실행하는 게
이제 정착된 패턴 — 앞으로도 이 커맨드를 단위 테스트 기본 실행 명령으로 사용.

---

## 2026-07-18 — 사용자 버그 리포트("검색 필터링 안 됨") 라이브 재현 확인(dev-pl 긴급 지시)

**배경**: 사용자가 "검색창에 이름을 써도 필터링이 안 된다"고 보고, 메인 세션이 백엔드 API는
curl로 정상 확인 → 프론트 쪽 라이브 재현만 확인해 달라는 요청. frontend-engineer가 `static/`을
별도 라운드로 수정 중이라 이번엔 `static/` 코드를 일절 건드리지 않고 재현/진단만 수행(테스트
코드도 새로 커밋하지 않고 스크래치패드 1회성 스크립트로 처리).

**1) 기존 회귀 케이스 재실행**: `test_tc_e2e_scr002_04_search_by_name_replaces_list`(06 문서
§5-3, qa-planner 기설계 TC-E2E-SCR002-04)만 단독 재실행 → **1 passed**(1.11s). 이 테스트는
`api_request`로 "윤아" 2건을 미리 넣고 검색하는 패턴.

**2) 라이브 재현 스크립트(사용자 시나리오 그대로, UI로 계정 생성부터)**: pytest 정식 케이스가
아닌 1회성 Playwright 스크립트(스크래치패드, 저장소 미커밋)로 회원가입→로그인→UI 폼으로
서로 다른 이름 4건("윤아"/"철수"/"영희"/"민수") 추가→검색창에 "윤아"→[검색] 클릭까지 실제
사용자 흐름을 재현. 콘솔(`console`/`pageerror`)·네트워크(`/contacts` 요청/응답) 전부 캡처.

**결과: 재현 안 됨.** 검색 후 화면에 "윤아" 1건만 남고 "검색결과 총 1건"으로 정상 교체(다른
3건 사라짐). 네트워크 로그상 `GET /contacts?name=%EC%9C%A4%EC%95%84` → `200` 정상 요청/응답
확인. `pageerror` 0건. 페이지 최초 진입(로그인 전) 시점의 401 콘솔 에러 1건은 검색 동작과
무관(로그인 이후 흐름엔 영향 없음).

**결론**: 현재 코드에서는 버그 미재현. 가능한 원인(추정): (1) 사용자 테스트 시점과 현재 사이에
frontend-engineer 라운드에서 이미 수정됐을 가능성, (2) 브라우저 캐시로 구버전 `app.js` 실행,
(3) 이번엔 "전체" 카테고리+신규 계정 조합만 검증 — 특정 카테고리 필터 선택 후 검색 등 다른
조합은 검증 범위 밖(재현 안 되면 사용자에게 정확한 재현 스텝 추가 요청 필요).

**보고서**: `docs/test-reports/integration-2026-07-18.md`(단발성 라이브 재현 확인 전용, 전체
회귀 스위트 재실행 아님) 신규 작성. 스크린샷 `docs/screenshot/search-repro-01~06` 6장 신규 캡처.

**주의(역할 경계 재확인)**: `static/index.html`/`app.js`는 이번 작업에서 읽기만 하고 수정하지
않음 — frontend-engineer 병행 라운드와 충돌 방지 지시를 그대로 준수.

---

## 2026-07-18 — 카테고리 nav 클릭 필터링 신규 기능 테스트 4건 추가(frontend-engineer 제안 케이스)

**배경**: 사용자 결정으로 사이드바 카테고리 nav 클릭 시 실제 필터링 동작이 신규 추가됨
(frontend-engineer 구현 완료, `static/app.js`의 `selectCategoryFilter`/`renderCategoryNav`/
`runSearch`). 원래 02 화면정의서 v1.15 255행("클릭 시 필터링 동작 없음")을 사용자가 이번에
기능 확장하기로 결정 — 문서 개정은 dev-pl이 별도로 planning 팀에 요청 예정, 이 라운드에서 02
문서는 건드리지 않음. 06 테스트계획서에도 이 기능 관련 문구가 전혀 없어(grep 0건 확인) qa-planner
설계 케이스가 아니라 frontend-engineer가 제안한 4개 케이스를 실제 구현 코드를 직접 읽고 확인한
뒤 옮김.

**구현 확인(코드 리딩)**: `selectCategoryFilter`는 클릭 시 검색창 값을 비우고
`category_id` 쿼리로 `loadContacts` 호출, `renderCategoryNav`는 `state.selectedCategoryId`
기준으로 `active` 클래스+`aria-pressed`를 부여. `runSearch`는 검색 실행 시
`state.selectedCategoryId`를 null로 되돌려 "전체"를 다시 active로 만든다 — 즉 카테고리 필터와
검색은 상호 배타적으로 서로를 리셋하는 구조(양방향 모두 확인 후 테스트 작성).

**추가한 4개 테스트**(`tests/test_categories.py`, SCR-003 E2E 섹션 맨 끝에 추가):
1. `test_tc_e2e_scr003_09_category_nav_click_filters_contacts_table` — "친구" 클릭 시 해당
   카테고리 연락처만 테이블에 표시.
2. `test_tc_e2e_scr003_10_category_nav_click_shows_active_state` — 클릭 항목
   `aria-pressed="true"`+`active` 클래스, 나머지는 `false`/클래스 없음.
3. `test_tc_e2e_scr003_11_category_nav_click_all_resets_filter` — "전체" 클릭 시 필터 해제,
   전체 목록 복원.
4. `test_tc_e2e_scr003_12_category_filter_and_search_are_mutually_exclusive` — 카테고리 필터
   중 검색 실행(→ 전체 active로 복귀, 검색은 카테고리 무관 전체 대상) / 검색 중 카테고리 클릭
   (→ 검색어 지워지고 카테고리 필터만 적용) 양방향 모두 검증.

**검증 결과**: 신규 4개 단독 실행 4 passed(7.07s). 단위 테스트(`test_tc_api or test_tc_iso`)
76 passed(11.34s, 회귀 없음). 전체 E2E(`test_tc_e2e`) 42 passed(38 기존+4 신규, 32.41s).
TC-PERSIST 4 passed(4.92s, `pg-lab` 재시작 후 정상 재기동 확인). 합계 **122개(76+42+4) 전부
GREEN**, 실패 0건.

**스크린샷**: 신규 8장(`category-11-필터전전체목록.png`~`category-16-검색중카테고리클릭.png`,
파일당 1~2스텝).

**발견 사항(dev-pl 보고)**: `docs/screenshot/category-11-이름수정모달.png`,
`category-12-삭제확인모달.png` 2개 orphan 파일 발견 — 현재 어떤 테스트 코드도 이 파일명을
생성하지 않음(과거 리팩토링 이전 버전의 잔재로 추정). 이번에 신규 케이스가 같은 번호(11/12)를
이어받아 사용해 번호가 겹친다(파일명은 다름). 삭제하지 않고 보고만 함(산출물 임의 삭제 금지 원칙).

**보고서**: `docs/test-reports/unit-2026-07-18.md`(신규), `docs/test-reports/
integration-2026-07-18.md`(같은 날 앞선 "검색 필터링 버그 재현" 섹션에 새 섹션 이어붙임, 덮어쓰지
않음).

---

## 2026-07-18 — 프론트엔드 정합화 작업 완료 후 최종 전체 회귀(dev-pl 지시, 오늘 마무리 라운드)

**배경**: 오늘 하루 진행된 프론트엔드 정합화 작업(카테고리 모달, 아이콘, 로고, 배너 오버레이 통합,
사이드바 스크롤, 테이블 컬럼/스크롤, 포커스 상태, 웹폰트 로딩 등)이 전부 완료된 뒤 dev-pl이 요청한
최종 마무리 회귀 라운드. 새 테스트 케이스 추가 없이 기존 스위트 전체 재실행 + 보고서 갱신 +
어제자 보고서 아카이브가 목적.

**환경 확인(매번 반복되는 패턴)**: 지시 없이도 직접 `curl`/`docker ps`로 확인 — 이번에도 백엔드가
다운(`curl` 000)돼 있어 `.venv/bin/uvicorn`으로 재기동 후 진행(DB 컨테이너 `pg-lab`은 기동 중).

**단위 테스트**: `pytest tests/test_auth.py tests/test_contacts.py tests/test_categories.py -k
"test_tc_api or test_tc_iso" -v` → **76개 전부 PASSED**, 12.06s. 오늘 앞선 두 라운드와 동일 수치,
정합화 작업이 UI 전용이라 API 로직 영향 없음을 실측으로 재확인.

**통합 테스트**: `pytest tests/ -k "test_tc_e2e" -v` → **42개 전부 PASSED**, 51.15s(SCR-001 7 +
SCR-004 6 + SCR-900 5 + SCR-002 12 + SCR-003 12). `test_persistence.py`(`.env` source 후 단독
실행) → **4개 전부 PASSED**, 5.57s(TC-PERSIST-02가 `pg-lab` 재시작 후 8초 만에 정상 재기동
확인). 합계 **46개 전부 GREEN**.

**최종 결과**: 단위 76 + 통합 46(E2E 42 + PERSIST 4) = **122개 전부 GREEN**, 실패 0건. 오늘 하루
전체 작업(버그 재현 확인, 카테고리 nav 필터링 신규 4건, 프론트엔드 정합화)을 통틀어 회귀 없음.

**스크린샷**: `docs/screenshot/` 실측 총 **82장**. 로그인/회원가입/비밀번호재설정(`login-*`,
`pwreset-*`), 세션만료/오류알림(`alert-*`), 연락처 CRUD+빈상태(`contacts-*`), 카테고리 CRUD+nav
필터링(`category-*`), 데이터지속성(`persist-*`) 등 정식 pytest 스위트 커버 화면 75장(mtime
05:14 전후, 이번 실행분으로 갱신 확인) + 오늘 정합화 작업 자체를 캡처한 `round-login-*`/
`round-main-*` 7장(mtime 05:08, 우리 테스트 코드 소관 아닌 별도 라운드 산출물 — 그대로 둠) = 82장.
과거 로그에 있던 orphan 파일(`category-11/12-이름수정모달·삭제확인모달.png`)은 이번 실측에서
더 이상 발견되지 않음(자연 소멸, 재조치 불필요). 지난 라이브 재현 라운드의 `search-repro-*`
6장(스크래치패드 산출물, 미커밋)도 남아있지 않음 — 둘 다 정상.

**보고서**: `docs/test-reports/unit-2026-07-18.md`/`integration-2026-07-18.md`를 지시대로
최종 라운드 내용으로 덮어씀(단, integration은 기존 관례대로 오늘 앞선 두 섹션 뒤에 세 번째
섹션으로 이어붙이는 형태 유지 — 완전 삭제 없이 이력 보존). 어제자(`unit-2026-07-17.md`,
`integration-2026-07-17.md`)는 `docs/test-reports/old/`로 이동(원본 파일명 그대로 보존, 신규
생성).

**다음 라운드 참고**: `round-*` 접두사 스크린샷은 우리 테스트 스위트가 생성하는 파일이 아니므로
회귀 스위트 재실행 시 갱신되지 않는 게 정상 — 개수 확인 시 혼동 주의.

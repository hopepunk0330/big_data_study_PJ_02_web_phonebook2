# 통합 테스트(E2E) 실행 보고서 — 2026-07-18 (검색 필터링 버그 리포트 라이브 재현 확인)

## 배경
- 사용자 보고: "검색창에 이름을 써도 필터링이 안 된다"
- 메인 세션이 `GET /contacts?name=윤아`를 curl로 직접 확인해 백엔드 API는 정상 동작 확인 →
  프론트엔드(`static/index.html`/`app.js`) 쪽 라이브 재현 여부 확인을 QA에 요청.
- **주의**: frontend-engineer가 `static/` 아래 파일을 별도 라운드로 계속 수정 중 → 이번 작업에서는
  `static/` 코드를 일절 수정하지 않고 재현 확인만 수행.

## 실행 정보
- 백엔드: `127.0.0.1:8000` (이미 uvicorn 기동 중, 별도 재기동 불필요)
- 실행 일시: 2026-07-18

## 1. 기존 회귀 테스트: TC-E2E-SCR002-04 재실행
- 실행 명령: `.venv/bin/python -m pytest tests/test_contacts.py -k "test_tc_e2e_scr002_04" -v --durations=0`
- 대상: `test_tc_e2e_scr002_04_search_by_name_replaces_list` (06 문서 §5-3, SCR-002/AC-08 —
  qa-planner가 이미 설계한 케이스, 새로 만들지 않음)
- **결과: 1 passed** (소요 1.11s)

## 2. 라이브 재현 스크립트 (사용자 시나리오 그대로: UI로 회원가입 → 로그인 → 서로 다른 이름 4건을
   UI 폼으로 추가 → 검색창에 "윤아" 입력 → [검색] 클릭)
- pytest 정식 케이스가 아닌 1회성 진단 스크립트(콘솔/네트워크 로그 캡처 목적, 저장소에 커밋 안 함,
  스크래치패드에서 실행)로 사용자가 보고한 상황을 최대한 그대로 재현.
- 추가한 연락처: 윤아 / 철수 / 영희 / 민수 (4건, 카테고리 "가족")
- 검색어: "윤아"

### 결과
- **재현되지 않음** — 검색 후 화면에 "윤아" 1건만 남고 "검색결과 총 1건"으로 정상 교체됨. "철수"
  등 나머지 3건은 화면에서 사라짐(정상 필터링).
- 네트워크 로그: `GET /contacts?name=%EC%9C%A4%EC%95%84` → `200` 정상 요청/응답 확인(요청 자체가
  안 나가는 문제도, 응답을 반영 안 하는 문제도 없음).
- 콘솔: `[error] Failed to load resource: the server responded with a status of 401
  (Unauthorized)` 1건 발생 — 페이지 최초 진입(로그인 전) 시점의 401로, 검색 동작과는 무관(로그인
  이후 흐름에는 영향 없음).
- `page.on("pageerror", ...)` 캡처된 JS 런타임 에러 없음.

## 결론
- **현재 코드(2026-07-18 시점)에서는 사용자가 보고한 "검색 필터링 안 됨" 현상이 재현되지 않음.**
- 가능한 원인(추정, 확정 아님):
  1. 사용자가 테스트한 시점과 현재 사이에 frontend-engineer 라운드에서 이미 수정됐을 가능성.
  2. 브라우저 캐시(오래된 `app.js` 캐시)로 구버전 스크립트가 실행됐을 가능성.
  3. 재현 스크립트는 "전체" 카테고리 상태 + 신규 계정으로만 검증함 — 특정 카테고리 필터를 먼저
     선택한 상태에서 검색을 시도하는 등, 이번에 다루지 않은 조합은 검증 범위 밖(사용자가 정확한
     재현 스텝을 추가로 제공하면 재확인 가능).

## 실패 케이스
없음(1건 pytest 재실행 GREEN, 1건 라이브 재현 스크립트 정상 동작 확인 — 버그 미재현).

## 스크린샷
- `docs/screenshot/search-repro-01-초기화면.png` ~ `-06-검색결과.png` 총 6장 캡처(1회성 스크래치패드
  스크립트 산출물, 저장소 미커밋 — 이번 최종 라운드 시점 `docs/screenshot/` 실측 목록에는 남아있지
  않음. 정식 pytest 케이스가 아니므로 회귀 스위트 재실행 시 재생성되지 않는 게 정상).

## 참고
- `static/` 코드는 이번 작업에서 수정하지 않음(읽기만 수행, frontend-engineer 병행 라운드와의
  충돌 방지).
- 이 섹션은 이번 특정 버그 리포트에 대한 라이브 재현 확인 전용이며, 전체 회귀 스위트 실행 결과는
  아니다(전체 회귀 결과는 아래 이어지는 섹션 참고).

---

# 통합 테스트(E2E) 실행 보고서 — 2026-07-18 (카테고리 nav 클릭 필터링 신규 케이스 추가 + 전체 회귀)

## 배경
- 사용자 결정으로 사이드바 카테고리 nav 클릭 필터링 기능이 신규 추가됨(frontend-engineer 구현
  완료, `static/app.js`의 `selectCategoryFilter`/`renderCategoryNav`/`runSearch`). 원래 02
  화면정의서 v1.15 255행("클릭 시 필터링 동작 없음(표시 전용)")을 사용자가 이번에 기능 확장하기로
  결정 — 문서 개정은 dev-pl이 별도로 planning 팀에 요청 예정(이 라운드에서 02 문서는 미변경).
- qa-planner의 06 문서에는 이 신규 기능에 대한 설계 케이스가 없어(§5-4 SCR-003에 관련 문구 검색
  결과 0건 확인), frontend-engineer가 제안한 4개 케이스를 실제 구현(`static/app.js`)을 직접 읽고
  확인한 뒤 `test_categories.py`(SCR-003 E2E 섹션)에 `test_tc_e2e_scr003_09~12`로 추가.

## 신규 추가 테스트 케이스 (4개)
1. `test_tc_e2e_scr003_09_category_nav_click_filters_contacts_table` — 사이드바 "친구" 클릭 시
   테이블에 "친구" 카테고리 연락처만 표시되는지("가족" 연락처는 제외).
2. `test_tc_e2e_scr003_10_category_nav_click_shows_active_state` — 클릭한 항목이
   `aria-pressed="true"`+`active` 클래스로, 나머지("전체")는 `aria-pressed="false"`로 구분되는지.
3. `test_tc_e2e_scr003_11_category_nav_click_all_resets_filter` — "친구" 필터 적용 후 "전체" 클릭
   시 필터가 해제되고 전체 목록이 복원되는지.
4. `test_tc_e2e_scr003_12_category_filter_and_search_are_mutually_exclusive` — 실제 구현 동작을
   먼저 확인 후 그대로 검증: (a) 카테고리 필터 적용 중 검색 실행 → `runSearch`가
   `selectedCategoryId`를 null로 되돌려 "전체"가 다시 active 되고 검색은 카테고리 무관 전체 대상으로
   실행됨, (b) 검색 결과가 남아 있는 상태에서 카테고리 클릭 → `selectCategoryFilter`가 검색창 값을
   비우고 카테고리 필터만 적용함. 두 방향 모두 검증.

## 실행 정보(이 섹션 실행분)
- 실행 명령(신규 4개 단독): `.venv/bin/python -m pytest tests/test_categories.py -k "scr003_09 or scr003_10 or scr003_11 or scr003_12" -v`
- 실행 명령(전체 E2E 회귀): `.venv/bin/python -m pytest tests/ -k "test_tc_e2e" -v`
- 실행 명령(TC-PERSIST, 단독): `set -a; source .env; set +a; .venv/bin/python -m pytest tests/test_persistence.py -v`
- 백엔드: `127.0.0.1:8000`(기동 확인), DB 컨테이너 `pg-lab` 기동 확인
- 실행 일시: 2026-07-18(신규 기능 추가 직후 라운드)

## 결과 요약(이 섹션 실행분)
- **신규 4개: 4 passed**, 7.07s
- **전체 E2E(`test_tc_e2e_*`): 42 passed**, 32.41s (기존 38 + 신규 4, 실패 0)
- **TC-PERSIST(`test_persistence.py`): 4 passed**, 4.92s
- **합계: 46 passed / 0 failed**

## 스크린샷(이 섹션 실행분)
- 신규 8장: `category-11-필터전전체목록.png`, `category-12-친구필터적용.png`,
  `category-13-친구액티브상태.png`, `category-14-전체클릭필터해제.png`,
  `category-15-카테고리필터중검색실행.png`, `category-16-검색중카테고리클릭.png`
  (테스트 함수당 1~2장, 총 8회 `page.screenshot()` 호출).

## 발견 사항(dev-pl 보고 필요, 미해결 이월)
- **번호 중복 orphan 스크린샷**: `docs/screenshot/category-11-이름수정모달.png`,
  `category-12-삭제확인모달.png` 2개 파일명이 과거 리팩토링 이전 버전의 잔재로 존재했었음(현재
  어떤 테스트 코드도 생성하지 않음). 이번 최종 라운드 실측 결과 이 두 파일은 현재
  `docs/screenshot/` 목록에 더 이상 존재하지 않음(자연 소멸 또는 별도 정리된 것으로 추정) — 재확인
  결과 문제 해소, 별도 조치 불필요.

---

# 통합 테스트(E2E) 실행 보고서 — 2026-07-18 (프론트엔드 정합화 작업 완료 후 최종 회귀)

## 배경
- 오늘 하루 진행된 프론트엔드 정합화 작업(카테고리 모달, 아이콘, 로고, 배너 오버레이 통합, 사이드바
  스크롤, 테이블 컬럼/스크롤, 포커스 상태, 웹폰트 로딩 등)이 모두 완료된 뒤의 최종 마무리 회귀
  라운드. dev-pl 지시로 전체 E2E + TC-PERSIST 재실행.
- 이번 라운드에서 새로 추가된 통합 테스트 케이스는 없음 — 오늘 앞선 라운드에서 이미 42개(E2E)+
  4개(PERSIST)로 확정된 스위트를 그대로 최종 재실행해 회귀 여부만 확인.

## 실행 정보
- 실행 명령(전체 E2E): `.venv/bin/python -m pytest tests/ -k "test_tc_e2e" -v --durations=0`
- 실행 명령(TC-PERSIST, `.env` source 필수): `set -a; source .env; set +a; .venv/bin/python -m pytest tests/test_persistence.py -v --durations=0`
- 백엔드: `127.0.0.1:8000` — 실행 전 다운 상태 확인 후 `.venv/bin/uvicorn`으로 재기동, `curl
  /docs` → 200 확인
- DB 컨테이너 `pg-lab`: 기동 확인(`docker ps`)
- 실행 일시: 2026-07-18(최종 라운드)

## 결과 요약
- **전체 E2E(`test_tc_e2e_*`): 42 passed / 0 failed**, 소요 **51.15s**(SCR-001 7 + SCR-004 6 +
  SCR-900 5 + SCR-002 12 + SCR-003 12(기존 8 + nav 필터링 4))
- **TC-PERSIST(`test_persistence.py`): 4 passed / 0 failed**, 소요 **5.57s**
- **합계: 46 passed / 0 failed**, 총 소요 약 **56.72s**

## 파일별 내역
| 파일 | 통과 | 실패 |
|---|---|---|
| tests/test_auth.py (SCR-001 7 + SCR-004 6 + SCR-900 5) | 18 | 0 |
| tests/test_categories.py (SCR-003 12) | 12 | 0 |
| tests/test_contacts.py (SCR-002 12) | 12 | 0 |
| tests/test_persistence.py (TC-PERSIST 01~04) | 4 | 0 |
| **합계** | **46** | **0** |

## 실패 케이스
없음(전부 GREEN).

## TC-PERSIST 사후 확인
- `test_tc_persist_02`가 실행 중 `docker restart pg-lab`을 수행 — 스위트 종료 후 `docker ps`로
  `pg-lab` 상태 재확인: `Up 8 seconds`로 정상 재기동됨.
- `curl /docs` → `200`으로 서버도 정상 응답 유지 확인.

## 스크린샷
- 이번 최종 라운드 실측 결과 `docs/screenshot/` 총 **82장** 확인. 로그인/회원가입/비밀번호 재설정
  (`login-*`, `pwreset-*`), 세션 만료/오류 알림(`alert-*`), 연락처 CRUD(`contacts-*`, 빈 상태
  `contacts-table-empty-state-*`), 카테고리 CRUD+nav 필터링(`category-*`), 데이터 지속성
  (`persist-*`) 등 오늘까지의 전체 테스트 스위트가 커버하는 화면이 모두 포함됨을 확인.
- 추가로 오늘 프론트엔드 정합화 작업 자체를 별도로 캡처한 `round-login-01-초기화면-폰트로딩.png`,
  `round-main-01~06-*.png`(대시보드 폰트 로딩, 연락처 수정 모달, 카테고리 이름수정/삭제확인 모달,
  카테고리 추가 에러 공통 슬롯, 사이드바 입력창 노출 확인) 7장이 함께 존재 — 이 7장은 pytest 회귀
  스위트가 생성한 파일이 아니라(고정 파일명 컨벤션 밖의 `round-` 접두사) 정합화 작업 확인용 별도
  캡처로 판단됨(우리 테스트 코드 소관 아님, 그대로 둠).
- 파일당 mtime 확인 결과 `category-*`/`contacts-*`/`login-*` 등 75장은 이번 최종 회귀 실행 시각
  (05:14 전후)으로 갱신, `round-*` 7장은 그보다 앞선 시각(05:08)의 별도 라운드 산출물임을 확인함
  (합계 82장, 개수 불일치 없음).

## 이력(같은 날 이전 실행)
- 이번 라운드 이전(오늘 앞선 두 섹션): (1) "검색 필터링 안 됨" 버그 라이브 재현 확인(1건 회귀
  재실행 GREEN + 1회성 스크립트 미재현), (2) 카테고리 nav 클릭 필터링 신규 4개 추가 + 전체 회귀
  46 passed. 이번 최종 라운드도 동일하게 **46 passed / 0 failed**로 신규 기능 추가 이후 오늘
  전체 프론트엔드 정합화 작업을 거치고도 **회귀 없음**을 재확인.
- 전날(2026-07-17) 최종 라운드: E2E 38 + PERSIST 4 = 42개 GREEN(`docs/screenshot/old/
  integration-2026-07-17.md`로 이관) — 어제 이후 SCR-003 nav 필터링 4건 순증(38→42)만 있고
  그 외 회귀는 없음.

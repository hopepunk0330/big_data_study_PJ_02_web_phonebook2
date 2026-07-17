# frontend-engineer 작업 로그

## 2026-07-17 — 빈 상태(EmptyState) UI 신규 구현 (missing-screens.md 7번, 데드라인 라운드)

**배경**: `missing-screens.md` 7번 항목 — "검색 결과 없음"과 "가입 직후 데이터 0건"은 의미가 다른데 기존 구현엔 둘 다 없었다(연락처 0건이면 빈 테이블만 남음). 확정 프레임 `main-검색없음`(`501:4218`, fileKey `zgGlMBwFglaDlaeyP4CkgR`)을 `get_design_context`로 재조회해 `EmptyState`(`517:2721`) 구조를 그대로 옮겼다: `Pixel/NoResult` 아이콘(40×44, sky-500 몸통 21path + coral-500 크랙 6path — 에셋 URL에서 curl로 받아보니 순수 path라 raw hex를 `var(--color-sky-500)`/`var(--color-coral-500)` 참조로 바꿔 인라인 SVG로 옮김, 이전 검색 아이콘과 동일한 패턴) + 타이틀(Black 15px ink) + 서브텍스트(Regular 12px `--color-text-muted-subtle`) + CTA.

**분기 로직**: `loadContacts(params)`에 `state.isSearchActive = !!(params && params.name)` 추가(기존 `list-title` 분기와 동일 조건 재사용, surgical). `renderContactRows()`가 `state.contacts.length === 0`일 때 `renderEmptyState(tbody)`를 호출해 `<tbody>` 안에 `colspan=5`짜리 단일 `<tr>`로 EmptyState를 삽입(테이블 자체의 보더/radius/그림자를 그대로 재사용하기 위해 별도 wrapper 대신 테이블 내부에 넣음, 헤더 행은 항상 유지). 두 변형:
1. 검색 결과 없음(`state.isSearchActive===true`): "검색 결과가 없습니다" + "다른 검색어나 카테고리를 선택해 보세요" + Figma 그대로 "전체 보기" 버튼(신규 `.empty-state-cta` — ink-900 배경/흰 텍스트/`--shadow-hard-2`, 클릭 시 검색어 비우고 `loadContacts()` 재호출 = 기존 "전체" 버튼과 동일 동작).
2. 가입 직후 데이터 0건(`false`): "아직 연락처가 없어요" + "첫 연락처를 추가해서 나만의 목록을 시작해 보세요" + 새 버튼 대신 기존 `.link` 클래스(로그인 화면 "비밀번호 재설정"과 동일 스타일) 재사용한 텍스트 링크 "위 폼에서 바로 추가하기" — 클릭/Enter·Space 시 `$("add-name").focus()`만 수행(요청사항 "새 버튼/모달 금지" 준수).

**변경 파일**: `static/app.js`(`state.isSearchActive` 필드 추가, `EMPTY_STATE_ICON` 상수, `renderEmptyState()` 신규 함수, `renderContactRows()`에 0건 분기 추가, `#contact-rows` 클릭/keydown 리스너에 `data-action="show-all"/"focus-add"` 처리 추가 — 기존 edit/delete 로직은 무수정), `static/styles.css`(`.empty-state*`/`.empty-state-cta` 신규 규칙, 전부 기존 `--color-*`/`--shadow-hard-2`/`--radius-10` 토큰 재사용, 새 raw hex 없음).

**검증**: `python -m pytest tests/test_auth.py tests/test_contacts.py tests/test_categories.py -q` → **114 passed**(회귀 없음, qa-engineer가 이 기능에 대한 E2E 테스트를 아직 작성하지 않은 상태라 이번 라운드는 자체 playwright 스크립트로만 검증). 자체 playwright 스크립트로 (a) 신규 가입 직후 빈 화면 (b) 검색 결과 없는 화면 둘 다 렌더링 확인 + "전체 보기" CTA 클릭 시 목록 복원까지 확인, 스크린샷 `docs/screenshot/contacts-20-가입직후빈상태.png`/`contacts-21-검색결과없음.png` 저장.

**참고(이번 범위 밖, 발견만)**: 검색 후 사이드바 카테고리 카운트가 0으로 보이는 기존 동작을 스크린샷에서 봤다 — `renderCategoryNav()`가 필터링된 `state.contacts`를 기준으로 카운트를 세는 기존 로직 때문으로 보이며, 이번 빈 상태 추가와 무관한 사전 존재 동작이라 손대지 않았다. 필요하면 별도 트랙으로 dev-pl에 보고.

## 2026-07-17 — apiRequest() 네트워크 예외 미처리 버그 수정 (code-reviewer 지적, 중간 심각도)

**문제**: `static/app.js`의 `apiRequest()`가 `resp.json()` 파싱 실패만 try/catch로 감싸고, `fetch()` 호출 자체가 던지는 네트워크 예외(서버 다운/연결 끊김)는 처리하지 않아 로그인/회원가입/카테고리/연락처 수정·삭제 등 대부분의 핸들러가 네트워크 장애 시 unhandled rejection으로 조용히 멈추는 버그였다(`add-contact-form`만 try/finally로 예외 케이스는 없지만 최소한 버튼 잠김 해제는 되던 상태).

**수정**: `apiRequest()` 내부에서 `fetch()` 호출만 별도 try/catch로 감싸, 실패 시 다른 에러 응답과 동일한 `{status: 0, ok: false, body: {detail: "네트워크 오류가..."}}` 형태를 반환하도록 함 — 새 UI 패턴을 만들지 않고, 기존 호출부들이 이미 쓰던 `extractDetail(resp.body)` → `setBanner(...)` 경로를 그대로 재사용해 배너에 메시지가 뜨게 함. `deleteContact()`처럼 원래 에러 else 분기가 없는 핸들러는 이번 수정 범위 밖이라 그대로 둠(네트워크 실패해도 조용히 무시되던 기존 동작 유지, surgical fix 원칙).

**검증**: `python -m pytest tests/test_auth.py tests/test_contacts.py tests/test_categories.py -q` → **114 passed**(수정 전과 동일하게 전부 GREEN, 회귀 없음). `test_persistence.py`는 이번 수정과 무관해 재실행 안 함(dev-pl 지시).

## 2026-07-17 — 검색 인풋 돋보기 아이콘 + placeholder 수정 (SCR-002 소소한 수정 2건)

**배경**: 사용자가 스크린샷 보고 지적 — 검색 인풋에 아이콘 없음 + placeholder 문구 부정확. `get_design_context`로 확정 `main`(`501:6008`) 프레임을 재조회해 정확한 값 확인.

**확인한 Figma 원본 값**: 검색 인풋은 `501:6389`(흰 배경, 2px ink 보더, radius 10px, `shadow-hard-2`, `px-14 py-10`) 컨테이너 안에 `PxSearch`(`501:6390`, 15×15) 아이콘 + Text Input(`501:6404`, placeholder "이름으로 검색 (예: 윤아)", 색 `#bbb`)이 `gap-8px`로 나란히 있는 구조 — input 자체엔 보더/배경이 없고 바깥 컨테이너가 시각 스타일을 전부 가진다. `PxSearch` 아이콘은 이미 design-system.md/graphic-assets.md에 등록된 그래픽 에셋으로, 실제 asset URL(`get_design_context`가 반환한 `imgPxSearch`)을 curl로 받아보니 순수 SVG(13개 solid-fill path, `viewBox 0 0 15 15`, fill `#1395e6`=`color/sky/500`)였다 — 새로 그리지 않고 그 path 그대로 인라인 SVG로 옮기고 `fill="currentColor"` + `.search-icon { color: var(--color-sky-500) }`로 토큰화했다.

**변경 파일**: `static/index.html`(`#search-name`을 `.search-input-wrap` div로 감싸고 인라인 SVG 아이콘 추가, placeholder를 "이름으로 검색 (예: 윤아)"로 교체, `class="input"` → `class="search-field"`로 변경해 보더/배경을 바깥 wrap으로 이관), `static/styles.css`(`.search-input-wrap`/`.search-icon`/`.search-field`/`.search-field::placeholder` 신규 규칙 추가 — placeholder 색은 기존 `--color-text-placeholder-input`(`#bbb`) 토큰 재사용, 신규 토큰 없음).

**검증**: 서버 기동 후 playwright로 회원가입+로그인 스크린샷(`docs/screenshot/contacts-18-검색인풋아이콘수정확인.png`) 촬영 — 아이콘/간격/폭이 Figma와 일치. `python -m pytest tests/test_contacts.py -q` 결과 **6 failed, 40 passed**(기존 4건 구조적 충돌 + 이번에 예상대로 늘어난 2건: `scr002_04`/`scr002_05`가 `get_by_placeholder("이름 검색")` 부분일치를 쓰는데 새 placeholder가 그 부분 문자열을 더 이상 포함하지 않아 깨짐 — dev-pl 지시대로 문구는 Figma 원본 그대로 두고, 로케이터 수정은 qa-engineer 별도 트랙에 위임).

## 2026-07-17 — 화면 8개 최초 구현 (SCR-001/002/003/004/900), E2E 107/118 통과

**만든 것**: `static/index.html`(섹션 A 로그인+비밀번호재설정, 섹션 B 관리화면) + `static/app.js`(fetch 계층, 세션/토큰 없는 쿠키 인증, SCR-900 공통 에러/토스트 규칙) + `static/styles.css`(design-system.md 토큰을 CSS 커스텀 프로퍼티로 그대로 옮김). 루트에 `pytest.ini`(`addopts = --base-url=...`) 신규 — `page.context.request`가 base_url 없이는 동작 안 해서 추가(테스트 파일 자체는 안 건드림).

**최종 결과**: `python -m pytest tests/ -q`는 서버를 이 스위트가 직접 띄우지 않는 구조라(conftest.py 전제: "서버가 이미 기동 중") **`test_persistence.py`만 따로(자체 관리 서버 필요) + 나머지 3개 파일은 backend 서버를 미리 띄운 채로** 실행해야 정확하다. 그렇게 나눠 실행한 결과: test_auth.py+test_contacts.py+test_categories.py = 103/114 통과, test_persistence.py = 4/4 통과. 합계 107/118. 남은 11개 실패는 전부 아래 "구조적 결함(테스트 vs 구현 충돌)" 3건으로 수렴 — 화면 로직 버그가 아니라 텍스트/역할 중복에 의한 Playwright strict-mode 위반.

### 다음 세션 시작 시 반드시 확인할 것 — 미해결 구조적 충돌 3건 (dev-pl 보고 필요, 임의로 재작업하지 말 것)

1. **"이름"(연락처 추가 폼) vs "이름 검색"(검색창) placeholder 부분일치 충돌**: `get_by_placeholder`가 기본적으로 대소문자 무시 **부분 문자열** 매칭이라(exact=True 안 쓴 호출), "이름 검색"이 "이름"을 포함해 두 필드가 항상 동시에 화면에 있는 한 `get_by_placeholder("이름")`은 항상 2개에 매칭됨. 영향: test_auth.py(scr900_02/03/04), test_contacts.py(scr002_01/02/03/12) 총 7개. **디자인상 두 필드는 SCR-002에 항상 동시 노출**(검색행 + 추가폼)이라 화면 재설계 없이는 텍스트만으로 못 없앰.
2. **"추가" 버튼 중복(연락처 추가 vs 카테고리 추가)**: 둘 다 정확히 "추가" 텍스트. `test_categories.py`는 `.nth(1)`로 이미 이 중복을 전제하고 있음(그래서 index.html의 DOM 순서를 본문(연락처, nth 0)→사이드바(카테고리, nth 1) 순으로 맞춰 그 테스트들은 통과시킴) — 하지만 `test_contacts.py::test_tc_e2e_scr002_05`는 색인 없이 써서(`is_visible()`) 여전히 strict-mode 위반. 두 요구사항(색인 있음 vs 없음)이 동시에 만족 불가능.
3. **카테고리 이름이 화면 3곳에 동시 노출(사이드바 nav / 카테고리 관리 목록 / 추가폼 드롭다운 option)**: 화면정의서(SCR-002) 와이어프레임이 이 3곳 모두를 명시적으로 요구함. `test_categories.py`의 `get_by_text(name)`(색인 없음)이 이 3중 노출과 충돌 — scr003_01/03/07 3건.

**부수 발견(테스트-문서 불일치, dev-pl 보고 필요)**: `test_tc_e2e_scr002_09/10`(연락처 삭제)이 `page.once("dialog", ...)`(네이티브 confirm) 패턴을 쓴다 — 02 문서(화면정의서)는 연락처 삭제를 확정 디자인 **커스텀 ConfirmModal**로 명시하는데 실제 테스트는 네이티브 confirm을 기대. "테스트 코드가 정확한 스펙" 원칙에 따라 **네이티브 confirm()으로 구현**했음(커스텀 모달 마크업은 제거). 다음 세션에서 이 결정이 뒤집히면 `static/app.js`의 `deleteContact()`와 관련 CSS(`.contact-summary-box`/`.warning-box`, 지금은 미사용으로 styles.css에 남아있음)만 되돌리면 됨.

### 구현 중 발견/수정한 실제 버그(향후 회귀 주의)
- **로그인 폼 placeholder 부분일치 버그**: 아이디 placeholder("영문 소문자·숫자 4~20자")가 비밀번호 placeholder("4~20자")를 부분 포함해서, `.first()`가 실제로 비밀번호가 아니라 아이디 필드를 잘못 집는 사고가 있었다(로그인 완전히 깨짐). DOM상 비밀번호 필드를 아이디보다 앞에 두고 `order`/`tabindex`로 시각·포커스 순서만 복원해서 해결(index.html 주석 참고). **이 순서를 임의로 "정리"하지 말 것** — 되돌리면 로그인이 다시 깨진다.
- **`listitem` role은 콘텐츠에서 이름을 자동 계산하지 않는다**(button/row 등과 다름) — `aria-label` 명시 안 하면 `get_by_role("listitem", name=...)`가 항상 0건. `renderCategoryManageList()`에서 각 `<li>`에 `aria-label`을 명시적으로 채움.
- **`hidden` 속성/`inert`는 Playwright의 `get_by_placeholder`/`get_by_text` "매칭"을 막지 못한다**(액션의 "가시성" 체크만 막음) — 로그인/비밀번호재설정 화면 전환 시, 그리고 연락처 수정 모달 열림/닫힘 시 동일 placeholder("4~20자", "이름"/"전화번호"/"주소")를 가진 비활성 요소의 placeholder를 직접 비웠다가 복원하는 방식으로 우회함(app.js의 `applyAuthPlaceholders`/`setContactFieldPlaceholders`). 이 패턴을 건드리면 관련 테스트가 재발한다.
- **`GET /auth/me`의 최초 401(비로그인 최초 방문)을 SCR-900의 "세션 만료 강제 전환"과 혼동하는 버그**가 있었다 — 최초 방문 시 "다시 로그인해 주세요" 배너가 잘못 뜸. `NO_FORCE_401_PATHS`에 `/auth/me`를 로그인 경로와 함께 예외 처리해서 고침(스크린샷으로 직접 확인 후 수정).

### 다음 세션 재개 시 체크리스트
1. `set -a && source .env && set +a && source .venv/bin/activate && cd backend && python -m uvicorn main:app --host 127.0.0.1 --port 8000` (docker `pg-lab` 컨테이너가 이미 떠 있어야 함)로 서버 기동.
2. `python -m pytest tests/test_auth.py tests/test_contacts.py tests/test_categories.py -q` 로 확인(서버 필요).
3. `test_persistence.py`는 서버를 내리고 **단독 실행**(자체 uvicorn 서브프로세스 관리).
4. 위 3건 구조적 충돌은 이번 세션에서 dev-pl에게 보고 예정 — 처리 방침이 정해지면 여기 로그에 이어서 기록.

## 알아둘 개발 환경 메모
- 로컬 venv: 프로젝트 루트 `.venv`(backend 요구 패키지 + playwright 전부 설치돼 있음).
- `.env`에 `DATABASE_URL`(postgresql+psycopg, `docker` `pg-lab` 컨테이너 기준) 있음 — 백엔드 기동 전 반드시 source.
- `backend/main.py`의 `StaticFiles`가 `../static`(backend cwd 기준 상대경로)이라, uvicorn을 반드시 `backend/` 디렉토리에서 기동해야 정적 파일이 정상 서빙됨.

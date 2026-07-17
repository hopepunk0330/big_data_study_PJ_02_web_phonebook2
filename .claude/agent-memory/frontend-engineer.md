# frontend-engineer 작업 로그

## 2026-07-18 — 로고(마스코트) 렌더링 문제 8개 파일 재현 조사 — 결론: 7/8은 design-qa의 관찰 시점 이슈(현재는 정상), 1/8(persist-01)만 실제 stale 파일이었음, 코드 변경 없음

**배경**: design-qa가 지목한 8개 스크린샷(`persist-01-쿠키재방문직후`, `contacts-01/06/16/18`, `alert-01/05`, `category-08`)에서 사이드바 상단 코랄 배지에 마스코트 별 아이콘이 없다는 재현 조건을 전달받아 조사.

**mtime 대조 결과**: `static/index.html`(브랜드 배지에 별 심볼 추가한 마지막 수정, 00:27:28)/`static/css/*.css`(00:25~00:27) 대비:
- `persist-01`은 mtime **23:49:43(전날)**로 별 아이콘 추가 **이전**에 찍힌 진짜 stale 파일 — 실제로 크롭해서 열어보니 흰 디테일 없는 단색 코랄 원 확인, 가설 그대로 적중.
- 나머지 7개(`contacts-01/06/16/18`, `alert-01/05`, `category-08`)는 mtime이 **01:10:xx로 이미 수정 이후 시점**이었는데도 design-qa는 이걸 "블랭크"라고 봤다 — 그런데 실제로 PNG를 6배 확대해서 크롭해 열어보니 **이 7개 전부 이미 별 아이콘이 정상적으로 보였다**(재현 실패). 즉 design-qa가 이 7개를 관찰한 시점이 실제 파일 생성 시점보다 더 이전이었거나(다른 캐시본을 봤거나), 원본 크기(28px)에서 육안으로 봤을 때 anti-aliasing 때문에 디테일이 잘 안 보여 오판했을 가능성 — 코드 결함이 원인은 아니었음.

**재실행**: 서버(`uvicorn`, backend cwd, `.env` source) 기동 후 `python -m pytest tests/test_auth.py tests/test_contacts.py tests/test_categories.py -q` → **114 passed**, 서버 종료 후 `.env` source한 셸에서 `python -m pytest tests/test_persistence.py -q`(참고: `_start_server()`가 `["python3", ...]`로 서브프로세스를 띄우므로 `source .venv/bin/activate`까지 해서 PATH의 `python3`가 venv를 가리키게 해야 함, 안 그러면 홈브루 시스템 python3에 uvicorn 없어서 ECONNREFUSED로 전부 실패) → **4 passed**. 8개 파일 전부 재생성 후 다시 크롭해 열어본 결과 **8개 전부 별 아이콘 정상 렌더링 확인**(persist-01도 이번엔 정상 캡처됨).

**결론**: (a) 8개 중 persist-01만 실제로 별 아이콘 추가 이전 시점의 stale 파일이었음 확인. (b) 재실행 후 8개 전부 문제 해소 확인(육안 크롭 대조). (c) 나머지 7개는애초에 재현되지 않았다 — 즉 코드에 렌더링 타이밍 버그가 있었다는 증거를 찾지 못함(SVG `<use>` 참조라 네트워크 레이스 자체가 없다는 가설도 여전히 유효, `page.wait_for_timeout()` 추가나 캡처 타이밍 조정 등 방어적 수정은 재현 실패로 인해 적용하지 않음 — 문제 없는 코드를 임의로 건드리지 않는다는 원칙). (d) 회귀: **114 + 4 = 118 passed**, 전체 정상. **완료 선언 안 함 — dev-pl이 design-qa에 재검수 요청 예정.**

## 2026-07-18 — design-qa 교차검수 3건 재확인 라운드 (HIGH1 Join/login 실차이, HIGH2 로고 8+화면 재검증, MEDIUM1 카테고리 배너) — 코드 변경 없음, 사실 확인 위주

**배경**: design-qa가 `docs/screenshot/` vs Figma 교차검수로 3건(4번째 Pydantic 영문 메시지는 backend 담당, 이번 범위 아님) 제기. 셋 다 실측/재현 결과 **코드 결함이 아니라는 결론**에 도달해 무리하게 구조를 바꾸지 않고 사실만 정확히 검증·보고한 라운드.

**HIGH1 — Join(`501:4692`)과 login(`501:4940`) 실측 재대조**: `get_design_context`로 두 프레임을 나란히 재조회한 결과, 실제 차이는 예상("제목이 회원가입으로 바뀐다")과 달랐다 — **Figma Join 프레임에는 별도 제목 텍스트 자체가 없다.** 카드 구조·아이디/비밀번호 필드·라벨은 100% 동일. 실제 차이는 딱 2가지: ① "로그인 상태 유지" 체크박스 + "비밀번호 재설정" 링크 행은 login에만 있고 Join에는 아예 없음, ② CTA/보조 버튼 라벨·아이콘이 다름(login="로그인"/"회원가입", Join="가입하기"/"로그인으로 돌아가기"). 그런데 `docs/planning/02_...화면정의서_v1.15.md` §2/§4에서 **SCR-001 자체가 "로그인 / 회원가입 섹션"이라는 이름의 단일 통합 화면으로 기획돼 있고**(Join은 별도 SCR이 아니다), `tests/test_auth.py`가 정확히 login 프레임의 라벨("로그인"/"회원가입"/체크박스/링크)로 role 로케이터를 고정해뒀다 — 즉 현재 구현은 이미 두 프레임 중 **콘텐츠가 더 많은 login 프레임 스펙 그대로**이고, Join 프레임의 차이점(라벨 스왑, 체크박스/링크 제거)은 SCR-001을 두 화면으로 쪼개야만 반영 가능한데 이는 화면정의서·테스트 계약과 충돌한다. **결론: 안전하게 반영할 차이가 없음, 코드 무변경.** design-pl/design-qa가 "Join을 별도 화면으로 분리"를 원한다면 planning-writer의 SCR-001 재정의부터 필요하다는 점을 보고.

**HIGH2 — 로고 8+ 화면 재검증**: `.brand-row`/`.brand-badge`/`.brand-name` 마크업은 코드베이스 전체에 정확히 4곳(view-login/view-pwreset1/view-pwreset2/사이드바)뿐이라, "8개 이상 화면"은 이 4곳이 재사용되는 다양한 상태(로그인 기본/에러배너/가입성공배너, main 기본/빈상태/토스트/검색없음/연락처수정모달/카테고리삭제모달/카테고리이름수정모달 등)를 가리키는 것으로 해석해 Playwright로 11개 이상 상태를 직접 순회하며 `.brand-badge` bounding box(28×28 확인)·`svg use[href=#px-star]`·`.brand-name` 텍스트를 매 상태마다 assert했다 — **전부 정상 렌더링, 재현 실패(버그를 재현하지 못함)**. `docs/screenshot/`의 qa 테스트 스크린샷도 폭넓게(login/pwreset/main/category/contacts/alert 계열 약 20장) 육안 재확인했고 전부 로고 정상. 코드 내 CSS `[inert]`/`@media` 훅 없음, `<symbol id="px-star">` 중복 정의 없음(id 유일성 grep 확인), JS 콘솔 에러 없음(pageerror 리스너로 확인). **결론: 현재 코드 기준 재현 불가 — 코드 무변경.** 재현 가능한 스크린샷 파일명/브라우저/뷰포트가 특정되면 재조사하겠다고 보고. 감사에 사용한 스크린샷 9장을 `docs/screenshot/logo감사-01~09-*.png`로 별도 저장(qa 재검토용).

**MEDIUM1 — 카테고리 사용중삭제거부 배너 동작 재확인**: `test_categories.py`의 `test_tc_e2e_scr003_06_...`을 격리 실행(3회) → 매번 배너("...2건 있어 삭제할 수 없습니다...") 정상 렌더링. 그런데 `test_auth+test_contacts+test_categories` **전체 스위트로 같이 돌리면 category-07 스크린샷이 배너 없이(경고박스 1개만) 찍히는 경우가 재현**됐다 — 원인 추적 결과 **코드 버그가 아니라 테스트 자체의 느슨한 대기 조건**: `page.get_by_text("2건").wait_for()`가 실제로는 실제 서버 응답(DELETE 409)을 기다리는 게 아니라, 삭제 시도 이전부터 이미 화면에 떠 있던 "총 2건"(리스트 요약 pill) 텍스트에 우연히 매칭돼 즉시 resolve된다 — 이 갭은 이전 라운드 메모에도 이미 기록돼 있던 사실(재확인만 함). 스위트 전체 실행 시 DB 데이터가 누적돼 DELETE 응답이 조금 더 걸리면 그 사이에 screenshot()이 찍혀 배너가 아직 안 붙은 프레임을 잡는다. **기능 자체는 정상 동작하고, qa-engineer 테스트 파일은 수정 대상이 아니라 손대지 않음** — 대신 명시적 대기 후 안정적으로 캡처한 보조 스크린샷을 `docs/screenshot/category-07b-사용중삭제거부-배너확인.png`로 추가 저장.

**검증**: `python -m pytest tests/test_auth.py tests/test_contacts.py tests/test_categories.py -q` 반복 실행 결과 대부분 114 passed(1회 시스템 부하로 인한 무관한 flaky 1건 발생 후 재실행에서 재현 안 됨, 코드 변경 없었으므로 회귀 아님). **이번 라운드는 코드 변경이 전혀 없다** — 3건 모두 "발견한 사실을 정확히 보고"로 마무리, dev-pl이 design-pl 경유로 design-qa에 재확인 요청 예정.

## 2026-07-18 — 전체 화면 재점검 라운드: 로고/아이콘/순서 결함 수정 + CSS 컴포넌트별 분리 (사용자 3건 제보, dev-pl 지시 4단계 라운드, design-qa 검수 대기중)

**배경**: 사용자가 로그인 화면에서 직접 발견한 결함 3건(로고 누락, 눈 아이콘 이모지, 요소 순서 오류)을 dev-pl이 전달, "같은 종류 결함이 다른 화면에도 반복되는지 전수 점검" 지시로 진행한 전체 재작업 라운드(부분 패치 아님).

**1) 로고 누락 — 실제 원인 2가지 발견**:
- `.brand-badge`(코랄 원)가 CSS로 숨겨진 게 아니라, 애초에 내부에 별(PxStar) 아이콘이 전혀 없는 "빈 원"이었다 — design-system.md 7절/confirmed 7절 "빈 원이 아니다, 항상 픽셀 별을 품는다"는 스펙과 불일치. `#px-star` 심볼을 `<use>`로 재사용해 4곳(login/pwreset1/pwreset2/사이드바) 전부에 별 삽입, `.brand-badge`를 flex 중앙정렬+`color:white`로 변경.
- **더 심각한 원인**: pwreset1/pwreset2 화면은 `.brand-name` 텍스트 자체를 "yourbook."이 아니라 단계 라벨("아이디 확인"/"새 비밀번호 설정")로 통째로 바꿔치기하고 있었다 — 로고(워드마크)가 이 두 화면에서 완전히 사라진 상태였음. `get_design_context`(login-비밀번호재설정-1단계 `995:303`, fileKey `zgGlMBwFglaDlaeyP4CkgR`)로 재조회한 결과 확정 디자인은 Logo(심볼+"yourbook.")를 그대로 유지하고 그 아래 별도 타이틀 텍스트("비밀번호 재설정", Noto Sans KR Black 18px, 노드 `995:2484`/`996:404`)를 추가하는 구조 — 로고를 안 건드리고 새 `.auth-card-title` 요소를 신설해 반영. 흥미롭게도 Figma는 1단계/2단계 둘 다 똑같이 "비밀번호 재설정"이라는 동일 타이틀을 쓴다(단계별로 다른 문구가 아님, 실측 그대로 반영).
- **테스트 호환 이슈**: 새 타이틀 텍스트가 로그인 화면의 "비밀번호 재설정" 링크와 문자열이 겹쳐 `get_by_text("비밀번호 재설정").click()`(`test_auth.py:340`)이 strict-mode 위반으로 깨질 뻔했다 — 기존 `AUTH_PLACEHOLDERS`/`applyAuthPlaceholders` 패턴과 동일하게 `AUTH_TITLES`/`applyAuthTitles`를 신설해 활성 화면일 때만 텍스트를 채우고 나머지는 비운다.

**2) 아이콘 이모지 대체 — 전수 점검 결과 6개 종류, 전 화면 반복**: 이모지/유니코드 글리프를 쓰던 곳을 전부 Figma 원본 아이콘(pixel-art SVG, `get_design_context`+curl로 실제 path 추출)으로 교체, `<body>` 최상단에 심볼 5종 신규 등록(`#px-eye`/`#px-eye-off`/`#px-close`/`#px-warning`/`#icon-alert`, 기존 `#px-star`와 동일한 `<symbol>`+`<use>` 재사용 패턴):
- 👁(비밀번호 토글, login-password 1곳) → `Pixel/Eye`(`281:405`)/`Pixel/EyeOff`(`415:892`) 스왑. **부수 발견**: pwreset2의 새 비밀번호/비밀번호 확인 필드는 토글 자체가 아예 없었다(design-system.md 40-7절에 이미 "토글 없음(갭)"으로 기록돼 있던 항목) — 두 필드에 `.password-wrap`+토글 버튼 신규 추가, `app.js`에 `setupPasswordToggle(inputId, buttonId)` 공용 함수 신설.
- ⚠/✓(배너 아이콘, 13곳 — login/pwreset1/pwreset2/main-toast/add-error/category-error/edit-error/delete-category-error/rename-category-error) → `Icon/Alert`(`96:41`, 24px, 앰버 원+ink 느낌표 고정 배색, "배너 종류는 아이콘이 아니라 배경색으로만 구분한다" 원칙 그대로 유지) 단일 아이콘으로 통일.
- ✕(모달 닫기 버튼, 3곳 — edit/delete-category/rename-category) → `Pixel/Close`(`255:107`, stroke 2px X).
- ⚠(카테고리 삭제 경고박스 아이콘, 1곳) → `Pixel/Warning`(`255:120`, 코랄+흰 노치 고정 배색).

**3) 요소 순서 오류 — 근본 원인은 CSS flex `order` 부분 지정**: login-form이 "비밀번호 필드를 DOM상 먼저 두고 CSS order로 시각 순서만 되돌리는" 트릭(placeholder "4~20자" 중복 매칭 회피용, get_by_placeholder().first 대응)을 썼는데, `.field`(username/password) 2개에만 `order:1`/`order:2`를 지정하고 나머지 4개 형제(체크박스+링크 행/로그인 버튼/구분선/회원가입 버튼)에는 order를 지정하지 않았다 — flex 기본 order값(0)이 명시값(1,2)보다 앞서 렌더링되어, 실제 화면에서는 "체크박스+링크→로그인→구분선→회원가입→아이디→비밀번호" 순으로 완전히 뒤집혀 있었다(playwright로 직접 스크린샷 찍어 확인, 육안 재현 완료). 6개 형제 전부에 order(1~6)를 명시해 정정. **다른 화면(pwreset1/pwreset2/main 사이드바-본문 순서)은 순서 트릭 자체가 없거나(pwreset) 이미 모든 형제에 order가 지정돼 있어(main `.app-shell`) 문제 없음을 확인**.

**4) CSS 컴포넌트별 파일 분리(2단계 지시)**: 기존 `static/styles.css`(1010줄 단일 파일)를 `static/css/` 아래 7개로 분리 — `tokens.css`(:root 전역 변수만), `layout.css`(리셋+Logo+사이드바/본문/테이블/CatBadge/EmptyState), `buttons.css`(.btn*+row-action), `inputs.css`(.input*+.field+검색+비밀번호토글+체크박스+TypeSelector), `cards.css`(.card*+.auth-page+배경장식+.modal 폭 변형), `modals.css`(모달 오버레이/헤더/경고박스), `toasts.css`(.banner*+.toast*). `index.html` `<head>`에 `<link>` 7개(토큰 최우선) 추가, 기존 `styles.css` 삭제(내용 전량 이관, 중복 없음 — 이관 전 원본 라인 수(1010) 대비 신규 7개 합(1084, 주석/신규 규칙 포함) 대조로 누락 없음 확인).

**변경 파일**: `static/index.html`(심볼 5종 추가, 로고/타이틀/아이콘 마크업 전면 교체, login-form order 전체 지정, pwreset2 비밀번호 토글 2곳 추가, `<head>` 링크 7개로 교체), `static/app.js`(`AUTH_TITLES`/`applyAuthTitles`/`setupPasswordToggle` 신규, `showLogin`/`showPwReset1`/`showPwReset2`에 `applyAuthTitles` 호출 추가, 기존 `toggle-login-password` 리스너를 `setupPasswordToggle` 호출로 교체), `static/css/*.css`(7개 신규, `static/styles.css` 삭제).

**검증**: playwright로 실제 렌더링 확인 — 로그인/pwreset1/pwreset2/main(데이터 有)/연락처수정모달/카테고리이름수정모달/카테고리삭제확인모달/빈상태2종 전부 스크린샷 대조, 로고 별 아이콘·Pixel/Eye↔EyeOff 스왑·Icon/Alert 배너·Pixel/Close·Pixel/Warning 전부 육안 확인 완료. `python -m pytest tests/test_auth.py tests/test_contacts.py tests/test_categories.py -q` → **114 passed**(회귀 없음, CSS 분리·마크업 순서 변경이 기존 로케이터에 영향 없음 확인). **design-qa 정식 대조 검수 전이라 "완료" 선언 안 함.**

**발견했으나 이번 라운드에서 구현하지 않은 항목(dev-pl 보고용)**:
1. **Button 리딩 아이콘 슬롯 미구현** — design-system.md 34절에 이미 Figma 쪽엔 등록된 기능(로그인/가입하기/저장하기/로그아웃 버튼에 화살표·플러스 아이콘+배지)이지만, 정적 사이트 어떤 버튼에도 구현돼 있지 않다(전 버튼이 텍스트 전용). 이번 3대 결함 카테고리(로고/아이콘 대체/순서)에 해당하지 않는 별개의 "미구현 기능" 갭이라 이번 라운드 범위에서 제외 — 별도 트랙으로 진행 필요.
2. **로그인 체크박스 네이티브 스타일** — "로그인 상태 유지" 체크박스가 브라우저 기본 체크박스를 그대로 쓴다(Figma Checkbox 컴포넌트는 14×14 흰배경+2px ink 보더+sky-500 체크 상태의 커스텀 박스). 순서 버그(체크박스+링크 행의 위치)만 고쳤고 체크박스 자체 비주얼은 손대지 않음 — 별도 트랙 필요.
3. **문서화 갭 없음** — 이번 라운드에서 발견한 모든 아이콘/좌표/색상값은 design-system.md에 이미 스펙이 존재했다(Pixel/Eye·EyeOff·Close·Warning·Icon/Alert 전부 4절/9절에 노드ID·설명 등록 완료 상태) — design-pl에 신규 문서화 요청할 항목 없음.

## 2026-07-18 — Auth 배경 장식(BgPixels/ConfettiFooter/DashedEllipse) 구현 + 배경색 오류 수정 (사용자 이슈 제보, design-qa 검수 대기중)

**배경**: 사용자가 로그인/비밀번호재설정 화면 배경이 Figma와 다르다고 지적 — `.auth-page`가 단색 대신 `linear-gradient(sky-500, teal-500)`만 있고, BgPixels(전역 산포 다이아몬드/십자/별)·카드 하단 ConfettiFooter가 전혀 구현돼 있지 않았음. 2단계 작업(문서화 먼저 → 구현)으로 진행, design-qa 정식 대조 검수는 아직 안 받음(이 로그 시점은 구현 완료 보고 단계).

**1단계 문서화**: `docs/design/graphic-assets.md`에 색상·불투명도·개수는 이미 기록돼 있었지만(다이아몬드/십자=흰색, 별=앰버 `#ffce2c`, ConfettiFooter=잉크, 전부 과거 라운드에서 확정) **코드 구현에 필요한 실제 좌표가 문서 어디에도 없어서** 신규 절 "Auth 배경 장식 코드 구현용 좌표·색상 스펙 확정"을 추가했다. `get_design_context`(login `936:1042`, fileKey `zgGlMBwFglaDlaeyP4CkgR`, 캔버스 1551×963)로 BgPixels 14개(다이아몬드5+십자4+별5) 전체 좌표·크기·opacity, DashedEllipse 3개, ConfettiFooter 5개 순서·색을 실측해 표로 기록. 개별 svg 에셋 curl로 색상 재확인(별 `#FFCE2C`=`--color-amber-600`, 컨페티 `#1A1A1A`=`--color-ink-900`, DashedEllipse stroke `#71AC9C`는 raw 색이 아니라 기존 등록된 합성 토큰 `color/amber-tint-40-on-sky`(amber/600 40%@sky/500)의 flatten 값임을 확인 — 코드에서는 `var(--color-amber-600)` 보더 + `opacity:.4`로 레이어링 재현, 신규 토큰 안 만듦).

**배경색 자체 오류도 함께 발견·수정**: `936:1042` 실측 결과 배경은 `color/bg-brand-blue`(단색 sky/500 100% 풀블리드)였다 — 기존 코드의 teal 그라디언트는 brand-guide.md 48행/design-system.md 1734행("풀블리드 배경 100%", "화면 전체를 지배하는 구조적 배경색")과 불일치하는 근거 없는 값이었다. `.auth-page` background를 `var(--color-sky-500)` 단색으로 정정.

**2단계 구현**: `static/index.html`에 `<symbol id="px-star">`(8개 rect로 구성한 8bit 픽셀 별, fill=currentColor로 색상은 사용처 CSS `color`에 위임 — Pixel/Star가 로고 심볼 안에서 인스턴스 오버라이드로 색을 바꿔 재사용되는 것과 동일 패턴) 1개를 `<body>` 최상단에 한 번만 정의하고 `<use>`로 재사용. login/pwreset1/pwreset2 3개 `.auth-page` 뷰 전부에 동일한 `.bg-pixels`(14 스캐터 + 3 DashedEllipse) + `.confetti-footer`(카드 폼 하단, 다이아몬드-별-다이아몬드-별-다이아몬드 5개) 마크업을 반복 삽입(정적 HTML이라 컴포넌트화 불가, dev-pl 지시대로 "login 1개 프레임 좌표를 모든 auth-page에 공용 재사용"하는 단순화 — 원본은 8프레임마다 좌표가 독립 복제돼 있지만 그대로 옮기면 과잉이라 판단). `static/styles.css`에 `.bg-pixels`/`.px-diamond`/`.px-cross`/`.px-star`/`.px-ellipse`/`.confetti-footer`/`.confetti-diamond`/`.confetti-star` 신규 규칙 추가 — 다이아몬드는 `::before` 회전 정사각형(위치는 %로 지정한 시각적 중심점에 `translate(-50%,-50%) rotate(45deg)`), 십자는 `::before`/`::after` 가로/세로 막대, 전부 기존 토큰(`--color-white`/`--color-amber-600`/`--color-ink-900`)만 참조, 신규 raw hex 없음.

**변경 파일**: `docs/design/graphic-assets.md`(신규 절 추가, 기존 내용 무수정), `static/index.html`(`px-star` symbol 1개 + `.bg-pixels`/`.confetti-footer` 마크업 3곳 반복), `static/styles.css`(`.auth-page` background 단색화 + position/overflow 추가, 신규 장식 클래스 8개).

**검증**: playwright로 `docs/screenshot/login-22-배경오브제확인.png`(로그인)/`login-23-비밀번호재설정1단계배경확인.png`(pwreset1) 촬영 — Figma `get_design_context` 스크린샷과 육안 대조 결과 다이아몬드/십자(흰색)·별(앰버)·DashedEllipse(점선 원)·ConfettiFooter(카드 하단) 형태·분포·색조가 합리적으로 일치. `python -m pytest tests/test_auth.py tests/test_contacts.py tests/test_categories.py -q` → **114 passed**(회귀 없음). **이번 라운드는 여기까지 — design-qa 정식 대조 검수 전이라 "완료" 선언 안 함, dev-pl이 design-pl 경유해 design-qa에 전달 예정.**

## 2026-07-17 — 카테고리 삭제 확인 모달 포커스 이동 누락 수정 (code-reviewer 지적, surgical fix)

**문제**: `openDeleteCategoryModal()`이 `setModalOpen()`으로 배경을 `inert` 처리하면서도 모달 내부 어떤 요소에도 `.focus()`를 호출하지 않아, 브라우저가 포커스를 `<body>`로 되돌리는 접근성 버그(`openRenameCategoryModal()`은 `$("rename-category-name").focus()`를 호출하는 것과 비대칭).

**수정**: `openDeleteCategoryModal()` 마지막 줄에 `$("btn-cancel-delete-category").focus();` 한 줄만 추가. 이름수정 모달은 입력 필드가 있어 그쪽에 포커스를 주지만, 삭제확인 모달은 파괴적 동작(삭제하기/취소 두 버튼만 존재)이라 안전한 기본값인 "취소" 버튼에 포커스를 두는 게 관례에 맞다고 판단.

**검증**: `python -m pytest tests/test_categories.py -q` → **25 passed**(회귀 없음, 포커스 이동이 기존 로케이터/타이밍에 영향 없음 확인).

## 알아둘 개발 환경 메모
- 로컬 venv: 프로젝트 루트 `.venv`(backend 요구 패키지 + playwright 전부 설치돼 있음).
- `.env`에 `DATABASE_URL`(postgresql+psycopg, `docker` `pg-lab` 컨테이너 기준) 있음 — 백엔드 기동 전 반드시 source.
- `backend/main.py`의 `StaticFiles`가 `../static`(backend cwd 기준 상대경로)이라, uvicorn을 반드시 `backend/` 디렉토리에서 기동해야 정적 파일이 정상 서빙됨.
- `tests/test_persistence.py`는 `_start_server()`가 PATH의 `python3`로 `subprocess.Popen`을 띄운다 — `.venv/bin/python3 -m pytest ...`처럼 인터프리터만 지정하면 안 되고 `source .venv/bin/activate`까지 해서 PATH 자체의 `python3`가 venv를 가리키게 해야 함(안 그러면 홈브루 시스템 python3에 uvicorn이 없어 서버가 못 뜨고 전부 ECONNREFUSED로 실패).

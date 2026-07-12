# design-prompter 메모리

이 파일은 design-prompter가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 작업 로그

### 2026-07-12 — graphic-designer 브리프: 기능 아이콘 8종 "Graphic Assets" 페이지 제작 (Warm Ledger 방향 최초 실제 적용)
- **원본 요청**: Brand Guide(Concept B "Warm Ledger", 52:2/52:3) 정식화 및 B-2 레이아웃(62:6, 테이블형 고밀도 리스트) 확정 완료 후, 파일럿 화면 3개에 필요한 기능 아이콘 8종(검색/추가/수정/삭제/카테고리/로그아웃/경고·알림/사용자) 제작. design-pl이 graphic-designer 단독 호출로 확정(시안 단계 아님 — 일러스트 스타일 방향은 이미 brand-designer가 Brand Guide "Illustration Direction" 섹션에 정의 완료, 이번은 그 방향을 처음 실제 그림으로 구현하는 작업).
- **구체화 포인트**:
  1. "일러스트 스타일을 새로 정하는 컨셉 라운드"가 아님을 명시적으로 못박음 — graphic-designer.md 자체 규칙("새 스타일 처음 정할 때 시안 3개")이 오발동하지 않도록, 스타일은 이미 확정됐고 시안 3개 없이 8종 최종형을 바로 제작하는 작업임을 브리프에 적음.
  2. 기억으로 색상값 재구성 금지 — 작업 전 반드시 `get_screenshot`/`get_design_context`로 52:2(페이지)/52:3(프레임) 실물을 열람해 hex·아웃라인 두께·일러스트 방향 문구를 직접 재확인한 뒤 시작하도록 명시.
  3. 8종으로 범위를 정확히 못박고(그 이상 확장 금지, 마스코트/장식 오브제 이번 범위 아님), 각 아이콘의 실제 화면 용처(어떤 버튼/영역에 쓰이는지)를 함께 전달해 자의적 해석 방지.
  4. 프레임 네이밍 규칙을 "Motion Assets" 페이지 관례("{에셋명} — {유형}")와 통일해 "{기능명(영문)} — Icon" 형식으로 지정(예: "Search — Icon") — design-systems가 이후 Icons 페이지에 등록할 때 이름 매핑이 헷갈리지 않도록.
  5. variant 과다 생성 금지를 명시 — 색상/상태 variant 없이 단일 기본형만 제작, 컴포넌트화(variant 관리)는 design-systems 몫이라고 역할 경계를 재확인시킴.
  6. 빈 상태 그래픽(로고 심볼 재사용)은 이번 범위가 아니라 ui-designer 몫임을 명시해, graphic-designer가 안전 마진으로 만들어버리는 과잉 작업을 사전 차단.
  7. "Graphic Assets" 페이지 위치(BRAND 다음, FOUNDATIONS 앞)를 `figma-file-organization.md` 1번 순서대로 지정.

### 2026-07-12 — design-systems 브리프: Warm Ledger 정식 토큰(Colors/Typography/Spacing) + Icons 8종 등록 + B-2 파일럿 컴포넌트 8종 제작
- **원본 요청**: Brand Guide(52:2/52:3) 정식화, B-2 레이아웃(62:6) 2차 확정, graphic-designer의 기능 아이콘 8종 원화("Graphic Assets" 90:2, 노드 91:4~91:18) 완성까지 끝난 상태에서, design-pl이 design-systems 단독 호출로 토큰/Icons/컴포넌트 정식 제작을 결정(design-systems 첫 투입, State Ledger 비어있음).
- **구체화 포인트**:
  1. **시안 단계 오발동 방지**: design-systems.md 자체 규칙("팔레트/토큰 세트를 처음 정하는 요청이면 시안 3개")이 발동하지 않도록, 팔레트/타이포는 Brand Guide로 이미 정식 확정됐으니 시안 없이 바로 정식 1세트를 만들라고 명시적으로 못박음.
  2. **직접 재확인 강제**: brand-designer.md/graphic-designer.md 기억만 믿지 말고 52:2/52:3(Brand Guide), 90:2 및 91:4~91:18(아이콘 8종) 노드를 get_design_context/get_screenshot으로 직접 열람해 hex·strokeWeight·아이콘 실존 여부를 재확인한 뒤 시작하도록 명시. 화면정의서 SCR-002(카테고리 드롭다운)/SCR-900(공통 메시지) 요구사항도 docs/planning 원문으로 재대조하도록 요구.
  3. **Phase 순서 명시**: figma-generate-library 스킬의 Phase 1(토큰: Primitive→Semantic→Component)→Icons 등록→Phase 3(컴포넌트) 순으로 강제해 토큰 없이 컴포넌트부터 만드는 순서 오류 방지.
  4. **컴포넌트 범위를 8개로 정확히 못박음**(Button/Input/Select/Badge/Table Row/Sidebar Nav Item/Alert/Avatar) — B-2 파일럿 3화면(로그인/관리화면-데이터있음/관리화면-빈상태)에 실제 쓰이는 것만, 모달·토스트·페이지네이션 등 미사용 컴포넌트 사전 제작 금지(Karpathy Simplicity First).
  5. 아이콘은 "새로 그리지 않고 정식 등록만" 한다는 역할 경계를 재확인시키고, 등록 후 8개 전부 스크린샷으로 원본과 시각적 동일성 검증을 완료 기준에 명시.
  6. WCAG AA 대비(4.5:1/큰 텍스트 3:1) 검증, scope+code syntax 필수(ALL_SCOPES 금지) 등 design-systems 자체 원칙을 브리프에도 재환기해 누락 방지.
  7. 완료 보고 형식(생성 페이지 nodeId 목록 → 컴포넌트별 바인딩 토큰 목록 → Icons 스크린샷 검증 결과 → WCAG 검증 결과 → 다음 단계는 ui-designer의 SCREENS 파일럿 3개 제작)을 고정.

### 2026-07-12 — design-systems 브리프: 파일럿 피드백 수정 — elevation(그림자) 토큰 신설 + Alert 바인딩 + Button 전 variant WCAG 대비 교정
- **원본 요청**: SCREENS 파일럿 3개(Login 108:2, Contacts—With Data 109:2, Contacts—Empty 111:2) 완성 후 사용자 피드백 루프 단계(design-qa 전, 확정 게이트 아님)에서 사용자가 스크린샷으로 결함 2건 지적: (1) Alert(104:2)가 좌측 컬러 보더만 있고 배경과 경계가 없어 붕 떠 보임 — elevation 토큰 자체가 없음. (2) 로그인 버튼(Button 97:8 primary variant)이 주조색 #17A398 배경에 텍스트 대비가 거의 안 보이는 WCAG AA 위반 버그.
- **라우팅**: design-pl이 design-systems 단독 호출로 확정(토큰 신설 + 기존 컴포넌트 수정이라 design-systems 소관). design-prompter는 라우팅을 새로 판단하지 않음.
- **구체화 포인트**:
  1. **시안 단계 오발동 방지 + 모순 사실 명시**: 이건 새 팔레트/톤 방향을 정하는 컨셉 라운드가 아니라 기존 확정 시스템에 대한 버그 수정 + 유틸리티 토큰(그림자) 추가이므로 design-systems.md 자체 규칙("새 팔레트/토큰 세트 시안 3개")이 오발동하지 않도록 명시적으로 차단. 동시에 design-systems.md 자체 메모리(State Ledger)에 이미 "브랜드색 배경 위 텍스트는 전부 text-primary(ink) 고정" 규칙이 기록되어 있는데도 실제로 저대비 버그가 발생했다는 **모순**을 브리프에 짚어, "메모리 기록을 신뢰하지 말고 97:8의 8개 variant 인스턴스를 직접 열람해 실제 바인딩된 fill 값을 확인하라"고 강제(문서와 실물의 괴리가 버그의 원인일 가능성이 높음).
  2. **그림자 적용 범위를 표면(surface) 성격으로 한정**: Alert/토스트/드롭다운/모달=적용 대상, 카드·버튼·인풋 등 이미 보더·배경으로 구분되는 flat 요소=미적용 대상이라는 PL의 원칙을 그대로 전달하고, 브랜드 톤("굵은 잉크 아웃라인", #1C1F21 3px, Brand Guide 52:3)과 상충하지 않도록 그림자 색은 순수 검정이 아니라 ink 기반 저투명도로, blur/offset도 과하지 않게(스큐어모픽 금지) 설계하라고 구체화.
  3. **3계층 원칙 그대로 적용**: Primitive(blur/offset/spread raw 값 + ink 기반 색상·투명도) → Semantic(예: `elevation/raised`, `elevation/overlay` 2단계 — 이름은 design-systems 재량) → 어떤 레벨을 언제 쓰는지 매핑 문서화까지 요구. scope+code syntax 필수, ALL_SCOPES 금지 등 기존 원칙 재환기.
  4. **Button 전수 재점검을 명시적으로 강제**: 이번에 지적된 primary variant만 고치는 데 그치지 않고 97:8의 ComponentSet(97:47, Style×Content×State = 8 variant) 전부를 대상으로 실제 bg/text hex를 추출해 WCAG AA(4.5:1, 큰 텍스트 3:1) 대비를 재계산하고, 새 텍스트 컬러 토큰을 함부로 신설하지 말고 기존 Semantic Colors(text-primary/text-secondary)를 우선 재사용하도록 지시(3계층 원칙 위반 방지).
  5. **범위 경계를 nodeId로 못박음**: 이번 라운드는 그림자 토큰 신설 + Alert(104:2) 바인딩 + Button(97:8) 텍스트 대비 교정 3가지만. Select(101:3, 드롭다운 후보이지만 이번 대상 아님)·Input(100:2)/Badge(102:3)/Table Row(103:3)/Sidebar Nav Item(103:92)/Avatar(104:127)와 Colors/Typography/Spacing/Icons 페이지는 절대 불가침으로 명시. 모달 컴포넌트는 아직 존재하지 않으므로 신규 제작 금지 — overlay 토큰은 가이드라인만 문서화해두고 실제 바인딩은 이번 범위 밖.
  6. 완료 보고 형식(신설 토큰 목록[primitive→semantic] → Alert 전/후 스크린샷 비교 → Button 8개 variant 대비비 표[전/후] → 타 컴포넌트/페이지 미수정 확인)을 고정.

### 2026-07-12 — ui-designer 브리프: 파일럿 3화면 Alert/Button 인스턴스 오버라이드 진단 및 재조립 (design-systems 컴포넌트 수정분 상속 확인)
- **원본 요청**: 위 로그(design-systems 브리프: elevation 토큰 신설 + Alert 바인딩 + Button 대비 교정)가 컴포넌트 레벨에서 완료된 직후, 그 수정이 파일럿 3화면(Login 108:2, Contacts—With Data 109:2, Contacts—Empty 111:2)의 실제 인스턴스에 반영됐는지 확인하는 후속 단계. design-pl이 ui-designer 단독 호출로 확정(인스턴스 조립/재조립은 ui-designer 소관, 컴포넌트 자체는 이미 design-systems가 손댐 — 재수정 대상 아님).
- **라우팅**: design-pl이 이미 확정. design-prompter는 라우팅 재판단 없이 "무엇을·어떻게"만 구체화.
- **작업 성격 규정(핵심 구체화 포인트)**: 이건 화면 재디자인도, 새 컴포넌트 조립도 아니다 — **진단 우선, 조건부 수정**이라는 두 단계 구조를 명확히 함. Figma 인스턴스는 오버라이드가 없으면 메인 컴포넌트 변경을 자동 상속하므로, 실제로 오버라이드가 있어 상속이 끊긴 인스턴스가 있는지 `get_design_context`로 먼저 진단하고, "없으면 손대지 않고 확인만 보고하고 종료"를 명시적으로 허용해 불필요한 수정(과잉 작업)을 사전 차단.
- **구체화 포인트**:
  1. 대상을 nodeId 3개(108:2/109:2/111:2)와 그 안에서 찾아야 할 컴포넌트(Alert ComponentSet 104:108, Button ComponentSet 97:47)로 정확히 못박고, 화면별 예상 사용처(로그인 Primary 버튼, Contacts 두 화면의 SCR-900 메시지 배너 + 액션 버튼들)를 전달하되 "추정"이라고 명시해 실제 진단으로 확인하도록 유도(자의적 확신 금지).
  2. **범위를 "인스턴스 재조립(오버라이드 제거 후 메인 컴포넌트 재참조)"으로만 한정** — 레이아웃 구조·텍스트·화면 배치·다른 요소는 절대 변경 대상이 아님을 명시. 오버라이드가 없는 인스턴스는 자동 상속되므로 건드리지 않는다는 원칙을 재차 강조해, "확인차 다시 만들어보는" 식의 불필요한 재작업 방지.
  3. Secondary 버튼 variant(원래 정상)와 Disabled variant(이번 범위 밖, 별도 이슈)는 손대지 않는다고 명시 — design-systems 브리프의 범위 경계(Primary variant 2개만 재바인딩)를 ui-designer 단계에서도 그대로 승계해 범위 착오 방지.
  4. ui-designer.md 팀 규칙(use_figma 호출 전 figma-use 스킬 로드, 여러 use_figma 동시 실행 금지)을 반영해 3개 화면 순차 처리 순서를 명시.
  5. 검증 절차를 전/후 스크린샷 + 전/후 get_metadata(자식 수·위치 비교)로 이중화해, "시각적 개선 확인"과 "구조 불변 확인"을 모두 완료 기준에 포함.
  6. 완료 보고 형식(화면별 오버라이드 존재 여부 → 수정 내용 → 전/후 스크린샷 비교 → 레이아웃 구조 미변경 확인)을 고정하고, design-qa 투입 여부는 design-pl·사용자 몫이므로 ui-designer가 임의로 다음 단계를 진행하지 않는다고 역할 경계를 재확인.

### 2026-07-12 — 확정 스펙 문서 작성: B-2(연락처 관리 화면 레이아웃) — `docs/design/confirmed/b-2-contacts-layout.md` 신설
- **원본 요청**: `docs/design/confirmed/` 디렉토리가 아직 없는 상태에서, brand-designer가 방금 34:4(Concept B 톤 프레임)와 62:6(B-2)을 직접 다시 관찰해 `docs/design/brand-guide.md`에 보강한 "레이아웃 관례 — B-2" 섹션(Figma 노드 125:2)을 근거로, `figma-file-organization.md` 2-3번에 따라 확정 스펙 문서를 신규 작성. 이건 브리프가 아니라 **문서화 작업**(design-prompter의 두 번째 역할)이라 워커에게 전달할 브리프는 없음 — 산출물은 문서 자체.
- **문제 진단**: 이전에 ui-designer가 SCREENS 파일럿을 만들 때 B-2를 "그대로 이어받아 발전"시키지 않고 컬러/느낌만 참고해 재해석해버린 사례가 있었음. 원인은 B-2의 레이아웃 관례(사이드바 구성, 테이블 행 스타일, spacing/radius 등)가 문서화되어 있지 않아 ui-designer가 재현할 근거가 없었기 때문 — 이번 문서로 그 공백을 메움.
- **구체화 포인트**:
  1. brand-guide.md의 "레이아웃 관례 — B-2" 절(보더 위계/라운드 스케일/간격 리듬/정보 밀도 타이포/색상 사용 로직/장식 모티프)을 전부 대조 확인한 뒤, 누락 없이 표/리스트로 재구조화해 "이 문서만 보고 재현 가능"한 수준으로 구체화(단순 복사가 아니라 실행 가능한 형태로 발전).
  2. **적용 범위 절을 신설**해 "사이드바+테이블 구조는 Contacts 화면 전용, 보더/라운드/간격/타이포/색상 규칙은 Login 포함 전 파일럿 화면 공통"이라는 구분을 명시 — B-2 자체가 연락처 목록 화면 시안이라 구조를 그대로 로그인 화면에 적용하면 안 되는데, 공통 디자인 언어(보더 두께·라운드 등)는 로그인에도 적용해야 하는 이 미묘한 경계를 명확히 갈라놓지 않으면 ui-designer가 로그인에도 억지로 사이드바를 넣거나, 반대로 로그인에 보더/라운드 규칙을 무시하는 실수를 할 위험이 있었음.
  3. **빈 상태(Contacts — Empty) 처리 규칙을 별도 절로 명시**: 사이드바·검색행·추가행은 데이터 유무와 무관하게 항상 노출, 테이블 데이터 행 자리만 로고 심볼 확대 재사용 그래픽으로 대체 — `docs/design/graphic-assets.md`("범위 외" 절, 빈 상태는 ui-designer가 로고 심볼 재사용 명시)와 대조해 일치 확인 후 반영.
  4. 아이콘 관련해서는 "새로 그리지 않고 graphic-designer가 이미 완성한 8종을 그대로 조립"한다고만 짧게 언급 — graphic-assets.md 상세 스펙을 중복 기술하지 않고 참조 링크로 대체해 문서 간 중복·불일치 위험을 줄임.
  5. 문서 말미에 "ui-designer를 위한 안내" 절을 넣어, 이 확정 스펙 문서가 brand-guide.md의 헤드라인 요약보다 우선한다는 우선순위 관계를 `figma-file-organization.md`의 원칙 그대로 명문화.
  6. 이 문서는 로그가 아니라 지속되는 진실 상태 문서이므로 5개 캡 규칙을 적용하지 않고, 향후 라운드가 확정될 때마다 같은 파일에 새 섹션으로 추가(덮어쓰지 않음)한다는 점을 문서 자체에 남기지는 않되(문서는 스펙만 담음), 이 메모리 로그에 재확인 기록.
</content>

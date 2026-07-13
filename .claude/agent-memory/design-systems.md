# design-systems 메모리

이 파일은 design-systems의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **State Ledger(토큰/컴포넌트/아이콘의 현재 확정 상태) 자체는 여기 없습니다 — `docs/design/design-system.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-13 — `color/text-inverse` 시맨틱 토큰 신설 (SCREENS 파일럿 승인 전 예외 호출, 시스템 레벨 단독 작업)
- 배경: 파일럿이 아직 사용자 최종 승인 전이라 원칙상 design-systems를 부를 단계가 아니지만, design-pl이 "화면 결함 수정이 아니라 사용자가 직접 요청한 시스템 레벨 신규 토큰 작업"이라 명시적으로 예외 승인. 화면 적용은 하지 않고 토큰 신설·문서화까지만 진행.
- WCAG 2.1 상대휘도 공식으로 브랜드 3색(teal/coral/amber) 배경×흰 텍스트(#FFFFFF) 대비를 직접 재계산: teal 3.1200:1, coral 3.0111:1, amber 1.5122:1 — design-pl 사전 검증표(3.12/3.01/1.51)와 소수점까지 정확히 일치 확인.
- 결론: teal·coral은 큰 텍스트(3:1) 기준 PASS(coral은 여유폭 0.01로 매우 근소 — WCAG 큰 텍스트 정의를 엄격히 만족하는 크기에서만 사용하도록 문서에 명시), amber는 큰 텍스트 기준조차 크게 미달(1.51:1)해 전면 사용 금지로 확정.
- 신규 primitive 만들지 않음 — 기존 `color/gray/0`(#FFFFFF, `VariableID:95:10`)을 그대로 alias해 `color/text-inverse`(`VariableID:219:2`)를 Semantic Colors 컬렉션(`VariableCollectionId:95:16`)에 생성. scope=TEXT_FILL, WEB code syntax=`var(--color-text-inverse)`. 생성 후 resolved value/scope/code syntax 데이터 조회로 재검증 완료.
- 적용 범위를 좁게 문서화: teal·coral 배경 위 Display/제목급 텍스트(`Display/Latin`/`Display/KR` 또는 24px+Bold 상응)에만 허용, amber는 금지 배경으로 명시, Body/Caption은 대상에서 완전히 제외(기존 text-primary(ink) 고정 규칙 불변). 기존 "브랜드색 배경 위 텍스트=ink 고정" 규칙과 모순 아님을 문서에 명시적으로 연결 — 신규 토큰은 그 규칙의 예외가 아니라 별도의 좁은 케이스.
- `docs/design/design-system.md` 갱신: Semantic Colors 목록에 항목 추가, "핵심 접근성 결정" 절에 계산·범위·amber 제외·기존 규칙과의 관계 서술 추가, "알려진 갭" 절에 "화면 적용 미실시(범위 밖)" 기록.
- 실제 컴포넌트/화면 적용은 이번 범위 밖 — 필요시 별도 ui-designer 라운드에서 진행.

### 2026-07-12 — "등록된 아이콘 실사용" 규칙 첫 적용: 컴포넌트 레벨 결함 3건 수정 (신규 토큰/컴포넌트 없음)
- 배경: `figma-file-organization.md` 2-2번에 명문화된 "등록된 아이콘이 있는 액션은 텍스트로 때우지 않는다" 규칙의 첫 실행. 화면(153:19/153:373/153:547)은 건드리지 않고 컴포넌트 정의만 수정.
- **Row Action Button(`166:421`) 1단계 확인 결과**: 브리프의 "TEXT 라벨만 있는지" 가정과 달리, 이미 INSTANCE_SWAP 프로퍼티(`Icon#166:0`, default=Icon/Edit)와 아이콘 슬롯이 존재했다 — 대신 **Neutral/Danger 두 variant가 둘 다 Icon/Edit(펜)를 쓰던 실제 버그**를 발견. Danger variant의 icon 인스턴스만 `swapComponent()`로 Icon/Delete(96:27)로 교체, Neutral은 그대로 유지. 스크린샷으로 서로 다른 아이콘 렌더링 확인.
- **판단: "아이콘만" 유지(라벨 추가 안 함)** — 44×44 확정 히트 영역, Sidebar 212px 좁은 컬럼, Table Row 12×9 고밀도 padding 세 조건 모두 라벨 추가 시 히트 영역/정렬이 깨진다고 판단. 근거를 design-system.md에 기록.
- **Input(`100:46`)**: leading icon 슬롯 없었음 확인 → `Show Search Icon`(BOOLEAN) + `Icon`(INSTANCE_SWAP, default=Icon/Search) 컴포넌트 프로퍼티 신설, 4개 State×Size variant 전부에 hidden-by-default 아이콘 인스턴스 삽입(선택적 슬롯이라 비검색 입력 폼엔 영향 없음 — 스크린샷으로 기존 4 variant 무변화 확인). itemSpacing을 spacing/2(8px) GAP 바인딩으로 추가했으나 invisible 자식은 오토레이아웃 gap 계산에서 제외되어 기본 상태엔 영향 없음. 테스트 인스턴스로 Show Search Icon=true 렌더링 확인(높이가 hug로 31→38px 자동 확장, padding 토큰 자체는 안 건드림).
- **헤더 로그아웃**: 신규 컴포넌트 만들지 않음 — Button(`97:47`) Style=Primary×Content=IconText 인스턴스에서 Icon만 Icon/Logout(96:36)으로 스왑하는 것으로 충분함을 테스트 인스턴스+스크린샷으로 확인. 사용 패턴만 design-system.md에 기록.
- 신규 색상/그림자 토큰 추가 없음(제약 준수). Icon/Delete의 teal 장식 요소가 coral 배경과 저대비(~1.04:1)임을 계산으로 발견했으나 ink 실루엣이 형태 인지를 주도해 비차단으로 기록(아이콘 재작색은 graphic-designer 소관, design-systems 범위 밖).
- `docs/design/design-system.md` 전체 갱신 완료 — Row Action Button/Input/Button 표 갱신, "알려진 갭"에 해소 3건 + 비차단 참고 1건 기록.

### 2026-07-12 — 파일럿 재바인딩 중 발견된 공유 컴포넌트 결함 4건 수정 (HIGH 해소용, 확정 게이트 아님)
- 배경: ui-designer가 직전 HIGH 결함(raw 프레임 잔존) 재바인딩 도중 컴포넌트 자체 결함 4건을 신규 발견해 design-systems로 넘김 — 화면이 아니라 컴포넌트 원인이라 여기서 처리.
- **Button Style=Amber 신설**: 신규 `component/button-bg-amber`(→color/amber/500) 토큰 추가. 기존 Danger variant 8개(Content×State×Size)를 `clone()`해 Style만 리네임하고 fill만 재바인딩하는 방식으로 재사용 — Primary/Danger와 동일한 보더 없는 솔리드-필 패턴, 라벨은 ink 고정. WCAG 10.95:1 PASS(직접 계산, Badge Count Default와 동일 색조합). 24→32 variant. **주의사항 재확인**: `componentSet.appendChild(clone)` 후 `clipsContent:true`인 ComponentSet 프레임이 새 variant 위치를 반영해 자동으로 커지지 않는다는 점을 이번에 처음 발견 — `set.resize()`로 bounding box(476→640)를 수동 갱신해야 새 variant가 스크린샷/렌더링에서 잘리지 않음(다음에도 재사용할 패턴, 알려진 갭에도 기록).
- **Sidebar Nav Item 배경 반전 버그 수정(HIGH 해소 필수)**: `component/navitem-bg-active`가 `color/teal/500`(사이드바 배경과 동색)에 직접 alias되어 있어 Active 강조가 시각적으로 사라지던 실제 버그를 발견·수정(amber로 재바인딩). Default nav-item도 `color/surface`(흰색) 하드바인딩이던 것을 fill 제거(투명)로 정정 — 둘 다 컴포넌트 레벨 수정, 인스턴스 오버라이드 아님. count-badge 스왑 로직은 건드리지 않고 유지 확인.
- **Alert content 서브프레임 흰색 fill 제거**: `104:8`/`104:16` "content" 프레임이 변수 바인딩 전혀 없는 하드코딩 흰색 fill을 갖고 있어 민트 틴트 배경 위에 흰 박스가 튀어나오는 결함 발견 — 별도 배경 필요성 없음을 확인 후 fill 제거, 상위 Alert 배경(민트 틴트)이 그대로 노출되도록 정정.
- **Table Row 헤어라인 divider 색상 오차 수정**: `component/table-row-border`가 범용 `color/border`(→gray/200, 실제 렌더링 #DCE0E1)를 재사용하고 있어 confirmed 2절의 정확한 예외값(#E0E0E0)과 미묘하게 어긋나 있던 것을 발견 — 신규 프리미티브 `color/border-hairline-value`(#E0E0E0) + 전용 시맨틱 `color/border-hairline`을 신설(범용 토큰 재사용 금지 원칙 준수)해 재바인딩, resolved color를 직접 조회해 정확히 일치함을 확인.
- 검증: 4건 모두 스크린샷 + boundVariables/resolved color 데이터 조회 병행 확인. Button 첫 variant(Primary) fallback 검정 렌더링은 이번에도 재현(알려진 MCP 도구 이슈, 데이터상 정상).
- `docs/design/design-system.md` 전체 갱신 완료 — 신규 토큰 2개(프리미티브 1+시맨틱 1) + 컴포넌트 토큰 1개(button-bg-amber) 추가, navitem-bg-active/table-row-border 값 변경 반영, Button 32 variant 반영, "알려진 갭"에 이번 해소 항목 4개 + 신규 도구 주의사항(ComponentSet resize) 기록.

### 2026-07-12 — SCREENS 3차본 HIGH 결함 수정 라운드 (7개 컴포넌트, 확정 게이트 아님)
- 사전 확인: `b-2-contacts-layout.md` 1~6절을 최우선 근거로 재확인 — 이전 라운드에서 "회귀 금지 우선, Default padding 그대로 유지"라 결정했던 것(Button/Input)이 정확히 이번 HIGH 결함의 원인이었음을 확인, 이번엔 그 결정을 뒤집고 confirmed 값으로 정정.
- 신규 프리미티브: `spacing/1-75`(7px)·`spacing/2-25`(9px)·`spacing/2-5`(10px)·`radius/xs`(5px) — 4px 그리드 예외를 반올림하지 않고 정확한 리터럴로 등록(변수명에 `.` 불가 확인, `-`로 대체). `color/mint/tint`(#E5F0ED, Alert 배경).
- 신규 세맨틱: `color/background-info`(→mint/tint), `color/border-ink`(→ink/900, Input/Select/Row Action Button/Alert 공유), `color/text-accent`. **WCAG 계산 중 발견한 사고**: `color/text-accent`를 처음엔 raw teal/500으로 alias했다가 흰 배경 대비 3.12:1(AA 미달)로 계산됨 → 브랜드 워드마크 스펙(9-2절)의 톤다운 값 `#0F7A6E`을 신규 `color/teal/700` 프리미티브로 등록해 재교체, 5.21:1 PASS로 재검증. **모든 색상 조합을 "이 정도면 되겠지"로 넘기지 않고 실제 계산해야 하는 이유를 몸소 재확인.**
- Button(`97:47`): Default padding 12×7 교정(8개 variant). Style=Danger 신설 — Primary variant 8개를 clone→Style 리네임→fill을 `component/button-bg-danger`(신규)로 재바인딩, 라벨은 ink 유지(WCAG 5.5:1 PASS). Style 옵션에 Danger 자동 등록 확인, 16→24 variant.
- Input(`100:46`)/Select(`101:64`): Default padding 10×7 교정, radius/sm(4)→radius/md(8) 전 variant 교정, State=Default/Selected 보더를 1px 회색→1.5px `color/border-ink`로 교정(Error는 코랄, Select Open은 기존 틸 유지 — 손대지 않음). Select Open 옵션패널 `effects:[]` 이미 그림자 없음 재확인(design-system.md 구판의 "적용 예정" 메모보다 confirmed "그림자 전혀 없음"이 우선).
- Badge(`102:65`): State(Default/Active) 축 신설 — Count는 Default=앰버/Active=흰색 플랫 필(보더 제거), Tag는 조합 완전성을 위해 State 복제만 하고 시각 변경 없음. Sidebar Nav Item(`103:106`)의 count-badge 인스턴스가 이전엔 Default/Active 둘 다 동일한 회색 배지를 가리켜 활성 구분이 전혀 없었던 실제 버그를 발견 → `swapComponent()`(Async 아님, 동기 API)로 상태별 정상 인스턴스로 스왑, radius도 4→8 교정.
- Table Row(`103:7`): padding 12×9 교정. category-badge(Badge Type=Tag 인스턴스) 제거 → `color/text-accent` teal 인라인 TEXT로 교체. **edit-icon/delete-icon 실측 결과, 기존 design-system.md가 서술했던 "8×4 padding+보더+radius5 유지" 스펙 자체가 실제 Figma엔 존재한 적이 없었음(bare 24×24 아이콘, 패딩/보더/hit area 전무)** — 신규 컴포넌트 `Row Action Button`(`166:421`, Style=Neutral/Danger, 같은 페이지에 생성)을 만들어 44×44 투명 hit-area 안에 실제 8×4/보더1px/radius5 시각 버튼을 중앙 배치, Table Row 인스턴스 교체. `figma.combineAsVariants`는 COMPONENT 노드만 자식으로 받는다는 제약 재확인(FRAME으로 만들면 에러 — `figma.createComponent()`로 처음부터 생성해야 함).
- Alert(`104:6`/`104:14`): 배경을 `color/surface`→`color/background-info`(민트 틴트)로 교체(WCAG 14.32:1). `Elevation/Raised`(effectStyleId+effects) 제거, 대신 1.5px `color/border-ink` 보더 신설, radius 4→8 교정. Elevation 토큰 정의 자체는 유지(다른 컴포넌트 재사용 위해).
- 검증: 전 컴포넌트 Instance Preview Row 방식으로 스크린샷 확인(Button `97:47` 첫 자식은 이번에도 fallback 검정 렌더링 재현 — 기존 알려진 도구 이슈, 인스턴스는 정상). 범위 외 항목(Button Disabled WCAG, 모달/토스트, MEDIUM/LOW) 미변경 확인.
- `docs/design/design-system.md` 전체 갱신 완료 — 7개 컴포넌트 결함 수정 내역, 신규 토큰 9개, Row Action Button 신규 컴포넌트 행 추가, "알려진 갭"에 이번에 해소된 6개 항목 기록.

### 2026-07-12 — Button/Input에 Size=Default/Large variant 축 신설 (로그인 화면 고정 크기 문제 대응)
- 사전 확인: `use_figma` 읽기 전용 스크립트로 Button(`97:47`)/Input(`100:46`) 실제 노드를 재열람 → 둘 다 이미 padding+hug 오토레이아웃 구조였음 확인(Button은 HUG×HUG, Input은 width FIXED×height HUG) — "고정 높이 재구성"은 조건부로 불필요, Size 축 추가만 진행.
- 실제 바인딩된 padding이 확정 스펙 문서(`b-2-contacts-layout.md`, Button 12×7px/Input 10×7px)와 다름을 발견(Button 실측 16×12, Input 실측 12×12 균일) — 스펙 문서 값은 참고만 하고 Default는 **기존 바인딩을 그대로 유지**(회귀 금지 원칙 우선, 재조정하지 않음). **→ 다음 라운드에서 바로 이 결정이 HIGH 결함으로 판정되어 뒤집힘.**
- Size=Large 구현: 새 색상/그림자 토큰 추가 없이 기존 spacing 토큰만 재사용(한 단계씩 상향) — Button: 가로 spacing/4(16)→spacing/6(24), 세로 spacing/3(12)→spacing/4(16) = 24×16px. Input: 전 방향 spacing/3(12)→spacing/4(16) 균일 = 16×16px(폭 220px는 그대로 FIXED 유지).
- 구현 절차: 기존 variant를 rename(`, Size=Default` 추가) → `clone()` → 패딩만 `setBoundVariable`로 재바인딩. **주의**: `clone()`이 ComponentSet 자식이 아니라 페이지에 떨어짐을 확인 → `componentSet.appendChild(clone)`으로 재편입 필요(다음에도 동일 패턴 재사용). Button 8→16 variant, Input 2→4 variant, `variantGroupProperties`에 Size(Default/Large) 정상 등록 확인.
- 회귀 검증: Button Primary+Default 계열(WCAG 수정된 `color/text-primary` 바인딩)이 clone에도 그대로 승계됨을 Default/Large 양쪽에서 직접 확인. Alert(`104:6`/`104:14`)의 `Elevation/Raised` 바인딩은 손대지 않았고 그대로임을 재확인.
- 검증: 각 컴포넌트 페이지에 "Instance Preview Row (Size=Large)" 신설해 실제 인스턴스 렌더링으로 확인(ComponentSet 직접 스크린샷은 기존에 알려진 fallback 검정 렌더링 버그 재현됨 — 데이터 이상 아님, 인스턴스는 정상 색상 렌더링).
- `docs/design/design-system.md` 갱신: Button/Input 컴포넌트 표에 Size variant·정확한 padding 값 반영, "알려진 갭" 섹션에 고정 높이 문제 해소 기록.

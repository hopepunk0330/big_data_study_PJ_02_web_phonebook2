# Design System — 확정 토큰/컴포넌트 인벤토리 (State Ledger)

이 문서는 design-systems가 만든 토큰(변수)·컴포넌트·아이콘 등록 현황의 **현재 확정 상태**다. Figma FOUNDATIONS/COMPONENTS 구역(비주얼 원본)의 텍스트 미러이며, ui-designer·interaction-designer 등 컴포넌트를 소비하는 모든 에이전트의 소스 오브 트루스다. design-systems가 토큰/컴포넌트를 추가·수정할 때마다 이 파일을 **덮어써서** 최신 상태로 유지한다(로그가 아니다 — 만든 과정은 각 에이전트의 `.claude/agent-memory/*.md` 작업 로그와 git 히스토리에 남는다).

**fileKey**: `zgGlMBwFglaDlaeyP4CkgR`

## 페이지 순서 (전체 파일, 확정)

| idx | pageId | name |
|---|---|---|
| 0 | `15:2` | 레퍼런스 |
| 1 | `52:2` | Brand Guide |
| 2 | `90:2` | Graphic Assets |
| 3 | `95:2` | Colors |
| 4 | `95:3` | Typography |
| 5 | `95:4` | Spacing |
| 6 | `116:5` | Elevation |
| 7 | `96:7` | Icons |
| 8 | `34:2` | 브랜드 컨셉 Concepts |
| 9 | `97:8` | Button |
| 10 | `100:2` | Input |
| 11 | `101:3` | Select |
| 12 | `102:3` | Badge |
| 13 | `103:3` | Table Row (Row Action Button 서브 컴포넌트도 이 페이지에 위치, `166:421`) |
| 14 | `103:92` | Sidebar Nav Item |
| 15 | `104:2` | Alert |
| 16 | `104:127` | Avatar |
| 17 | `222:524` | 파일럿 (ui-designer 소관, SCREENS) — Login/Contacts—With Data/Contacts—Empty 3개 파일럿 화면(각 최신 1개 + 폐기본 2세대)을 한 페이지에 좌우로 배치. 기존 idx 17~19(Login/Contacts—With Data/Contacts—Empty 개별 페이지)는 이 라운드에서 통합·삭제됨. |

주의: `figma.root.insertChild`로 페이지를 끼워 넣으면 새 페이지가 맨 끝에 붙는다 — 반드시 `insertChild(targetIdx, page)`로 FOUNDATIONS 규칙 순서에 맞게 재배치하고 `figma.root.children` 순서를 재확인할 것.

**[알려진 이슈, 이번 라운드 발견] 이 표의 나머지 항목과 실제 파일의 전체 페이지 개수가 이번 라운드 전부터 이미 어긋나 있었다**: idx 17 재배치 후 `figma.root.children` 전수 조회 결과, 실제 파일에는 (a) idx 1 자리에 "Brand Guide"가 아니라 "브랜드 컨셉 Concepts"(`34:2`)가 먼저 오고 "Brand Guide"(`52:2`)가 그 다음이며, (b) 이 표에 전혀 기록되지 않은 페이지 2개("컨셉, 디자인시안" `0:1`, "UI-design " `15:3`)가 맨 끝(현재 idx 18~19)에 이미 존재했다. 이번 작업 범위는 idx 17(파일럿) 한 줄 교체로 한정되어 있어 위 두 가지는 고치지 않았다 — design-pl에게 별도 보고, 후속 라운드에서 전체 표 재조사·정정 필요.

## 변수 컬렉션

- **Primitives** (`VariableCollectionId:95:5`, mode `Value`=`95:0`, scopes=[] 전부 — 의도된 설계, 피커에서 숨김): `color/teal/500`(#17A398) `color/teal/700`(#0F7A6E, 딥틸 — 밝은 배경 위 teal **텍스트** 전용 톤다운. 9-2절 워드마크 색상과 동일 값 재사용, WCAG 근거는 아래 "핵심 접근성 결정" 참고) `color/coral/500`(#FF5A76) `color/amber/500`(#FFCB47) `color/ink/900`(#1C1F21) `color/gray/0`(#FFFFFF) `color/gray/50`(#F7F8F8) `color/gray/100`(#EDEFEF) `color/gray/200`(#DCE0E1) `color/gray/400`(#9CA3A6) `color/gray/600`(#5C6366) `color/mint/tint`(#E5F0ED, Alert 배경 전용) `color/border-hairline-value`(#E0E0E0, `VariableID:181:692`, 테이블 행 구분선 전용 원시값) `shadow/color/ink-8`(ink, a=0.08) `shadow/color/ink-16`(ink, a=0.16)
- **Semantic Colors** (`VariableCollectionId:95:16`, mode `Value`=`95:1`): `color/background`(→gray/50) `color/surface`(→gray/0) `color/text-primary`(→ink/900) `color/text-secondary`(→gray/600) `color/border`(→gray/200) `color/success`(→teal/500) `color/error`(→coral/500) `color/warning`(→amber/500) `color/background-info`(→mint/tint, Alert 배경 전용, 브랜드 3색 대신 옅은 톤) `color/border-ink`(→ink/900, 1.5px/1px 잉크 보더 전용 semantic, Input/Select/Row Action Button/Alert가 공유) `color/text-accent`(→teal/700, 인라인 강조 텍스트 전용. 원시 teal/500 텍스트는 흰 배경 대비 3.12:1로 AA 미달이라 워드마크 톤다운 값을 재사용해 5.21:1로 교정) `color/border-hairline`(`VariableID:181:693`, →border-hairline-value, 테이블 행 헤어라인 전용, scope=STROKE_COLOR) `color/text-inverse`(`VariableID:219:2`, →`color/gray/0`(#FFFFFF) 그대로 alias, 신규 primitive 없음, scope=TEXT_FILL, WEB code syntax=`var(--color-text-inverse)`. **적용 범위는 브랜드 3색(teal/coral/amber) 배경 위 Display/제목급 텍스트로 한정** — 상세 근거·허용/금지 배경은 아래 "핵심 접근성 결정" 참고. gray 계열 배경(`color/surface`/`color/background` 등)에는 이 토큰을 쓰지 않는다 — 그 위 텍스트는 기존 `color/text-primary`(ink) 그대로)
- **Spacing** (`VariableCollectionId:95:25`, mode `Value`=`95:2`): `spacing/1`(4, `VariableID:95:26`) `spacing/1-75`(7, `VariableID:165:4`, 4px 그리드 예외, B-2 확정 padding 재현용) `spacing/2`(8, `VariableID:95:27`) `spacing/2-25`(9, `VariableID:165:5`, 위와 동일 사유) `spacing/2-5`(10, `VariableID:165:6`, 위와 동일 사유) `spacing/3`(12, `VariableID:95:28`) `spacing/4`(16, `VariableID:95:29`) `spacing/6`(24, `VariableID:95:30`) `spacing/8`(32, `VariableID:95:31`) `radius/sm`(4, `VariableID:95:32`) `radius/xs`(5, `VariableID:165:7`, 행 내부 소형 액션 버튼 전용) `radius/md`(8, `VariableID:95:33`) `radius/lg`(12, `VariableID:95:34`) `radius/full`(999, `VariableID:95:35`). 변수 이름에 `.`은 허용되지 않아 `-`로 표기(예: `spacing/1-75`=7px).
- **Elevation** (`VariableCollectionId:114:4`, mode `Value`=`114:0`, FLOAT 원시값, scope=`EFFECT_FLOAT`): `shadow/blur/sm`(8) `shadow/blur/lg`(16) `shadow/offset-y/sm`(2) `shadow/offset-y/lg`(4) `shadow/spread/none`(0)
- **Component Tokens** (`VariableCollectionId:97:2`, mode `Value`): `component/button-bg-primary`(→teal) `component/button-bg-secondary`(→gray/0) `component/button-border-secondary`(→teal) `component/button-bg-disabled`(→gray/200) `component/button-text-disabled`(→gray/400) `component/button-bg-danger`(→coral/500, Button Style=Danger 전용) `component/button-bg-amber`(`VariableID:180:98`, Button Style=Amber 전용, →`color/amber/500` 직접 alias, scope=[FRAME_FILL, SHAPE_FILL], Primary/Danger와 동일한 보더 없는 솔리드-필 패턴) `component/select-border-open`(→teal) `component/badge-bg-tag`(→teal) `component/table-row-border`(→`color/border-hairline` semantic, #E0E0E0 정확히 일치) `component/navitem-bg-active`(→`color/amber/500`, confirmed 6절 "선택된 내비게이션 상태=amber" 반영) `component/avatar-bg`(→teal)
- **Effect Styles (Semantic elevation)**: `Elevation/Raised`(id `S:59c3b20117267d27f5a05be838e769599240568d,` — DROP_SHADOW, color=shadow/color/ink-8, offsetY=shadow/offset-y/sm, radius=shadow/blur/sm, spread=shadow/spread/none. Alert에서는 제거됨 — 토큰 정의 자체는 유지, 향후 토스트 등 다른 배경 위 표면에 재사용 가능) `Elevation/Overlay`(id `S:53c51d35c8d8cde4a0d3202c2118502f1c6eeac8,` — color=shadow/color/ink-16, offsetY=shadow/offset-y/lg, radius=shadow/blur/lg. 적용 예정: 드롭다운/모달·팝오버 — 아직 실제 컴포넌트 바인딩 없음, Select Open 상태도 confirmed 문서 2절 "그림자 전혀 쓰지 않음" 규칙에 따라 바인딩하지 않음). 미적용 대상: 카드/버튼/인풋/Alert 등 flat 요소 — 남용 금지. B-2 확정 문서(2절)는 이 레이아웃 언어에서 그림자를 전혀 쓰지 않고 구조적 중요도를 잉크 보더 두께로만 표현하도록 규정한다.
- **핵심 접근성 결정**: 브랜드 3색(teal/coral/amber)은 전부 mid-tone이라 white 텍스트와 페어링하면 3:1대(AA 미달). 대신 `text-primary`(ink)를 브랜드색 배경 위에 얹으면 5.3~11:1(AA 통과) — **버튼/배지/배너 등 브랜드색 배경 위 텍스트는 전부 text-primary(ink) 고정**, 브랜드색은 배경·보더·아이콘에만 사용. success/error 자체도 본문 텍스트 색으로는 안 쓰고 아이콘/좌측 보더/보더 전용. **반대 방향(밝은 배경 위 브랜드색 텍스트)도 동일 원칙 적용**: teal/500(#17A398)을 흰 배경 위 텍스트로 쓰면 3.12:1로 AA 미달 — Table Row category 인라인 텍스트에 raw teal/500 대신 톤다운된 `color/teal/700`(#0F7A6E, 대비 5.21:1)을 `color/text-accent` semantic으로 등록해 사용한다. **Button Style=Amber 배경(#FFCB47)+text-primary(ink) 대비 10.95:1 PASS**. **Icon/Logout(ink 실루엣)+Button Style=Primary(teal) 배경 조합 재확인**: 위 "브랜드색 배경 위 텍스트=ink 고정" 규칙과 동일 팔레트라 라벨("로그아웃") 대비는 기존 5.3~11:1 PASS 범위 그대로, 아이콘 자체도 ink 실루엣이라 시인성 문제 없음(직접 테스트 인스턴스로 스크린샷 확인). **`color/text-inverse` 신설과 브랜드 3색 흰 텍스트 재검증(이번 라운드)**: WCAG 2.1 상대휘도 공식으로 브랜드 3색 배경×흰 텍스트(#FFFFFF)를 직접 재계산한 결과 — `teal`(#17A398) 대비 **3.1200:1**(큰 텍스트 3:1 PASS, 본문 4.5:1 FAIL), `coral`(#FF5A76) 대비 **3.0111:1**(큰 텍스트 3:1 PASS, 다만 여유폭이 0.01로 매우 근소 — WCAG 큰 텍스트 정의(18pt 이상 Regular 또는 14pt 이상 Bold)를 엄격히 만족하는 크기에서만 사용할 것, 그 아래로는 절대 확장하지 않는다), `amber`(#FFCB47) 대비 **1.5122:1**(큰 텍스트 3:1조차 크게 미달, FAIL). 이 세 값은 design-pl 사전 검증표(3.12/3.01/1.51)와 소수점까지 정확히 일치한다. **결론**: `color/text-inverse`(→`color/gray/0` alias)는 **teal·coral 배경 위 Display/제목급 텍스트(text style `Display/Latin`/`Display/KR`, 또는 시각적으로 24px 이상 且 Bold 이상에 상응하는 크기)에 한해서만 허용**한다. **amber 배경은 큰 텍스트 기준조차 미달이므로 이 토큰의 사용을 전면 금지**하고 "사용 금지 배경"으로 명시한다. **기존 규칙과의 관계**: 위 "브랜드색 배경 위 텍스트는 text-primary(ink) 고정" 규칙은 그대로 유지되며 변경되지 않는다 — Body/Caption 등 본문·일반 텍스트는 브랜드색 배경 위에서 계속 ink 고정이다. `color/text-inverse`는 이 규칙에 대한 예외가 아니라 **좁게 한정된 별도 케이스**다: Display/제목급처럼 애초에 큰 텍스트(3:1 기준 적용)에만, 그리고 teal·coral 두 배경에만 국한된다. Body/Caption 텍스트 스타일에는 이 토큰을 절대 바인딩하지 않는다. 실제 화면·컴포넌트 적용은 이번 범위에 포함하지 않는다(필요시 별도 ui-designer 라운드).

## Text Styles (Typography 페이지, `95:3`)

`Display/Latin`(Baloo 2 ExtraBold 40) `Display/KR`(Noto Sans KR Black 32) `Body`(Noto Sans KR Regular 16) `Caption`(Noto Sans KR Medium 12)

## Icons (`96:7`, 8개, `createComponentFromNode`로 원본 그대로 컴포넌트화)

`Icon/Search`(96:12) `Icon/Add`(96:17) `Icon/Edit`(96:22) `Icon/Delete`(96:27) `Icon/Category`(96:31) `Icon/Logout`(96:36) `Icon/Alert`(96:41) `Icon/User`(96:45)

이번 라운드는 새 아이콘을 추가 등록하지 않았다 — 기존 8종을 컴포넌트 레벨에서 실사용으로 연결(binding)하는 라운드였다(`Icon/Edit`/`Icon/Delete`를 Row Action Button에, `Icon/Search`를 Input에, `Icon/Logout`을 Button 사용 패턴에).

## 컴포넌트 (COMPONENTS 구역, 9개)

| 컴포넌트 | 페이지 | ComponentSet/Component ID | variant |
|---|---|---|---|
| Button | `97:8` | `97:47` | Style(Primary/Secondary/Danger/Amber)×Content(Text/IconText)×State(Default/Disabled)×Size(Default/Large) = 32. Label(TEXT), Icon(INSTANCE_SWAP, default=Icon/Add). 컴포넌트 구조 변경 없음. **신규 사용 패턴 문서화(이번 라운드)**: 헤더 로그아웃 액션은 신규 컴포넌트를 만들지 않고 **Style=Primary, Content=IconText 인스턴스에서 Icon만 `Icon/Logout`(96:36)으로 INSTANCE_SWAP**하는 것으로 완전히 충분함을 테스트 인스턴스로 직접 확인(스크린샷 검증, 라벨 "로그아웃"으로 교체해 확인). 기존 IconText 패딩·gap(spacing/2)·높이(padding+hug)가 그대로 로그아웃 액션에도 성립해 상단바 인라인 배치에 별도 제약이 발견되지 않았다 — 별도 컴포넌트/variant 확장 불필요로 판단. 사용 규칙: 헤더 로그아웃 = `Button(Style=Primary, Content=IconText, Size=Default)` + `Icon=Icon/Logout` + `Label="로그아웃"` |
| Input | `100:2` | `100:46` | State(Default/Error)×Size(Default/Large) = 4(기존 variant 그대로, 무결성 확인 완료). **신규 컴포넌트 프로퍼티 추가(이번 라운드)**: `Show Search Icon#192:0`(BOOLEAN, default=false), `Icon#192:5`(INSTANCE_SWAP, default=Icon/Search `96:12`). 4개 variant 전부에 `leading-icon`이라는 이름의 Icon/Search 인스턴스를 첫 번째 자식으로 삽입하고 두 프로퍼티에 바인딩(`visible`→Show Search Icon, `mainComponent`→Icon), 기본값 false라서 인스턴스 자체도 `visible=false`로 시작 — 기존 4 variant는 스크린샷으로 픽셀 단위 무변화 확인(비검색 입력 폼에는 아이콘이 전혀 나타나지 않음). itemSpacing을 0→`spacing/2`(8px, `VariableID:95:27`) GAP 바인딩으로 변경했으나 Figma 오토레이아웃은 invisible 자식을 gap 계산에서 제외하므로 아이콘이 꺼진 상태에서는 시각적 영향 없음(직접 확인). `Show Search Icon=true`로 테스트 인스턴스를 만들어 검증: Icon/Search가 좌측에 정상 렌더링되고, counterAxisSizingMode=AUTO(hug)라 Default 높이가 31→38px로 자연스럽게 커짐(24×24 아이콘을 수용하기 위한 의도된 결과, padding 토큰 자체는 손대지 않음 — "높이는 padding+hug로 도출" 원칙 그대로 유지). confirmed 문서(4절)의 padding 10×7px(Default)/16×16px(Large)은 변경하지 않았다 |
| Select | `101:3` | `101:64` | State(Default/Selected/Open) = 3. 변경 없음 |
| Badge | `102:3` | `102:65` | Type(Tag/Count)×State(Default/Active) = 4. 변경 없음 |
| Table Row | `103:3` | `103:7` (variant 없음) | Name/Phone/Address(TEXT), category(TEXT), edit-action/delete-action(INSTANCE, Row Action Button). 변경 없음(이번 라운드는 Row Action Button 서브 컴포넌트 자체만 수정, Table Row 레이아웃은 그대로) |
| **Row Action Button** | `103:3` (Table Row와 같은 페이지) | `166:421` | Style(Neutral/Danger) = 2. **버그 수정(이번 라운드, 필수)**: `get_metadata`/`get_design_context`로 직접 열어 확인한 결과, TEXT 라벨은 애초에 없었고 이미 INSTANCE_SWAP 컴포넌트 프로퍼티(`Icon#166:0`, default=Icon/Edit `96:22`)와 아이콘 인스턴스 슬롯이 존재했다 — 다만 **Neutral과 Danger 두 variant의 내부 icon 인스턴스가 둘 다 Icon/Edit(펜)로 바인딩돼 있어 Danger(삭제) 행에서도 수정 아이콘이 표시되는 실제 버그**를 발견했다. Danger variant(`166:420`)의 icon 인스턴스(`166:416`)를 `swapComponent()`로 `Icon/Delete`(96:27)로 교체하고 `componentPropertyReferences`(`mainComponent`→`Icon#166:0`)를 재확인, Neutral(`166:414`, 아이콘 `166:410`)은 Icon/Edit 그대로 유지 — 수정 후 스크린샷으로 Neutral=편집 아이콘 / Danger=삭제 아이콘이 서로 다르게 렌더링됨을 확인. **판단 포인트("아이콘만" vs "아이콘+라벨") 근거**: 기존 구조가 이미 "아이콘만"(라벨 없음) 형태였고, 이번 라운드에서 이 형태를 그대로 유지하기로 판단했다 — 이유: (1) 44×44 히트 영역이 confirmed 값으로 고정돼 있어 라벨 텍스트(14px)+gap(8px)를 추가하면 정사각형 히트 타깃을 깨거나 아이콘을 축소해야 함, (2) Sidebar Nav Item 폭 212px 컬럼 안에서 이미 아이콘+라벨+count-badge를 배치하는 좁은 공간이라 행 액션까지 라벨을 붙이면 밀도가 과해짐, (3) Table Row 자체가 12×9px 고밀도 padding의 리스트라 라벨 추가 시 행 폭이 늘어나 열 정렬이 깨짐. 44×44 히트 영역(투명 padding), radius/xs(5px), Style=Neutral/Danger의 잉크 보더(1px) 회귀 없음 재확인. **접근성 참고(비차단)**: Icon/Delete의 teal 장식 요소는 coral 배경과 대비가 매우 낮다(약 1.04:1, 직접 계산) — 다만 아이콘의 형태 인지는 ink 실루엀(대비 약 5.50:1, PASS)이 주도하므로 식별성 문제는 없다고 판단. 이 다색 아이콘 그래픽 자체(Icon/Add도 teal+ink 조합으로 Primary 버튼 위에서 이미 동일 특성을 가짐)는 graphic-designer 원화의 고유 특성이라 design-systems가 재작색하지 않는다(역할 경계) — 재검토가 필요하면 graphic-designer에게 요청 |
| Sidebar Nav Item | `103:92` | `103:106` | State(Default/Active) = 2. Label(TEXT), count-badge(Badge Type=Count 인스턴스). 변경 없음(이번 라운드 대상 아님 — 화면상 Sidebar의 edit/delete 액션 재바인딩은 ui-designer 후속 작업) |
| Alert | `104:2` | `104:108` | Type(Success/Error) = 2. Message(TEXT), icon(Icon/Alert 고정 인스턴스), accent-bar(success/error semantic 컬러). 변경 없음 |
| Avatar | `104:127` | `104:131` (variant 없음) | icon(Icon/User 인스턴스), 32x32 원형, 단일 크기. 변경 없음 |

## 알려진 갭 / 이슈

- **Button Disabled variant 6종(Primary/Secondary/Danger/Amber) WCAG 대비 미달(1.93:1)** — 별도 라운드 필요, 여전히 미해결.
- **Heading/Label 텍스트 스타일 토큰, Table Header 컴포넌트 없음** — 여전히 미해결.
- **radius/lg(12)가 confirmed 3절의 "10px" 값과 정확히 일치하지 않음** — Table Row 자체(`103:7`)의 cornerRadius는 0이라 이번 라운드에도 해당하지 않음.
- **화면상 버튼 색 스왑 미해결**: 사이드바/본문 버튼 색이 뒤바뀐 상태 — 여전히 ui-designer 후속 작업 대기.
- **[해소됨, 이전 라운드] Row Action Button Danger variant가 Icon/Edit를 잘못 사용하던 버그** — Icon/Delete로 정정(위 표 참고). Neutral/Danger 두 variant가 서로 다른 아이콘을 실제로 렌더링하는지 스크린샷으로 확인 완료.
- **[해소됨, 이전 라운드] Input에 검색 leading icon 슬롯 부재** — `Show Search Icon`(BOOLEAN) + `Icon`(INSTANCE_SWAP) 컴포넌트 프로퍼티 신설, 4개 State×Size variant 전부에 hidden-by-default 아이콘 인스턴스 삽입. 기존 4 variant 무결성 스크린샷으로 확인, 신규 사용(검색창)에서 아이콘 정상 노출 및 높이 자동 확장(31→38px, hug) 테스트 인스턴스로 확인.
- **[해소됨, 이전 라운드] 헤더 로그아웃 액션에 등록된 Icon/Logout 미사용** — 신규 컴포넌트 없이 기존 Button(Style=Primary, Content=IconText)에서 Icon만 스왑하는 것으로 충분함을 확인, 사용 패턴으로 문서화(위 Button 표 참고).
- **비차단 참고(이전 라운드 발견)**: Icon/Delete의 teal 장식 요소가 coral(Danger) 배경과 저대비(~1.04:1)이나 ink 실루엣이 형태 인지를 주도해 식별성 문제 없음(위 Row Action Button 행 참고). 아이콘 자체 재작색은 design-systems 범위 밖(graphic-designer 소관).
- **[신규, 이번 라운드] `color/text-inverse` 신설 — 화면/컴포넌트 실제 적용은 아직 없음**: 토큰 정의·문서화만 완료(위 "핵심 접근성 결정" 참고), teal·coral 배경 위 Display/제목급 텍스트에만 한정. 실제 어느 컴포넌트/화면에 바인딩할지는 이번 범위 밖 — 필요시 후속 ui-designer 라운드에서 적용.
- **[해소됨, 이전 라운드]** Sidebar Nav Item 배경 반전 버그, Alert content 서브프레임 하드코딩 흰색 fill, Table Row 헤어라인 divider 색상 오차, Button Style=Amber 부재, Button/Input 고정 높이 문제, Button Default 패딩 4px 그리드 반올림 결함, Input/Select 보더·라운드 결함, Badge Count 상태 미분화 결함, Table Row category 필드 오용 바인딩, Table Row 소형 액션 버튼 터치 영역 문제, Alert 그림자/배경 결함.
- **알려진 도구 이슈**: 방금 만든/수정한 ComponentSet의 첫 번째 자식이 `get_screenshot`에서 variable-bound fill이 fallback(검정)으로 렌더링되는 경우가 있음(MCP 렌더링 한계로 추정, 데이터상 바인딩은 정상). 검증은 항상 데이터 조회(boundVariables/resolved color/componentPropertyReferences) + screenshot 병행으로 한다.
- **추가 발견(이전 라운드)**: 방금 만든 컴포넌트를 담는 ComponentSet 프레임이 `clipsContent: true`이면서 기존 bounding box를 넘어서는 위치에 신규 variant를 추가할 경우 잘려 보이지 않을 수 있음 — variant 추가 후 항상 `set.resize()`로 프레임 크기를 자식 bounding box에 맞게 갱신할 것.
- **[신규, 이번 라운드] 페이지 통합 작업 중 106:3(Contacts — With Data)에서 파일럿 3세대와 무관한 프레임 3개 발견**: "확정 디자인 - 절대 원본 건들지 말것"(`214:349`)과 "Document"(`215:2775`, `214:852`) — 이름/보호 라벨로 볼 때 다른 작업 맥락의 참조 콘텐츠로 추정. 내용은 전혀 수정하지 않고 삭제도 하지 않았다(라벨 그대로 "절대 건들지 말것" 존중) — 새 "파일럿" 페이지 안에서 3개 카테고리 비교 그리드와 완전히 분리된 하단 영역(y=5000, 그리드와 500px+ 간격)으로만 위치 이동. 원래 있어야 할 자리(다른 페이지? 별도 레퍼런스?)는 design-pl 판단이 필요 — 이번 작업 범위(구조 이동)에서 임의로 재배치 결정하지 않았다.

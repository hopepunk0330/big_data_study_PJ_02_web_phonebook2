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
| 13 | `103:3` | Table Row |
| 14 | `103:92` | Sidebar Nav Item |
| 15 | `104:2` | Alert |
| 16 | `104:127` | Avatar |
| 17 | `106:2` | Login (ui-designer 소관, SCREENS) |
| 18 | `106:3` | Contacts — With Data (ui-designer 소관) |
| 19 | `106:4` | Contacts — Empty (ui-designer 소관) |

주의: `figma.root.insertChild`로 페이지를 끼워 넣으면 새 페이지가 맨 끝에 붙는다 — 반드시 `insertChild(targetIdx, page)`로 FOUNDATIONS 규칙 순서에 맞게 재배치하고 `figma.root.children` 순서를 재확인할 것.

## 변수 컬렉션

- **Primitives** (`VariableCollectionId:95:5`, mode `Value`=`95:0`, scopes=[] 전부 — 의도된 설계, 피커에서 숨김): `color/teal/500`(#17A398) `color/coral/500`(#FF5A76) `color/amber/500`(#FFCB47) `color/ink/900`(#1C1F21) `color/gray/0`(#FFFFFF) `color/gray/50`(#F7F8F8) `color/gray/100`(#EDEFEF) `color/gray/200`(#DCE0E1) `color/gray/400`(#9CA3A6) `color/gray/600`(#5C6366) `shadow/color/ink-8`(ink, a=0.08) `shadow/color/ink-16`(ink, a=0.16)
- **Semantic Colors** (`VariableCollectionId:95:16`, mode `Value`=`95:1`): `color/background`(→gray/50) `color/surface`(→gray/0) `color/text-primary`(→ink/900) `color/text-secondary`(→gray/600) `color/border`(→gray/200) `color/success`(→teal/500) `color/error`(→coral/500) `color/warning`(→amber/500)
- **Spacing** (`VariableCollectionId:95:25`, mode `Value`=`95:2`): `spacing/1`(4) `spacing/2`(8) `spacing/3`(12) `spacing/4`(16) `spacing/6`(24) `spacing/8`(32) `radius/sm`(4) `radius/md`(8) `radius/lg`(12) `radius/full`(999)
- **Elevation** (`VariableCollectionId:114:4`, mode `Value`=`114:0`, FLOAT 원시값, scope=`EFFECT_FLOAT`): `shadow/blur/sm`(8) `shadow/blur/lg`(16) `shadow/offset-y/sm`(2) `shadow/offset-y/lg`(4) `shadow/spread/none`(0)
- **Component Tokens** (`VariableCollectionId:97:2`, mode `Value`): `component/button-bg-primary`(→teal) `component/button-bg-secondary`(→gray/0) `component/button-border-secondary`(→teal) `component/button-bg-disabled`(→gray/200) `component/button-text-disabled`(→gray/400) `component/select-border-open`(→teal) `component/badge-bg-tag`(→teal) `component/table-row-border`(→color/border semantic) `component/navitem-bg-active`(→teal) `component/avatar-bg`(→teal)
- **Effect Styles (Semantic elevation)**: `Elevation/Raised`(id `S:59c3b20117267d27f5a05be838e769599240568d,` — DROP_SHADOW, color=shadow/color/ink-8, offsetY=shadow/offset-y/sm, radius=shadow/blur/sm, spread=shadow/spread/none. 적용 대상: Alert/토스트 등 배경 위 낮은 표면) `Elevation/Overlay`(id `S:53c51d35c8d8cde4a0d3202c2118502f1c6eeac8,` — color=shadow/color/ink-16, offsetY=shadow/offset-y/lg, radius=shadow/blur/lg. 적용 예정: 드롭다운/모달·팝오버 — 아직 실제 컴포넌트 바인딩 없음, 모달 컴포넌트 자체가 미존재). 미적용 대상: 카드/버튼/인풋 등 flat 요소 — 남용 금지.
- **핵심 접근성 결정**: 브랜드 3색(teal/coral/amber)은 전부 mid-tone이라 white 텍스트와 페어링하면 3:1대(AA 미달). 대신 `text-primary`(ink)를 브랜드색 배경 위에 얹으면 5.3~11:1(AA 통과) — **버튼/배지/배너 등 브랜드색 배경 위 텍스트는 전부 text-primary(ink) 고정**, 브랜드색은 배경·보더·아이콘에만 사용. success/error 자체도 본문 텍스트 색으로는 안 쓰고 아이콘/좌측 보더/보더 전용.

## Text Styles (Typography 페이지, `95:3`)

`Display/Latin`(Baloo 2 ExtraBold 40) `Display/KR`(Noto Sans KR Black 32) `Body`(Noto Sans KR Regular 16) `Caption`(Noto Sans KR Medium 12)

## Icons (`96:7`, 8개, `createComponentFromNode`로 원본 그대로 컴포넌트화)

`Icon/Search`(96:12) `Icon/Add`(96:17) `Icon/Edit`(96:22) `Icon/Delete`(96:27) `Icon/Category`(96:31) `Icon/Logout`(96:36) `Icon/Alert`(96:41) `Icon/User`(96:45)

## 컴포넌트 (COMPONENTS 구역, 8개)

| 컴포넌트 | 페이지 | ComponentSet/Component ID | variant |
|---|---|---|---|
| Button | `97:8` | `97:47` | Style(Primary/Secondary)×Content(Text/IconText)×State(Default/Disabled) = 8. Label(TEXT), Icon(INSTANCE_SWAP, default=Icon/Add). 전 variant WCAG PASS(Disabled 4종 제외 — 원래도 미달, 별도 이슈로 트래킹 중, 아래 참고) |
| Input | `100:2` | `100:46` | State(Default/Error) = 2. Placeholder(TEXT) |
| Select | `101:3` | `101:64` | State(Default/Selected/Open) = 3. Label(TEXT). Open은 옵션 패널(가족/친구/기타) 포함 |
| Badge | `102:3` | `102:65` | Type(Tag/Count) = 2. Label(TEXT) |
| Table Row | `103:3` | `103:7` (variant 없음) | Name/Phone/Address(TEXT), category-badge(Badge Type=Tag 인스턴스), edit-icon(Icon/Edit), delete-icon(Icon/Delete) |
| Sidebar Nav Item | `103:92` | `103:106` | State(Default/Active) = 2. Label(TEXT), count-badge(Badge Type=Count 인스턴스) |
| Alert | `104:2` | `104:108` | Type(Success/Error) = 2. Message(TEXT), icon(Icon/Alert 고정 인스턴스), accent-bar(success/error semantic 컬러). 최상위 노드(`104:6`, `104:14`)에 `Elevation/Raised` 바인딩 |
| Avatar | `104:127` | `104:131` (variant 없음) | icon(Icon/User 인스턴스), 32x32 원형, 단일 크기 |

## 알려진 갭 / 이슈

- **Button Disabled variant 4종 WCAG 대비 미달(1.93:1)** — 활성 상태 버그 수정 범위 밖이라 아직 미해결. 별도 라운드 필요.
- **Heading/Label 텍스트 스타일 토큰, Table Header 컴포넌트 없음** — ui-designer가 파일럿 제작 중 임시 대체해서 사용 중. 전체 확장 전 보완 필요.
- **알려진 도구 이슈**: 방금 만든 ComponentSet의 첫 번째 자식이 `get_screenshot`에서 variable-bound fill이 fallback(검정)으로 렌더링되는 경우가 있음(MCP 렌더링 한계로 추정, 데이터상 바인딩은 정상). 검증은 항상 "Instance Preview Row"(각 variant의 인스턴스 나열)로 한다.

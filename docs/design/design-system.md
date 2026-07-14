# Design System — 확정 토큰/컴포넌트 인벤토리 (State Ledger)

**⚠ ui-designer 등 컴포넌트를 소비하는 모든 에이전트는 반드시 1~7절만 참조하고 8절(Legacy)은 절대 사용하지 않는다.**

이 문서는 design-systems가 만든 토큰(변수)·컴포넌트·아이콘 등록 현황의 **현재 확정 상태**다. Figma FOUNDATIONS/COMPONENTS 구역(비주얼 원본)의 텍스트 미러이며, ui-designer·interaction-designer 등 컴포넌트를 소비하는 모든 에이전트의 소스 오브 트루스다. design-systems가 토큰/컴포넌트를 추가·수정할 때마다 이 파일을 **덮어써서** 최신 상태로 유지한다(로그가 아니다 — 만든 과정은 각 에이전트의 `.claude/agent-memory/*.md` 작업 로그와 git 히스토리에 남는다).

**fileKey**: `zgGlMBwFglaDlaeyP4CkgR`

## 0. 이번 라운드 — 사용자 확정 디자인(8개 프레임)에서 직접 추출 (2-4번 규칙)

이번 라운드는 `docs/harness/design-team/figma-file-organization.md` 2-4번 규칙에 따라, **AI 파일럿을 거치지 않고** 사용자가 Figma에서 직접 만들어 확정한 8개 프레임("확정 디자인 - 절대 원본 건들지 말것-", 부모 섹션 `248:11689`)에서 실제 사용된 값을 직접 관찰(`get_screenshot`/`get_metadata`)해 토큰·컴포넌트로 추출했다. 8개 프레임은 전부 읽기 전용으로만 관찰했고 내용/이름을 전혀 수정하지 않았다.

이 라운드 이전에 존재하던 "B-2 파일럿" 기반 컴포넌트(Button/Input/Select/Badge/Table Row/Sidebar Nav Item — 아래 8절)는 `docs/design/confirmed/user-confirmed-final-design.md`에 따라 **완전히 대체**됐다. 이름이 겹치는 3개 컴포넌트(Button, Row Action Button, Sidebar Nav Item)는 구분을 위해 기존 것을 `[Legacy B-2] ` 접두사로 리네임했다(내용은 전혀 건드리지 않음, 이름만 변경). **(갱신)** 나머지 겹치지 않는 이름(Input/Select/Badge/Table Row/Alert의 옛 컴포넌트) 5개도 동일하게 `[Legacy B-2] ` 접두사로 리네임 완료했다(내용은 전혀 건드리지 않음, 이름만 변경 — 8절 참고). Avatar(`104:131`)만 유일하게 리네임 대상에서 제외됐다 — 확정 디자인과 정확히 일치해 현재도 유효하기 때문이다. 즉 옛 legacy 9개 컴포넌트 중 8개는 `[Legacy B-2] ` 접두사로 구분되고, Avatar 1개만 접두사 없이 그대로 유효 컴포넌트로 남는다. **이 문서의 "1~7절"이 현재 정식 소스이고 "8절 legacy"는 참고용 이력**이다.

### 0-1. design-qa 감사 후 정정 (추가 라운드, 원본 프레임은 무수정)

design-qa 감사에서 등록 컴포넌트 3건이 원본 확정 프레임 실측값과 다르게 잘못 추출되어 있음이 지적되어, 컴포넌트/토큰 쪽만 정정했다(원본 8개 프레임은 이번에도 손대지 않음, 읽기 전용 재확인만 수행). 재확인은 `get_metadata`/`use_figma` 읽기 전용 스크립트로 hex 값까지 재실측했다.

1. **TypeSelector(`257:28`) 색상 불일치** — 미선택 칩 보더가 `component/typeselector-unselected-text`(#888, 텍스트용 토큰)를 잘못 재사용해 텍스트와 보더가 같은 색으로 나오고 있었다. 원본 실측 보더는 `#CCCCCC`. 또한 "회사" 선택 텍스트가 `component/typeselector-company-selected-accent`(#E6800A, 보더/닷 전용 토큰)를 잘못 재사용하고 있었다. 원본 실측 텍스트색은 `#7A3D00`. → 신규 원시값 `color/gray/300`(#CCCCCC), `color/orange/900`(#7A3D00) + 신규 컴포넌트 토큰 `component/typeselector-unselected-border`, `component/typeselector-company-selected-text`를 만들어 TypeSelector 전용으로 재바인딩(4개 미선택 칩 보더 + "기타/선택" 칩 보더 + "회사/선택" 텍스트, 총 6개 노드). 다른 컴포넌트는 이 두 신규 토큰을 참조하지 않는다.
2. **Table Row Action(`260:100`) 텍스트 크기 불일치** — 등록 컴포넌트가 13px였으나 원본(main `214:590`/`214:593` 등)은 10px. → "수정"/"삭제" 텍스트 노드 fontSize를 10px로 직접 정정.
3. **Row Action Button(`260:95`) Neutral 보더 불일치** — `color/ink/900`(#1A1A1A, 2px 기본 컴포넌트 보더용)을 재사용하고 있었으나, 원본(사이드바 "카테고리 관리" 소형 버튼, `215:2365`/`215:2414` 등)과 확정 스펙 문서(§4-1)의 실측값은 `#1C1F21`로 별개 값이다. → 신규 원시값 `color/ink/800`(#1C1F21, ink/900과 별개) + 신규 컴포넌트 토큰 `component/row-action-button-border-neutral`을 만들어 Row Action Button Neutral 보더에만 재바인딩. `component/button-border-neutral`(ink/900, NeoBtn/Button Neutral 아웃라인 2px 보더)은 그대로 유지 — 두 보더 토큰은 굵기·용도가 다른 별개 값이라 통합하지 않는다.

정정 후 `use_figma` 읽기 전용 스크립트로 3건 모두 원본과 hex 단위로 일치함을 재확인했다(아래 1절/5절에 갱신 반영).

### 0-2. 후속 정정 및 추가 (2026-07-14)

design-qa/graphic-designer의 갭 감사에서 발견된 두 건을 처리했다(원본 확정 프레임은 이번에도 전혀 수정하지 않음, 읽기 전용 재확인만 수행).

1. **`Pixel/Star`(`255:11`) description 오기 정정** — description 텍스트가 "흰색"이라고 적혀 있었으나, 마스터 컴포넌트의 실제 vector fill을 재확인한 결과 잉크 `#1a1a1a`였다(graphic-designer가 `docs/design/graphic-assets.md`에 이미 관찰해 기록해둔 특이사항). **fill 값 자체는 정상이라 건드리지 않았고, description 텍스트만 실측값에 맞게 정정**했다: "로고 심볼 내부 별(12px, 잉크 #1a1a1a). 마스터 컴포넌트 fill 실측값 기준(로고 심볼 코랄 원 안에서는 흰색으로 인스턴스 오버라이드되어 사용됨). PxStar 원본."
2. **`Pixel/Eye` 신규 추출·등록** — 9종 추출 라운드(0절)에서 누락됐던 비밀번호 표시/숨김 토글 아이콘. 확정 login 프레임(`247:6666`) 안의 원본 `PixelEye`(`247:6814`, 14×10, 6개 vector 블록, 잉크 `#1a1a1a`)를 비파괴적으로 clone(원본은 무수정, 여전히 `247:6814`에 그대로 존재) → "Icons" 페이지(`96:7`, y=2000 클러스터, x=1080)로 이동 → `createComponentFromNode`로 `Pixel/Eye` 컴포넌트(`281:405`)로 정식 등록했다. 나머지 9종과 동일한 마이크로 픽셀 아이콘 트랙 컨벤션(단색 실루엣, 사각 블록 조합, 안티앨리어싱 없는 각진 형태)을 그대로 따른다. 스크린샷으로 형태 일치 검증 완료. 아래 4절 Icons 목록에 반영.

### 0-3. Legacy 컴포넌트 폐기(컴포넌트 등록 해제) 및 CornerInput 정정 (2026-07-14)

사용자가 "레거시라고 되어 있는것은 폐기처리해줘. 컴포넌트를 해제해야 피그마에 얽히지 않을거 같아"라고 요청해, 8절 Legacy 목록의 컴포넌트 8개(Avatar 제외)를 대상으로 처리했다. 원본 확정 8개 프레임(`248:11689` 하위)은 이번에도 전혀 손대지 않았다.

**절차**: ① 8개 컴포넌트를 참조하는 INSTANCE가 파일 전체(전체 20개 페이지, 확정 8개 프레임 포함 — 읽기 전용 확인만)에 실제로 존재하는지 `use_figma` 읽기 전용 스크립트로 전수 검색했다. ② 인스턴스가 없는 컴포넌트만 COMPONENT/COMPONENT_SET → FRAME 전환(자식 노드를 새 FRAME으로 이동해 시각적 내용을 그대로 유지하고 원래 COMPONENT/COMPONENT_SET 노드는 제거)을 진행했다.

**인스턴스 검색 결과**:
- **`[Legacy B-2] Table Row`(`103:7`) — 인스턴스 7개 발견, 해제하지 않고 보류**: Table Row 페이지(`103:3`)에 1개(`103:77`), 파일럿 페이지(`222:524`)의 `❌ 폐기 — B-2 레이아웃 미반영(재해석됨) — Contacts — With Data — Screen` 프레임 안에 6개(`110:220`/`110:234`/`110:248`/`110:262`/`110:276`/`110:290`). 지시에 따라 이 컴포넌트는 건드리지 않았다.
- 나머지 7개(`[Legacy B-2] Button` `97:47`, `[Legacy B-2] Row Action Button` `166:421`, `[Legacy B-2] Sidebar Nav Item` `103:106`, `[Legacy B-2] Input` `100:46`, `[Legacy B-2] Select` `101:64`, `[Legacy B-2] Badge` `102:65`, `[Legacy B-2] Alert` `104:108`)는 인스턴스 0개 확인 → 아래 표대로 전환 완료.

**전환 결과** (이름은 그대로 유지, 자식 노드/시각 내용 무손실 이전 — 스크린샷으로 개별 검증 완료):

| 컴포넌트 | 페이지 | 기존 ID (COMPONENT_SET, 삭제됨) | 신규 ID (FRAME) |
|---|---|---|---|
| [Legacy B-2] Button | `97:8` | `97:47` | `314:843` |
| [Legacy B-2] Row Action Button | `103:3` | `166:421` | `314:319` |
| [Legacy B-2] Sidebar Nav Item | `103:92` | `103:106` | `314:876` |
| [Legacy B-2] Input | `100:2` | `100:46` | `314:879` |
| [Legacy B-2] Select | `101:3` | `101:64` | `314:893` |
| [Legacy B-2] Badge | `102:3` | `102:65` | `314:897` |
| [Legacy B-2] Alert | `104:2` | `104:108` | `314:902` |

전환된 7개는 이제 FRAME 타입이라 Figma의 Assets/Insert 패널에 컴포넌트로 노출되지 않는다. 전환 과정에서 CatBadge(`256:17`)/TypeSelector(`257:28`)/Toast(`263:53`)/Avatar(`104:131`)/Table Row(`103:7`)와 그 인스턴스(`103:77`)는 전혀 건드리지 않았음을 각 단계마다 재확인했다.

**CornerInput(`261:12`, Focus=Yes 짝 `288:13`) 결함 수정 — 확정 디자인과 불일치**: 메인 세션이 확인한 결함으로, 확정 디자인(로그인 `247:6666`의 `247:6801`/`247:6811`, main-수정 모달 `248:8103`의 `248:9813`/`248:9823`/`248:9833`)의 실제 "각진(radius 0) 입력창"은 순수 2px ink 사각 보더 하나뿐이고 모서리 장식이 없다. 그런데 등록된 CornerInput에는 네 모서리에 8×8 `CornerBracket` 노드가 붙어 있어(확정 프레임에 없는 걸 임의로 추가한 오류) 정정했다.

- Focus=No(`261:12`)에서 `CornerBracket` 4개(`261:14`/`261:17`/`261:20`/`261:23`) 제거.
- Focus=Yes(`288:13`)에서 대응하는 `CornerBracket` 4개(`288:15`/`288:18`/`288:21`/`288:24`) 제거.
- 남은 자식은 텍스트 노드(`261:13`/`288:14`, placeholder "윤아")뿐이며, 시각 요소는 컴포넌트 루트의 흰 배경 + 2px ink(`color/ink/900` 바인딩) `INSIDE` 스트로크 + `radius 0`뿐임을 재확인(스크린샷 검증 완료).
- **폭 처리**: 로그인/가입 입력창 실측 352px, CornerInput 고정 392px(모달 쪽과 일치)로 서로 다르다. 새 variant를 만들지 않고 **392px를 베이스로 유지**하며, 로그인/가입처럼 352px가 필요한 컨텍스트는 인스턴스 리사이즈로 대응하기로 컴포넌트 description에 명시했다.

## 1. 변수 컬렉션 (최신, 확정 디자인 기준)

### 1-1. Primitives (`VariableCollectionId:95:5`, mode `Value`=`95:0`, scopes=[] 전부 — 피커에서 숨김)

**기존 브랜드 3색 재사용 확인**: `color/teal/500`(#17A398) `color/coral/500`(#FF5A76) `color/amber/500`(#FFCB47) — 이번 확정 디자인에서도 동일 hex로 실제 사용됨을 재확인, 신규 선언 없이 그대로 재사용.

**정정**: `color/ink/900` 값을 기존 `#1C1F21`에서 확정 디자인의 실측값 `#1a1a1a`로 정정(구조선·보더·하드 그림자·기본 텍스트에 실제 쓰인 값). `shadow/color/ink-8`/`ink-16`(소프트 그림자 전용, rgba(28,31,33,...))은 두 문서 모두 원문에 그 rgba를 그대로 명시하고 있어 손대지 않음 — 하드 보더/텍스트용 ink와 소프트 그림자용 ink는 이제 미세하게 다른 두 값이며 의도적으로 분리 유지.

**추가 정정(0-1절, design-qa 감사)**: `color/ink/800`(#1C1F21, alpha=1) 신규 원시값 추가 — Row Action Button(`260:95`) Neutral 보더 전용, `color/ink/900`(#1A1A1A)과 별개 값. 우연히 `shadow/color/ink-8`/`ink-16`의 rgb 성분과 같은 rgb(28,31,33)이지만 이 둘은 alpha가 달라(그림자는 반투명, 이건 alpha=1 하드 보더) 별도 primitive로 유지한다.

**신규 카테고리 색 원시값** (CatBadge 팔레트, main 테이블에서 실측):
- `color/blue/100`(#E0F0FF) `color/blue/500`(#4A90D9) `color/blue/900`(#1A4C88) — 친구
- `color/coral/100`(#FFE4E8) `color/coral/900`(#A8003B) — 가족 (보더는 기존 coral/500 재사용)
- `color/purple/100`(#EDE0FF) `color/purple/500`(#9B72CF) `color/purple/900`(#4B0D9C) — 기타
- `color/mint/100`(#D8FFF5) `color/teal/900`(#0A4F49) — 회사 (보더는 기존 teal/500 재사용)

**TypeSelector 전용 레거시 원시값** (편집 모달에서 실측, CatBadge와 별개 — 2절 결정 참고):
`color/green/500`(#27AE60) `color/orange/100`(#FFF3E0) `color/orange/500`(#E6800A)

**TypeSelector 전용 추가 원시값(0-1절, design-qa 감사 후 정정)**: `color/gray/300`(#CCCCCC, 미선택 칩 보더 실측값) `color/orange/900`(#7A3D00, 회사 선택 텍스트 실측값) — 기존 `color/gray/450`(#888, 텍스트용)·`color/orange/500`(#E6800A, 보더/닷용) 토큰과 혼동해 재사용되던 것을 분리.

**뮤트 텍스트 원시값** (main 테이블 실측 — 전화번호 #555/주소 #777/보조 라벨 #888):
`color/gray/450`(#888888) `color/gray/500`(#777777) `color/gray/650`(#555555)

**하드 그림자 전용**: `shadow/color/ink-solid`(#1a1a1a, alpha=1 — 기존 ink-8/ink-16과 별개, 블러 없는 순수 오프셋 그림자용) `shadow/offset/hard-1`(1) `shadow/offset/hard-2`(2) `shadow/offset/hard-6`(6) `shadow/blur/none`(0) — Elevation 컬렉션(`VariableCollectionId:114:4`, mode `114:0`)에 위치.

**Radius/Border 신규 스텝** (Spacing 컬렉션 `VariableCollectionId:95:25`, mode `95:2`): `radius/none`(0) `radius/6`(6) `radius/10`(10) `border/hairline`(1, scope STROKE_FLOAT) `border/base`(2, scope STROKE_FLOAT) `border/heavy`(3, scope STROKE_FLOAT).

### 1-2. Semantic Colors (`VariableCollectionId:95:16`, mode `95:1`)

카테고리 팔레트(CatBadge 정식 채택 — 2절 참고): `color/category/friend-bg/-border/-text` `color/category/family-bg/-border/-text` `color/category/other-bg/-border/-text` `color/category/company-bg/-border/-text` (각 bg=FRAME_FILL/SHAPE_FILL, border=STROKE_COLOR, text=TEXT_FILL).

뮤트 텍스트 역할: `color/text-muted-strong`(→gray/650 #555, 전화번호) `color/text-muted`(→gray/500 #777, 주소) `color/text-muted-subtle`(→gray/450 #888, 마이크로 라벨/TypeSelector 미선택 텍스트) — **⚠ WCAG 검증 결과, 아래 3절 대비 계산 참고: muted-strong만 PASS, muted/muted-subtle는 원본 확정 디자인에 이미 내재된 미달값(→7-1절에서 RESOLVED로 종결, 사용자 확정)**.

기타: `color/border-neutral`(→ink, 취소/로그아웃류 아웃라인 버튼 보더) `color/background-success`(→mint/100, 토스트 성공) `color/background-error`(→coral/100, 배너 에러).

### 1-3. Component Tokens (`VariableCollectionId:97:2`, mode `97:0`)

기존 재사용(변경 없음): `component/button-bg-primary`(teal) `component/button-bg-danger`(coral) `component/button-bg-amber`(amber) — 이번 확정 디자인의 NeoBtn/Button Style=Teal/Coral/Amber에 그대로 재사용, 신규 선언 없음.

신규: `component/button-border-neutral`(→ink/900, NeoBtn/Button Neutral 스타일 2px 아웃라인 보더) `component/typeselector-unselected-text`(→gray/450 #888) `component/typeselector-family-selected-bg`(→green/500) `component/typeselector-company-selected-bg`(→orange/100) `component/typeselector-company-selected-accent`(→orange/500, 회사 선택 보더/닷 전용).

**신규(0-1절, design-qa 감사 후 정정)**: `component/typeselector-unselected-border`(→gray/300 #CCCCCC, TypeSelector 미선택 칩 4개 + "기타/선택" 칩 보더 전용, scope STROKE_COLOR) `component/typeselector-company-selected-text`(→orange/900 #7A3D00, TypeSelector "회사/선택" 텍스트 전용, scope TEXT_FILL) `component/row-action-button-border-neutral`(→ink/800 #1C1F21, Row Action Button Neutral 보더 전용, scope STROKE_COLOR — `component/button-border-neutral`과는 별개 값·별개 컴포넌트).

### 1-4. Effect Styles

**하드 "스티커" 그림자(신규, neo-brutalist)** — 블러 없음, `drop-shadow(Npx Npx 0px ink)`, 색=`shadow/color/ink-solid`, offsetX=offsetY=해당 오프셋 변수, radius=`shadow/blur/none`, spread=`shadow/spread/none`:
- `Shadow/Hard-1` — count pill(비활성)
- `Shadow/Hard-2` — 주요 CTA 버튼(검색/전체/추가/로그인/가입하기/저장하기/삭제하기), 활성 사이드바 nav, 모달 닫기(X) 버튼
- `Shadow/Hard-6` — 모달 카드, 인증 카드(Join/login) 전체

**소프트 블러 그림자(기존 재사용)** — `Elevation/Raised`(color=ink-8, offsetY=2, blur=8, spread=0 = `0px 2px 8px rgba(28,31,33,0.08)`) — Toast(성공/에러 배너) 전용으로 실사용 시작. **하드/소프트를 반드시 별개 토큰으로 유지** — 하나로 합치지 않는다.

### 1-5. Text Styles (신규 10종, 확정 디자인 5단 위계 그대로)

`Wordmark/Logo`(Baloo 2 ExtraBold 22, tracking -0.55) `Heading/Page`(Noto Sans KR Black 18, tracking -0.4) `Heading/Modal`(Noto Sans KR Black 16, tracking 0) `Label/Micro`(Inter Black 9, tracking 1) `Label/CountNumber`(Inter Black 12) `Label/Badge`(Inter Semi Bold 11, tracking 0.0645) `Body/Button`(Noto Sans KR Bold 14) `Body/Banner`(Noto Sans KR Medium 13) `Body/Regular`(Noto Sans KR Regular 14) `Body/Caption`(Noto Sans KR Regular 11).

세 폰트 패밀리(Baloo 2/Inter/Noto Sans KR) 역할 분리를 그대로 유지 — 텍스트 스타일 하나가 한 역할만 담당한다.

**참고**: Table Row Action("수정"/"삭제")의 10px 텍스트는 위 10종 텍스트 스타일 어디에도 해당하지 않는 컴포넌트 로컬 fontSize(직접 지정, 스타일 미바인딩)다 — 0-1절 정정으로 13px→10px 직접 수정.

## 2. TypeSelector vs CatBadge 색 불일치 — 결정 및 근거

**결정: CatBadge 팔레트를 이 시스템의 정식(canonical) 카테고리 색으로 채택한다.** TypeSelector(편집 모달 `248:8103`의 "종류" 칩)는 원본 확정 프레임에 실제로 존재하는 별도 팔레트를 그대로 재현하되, `component/typeselector-*` 전용 컴포넌트 토큰으로 격리해 CatBadge와 절대 혼용하지 않는다.

**근거**:
1. CatBadge는 main 목록 화면(가장 트래픽이 높은 주 화면)에서 4개 카테고리 전부에 "연한 배경+진한 보더/닷+더 진한 텍스트"라는 하나의 명확한 공식으로 일관되게 적용된 시스템이다.
2. TypeSelector는 실측 결과 미선택 텍스트가 카테고리 무관 전부 회색(#888)이고, 선택 시 accent도 카테고리별 논리가 불명확하다(가족=초록, 기타=미선택과 동일한 회색이라 사실상 변화 없음, 회사=주황) — CatBadge처럼 카테고리 정체성을 일관되게 반영하지 않는다.
3. 원본 확정 프레임(`248:8103`)은 절대 수정하지 않는다는 규칙에 따라 TypeSelector의 실제 관찰값은 그대로 컴포넌트화했다. **친구/기타 선택 상태의 정확한 accent는 이번 확정 프레임 인스턴스(회사만 선택된 상태)에서 직접 관찰되지 않았다** — 친구 선택 상태는 CatBadge 친구 색을 재사용해 대체했고(신규 색 발명 아님, 이미 확정된 시스템 내 재사용), 기타 선택 상태는 미선택과 동일하게(원본의 특성 그대로) 처리했다.
4. **향후 신규 화면 설계 시 권장**: CatBadge 팔레트를 우선 사용한다. TypeSelector 전용 팔레트는 이 특정 컴포넌트의 원본 재현에만 한정한다.

## 3. WCAG 대비 계산 (이번 라운드 신규 값 전수 검증)

- CatBadge 4종: bg/text 조합 전부 "연한 배경+짙은 텍스트" 공식이라 7:1 이상 여유 있게 PASS(예: friend #1A4C88 on #E0F0FF).
- NeoBtn/Button Style=Amber/Teal/Coral + ink 텍스트: 기존 "브랜드색 배경 위 텍스트=ink 고정" 규칙 재사용, 기존 검증된 5.3~11:1 범위 그대로 PASS(신규 계산 불필요, 동일 팔레트·동일 규칙 재적용).
- NeoBtn/Button Style=Neutral(흰 배경+ink 텍스트): 21:1 PASS.
- Toast Success(#D8FFF5 bg)/Error(#FFE4E8 bg) + ink(#1a1a1a) 텍스트: 각각 15.8:1 / 14.5:1 PASS(밝은 배경+ink 조합, 전 계산식 재사용 범위).
- **⚠ 뮤트 텍스트 3종 — 흰 배경 위 대비 직접 계산(WCAG 2.1 상대휘도 공식)**:
  - `color/text-muted-strong`(#555555): **7.45:1 PASS** (전화번호 텍스트)
  - `color/text-muted`(#777777): **4.46:1 — AA 4.5:1 기준 근소하게 미달** (주소 텍스트)
  - `color/text-muted-subtle`(#888888): **3.55:1 — AA 4.5:1 기준 미달** (마이크로 라벨/TypeSelector 미선택 텍스트, 9~11px 소형 텍스트라 큰 텍스트 예외(3:1)도 적용 불가)
  - **이 두 값은 사용자의 확정 원본 프레임에 이미 실측된 값이다. → RESOLVED(7-1절 참고)**: 사용자가 "이번 프로젝트에 한해 무시하고 원본 그대로 유지"하기로 명시적으로 확인·결정했다(더 이상 별도 보고나 원본 색상 변경 대기 상태가 아니다) — design-systems가 임의로 값을 진하게 바꾸지 않았고, 이번 결정도 원본 프레임 자체는 전혀 수정하지 않았다.
- **TypeSelector "회사/선택" 텍스트**(0-1절 정정값 #7A3D00) on 배경 `#FFF3E0`(orange/100): **약 7.9:1 PASS** — 원본 실측값 그대로 채택, 대비 문제 없음.

## 4. Icons (`96:7`)

**기존 8종 유지**(변경 없음): `Icon/Search` `Icon/Add` `Icon/Edit` `Icon/Delete` `Icon/Category` `Icon/Logout` `Icon/Alert` `Icon/User` — 확정 디자인에서도 `Icon/Alert`(토스트/배너)와 `Icon/User`(아바타)가 그대로 재사용됨을 확인. **(2026-07-14 문서 동기화 재확인)** graphic-designer가 "Icons" 페이지를 직접 재실측(`use_figma`)한 결과 8종 전부 strokeWeight 3px 균일로 원상태 그대로다 — 상세는 `docs/design/graphic-assets.md` 참고.

**신규 10종** (`Pixel/*` 네임스페이스, 확정 프레임에서 비파괴적으로 clone 후 `createComponentFromNode`로 컴포넌트화 — 원본은 전혀 수정하지 않음): `Pixel/Star`(12px, 로고 심볼 내부) `Pixel/Search`(15px) `Pixel/Plus`(9px) `Pixel/Logout`(12px) `Pixel/Edit`(14px) `Pixel/Delete`(14px) `Pixel/Close`(10px, 모달 닫기) `Pixel/Warning`(16px, 삭제 경고) `Pixel/NoResult`(40x44, 빈 검색결과 그래픽 — 신규 마스코트가 아니라 기능 아이콘 언어의 확장) `Pixel/Eye`(14x10, login 비밀번호 표시/숨김 토글 — 0-2절, 처음 9종 추출 라운드에서 누락됐다가 이번에 마저 등록).

## 5. 컴포넌트 (확정 디자인 기준, 신규 등록)

| 컴포넌트 | 페이지 | ComponentSet ID | Variant |
|---|---|---|---|
| CatBadge | Badge `102:3` | `256:17` | Category=Friend/Family/Other/Company (4). CatBadge 팔레트(2절) 바인딩. |
| TypeSelector | Badge `102:3` | `257:28` | Category × State=Selected/Unselected (8). 레거시 팔레트, 2절 결정 참고. **0-1절 정정 완료**: 미선택 보더=`component/typeselector-unselected-border`(#CCCCCC), 회사/선택 텍스트=`component/typeselector-company-selected-text`(#7A3D00) — 원본과 hex 일치 재확인됨. **9-3절**: Focus=No/Yes 축 추가로 16 variant로 확장.|
| Count Pill | Sidebar Nav Item `103:92` | `258:16` | State=Active(흰 배경, 그림자 없음)/Inactive(앰버 배경, Shadow/Hard-1). |
| Sidebar Nav Item | Sidebar Nav Item `103:92` | `258:29` | State=Active/Inactive(앰버+radius10+Shadow/Hard-2+흰 CountPill / 투명+그림자 없음+앰버 CountPill) × **Focus=No/Yes**(9-3절 추가, 총 4 variant). **9-5절 정정**: Inactive+Focus=Yes(`287:17`)는 배경이 투명이라 다른 7쌍과 달리 DROP_SHADOW가 아닌 3px ink OUTSIDE 스트로크로 링을 구현한다(시각 결과는 동일). |
| NeoBtn | Button `97:8` | `259:126` | Style=Amber/Teal/Coral/Neutral × Size=Default(36px)/Compact(25px, 헤더 로그아웃) × **State=Default/Hover/Press/Focus/Disabled/Loading**(9-2절 추가) = 48. main 검색·필터·추가행, 사이드바 카테고리 추가, 헤더 로그아웃. **9-5절 정정**: Disabled 8종 모두 대비 재계산 완료. |
| Button | Button `97:8` | `259:609` | Style=Amber/Coral/Neutral × **State=Default/Hover/Press/Focus/Disabled/Loading**(9-2절 추가) = 18. 모달 저장·삭제·취소, 인증 카드 CTA 공용. Amber/Coral=Shadow/Hard-2, Neutral=그림자 없음(Default 기준). **9-5절 정정**: Disabled 3종 대비 재계산 완료. |
| Icon Button | Button `97:8` | `259:613` | Type=Close × **State=Default/Hover/Press/Focus/Disabled**(9-2절 추가, Loading 제외) = 5. 모달 닫기 X, 28x28, Shadow/Hard-2(Default 기준). **9-5절 정정**: Disabled 1종 대비 재계산 완료. |
| Row Action Button | Table Row `103:3` | `260:95` | Style=Neutral(Pixel/Edit)/Danger(Pixel/Delete) × **State=Default/Hover/Press/Focus/Disabled**(9-2절 추가, Loading 제외) = 10. 사이드바 "카테고리 관리" 목록 전용, 28x22 아이콘 전용, 그림자 없음. **0-1절 정정 완료**: Neutral 보더=`component/row-action-button-border-neutral`(#1C1F21, ink/900과 별개) — 원본과 hex 일치 재확인됨. **9-5절 정정**: Disabled 2종 대비 재계산 완료. |
| Table Row Action | Table Row `103:3` | `260:100` | Style=Neutral(수정, teal)/Danger(삭제, coral) × **State=Default/Hover/Press/Focus/Disabled**(9-2절 추가, Loading 제외) = 10. main 테이블 행 텍스트 아웃라인 버튼, 41x25, 그림자 없음. **0-1절 정정 완료**: 텍스트 10px(기존 13px 오류 정정) — 원본과 일치 재확인됨. **9-5절 정정**: Disabled 2종은 배경 대비는 해소했으나 텍스트색 자체가 7-1절 §3의 기존 수용된 미달 이슈를 그대로 승계한다(신규 회귀 아님, 상세는 9-5절). |
| NeoInput | Input `100:2` | `288:12`(신규, 9-3절) | Focus=No(원 `261:10`, 그대로 보존)/Yes(신규). main 검색·필터 입력창, radius10, 브래킷 없음. |
| CornerInput | Input `100:2` | `288:27`(신규, 9-3절) | Focus=No(원 `261:12`, 그대로 보존)/Yes(신규). 인증 폼/편집 모달 입력창. **0-3절 정정 완료(2026-07-14)**: radius0 + 2px ink 사각 보더만(모서리 8×8 ㄱ자 `CornerBracket` 4개는 확정 프레임에 없던 임의 추가였음이 확인되어 Focus=No/Yes 양쪽에서 전부 제거). 베이스 폭 392px(main-수정 모달 `248:8103` 기준) 유지, 로그인/가입(352px 실측)은 별도 variant 없이 인스턴스 리사이즈로 대응 — description에 명시. |
| NeoSelect | Select `101:3` | `261:660` | 단일. main 필터 드롭다운, radius10. |
| Card | **Card**(신규 페이지) | `262:15` | Type=Modal(상단 앰버 스트립만)/Auth(상단 앰버+하단 틸 샌드위치) = 2. 2px ink 보더+radius8+Shadow/Hard-6. Content 영역은 화면 조립 시 채움(쉘까지만 등록). |
| Toast | Alert `104:2` | `263:53` | Type=Success(민트)/Error(코랄 틴트) = 2. `Elevation/Raised`(소프트) 사용. **플로팅 오버레이 패턴**(11절) — 하단 콘텐츠를 밀어내지 않는 absolute 배치를 컴포넌트 설명에 명시. |
| Logo | **Logo**(신규 페이지) | `263:692` | Background=Teal(흰 워드마크)/White(ink 워드마크) = 2. 심볼(코랄 원+2px ink+내부 흰 Pixel/Star 12px)+워드마크(Baloo 2 ExtraBold 22, gap10). |
| Avatar | Avatar `104:127` | `104:131`(기존 재사용) | 변경 없음 — 기존 컴포넌트(teal 배경+Icon/User)가 확정 디자인과 정확히 일치함을 확인, 신규 작업 불필요. |

## 6. 알림/토스트 오버레이 — 컴포넌트 설명에 명시된 배치 규칙

`Toast`(Type=Success/Error) 컴포넌트 설명에 "플로팅 오버레이" 성격을 명시했다: main-알림창/login-알림창은 각각 main/login 화면 위에 최상위 z-index로 절대 위치(absolute)로 뜨며 하단 콘텐츠를 밀어내지 않는다(레이아웃 버그 아님, 사용자 확정 의도). ui-designer가 화면에 조립할 때 이 배치 방식을 그대로 유지해야 한다. 자동 소멸 타이밍/애니메이션은 interaction-designer·motion-designer 몫이며 이 컴포넌트는 정적 배치·스타일까지만 규정한다.

## 7. 알려진 갭 / 후속 필요 사항

### 7-1. 종결된 결정 (RESOLVED) — 사용자 확정, 이번 프로젝트 범위에서 개선하지 않음

design-qa 감사에서 발견되어 이전에는 이 절에 열린 이슈(TODO)로 기록되어 있었으나, 사용자가 아래 5건을 **"이번 프로젝트에 한해 무시하고 원본 그대로 유지"**하기로 명시적으로 결정했다. 원본 확정 프레임(8개, `248:11689` 하위)은 이 결정 과정에서도 전혀 손대지 않았다 — **문서 상태만 TODO → RESOLVED로 갱신**한 것이며 어떤 컴포넌트/토큰/원본 프레임 값도 변경하지 않았다.

1. **뮤트 텍스트 WCAG 대비 미달 2건**(3절 참고) — `color/text-muted`(#777777, 4.46:1, 주소 텍스트), `color/text-muted-subtle`(#888888, 3.55:1, 마이크로 라벨/TypeSelector 미선택 텍스트). AA 4.5:1 기준 미달. **사용자 확인 후 이번 프로젝트 범위에서 개선하지 않기로 결정 — 원본 확정 프레임 값 그대로 최종.**
2. **사이드바 비활성 nav 텍스트 대비 미달**, **사이드바 라벨 대비 미달**. **사용자 확인 후 이번 프로젝트 범위에서 개선하지 않기로 결정 — 원본 확정 프레임 값 그대로 최종.**
3. **Table Row Action(`260:100`) 텍스트 대비 미달**(수정/삭제 라벨). **사용자 확인 후 이번 프로젝트 범위에서 개선하지 않기로 결정 — 원본 확정 프레임 값 그대로 최종.** (9-5절: Disabled variant의 텍스트 대비도 이 미해결 기준선을 그대로 승계함 — 별개 신규 결함 아님.)
4. **터치 타겟 44×44px 미달 다수** — Row Action Button(`260:95`), Table Row Action(`260:100`), 헤더 로그아웃 NeoBtn, 검색/전체 NeoBtn, 사이드바 nav, TypeSelector 칩(`257:28`). **사용자 확인 후 이번 프로젝트 범위에서 개선하지 않기로 결정 — 원본 확정 프레임 값 그대로 최종.**
5. **placeholder 텍스트 대비 미달**. **사용자 확인 후 이번 프로젝트 범위에서 개선하지 않기로 결정 — 원본 확정 프레임 값 그대로 최종.**

### 7-2. 열린 이슈 (TODO, 미해결 — 위 5건과는 별개)

- **TypeSelector 친구/기타 선택 상태 accent 미관찰** — 위 5건과는 별개 이슈, 종결되지 않음. 2절 결정에 따라 대체 처리(친구=CatBadge 재사용, 기타=변화 없음). 원본에서 해당 상태가 실제로 다르게 디자인되어 있다면 재확인 필요.
- **Card 컴포넌트는 쉘까지만** — 실제 필드/버튼 조합(편집 모달, 삭제 모달, Join, login)은 ui-designer가 SCREENS 단계에서 Card+CornerInput+TypeSelector+Button 등을 조립해 완성한다.
- **Table Header, EmptyState 조립체는 컴포넌트화하지 않음** — 화면 레이아웃 조립의 영역이라 판단해 범위에서 제외(Pixel/NoResult 아이콘만 등록, 빈 상태 레이아웃 자체는 ui-designer 담당).
- ~~**Button Disabled variant 없음**~~ — **RESOLVED(interaction-designer, 2026-07-14)**: 9절 "인터랙션 상태" 라운드에서 NeoBtn/Button을 포함한 버튼류 5개 컴포넌트에 Hover/Press/Focus/Disabled(+해당 시 Loading)를 정식 추가했다. 원본 8개 확정 프레임에는 없는 값이므로 프레임을 다시 관찰한 것이 아니라 브랜드 톤(하드 스티커 그림자, ink 아웃라인, teal/coral/amber 팔레트)을 확장하는 공식으로 새로 설계했다 — 상세는 9절 참고.
- **Legacy Table Row(`103:7`) 컴포넌트 해제 보류** — 0-3절에서 발견: 인스턴스 7개가 아직 파일 안에 남아 있어(Table Row 페이지 1개 + 파일럿 페이지 `❌ 폐기 —` 라벨 붙은 구 화면 6개) 컴포넌트 해제(COMPONENT_SET→FRAME 전환)를 보류했다. 그 인스턴스들이 실제로 더 이상 필요 없다고 확인되면(예: `❌ 폐기 —` 프레임 자체를 정리하는 별도 작업), 그 이후에 이 컴포넌트도 동일한 방식으로 해제할 수 있다 — design-pl/사용자 확인 필요.

## 8. Legacy — B-2 파일럿 기반 컴포넌트 (참고용, 더 이상 정식 소스 아님)

아래는 이전 B-2 파일럿 라운드에서 추출한 컴포넌트 인벤토리다. `docs/design/confirmed/user-confirmed-final-design.md`에 따라 8개 사용자 확정 프레임이 이를 완전히 대체했으므로 **더 이상 정식 소스가 아니다**. 삭제하지 않고 이력으로 보존하며, 이름이 겹쳤던 3개(`Button`/`Row Action Button`/`Sidebar Nav Item`)에 이어 이번에 나머지 5개(`Input`/`Select`/`Badge`/`Table Row`/`Alert`)도 `[Legacy B-2] ` 접두사로 리네임해 위 5절의 신규 컴포넌트와 구분했다(내용은 전혀 건드리지 않음, 이름만 변경). Avatar(`104:131`)만 확정 디자인과 완전히 일치해 현재도 유효하므로 접두사 없이 그대로 둔다.

**(갱신, 0-3절 — 2026-07-14) 컴포넌트 등록 해제(폐기) 진행**: 사용자 요청으로 아래 9개 중 Avatar를 제외한 8개를 컴포넌트 등록 해제 대상으로 검토했다. 인스턴스가 없는 7개는 COMPONENT/COMPONENT_SET → FRAME으로 전환 완료(더 이상 Assets/Insert 패널에 노출되지 않음, 이름/시각 내용은 그대로 유지). Table Row는 인스턴스 7개가 남아 있어 해제하지 않고 컴포넌트 상태 그대로 보류했다. 상세는 아래 표의 "상태" 컬럼 참고.

### 페이지 순서 (전체 파일)

| idx | pageId | name |
|---|---|---|
| 0 | `15:2` | 레퍼런스 |
| 1 | `52:2` | Brand Guide |
| 2 | `95:2` | Colors |
| 3 | `95:3` | Typography |
| 4 | `95:4` | Spacing |
| 5 | `116:5` | Elevation |
| 6 | `96:7` | Icons |
| 7 | `34:2` | 브랜드 컨셉 Concepts |
| 8 | `97:8` | Button |
| 9 | `100:2` | Input |
| 10 | `101:3` | Select |
| 11 | `102:3` | Badge |
| 12 | `103:3` | Table Row |
| 13 | `103:92` | Sidebar Nav Item |
| 14 | `104:2` | Alert |
| 15 | `104:127` | Avatar |
| 16 | `222:524` | 파일럿(SCREENS) |
| — | `262:5` | **Card**(이번 라운드 신규) |
| — | `263:665` | **Logo**(이번 라운드 신규) |

**[알려진 이슈, 이전 라운드부터]** 이 표와 실제 파일의 전체 페이지 개수가 어긋나 있다(예: `34:2`가 `52:2`보다 먼저 오고, 표에 없는 `0:1`/`15:3` 페이지가 파일 끝에 존재). 이번 라운드 범위(토큰/컴포넌트 추출)에서는 페이지 순서 재정렬을 다루지 않았다 — design-pl에게 별도 보고, 후속 라운드에서 전체 표 재조사·정정 필요. (참고: 실제 페이지 목록 재조회 결과 `15:3`="UI-design ", `242:2330`="old-사용하지말것" 페이지도 존재함 — 0-3절 인스턴스 전수 검색 시 확인.)

**추가(2026-07-14, graphic-designer 문서 동기화)**: `90:2`(Graphic Assets) 페이지는 사용자가 직접 삭제해 더 이상 파일에 존재하지 않는다 — `use_figma`로 전체 페이지를 재조회한 결과 21개 페이지 중 `90:2`가 없음을 확인했고, 위 표에서 해당 행을 제거했다(기존 idx 2~17이 한 칸씩 당겨짐). 상세는 `docs/design/graphic-assets.md` 참고.

### Legacy 변수 컬렉션 요약

- **Primitives**: `color/teal/500` `color/coral/500` `color/amber/500` `color/ink/900`(1절에서 값 정정됨) `color/gray/0,50,100,200,400,600` `color/mint/tint` `color/border-hairline-value` `shadow/color/ink-8,ink-16` `color/teal/700`
- **Semantic Colors**: `color/background` `color/surface` `color/text-primary` `color/text-secondary` `color/border` `color/success` `color/error` `color/warning` `color/background-info` `color/border-ink` `color/text-accent` `color/border-hairline` `color/text-inverse`(teal·coral 배경 위 Display급 텍스트 전용, amber 금지 — 화면 미적용)
- **Spacing**: `spacing/1,1-75,2,2-25,2-5,3,4,6,8` `radius/sm,xs,md,lg,full`
- **Elevation(legacy)**: `shadow/blur/sm,lg` `shadow/offset-y/sm,lg` `shadow/spread/none`, Effect Styles `Elevation/Raised`(이번 라운드부터 Toast에 실사용 시작) `Elevation/Overlay`(미바인딩)
- **Component Tokens(legacy)**: `component/button-bg-primary,secondary,border-secondary,bg-disabled,text-disabled,bg-danger,bg-amber` `component/select-border-open` `component/badge-bg-tag` `component/table-row-border` `component/navitem-bg-active` `component/avatar-bg` — **이번 라운드에서 button-bg-primary/danger/amber 3개는 확정 디자인 NeoBtn/Button에도 그대로 재사용됨(1-3절 참고), 나머지는 legacy 전용으로 유지**.

### Legacy 컴포넌트 (`[Legacy B-2]` 리네임됨)

| 컴포넌트 | 페이지 | ID | 비고 | 상태(0-3절, 2026-07-14) |
|---|---|---|---|---|
| [Legacy B-2] Button | `97:8` | `97:47` | Style×Content×State×Size = 32 | **폐기(컴포넌트 해제 완료, 2026-07-14)** — FRAME `314:843`로 전환, 인스턴스 0개 확인 |
| [Legacy B-2] Input | `100:2` | `100:46` | State×Size = 4, 검색 아이콘 슬롯 포함 | **폐기(컴포넌트 해제 완료, 2026-07-14)** — FRAME `314:879`로 전환, 인스턴스 0개 확인 |
| [Legacy B-2] Select | `101:3` | `101:64` | State = 3 | **폐기(컴포넌트 해제 완료, 2026-07-14)** — FRAME `314:893`로 전환, 인스턴스 0개 확인 |
| [Legacy B-2] Badge | `102:3` | `102:65` | Type×State = 4 | **폐기(컴포넌트 해제 완료, 2026-07-14)** — FRAME `314:897`로 전환, 인스턴스 0개 확인 |
| [Legacy B-2] Table Row | `103:3` | `103:7` | variant 없음 | **보류 — 인스턴스 존재 (7개: Table Row 페이지 `103:77` 1개 + 파일럿 페이지 `❌ 폐기 —` 프레임 안 `110:220`/`110:234`/`110:248`/`110:262`/`110:276`/`110:290` 6개)** — 컴포넌트 상태 그대로 유지, 미해제 |
| [Legacy B-2] Row Action Button | `103:3` | `166:421` | Style = 2 | **폐기(컴포넌트 해제 완료, 2026-07-14)** — FRAME `314:319`로 전환, 인스턴스 0개 확인 |
| [Legacy B-2] Sidebar Nav Item | `103:92` | `103:106` | State = 2 | **폐기(컴포넌트 해제 완료, 2026-07-14)** — FRAME `314:876`로 전환, 인스턴스 0개 확인 |
| [Legacy B-2] Alert | `104:2` | `104:108` | Type = 2 | **폐기(컴포넌트 해제 완료, 2026-07-14)** — FRAME `314:902`로 전환, 인스턴스 0개 확인 |
| Avatar | `104:127` | `104:131` | **확정 디자인에서도 그대로 재사용 — legacy이자 현재 유효, 접두사 없음(유일한 예외)** | 대상 아님(해제 검토 제외) |

### Legacy 알려진 갭 (미해결 상태 그대로 이월)

- Button Disabled variant 6종 WCAG 대비 미달(1.93:1) — legacy 컴포넌트 한정 이슈, 신규 Button/NeoBtn에는 Disabled variant 자체가 없음(7절 참고). (0-3절: 이 legacy Button은 이제 FRAME `314:843`로 전환되어 컴포넌트가 아니므로 이 갭은 사실상 봉인됨.)
- Heading/Label 텍스트 스타일 토큰, Table Header 컴포넌트 없음 — 여전히 미해결(신규 텍스트 스타일은 1-5절에 별도 등록됨).
- radius/lg(12)가 이전 확정 문서의 "10px" 값과 불일치 — 이번 라운드 `radius/10` 신규 추가로 해소됨(신규 컴포넌트는 radius/10 사용).
- 화면상 버튼 색 스왑 문제 — legacy 파일럿 화면(`222:524`) 한정 이슈, 확정 디자인 8개 프레임에는 해당 없음.

## 9. 인터랙션 상태 (Hover/Press/Focus/Disabled/Loading) — interaction-designer 추가 (2026-07-14)

이 절은 interaction-designer가 추가한 상태·트리거 정의다. 8개 사용자 확정 프레임은 정적 스크린샷이라 이 상태들이 원본에 없다 — 아래 값은 브랜드 톤(1-4절 하드 스티커 그림자, ink 보더, teal/coral/amber 팔레트)을 확장해 새로 설계한 것이며, 원본 프레임(`248:11689` 하위 8개)은 이번에도 전혀 수정하지 않았다(컴포넌트 쪽에서만 작업). `docs/design/brand-guide.md`(하드 스티커 그림자 5절, 보더/Radius 4절, 팔레트 2절)와 `.claude/agent-memory/ux-designer.md`의 접근성 메모(터치 타겟·색상 단독 구분 금지)를 참고해 설계했다.

### 9-1. 공통 규칙 (모든 컴포넌트에 동일 적용)

- **State 속성**: 각 컴포넌트 세트에 기존 Style/Size/Category 등 속성은 그대로 두고, 새 변형 속성 `State`(값: Default/Hover/Press/Focus/Disabled/[Loading])를 추가했다. 기존 Default 변형은 시각적으로 전혀 바꾸지 않았고, Figma 변형 속성 일관성(모든 variant가 동일한 속성 키 집합을 가져야 함)을 위해 이름에 `State=Default`만 추가로 붙였다(순수 네이밍 변경, 색상/크기/그림자 등 값은 무수정).
- **Hover** — 배경을 ink(#1A1A1A) 쪽으로 소폭 블렌드(`mix(base, ink, t) = base + (ink-base)×t`), 그림자/보더는 원본 그대로 유지("그림자는 유지"). 브랜드색 배경(Amber/Teal/Coral)은 t=12%, 흰 배경+아웃라인류(Neutral, Icon Button)는 t=6%(색이 옅어 과하게 어두워지지 않도록 절반 비율).
- **Press** — Hover보다 진하게 블렌드(브랜드색 t=24%, 흰 배경류 t=12%) + 하드 그림자 완전 제거(`effects=[]`)로 "눌린" 느낌을 표현. 브리프가 제시한 두 옵션("2px 또는 0px로 축소") 중 완전 제거(0px)를 채택 — 원본 하드 스티커 그림자가 블러 없는 순수 오프셋이라 제거만으로도 "짜부라진" 느낌이 명확하고, 스티커 아래 배경을 재계산하는 오프셋 축소보다 구현이 단순하다.
- **Focus** — 기존 효과에 ink 색 "포커스 링"을 추가: `DROP_SHADOW`, offset (0,0), blur(radius) 0, **spread 3px**, color `#1A1A1A` 100% opacity. 블러 없는 하드 링이라 브랜드의 "블러 없는 스티커 그림자" 톤과 통일된다. 배경/보더/그림자는 Default와 동일하게 유지하고 링만 추가하므로 키보드 탭 포커스가 색상 시스템을 흔들지 않는다. **모든 컴포넌트·모든 색상이 동일한 ink 링을 공유** — "예측 가능성" 원칙에 따라 포커스 인디케이터는 컴포넌트 색과 무관하게 항상 동일해야 사용자가 접근성 신호로 학습할 수 있다. **예외 1건(9-5절)**: Sidebar Nav Item Inactive+Focus=Yes(`287:17`)는 배경이 완전 투명이라 이 DROP_SHADOW 기법이 그대로 통하지 않아, 시각적으로 동일한 결과를 내는 3px ink OUTSIDE 스트로크로 구현을 대체했다 — 규칙의 "링 자체"는 동일하게 유지, 렌더링 기법만 이 한 변형에 한해 다르다.
- **Disabled** — **(9-5절에서 정정됨)** 컴포넌트 컨테이너 자체의 `opacity`는 1로 유지하고, ①배경 fill/보더 stroke의 **페인트 레벨 opacity만 0.5**로 낮춰 "흐려진 배경/보더"를 만들고 ②텍스트·아이콘 자식 노드의 opacity는 **0.85**로 살짝만 낮춘다. 배경/보더/텍스트 색상 값 자체는 바꾸지 않는다. Figma에서 프레임 opacity는 자식까지 곱연산으로 흐리게 하지만, 페인트(fill/stroke) 자체의 opacity 필드는 그 페인트 레이어에만 적용되고 자식에는 영향이 없다는 점을 이용해 "배경은 확실히 흐리게, 텍스트는 읽히게"를 분리했다(최초 도입했던 컨테이너 전체 균일 `opacity=0.45` 값은 design-qa 감사에서 WCAG 대비 미달 HIGH 결함으로 지적되어 이 값으로 교체됨 — 상세 계산·근거는 9-5절 참고). 커서(`not-allowed`)는 Figma 노드 속성이 아니므로 이 문서에 코드 구현 지침으로만 남긴다 — 실제 구현 시 disabled 버튼은 `cursor: not-allowed`와 `pointer-events` 처리로 클릭 자체를 막아 "오류를 인터랙션으로 예방"한다.
- **Loading**(버튼류 5개 중 NeoBtn·Button 2개만 해당 — 아래 9-2 표 참고) — `opacity=0.7`(Default의 1.0보다는 흐리게) + 그림자 제거(그라운드에 붙어 "진행 중"인 느낌). **텍스트/아이콘을 스피너로 바꾸거나 회전 애니메이션을 넣는 작업은 하지 않았다** — 실제 스피너/펄스 애니메이션 에셋과 움직임은 motion-designer의 몫이며, 이 상태는 그 애니메이션이 나중에 얹힐 수 있는 "정적인 컨테이너 톤"(흐려지고 그림자가 가라앉은 버튼)까지만 정의한다. 이중 제출 방지 목적(기존 레거시 Button 컴포넌트 설명에 있던 "이중 제출 방지(SCR-900)" 취지 계승)이라 실제 구현 시 Loading 상태에서는 클릭도 함께 막아야 한다. **Loading은 이번 design-qa 감사 대상이 아니었고 대비 재계산도 하지 않았다** — Disabled(0.5/0.85 분리)와 달리 컨테이너 균일 opacity 방식을 그대로 유지한다(진행 중 상태는 클릭 자체가 막혀 있어 텍스트 판독보다 "처리 중" 신호 전달이 우선이라는 기존 설계 의도를 유지).

### 9-2. 버튼류 5개 컴포넌트 — Hover/Press/Focus/Disabled(+Loading) 적용 현황

| 컴포넌트 | ComponentSet ID | 기존 축 | 추가 축 | 추가된 State | Loading 포함 여부 |
|---|---|---|---|---|---|
| NeoBtn | `259:126` | Style(4: Amber/Teal/Coral/Neutral)×Size(2: Default/Compact) | State | Hover/Press/Focus/Disabled/Loading | **O** — 검색/전체/추가/로그아웃 등 네트워크 호출 가능성이 있는 버튼 |
| Button | `259:609` | Style(3: Amber/Coral/Neutral) | State | Hover/Press/Focus/Disabled/Loading | **O** — 모달 저장/삭제, 인증 CTA(로그인/가입하기) 등 실제 제출 액션 |
| Icon Button | `259:613` | Type(1: Close) | State | Hover/Press/Focus/Disabled | X — 모달 닫기(X)는 클라이언트 사이드 즉시 액션, 제출 없음 |
| Row Action Button | `260:95` | Style(2: Neutral/Danger) | State | Hover/Press/Focus/Disabled | X — 카테고리 관리 연필/휴지통은 모달/리네임을 여는 트리거일 뿐 자체 제출 없음 |
| Table Row Action | `260:100` | Style(2: Neutral/Danger) | State | Hover/Press/Focus/Disabled | X — 수정/삭제 텍스트 버튼도 모달을 여는 트리거, 실제 제출은 모달 내부 Button이 담당 |

**Hover/Press 블렌드 비율 상세**:
- NeoBtn/Button 브랜드색(Amber/Teal/Coral): Hover 12% / Press 24%, ink로 블렌드.
- NeoBtn/Button/Icon Button Neutral(흰 배경+ink 아웃라인): Hover 6% / Press 12%, ink로 블렌드.
- Row Action Button: 자기 보더색(Neutral=ink/800 `#1C1F21`, Danger=coral `#FF5A76`) 쪽으로 흰 배경을 Hover 10% / Press 20% 블렌드(아이콘 버튼이 작아 톤 차이가 과하지 않도록 완만하게 설계).
- Table Row Action: 자기 보더/텍스트색(Neutral=teal `#17A398`, Danger=coral `#FF5A76`) 쪽으로 흰 배경을 Hover 12% / Press 24% 블렌드 — hover 시 배경에 옅은 색이 스며들어 "클릭 가능한 아웃라인 버튼"이라는 어포던스를 강화한다.

### 9-3. Focus 상태만 추가한 보조 컴포넌트 (필요 판단, 2026-07-14)

명백히 인터랙티브하지만 위 버튼류와 별개 상태 모델(토글/선택/텍스트입력)을 갖는 3개 컴포넌트는 접근성용 Focus 상태만 추가했다(Hover/Press/Disabled/Loading은 각 컴포넌트의 기존 상태 모델과 충돌하거나 이번 범위에서 불필요하다고 판단해 제외 — 아래 사유 참고):

| 컴포넌트 | ComponentSet ID | 기존 축 | 추가 축 | 비고 |
|---|---|---|---|---|
| Sidebar Nav Item | `258:29` | State=Active/Inactive | Focus=No/Yes | 기존 `State`에 값을 얹는 대신 직교하는 `Focus` 축을 신설 — Active/Inactive 각각에 포커스 링만 얹은 변형을 추가(총 4 variant). **9-5절**: Inactive+Focus=Yes(`287:17`)만 스트로크 기법으로 구현(사유는 9-5절). |
| TypeSelector | `257:28` | Category(4)×State=Selected/Unselected | Focus=No/Yes | 기존 8개 변형 각각에 `Focus=Yes` 짝을 추가(총 16 variant). 칩 자체 배경/텍스트는 무수정, 포커스 링만 추가. |
| NeoInput | `288:12`(신규 ComponentSet, 기존 `261:10`은 그 안의 `Focus=No` 변형으로 그대로 보존) | 단일 컴포넌트 | Focus=No/Yes | `figma.combineAsVariants`로 2-variant 세트로 승격. 기존 인스턴스는 동일 노드 ID(`261:10`)를 계속 참조하므로 화면상 깨지지 않는다. |
| CornerInput | `288:27`(신규 ComponentSet, 기존 `261:12`은 `Focus=No`) | 단일 컴포넌트 | Focus=No/Yes | 위와 동일한 방식(원본 `261:12` 보존, `Focus=Yes` 신규). **0-3절 정정**: 양쪽 variant에서 4모서리 `CornerBracket` 장식 제거 완료, 순수 2px ink 사각 보더만 유지. |

**Hover/Press/Disabled를 제외한 이유**: Sidebar Nav Item·TypeSelector는 색상 자체가 곧 "선택/미선택" 신호라 hover 시 별도 색 변화를 추가하면 선택 상태와 혼동될 위험이 있어, 이번 라운드에서는 손대지 않고 design-systems와 협의가 필요한 사안으로 남겼다. NeoInput/CornerInput은 값 입력 필드라 disabled/loading보다 focus(입력 가능 신호)가 압도적으로 우선순위가 높은 상태라 이번 라운드에서는 focus만 먼저 처리했다.

### 9-4. 알려진 갭 (후속 필요)

- Sidebar Nav Item/TypeSelector/NeoInput/CornerInput의 Hover/Press/Disabled 상태는 이번 라운드에서 다루지 않았다(9-3절 사유 참고) — design-pl/design-systems와 협의 후 필요 시 추가.
- Loading 상태의 실제 스피너/펄스 애니메이션(움직임)은 motion-designer 담당이다 — 이번에 만든 것은 정적인 "흐려지고 그림자가 가라앉은" 컨테이너 톤뿐이며, 그 위에 움직이는 인디케이터를 얹는 작업은 범위 밖이다.
- 포커스 링(spread 3px ink, 100% opacity / 9-5절 예외 1건은 3px 스트로크)은 원본 확정 디자인에 없던 완전 신규 값이라 정식 디자인 토큰(Variable)으로 등록하지 않고 컴포넌트 로컬 raw 값으로만 적용했다 — design-systems가 필요하다고 판단하면 `component/focus-ring-*` 토큰으로 정식 승격을 검토할 수 있다.
- Disabled 배경/보더 opacity(0.5)·텍스트/아이콘 opacity(0.85, 9-5절)도 마찬가지로 컴포넌트 로컬 raw 값이다 — design-systems가 필요하다고 판단하면 `component/disabled-*` 토큰으로 정식 승격을 검토할 수 있다.
- Table Row Action Disabled(9-5절)의 텍스트 대비는 7-1절 §3의 기존 수용된 미달을 그대로 승계해 3:1 미만이다 — 근본 해결은 7-1절 §3 자체(Default 상태 텍스트 색)를 바꿔야 하는데 이는 사용자가 이미 "이번 프로젝트 범위에서 개선하지 않기로" 확정한 영역이라 이번 정정 범위 밖이다.
- 화면 간 전환 애니메이션(로그인 성공→관리 화면 등 프로토타입 Smart Animate 연결)은 이번 라운드에서 다루지 않았다 — 컴포넌트 상태 정의가 선행 작업이라 이번엔 컴포넌트 레벨까지만 완료했고, 프로토타입 연결은 다음 라운드 대상이다.

### 9-5. design-qa 감사 후 정정 (2026-07-14 추가 라운드, 원본 8개 프레임은 이번에도 무수정)

design-qa가 인터랙션 상태 라운드(9절)에서 두 건의 HIGH 결함을 발견해 정정했다. 컴포넌트 쪽만 수정했고 원본 확정 프레임은 이번에도 손대지 않았다.

**결함 1 — Sidebar Nav Item Inactive+Focus=Yes(`287:17`) 포커스 링 미렌더링**

- **증상**: `get_screenshot` 바운딩박스 비교 결과 `287:17`이 Focus=No 변형과 완전히 동일한 173×40으로 렌더링되어(정상이라면 179×46), 포커스 링이 시각적으로 전혀 보이지 않았다.
- **1차 진단**: 노드의 `effects` 속성 자체는 `DROP_SHADOW offset(0,0) blur 0 spread 3 ink 100%`로 정확히 설정되어 있었다(287:14 Active+Focus=Yes와 동일한 파라미터). 파라미터는 맞는데 렌더링이 안 되는 원인을 추가로 조사했다.
- **근본 원인**: `287:17`은 Inactive 상태 스펙("투명 배경, 그림자 없음")대로 `fills=[]`(완전 투명)이다. Figma에서 프레임 노드의 DROP_SHADOW는 그 프레임 자신의 채워진(opaque) 실루엣을 기준으로 그림자 모양을 계산한다 — `fills`가 완전히 비어 있으면 그림자가 그려질 실루엣 자체가 없어 렌더링되지 않는다. 반면 `287:14`(Active)는 앰버 배경이 불투명하게 채워져 있어 같은 파라미터로도 정상적으로 링이 보인다.
- **1차 시도(기각)**: 배경에 opacity가 매우 낮은(0.02) 흰색 SOLID fill을 추가해 "그림자가 그려질 실루엣"만 확보하는 방법을 시도했다. 이 방법은 바운딩박스 수치(179×46)는 맞았지만, 실제 스크린샷으로 확인한 결과 시각적으로 완전히 잘못되었다 — DROP_SHADOW는 확장된 실루엣 "전체"를 잉크색으로 채우고 그 위를 불투명한 전경이 가려주는 방식이라, 전경이 2%로 거의 투명한 이 변형에서는 잉크색 그림자가 전혀 가려지지 않고 컴포넌트 전체가 완전히 까맣게 칠해진 사각형으로 렌더링됐다(Active 변형처럼 가장자리만 살짝 보이는 "링"이 아니라 속이 꽉 찬 "블록"). 스크린샷으로 실제 렌더링 결과를 확인하지 않았다면 "바운딩박스만 맞고 시각적으로는 틀린" 상태로 오판할 뻔한 케이스라 기록해둔다.
- **최종 정정**: ghost fill과 DROP_SHADOW를 모두 제거하고(`fills=[]`로 원상 복구, `effects=[]`), 대신 **3px ink(#1A1A1A) `strokeAlign=OUTSIDE`** 스트로크를 직접 추가했다. 스트로크는 실루엣 내부를 채우지 않고 테두리만 그리므로, 배경이 완전 투명한 컴포넌트에서도 "3px 링이 바깥쪽으로 확장된다"는 동일한 시각적 결과를 정직하게 재현한다. `cornerRadius=10`은 그대로 유지되어 스트로크도 둥근 모서리를 따라간다.
- **재검증**: `get_screenshot` 바운딩박스가 179×46으로 `287:14`와 정확히 일치함을 재확인했고, `use_figma`의 `node.screenshot()` 인라인 렌더로 실제 시각 결과(둥근 사각형 테두리 링, 속이 채워지지 않음, "전체" 텍스트와 앰버 Count Pill 정상 표시)를 직접 확인했다. Sidebar Nav Item 전체 4-variant 세트를 한 화면에 렌더링해 Active/Inactive × Focus=No/Yes 4종이 모두 일관된 톤으로 보이는 것도 확인했다.
- **범위**: 이 기법 변경은 `287:17` 1건에만 적용했다. 나머지 8쌍(TypeSelector/NeoInput/CornerInput/NeoBtn/Button/Icon Button/Row Action Button/Table Row Action Focus 변형, `287:14` 포함)은 전부 불투명 전경을 갖고 있어 기존 DROP_SHADOW 기법이 정상 작동하며 그대로 둔다.

**결함 2 — Disabled 상태(균일 opacity=0.45)가 WCAG 최소 대비 미달**

- **증상**: NeoBtn(`259:126`)/Button(`259:609`)/Icon Button(`259:613`)/Row Action Button(`260:95`)/Table Row Action(`260:100`)의 Disabled variant(top-level variant 노드 기준 총 16개)에 컨테이너 전체 `opacity=0.45`를 균일 적용한 결과, WCAG 상대휘도 공식으로 재계산했을 때 가장 유리한 조합(흰 배경+ink 텍스트)도 2.89:1, 가장 불리한 조합(Teal/Coral 배경+ink 텍스트)은 각각 1.76:1/1.73:1로 AA 기준(4.5:1, 큰 텍스트/UI 요소 3:1) 전부 미달이었다.
- **검토한 두 옵션과 선택**: 사용자가 제시한 두 옵션(①opacity를 배경/텍스트 분리 ②opacity 값 자체를 상향) 중 순수 상향 조정(②)만으로 성립하는 최소 opacity를 먼저 계산했다 — Teal/Coral+ink 최악 조합이 3:1을 넘으려면 α≈0.72 이상이 필요했는데, 이 값에서는 Amber+ink가 5.59:1(원래 Default의 풀컬러 대비 거의 근접)까지 진해져 "비활성화된 것처럼 보이지 않는" 문제가 생긴다 — 대비를 고치려다 "오류를 인터랙션으로 예방"하는 Disabled의 핵심 어포던스(명백히 비활성으로 보여야 클릭을 시도하지 않음)를 해친다고 판단해 기각했다. 대신 **①번(배경/텍스트 분리)**을 채택했다: 컨테이너 자체 `opacity`는 1로 되돌리고, 배경 fill과 보더 stroke의 **페인트 opacity만 0.5**로 낮춰 "확실히 흐려진 배경/보더"를 유지하면서(Disabled임을 알아볼 수 있는 시각 신호는 그대로 보존), 텍스트/아이콘 자식 노드의 opacity는 **0.85**로만 살짝 낮춰 대비를 확보했다. Figma에서 페인트(fill/stroke) 자체의 opacity 필드는 그 레이어에만 적용되고 자식 노드에 곱연산으로 전파되지 않는다는 특성을 이용해, 배경은 진짜로 흐리게·텍스트는 읽히게 두 목표를 분리했다.
- **재계산 결과** (WCAG 2.1 상대휘도 공식, 페이지 배경을 흰색으로 가정해 blend):
  - Amber bg + ink 텍스트: **8.88:1 PASS**
  - Teal bg + ink 텍스트: **6.31:1 PASS**
  - Coral bg + ink 텍스트: **6.22:1 PASS**
  - Neutral(흰) bg + ink 텍스트: **10.97:1 PASS**
  - Icon Button 아이콘(ink) / Row Action Button 아이콘(ink/800 #1C1F21) on 흰 bg: 위 whiteBg+ink 그룹과 동일 프로파일로 약 9~11:1 **PASS**
  - Table Row Action 텍스트(Neutral=teal `#17A398`/Danger=coral `#FF5A76`) on 흰 bg: **약 2.60~2.62:1로 3:1 미달** — 아래 참고.
- **Table Row Action은 별도 취급**: 이 컴포넌트만 배경이 항상 흰색(다른 색을 가진 배경이 없음)이라 이번 배경-opacity 분리 기법이 대비에 기여하지 못하고, 텍스트 자체의 색(teal/coral)이 **7-1절 §3에서 이미 사용자가 "이번 프로젝트 범위에서 개선하지 않기로" 확정한 기존 대비 미달 텍스트**다. Default(Enabled, 풀 opacity) 상태조차 이미 3:1 미만으로 수용된 상태이므로, Disabled가 그보다 더 진하게 보일 수는 없다(Disabled는 Default보다 강조가 약해야 한다는 원칙과 모순). 따라서 이번 정정에서는 opacity=0.45 균일 적용으로 인한 "추가 악화분"만 제거했고(1.6:1대→2.6:1대로 개선, 균일 opacity 이전 대비 명백한 개선), 7-1절 §3 자체의 근본 원인(텍스트 색)은 건드리지 않았다 — 이는 신규 회귀가 아니라 기존에 수용된 한계의 연장선이다.
- **적용 범위**: Disabled top-level variant 16개 전체(NeoBtn 8, Button 3, Icon Button 1, Row Action Button 2, Table Row Action 2)에 동일 공식(컨테이너 opacity=1, fill/stroke opacity=0.5, 자식 opacity=0.85)을 일괄 적용했다 — "예측 가능성" 원칙에 따라 5개 컴포넌트 전부 동일한 Disabled 규칙을 공유한다.
- **재검증**: 대표 variant(NeoBtn Teal, Table Row Action Neutral/Danger, Row Action Button Danger, Icon Button Close) 스크린샷으로 배경은 파스텔톤으로 흐려지고 텍스트/아이콘은 선명하게 읽히는 것을 시각 확인했고, 위 대비 수치를 코드로 재계산해 확인했다.

# mercari 가격제안 화면 — Graphic Assets (원화)

Figma `SIBLz4S4IZbjabzhMSAgdo` 소유 문서. graphic-designer가 "Graphic Assets" 페이지(`195:3`, `--- GRAPHIC ASSETS ---` 구분 페이지 `195:2` 아래, Brand Guide와 FOUNDATIONS 사이에 신설)에 그린 아이콘/오브제 원화의 현재 확정 상태를 기록하는 소스 오브 트루스다. 이 프로젝트는 fileKey가 `SIBLz4S4IZbjabzhMSAgdo`로, 연락처 관리 앱(`zgGlMBwFglaDlaeyP4CkgR`) 소유의 `docs/design/graphic-assets.md`와 무관하다 — `figma-file-organization.md`의 "여러 Figma 파일을 동시에 다룰 때 서브폴더로 분리" 규칙에 따라 이 문서를 별도로 둔다.

## 배경 — 이번 라운드의 트리거

design-qa가 지난 컴포넌트 추출 라운드에서 HIGH로 지적: 확정 화면(Concept A_01~04, B_01~03 — 브랜드 가이드 서술상의 이름, 실제로는 아래 "노드 ID가 바뀐 이유" 참고) 안에 `chevron-right`(24×24)·`star-01`(12×12)·`shield-check`(32×32) 3개 아이콘이 재사용 불가능한 raw FRAME으로만 조립돼 있음. 이번 라운드는 이 3개를 design-systems가 COMPONENT로 승격시킬 수 있는 표준 아이콘 프레임으로 정리하는 것이 목적이다. **아이콘의 형태 자체는 새로 그리지 않았다 — 확정 화면에서 관찰한 형태를 그대로 옮겼다.**

### 노드 ID가 바뀐 이유 (중요 — design-pl/후속 워커 참고)

브리프에 적힌 확정 화면 노드 ID(`110:103` 등, `docs/design/mercari/brand-guide.md` 근거절 기준)는 이번 라운드 시작 시점에 **더 이상 존재하지 않았다**(`getNodeByIdAsync`로 전부 not found 확인). 대신 "UI 디자인" 페이지(`187:2672`) 안의 섹션 `"SCR-002/SCR-003 가격 제안 화면"`(`187:2673`)에서 이름이 `Concept A_SCR-002_01~04`·`Concept B_SCR-002_01~03`로 바뀐 동일 내용(스크린샷·구조·텍스트 전부 일치, 다크히어로/화이트시트 구성·딤 오버레이 유무·Hero Price Card 단일가/범위가 패턴이 브랜드 가이드 서술과 정확히 대응)의 7개 화면을 발견했다 — design-systems가 그 사이 라운드에서 화면을 이 섹션으로 옮기고 이름에 `_SCR-002`를 끼워 넣은 것으로 추정된다(직접 확인은 안 됨). **확정 화면 자체는 이번 라운드에서 열람만 하고 수정하지 않았다** — 노드 재배치 자체도 이번 라운드의 작업이 아니다.

| 브리프 표기(구 ID) | 실제 현재 노드 |
|---|---|
| Concept A_01 (`110:103`) | `Concept A_SCR-002_01` (`187:2674`) |
| Concept A_02 (`124:890`) | `Concept A_SCR-002_02` (`187:2872`) |
| Concept A_03 (`124:1149`) | `Concept A_SCR-002_03` (`187:2919`) |
| Concept A_04 (`124:991`) | `Concept A_SCR-002_04` (`187:2966`) |
| Concept B_01 (`124:1455`) | `Concept B_SCR-002_01` (`187:2720`) |
| Concept B_02 (`126:1771`) | `Concept B_SCR-002_02` (`187:2766`) |
| Concept B_03 (`126:1951`) | `Concept B_SCR-002_03` (`187:2817`) |
| 부모 (`126:2601`) | 섹션 `SCR-002/SCR-003 가격 제안 화면` (`187:2673`) |

## 아이콘 3종 — 트랙 판정·정리 결과 (design-systems 인수인계용)

`docs/harness/design-team/icon-craft-guide.md`의 트랙 판정 기준(반복 등장·기능성 전달 vs 브랜드 퍼스낼리티 전달)을 브랜드 가이드의 "라인/라인+면/면" 서술과 독립적으로 새로 적용했다.

### 1. `chevron-right` — Basic/Utility 트랙

- **정리된 노드**: `195:14`(프레임, 24×24) > `195:17`("Icon" 벡터)
- **관찰 근거 노드(원본, 미수정)**: 7개 확정 화면 CTA 버튼에 전부 등장. 그중 5개는 이미 존재하는 `CTA` 컴포넌트 인스턴스 내부에 중첩된 raw 프레임(`I187:2719;124:1128` 등, 컴포넌트 마스터 자체가 내부적으로 raw 프레임을 쓰고 있어 인스턴스 오버라이드 형태로 노출됨) — 이건 "컴포넌트 안에 이미 포함된" 상태라 QA가 지적한 문제와는 결이 다르다. QA가 지적한 진짜 문제는 **컴포넌트 인스턴스가 아니라 화면에 직접 박힌 raw "CTA Button" 프레임 2개**다: B_SCR-002_03(`187:2817`) 안의 `187:2870`, A_SCR-002_04(`187:2966`) 안의 `187:3015` — 이 두 화면은 CTA 컴포넌트 인스턴스 대신 손으로 다시 조립한 프레임을 쓰고 있어 `chevron-right`가 완전히 고립된 raw FRAME이다. 이번 정리는 이 2개를 원본으로 삼았다(둘 다 완전히 동일한 형태·수치).
- **판정 근거**: 화면 전환/다음 단계 이동을 나타내는 순수 방향 기호이자 7개 화면 전부의 CTA 버튼에 반복 등장. 아이콘이 없어도 브랜드 인상은 달라지지 않는다 → Basic/Utility.
- **크래프트 확인**: 이미 stroke-only(면색 없음, `fills: []`)로 그려져 있어 Basic 트랙 규칙에 원래부터 부합 — 정리 과정에서 fill을 제거하는 등의 수정은 필요 없었다. strokeWeight 2px(raw 2개·컴포넌트 내부 5개 인스턴스 전부 동일) — 세트 내 일관성 이상 없음.
- **정리 전/후 차이**: 형태·수치 변경 없음. raw 프레임을 표준 24×24 아이콘 프레임(`195:14`)으로 옮겨 담고 배경(투명, 정리 유지)·벡터 지오메트리(x=15,y=8,rotation=-90°,path `M 0 5 L 5 0 L 10 5`, strokeCap/Join ROUND)를 그대로 재현했을 뿐이다.
- **색상(하드코딩 유지, 미변경)**: 정리본은 raw occurrence 그대로 흰색(`#FFFFFF`) stroke — 화면상 CTA 활성(파란 배경) 상태에서 쓰이는 색. Graphic Assets 페이지에서는 가독성을 위해 다크 배경(`#1A1D29`) 스와치를 아이콘 프레임 자체에 얹었다(아이콘 fill이 아니라 리뷰용 배경일 뿐).
- **⚠ 특이사항(design-systems 별도 확인 필요, 이번 라운드에서 고치지 않음)**: 컴포넌트 인스턴스 안에 중첩된 `chevron-right`(비활성 CTA, `CTA Button Disabled` variant)의 실제 색상은 순수 검정 `#000000`(불투명도 100%)이다 — `brand-guide.md`가 정의한 비활성 스펙(`Ink 35%`, 즉 `#1A1D29` @ 0.35 opacity)과 다르다. 이건 raw FRAME 문제가 아니라 이미 존재하는 `CTA` 컴포넌트 마스터 내부의 색상 하드코딩 오류라서 이번 브리프 범위(raw FRAME 정리) 밖이다 — design-systems가 CTA 컴포넌트 색상 감사 때 확인할 것.
- **[2026-08-27 정정 포인터, 2026-08-27 재정정]** 위 "불투명도 100%" 기록에 대해, `docs/design/mercari/brand-guide.md` 9-3에서 이뤄진 재관찰 시점에는 opacity 0.3으로 확인됐다 — design-systems가 그 값(`#000000` opacity 0.3)을 `color/text-muted-35-on-surface-muted` 토큰(합성 hex `#AAABB1`)에 바인딩했다. **두 기록 중 어느 쪽이 측정 오류였는지, 혹은 두 관찰 시점 사이에 실제로 값이 바뀌었는지는 확정할 근거가 없다**(brand-guide.md 9-3 원문 참고 — 그쪽도 "그 사이 누군가 opacity만 손댄 흔적"이라는 가능성을 열어둔다). 확실한 것은 design-systems가 최종적으로 바인딩한 값(opacity 0.3 → `#AAABB1`)이 브랜드 가이드 1절의 정식 스펙(Ink 35%)과 일치한다는 것뿐이다. 이 문서의 원본 관찰 기록(불투명도 100%)은 정정하지 않고 그대로 두며, 참고 포인터만 남긴다.
- **⚠ 구조적 특이사항(design-systems 참고, 이번 라운드에서 고치지 않음)**: B_SCR-002_03·A_SCR-002_04 두 화면은 `CTA` 컴포넌트 인스턴스 대신 손으로 다시 만든 "CTA Button" 프레임을 쓰고 있다 — 확정 화면 자체이므로 이번 라운드에서 수정하지 않았지만, 이 두 화면을 나중에 `CTA` 인스턴스로 교체하면 raw chevron-right 중복 자체가 사라진다는 점을 design-systems에 참고 보고한다(화면 수정은 ui-designer/design-systems 소관, graphic-designer 권한 밖).

### 2. `star-01` — Visual/Feature 트랙

- **정리된 노드**: `195:15`(프레임, 12×12) > `195:18`("Ellipse 1") + `195:19`("Star 1")
- **관찰 근거 노드(원본, 미수정)**: 7개 확정 화면 전부의 Progress Row > Badge("빅데이터 산출로 제안") 좌측에 raw FRAME으로 반복(예: `187:2698`, `187:2744`, `187:2790`, `187:2841`, `187:2897`, `187:2944`, `187:2991`) — 전부 인스턴스가 아니라 화면마다 독립 복제된 raw 프레임. 좌표·크기·strokeWeight·자식 구성(Ellipse+Star)이 7개 전부 완전히 동일함을 확인(들쭉날쭉함 없음).
- **판정 근거**: "AI가 빅데이터로 분석해 제안했다"는 신뢰 신호를 색이 있는 원+별 조합으로 전달하는 자리 — brand-guide가 정의한 Primary 컬러(`#3182F6`)를 그대로 쓰는 브랜드 표현 요소다. 제거하면 "데이터 기반 신뢰"라는 브랜드 인상이 옅어진다 → Visual/Feature.
- **크래프트 확인**: 이미 순수 fill 조합(원=Primary 파랑 solid, 별=흰색 solid, 둘 다 stroke 없음)으로 그려져 있어 Visual 트랙의 "브랜드색 평면 채색" 규칙에 원래부터 부합. 정리 과정에서 형태·색 변경 없음.
- **정리 전/후 차이**: 없음. 7개 raw 복제본 중 대표 1개(A_SCR-002_01의 `187:2698`/`187:2699`/`187:2700`)를 표준 12×12 아이콘 프레임(`195:15`)에 그대로 재현했다 — Ellipse(12×12, fill `#3182F6`), Star(10×10 at x≈1,y≈1, pointCount 4, innerRadius 0.34, fill `#FFFFFF`).
- **특이사항**: 없음 — 7개 occurrence가 완전히 동일해 어느 것을 정리 기준으로 삼아도 무방했다.

### 3. `shield-check` — Visual/Feature 트랙

- **정리된 노드**: `195:16`(프레임, 32×32, 배경 투명 유지) > `195:20`("Icon" 벡터)
- **관찰 근거 노드(원본, 미수정)**: `Choice Card` 컴포넌트 인스턴스 내부에 중첩된 raw FRAME으로만 존재 — 선택된 카드에서만 등장(브랜드 가이드 서술과 일치). 확인된 occurrence 2쌍: B_SCR-002_02(`187:2766`)의 `I187:2810;124:657`, A_SCR-002_03/04 계열의 `I187:2964;124:534`·`I187:3011;124:534` — 두 계열(`124:657` 기반/`124:534` 기반, 서로 다른 Choice Card 컴포넌트 variant에 속함) 전부 벡터 path·색상·strokeWeight가 완전히 동일함을 확인.
- **판정 근거**: "이 선택이 확정·보증됐다"는 신뢰 신호이자, 사용자가 실제로 고르는 상호작용 지점(선택된 카드)에서만 조건부로 등장 — icon-craft-guide의 "카테고리·알림처럼 사용자가 그 화면/기능의 성격을 느끼는 지점" 예시에 정확히 해당 → Visual/Feature.
- **⚠ 관찰 중 발견한 브랜드 가이드와의 불일치(형태를 재해석하지 않고 실제 관찰값을 그대로 기록)**: `brand-guide.md` 6절은 이 아이콘을 "파란 방패 바탕 + 흰색 체크(면/필)"로 서술하지만, **실제로 화면에 그려진 것은 방패 배경 도형이 전혀 없는 체크마크 하나뿐**이다 — `shield-check`라는 이름의 FRAME은 배경 fill이 `visible:false`(비가시)이고, 그 안의 "Icon" 벡터는 파란색(`#3789FF`, Secondary 토큰) **stroke**(두께 5px, fill 없음) 체크 글리프뿐이다. `get_screenshot`으로 실제 화면(선택된 "아니요, 다르게 하고 싶어요" 카드)을 재확인해 방패 도형이 없다는 것을 시각적으로도 재확인했다. **이번 라운드는 관찰된 형태를 그대로 정리했다** — 방패 배경을 새로 그려 넣지 않았다. brand-guide.md 서술과 실물이 다르다는 점만 design-pl/brand-designer에 참고 보고하고, 어느 쪽이 "맞는" 것인지(방패를 추가로 그려야 하는지, 브랜드 가이드 서술을 체크 단독으로 정정해야 하는지)는 이번 브리프 범위 밖이라 판단하지 않았다.
- **크래프트 확인**: stroke 5px(32px 프레임 기준)로 Visual 트랙이 요구하는 "굵은 잉크 아웃라인" 느낌에는 부합하나, 같은 Visual 트랙인 `star-01`(순수 fill, stroke 없음)과 렌더링 기법 자체가 다르다(하나는 fill 조합, 하나는 굵은 stroke 체크) — 이는 두 글리프의 형태가 원래 다르기 때문(별 vs 체크마크)이며, 아이콘을 다시 그려서 강제로 같은 stroke 두께를 맞추는 건 "형태 재해석 금지" 범위를 벗어나므로 이번 라운드에서 손대지 않았다. design-qa가 "같은 트랙인데 두께가 들쭉날쭉하다"고 판단할 경우를 대비해 특이사항으로 남겨둔다.
- **정리 전/후 차이**: 형태·색 변경 없음. 컴포넌트 인스턴스 내부에 중첩돼 있던 것을 독립된 32×32 표준 아이콘 프레임으로 옮겨 벡터 지오메트리(x=7.82,y=11.53,width=17.70,height=11.80, path `M 0 5.9 L 5.9 11.8 L 17.7 0`, strokeCap/Join ROUND)를 그대로 재현했다.

## 정리 결과 요약 (design-systems가 COMPONENT로 승격할 때 참고)

| 아이콘 | 정리된 프레임 | 트랙 | 정리 전/후 차이 | 비고 |
|---|---|---|---|---|
| `chevron-right` | `195:14` (24×24) | Basic/Utility | 없음(구조 이전만) | 흰색 stroke 2px, fill 없음. 비활성 색상(#000000) 불일치는 CTA 컴포넌트 쪽 별도 이슈 |
| `star-01` | `195:15` (12×12) | Visual/Feature | 없음(구조 이전만) | Primary 원 + 흰색 별, fill only |
| `shield-check` | `195:16` (32×32) | Visual/Feature | 없음(구조 이전만) | Secondary stroke 체크마크만 존재 — 이름과 달리 방패 도형 없음(브랜드 가이드 서술과 불일치, 관찰값 그대로 유지) |

**확정 화면 7개(`187:2674`/`187:2872`/`187:2919`/`187:2966`/`187:2720`/`187:2766`/`187:2817`) 자체는 이번 라운드에서 열람만 하고 일절 수정하지 않았다.**

## 이어지는 라운드 — design-systems의 컴포넌트 승격·occurrence 교체 마무리

design-systems가 위 인수인계를 이어받아 처리한 결과를 기록한다(위 섹션은 graphic-designer 원본, 이 섹션부터 design-systems 작업).

### 노드 ID 재검증 결과 (이번이 세 번째 확인)

브리프에 적힌 `195:14`/`195:15`/`195:16`(raw FRAME)은 **이미 이전의 별도 라운드에서 정식 COMPONENT로 승격 완료된 상태**였다(이번 라운드 시작 시점에 `get_metadata`로 확인) — 실제 컴포넌트 노드는 `206:32`(chevron-right) / `206:33`(star-01) / `206:34`(shield-check)이며, 내부 벡터/도형은 원래 ID(`195:17`/`195:18`+`195:19`/`195:20`)를 그대로 유지한 채 부모만 COMPONENT로 바뀌어 있었다. 이 승격 작업이 언제·누구에 의해 이뤄졌는지는 기록이 없으나(같은 `206:` ID 대역에 CTA 인스턴스 교체, Icons 페이지, 변수 컬렉션까지 함께 생성된 흔적으로 보아 한 세션에서 일괄 처리된 것으로 추정), **문서화가 누락된 채 방치**돼 있었다 — 이번 라운드에서 뒤늦게 확인·기록한다.

같은 이유로 브리프가 지목한 chevron-right occurrence 2개(`187:2870`, `187:3015`, "손으로 만든 CTA Button 프레임")도 **더 이상 존재하지 않았다** — B_SCR-002_03·A_SCR-002_04 두 화면 모두 이미 정식 `CTA` 컴포넌트 인스턴스(`206:869`, `206:874`)로 교체돼 있었다(위 "구조적 특이사항"이 이 사이 라운드에서 이미 해소됨). 반면 **shield-check는 이미 `Choice Card` 컴포넌트 마스터 내부에서 `206:34` 컴포넌트의 INSTANCE로 존재**했고(`206:815`/`206:817`/`206:819`/`206:821`/`206:823`/`206:825`), star-01 occurrence 7개(`187:2698` 등)만 브리프 기록 그대로 raw FRAME으로 남아 있었다.

### 실제로 수행한 교체·수정

- **chevron-right**: 화면에 남은 raw occurrence가 없어, 대신 `CTA` 컴포넌트 마스터 두 variant(`124:1135` Disabled, `124:1136` Active) 내부에 raw FRAME+VECTOR로 박혀 있던 chevron을 찾아 `206:32` 컴포넌트의 INSTANCE로 교체했다(위치/크기 24×24 무변화 확인). 마스터 단위 교체라 7개 화면 전체에 자동 전파된다.
- **⚠ 회귀 발견·즉시 수정**: `206:32`(chevron-right) 컴포넌트 자체에 리뷰용으로 얹은 것으로 추정되는 진한 남색(#1A1D29) 배경 fill이 **컴포넌트 자신의 fill로 박혀 있어**, 위 교체 직후 CTA 버튼에 검은 사각형이 나타나는 회귀가 발생했다. 즉시 `206:32.fills = []`로 제거해 star-01(`206:33`)·shield-check(`206:34`)와 동일하게 투명 배경으로 맞췄다(스크린샷으로 CTA 재검증 완료). 이 배경이 빠지면서 "Graphic Assets" 페이지의 chevron-right 스와치 자체는 흰 배경 위 흰 stroke라 육안 확인이 어려워졌다 — 별도 배경 사각형을 컴포넌트 바깥에 추가하려 시도했으나 auto-layout 흐름에 끼어들어 레이아웃이 틀어지는 문제가 반복돼(2회) 정리 차원에서 되돌렸다. **다음 라운드 참고**: chevron-right 스와치 가독성 개선은 `layoutPositioning='ABSOLUTE'`로 도큐먼트 전용 배경을 붙이는 방식으로 별도 처리 필요(이번엔 보류).
- **star-01**: 7개 occurrence(`187:2698`/`187:2744`/`187:2790`/`187:2841`/`187:2897`/`187:2944`/`187:2991`) 전부 `206:33` 컴포넌트의 INSTANCE로 교체(12×12 위치/크기 무변화 확인).
- **shield-check**: 이미 인스턴스였으므로 구조 변경 없음.

### 아이콘 마스터 색상 바인딩

세 아이콘 마스터의 내부 벡터/도형 색을 (이번 라운드에서 신설한) Semantic Colors 변수에 바인딩했다: chevron-right stroke → `color/bg-surface`(흰색, STROKE_COLOR 스코프 확장), star-01 Ellipse fill → `color/primary`, Star fill → `color/bg-surface`, shield-check stroke → `color/secondary`. 상세는 `docs/design/mercari/brand-guide.md`의 신규 절 참고.

## SCR-004/005/006 오브제 보강 — 이모지 교체 2건 + 빈 인디케이터 채우기 (2026-08-26)

이 절은 `docs/harness/design-team/icon-craft-guide.md`의 "이모지는 포인트로만 쓴다"(2026-08-26 신설) 원칙 적용 라운드다. "설문UI" 페이지(`187:4084`) 아래 SCR-004(`258:143`)·SCR-005(`261:157`)·SCR-006(`261:160`)을 대상으로 했다.

### 1. Selection Indicator — 16×16 (Basic/Utility 트랙)

- **대상**: SCR-004 Reason List Item 3개(`258:160`/`258:165`/`258:169`) 좌측 16×16 자리(`258:161`/`258:166`/`258:170`).
- **작업 전 상태(재확인 필요)**: `get_metadata`는 이 3개 프레임을 빈 것처럼(self-closing) 보고했으나, 실제로는 이미 라디오 버튼 형태(흰 원 + 얇은 보더 + 선택 시 안쪽에 작은 Primary 도트)가 그려져 있었다 — `get_metadata`의 깊이 제한(6단계 이상 하위 노드 생략 추정)으로 누락된 것으로 보인다. **브리프가 "빈 placeholder"로 서술한 것과 실제 상태가 달랐다는 점을 기록**: 이후 유사 브리프에서 `get_metadata`만으로 "비어 있다"고 단정하지 말고 `use_figma`로 자식 노드를 직접 순회해 재확인할 것.
- **재작업 이유**: 기존 라디오 형태(흰 원+파란 링+파란 도트)는 브리프가 지정한 "Primary 솔리드 원 채움 + 흰색 체크(또는 흰 도트)" 크래프트와 반대 구성(면이 아니라 링+도트)이라, 브리프 craft 지시대로 다시 그렸다.
- **선택(Selected) 상태**: Ellipse 16×16, fill `#3182F6`(`color/primary`), stroke 없음 + Vector 체크(8.85×5.9, path `M 0 2.95 L 2.95 5.9 L 8.85 0`, strokeWeight 1.7, 흰색 `color/bg-surface`, strokeCap NONE/strokeJoin MITER — `shield-check`(`206:34`)의 체크 path를 0.5배로 스케일한 동일 비율). SCR-004 안에서는 item1(`258:161`, "가격이 딱 떨어져서 좋았어요")에 적용 — 이 아이템만 카드 배경이 Accent Tint+Primary 2px 보더로 이미 선택 표시돼 있어 실제 선택 상태와 일치.
- **미선택(Unselected) 상태**: Ellipse 16×16, fill 없음(`fills: []`, 완전 투명 — Basic 트랙 "면색 없음" 원칙 그대로), stroke 1.5px `color/border-neutral`(`#E2E6EC`). item2(`258:166`)·item3(`258:170`)에 적용.
- **크래프트 확인**: 체크 두께(1.7px)는 shield-check(32px 프레임 기준 5px)를 16px 프레임 비율로 그대로 스케일한 값이 아니라(비례값은 2.5px) 가독성을 위해 낮춘 값이다 — 8.85px 폭의 체크에 2.5px 스트로크를 쓰면 형태가 뭉개지는 문제를 실측 후 확인해 1.7px로 조정했다. 미선택 stroke(1.5px)는 chevron-right(2px, Basic 트랙)보다 얇아 "세트 내에서도 더 얇고 중립적"이라는 규칙에 부합.
- **색상**: 새 hex 발명 없음 — Primary/Accent 계열은 전부 Choice Card 선택 언어(`color/primary`, `color/border-neutral`, `color/bg-surface`)를 그대로 재사용.
- **정리된 노드(Graphic Assets 페이지 원화)**: `279:147`(Selected, Ellipse+Check) / `279:153`(Unselected, Ring) — `279:143` 프레임 하위.
- **화면 적용 노드**: `258:161`(Selected, 체크 `274:157`) / `258:166`·`258:170`(Unselected).

### [2026-08-27 결함 수정] Selection Indicator — Selected 상태 면색 위반 재작업

design-qa 46차·harness-auditor 98차가 공통으로 HIGH 지적: 위 "선택(Selected) 상태" 서술의 구성 — `Ellipse 16×16, fill #3182F6(color/primary), stroke 없음` — 이 `icon-craft-guide.md`의 Basic/Utility 트랙 규칙("면색을 넣지 않는다 — 순수 스트로크만 사용한다")을 위반한 상태였다. **미선택(Unselected) 상태는 위반이 없어 그대로 유지했다.**

- **재설계 방식**: 브리프가 제시한 두 대안 중 "체크 글리프" 방식을 채택했다(이중 링보다 "선택됨" 의미가 더 명확히 읽힘). 외곽 Ellipse는 fill을 완전히 제거하고 stroke 2px `color/primary`(`#3182F6`)만 남긴 링으로 바꿨다(레이어명 "Selected Ring"). 내부 Check Vector(기존 path `M 0 2.95 L 2.95 5.9 L 8.85 0`, 8.85×5.9 그대로 유지)는 stroke 색을 흰색(`color/bg-surface`)에서 `color/primary`로 바꿨다(strokeWeight 1.7 유지, fill은 원래부터 없었음). 결과적으로 원·체크 두 도형 모두 `fills: []`이고 stroke만으로 "선택됨"을 표현한다 — Unselected(얇은 회색 빈 링)와는 색(Primary vs 뉴트럴)·두께(2px vs 1.5px)·체크 유무로 명확히 구분된다.
- **반영 노드(같은 패턴의 모든 occurrence 스캔·교체 완료)**:
  - Graphic Assets 원화: `279:147`(Selected 프레임) — `279:148`(Selected Ring, 이전 이름 "Selected Fill") + `279:149`(Check).
  - SCR-004 base 배치본: `258:161`(Selected 프레임) — `258:162`(Selected Ring) + `274:157`(Check).
  - "기타" 모달(`259:183`) 배경 복제본: `259:174` — 이 occurrence는 위 두 곳과 구조 자체가 달랐다(fill 위반이 아니라 훨씬 더 오래된 "흰 원+파란 링(`259:175`)+안쪽 파란 도트(`259:176`)" 구성이었음, 즉 Selection Indicator 재작업 라운드 이전 상태로 추정). 도트(`259:176`)를 제거하고 `259:175`를 fill 제거+stroke 2px Primary 링으로 바꾼 뒤, 기준 Check(`274:157`)를 clone해 신규 Check(`284:954`)로 삽입해 base와 동일한 구성으로 맞췄다.
- **레이어명 정정(결함 2, MEDIUM)**: "기타" 모달의 Selection Indicator 래퍼 3개(`259:166`/`259:170`/`259:174`)가 전부 "Frame"으로 일반화돼 있던 것을 SCR-004 base와 동일하게 "Selection Indicator — Selected"(`259:174`)/"Selection Indicator — Unselected"(`259:166`, `259:170`)로 통일했다.
- **추가로 발견해 함께 정리(브리프에 명시되진 않았으나 같은 트랙 규칙 위반)**: `259:166`/`259:170`의 내부 Ellipse(`259:167`/`259:171`)가 base(`258:167`/`258:171`)와 달리 흰색 solid fill(`color/bg-surface`)을 갖고 있었다 — 흰색이라도 "면색을 채우지 않는다" 원칙 위반이라 fill을 제거해 base와 동일한 stroke-only 구성으로 맞췄다.
- **검증**: `use_figma`로 위 8개 occurrence(`279:147`/`279:153`/`258:161`/`258:166`/`258:170`/`259:174`/`259:166`/`259:170`) 하위 모든 Ellipse/Vector의 `fills` 배열이 빈 배열임을 재조회로 최종 확인. `get_screenshot`으로 SCR-004 base·"기타" 모달 양쪽 모두 Selected 항목이 파란 스트로크 링+체크로, Unselected 항목은 얇은 회색 빈 링으로 뚜렷이 구분됨을 시각 확인했다. Graphic Assets 페이지의 라벨 텍스트(`279:146`)도 새 구성을 반영해 갱신했다.

### [2026-08-27 대체] Celebration Badge / Confirmation Badge → 아트팩트 확정 아이콘으로 교체

**아래 "2. Celebration Badge"·"3. Confirmation Badge" 절(단순 원+체크마크 구성)은 house rule에 따라 삭제하지 않고 그대로 보존하되, 실제 최종 채택안은 아니게 됐다** — 사용자가 메인 세션과의 아트팩트 브레인스토밍(8개 후보 비교)을 거쳐 다른 형태를 최종 확정했다. 아래 두 절의 제목에 `❌ 대체됨 —`을 붙여 레거시로 표시한다.

- **새 확정 아이콘**: SCR-005 = "파티 팝퍼"(크래커+콘페티 폭죽), SCR-006 = "흔드는 손"(손 제스처, `docs/harness/asset-reference/visual icon/hand/` 레퍼런스 스타일 — 캡슐형 손가락 4개+엄지, 손가락은 무테두리 면채색으로 손바닥에 깊이 파묻어 이음새 제거, 엄지는 손 전체와 동일한 그라데이션 + 손바닥 접합부에만 반투명 방사형 그림자로 자연스러운 음영 구분, 회전각 -38°).
- **정본(source of truth) 위치 — Figma 아님**: `docs/design/mercari/artifacts/scr005-006-icon-options.html`(git 추적). 이 라운드는 `docs/harness/design-team/figma-file-organization.md` 3-E번의 "확정본은 Figma로 옮긴다" 기본 절차를 **사용자 명시적 결정으로 예외 처리**했다 — 이 두 아이콘은 실제 화면 코드에 SVG로 직접 임베드될 예정이라 Figma 네이티브 벡터로 재현할 실익이 없다고 판단해, 아트팩트 HTML 파일 자체를 정본으로 확정했다(2026-08-27, 사용자 승인 — 예외 사유는 `figma-file-organization.md` 3-E번 각주 참고).
- **⚠ Figma 화면과의 불일치(의도된 상태, 결함 아님)**: Figma의 실제 SCR-005(`276:157`)/SCR-006(`277:157`) 노드는 위 "대체됨" 처리된 옛 Celebration/Confirmation Badge를 여전히 시각적으로 보여준다 — 이 라운드는 Figma를 거치지 않기로 했으므로 그 노드들을 갱신하지 않았다. 나중에 이 화면의 Figma 목업을 실제로 최신화하고 싶어지면, graphic-designer가 위 아트팩트 파일의 SVG 마크업을 그대로 붙여넣어(재해석 없이) 반영하는 별도 라운드가 필요하다.

### ❌ 대체됨 — 2. Celebration Badge — 72×72 (Visual/Feature 트랙, SCR-005 완료/감사)

- **대상**: SCR-005(`261:157`)의 🎉 이모지 텍스트 노드(`261:158`, 완전 제거).
- **구성**: Ellipse 72×72 solid fill `color/primary`(`#3182F6`) + Vector 체크(39.8×26.6, path `M 0 13.3 L 13.3 26.6 L 39.8 0`, strokeWeight 10, 흰색 `color/bg-surface`, strokeCap NONE/strokeJoin MITER) — "아이콘2"(edit-02, 파란 원형 배경+흰 라인 아이콘 합성) 패턴을 축하 톤으로 변주, shield-check와 동일한 체크 모티프를 재사용해 세트 전체의 "체크=확정/완료" 의미 일관성을 유지했다.
- **배치**: SCR-005는 `layoutMode: VERTICAL`, `primaryAxisAlignItems/counterAxisAlignItems: CENTER`인 auto-layout 프레임이라, 배지를 `insertChild(0, badge)`로 기존 이모지가 있던 첫 번째 자식 자리에 넣어 auto-layout이 위치·중앙 정렬을 자동 계산하도록 했다(절대 좌표 지정 시 auto-layout 흐름과 충돌해 배지가 엉뚱한 위치로 밀리는 문제를 실측 중 확인 → `layoutPositioning`을 건드리지 않고 자식 순서로 해결).
- **정리된 노드(Graphic Assets 페이지 원화)**: `279:158`(Celebration Badge, `279:155` 프레임 하위).
- **화면 적용 노드**: `276:157`(Celebration Badge, SCR-005 첫 번째 자식) — 원 `276:158`, 체크 `276:159`.

### ❌ 대체됨 — 3. Confirmation Badge — 64×64 (Visual/Feature 트랙, SCR-006 이미 참여함/재확인)

- **대상**: SCR-006(`261:160`)의 👋 이모지 텍스트 노드(`261:161`, 완전 제거).
- **구성**: Ellipse 64×64 solid fill `color/bg-accent-tint`(`#E8F3FF`) + Vector 체크(35.4×23.6, path `M 0 11.8 L 11.8 23.6 L 35.4 0`, strokeWeight 6, `color/primary`(`#3182F6`) 라인, strokeCap NONE/strokeJoin MITER, fill 없음).
- **톤 구분 근거**: SCR-005(축하)와 감정이 다르다는 브리프 지시에 따라 ① 배경을 solid Primary가 아니라 옅은 Accent Tint로 낮추고, ② 체크를 면 채움이 아니라 라인(스트로크 6px, Primary)으로 그려 "정보성 재확인" 신호로 절제했다. 두 배지를 나란히 스크린샷으로 비교해 시각적으로 뚜렷이 구분됨을 확인.
- **배치**: SCR-005와 동일하게 auto-layout 첫 번째 자식 자리에 `insertChild(0, badge)`로 배치.
- **정리된 노드(Graphic Assets 페이지 원화)**: `279:164`(Confirmation Badge, `279:161` 프레임 하위).
- **화면 적용 노드**: `277:157`(Confirmation Badge, SCR-006 첫 번째 자식) — 원 `277:158`, 체크 `277:159`.

### 4. `258:152`(shield-check 인스턴스) — 확인 결과

**확인 완료, 이상 없음.** `258:152`는 `206:34`(shield-check 마스터)를 정확히 참조하는 INSTANCE이며, 크기(32×32)·위치(카드 내 절대좌표 x=120.5, y=8)에 오버라이드가 없다. 유일한 오버라이드는 `layoutPositioning`(카드 내부에서 절대 위치로 얹히기 위한 것 — 브랜드 가이드 6절 "카드 우측 padding 영역에 절대 위치로 얹힘" 서술과 일치, 색상·형태 오버라이드 아님)뿐이다. 색상·형태 관련 오버라이드는 전혀 없음.

### 정리 결과 요약

| 오브제 | 트랙 | 화면 적용 노드 | Graphic Assets 원화 노드 | 크기 | 색상 |
|---|---|---|---|---|---|
| Selection Indicator (Selected) | Basic/Utility | `258:161` | `279:147` | 16×16 | stroke만 `color/primary` 2px 링 + `color/primary` 체크(2026-08-27 수정, 과거 fill 채움 기록은 위 결함 수정 절 참고) |
| Selection Indicator (Unselected) | Basic/Utility | `258:166`, `258:170` | `279:153` | 16×16 | stroke `color/border-neutral` 1.5px, fill 없음 |
| ❌ Celebration Badge (대체됨) | Visual/Feature | `276:157` (SCR-005, 화면엔 아직 이 상태로 남아있음) | `279:158` | 72×72 | fill `color/primary`, 체크 `color/bg-surface` |
| ❌ Confirmation Badge (대체됨) | Visual/Feature | `277:157` (SCR-006, 화면엔 아직 이 상태로 남아있음) | `279:164` | 64×64 | fill `color/bg-accent-tint`, 체크 `color/primary` |
| **SCR-005 파티 팝퍼(신규 확정)** | Visual/Feature | Figma 미적용 — `docs/design/mercari/artifacts/scr005-006-icon-options.html`이 정본 | 없음(Figma 미거침) | 72×72(아트팩트 viewBox 기준) | 크래커 다크네이비 + 콘페티 옐로/레드/틸/오렌지, 배경 `#3182F6` 계열 라디얼그라데이션 |
| **SCR-006 흔드는 손(신규 확정)** | Visual/Feature | Figma 미적용 — `docs/design/mercari/artifacts/scr005-006-icon-options.html`이 정본 | 없음(Figma 미거침) | 64×64(아트팩트 viewBox 기준) | 살구색 스킨 그라데이션, 배경 `#E8F3FF` |

**COMPONENT 승격은 이번 라운드 범위가 아니다** — design-systems가 후속 판단.

## 근거

- Figma `SIBLz4S4IZbjabzhMSAgdo`, `use_figma`/`get_metadata`/`get_screenshot`(inline `node.screenshot()` 포함)로 이번 라운드에 직접 관찰·재구성.
- `docs/design/mercari/brand-guide.md` 1절(색상)·6절(아이콘 스펙) — 정본이나, `shield-check` 항목은 위에서 기록한 대로 실물과 서술이 어긋남을 확인.
- `docs/harness/design-team/icon-craft-guide.md` — 트랙 판정 기준·체크리스트("이모지는 포인트로만 쓴다" 절 포함).
- (design-systems 이어지는 라운드) 위 "이어지는 라운드" 섹션은 노드 재조회·`node.screenshot()` 스크린샷 재검증으로 직접 확인한 결과다.
- harness-auditor 95차 LOW 지적(2026-08-27) 반영: 위 opacity 정정 포인터가 "측정 오류였다"고 단정하지 않도록 재정정 — brand-guide.md 9-3의 원래 서술(드리프트 가능성 언급)과 모순되지 않게 두 가설을 모두 열어둔 표현으로 바꿨다.
- "SCR-004/005/006 오브제 보강" 절은 `get_metadata`/`use_figma`(읽기 전용 실측 + 노드 생성·수정)/`get_screenshot`(inline `node.screenshot()` 포함)로 이번 라운드에 직접 실행·검증한 결과다.
- design-qa 46차·harness-auditor 98차 HIGH 지적(2026-08-27) 반영: "[2026-08-27 결함 수정]" 절은 `get_metadata`/`use_figma`(읽기 전용 실측 + 노드 수정·clone·삭제)/`get_screenshot`으로 이번 라운드에 직접 실행·검증한 결과다.

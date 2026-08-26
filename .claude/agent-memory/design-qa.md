# design-qa 메모리

이 파일은 design-qa가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 작업 로그

### 2026-08-25 (43차) — mercari 가격 UX 실험 대안 디자인: 확정 7화면(`126:2601`) + 신규/보강 컴포넌트(`126:2599`) + 스펙시트 완성도 감사 — HIGH 5건(신규) + MEDIUM 2건(신규) + PASS 다수

배경: 사용자 확정 디자인(`126:2601`, 7화면) → design-systems 컴포넌트 추출(Choice Card/Hero Price Card/CTA/Price Input/Progress Row/Product Row/Badge) → brand-designer가 `docs/design/mercari/brand-guide.md` 작성 완료 후 감사 라운드. Figma `SIBLz4S4IZbjabzhMSAgdo`.

**HIGH(신규) — 대비 미달 3계열, 전부 확정 원본(`126:2601`)에 존재, 사전 승인 기록 없음**: White Sheet 영역 "AI 추천" 팁 배지·"빅데이터 산출로 제안" Badge_01·Ink 뮤트 캡션 계열 전부 4.5:1 미달(약 3.11~3.80:1). 다크 히어로 텍스트는 문제 없음.

**HIGH(신규) — 아이콘이 전부 등록된 Icon 컴포넌트의 INSTANCE가 아니라 raw FRAME으로 조립됨**: shield-check/star-01/chevron-right/아이콘1·2가 컴포넌트 마스터·확정 화면 어디서도 INSTANCE가 아니라 FRAME. `component-state-guide.md` §4 위반.

**HIGH(신규) — 신규/보강 컴포넌트 7종 전부 Figma Variable 바인딩이 전무, 완전 하드코딩**: "No token = no component" 위반, Variables 인프라 자체 부재로 추정.

**HIGH(완성도) — 컴포넌트 스펙 시트가 7종 중 4종만 존재**: Choice Card/Hero Price Card/CTA 스펙 시트 및 description 이중 누락.

**MEDIUM(신규) — variant 축 이름이 전부 `State`가 아니라 `Property 1`**: 프로젝트 전반 기존 관례라 신규 사고는 아님.

**MEDIUM(신규) — 신규 4종(Badge/Progress Row/Product Row/Price Input)이 확정 화면 안에서 컴포넌트 INSTANCE로 치환되지 않음**: Hero Price Card/Choice Card/CTA는 인스턴스화됐으나 이 4종은 raw FRAME 잔존.

**PASS 다수**: B_03 상태배지 보더 누락 예외 재검증, 값 원본 대조(그림자 0건·hex/radius/padding 전부 brand-guide 일치), 네이밍("check box"→"Choice Card" 마스터 개명).

**종합**: HIGH 5건 + MEDIUM 2건 + PASS 다수, 전부 신규, design-systems/brand-designer 재작업 필요.

### 2026-08-25 (44차) — mercari "Brand Guide" 문서화 페이지(`165:10`) 감사 — MEDIUM 2건 + LOW 3건(전부 신규, 서식/데모 정확도), HIGH 0건

**MEDIUM(신규) — Colors 카탈로그(174:2) 16개 스와치의 보더 유무·굵기가 3가지 방식(무보더/1px/4px)으로 혼재**: `figma-page-format-guide.md` §1 위반. cornerRadius는 통일(PASS).

**MEDIUM(신규) — Ink 뮤트/흰 텍스트 opacity 스와치(7개) 데모 배경이 실제 사용 맥락(밝은 배경)과 반대(다크칩 복제)**: 라벨 텍스트는 정확, 데모 이미지만 오해 소지.

**LOW 3건**: 섹션 간 세로 여백 불일치(60px vs 40px 통일 구간), 타이포그래피 2절 위계 라벨 완전성 부족(₩/원 14px 차이 미표기), CTA 예시 소품 padding 불일치(px-20 py-14 vs 문서 py-16).

**PASS — 색상 16개/보더·Radius 12개/Spacing/주석 전수 hex·수치 대조 정확**.

**종합**: HIGH 0건, MEDIUM 2건, LOW 3건 — 값 정확성은 전수 PASS, brand-designer 후속 정리 권고.

### 2026-08-26 (45차) — mercari design-systems 결함 수정 4건 재검증(아이콘 INSTANCE 교체, chevron 배경 fill 회귀 수정, CTA Disabled 색상 정정, 7종 컴포넌트 토큰 바인딩 + 스펙시트 3종/Colors 페이지 신설) — HIGH 0건, MEDIUM 1건(신규 아님·지속), LOW 2건(도구 한계·문서 self-reference), PASS 다수(전수 재실측)

배경: 43차에서 지적한 HIGH 5건 중 아이콘 raw FRAME·토큰 미바인딩·스펙시트 누락 3건에 대한 design-systems의 수정 작업 결과를 보고서에만 의존하지 않고 Figma 직접 재실측으로 검증.

**PASS — star-01(7곳)/chevron-right(CTA 마스터 2 variant) INSTANCE 교체 전수 확인**: 7개 확정 화면(`187:2674/2720/2766/2817/2872/2919/2966`) 전부에서 star-01 인스턴스가 `<instance>` 타입으로 `206:33` 정확히 참조(위치/크기 12×12 @ x=8,y=5 원본과 동일). CTA 마스터(`124:1135`/`124:1136`) 내부 chevron(`221:774`/`221:809`)도 실제 `<instance>` 타입(raw FRAME 아님) 확인.

**PASS — chevron-right 배경 fill 제거 확인**: `187:2674`/`187:2817` 전체 화면 및 CTA Disabled 컴포넌트 단독 스크린샷에서 검은 박스 없음, 정상 렌더링.

**PASS — CTA Disabled 색상 계산 독립 검산**: `0.65×(247,248,250)+0.35×(26,29,41)=(169.65,171.35,176.85)→#AAABB1`, Colors 페이지 등록 토큰(`#aaabb1`)과 정확히 일치. 시각적으로도 아이콘·텍스트 동일 톤.

**PASS — 7종 컴포넌트(Choice Card/Hero Price Card/CTA/Progress Row/Product Row/Price Input/Badge) 토큰 바인딩**: `get_design_context` 전수 조회 결과 하드코딩 hex-only 클래스 0건, 전부 `var(--color-xxx, #hex)`이며 변수명이 신규 Colors 페이지(`233:143`) 캐논 컬렉션과 1:1 일치.

**PASS — 스펙 시트 3종(Choice Card `231:40`/Hero Price Card `232:99`/CTA `232:143`) 및 신규 Colors 페이지(`233:143`) 서식**: 기존 4개 스펙 시트와 동일한 제목→설명→그리드→라벨 순서, x=450 정렬 통일, 80px 간격 정확히 일치(실측: 600→843→1103→1369→1617→2003→2436). Colors 페이지 35개 스와치 전부 cornerRadius 6px·1px `#e2e6ec` 보더(흰색 계열도 예외 없이 포함)·112×56 크기·16px gap 완전 통일 — `figma-page-format-guide.md` 1절 모범 준수.

**MEDIUM(신규 아님, 지속 미해소) — 화면 레벨 Badge/Progress Row/Product Row/Price Input이 여전히 raw FRAME**: 예) `187:2697` Badge가 `bg-[#e8f3ff]`/`text-[#3182f6]` 하드코딩 유지 — 이번 라운드는 그 안의 아이콘만 인스턴스로 교체했을 뿐 프레임 자체는 미치환. 43차에서 이미 지적된 갭, 이번 라운드로 해소 안 됨.

**LOW(신규) — 도구 한계로 완전 검증 불가 2개 서브항목**: (1) 변수 scope가 `ALL_SCOPES`인지 여부, (2) CTA Disabled 아이콘 stroke가 실제 Variable 바인딩인지 우연히 일치하는 하드코딩 hex인지 — 둘 다 이 에이전트가 쓸 수 있는 읽기 전용 Figma MCP 도구로는 직접 조회 불가(변수 API 도구 부재, 벡터는 SVG 에셋으로 export되어 코드젠에 바인딩 정보 미노출). 결함 발견이 아니라 검증 공백 — Figma 데스크톱 Inspect 패널 수동 재확인 권고.

**LOW(신규) — Colors 페이지 라벨 텍스트가 자기 자신의 토큰을 안 씀**: 스와치 이름/hex 라벨이 `text-[#1a1d29]`/`rgba(26,29,41,0.5)`로 하드코딩. 44차 Brand Guide 문서 페이지도 동일 패턴이라 이 프로젝트 문서 페이지 전반의 기존 관례, 신규 사고는 아님.

**종합**: design-systems의 45차 보고 내용은 A/B/C/E/F 전부 실측과 정확히 일치(스펙 시트 3종·Colors 페이지는 top-level 페이지 목록엔 안 보였으나 알려진 조회 한계대로 직접 nodeId 조회 시 존재 확인됨). D도 확인 가능한 범위에서 전부 부합. 기존 MEDIUM 1건만 미해소 상태로 이월, HIGH 0건.

### 2026-08-26 (46차) — mercari 신규 화면 3개(SCR-004/005/006) + 오브제 보강(선택 인디케이터, Celebration/Confirmation Badge) 감사 — HIGH 3건(2건 신규 + 1건 기존 확산) + MEDIUM 4건(신규) + LOW 2건, PASS 다수

배경: SCR-004(선택+이유 설문, `258:143`, "기타" 모달 `259:183`)·SCR-005(완료, `261:157`/`276:157`)·SCR-006(중복 참여, `261:160`/`277:157`) 신규 조립 + 이모지(🎉/👋) 정식 오브제 교체 + Reason List Item 선택 인디케이터(`258:161`/`258:166`/`258:170`) 채움 라운드에 대한 감사.

**HIGH(신규) — Selection Indicator(Selected)가 Basic/Utility 트랙 규칙(면색 금지) 위반**: Graphic Assets `279:147`·화면 적용 `258:161` 모두 "Basic/Utility 트랙"으로 명시하면서 Ellipse에 솔리드 Primary fill을 채움. `icon-craft-guide.md`는 Basic 트랙에 상태별 예외 없이 "면색 금지, 순수 스트로크만"을 규정 — 미선택 상태(`258:166`/`258:170`, `fills:[]`+stroke 1.5px)는 규칙 준수, 선택 상태만 위반.

**HIGH(신규) — Reason List Item 터치 타겟 41px, WCAG 2.1 AA 최소 44px 미달**: `get_metadata` 실측(`258:160`, height=41, `px-14 py-12`+14px 텍스트) 확인. 원본 Choice Card(50px대)는 기준 충족했으나 신규 Reason List Item은 세로 padding 축소로 기준 미달.

**HIGH(기존 이슈 확산, 미해결) — Ink 뮤트 55% 캡션 대비 미달이 SCR-004/기타 모달까지 확산**: "A안"/"B안" 라벨(`258:150`/`258:155`, 12px, 계산 대비 ~3.68:1), "기타" 모달 "최소 6자 이상"(`259:189`, ~4.13:1) 모두 4.5:1 미달. 43차 HIGH(White Sheet Ink 뮤트 계열 대비 미달)와 동일 토큰(`color/text-muted-55(-on-tint)`)이 신규 화면에 재사용되며 확산. `brand-guide.md` 9-6절은 "수정하지 않음"만 명시, 사용자 승인 기록 없음.

**MEDIUM(신규) — "기타" 모달 내 Selection Indicator 레이어명이 "Frame"으로 일반화**: `259:166`/`259:170`/`259:174`가 SCR-004 base(`258:161` 등 "Selection Indicator — Selected/Unselected")와 다른 이름 — 네이밍 일관성 위반.

**MEDIUM(신규) — 신규 "Comparison Card"(A안/B안)가 2개 화면에 raw FRAME으로 중복**: `258:149`/`258:154`(base)·`259:154`/`259:159`("기타" 모달) 완전 동일 구조가 INSTANCE 아닌 독립 FRAME으로 중복 — 기존 43/45차 지적(Badge 등 raw FRAME 잔존) 패턴이 신규 오브제에도 반복.

**MEDIUM(신규) — 신규 "Text Input Field"에 Input 필수 상태 커버리지 없음**: `259:187`이 raw FRAME 단일 정적 상태(1.5px Primary 보더 고정)만 존재, `component-state-guide.md` §2(Default/Placeholder/Focus/Error/Disabled) 미충족.

**MEDIUM(신규) — Selection Indicator가 정식 COMPONENT/variant 미등록으로 Focus/Disabled 상태가 구조적으로 부재**: 라디오/체크류 §2 요구사항 미충족. `graphic-assets.md`가 "COMPONENT 승격은 이번 라운드 범위 아님"이라 명시적으로 유보한 점은 확인 — 다음 라운드 필수 후속.

**LOW — CTA press 상태 부재는 결함 아님, 정직하게 기록된 백로그로 확인**: `CTA` 컴포넌트셋(`124:1148`) 직접 재조회로 State 축 부재 재확인, `brand-guide.md` 10-1절에 design-systems 앞 명시적 스펙과 함께 요청·대기 중임을 확인 — 다음 라운드 반영 여부 재확인 필요.

**LOW — "기타" 모달 트랜지션 프로토타입 값 도구 한계로 직접 재검증 불가**: `get_motion_context`가 이 에이전트에 제공되지 않아 duration/easing 재조회 불가. 문서 기록(0.25s EASE_IN_AND_OUT)은 `motion-timing-guide.md` 범위(200~400ms) 부합하나 독립 재검증은 아님.

**PASS 다수**: 신규 조립 요소 전수 색상 토큰 바인딩(하드코딩 0건), 합성 hex 4종(`#777d89`/`#818389`/`#aaabb1`/`#afb0b4`) 독립 재계산 전부 일치, 그림자 신규 오브제 포함 0건, Celebration/Confirmation Badge 톤 구분 명확(stroke 10px/6px 짝수), 이모지 🤔 accent 허용 사례 확인.

**종합**: HIGH 3건(신규 2 + 확산 1) + MEDIUM 4건(신규) + LOW 2건, PASS 다수 — design-systems/graphic-designer 재작업 필요, 특히 대비 미달 토큰(`text-muted-55` 계열) 근본 수정이 반복 확산을 막을 유일한 방법.

### 2026-08-26 (47차) — 46차 HIGH 2건(Selection Indicator 면색 위반, Reason List Item 터치 타겟) 재검증 — 둘 다 해소 확인, HIGH 0건, LOW 1건(도구 한계로 fill=[] 바이트 단위 검증 불가)

배경: ui-designer/graphic-designer가 46차 HIGH 2건에 대한 수정을 보고, Figma 직접 재조회로 독립 재검증. 46차의 나머지 MEDIUM/LOW/Ink 뮤트 HIGH는 이번 라운드 범위 아님.

**해소 확인 — Selection Indicator(Selected) Basic 트랙 면색 위반**: `get_metadata`로 8개 관련 노드(Graphic Assets `279:147/148/149`, SCR-004 base `258:161/162`+`274:157`, "기타" 모달 `259:174`+`284:954`) 전수 존재 확인. `get_design_context`는 Ellipse/Vector 타입이 전부 flattened SVG 이미지로 export되어 raw fill 속성이 코드에 노출되지 않는 도구 한계(45차에서도 동일 한계 기록)로 직접 hex 대조는 불가했으나, `get_screenshot`을 상위 컨테이너(Reason List `258:159`/`259:164`, 335×159, native 1x)로 확대 캡처해 시각 재확인한 결과 Selected 인디케이터가 SCR-004 base·"기타" 모달 양쪽 모두 흰색 내부+파란 스트로크 링+파란 스트로크 체크(솔리드 면 없음)로 정확히 렌더링됨, Unselected는 얇은 회색 링만 유지 — 선택/비선택 시각 구분 명확, 레이아웃 깨짐 없음. 레이어명도 "기타" 모달 3개 전부 "Selection Indicator — Selected/Unselected"로 SCR-004 base와 동일하게 정정됨(46차 MEDIUM 네이밍 지적도 부수적으로 해소).

**해소 확인 — Reason List Item 터치 타겟 44px 미달**: `get_metadata` 재실측 결과 6개 노드(SCR-004 base `258:160`/`258:165`/`258:169`, "기타" 모달 `259:165`/`259:169`/`259:173`) 전부 height=45px로 WCAG 2.1 AA 최소 44px 충족. `258:159`/`259:164`(Reason List 컨테이너) 높이도 159px로 3×45+2×12(gap) 계산과 정확히 일치해 레이아웃 사이드이펙트 없음 확인.

**LOW(신규 아님, 45차 동일 패턴 재확인) — Unselected 인디케이터의 "흰색 solid fill 제거" 여부는 도구로 바이트 단위 검증 불가**: 카드 배경이 이미 흰색이라 흰색 fill 유무가 시각적으로 구분 불가능하고, get_design_context가 이 노드 타입을 SVG로 flatten해 코드상 fill 속성도 노출 안 됨(forceCode 시도해도 동일). 결함이 아니라 검증 공백 — Figma 데스크톱 Inspect 패널 수동 확인 권고.

**종합**: 46차 HIGH 2건 모두 재작업 없이 재검증 통과. 신규 회귀(다른 곳 fill 잔존, 레이아웃 깨짐, 대비 약화) 없음.

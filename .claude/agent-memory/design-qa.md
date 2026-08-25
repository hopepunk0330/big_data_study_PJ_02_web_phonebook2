# design-qa 메모리

이 파일은 design-qa가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 작업 로그

### 2026-07-18 (40차) — 마감 임박 최종 조립분 감사: 카테고리삭제거부배너(409, `1057:1626`) + 가입직후 빈 상태(`1060:2014`) + 인터랙션 리액션 실재 여부 — MEDIUM 1건 신규(Toast 진입 리액션 미확인) + PASS 다수, HIGH 0건

**PASS — `1057:1626`/`1060:2014` 문구·색상·아이콘·카운트·CTA 인스턴스 전수 확인**. **MEDIUM(신규) — Toast 등장 트랜지션 증거 미확인**(`get_motion_context` 툴 부재로 확정 불가, interaction-designer/design-pl 재확인 권고).

### 2026-07-18 (41차) — dev-pl 프론트엔드 재추출 후 `docs/screenshot/` 실제 구현 vs Figma 확정본 교차 검수 — HIGH 2건(신규) + MEDIUM 2건(신규)

**HIGH — Join 화면이 확정 Figma(코랄 배지+반전 화살표 "로그인으로 돌아가기" 전용 카드)와 다르게 로그인 폼 재사용**. **HIGH — 로고 마스코트 간헐적 렌더링 실패(41차 지목, 42차에서 자체 오탐으로 정정됨)**. MEDIUM 2건은 42차에서 해소 확인.

### 2026-07-18 (42차) — 41차 지적 4건 재확인 — HIGH2는 자체 오탐 인정·정정, HIGH1 여전히 미해결, MEDIUM1/MEDIUM2 해소 확인

**정정(자기 오탐 인정) — 로고 마스코트 간헐적 렌더링 실패는 오탐**(축소 렌더링에서 디테일 뭉개짐 오인, 원본 해상도 재확인 시 17곳 전부 정상). **여전히 미해결 — Join 전용 화면이 프론트엔드에 반영되지 않음**(login-06~09, `935:33`/`1043:9`와 괴리 지속). **해소 확인 — 409 동적배너/영문 오류 노출 둘 다 PASS.**

**종합**: HIGH1(Join 미구현) 미해결 유지, HIGH2 자체 오탐 정정, MEDIUM 2건 해소.

### 2026-08-25 (43차) — mercari 가격 UX 실험 대안 디자인: 확정 7화면(`126:2601`) + 신규/보강 컴포넌트(`126:2599`) + 스펙시트 완성도 감사 — HIGH 5건(신규) + MEDIUM 2건(신규) + PASS 다수

배경: 사용자 확정 디자인(`126:2601`, 7화면) → design-systems 컴포넌트 추출(Choice Card/Hero Price Card/CTA/Price Input/Progress Row/Product Row/Badge) → brand-designer가 `docs/design/mercari/brand-guide.md` 작성 완료 후 감사 라운드. Figma `SIBLz4S4IZbjabzhMSAgdo`.

**HIGH(신규) — 대비 미달 3계열, 전부 확정 원본(`126:2601`)에 존재, 사전 승인 기록 없음**: (1) "AI 추천" 팁 배지 `#F5F5F5` on `#3789FF`(Choice Card 우상단, 11px bold) 실측 대비 약 3.11:1 — 4.5:1 미달. (2) "빅데이터 산출로 제안" Badge_01 텍스트 `#3182F6` on `#E8F3FF`(10px bold) 약 3.31:1 — 미달. (3) Ink 뮤트(opacity 0.5/0.55) 계열 캡션 — Choice Card 설명(12px, on 흰색 약 3.80:1 / on `#E8F3FF` 약 3.68:1), HeroPriceCard "추천 판매가"(12px bold, 흰 배경 약 3.80:1), Product 서브텍스트(11px, 흰 배경 약 3.27:1) — 전부 4.5:1 미달. 다크 히어로 텍스트(화이트/Secondary블루, 대비 15:1·4.9:1)는 문제 없음 — 이번 미달은 전부 White Sheet 영역의 별도 발견으로, 브리프의 "다크 히어로 소프트닝" 예외 대상이 아니라 완전 신규 HIGH.

**HIGH(신규) — 아이콘이 전부 등록된 Icon 컴포넌트의 INSTANCE가 아니라 raw FRAME으로 조립됨**: `get_metadata` 재확인 결과 shield-check(`124:534`/`124:657`)/star-01(`147:3` 등)/chevron-right(`124:1133` 등)/아이콘1·아이콘2(`124:524`/`124:538`)가 컴포넌트 마스터·확정 화면 어디서도 `<instance>`가 아니라 `<frame>`으로 나타남 — 이 파일에 별도 등록된 Icon/* 컴포넌트 자체가 없음(FOUNDATIONS Icons 페이지 부재로 추정). `component-state-guide.md` §4 위반.

**HIGH(신규) — 신규/보강 컴포넌트 7종 전부 Figma Variable 바인딩이 전무, 완전 하드코딩**: Choice Card/Hero Price Card/CTA/Price Input/Progress Row/Product Row/Badge의 `get_design_context` 결과 전부 `bg-[#hex]`/`text-[#hex]` 리터럴만 있고 `var(--token-name, #hex)` 형태가 단 하나도 없음 — "No token = no component" 위반, 이 프로젝트 자체의 Variables 인프라(FOUNDATIONS Colors 등)가 아예 없는 것으로 추정.

**HIGH(완성도) — 컴포넌트 스펙 시트가 7종 중 4종만 존재**: `126:2599` 페이지에 Progress Row/Product Row/Price Input/Badge는 "OOO — Spec Sheet" 프레임(제목→설명→variant 그리드 순서, 인셋 x=24 통일 — 서식 자체는 4개 다 일관돼 PASS)이 있지만, **Choice Card/Hero Price Card/CTA는 스펙 시트가 아예 없음**(스크린샷 직접 확인, 컴포넌트 정의만 덩그러니 존재). 이 3개는 Figma 컴포넌트 description도 없음(Choice Card만 description 있고 스펙시트 없음, Hero Price Card·CTA는 description·스펙시트 둘 다 없음) — 문서화 이중 누락.

**MEDIUM(신규) — variant 축 이름이 전부 `State`가 아니라 `Property 1`**: CTA(Button/Disabled)·Price Input(Placeholder/Filled)처럼 실질적으로 상태를 나타내는 축도 `component-state-guide.md` §1 표준(`State`)을 따르지 않음. 다만 이 프로젝트 전반의 기존 관례(`Property 1=...`)와 일치해 신규 사고는 아님 — 다음 컴포넌트 작업 시 정정 권고.

**MEDIUM(신규) — 신규 4종(Badge/Progress Row/Product Row/Price Input)이 확정 화면 안에서 컴포넌트 INSTANCE로 치환되지 않음**: 확정 화면(`126:1951` 등) 재확인 결과 Hero Price Card/Choice Card/CTA는 화면 안에서 `<instance>`로 치환돼 있는 반면(이전 라운드 추출 작업으로 추정), Badge/Progress Row/Product Row/Price Input은 여전히 원본 그대로의 raw `<frame>` — 향후 컴포넌트 갱신이 확정 화면에 자동 반영 안 됨. 확정 화면은 읽기 전용이라 지금 고치라는 게 아니라, 다음 유지보수 라운드에서 참고할 구조적 갭으로 기록.

**PASS — B_03 상태배지 보더 누락 예외 재검증**: (1) 확정 화면 `126:1951`의 배지(`126:1966`)는 실제로 `border` 클래스 없이 `bg-white`만 있음 — 원본 무결성(안 고쳐짐) 확인. (2) 컴포넌트 마스터 Badge_03(`147:9`)은 실제로 `border border-[#dedede]` 보유 확인. design-systems·brand-designer의 기존 처리가 정확함 — 재작업 불필요.

**PASS — 값 원본 대조**: 그림자 0건(전체 스캔에서 box-shadow 클래스 전무), Eyebrow 배경 비가시 정상 재현, 색상 hex·radius·padding(Choice Card pl14/pr36/py14, HeroPriceCard px18/py24, CTA px20/py16, Price Input px14/py12/h46, 배지류 padding 전종)이 `docs/design/mercari/brand-guide.md` 수치와 정확히 일치, shield-check "선택된 카드에만" 규칙도 마스터 3 variant 전부에서 정확히 지켜짐.

**PASS — 네이밍**: "check box" → "Choice Card" 마스터 컴포넌트명 및 description 개명 완료 확인. (단 확정 화면 내 인스턴스 레이어명은 옛 이름 "check box" 잔존 — 읽기 전용 원본이라 수정 대상 아님, 정보성 기록만.)

**종합**: HIGH 5건(대비 미달 3계열, 아이콘 raw frame, 토큰 미바인딩+스펙시트 3종 누락은 완성도 HIGH로 별도 집계) + MEDIUM 2건(variant 축 네이밍, 신규 컴포넌트 미인스턴스화) + PASS 다수(B_03 예외 재검증 2건, 원본 값 대조, 네이밍 리네임). 전부 신규, design-systems/brand-designer 재작업 필요.

### 2026-08-25 (44차) — mercari "Brand Guide" 문서화 페이지(`165:10`, brand-guide.md 시각화) 감사 — MEDIUM 2건 + LOW 3건(전부 신규, 서식/데모 정확도) + 주요 항목 다수 PASS, HIGH 0건

배경: brand-designer가 확정 마크다운(`docs/design/mercari/brand-guide.md`)을 Figma 프레임으로 시각화. 컴포넌트/토큰 라이브러리가 아니라 순수 문서화 페이지라 값 정확성+`figma-page-format-guide.md` 서식 일관성만 감사.

**전제 정정(HIGH 아님, 정보성) — "Ink 뮤트 4단계 vs 5단계" 불일치 지시는 현재 상태와 다름**: 브리프는 "문서 1절엔 0.55/0.5/0.4/0.35 4단계만 명시"라고 전제했으나, `brand-guide.md` 1절 표를 직접 재확인한 결과 이미 `rgba(26,29,41,0.6/0.55/0.5/0.4/0.35)` 5단계로 기재돼 있고 "0.6=Price Input 원 단위" 매핑까지 2절 타이포그래피 표와 정확히 일치. Figma 스와치도 5개(174:57/64/70/76/82) 전부 존재해 문서와 완전히 일치 — **불일치 없음**. design-pl은 이 항목의 지시 전제(문서가 이미 갱신됐을 가능성)를 최신화할 것.

**MEDIUM(신규) — Colors 카탈로그(174:2) 16개 스와치의 보더 유무·굵기가 3가지 방식으로 혼재**: `figma-page-format-guide.md` §1 "동일 카탈로그는 동일 보더 유무·색·굵기" 위반. White Sheet(174:11)·CTA 비활성 배경(174:41)만 `border border-[#e2e6ec]`(1px)이 있고, Dark Hero(174:7)·Neutral Border(174:15)·Primary(174:19)·Secondary(174:24)·Accent Tint(174:28)·Ink(174:32) 등 나머지 순색 스와치는 보더가 전혀 없음. 상태배지 보더 스와치(174:36, `#DEDEDE`)는 `border-4`(4px)로 렌더링돼 White Sheet의 1px 보더와도 굵기가 다름 — 무보더/1px/4px 세 방식 혼재. cornerRadius(전부 `rounded-[10px]`)는 통일돼 있어 그 부분만 PASS.

**MEDIUM(신규) — Ink 뮤트/흰 텍스트 opacity 스와치(174:57~82, 7개) 데모 배경이 실제 사용 맥락과 반대**: 흰 텍스트 2종(#FFFFFF/#F5F5F5)은 다크 히어로 위에서 쓰이므로 다크 배경(`#2D3241`, 문서에 없는 임의색) 데모가 맞지만, 같은 다크칩 포맷을 Ink 뮤트 5단계(0.6/0.55/0.5/0.4/0.35)에도 그대로 복제 — 이 값들은 문서상 전부 White Sheet·CTA 비활성 배경 같은 **밝은** 배경 위 텍스트인데 데모는 어두운 배경 위에 렌더링돼 실제 시각 효과(연한 회색 텍스트)와 반대로 보임. 라벨 설명 텍스트 자체는 정확해 완전한 오정보는 아니지만, 데모 이미지만 보면 오해 소지.

**LOW(신규) — 섹션 간 세로 여백 불일치**: 0번(Concept A/B, `165:13`, bottom y=513)과 1번(Colors, `174:2`, y=573) 사이 간격 60px, 반면 1↔2/2↔3/3↔4/4↔5/5↔6 나머지 전 구간은 40px로 통일 — `figma-page-format-guide.md` §3 "프레임 사이 여백 통일" 경미한 위반(8pt 그리드 자체는 준수).

**LOW(신규) — 타이포그래피 2절 위계 개수 및 라벨 완전성**: 문서는 "Price Input 값/placeholder"(16px)와 "Price Input 통화기호·단위"(₩16px/원14px)를 별도 2개 행으로 구분하는데, Figma는 이를 하나의 예시(175:98)로 합침. 실제 렌더링 값(₩·60,000=16px Bold Ink, 원=14px Regular Ink 60%, placeholder=16px Ink 35%)은 정확하지만, 하단 라벨 텍스트가 "Noto Sans KR Bold 16px"로만 뭉뚱그려 원의 14px 차이를 명시하지 않음.

**LOW(신규) — 타이포그래피 CTA 예시 소품 padding 불일치**: 175:89 "다음 보기" 버튼 예시가 `px-20 py-14`로 렌더링돼 있으나, 문서 5절 spacing 표는 CTA 버튼 padding을 `px-20 py-16`으로 명시 — 텍스트 색상 데모용 소품이라 핵심 스펙은 아니지만 문서 값과 다른 padding이 그대로 노출됨.

**PASS — 색상 스와치 16개 hex 전수 대조**: Dark Hero #1A1D29, White Sheet #FFFFFF, Neutral Border #E2E6EC, Primary #3182F6, Secondary #3789FF, Accent Tint #E8F3FF, Ink #1A1D29, 상태배지 보더 #DEDEDE, CTA 비활성 배경 #F7F8FA, 흰 텍스트 #FFFFFF/#F5F5F5, Ink 뮤트 5단계 — 전부 `docs/design/mercari/brand-guide.md` 1절 표와 hex/역할 설명 정확히 일치.

**PASS — 보더/Radius 12개, Spacing 대표 padding 3개, 주석 2개(Eyebrow 비가시·B_03 보더 누락) 위치·내용**: `176:2`(보더/Radius) 12개 값 전부 문서 3절과 일치(White Sheet 상단 24px 비대칭 `rounded-tl/tr`만 적용도 정확). `178:2`(Spacing) 2px 그리드 눈금 13개(2~36px)와 HeroPriceCard(px18/py24)·Dark Hero(px20/py28)·Choice Card(pl14/pr36/py14) 3개 padding 다이어그램 전부 정확. 주석 2개 모두 Colors 섹션 하단(174:88/174:91)에 문서 내용 그대로 배치.

**참고**: "기존 브랜드컨셉 페이지"와의 서식 비교는 해당 페이지를 파일 내에서 찾지 못해(get_metadata 최상위 조회엔 "레퍼런스" 페이지만 노출 — 알려진 조회 한계) 수행하지 못함, `figma-page-format-guide.md` 표준만으로 내부 일관성 검증.

**종합**: HIGH 0건, MEDIUM 2건(보더 혼재, opacity 데모 배경 오맥락), LOW 3건(섹션 간격, 타이포 라벨 완전성, CTA 소품 padding) — 전부 신규. 값 정확성(색상 16/보더·radius 12/spacing/주석)은 전수 PASS. brand-designer 후속 정리 권고, 재작업 급박성은 낮음.

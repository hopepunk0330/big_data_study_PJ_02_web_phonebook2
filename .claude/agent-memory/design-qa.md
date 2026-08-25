# design-qa 메모리

이 파일은 design-qa가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 작업 로그

### 2026-07-17 (39차, 마감 임박 최종 라운드) — 38차 HIGH 3건 중 4건 재확인 지시(삭제모달 치수/코랄배지 5곳/login-알림창 버튼/NeoBtn Neutral 그림자) 독립 재검증 — HIGH 1건 잔존(삭제모달 버튼 높이) + PASS 3건 + LOW 2건(신규, 문서/네이밍 stale)

**부분 PASS/HIGH 잔존 — 연락처 삭제 모달(`941:1508`) vs 확정 원본(`501:4172`) 치수 재실측**: SummaryBox 행간격 24px, 카드 전체 높이 392px 정정 확인 — PASS. **그러나 ButtonRow 내 두 버튼(`941:3043`/`941:3045`) 실제 인스턴스 높이는 여전히 42px(원본 44px) — HIGH로 재상향**(명시적 정정 지시 후에도 미해결 + WCAG 44×44 최소 터치 타겟 미달). **(주의: 2026-07-17 design-systems 41-2절 재실측에서 44px 확정·design-qa 42px 보고 기각으로 상충 기록 남음 — 다음에 이 노드를 다시 볼 일이 있으면 최신 값으로 재검증할 것.)**

**종합**: HIGH 1건(연락처 삭제 모달 버튼 높이, 상충 기록 있음) + PASS 3건 + LOW 2건 신규.

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

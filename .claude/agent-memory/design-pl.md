# design-pl 메모리

이 파일은 design-pl이 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 팀 로스터 (참고용)
- design-prompter, design-scanner, brand-designer, design-systems, ux-designer, ui-designer, interaction-designer, motion-designer, content-designer, design-qa

## 작업 로그

### 2026-07-12 브랜드 컨셉 시안 3개 — 2차 (레퍼런스 기반 재작업)
- 라우팅: design-prompter(재작업 브리프) → brand-designer(단독 재호출, nodeId 15:2 직접 조회 지시).
- brand-designer가 nodeId 15:2로 직접 get_metadata/get_screenshot 실행, "컨셉 참고" 섹션(15:6) 내 무드보드 이미지 9장 실제 열람 확인(Y2K/레트로팝 톤).
- "브랜드 컨셉 Concepts" 페이지(fileKey zgGlMBwFglaDlaeyP4CkgR, pageId 34:2)의 기존 프레임 34:3/34:4/34:5를 새 시안으로 완전 교체(버그 수정 재작업이라 ❌ 미채택 표시 없이 덮어씀):
  - Concept A "Deskline" — #1D3A5F/#F2E9D8/#F2A93B, Space Mono+Noto Sans KR
  - Concept B "Warm Ledger" — #17A398/#FF5A76/#FFCB47, Baloo 2+Noto Sans KR
  - Concept C "Gridline" — #22252A/#EFEEE8/#FFC845, IBM Plex Sans KR+JetBrains Mono
- 상태: 사용자에게 보고, 확정 요청.

### 2026-07-12 브랜드 컨셉 3안 × 메인 화면 적용 시안 — 3차
- 사용자 요청 변경: 무드 프레임만으로 선택 어려움 → 각 컨셉이 실제 메인 화면(연락처 목록)에 적용된 모습을 봐야 최종 선택 가능. design-systems는 이 단계에 투입하지 않고(토큰 없음), 브랜드 컨셉 원본 값을 화면에 직접 적용하는 가벼운 시안만 우선 제작.
- 배치: 별도 페이지 대신 기존 "브랜드 컨셉 Concepts" 페이지(34:2, 공용) 안에서 각 브랜드 프레임 옆에 배치.
- 라우팅: design-prompter(ui-designer용 브리프) → ui-designer(단독 호출).
- 결과: 34:2 페이지에 기존 브랜드 프레임 34:3/34:4/34:5는 그대로 두고, 그 아래(y=760)에 대응 메인 화면 시안 3장 추가 — Concept A 적용(44:2)/B 적용(45:2)/C 적용(46:2). 공통: 헤더/검색/연락처리스트(7건 동일 목업)/카테고리.
- 검증: ui-designer가 screenshot+get_metadata로 기존 프레임 미수정, 토큰 미생성 확인.

### 2026-07-12 하네스 보완 1차 — 컨셉 세트 구성/파이프라인/해상도 (4차)
- 사용자가 Concept B "Warm Ledger" 확정 + "웹 화면은 실제 사이즈로, docs/planning 기반 환경도 항상 반영" 요청 → 확정 후 파이프라인(brand-designer 정식화 → design-systems 토큰화 → ui-designer 프로덕션 화면) 계획을 승인받음.
- 실행 전, 사용자가 하네스 전체 점검 요청 → 마찰 지점 3가지 식별·반영:
  1. 브랜드 컨셉 시안에 "적용 화면" 세트 미포함 → `figma-file-organization.md` "2-1" 신설.
  2. 여러 에이전트가 만든 시안 세트의 미채택 라벨링 책임 불명확 → 2번 4항에 "정식화 담당 에이전트가 세트 전체에 라벨링" 명시.
  3. 시안 단계 vs 정식 SCREENS 단계 해상도 기준 없음 → "3번" 신설(정식 화면 PC 웹 기본 1440px + docs/planning 반영). `ui-designer.md` 동일 반영.
- `design-pl.md`에 2-1/3번 반영 + tools에 `Skill` 추가. 신규 스킬 `.claude/skills/design-concept-round/SKILL.md` 생성(컨셉 라운드 유형별 워커 조합·확정 게이트·파이프라인·라벨링·보고 절차화).

### 2026-07-12 하네스 보완 2차 — 트렌드/레이아웃 다양성 + 아이콘·오브제 담당 (5차)
- Concept B 확정 파이프라인 1단계(brand-designer Brand Guide 정식화 + 미채택 라벨링) 브리프까지 design-prompter로 준비 완료, brand-designer 호출 직전에 사용자가 두 가지 추가 피드백을 줌:
  1. "레퍼런스는 잘 반영했지만 디자인 트렌드나 레이아웃의 다양성이 아쉽다" → 지금까지 3개 시안이 컬러/퍼스낼리티로만 구분되고 실제 디자인 트렌드(무브먼트)·레이아웃 구조 다양성은 강제되지 않았던 게 원인.
  2. "아이콘/오브제 담당이 없다, content-designer가 하는 거 아니냐" → 확인 결과 content-designer는 마케팅 비주얼 전용이라 제품 화면 아이콘은 범위 밖. 실제로 아이콘/일러스트 담당이 팀 정의에 빠져 있었음(진짜 공백).
- 반영 내용:
  - `figma-file-organization.md`: FOUNDATIONS에 "Icons" 페이지 추가. 2-1번에 트렌드 다양성(뉴브루탈리즘/글래스모피즘/미니멀/벤토그리드/Y2K 등 실제 트렌드에 각 시안 대응) + 레이아웃 구조 다양성(네비 위치/리스트 표현/정보밀도) 요구 추가. "2-2. 아이콘·일러스트레이션(오브제) 담당" 신설: brand-designer(스타일 방향만) → design-systems(기능 아이콘 세트, Icons 페이지) → ui-designer(조립), content-designer는 마케팅 전용이라 제외, motion-designer는 애니메이션 버전만.
  - `brand-designer.md`: 판단 기준에 "트렌드 다양성" 추가, 할 일에 "일러스트레이션/오브제 방향 정의(제작은 안 함)" 추가.
  - `design-systems.md`: Atomic Design에 "아이콘도 atom" 명시, 할 일에 "Icons 페이지에 기능 아이콘 세트 제작(마스코트/오브제는 제외)" 추가.
  - `ui-designer.md`: 판단 기준에 "레이아웃 구조 다양성"(컨셉 단계 한정) 추가, 할 일에 "Icons 세트만 사용해 조립, 임의 아이콘 생성 금지" 추가.
  - `design-concept-round` 스킬: 1단계에 "다양성 체크"(트렌드+레이아웃) 공통 원칙 추가, 3단계 파이프라인에 design-systems 아이콘 세트 생성 단계 추가.
- 브랜드 확정 파이프라인 1단계(brand-designer Brand Guide 정식화)는 이후 별도로 실행 완료됨(`brand-designer.md` 참고, 52:2).

### 2026-07-12 연락처 목록 레이아웃 시안 A/B/C 재작업 — placeholder 버그 수정 (6차, 최신)
- 배경: 브랜드는 Concept B "Warm Ledger"로 확정·Brand Guide 정식화 완료된 상태(`brand-designer.md` 참고). 그런데 3차 라운드에서 만든 "연락처 목록 메인 화면" 적용 시안(34:2 페이지의 45:2, Concept B 적용)이 기획 문서 요건을 전혀 반영하지 않은 채 "검색창+연락처 7건" 제네릭 placeholder였다는 걸 사용자가 지적. Concept A/C 적용 화면(44:2/46:2)은 이미 미채택 브랜드에 딸린 것이라 이번 작업 범위 아님.
- 라운드 유형 판단: Type (C) "화면 레이아웃만" 라운드이나, design-systems 토큰이 아직 없어 `ui-designer.md`의 "브랜드 확정 전 단계" 예외를 적용 — design-systems 미투입, Warm Ledger 원본 hex/폰트 값을 ui-designer가 직접 사용. design-concept-round 스킬 로드해 1단계(design-prompter→ui-designer 단독 호출) 절차 확인 후 진행.
- design-prompter에게 ui-designer 브리프 작성 요청 → docs/planning 화면정의서/기능정의서 실제 열람 지시, 6개 필수 반영 요소(검색/필터, 목록 필드, 카테고리, 액션 진입점, 상태 표현, placeholder 금지) 체크리스트화, 레이아웃 구조 다양성(네비 위치/리스트 표현 방식/정보 밀도) 축 3개 명시, 44:2/46:2 불가침 명시.
- ui-designer 단독 호출(design-systems 등 다른 워커 없음) → `docs/planning/02_...화면정의서_v1.0.pdf`(SCR-002/003), `03_...기능정의서_v1.0.pdf`(FN-009/010, ContactCreate/CategoryCreate 스키마)를 직접 읽고 반영. 34:2 페이지의 45:2를 삭제하고 Layout A(62:2)/B(62:6)/C(62:10)로 교체(y=1650, 라벨 없이 완전 덮어씀 — 버그 수정 재작업이라 ❌ 미채택 표시 안 함).
  - Layout A(62:2): 상단 헤더 내비 + 카테고리 태그 필터 + 카드형 단일 컬럼, 정보밀도 중간.
  - Layout B(62:6): 좌측 사이드바 내비(카테고리 건수 배지) + 테이블형 리스트, 정보밀도 높음.
  - Layout C(62:10): 얇은 상단 헤더 + 칩 필터 + 2열 그리드 타일, 정보밀도 낮음(여백 확대).
  - 공통 반영 요소: 검색(이름), 추가 폼(이름/전화번호/주소/종류), 목록 필드(이름/전화번호/주소/종류 배지+수정/삭제), "총 N건", 동명이인 사례, 카테고리 관리(추가/수정/삭제), 헤더 "{username}님+로그아웃"(세션/격리 신호), SCR-900 메시지 배너.
  - 검증: get_metadata로 44:2/46:2 자식 수 불변 확인(미수정).
- 상태: 시안 3개(Layout A/B/C) 완성, design-concept-round 2단계 확정 게이트 — 메인 세션에 보고 후 여기서 멈춤. 사용자 확정([메인 세션 확인] 형식) 전까지 정식화(SCREENS 단계 프로덕션 화면, design-qa 등) 진행하지 않음.

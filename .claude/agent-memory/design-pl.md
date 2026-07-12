# design-pl 메모리

이 파일은 design-pl이 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 팀 로스터 (참고용)
- design-prompter, design-scanner, brand-designer, graphic-designer, design-systems, ux-designer, ui-designer, interaction-designer, motion-designer, content-designer, design-qa

## 작업 로그

### 2026-07-12 Layout A/B/C 프레임 라벨링 — 2차 시안 네이밍 규칙 소급 적용 (7차)
- 배경: `figma-file-organization.md` 2-1-B번에 2차 시안 네이밍 규칙(1차 확정 라벨 + `-1/-2/-3` 접미사, A/B/C 재사용 금지) 신설. 6차에서 만든 "Layout A/B/C"(62:2/62:6/62:10, 34:2 페이지)는 이 규칙 이전 산물이라 이름이 규칙과 안 맞는다고 사용자 지적. 메인 세션이 "[메인 세션] 라벨링 전용 작업 지시"로 재요청.
- 판단: 순수 이름표 변경(재작업/재디자인 아님, 확정 게이트 아님)이라 확정 게이트 절차 없이 바로 진행. design-prompter(브리프) → ui-designer(단독 호출) 순서만 지킴.
- 결과: `62:2` "Layout A" → "B-1", `62:6` "Layout B" → "B-2", `62:10` "Layout C" → "B-3" (내부 라벨도 동일 규칙 반영). 34:3/34:4/34:5·44:2/46:2 이름·자식 수 변동 없음 확인.
- 상태: 라벨링 완료. 이 프레임들은 여전히 "2차 시안 확정 게이트" 대기 상태였음(당시엔 미확정).

### 2026-07-12 B-2 확정 후 표준 파이프라인 — 아이콘→토큰/컴포넌트→SCREENS 파일럿 3개 (8차)
- 배경: 메인 세션이 "[메인 세션 확인]" 형식으로 B-2(62:6, 좌측 사이드바+테이블형 리스트) 최종 확정을 전달. Brand Guide(52:2) 정식화는 기존 완료 상태. `figma-file-organization.md` 2번 4항 표준 파이프라인의 나머지 단계(아이콘 필요 여부 판단 → design-systems 토큰/컴포넌트 → ui-designer SCREENS 파일럿)를 순서대로 진행하라는 지시.
- 아이콘 필요 여부 판단: B-2가 "정보 밀도 높음" 테이블형이라 행 액션을 텍스트 버튼 대신 아이콘 버튼으로 압축하는 것이 합리적이라 판단 → 필요로 결론, graphic-designer 투입.
- 순서(매 단계 design-prompter로 워커별 브리프 작성 후 단독 호출, 병렬 호출 없음):
  1. **graphic-designer**: 기능 아이콘 8종(Search/Add/Edit/Delete/Category/Logout/Alert/User) 24px 단일 기본형 제작. "Graphic Assets" 페이지(90:2, Brand Guide 다음) 신설. Brand Guide 실물(52:3) 재확인해 컬러/아웃라인(#1C1F21, 3px) 그대로 적용. variant/마스코트/빈상태그래픽/애니메이션 레이어는 범위 밖으로 명시 배제(빈 상태는 로고 심볼 재사용이라 별도 제작 불필요).
  2. **design-systems** (첫 투입): Primitive→Semantic→Component 토큰(Colors 95:2/Typography 95:3/Spacing 95:4) + Icons 페이지(96:7, graphic-designer 원화 8종 정식 등록, 새로 안 그림) + 파일럿 3화면에 실제 쓰이는 컴포넌트 8종만 제작(Button 97:8/Input 100:2/Select 101:3/Badge 102:3/Table Row 103:3/Sidebar Nav Item 103:92/Alert 104:2/Avatar 104:127). WCAG AA 검증(success/error 색상은 대비 부족해 본문 텍스트 금지, 아이콘·보더·배경 전용으로 한정하는 규칙 채택). 과잉 컴포넌트(모달/토스트 등) 생성 안 함.
  3. **ui-designer**: SCREENS 구역에 파일럿 3개 신설 — Login(108:2), Contacts — With Data(109:2), Contacts — Empty(111:2). 1440px, docs/planning 요소(placeholder 문구 원문, 동명이인 1쌍, 카테고리 관리, SCR-900 성공/오류 각 1건씩 배분) 실제 반영, design-systems 컴포넌트/토큰만 사용(하드코딩 없음), 빈 상태는 Brand Guide 로고 심볼(54:24) clone 재사용.
- 갭 발견(ui-designer 보고): Heading/Label 텍스트 스타일 토큰 부재(임시로 직접 굵기 지정, 색상만 토큰 바인딩), Table Header 컴포넌트 부재(일반 텍스트 행으로 대체) — 다음 라운드에서 design-systems 보완 필요할 수 있음.
- 상태: 파일럿 3개 완성, 3-B번 피드백 루프 단계 진입 — design-qa 투입하지 않고 메인 세션에 보고 후 멈춤.

### 2026-07-12 파일럿 피드백 수정 1차 — Elevation 토큰 신설 + Alert 바인딩 + Button WCAG 대비 교정 (9차)
- 배경: 8차에서 만든 파일럿 3개(Login 108:2/Contacts—With Data 109:2/Contacts—Empty 111:2)에 대해 사용자가 스크린샷으로 결함 2건 지적(메인 세션이 "[메인 세션] 파일럿 화면 피드백"으로 전달, 3-B 피드백 루프 단계라 확정 게이트 아님 → 승인 절차 없이 바로 진행): (1) Alert(104:2)에 elevation(그림자) 토큰 자체가 없어 좌측 컬러 보더만 있고 배경과 경계 없이 붕 떠 보임. (2) 로그인 버튼(Button 97:8 primary variant) 텍스트가 주조색(#17A398) 배경과 저대비라 WCAG AA 위반(명백한 버그로 규정, 판단 사안 아님).
- 순서(매 단계 design-prompter 브리프 → 워커 단독 호출):
  1. **design-systems**: 사전 진단에서 State Ledger 기록("브랜드색 배경엔 ink 텍스트 고정")과 실물이 어긋나 있음을 확인(97:8의 Primary+Default 2 variant Label이 실제로는 `component/button-text-disabled`(gray/400, 대비 1.22:1)에 잘못 바인딩)하고 실측 기반으로 수정. 작업 내용: (a) Elevation 토큰 신설(Primitive 7개[FLOAT 5+COLOR 2, ink 기반 저투명도] → Semantic Effect Style 2개 `Elevation/Raised`/`Elevation/Overlay`, Alert/토스트/드롭다운/모달=적용 대상·버튼/인풋/카드=미적용 대상으로 매핑 문서화, FOUNDATIONS "Elevation" 페이지 116:5 신설). (b) Alert(104:2, Success/Error 2 variant)에 `Elevation/Raised` 바인딩. (c) Button(97:8) 8 variant 전수 WCAG 재점검 — Primary+Default(Text/IconText) 2개만 실제 FAIL(1.22:1)이라 기존 `color/text-primary`로 재바인딩(신규 토큰 없이 재사용, 5.31:1 PASS). Secondary는 원래 정상(16.57:1). Disabled 4종은 전부 1.93:1 FAIL이지만 이번 요청 범위 밖이라 손대지 않고 별도 보고만.
  2. **ui-designer**: 파일럿 3화면에서 Alert/Button 인스턴스가 컴포넌트 레벨 수정을 오버라이드 없이 정상 상속했는지 진단(재조립은 오버라이드로 상속이 끊긴 경우에만 수행하는 조건부 작업으로 브리핑). 진단 결과 3화면 전부 오버라이드 없음 → 자동 상속 확인, 실제 수정 작업은 발생하지 않음(Contacts — Empty 111:2엔 애초 Alert 인스턴스가 없었다는 점도 확인). 읽기 전용 스크립트만 실행해 레이아웃/구조 변경 0건.
- 범위 외로 남겨둔 기지 이슈: Button Disabled variant 4종 전부 WCAG FAIL(1.93:1) — 이번 요청(활성 상태 버그)과 무관해 손대지 않음, 다음 라운드 후보로 기록.
- 상태: 수정 완료, 메인 세션에 보고 후 멈춤. design-qa나 전체 화면 확장으로 넘어가지 않음 — 사용자가 이 수정 결과를 확인하기 전까지 후속 단계 진행 안 함.

### 2026-07-12 Brand Guide 완성 + B-2 확정 스펙 문서화 + SCREENS 파일럿 재작업 (10차, 최신)
- 배경: 사용자가 직접 결함 2건 확인(메인 세션이 "[메인 세션] 사용자 지시로 재작업 진행"으로 전달, 확정 게이트 아닌 재작업/보완): (1) Brand Guide 페이지(52:2/52:3)가 "만들다 만" 상태로 미완성. (2) 8차에서 만든 SCREENS 파일럿(108:2/109:2/111:2)이 확정된 2차 시안 B-2(62:6, 좌측 사이드바+테이블형 리스트, 고밀도)를 이어받아 발전시킨 게 아니라 포인트 컬러/느낌만 참고해 사실상 재해석한 결과물이었음. 하네스 정책 변경(2-3번: 확정 시 프레임 직접 재관찰 의무화, 3-B번: 파일럿=발전이지 재해석 아님, 스타일 소스 오브 트루스가 `docs/design/*.md` 3파일로 명문화, 2번 5항: 결함 재작업도 삭제 금지·라벨만 변경 예외 없음)을 그대로 적용해 진행.
- 순서(매 단계 design-prompter 브리프 → 워커 단독 호출, 병렬 없음):
  1. **brand-designer**: 기존 요약을 베끼지 않고 `34:4`(Concept B 톤 프레임)와 `62:6`(B-2)을 `get_screenshot`/`get_design_context`로 직접 재관찰. hex/폰트명 외에 보더 위계(그림자 없음, 잉크 #1A1A1A 두께 3/2.5/1.5/1px + 헤어라인 1px #E0E0E0 예외), 라운드 스케일(16/10/8/5/999), 4px 그리드 간격 리듬, 정보 밀도 타이포 스케일, 색상 로직, 장식 모티프(로고 배지+pill 배지뿐)까지 기록. Brand Guide 페이지(52:3)에 신규 "레이아웃 관례(Layout Convention — B-2)" 섹션(125:2) 추가로 완성(기존 7개 섹션은 삭제·수정 없이 보강만). `docs/design/brand-guide.md` 덮어씀.
  2. **design-prompter**: brand-designer 관찰 내용 + brand-guide.md 대조해 `docs/design/confirmed/b-2-contacts-layout.md` 신규 작성(디렉토리 신설). 적용 범위 절(사이드바+테이블 구조=Contacts 전용, 보더/라운드/간격/타이포/색상=파일럿 공통)로 이전 재해석 원인을 구조적으로 방지. 보더/라운드/간격/타이포/색상 전부 수치표로 재현 가능하게 정리.
  3. **ui-designer**: (1단계) 기존 파일럿 3개(108:2/109:2/111:2) 이름 앞에 `❌ 폐기 — B-2 레이아웃 미반영(재해석됨) — ` 라벨만 부착(시각 내용 무수정, 삭제 없음). (2단계) 같은 3개 페이지에 신규 파일럿 생성 — Login(128:16)/Contacts — With Data(131:147)/Contacts — Empty(133:51), 1440px. `b-2-contacts-layout.md`를 최우선 근거로 B-2(62:6)를 재확인하며 사이드바 212px 고정폭+블록 순서(로고→카테고리 내비→카테고리 관리→새 카테고리 폼, "전체" 필터 nav 아이템 복원)와 테이블 관례(앰버틴트 헤더, 1px 헤어라인 구분선, 카테고리 인라인 텍스트) 그대로 이어받아 발전. 기존 design-system.md 컴포넌트(Button/Sidebar Nav Item/Alert/Table Row)가 confirmed 문서 값과 충돌하는 4곳은 raw 프레임으로 재구현(토큰 우선순위 규칙대로 confirmed 문서 우선), 충돌 없는 Icon 8종·Avatar는 기존 컴포넌트 인스턴스 재사용.
- 상태: Brand Guide 완성 + 확정 스펙 문서화 + 새 파일럿 3개 제작 완료. design-systems 재추출·design-qa로 넘어가지 않고 메인 세션에 보고 후 멈춤 — 사용자가 새 파일럿을 확인·승인하기 전까지 후속 단계 진행 안 함.

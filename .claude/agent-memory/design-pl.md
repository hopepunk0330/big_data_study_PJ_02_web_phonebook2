# design-pl 메모리

이 파일은 design-pl이 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 팀 로스터 (참고용)
- design-prompter, design-scanner, brand-designer, graphic-designer, design-systems, ux-designer, ui-designer, interaction-designer, motion-designer, content-designer, design-qa

## 작업 로그

### 2026-07-12 Brand Guide 완성 + B-2 확정 스펙 문서화 + SCREENS 파일럿 재작업 (10차)
- 배경: 사용자가 직접 결함 2건 확인(확정 게이트 아닌 재작업/보완): (1) Brand Guide 페이지(52:2/52:3)가 미완성. (2) 8차 SCREENS 파일럿(108:2/109:2/111:2)이 확정 2차 시안 B-2(62:6)를 재해석했음. 하네스 정책 변경(2-3번/3-B번/2번 5항)을 적용.
- brand-designer가 34:4/62:6 재관찰해 Brand Guide 완성 → design-prompter가 `docs/design/confirmed/b-2-contacts-layout.md` 작성 → ui-designer가 기존 파일럿에 `❌ 폐기 —` 라벨만 붙이고 신규 파일럿 3개(128:16/131:147/133:51) 제작(confirmed 문서 최우선 근거).
- 상태: 완료 후 메인 세션 보고, 사용자 승인 전까지 후속 단계 대기.

### 2026-07-12 SCREENS 3차본 결함 수정 — raw→컴포넌트, 터치 타겟 44×44, 빈 상태 그래픽/레이어명/문서 모호성 (11차)
- design-qa 3차 파일럿(153:19/153:373/153:547) 감사 결과 HIGH 2/MEDIUM 2/LOW 1 → design-systems(컴포넌트 7개 재작성, 토큰 9개 신설)→design-prompter(confirmed 문서 모호성 해소)→ui-designer(인스턴스 전환)→중간 조정(사이드바=teal/본문=amber 확정)→design-systems 2차 후속→ui-designer 2차 후속→design-qa 최종 재감사 전 항목 PASS.
- 상태: 결함 5건+연쇄 발견 4건 전부 해소·재검증 완료. 메인 세션 보고 후 대기.

### 2026-07-13 "등록된 아이콘 실사용" 규칙 첫 실행 — Row Action Button/Input/헤더 로그아웃 아이콘 바인딩 (12차)
- Icons 8종 중 7종이 파일럿에서 텍스트 버튼으로 대체돼 있던 문제. design-systems(Row Action Button Danger variant 버그 수정+Input 검색 아이콘 프로퍼티 신설)→ui-designer(인스턴스 교체, edit-action 아이콘 오버라이드 버그 추가 발견·수정)→design-qa(신규+회귀 전부 PASS, 문서 동기화 누락 MEDIUM 3건은 다음 라운드 후보로 남김).
- 상태: Figma 실제 결함 전부 해소. 메인 세션 보고 후 멈춤.

### 2026-07-13 파일럿 스크린샷 재피드백 4건 — 인스턴스 한정 수정, design-systems 완전 배제 (13차)
- 사용자 스크린샷 4장 지적(행 액션 아이콘 전용화 후퇴/검색 아이콘 비율/사이드바 추가 버튼 색/Select 화살표 이질감). design-systems 미투입 원칙(파일럿 미승인 상태) 준수, ui-designer 단독으로 3화면 인스턴스만 detach/오버라이드로 수정. 결함1(사이드바)은 브리프 문면과 다르게 판단(teal-on-teal 가독성 문제로 ink 텍스트 유지, 배경색 박스로 구분)해 근거와 함께 보고. 결함2는 실측 결과 이미 정상이라 미수정.
- 상태: 4건 전부 처리 완료, design-qa 미투입(사용자 직접 확인 예정). 메인 세션 보고 후 멈춤.

### 2026-07-13 화이트 텍스트 토큰 신설 + 파일럿 3페이지→1페이지 통합 (14차, 최신)
- 배경: 메인 세션이 "이전 라운드가 세션 한도로 중간에 끊겼다"며 재개 — 1번(아이콘 2트랙 분리, graphic-designer 완료분)은 이미 `docs/design/graphic-assets.md`에 반영돼 있어 확인만 하고 재작업 없이 넘어감. 남은 2번/3번 진행, 확정 게이트 아니라 승인 절차 없이 바로 진행.
- **2번 (design-systems, 사용자 직접 요청한 시스템 레벨 작업이라 파일럿 미승인 상태 예외 허용)**: `color/text-inverse`(→기존 `color/gray/0` alias, 신규 primitive 없음) semantic 토큰 신설. WCAG 상대휘도로 브랜드 3색×흰 텍스트 정밀 계산(design-pl/design-prompter 사전 계산과 소수점까지 일치): teal 3.1200:1(큰 텍스트 PASS)/coral 3.0111:1(큰 텍스트 간신히 PASS)/amber 1.5122:1(**큰 텍스트 기준조차 FAIL**). 최종 범위: Display/제목급 텍스트+teal·coral 배경에만 허용, amber는 흰 텍스트 사용 전면 금지로 명확히 구분 문서화, Body/Caption은 기존 ink 고정 규칙 불변. `docs/design/design-system.md` 갱신, Figma 변수 `VariableID:219:2` 생성.
  - **원 지시("브랜드 3색 전부 큰 텍스트는 통과")가 정확하지 않았음을 사전 검증에서 미리 잡아 브리프에 반영** — amber만 예외적으로 큰 텍스트도 실패한다는 사실을 design-systems가 안이하게 넘기지 않도록 명시했고, 실제로 그대로 확인됨.
- **3번 (ui-designer)**: Login(106:2)/Contacts—With Data(106:3)/Contacts—Empty(106:4) 3개 페이지 프레임 전부(총 12개, 예상보다 많음)를 새 "파일럿" 페이지(`222:524`)로 통합 이동, 좌→우 macro 순서(Login→With Data→Empty)×세대별 세로 스택(최신 위/폐기본 아래) 배치, 기존 3페이지 삭제, `insertChild(17, ...)`로 위치 고정, `docs/design/design-system.md` 페이지 순서표 갱신. 내용·라벨 전수 대조로 무수정 확인.
  - **예상 밖 발견 1 (design-pl이 사용자에게 반드시 전달할 것)**: `106:3`(Contacts—With Data)에 브리프 기대치(파일럿 3세대)보다 많은 프레임이 있었음 — "확정 디자인 - 절대 원본 건들지 말것"(`214:349`)과 "Document"(`215:2775`/`214:852`) 3개가 파일럿과 무관한 별도 보호 콘텐츠로 섞여 있었다. ui-designer가 삭제하지 않고 판단 범위를 넘어선다고 보아 파일럿 페이지 내 비교 그리드와 분리된 하단 영역(y=5000)으로만 이동(내용 무수정). **이 콘텐츠가 원래 왜 거기 있었는지, 어디로 옮겨야 맞는지는 design-pl/사용자 확인이 필요** — 방치하지 말 것.
  - **예상 밖 발견 2**: `design-system.md`의 페이지 순서표 자체가 이번 작업 이전부터 실제 파일과 어긋나 있었음(idx1이 실제로는 "Brand Guide"가 아니라 "브랜드 컨셉 Concepts", 표에 없는 페이지 2개 "컨셉, 디자인시안"/"UI-design "가 이미 존재). 이번 범위(idx17 교체) 밖이라 손대지 않고 이슈로만 기록 — 다음 라운드에서 design-scanner나 design-systems로 전체 페이지 순서표 재정합 필요.
- 상태: 2번/3번 모두 완료. design-qa 미투입(구조 이동·토큰 신설 라운드라 화면 변경 없음, 확정 게이트도 아님). 메인 세션에 위 2건의 예상 밖 발견을 반드시 포함해 보고 후 멈춤 — 후속 워커 호출 없음.

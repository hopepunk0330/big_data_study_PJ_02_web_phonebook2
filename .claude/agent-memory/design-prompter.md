# design-prompter 메모리

이 파일은 design-prompter가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 작업 로그

### 2026-07-13 — design-qa 브리프: 결함 수정 라운드 3(마지막) — 아이콘 실사용 반영 재감사 + 11차 PASS 항목 회귀 확인
- **원본 요청**: design-systems(컴포넌트: Row Action Button Danger 아이콘 오배선 정정/Input 검색 아이콘 프로퍼티/헤더 로그아웃 패턴)+ui-designer(파일럿 3화면 반영, 추가로 edit-action 인스턴스 96:27 강제 오버라이드 버그 발견·정정)가 끝난 뒤 design-qa가 최종 재감사. 이전 라운드(11차)에서 이미 PASS 확정된 HIGH2/MEDIUM2/LOW1이 이번 작업으로 회귀하지 않았는지도 함께 확인해야 함.
- **구체화 포인트**: (1) 핵심 신규 감사 항목을 "노드 단위로" 명시 — edit/delete-action이 실제로 다른 아이콘을 렌더링하는지(동일 버그가 두 번 재발한 이력을 근거로 특히 엄격히), 검색 Input 아이콘 노출+Search Row 정렬, 헤더 로그아웃 라벨/아이콘/WCAG 대비, 아이콘 8종(Search/Add/Edit/Delete/Category/Logout/Alert/User) 전수 재확인. Icon/Add·Icon/Category 미해결 2건은 "이번 라운드 결함"이 아니라 "보류 근거가 타당한 알려진 갭으로 문서화됐는지"를 판단하도록 감사 관점을 구분해 명시. (2) 회귀 확인 대상(11차 HIGH2: raw 프레임 전환/44×44 터치 타겟, MEDIUM2: 빈 상태 그래픽/로고 심볼 노드명, LOW1: confirmed 문서 표기)을 항목별로 열거, 특히 Row Action Button 44×44 히트 영역이 아이콘 교체로 깨지지 않았는지 강조. (3) 참고 문서 3종(design-system.md 최신/confirmed b-2-contacts-layout.md/figma-file-organization.md 2-2절) 명시. (4) 출력 형식을 PASS/FAIL 항목별 명시+FAIL 시 재작업 담당(design-systems/ui-designer) 판단까지 요구, design-qa는 발견만 하고 직접 수정하지 않는다는 역할 경계 재확인.

### 2026-07-13 — ui-designer 브리프: 사용자 지적 시각 결함 4건 — 파일럿 3화면 "인스턴스 한정" 수정 (마스터 컴포넌트 미변경, design-systems/design-qa 이번 범위 아님)
- **원본 요청**: 사용자가 파일럿 3화면 스크린샷을 직접 보고 결함 4가지 지적. 파일럿이 아직 최종 확정 전이라 design-pl이 "이번엔 컴포넌트(design-systems)를 건드리지 않고 3개 화면 인스턴스만 수정"으로 범위를 명시적으로 좁힘 — 이전 라운드들과 반대 방향(보통 컴포넌트 먼저 고치고 화면 재바인딩)이라는 점이 이번 브리프의 핵심 특이점.
- **핵심 판단(문서 원문 재확인으로 수정된 부분)**: 결함3 "새 카테고리 추가 버튼 색"에서 원 요청은 "amber 복원"이라고 썼지만, confirmed `b-2-contacts-layout.md` 6절 원문을 직접 재확인한 결과 **사이드바 카테고리 추가 버튼은 amber가 아니라 teal(Primary)**이 정답(본문 "추가" 행 버튼이 amber). 기억/추정이 아니라 문서 원문을 근거로 이 착오를 브리프에서 정정해 전달 — "모호함은 여기서 끝낸다" 원칙 적용 사례.
- **구체화 포인트**:
  1. 결함1(Row Action Button 아이콘 전용→텍스트 복원): Table Row 6곳(참고치, get_metadata 재확인 우선)+사이드바 카테고리 관리 행 전부(정확한 개수 실측) 대상. 마스터 컴포넌트(`166:421`) 미변경 원칙상 인스턴스 detach 후 로컬로 아이콘 제거→순수 텍스트 라벨("수정"/"삭제")로 재구성 지시. 색상은 원 요청 표현("초록/빨강 계열")을 기존 시맨틱(수정=`color/text-accent` #0F7A6E AA 근거, 삭제=coral/500 대비 직접 실측 후 미달이면 로컬 한정 톤다운, 새 전역 토큰 생성 금지)에 매핑해 구체화. 보더/radius/padding은 confirmed 2·3·4절의 기존 소형 버튼 값(1px, radius/xs 5px, 8×4px) 재사용해 이질감 방지, 44×44 히트 규칙은 아이콘 전용 컴포넌트 전제였음을 지적해 텍스트 버전엔 그대로 적용 안 됨을 명시.
  2. 결함2(검색 아이콘 비율): Input의 `Show Search Icon`/`Icon` 프로퍼티로 들어간 Icon/Search 인스턴스 크기를 16×16 또는 20×20 정사각형 고정, constraints/오토레이아웃 sizing mode 점검까지 포함.
  3. 결함3(카테고리 추가 버튼 색): teal(Primary) 배경 복원이 정답임을 명시하고, 원인 진단(오버라이드로 fill 삭제됐는지 vs variant 오선택)을 먼저 하도록 지시.
  4. 결함4(Select caret 이질감): 새 아이콘 창작 금지, 기존 caret 벡터의 스트로크만 3px+ink 컬러로 로컬 조정하는 수준으로 범위 한정. Icons 페이지(96:7)에 대체 가능한 화살표가 이미 있으면 그걸 우선 사용.
  5. 원칙 재천명: 오버라이드 우선, 구조 변경 필요시에만 해당 인스턴스 detach. 수정 후 3화면 전부 get_screenshot 재확인 없이는 완료 보고 금지. 보고 형식은 4가지 각각 "무엇을 어떻게 고쳤는지+스크린샷 재확인 결과"로 명시. design-systems/design-qa는 이번 범위 아님을 브리프에 명시(혼동 방지).

### 2026-07-13 — design-systems 브리프: "화이트 텍스트 토큰"(`color/text-inverse`) 신설 — Display/제목급 전용, 브랜드 3색 중 amber 사용 금지 확정, 파일럿 미승인 상태 예외 호출
- **원본 요청**: 사용자가 직접 요청한 시스템 레벨 작업(신규 semantic 토큰). SCREENS 파일럿이 아직 사용자 최종 승인 전이라 원칙(`figma-file-organization.md` 3-B번)상 design-systems를 이 시점에 부르면 안 되지만, "사용자 직접 요청 + 신규 토큰 신설"이라는 이유로 design-pl이 명시적 예외로 허용 — design-systems 자신의 정의("승인 전이면 순서 위반이니 확인 요청 후 멈춘다")를 브리프에서 선제적으로 무력화할 근거를 명시해야 했음.
- **사전 검증(design-prompter가 직접 재계산)**: WCAG 2.1 상대휘도 공식으로 세 배경×흰 텍스트 대비를 독립적으로 재계산해 design-pl의 사전 계산과 소수점까지 정확히 일치 확인 — teal `#17A398` 3.122:1(큰 텍스트 PASS/본문 FAIL), coral `#FF5A76` 3.011:1(큰 텍스트 간신히 PASS/본문 FAIL), amber `#FFCB47` 1.513:1(큰 텍스트조차 대폭 FAIL). 이 재검증 결과를 브리프에 "참고용 교차검증"으로 명시하되, 최종 계산 책임은 design-systems 자신의 재계산(design-systems.md 판단 기준에 이미 있는 원칙)에 있음을 분명히 함.
- **구체화 포인트**:
  1. 대상 한정: 브랜드 3색(teal/coral/amber) 배경 전용 논의, gray 계열(surface/background)에는 이 토큰 적용 대상 아님을 명시.
  2. 신규 primitive 생성 금지 — `color/text-inverse`는 기존 `color/gray/0`(#FFFFFF) alias로만 신설, Semantic Colors 컬렉션(`VariableCollectionId:95:16`)에 추가.
  3. 적용 범위 문서화를 "좁고 정확하게" — Display/제목급(text style `Display/Latin`/`Display/KR` 또는 24px+/Bold+ 상당)에 한해 PASS 배경(teal/coral, 조건부)에서만 허용, amber는 계산상 큰 텍스트 기준도 미달이라 "사용 금지 배경"으로 명시 표기. Body/Caption은 대상에서 완전히 제외 — 기존 ink 고정 규칙 불변임을 재천명.
  4. 기존 "핵심 접근성 결정" 절의 "브랜드색 배경 위 텍스트=ink 고정" 규칙과 신규 토큰이 모순되지 않도록 관계 명시(본문은 기존 규칙 그대로, 신규 토큰은 Display/제목급이라는 좁은 예외).
  5. `docs/design/design-system.md` 3개 절(변수 컬렉션/핵심 접근성 결정/알려진 갭) 갱신 지시, Figma Semantic Colors 컬렉션에도 실제 변수 생성.
- **범위 제한**: 화면 실제 적용(어느 컴포넌트/화면에 쓸지)은 이번 브리프 밖 — 토큰 신설·문서화까지만, 화면 적용은 별도 라운드(ui-designer). Button Disabled WCAG 등 기존 알려진 갭은 건드리지 않음.
- **보고 요구사항**: design-pl에게 (a) 3색 각각 정확한 계산 결과, (b) 최종 허용/금지 배경 구분, (c) 사전 계산과 실제 결과 일치 여부를 반드시 포함해 보고하도록 명시.

### 2026-07-13 — 확정 스펙 문서 작성: 사용자 직접 확정 디자인 8개 프레임 (`docs/design/confirmed/user-confirmed-final-design.md`)
- **원본 요청**: 사용자가 Figma에 직접 만든 8개 프레임(main/main-수정/main-삭제/main-검색없음/Join/login/login-알림창/main-알림창, fileKey `zgGlMBwFglaDlaeyP4CkgR`)을 "확정 디자인 - 절대 원본 건들지 말것-"으로 최종 확정 — 기존 AI 파일럿(B-2 기반)을 대체. brand-designer가 이 8개를 직접 관찰해 `docs/design/brand-guide.md`를 전면 갱신한 뒤, design-prompter가 2-3번 규칙에 따라 확정 스펙 문서를 작성하는 작업(브리프 발전이 아니라 문서화 작업).
- **작업 성격**: 통상적인 워커 브리프가 아니라 2-3번 "확정 스펙 문서" 작성 — 여러 전문 분야(design-systems/ui-designer/graphic-designer/interaction-designer/ux-designer)가 동시에 참고하는 공유 악보이므로 brand-guide.md보다 더 촘촘하게, 8개 화면 각각에 스펙이 어떻게 적용되는지까지 재구조화.
- **핵심 판단**: (1) brand-guide.md는 토큰 카테고리별(컬러/타이포/보더 등)로 정리되어 있어 "화면별로 어떻게 조합되는지"가 빠져 있음 — 이 문서의 핵심 부가가치는 8개 화면 각각의 레이아웃 구조·상태를 새로 서술한 10절("화면별 상세 스펙")임. (2) brand-guide.md가 명시한 두 가지 "그대로 전달해야 할 참고사항"을 임의로 축약하지 않고 원문 취지 그대로 문서에 포함: ① 편집 모달 TypeSelector 칩 색상이 CatBadge 팔레트와 다른 불일치(design-systems가 정리 판단할 대상, design-prompter가 임의로 통일하지 않음) ② 하드 스티커 그림자와 소프트 블러 그림자를 별개 effect 토큰으로 분리해야 한다는 점. (3) 이전 b-2-contacts-layout.md와 이번 문서가 로고 워드마크 웨이트(Bold vs ExtraBold)·색상(고정 딥틸 vs 배경별 반전)에서 서로 다른 값을 기록하고 있음을 명시적으로 대조해 혼동 방지 — 최신 소스(이번 문서)가 우선임을 표기.
- **문서 구성**: 체크리스트(로고/퍼스낼리티/구조 3대 영역) → 확정 배경 → 8개 프레임 표 → 브랜드 트라이앵글 → 컬러(팔레트/CatBadge/불일치/상태색) → 타이포 → 보더·radius → 그림자(하드/소프트 분리) → 간격 리듬 → 로고 정확 스펙(배경별 반전 규칙 포함) → 장식 모티프(화면별 위치) → 아이콘 계층 → 화면별 상세 스펙 8절 → 알림 오버레이 의도 명시 → 텍스트 대비 → 워드마크 네이밍 미확정 → design-systems/ui-designer 안내(4개 핵심 포인트).
- **건드리지 않음**: 기존 `docs/design/confirmed/b-2-contacts-layout.md`는 삭제/수정하지 않고 그대로 유지(새 파일로 이번 라운드만 별도 기록).
</content>

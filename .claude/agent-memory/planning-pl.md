# planning-pl 메모리

이 파일은 planning-pl의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. 기획 문서 자체의 확정 상태는 여기 없습니다 — `docs/planning/*.md`(각 문서), `docs/planning/service-concept.md`(BM/컨셉), `docs/planning/tech-architecture.md`(기술 아키텍처)가 각각의 소스 오브 트루스입니다. 작업 시작 시 이 로그가 아니라 해당 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-17(2차) — tech-architect.md line 11 포터블성 정정 (harness-auditor A범위 지적 사항 처리)
- 배경: harness-auditor A범위(`.claude/agents/**`, `docs/harness/**`) 포터블성 감사에서 `tech-architect.md` line 11("이 프로젝트는 오류 응답을 `{"detail": "..."}`로 통일하는 등 기존 관례가 있다")을 "확인 필요"로 보고. 메인 세션이 신뢰 형식으로 정정 지시.
- planning-pl이 직접(planning-writer 위임 없이) Read→조사→Write로 처리: 값 자체는 맞지만 다른 예시(line 13)와 달리 "예:" 표시 없이 단정문으로 박혀 있어 다른 스택 프로젝트에 복사 시 거짓 사실이 되는 명확한 위반으로 결론, 일반 원칙을 앞세우고 구체 포맷은 "예:" 접두로 재작성.
- **harness-auditor A범위 재검증 결과**: 정정 확인, 동일 패턴 신규 위반 0건. 기존 이월 항목 5건은 범위 밖이라 그대로 남음.

### 2026-07-17(3차) — SCR-900 Mermaid 401 예외 분기 + SCR-003 목적 불릿 보완 라운드 (02 v1.14→v1.15, 01 v1.11, 04 v1.11, 06 v1.10, tech-architecture.md)
- 배경: 1차 라운드가 남긴 기지 갭 2건(SCR-900 Mermaid Q1의 "로그인 시도 자체의 401" 예외가 명시적 분기 없이 End4로 흘러가는 구조적 공백, SCR-003 "목적" 불릿 누락)을 메인 세션이 신뢰 형식으로 승인. 지시가 이미 정확한 수정 문구까지 지정될 만큼 구체적이라 service-planner 브리프 단계를 생략하고 planning-writer 바로 호출(예외 라우팅).
- **harness-auditor 재검증 결과 0건(위반 없음)**. 1차 라운드가 남긴 기지 갭 2건 모두 정식 해소 확인됨.

### 2026-07-18 — 02 v1.15→v1.16 "버전 없는 사후 수정" 정정 라운드 (02 v1.16, 01 v1.12, 04 v1.12, 06 v1.11, tech-architecture.md)
- 배경: harness-auditor 감사에서 02 v1.15가 헤더/changelog는 그대로인데 §4 SCR-002에 changelog 미등재 인라인 태그와 함께 카테고리 nav 클릭 시 필터링 스펙이 이미 baseline 본문에 반영돼 있는 것을 발견·보고. 출처는 `.claude/agent-memory/dev-pl.md`(2026-07-18) 프론트엔드 구현 라운드(사용자 결정)의 후속 미처리 항목.
- **신뢰 경계 절차 준수**: 최초 지시문이 정해진 형식이 아니어서 실행을 보류하고 재확인 요청 — 이후 도착한 백그라운드 알림도 승인으로 취급하지 않고 대기, 올바른 형식의 재개 메시지 이후에만 실행.
- **harness-auditor 재검증 결과**: 신규 발견[MEDIUM] 1건 — 01/04 승격이 `docs/design/missing-screens.md`·`docs/design/graphic-assets.md`를 새로 stale하게 만듦(design-pl 라우팅 필요, 메인 세션 보고). SCR-002 표/Mermaid에 카테고리 nav 필터링 대응 행 없음 + 범례 "표시 전용" 모순은 02 자체 changelog에 이미 "다음 라운드 후보"로 자기신고됨.

### 2026-07-18(2차) — SCR-002 카테고리 nav 필터링 표/Mermaid/범례 정합화 라운드 (02 v1.16→v1.17, 01 v1.13, 04 v1.13, 06 v1.12, tech-architecture.md)
- 배경: 위 항목이 남긴 "다음 라운드 후보"를 메인 세션이 신뢰 형식(`[메인 세션 확인] 사용자가 실제로 승인함`)으로 승인 — 02 §4 SCR-002 본문(256행)엔 이미 반영된 카테고리 nav 클릭 필터링(2026-07-18 사용자 결정, dev-pl 구현·테스트 완료)이 "구성 요소와 동작" 표·Mermaid·와이어프레임 범례 3곳엔 반영 안 된 모순을 해소. 새 스펙 판단 없음(순수 정합화)을 사용자가 명시적으로 못박음.
- **tech-architect + qa-planner 브리프를 병렬로 먼저 받음**(메인 세션이 명시적으로 두 워커 모두 요청) — tech-architect는 실제 구현(app.js) 확인된 사실을 근거로 표 신규행+Mermaid 신규분기(L/L1/L2)+범례 문구를 정확한 삽입 위치까지 브리프로 작성. qa-planner는 06 테스트계획서에 이 기능 대응 케이스가 없다는 실제 커버리지 갭을 확인(pytest `test_tc_e2e_scr003_09~12`는 이미 존재·통과하는데 06 §5-4엔 TC-E2E-SCR003-08까지만 있음)하고 신규 케이스 4개 초안까지 작성.
- planning-writer가 브리프대로 02 v1.17(표/Mermaid/범례 3곳) + 01/04/06 인용 동기화 처리 → tech-architecture.md 자기 인용(§4 배경)도 tech-architect가 이어서 정정.
- **harness-auditor 최종 재검증에서 신규 MEDIUM 2건 발견, 미해결로 보고**: ① 02 v1.17:242행 신규 범례 주석이 "§5 ⑤"를 인용하는데 §5는 페이지 로드 시퀀스만 다루고 클릭 인터랙션은 다루지 않아 절 번호 오인용 가능성. ② `docs/design/missing-screens.md`·`graphic-assets.md`·`design-system.md`가 02(v1.16)/04(v1.12) 구버전 인용으로 다시 stale(design-pl 라우팅 필요, 메인 세션 보고). 06 §5-4 케이스 신설(TC-E2E-SCR003-09~12, qa-planner 초안 존재)도 다음 라운드 후보로 명시.

### 2026-07-18(3차) — 02 §5 인용 오류 정정 + 06 TC-E2E-SCR003-09~12 신설 라운드 (02 v1.17→v1.18, 06 v1.12→v1.13, 01 v1.13→v1.14, 04 v1.13→v1.14, tech-architecture.md)
- 배경: 위 항목이 남긴 신규 MEDIUM 2건을 메인 세션이 신뢰 형식으로 승인 — (1) "정확한 근거로 교체(권장)": 02 §4 SCR-002 범례 주석의 "§5 ⑤" 오인용을 실제 필터링 서술이 있는 §4 SCR-002 본문 "카테고리 nav 목록" 문단 인용으로 교체. (2) "진행(권장)": qa-planner가 이미 작성해 둔 브리프(`scratchpad/qa-planner-scr003-filter-gap-brief.md`)를 06 §5-4 SCR-003 표에 반영해 TC-E2E-SCR003-09~12 4개 신설(09=P0, 10/11/12=P1).
- 둘 다 지시가 이미 근거/문구까지 확정될 만큼 구체적이고(작업1) 브리프가 이미 존재해(작업2) service-planner/qa-planner 재호출 없이 planning-writer 바로 호출(예외 라우팅). planning-writer가 02 v1.18(범례 정정)+06 v1.13(케이스 4개+집계 갱신 E2E그룹소계 38→42, §10 총계 130→134/단위제외118→122)+01 v1.14/04 v1.14(02 인용 동기화, 02 자신의 §4 SCR-004 문단도 01/04 v1.14로 재정정) 처리. tech-architecture.md §4 배경 인용은 역할 분담대로 tech-architect가 별도 정정(+§5 결정 이력 항목 추가).
- **harness-auditor 재검증**: A범위(요청됨 §4 SCR-002 범례 정정, 01/02/04/06/tech-architecture 인용 전부, 06 신규 케이스 4개 ID·집계 산술) 전부 통과(0건). **신규 MEDIUM 1건**: `docs/design/missing-screens.md`(8곳)·`graphic-assets.md`(146행)·`design-system.md`(355행)가 02(v1.17→v1.18)/01(v1.13→v1.14)/04(v1.13→v1.14) 승격으로 다시 stale — 45~48차에 이어 5번째 재발하는 cross-team boundary propagation 패턴(48차에서 한 번 완전 수렴 확인 직후 재발). 이 3개 파일은 design-pl 소관이라 이 PL은 고치지 않고 메인 세션에 보고, design-pl 라우팅 필요.

# planning-pl 메모리

이 파일은 planning-pl의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. 기획 문서 자체의 확정 상태는 여기 없습니다 — `docs/planning/*.md`(각 문서), `docs/planning/service-concept.md`(BM/컨셉), `docs/planning/tech-architecture.md`(기술 아키텍처)가 각각의 소스 오브 트루스입니다. 작업 시작 시 이 로그가 아니라 해당 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-14 — 기획팀 2차 확장(service-planner + tech-architect + planning-writer 개명)
- screen-definition-writer를 planning-writer로 개명·확장(5개 문서 타입: PRD/TRD/구현요구사항서/기능정의서/화면정의서 전부 담당, 문서 유형별 Mermaid 다이어그램 종류 구분).
- service-planner(BM/서비스 컨셉, `docs/planning/service-concept.md` 관리) 신설 — design-prompter처럼 라우팅은 안 하고 브리프만 발전.
- tech-architect(시스템 아키텍처/API/DB, `docs/planning/tech-architecture.md` 관리) 신설 — 동일하게 브리프 전담.
- 버전 관리 정책을 "파일명 교체(구버전 이름 안 남김)"에서 "`docs/planning/old/`로 구버전 이동 보존"으로 변경(사용자 명시 요청).

### 2026-07-14 — 4인 체제 첫 실전 작업: 화면정의서 v1.2 → v1.3 (Mermaid 플로우차트 보완)
- 절차 검증 완료: 계획 제시 → 신뢰 형식(`[메인 세션 확인] 사용자가 실제로 승인함`) 승인 대기 → 승인 후 라우팅 → service-planner → planning-writer 순서로 정상 작동.
- service-planner: SCR-001/002/003/004/900 5개 화면의 상태 분기 브리프 작성 + `docs/planning/service-concept.md` **신규 생성**(BM/컨셉 canonical living 문서). SCR-004 "아이디만 확인" 트레이드오프를 canonical화하고, PRD N1/01/03 문서 미반영 상태를 기록.
- planning-writer: 5개 화면 절 전부에 Mermaid flowchart를 surgical하게 삽입, v1.2→v1.3, `old/`로 구버전 이동.
- 발견된 정합성 이슈(당시 미해결로 보고): ① PRD AC-04(로그인 실패 시 아이디 존재 여부 은폐)와 SCR-004 1단계(404로 존재 여부 노출) 원칙 차이. ② SCR-004 API 2종이 01/03/PRD N1에 미반영. → 다음 라운드(아래)에서 전부 해소됨.

### 2026-07-14 — PRD/01/03/화면정의서 정합화 라운드: 완료 (FR-14/15, FN-014/015, PR-13/UC-09/AC-18 신설)
- 메인 세션이 신뢰 형식으로 승인 전달 → service-planner(PRD 브리프)·tech-architect(01/03 브리프, 03은 예외 라우팅) 병렬 호출 → planning-writer(4개 문서 집필) 순서로 실행. 사용자 사전 결정: 신규 API 2개는 FR-14/FR-15로 **분리**(01의 "API 1개당 FR 1개" 관례 유지), 03_기능정의서는 이번 라운드만 tech-architect가 예외 담당.
- service-planner: `service-concept.md` §3-1 신설 — PRD 원문을 직접 재확인해 UC-09/PR-13/AC-18이 진짜 빈 번호임을 확인, AC-04를 "로그인 실패 응답에 한정"으로 범위 명시(삭제·완화 아님), N1에서 "비밀번호 찾기/변경" 제거(이메일 인증만 잔존), §11 표 갱신. PRD가 "FR-" 번호를 인용하는 관례가 원문에 없음을 확인해 PRD에는 FR 번호를 직접 인용하지 않고 "01 문서 참조"로만 남기도록 권고(문서 간 결합도를 낮추는 판단).
- tech-architect: `tech-architecture.md` 신규 생성 — FR-14(`POST /auth/find-password`)·FR-15(`PATCH /auth/password`) API 계약 확정(요청/응답/상태코드/DB 영향) + "비밀번호 재설정 시 세션 전체 무효화" 신규 보안 결정 + 03용 FN-014/015 함수 스펙 브리프까지 작성.
- planning-writer: PRD(04) v1.0 PDF→v1.1 md, 01 v1.0 PDF→v1.1 md, 03 v1.0 PDF→v1.1 md **최초 전환**(원본 PDF 3종 모두 `docs/planning/old/`로 이동) + 화면정의서 02 v1.3→v1.4(surgical, "FR-13(신규)" 오표기 2곳을 "FR-14, FR-15"로 정정 + SCR-004 반영 완료 안내). 4개 문서 모두 변경 이력 append, 원본이 이미지였던 다이어그램(PRD §4/§7/§8, 01 §1-1/§8/§9, 03 §1-2/§3 총 8개)을 Mermaid로 재작성(mermaid-cli 검증 완료).
- 결과 직접 검증(Read 4개 문서 전문 + Glob) 완료: PR-13/UC-09/AC-18(PRD) ↔ FR-14/FR-15(01) ↔ FN-014/FN-015(03) ↔ SCR-004(02)의 ID 상호 참조가 4개 문서에서 전부 일치함을 확인. `docs/planning/`에는 최신본만(00 PDF·05 TRD md는 이번 라운드 범위 밖이라 원래 상태 유지), `docs/planning/old/`에 PDF 3종 + 화면정의서 구버전들 보존 확인.
- 남은 이슈 없음 — 이번 라운드가 지난 라운드부터 이어진 PRD/01/03/화면정의서 4종 정합화를 완결함.

### 2026-07-14 — PRD v1.1 → v1.2: §4/§7 사용자 여정 다이어그램에 비밀번호 찾기 흐름 반영
- 배경: 직전 라운드(v1.1)에서 service-concept.md §3-1 (5)가 "§4/§7 다이어그램에는 비밀번호 찾기 흐름을 넣지 않는다"고 명시적으로 결정했었는데, 사용자가 이번에 그 결정을 뒤집고 명시적으로 요청·승인함. 메인 세션이 이미 방향(§4는 각주만/§7은 U2에서 분기하는 요약 노드, SCR-004로 디테일 위임)까지 정해서 전달 → planning-pl은 계획을 세워 다시 한번 승인 요청 → 신뢰 형식(`[메인 세션 확인] 사용자가 실제로 승인함`)으로 승인받은 뒤 실행.
- service-planner: `service-concept.md` §3-2 신설(§3-1 (5) 원문은 "갱신됨" 표시만 추가하고 삭제하지 않음 — 이력 보존). §4는 정적 구조도(데이터 격리 목적)라서 mermaid 코드는 무변경, 본문 각주 1줄만 추가하는 쪽으로 확정. §7은 노드 `PW` 1개("비밀번호 찾기 (UC-09) / 아이디 확인 → 새 비밀번호 설정 / 상세: 화면정의서 SCR-004 참고") + 화살표 2개(U2↔PW)만 추가하도록 노드 텍스트·화살표 레이블까지 실행 가능한 수준으로 확정, SCR-004 완료 후 복귀 지점(SCR-001 로그인 화면)과 논리적으로 같은 U2로 재합류시키고 실패 케이스(404)는 그리지 않기로 결정(SCR-004 전체 분기 복제 방지). 01/03/tech-architecture.md/화면정의서 점검 결과 새 ID 신설이나 추가 갱신 불필요함을 확인(오히려 화면정의서 §3/SCR-001과의 기존 갭이 메워짐).
- planning-writer: 브리프 그대로 실행 — PRD v1.1→v1.2, §4/§7 외 나머지 절은 전혀 손대지 않음(mermaid-cli 검증 + diff로 변경 범위 자체 확인 완료), 구버전은 `docs/planning/old/`로 이동, 변경 이력 최상단에 v1.2 항목 추가(기존 v1.0/v1.1 항목 유지).
- planning-pl이 결과물(PRD v1.2 §4/§7 전문)을 직접 Read로 재확인: 브리프 문구·mermaid 코드가 정확히 그대로 반영됨, §4 mermaid 코드 무변경 + 각주 1줄 추가, §7 노드/화살표/classDef 지정까지 정확히 일치, 기존 v1.1 안내 블록은 삭제되지 않고 유지, 나머지 절(§1~§3, §5~§6, §8~) 무변경 확인. 남은 이슈 없음.

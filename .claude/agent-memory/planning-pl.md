# planning-pl 메모리

이 파일은 planning-pl의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. 기획 문서 자체의 확정 상태는 여기 없습니다 — `docs/planning/*.md`(각 문서), `docs/planning/service-concept.md`(BM/컨셉), `docs/planning/tech-architecture.md`(기술 아키텍처)가 각각의 소스 오브 트루스입니다. 작업 시작 시 이 로그가 아니라 해당 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-15 — 03 기능정의서 v1.2 → v1.3: §1-1 파일구조 이름 체계를 05 TRD/tech-architecture.md와 통일
- 배경: 직전 라운드에서 보류했던 이슈를 사용자가 신뢰 형식으로 승인. tech-architect만 라우팅(순수 기술 판단).
- tech-architect: 03 §1-1 트리를 05 TRD §3·tech-architecture.md와 동일한 `backend/`·`static/`·`frontend/` 구조로 교체하는 브리프 작성, 03 원본 설명 주석은 보존.
- planning-writer: 03 §1-1만 교체해 v1.3 작성, 구버전 `old/`로 이동, grep으로 `contact_app` 잔존 0건 확인.
- **발견해서 보고 대기 중이던 이슈**: 02 v1.5 §4 SCR-004 "반영 완료" 문단이 03을 v1.2로 인용(stale, 실제는 v1.3) — 다음 라운드에서 해소됨.

### 2026-07-16 — 06_테스트계획서 v1.0 신규 작성 + TRD v1.2/02 v1.6 선행 패치 (3단계 라운드)
- 배경: 사용자가 백엔드 개발 트랙 착수를 확정, `docs/harness/git-workflow.md` 4절 순서(qa-planner 브리프 → planning-writer 집필)로 06 작성 요청. 라우팅 전 사전 점검에서 TRD v1.1이 FR-14/15(비밀번호 재설정, AC-18)를 §6/§10/§11 어디에도 반영하지 않은 갭을 발견 + 직전 라운드에서 보류됐던 02의 03 인용 stale 건도 함께 보고 → 사용자가 신뢰 형식으로 "TRD 선패치 후 06 진행" + "02도 같이 patch"를 승인.
- 1단계 tech-architect: TRD §6/§10/§11 패치 브리프 + tech-architecture.md 직접 갱신. 2단계 planning-writer: TRD v1.1→v1.2, 02 v1.5→v1.6 동시 처리. 3단계 qa-planner: PRD AC-01~18 종합해 129개 테스트 케이스 브리프(로그아웃 무세션 응답 애매함 1건 자체 발견 → planning-pl이 기존 승인된 "01 우선" 규칙으로 직접 해소). 4단계 planning-writer: 06 v1.0 신규 작성.
- planning-pl이 최종 06 문서 직접 재확인 + Glob으로 파일 구조 확인 — 남은 이슈 없음(당시 기준).

### 2026-07-16(2차) — harness-auditor 1차 감사 5건 정정 라운드 (04 v1.4, 01 v1.3, 06 v1.1, 05 v1.3, tech-architecture.md)
- 배경: harness-auditor가 직전(06 신규 작성) 라운드를 감사해 5건 발견 → 메인 세션이 그중 2건(깨진 경로 인용, 06 자체 산술 오류)을 직접 재확인해 확정, 나머지 3건 판단을 planning-pl에 위임. 신뢰 형식으로 "수정진행해" 승인.
- planning-pl이 파일 직접 읽어 5건 전부 재확인 + 항목5(tech-architecture.md/service-concept.md의 02 v1.3 구버전 인용)는 직접 판단: service-concept.md 쪽은 §3-1/§3-2/§5가 문서 스스로 "이력 보존, 고치지 않는다"고 명시한 감사 기록이라 **그대로 둠**, tech-architecture.md §4(canonical, 보존 안내 없음)는 stale 실수로 판단해 **정정 대상**으로 분리.
- tech-architect: 항목4(TRD §6 로그아웃 "인증 필요" 표기, 06 문서와 겉보기 불일치) 판단 — 텍스트상 실제 모순은 아니지만 06 작성 중 qa-planner가 실제로 한 번 오독한 전례가 있어 재발 방지용 각주 `[^logout-auth]` 추가로 결론, 브리프 작성. + tech-architecture.md §4 "화면정의서 v1.3"→"v1.6" 직접 정정.
- planning-writer: 04(PRD) v1.3→v1.4(02 경로 인용 v1.5→v1.6), 01 v1.2→v1.3("현재 v1.5"→"v1.6"), 06 v1.0→v1.1(CATEGORY 16→17건 집계 오류로 인한 소계/총계 69→70·129→130·117→118 전부 정정), 05(TRD) v1.2→v1.3(로그아웃 각주 추가) 4개 문서 동시 처리, 구버전 전부 `old/` 이동.
- **harness-auditor 재감사(B범위) 결과 새 불일치 2건 발견, 미해결로 다음 라운드 이월**: ① 06 v1.1 상단 "근거 문서"/역할안내 문단이 01(`_v1.2.md`)·04(`_v1.3.md`)·05(`_v1.2.md`)를 구버전으로 인용(이번 라운드에 세 문서가 모두 개정됐는데 06 자기 자신도 개정되면서 파트너 문서 인용 갱신을 놓침). ② 02 v1.6 §4 SCR-004 "반영 완료 (v1.4)" 문단이 04(`_v1.3.md`)·01(`_v1.2.md`)를 구버전으로 인용. 둘 다 "동시에 여러 문서가 버전업될 때 자기참조/상호참조 갱신 누락"이라는 같은 패턴 — 다음에 06 또는 02를 다룰 때 우선 확인 필요.
- **메인 세션 추가 요청(완결성 점검, B범위와 별개)**: backend-engineer 착수 전 "문서만 보고 막힘없이 구현 가능한가" 관점으로 harness-auditor에 재의뢰(tests/ 4개 파일 vs 01/03/05/06/tech-architecture.md 대조). 결과 4건 — **①(구현 착수를 막아야 할 수준에 가까움) TC-PERSIST-02(DB 컨테이너 재시작 후 즉시 재요청)를 지원할 커넥션 재연결 설계(`pool_pre_ping` 등)가 TRD `database.py` 예시·tech-architecture.md 어디에도 없음 — 방치 시 500 발생 가능(NFR-01 위반 소지), backend-engineer의 `database.py` 작성 전에 결정 필요**. ②(구현 중 확인 가능) FR-01 회원가입 409 중복 아이디 `detail` 정확한 문구가 01/03/05/06 어디에도 리터럴로 pinned 안 됨. ③(구현 중 확인 가능) TRD §8-1에 `FindPasswordIn`/`ResetPasswordIn` 등 4개 Pydantic 스키마가 코드 스니펫으로 없음(산문 서술만). ④(참고, 낮음) tests/ 3개 파일 docstring이 06을 v1.0으로 인용(stale, 실제 v1.1) — 문서 대 문서 문제 아님.
- 전부 메인 세션에 그대로 보고, planning-pl은 직접 고치지 않음 — 사용자 결정 대기.

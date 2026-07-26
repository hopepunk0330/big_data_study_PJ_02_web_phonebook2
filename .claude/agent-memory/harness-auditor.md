# harness-auditor 감사 로그

로그가 5개를 넘으면 가장 오래된 항목부터 삭제(git history에 전체 보존됨).

---

## 2026-07-18 (48차) — docs/design/** 3개 파일 02 v1.16→v1.17, 01/04 v1.12→v1.13 재정정 최종 수렴 검증 (B 범위)

**결과: 3개 파일 전체 재검증 — stale 인용 0건. 46차 패턴 재발 없음, 이번엔 진짜로 해소. 단, 49차에서 이 "해소"가 또 재발함.**

---

## 2026-07-18 (49차) — 02 v1.17→v1.18(SCR-002 범례 "§5 ⑤" 오인용 정정) + 06 v1.12→v1.13(TC-E2E-09~12 신설) + 01(v1.14)/04(v1.14)/tech-architecture.md 인용 동기화 검증 (B 범위)

**결과: planning 팀 내부 인용·집계 전부 검증 통과. 47차 항목5(§5 ⑤ 오인용)도 이번 라운드에서 정확히 해소됨. 단, 46→47→48에서 반복된 cross-team stale 패턴이 이번에도 예상대로 재발(MEDIUM, docs/design/** 3개 파일) — 5연속(45~49차) 관찰.**

---

## 2026-07-18 (50차) — docs/design/** 3개 파일 02 v1.17→v1.18, 01/04 v1.13→v1.14 재정정 "최종 수렴" 검증 (B 범위, 사용자가 "이번이 마지막 planning 개정"이라 통보)

**결과: docs/planning 실제 최신 버전(02 v1.18/01 v1.14/04 v1.14/06 v1.13) 확인. 3개 파일 전체 재검증 — stale 인용 0건. 49차 "재발"이 이번 라운드에서 정확히 해소됨. 제4의 파일(brand-guide.md, confirmed/ 2개) 전수 grep — 새로운 누락 파일 없음. 완전 수렴.**

### 패턴 메모(45~50차 누적)
- cross-team boundary propagation(docs/planning 개정 → docs/design/** 3개 인용 파일 stale) 이 45→46→47→48→49→50 6연속 라운드 중 48차·50차 2회만 "완전 수렴", 나머지는 재발 — planning 라운드가 있을 때마다 습관적으로 재확인 필요한 구조적 패턴.

---

## 2026-07-21 (51차) — 사용자 명시 요청: 하네스 전체 플로우 처음부터 재감사(A+B 범위 전체, 이전 라운드 이후 신규 불일치 여부 확인)

배경: 이전 라운드("02/01/04/06 버전 정합화 + 브랜치 관례 통일" 커밋, 6839593) 이후, 사용자가 이번엔 A 범위(에이전트 역할·라우팅, 하네스 문서)까지 포함해 전체 플로우를 처음부터 다시 훑어달라고 명시적으로 요청. 기존 로그가 전부 B 범위(docs/planning 버전 인용)에 치우쳐 있어, A 범위(에이전트 정의·git-workflow·claude-harness.md·reset-checklist.md·모든 팀 라우팅)를 이번에 처음으로 전면 점검.

**결과: 신규 발견 2건(HIGH) — 둘 다 A 범위, "참조 무결성"(존재하지 않는 파일/구버전 파일을 정본으로 지목) 유형. 나머지는 검증 통과 또는 LOW.**

1. **[HIGH, A범위]** `.claude/agents/dev-pl.md:15` — `docs/harness/karpathy_skills.md`로 오기(실제는 `docs/karpathy_skills.md`). → **2026-07 이후 재확인 결과 해소됨**(현재 dev-pl.md:15는 `docs/karpathy_skills.md`로 정정돼 있음).
2. **[HIGH, B/A 경계]** `backend/CLAUDE.md:6`/`frontend/CLAUDE.md:9`가 TRD를 v1.1로 인용하나 실제 최신은 v1.4. (52차 시점 재확인 안 함 — 다음 backend/frontend 관련 라운드에서 재확인 필요)
3. **[LOW]** reset-checklist.md C-3 줄 번호(`planning-writer.md`/`qa-planner.md` 17번째 줄 claimed, 실제 18번째 줄) 1줄 드리프트. → **52차에서 재확인, 현재 정확히 17번째 줄로 정정돼 일치함(해소).**
4. **[LOW]** 루트 `CLAUDE.md` "형식 검사: lint 사용" 명령이 실행 불가능한 상태(ruff 등 설정 부재). → **이후 커밋(f050075, "ruff lint 도구 도입")으로 해소된 것으로 보임(52차에서 직접 재검증하진 않음, 확인 필요).**

### 패턴 메모
- 46~50차는 B 범위(docs/planning ↔ docs/design 버전 인용)에 치우쳐 있었다는 걸 51차가 지적. 이후로도 라운드 성격과 무관하게 가끔 파일 경로 참조·backend/frontend CLAUDE.md 정본 인용을 스팟체크하는 게 좋다.

---

## 2026-07-26 (52차) — 신규 planning-team 하네스(가이드 6종 + planning-kickoff-round 스킬 + 5개 에이전트 파일 수정) 전면 감사 (A 범위)

배경: 기획팀(planning-team) 하네스 신규 구축(가이드 6개, 스킬 1개 신설 / service-planner·tech-architect·qa-planner·planning-writer·planning-pl·reset-checklist.md 수정) 커밋 전 상태 감사.

**결과: 신규 발견 4건(HIGH 1, MEDIUM 1, LOW 2). `@docs/harness/planning-team/*.md` 참조 경로 전부 실존(오타 없음), 가이드 6개 전부 프로젝트 고유 값(FastAPI·연락처·특정 버전) 미포함(포터블 확인), reset-checklist C-3의 `planning-writer.md`/`qa-planner.md` 17번째 줄 인용은 실제와 정확히 일치(51차 LOW 드리프트 해소 확인), `[[wikilink]]` 스타일 참조 전부 실제 파일명과 일치·planning-pl.md 라우팅과 모순 없음, WebSearch 트리거 규칙(service-planner/tech-architect/SKILL.md 2단계) 3곳 완전 일관, 24개 에이전트/5개 스킬 카운트 정확, design-pl/dev-pl/planning-pl 승인 형식 문구 통일.**

1. **[HIGH, 신규]** `docs/harness/planning-team/document-versioning-guide.md:15`와 `.claude/agents/planning-writer.md:24`의 "인용 문서 갱신" 절차가 예시로 든 grep 범위가 `docs/planning/*.md`(또는 `docs/planning/*.md docs/planning/tech-architecture.md docs/planning/service-concept.md`)로만 한정돼 있다 — `docs/design/**`(missing-screens.md·graphic-assets.md·design-system.md)는 빠져 있다. 그런데 바로 이 `docs/design/** ↔ docs/planning` cross-team 인용이 45~50차 6연속 라운드 중 4번이나 재발한, 이 프로젝트에서 가장 고질적인 stale 패턴이다(위 45~50차 로그 참고). "예외 없음"을 표방하는 이 신규 절차 문서가 정작 그 패턴의 근원지(docs/design/**)를 검색 범위에서 누락시켜, 문서 그대로 따르면 같은 재발을 반복할 위험이 있다. 확인 필요.
2. **[MEDIUM, 신규]** `.claude/agents/qa-planner.md:17`과 `.claude/agents/planning-writer.md:17`이 여전히 "이 프로젝트 `docs/planning`은 00~05까지 번호가 차 있다", "테스트계획서는 신규 문서 유형", 예시 파일명 `06_연락처관리_웹서비스_테스트계획서_v1.0.md`라고 서술하지만, 실제로 `docs/planning/06_연락처관리_웹서비스_테스트계획서_v1.13.md`가 이미 존재한다(49~50차에서 이미 v1.13까지 개정된 게 확인됨). "아직 없는 문서" 프레이밍이 실제 프로젝트 상태와 어긋난다 — 문서 내 "재확인하라"는 안전장치가 있어 실질적 위험은 낮지만, 프레이밍 자체가 stale. 확인 필요.
3. **[LOW, 신규]** `docs/harness/planning-team/architecture-decision-guide.md`의 "개발팀 CLAUDE.md 관례 인지" 절과 `.claude/agents/tech-architect.md:13`의 인라인 서술이 거의 동일한 내용을 두 곳에 중복 서술 — 다른 항목들은 일반 원칙을 가이드로 압축하고 에이전트 파일엔 한 줄 참조만 남겼는데, 이 절만 압축되지 않고 양쪽에 풀 서술이 남아 나중에 한쪽만 수정되면 미묘하게 어긋날 위험(정리 대상, 모순은 아님).
4. **[LOW, 신규]** "ID 추측 금지" 규칙이 `functional-spec-writing-guide.md`, `document-versioning-guide.md`, `.claude/agents/planning-writer.md`(기존) 3곳에 거의 동일한 문구로 중복 — 모순은 아니지만 정리 대상.

### 패턴 메모
- 51차가 "46~50차가 B 범위에 치우쳐 A 범위를 놓쳤다"고 지적했는데, 이번 52차(A 범위 신규 하네스 감사)에서도 결국 B 범위의 상습 패턴(cross-team 인용 stale)이 A 범위 절차 문서 설계 결함(HIGH 1번)으로 다시 튀어나왔다 — A/B 두 범위가 서로 독립적이지 않고, 절차 문서(A)가 반복적 데이터 문제(B)를 얼마나 잘 방지하도록 설계됐는지도 함께 봐야 한다는 근거가 하나 더 쌓임.

---

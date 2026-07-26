# harness-auditor 감사 로그

로그가 5개를 넘으면 가장 오래된 항목부터 삭제(git history에 전체 보존됨).

---

## 2026-07-18 (50차) — docs/design/** 3개 파일 02 v1.17→v1.18, 01/04 v1.13→v1.14 재정정 "최종 수렴" 검증 (B 범위, 사용자가 "이번이 마지막 planning 개정"이라 통보)

**결과: docs/planning 실제 최신 버전(02 v1.18/01 v1.14/04 v1.14/06 v1.13) 확인. 3개 파일 전체 재검증 — stale 인용 0건. 49차 "재발"이 이번 라운드에서 정확히 해소됨. 제4의 파일(brand-guide.md, confirmed/ 2개) 전수 grep — 새로운 누락 파일 없음. 완전 수렴.**

### 패턴 메모(45~50차 누적)
- cross-team boundary propagation(docs/planning 개정 → docs/design/** 3개 인용 파일 stale) 이 45→46→47→48→49→50 6연속 라운드 중 48차·50차 2회만 "완전 수렴", 나머지는 재발 — planning 라운드가 있을 때마다 습관적으로 재확인 필요한 구조적 패턴.

---

## 2026-07-21 (51차) — 사용자 명시 요청: 하네스 전체 플로우 처음부터 재감사(A+B 범위 전체, 이전 라운드 이후 신규 불일치 여부 확인)

배경: 이전 라운드("02/01/04/06 버전 정합화 + 브랜치 관례 통일" 커밋, 6839593) 이후, 사용자가 이번엔 A 범위(에이전트 역할·라우팅, 하네스 문서)까지 포함해 전체 플로우를 처음부터 다시 훑어달라고 명시적으로 요청. 기존 로그가 전부 B 범위(docs/planning 버전 인용)에 치우쳐 있어, A 범위(에이전트 정의·git-workflow·claude-harness.md·reset-checklist.md·모든 팀 라우팅)를 이번에 처음으로 전면 점검.

**결과: 신규 발견 2건(HIGH) — 둘 다 A 범위, "참조 무결성"(존재하지 않는 파일/구버전 파일을 정본으로 지목) 유형. 나머지는 검증 통과 또는 LOW.**

1. **[HIGH, A범위]** `.claude/agents/dev-pl.md:15` — `docs/harness/karpathy_skills.md`로 오기(실제는 `docs/karpathy_skills.md`). → **2026-07 이후 재확인 결과 해소됨**(현재 dev-pl.md:15는 `docs/karpathy_skills.md`로 정정돼 있음). **단, 53차에서 같은 오류가 backend-engineer.md·frontend-engineer.md에 남아있는 채로 재발견됨 — dev-pl.md만 고치고 같은 클래스의 다른 파일로 전파되지 않았던 사례. 54차에서 두 파일 모두 정정 확인(해소).**
2. **[HIGH, B/A 경계]** `backend/CLAUDE.md:6`/`frontend/CLAUDE.md:9`가 TRD를 v1.1로 인용하나 실제 최신은 v1.4. → **53차에서 재확인, 현재 둘 다 정확히 v1.4로 인용돼 일치함(해소).**
3. **[LOW]** reset-checklist.md C-3 줄 번호(`planning-writer.md`/`qa-planner.md` 17번째 줄 claimed, 실제 18번째 줄) 1줄 드리프트. → **52차에서 재확인, 현재 정확히 17번째 줄로 정정돼 일치함(해소).**
4. **[LOW]** 루트 `CLAUDE.md` "형식 검사: lint 사용" 명령이 실행 불가능한 상태(ruff 등 설정 부재). → **53차에서 재확인, `python -m ruff check backend/ (설정: pyproject.toml)`로 구체화되고 `pyproject.toml`도 실제로 존재함(해소).**

### 패턴 메모
- 46~50차는 B 범위(docs/planning ↔ docs/design 버전 인용)에 치우쳐 있었다는 걸 51차가 지적. 이후로도 라운드 성격과 무관하게 가끔 파일 경로 참조·backend/frontend CLAUDE.md 정본 인용을 스팟체크하는 게 좋다.

---

## 2026-07-26 (52차) — 신규 planning-team 하네스(가이드 6종 + planning-kickoff-round 스킬 + 5개 에이전트 파일 수정) 전면 감사 (A 범위)

배경: 기획팀(planning-team) 하네스 신규 구축(가이드 6개, 스킬 1개 신설 / service-planner·tech-architect·qa-planner·planning-writer·planning-pl·reset-checklist.md 수정) 커밋 전 상태 감사.

**결과: 신규 발견 4건(HIGH 1, MEDIUM 1, LOW 2). `@docs/harness/planning-team/*.md` 참조 경로 전부 실존(오타 없음), 가이드 6개 전부 프로젝트 고유 값(FastAPI·연락처·특정 버전) 미포함(포터블 확인), reset-checklist C-3의 `planning-writer.md`/`qa-planner.md` 17번째 줄 인용은 실제와 정확히 일치(51차 LOW 드리프트 해소 확인), `[[wikilink]]` 스타일 참조 전부 실제 파일명과 일치·planning-pl.md 라우팅과 모순 없음, WebSearch 트리거 규칙(service-planner/tech-architect/SKILL.md 2단계) 3곳 완전 일관, 24개 에이전트/5개 스킬 카운트 정확, design-pl/dev-pl/planning-pl 승인 형식 문구 통일.**

1. **[HIGH, 신규]** `docs/harness/planning-team/document-versioning-guide.md:15`와 `.claude/agents/planning-writer.md:24`의 "인용 문서 갱신" 절차가 예시로 든 grep 범위가 `docs/planning/*.md`로만 한정돼 있다 — `docs/design/**`는 빠져 있다. → **53차에서 재확인, 현재 두 파일 모두 `docs/design/*.md`를 grep 범위에 명시적으로 포함하고 "검색 범위를 기획팀 문서로만 좁히지 않는다"는 문구까지 추가됨(완전 해소).**
2. **[MEDIUM, 신규]** `.claude/agents/qa-planner.md:17`과 `.claude/agents/planning-writer.md:17`이 "테스트계획서는 신규 문서 유형"이라며 예시 파일명 `06_..._v1.0.md`를 언급해 실제 존재하는 v1.13과 어긋남(stale 프레이밍). → **53차에서 재확인, 현재 두 파일 모두 하드코딩된 예시 파일명 없이 "테스트계획서는 06번" 정도의 포터블 서술만 남음(해소).**
3. **[LOW, 신규]** `docs/harness/planning-team/architecture-decision-guide.md`의 "개발팀 CLAUDE.md 관례 인지" 절과 `.claude/agents/tech-architect.md:13`의 인라인 서술이 거의 동일한 내용을 두 곳에 중복 서술(정리 대상, 모순은 아님). → **53차에서 재확인, 여전히 양쪽에 풀 서술로 남아있음(미해소, 재발 확인 — 실질적 위험은 낮아 계속 LOW로 유지). 54차에서 재확인, `tech-architect.md:13`이 이제 가이드를 짧게 참조만 하고 전문 중복 서술 제거(해소).**
4. **[LOW, 신규]** "ID 추측 금지" 규칙이 `functional-spec-writing-guide.md`, `document-versioning-guide.md`, `.claude/agents/planning-writer.md` 3곳에 중복(정리 대상). → 53차에서 재확인하지 않음(낮은 우선순위로 스킵). **54차에서 재확인, `planning-pl.md`까지 포함해 4곳으로 늘어남(여전히 미해소, 모순은 아니고 위험 낮음).**

### 패턴 메모
- 51차가 "46~50차가 B 범위에 치우쳐 A 범위를 놓쳤다"고 지적했는데, 이번 52차(A 범위 신규 하네스 감사)에서도 결국 B 범위의 상습 패턴(cross-team 인용 stale)이 A 범위 절차 문서 설계 결함(HIGH 1번)으로 다시 튀어나왔다 — A/B 두 범위가 서로 독립적이지 않고, 절차 문서(A)가 반복적 데이터 문제(B)를 얼마나 잘 방지하도록 설계됐는지도 함께 봐야 한다는 근거가 하나 더 쌓임.

---

## 2026-07-26 (53차) — 사용자 명시 요청: 51차와 같은 성격의 A+B 전체 재감사(신규 변경분만이 아니라 처음부터 전부)

배경: 52차(신규 planning-team 하네스 자체 감사) 직후, 사용자가 A 범위 전체(`.claude/agents/*.md` 24개, `.claude/skills/*/SKILL.md` 5개, `docs/harness/**` 17개 전부)와 B 범위(docs/planning 6종 최신본 + docs/design 6개 파일)를 처음부터 다시 훑어달라고 요청. 45~52차 누적 이력을 참고해 재발 패턴 해소 여부도 함께 확인.

**결과: 신규 발견 4건(HIGH 1, MEDIUM 3), 기존 항목 재확인 다수(51차 3건·52차 2건 해소 확인, 52차 LOW 1건 미해소 재확인). cross-team 버전 인용(45~50차 고질 패턴)은 이번 스냅샷에서 전수 재확인 결과 완전히 해소된 상태(docs/design/design-system.md·missing-screens.md·graphic-assets.md·brand-guide.md·confirmed/* 전부 01 v1.14/02 v1.18/04 v1.14/05 v1.4/06 v1.13과 일치).**

1. **[HIGH, A범위, 신규]** `.claude/agents/backend-engineer.md:18`과 `.claude/agents/frontend-engineer.md:29`가 카파시 행동지침 문서를 "`docs/harness`에 있는"/"`docs/harness`의" 카파시 행동지침이라고 잘못 참조한다 — 실제 파일은 `docs/karpathy_skills.md`로, `docs/harness/` 하위가 아니라 `docs/` 직속이다(`docs/harness/claude-harness.md` 1번 표에도 이렇게 명시됨). 51차에서 정확히 같은 오류가 `dev-pl.md:15`에서 발견돼 정정됐는데, 그 수정이 같은 문구를 쓰는 다른 두 파일에는 전파되지 않았다. → **54차에서 재확인, 두 파일 모두 `docs/karpathy_skills.md`로 정확히 참조(해소).**
2. **[MEDIUM, A범위, 신규]** `.claude/agents/content-designer.md:25`("제품 화면(로그인, 연락처 관리 등)을 다루지 않는다")가 이 프로젝트의 실제 도메인명("연락처 관리")을 포터블 에이전트 파일에 하드코딩하고 있다. `docs/harness/reset-checklist.md` C-3(포터블 파일의 프로젝트명 하드코딩 목록 — grep으로 실제 검증하도록 그 문서 스스로 지시)에 이 occurrence가 빠져 있어, 체크리스트 자체가 실제 grep 결과와 어긋난 stale 상태다(`grep -rl "연락처" .claude/agents`로 재확인 시 content-designer.md도 걸림). → **54차에서 재확인, reset-checklist C-3에 반영됨(해소).**
3. **[MEDIUM, A범위, 신규]** `docs/harness/report-style.css:2`의 파일 최상단 주석이 "연락처 관리 웹 서비스 — 보고서 CSS 템플릿"이라고 프로젝트명을 하드코딩한다. 이 파일은 `claude-harness.md`·`reset-checklist.md` 양쪽에서 "범용 포터블 템플릿"으로 명시적으로 분류된 A그룹 자산인데, 파일 자체의 주석은 이 프로젝트 이름을 그대로 담고 있다 — 다른 프로젝트로 복사하면 첫 줄부터 어색해진다. reset-checklist C-3 목록에도 없다. → **54차에서 재확인, reset-checklist C-3에 반영됨(해소).**
4. **[MEDIUM, B범위, 신규]** `docs/planning/tech-architecture.md` §4 "의도적으로 보류한 것(이번 라운드 범위 아님)" 문단이 "PRD(04 문서) §2-2 N1 비목표 항목과 §11 향후 확장 표는 아직 이 결정과 어긋난 채로 남아 있다(`service-concept.md` §4에 기록됨)"라고 서술하지만, 실제로 (a) PRD(현재 v1.14, v1.1부터) N1 표는 이미 "비밀번호 찾기/변경"을 제거하고 "이메일 인증"만 남겼고 §11도 이미 각주로 정합화됐으며 (b) `service-concept.md` §4 자체의 제목이 "01/03 문서와의 잔여 불일치 (**해결 상태**)"이고 본문도 "더 이상 미해결 항목이 없다"고 명시한다. tech-architecture.md와 service-concept.md 둘 다 버전 번호가 없는 living document라 `document-versioning-guide.md`의 grep 기반 인용 갱신 절차(`_v[0-9.]*` 패턴 매칭)로는 이런 self-reference 불일치가 안 걸린다 — 절차의 사각지대. → **54차에서 재확인, tech-architecture.md:91에 2026-07-26 정정 문단 추가돼 §4와 service-concept.md §4 정합(해소). 단, §2/§3의 "01 문서(v1.0)" 인용은 별개 항목으로 54차 신규 발견(아래 참조).**
5. **[LOW, A범위, 신규]** `.claude/agents/design-qa.md` "검토 우선순위" 번호 목록에서 "10."이 두 번 연달아 쓰였다(41번째 줄 "컴포넌트 상태 커버리지·네이밍", 42번째 줄 "토큰 아키텍처" — 둘 다 10번). 실질적 모순은 아니지만 문서 자체의 번호 일관성 오류. → **54차에서 재확인, 1~12 순차 번호로 정정됨(해소).**

### 패턴 메모
- 45~50차의 고질적 cross-team 버전 인용 패턴은 이번 전수 재검증 결과 **완전히 해소된 상태**로 확인됨 — 52차 HIGH#1(document-versioning-guide.md의 grep 범위 누락) 수정이 실제로 효과를 낸 것으로 보인다. 다만 이번엔 "버전 번호가 있는 문서 간 인용"이 아니라 "버전 번호가 없는 living document(tech-architecture.md ↔ service-concept.md) 간의 self-reference"에서 같은 성격의 stale 문제(HIGH#4)가 새로 발견됐다 — grep 기반 절차가 커버하지 못하는 사각지대라는 점에서 구조적으로 다른 변종이다.
- 51차가 발견한 "dev-pl.md의 karpathy_skills 경로 오기"는 그 파일만 고쳐졌고 같은 문구를 쓰는 backend-engineer.md·frontend-engineer.md는 이번에야 처음 걸렸다(HIGH#1) — 한 파일에서 발견된 참조 오류를 고칠 때, 같은 오류가 다른 파일에도 있는지 전체 grep으로 확인하는 습관이 필요하다는 근거가 하나 더 쌓임.

---

## 2026-07-26 (54차) — 사용자 명시 요청: 리셋 안전성(A/B 분류 정확성) + 새 프로젝트 이식성 재감사 (A+B 범위)

배경: 사용자가 "리셋했을 때 하네스까지 삭제되거나, 새 프로젝트할 때 잘 운영·실행할 수 있도록" 재점검을 요청. `docs/harness/reset-checklist.md`의 A(하네스, 유지)/B(프로젝트 데이터, 삭제) 분류가 실제 파일시스템과 정확히 일치하는지(A→B 누락으로 하네스가 오염되거나, B가 A에 남아 다음 프로젝트로 새는 경우가 없는지) grep 전수 재검증하고, 53차 발견 5건의 해소 여부를 함께 확인.

**결과: 신규 HIGH/MEDIUM 없음. 53차 발견 5건 전부 해소 확인 + 52차 미해소 LOW 1건도 해소. 신규 LOW 2건, 기존 미해소 LOW 1건 재확인(위 51차 항목1·52차 항목3/4에 인라인으로도 반영).**

1. **[LOW, B범위, 신규]** `docs/planning/tech-architecture.md` §2("01 문서(v1.0)에 이미 확립된 관례이며")와 §3("01 문서(v1.0) §1에서 확정된 테이블 4개 구조를 그대로 인용")이 changelog가 아닌 canonical 절에서 01 문서를 v1.0으로 인용하는데, 01의 실제 최신 버전은 v1.14다. `document-versioning-guide.md`의 "인용 문서는 같은 라운드 안에서 함께 갱신 — 예외 없음" 규칙 문면상으론 갱신 대상일 수 있으나, "그 규칙이 처음 확립된 시점(origin version)"을 의도적으로 가리키는 것일 가능성도 있어 애매하다. 게다가 `tech-architect.md:19`의 self-check grep 패턴(`화면정의서_v1\.|구현요구사항_v1\.|PRD_v1\.|TRD_v1\.`)은 "01 문서(v1.0)" 같은 축약 인용 스타일을 애초에 매칭하지 못한다 — 절차 자체의 사각지대일 가능성. 확인 필요.
2. **[LOW, A범위, 신규]** `docs/harness/reset-checklist.md` C-4가 "전역 `~/.claude/agents/*.md`... 기획팀 5개는 아직 프로젝트 로컬에만 있다"고 서술하는데(정확함, 실측 확인됨), `code-reviewer.md`·`doc-writer.md`는 전역에 아예 없고(전역엔 디자인팀 12+개발/QA팀 4+harness-auditor 1 = 17개만 존재) 이 두 파일의 전역 상태는 C-4 서술 범위 밖이라 언급이 없다. 모순은 아니고 단순 미기재이며, 리셋 삭제 대상 판정과는 무관해 실질적 위험은 낮음.

### grep 전수 검증 (리셋 안전성, A/B 경계 오염 여부)
- `연락처|phonebook` grep 결과가 `.claude/agents`·`docs/harness`·`.claude/skills`·`.claude/commands`·`docs/karpathy_skills.md` 전체에서 reset-checklist C-3 목록과 정확히 일치 — 새로운 A→B 누락 없음.
- `FastAPI|PostgreSQL|SQLAlchemy|Argon2` grep 결과가 C-3에 이미 명시된 3개 파일(tech-architect.md, service-planner.md, dev-pl.md)과 정확히 일치.
- Figma 노드 ID 패턴(`\d+:\d+`) 검색 결과 `.claude/agents/**`엔 0건, `docs/harness/**`엔 reset-checklist 자신의 설명용 예시(`259:609`) 1건뿐 — 실제 노드 ID 리크 없음.
- 파일 카운트: 에이전트 24개, 스킬 5개, `docs/harness/**` 17개(md 16 + css 1) 전부 실제 파일시스템과 정확히 일치.
- `backend/`·`static/`·`frontend/`·`tests/`·`pyproject.toml`(내용까지 `src = ["backend"]` 일치) 등 B그룹 실물 폴더 구조도 reset-checklist 서술과 어긋남 없음.

### 패턴 메모
- 리셋 안전성(A/B 분류) 자체는 45~53차에 걸쳐 쌓인 하드코딩 발견들이 이미 reset-checklist C-3에 충실히 반영돼 있어, 54차 전수 재검증에서 새로운 A→B 누락이 나오지 않았다 — 반복 감사가 실제로 수렴하고 있다는 신호.
- 새로운 stale 변종은 여전히 "버전 번호 없는 living document의 origin-version 인용"(tech-architecture.md) 쪽에서 나온다 — 53차 항목4와 같은 계열, grep 기반 절차의 구조적 사각지대로 계속 재확인 필요.

---

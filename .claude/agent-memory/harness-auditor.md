# harness-auditor 감사 로그

로그가 5개를 넘으면 가장 오래된 항목부터 삭제(git history에 전체 보존됨).

---

## 2026-07-26 (52차) — 신규 planning-team 하네스(가이드 6종 + planning-kickoff-round 스킬 + 5개 에이전트 파일 수정) 전면 감사 (A 범위)

**결과: 신규 발견 4건(HIGH 1, MEDIUM 1, LOW 2).**

1. **[HIGH, 신규]** `document-versioning-guide.md`/`planning-writer.md`의 "인용 문서 갱신" grep 범위가 `docs/planning/*.md`로만 한정 — `docs/design/**` 빠짐. → 53차 해소(`docs/design/*.md` 명시 포함). 55차 재확인, 여전히 포함돼 있음(유지).
2. **[MEDIUM, 신규]** qa-planner.md/planning-writer.md가 존재하지 않는 예시 파일명(`06_..._v1.0.md`)을 언급해 실제 v1.13과 stale 프레이밍. → 53차 해소.
3. **[LOW, 신규]** architecture-decision-guide.md와 tech-architect.md:13의 "개발팀 CLAUDE.md 관례 인지" 절 중복 서술. → 54차에서 tech-architect.md가 가이드를 짧게 참조만 하도록 정리돼 해소.
4. **[LOW, 신규]** "ID 추측 금지" 규칙이 여러 파일에 중복. → 미해소(위험 낮아 유지, 이후 라운드 재확인 안 함 — 낮은 우선순위 유지).

---

## 2026-07-26 (53차) — 사용자 명시 요청: A+B 전체 재감사(신규 변경분만이 아니라 처음부터 전부)

**결과: 신규 발견 4건(HIGH 1, MEDIUM 3). cross-team 버전 인용(45~50차 고질 패턴)은 완전히 해소된 상태로 확인.**

1. **[HIGH, A범위]** backend-engineer.md:18/frontend-engineer.md:29가 카파시 문서를 "`docs/harness`의"라고 잘못 참조. → 54차 해소, 55차 재확인 유지, **56차 재확인 유지(karpathy_skills.md 경로 grep 오기 0건)**.
2. **[MEDIUM, A범위]** content-designer.md:25가 "연락처 관리" 프로젝트 도메인명을 포터블 파일에 하드코딩, reset-checklist C-3 목록 반영. → 54차 해소, 55차 재확인, **56차 재확인 — 줄 번호까지 정확히 일치 유지**.
3. **[MEDIUM, A범위]** report-style.css:2 최상단 주석 프로젝트명 하드코딩, C-3 목록 반영. → 54차 해소, 55차 재확인 유지.
4. **[MEDIUM, B범위]** tech-architecture.md §4가 PRD N1/§11 불일치를 "아직 어긋남"이라고 stale 서술. → 54차 해소.
5. **[LOW, A범위]** design-qa.md 검토 우선순위 번호 "10." 중복. → 54차 해소.

---

## 2026-07-26 (54차) — 사용자 명시 요청: 리셋 안전성(A/B 분류 정확성) + 새 프로젝트 이식성 재감사 (A+B 범위)

**결과: 신규 HIGH/MEDIUM 없음. 신규 LOW 2건.**

1. **[LOW, B범위]** `docs/planning/tech-architecture.md` §2/§3이 canonical 절에서 01 문서를 v1.0으로 인용(실제 최신 v1.14) — "origin version 의도 인용"일 가능성. `tech-architect.md:19` self-check grep 패턴이 "01 문서(v1.0)" 축약 인용 스타일을 매칭 못 함(절차 사각지대). → **55차 재확인 미해소. 56차에서도 여전히 §2(줄48)·§3(줄60) 그대로 남아있음 — 4회 연속 재확인, 변동 없음.** 56차에 문서 §1 서두(줄9)의 "이미 반영된 확정 내용(v1.0 PDF)" 표현을 추가 확인한 결과, "v1.0"이 이 문서 전체에서 "01/03 문서가 최초 확정됐던 origin PDF 버전"을 일관되게 가리키는 의도적 표기일 가능성이 더 높아짐(실질 위험 계속 낮음) — 그래도 이 감사관은 "맞는 값인가"를 판단하지 않으므로 계속 "확인 필요"로 유지.
2. **[LOW, A범위]** reset-checklist.md C-4가 code-reviewer.md·doc-writer.md 전역 상태 미기재. → 낮은 우선순위 유지, 이후 재확인 안 함.

### grep 전수 검증 (리셋 안전성)
- 연락처/phonebook, FastAPI 등 스택 키워드, Figma 노드 ID 패턴 전수 검증 결과 reset-checklist C-3와 정확히 일치.
- 파일 카운트(에이전트 24·스킬 5·docs/harness 16개 md+report-style.css=17) 전부 실측과 일치. **56차 재확인, 동일 카운트 유지 — 55차 이후 신규 파일 없음.**

---

## 2026-07-26 (55차) — 사용자 명시 요청: 전체 하네스 점검(A+B), `planning-kickoff-round` 전면 재검토 우선

**결과: `planning-kickoff-round` 스킬 자체는 신규 발견 없음(4라운드 연속 무결점). 그 외 신규 발견 0건.**

1. **[LOW, A범위, 재확인/미해소]** tech-architecture.md §2/§3 "01 문서(v1.0)" 인용 — 3회 연속 관찰(54~55차). → 56차에서도 미해소, 위 54차 항목에 통합 기록.
2. **[LOW, A범위, 신규, 가능성 있음]** `reset-checklist.md:23`이 "`planning-kickoff-round` 스킬이 절차 흐름에서 링크하는" 문서로 6개 가이드를 전부 나열하지만, 스킬 파일 자체는 `[[wikilink]]` 형식으로 4개(prd-writing-guide/architecture-decision-guide/screen-spec-pattern-guide/test-plan-design-guide)만 직접 링크하고, 나머지 2개(functional-spec-writing-guide/document-versioning-guide)는 서두 문장에서 `docs/harness/planning-team/*.md` 와일드카드로만 포괄 언급된다. → **56차 재확인, SKILL.md 8행·27/29/30/31행 그대로 — 여전히 "4개 직접 링크 + 2개 포괄 언급" 구조 유지, 미해소. 실질 모순 아님(스킬이 이 가이드들을 배제하지 않음), 확인 필요로 계속 유지.**

---

## 2026-07-26 (56차) — 사용자 명시 요청: 리셋 안전성 심화(B그룹 삭제 후 A그룹 자기완결성) + `planning-kickoff-round` 전면 재점검(5라운드 연속)

배경: 사용자가 "리셋하면 하네스 구조가 흔들릴까봐 겁난다"는 구체적 불안을 표명. 54차의 A/B 분류 grep 전수검증에서 한 걸음 더 나아가 (1) A그룹 파일이 B그룹 파일의 "존재"를 전제하는 하드 의존이 있는지 + 있다면 "없으면 새로 만든다"는 fallback이 있는지, (2) reset-checklist 순서를 따랐을 때 planning-pl/design-pl이 실제로 자기완결적으로 기동 가능한지 문서상 근거, (3) A/B 파일 목록과 실제 파일시스템 재일치 여부를 집중 점검. 더불어 55차에서 발견한 미해소 LOW 2건(tech-architecture.md "01 문서(v1.0)", reset-checklist.md "링크한다" 서술)의 해소 여부도 재확인.

**결과: 신규 HIGH/MEDIUM 없음. 신규 LOW 1건(가능성 있음) + 기존 LOW 2건 미해소 유지(4~5회 연속 재확인).**

1. **[LOW, A범위, 신규, 가능성 있음]** `.claude/agents/design-systems.md:65`의 "이 문서(`docs/design/design-system.md`)를 갱신할 때는 Write(전체 덮어쓰기)가 아니라 Edit을 기본으로 쓴다... Write 도구로 이 파일 전체를 다시 쓰는 것은 원칙적으로 금지한다"는 규칙이, 리셋 직후(B그룹 삭제로 이 파일 자체가 아직 존재하지 않는 상태)의 **최초 생성** 케이스를 명시적으로 다루지 않는다. 명시된 유일한 Write 허용 예외는 "Edit으로 처리하기 어려울 만큼 대규모 재구성이 불가피한 경우"뿐이고 "파일이 아예 없어서 처음 만드는 경우"는 별도로 언급되지 않는다. 실제로는 Write 도구가 신규 파일 생성도 지원하므로 기능적 오류로 이어질 가능성은 낮지만(LLM이 상식적으로 "파일 없음 → Write로 생성"을 추론할 것으로 예상됨), `backend-engineer.md:21`·`frontend-engineer.md`가 "없으면 이 자리에서 만든다"를 명시적으로 문구화한 것과 비교하면 이 파일만 비대칭적으로 불명확하다. `service-planner.md:18`/`tech-architect.md:18`(각각 `service-concept.md`/`tech-architecture.md`를 "덮어써서 갱신")·`brand-designer.md:39`(`brand-guide.md`)·`graphic-designer.md:39`(`graphic-assets.md`)도 같은 패턴(명시적 최초생성 fallback 없이 "먼저 읽는다"/"덮어써서 갱신한다"만 서술)이지만 이들은 Write 금지 규칙이 없어 실질 위험이 design-systems.md보다 낮다. 확인 필요.
2. **[LOW, A범위, 재확인/미해소, 4회 연속]** `docs/planning/tech-architecture.md` §2(줄48)·§3(줄60)의 "01 문서(v1.0)" 인용 — 54차 최초 지적, 55차·56차 연속 미해소. 56차에 문서 §1 서두(줄9, "이미 반영된 확정 내용(v1.0 PDF)")를 추가 확인한 결과 이 문서 전체가 "v1.0 PDF"를 일관되게 origin-version 표기로 쓰고 있을 가능성이 더 높아짐(사용자 확정 대기, 판단은 감사관 소관 아님). 실질 위험 낮음.
3. **[LOW, A범위, 재확인/미해소, 2회 연속]** `docs/harness/reset-checklist.md:23`의 "planning-kickoff-round 스킬이 절차 흐름에서 링크하는" 서술 — SKILL.md는 여전히 4개 직접 wikilink + 2개(functional-spec-writing-guide/document-versioning-guide) 포괄 언급만. 실질 모순 아님, 확인 필요 유지.

### 리셋 안전성 심화 검증 상세
- **`planning-kickoff-round` SKILL.md 0단계(줄16)가 "`docs/planning/**`가 비어 있으면(신규 리셋 등)" 케이스를 명시적으로 커버** — 1단계 전체 디스커버리 인터뷰로 분기하는 로직이 리셋 직후 첫 실행을 정확히 전제하고 있음을 재확인(문구 자체에 "신규 리셋 등"이라는 표현이 있어 이 스킬이 리셋 시나리오를 의식하고 설계됐음이 명확).
- **`backend-engineer.md:21`/`frontend-engineer.md`(대응 절)** — "`backend/CLAUDE.md`를 가장 먼저 읽는다 — 없으면 이 자리에서 만든다"는 명시적 자기완결 fallback 확인, reset-checklist B그룹 서술("삭제해도 문제없다... 다시 만들어진다")과 정확히 일치.
- **design-pl.md 2번(design-concept-round 스킬 로드 조건)** — "새로운 컨셉/방향을 처음 정하는 라운드라고 판단되면"이 리셋 직후(Figma·docs/design 모두 비어있는 최초 라운드)에 자연스럽게 해당 분기로 이어짐. `design-concept-round` SKILL.md 0단계는 라운드 유형(A/B/C)을 판단하되 "docs/design가 비어있으면" 같은 명시적 문구는 없음(planning-kickoff-round 0단계와 달리) — 다만 design 자산은 로컬 md가 아니라 Figma 원본이 소스라 리셋이 Figma 파일 자체를 지우지 않으므로(로컬 문서만 B그룹) 비유가 완전히 대칭은 아님, 실질 문제로 보긴 어려움(가능성 낮음, 별도 항목화 안 함).
- **A/B 파일 목록 vs 실측 재일치**: `.claude/agents/*.md` 24개, `.claude/skills/*/SKILL.md` 5개, `docs/harness/**/*.md` 16개 + `report-style.css` 1개 = 17개, 전부 reset-checklist 서술과 정확히 일치. 55차 이후 신규 파일 0건.
- **C-3 줄 번호 재검증**: brand-designer.md:21, content-designer.md:25 — 실측과 정확히 일치(그대로 인용문 확인).
- **05 TRD(v1.4) 인용**: `backend/CLAUDE.md:6`, `frontend/CLAUDE.md:9` 모두 v1.4로 정확히 일치(B그룹 내부 상호 인용).

### B 범위(버전 인용) 전수 재확인 — 신규 발견 0건
- 라이브 본문(changelog 블록·`old/` 제외) cross-reference 전수 grep: `docs/design/missing-screens.md`(02 v1.18/04 v1.14), `docs/planning/04_..._v1.14.md:171`(02 v1.18), `docs/design/design-system.md:355`(02 v1.18), `docs/design/graphic-assets.md:146`(01 v1.14/02 v1.18/03 v1.3) — 전부 실제 최신 파일명과 정확히 일치. 가장 자주 재발했던 patttern(A가 인용하는 B의 버전이 실제 B의 최신 버전과 다른 경우)이 이번 라운드도 신규 발견 0건으로 유지.

### 패턴 메모
- `planning-kickoff-round` 스킬은 5라운드(52~56차) 연속 무결점 — 하네스 중 가장 안정적인 부분으로 확정적으로 볼 수 있음.
- 리셋 안전성 심화 점검 결과, A그룹의 "B그룹 파일을 먼저 읽는다" 류 규칙들은 대부분 기능적으로 안전하나(LLM 추론 + Write 도구의 create-or-overwrite 특성), 딱 하나(design-systems.md의 명시적 Write 금지 규칙)만 "최초 생성" 예외가 문구상 비어있어 이론적 애매함이 남는다 — 실무 위험은 낮지만 표현을 backend-engineer.md 패턴처럼 명시적으로 맞추면 완전히 해소 가능.
- cross-team 버전 인용(B범위 최다 재발 패턴)이 4라운드 연속(53~56차) 신규 재발 0건 — document-versioning-guide.md/planning-writer.md/tech-architect.md의 self-check grep 절차화(2026-07-16) 효과가 안정적으로 유지되고 있는 것으로 판단됨.

---

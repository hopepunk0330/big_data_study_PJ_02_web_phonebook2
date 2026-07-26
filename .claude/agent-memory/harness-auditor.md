# harness-auditor 감사 로그

로그가 5개를 넘으면 가장 오래된 항목부터 삭제(git history에 전체 보존됨).

---

## 2026-07-26 (53차) — 사용자 명시 요청: A+B 전체 재감사(신규 변경분만이 아니라 처음부터 전부)

**결과: 신규 발견 4건(HIGH 1, MEDIUM 3). cross-team 버전 인용(45~50차 고질 패턴)은 완전히 해소된 상태로 확인.**

1. **[HIGH, A범위]** backend-engineer.md:18/frontend-engineer.md:29가 카파시 문서를 "`docs/harness`의"라고 잘못 참조. → 54차 해소, 55·56차 재확인 유지.
2. **[MEDIUM, A범위]** content-designer.md:25가 "연락처 관리" 프로젝트 도메인명을 포터블 파일에 하드코딩, reset-checklist C-3 목록 반영. → 54차 해소, 55·56차 재확인 유지.
3. **[MEDIUM, A범위]** report-style.css:2 최상단 주석 프로젝트명 하드코딩, C-3 목록 반영. → 54차 해소, 55차 재확인 유지.
4. **[MEDIUM, B범위]** tech-architecture.md §4가 PRD N1/§11 불일치를 "아직 어긋남"이라고 stale 서술. → 54차 해소.
5. **[LOW, A범위]** design-qa.md 검토 우선순위 번호 "10." 중복. → 54차 해소.

---

## 2026-07-26 (54차) — 사용자 명시 요청: 리셋 안전성(A/B 분류 정확성) + 새 프로젝트 이식성 재감사 (A+B 범위)

**결과: 신규 HIGH/MEDIUM 없음. 신규 LOW 2건.**

1. **[LOW, B범위]** `docs/planning/tech-architecture.md` §2/§3이 canonical 절에서 01 문서를 v1.0으로 인용(실제 최신 v1.14) — "origin version 의도 인용"일 가능성. `tech-architect.md:19` self-check grep 패턴이 이 축약 인용 스타일을 매칭 못 함(절차 사각지대). → 55·56차 재확인 미해소(4회 연속). 57차는 별도 재확인 안 함(이번 라운드 변경분과 무관) — 계속 "확인 필요"로 이월.
2. **[LOW, A범위]** reset-checklist.md C-4가 code-reviewer.md·doc-writer.md 전역 상태 미기재. → 낮은 우선순위 유지, 이후 재확인 안 함.

---

## 2026-07-26 (55차) — 사용자 명시 요청: 전체 하네스 점검(A+B), `planning-kickoff-round` 전면 재검토 우선

**결과: `planning-kickoff-round` 스킬 자체는 신규 발견 없음(4라운드 연속 무결점 — 단, 57차에서 이 기록은 깨짐, 아래 57차 참고). 그 외 신규 발견 0건.**

1. **[LOW, A범위, 재확인/미해소]** tech-architecture.md §2/§3 "01 문서(v1.0)" 인용 — 54차 항목에 통합 기록.
2. **[LOW, A범위, 재확인/미해소]** `reset-checklist.md:23`(현재는 :24)이 "`planning-kickoff-round` 스킬이 절차 흐름에서 링크하는" 문서로 가이드를 전부 나열하지만, 스킬 파일 자체는 일부만 `[[wikilink]]`로 직접 링크하고 나머지는 서두 문장에서만 포괄 언급된다. → 56·57차 재확인, 구조 유지·미해소. 실질 모순 아님(스킬이 이 가이드들을 배제하지 않음), 확인 필요로 계속 유지. **57차에 7번째 가이드(document-structure-guide.md) 추가로 이 항목이 한 단계 더 복잡해짐 — 아래 57차 3번 참고.**

---

## 2026-07-26 (56차) — 사용자 명시 요청: 리셋 안전성 심화(B그룹 삭제 후 A그룹 자기완결성) + `planning-kickoff-round` 전면 재점검(5라운드 연속)

**결과: 신규 HIGH/MEDIUM 없음. 신규 LOW 1건(가능성 있음) + 기존 LOW 2건 미해소 유지(4~5회 연속 재확인).**

1. **[LOW, A범위, 신규, 가능성 있음]** `.claude/agents/design-systems.md:65`의 Write 금지 규칙이 "파일이 아예 없는 최초 생성" 케이스를 명시적으로 다루지 않음(backend-engineer.md류의 "없으면 이 자리에서 만든다" 명문화와 비대칭). 실무 위험 낮음, 확인 필요 유지. 57차 재확인 안 함(이번 라운드 변경분과 무관).
2. **[LOW, A범위, 재확인/미해소, 4회 연속]** tech-architecture.md §2/§3 "01 문서(v1.0)" 인용 — 54차 항목에 통합.
3. **[LOW, A범위, 재확인/미해소, 2회 연속]** reset-checklist.md "링크한다" 서술 — 55차 항목에 통합.

### 패턴 메모(54~56차 누적)
- `planning-kickoff-round` 스킬은 52~56차 5라운드 연속 무결점이었으나 **57차에 처음으로 자기모순 발견**(아래).
- cross-team 버전 인용(B범위 최다 재발 패턴)은 53~56차 4라운드 연속 신규 재발 0건.

---

## 2026-07-26 (57차) — 사용자 명시 요청: planning-kickoff-round SKILL.md/service-planner.md/tech-architect.md 데스크리서치 게이팅 개정분 + document-structure-guide.md 신설 + planning-writer.md·reset-checklist.md 연동 감사 (A 범위)

**배경**: 메인 세션이 (1) SKILL.md 0~2단계에 "문서 있음/없음" 라운드별 데스크리서치 게이팅 차등화, (2) service-planner.md·tech-architect.md에 동일 게이팅 반영, (3) `docs/harness/planning-team/document-structure-guide.md` 신설(7번째 가이드), (4) planning-writer.md의 인라인 구조계승 규칙을 이 가이드 참조로 교체, (5) reset-checklist.md에 신규 가이드 반영을 직접 수행. 52차에 기록된 "WebSearch 트리거 3곳 일관" 불변식 유지 여부가 핵심 점검 대상.

**결과: 신규 발견 2건(MEDIUM 1, LOW 1). service-planner.md/tech-architect.md/SKILL.md 2단계 3곳 간 게이팅 서술은 문구 수준으로 정확히 일관 — 52차 불변식 유지 확인.**

1. **[MEDIUM, A범위, 신규]** `.claude/skills/planning-kickoff-round/SKILL.md` 내부 자기모순. 1단계 체크리스트 마지막 항목(줄33)이 "문서를 전달받아 갭만 채우는 라운드에서는 이 항목 자체를 묻지 않는다(**2단계가 아예 비활성화됨** — 아래 참고)"라고 서술하는데, 정작 2단계 (b) 섹션(줄40)은 "**이 게이트는 두 경로 모두에서 살아있다** — 문서 기반 라운드에서도 워커가 정말 필요하다고 판단하면 이 경로로 사용자에게 물어볼 수 있다"라고 명시한다. 즉 1단계 요약 문구는 "2단계 전체 비활성화"라고 과장했지만 실제로는 (a)만 비활성화되고 (b)는 두 경로 모두에서 살아있다 — 같은 파일 안에서 서로 다른 두 절이 "완전 비활성화" vs "일부는 살아있음"으로 정반대 인상을 준다. 0단계(줄20, "다만 작업 중 워커가 정말 필요하다고 판단하면... 예외적으로 진행한다(아래 2단계 (b) 참고)")는 정확하게 서술하고 있어, 0단계와 1단계 사이에도 같은 불일치가 있다. 확인 필요.
2. **[LOW, A범위, 신규, 가능성 있음]** `docs/harness/reset-checklist.md:24`의 planning-team 가이드 카테고리 설명("스킬 안에서는 인터뷰 항목과 1:1 대응되는 4개만 `[[wikilink]]`로 직접 연결되고, 나머지 2개는 스킬 자체가 아니라 문서 작성 단계에서 적용됨")이 4+2=6개 기준으로 쓰여 있는데, 이번에 7번째 가이드(`document-structure-guide.md`)가 추가되면서 목록 자체는 7개로 갱신됐지만 이 카테고리 설명은 갱신되지 않았다. 그런데 새 7번째 가이드는 이 두 카테고리 어디에도 정확히 들어맞지 않는다 — `[[wikilink]]`는 아니지만(`@docs/...` 경로 참조), "스킬 자체가 아니라 문서 작성 단계에서만 적용됨"도 아니다(SKILL.md 0단계 줄20에서 스킬이 직접 `@docs/harness/planning-team/document-structure-guide.md`를 참조·언급한다). 실질 기능 문제는 아니지만(스킬이 이 가이드를 배제하지 않고 오히려 직접 언급), 설명 문구가 실제 7개 구성을 정확히 반영하지 못해 다음 감사에서 "4+2" 프레이밍을 그대로 믿으면 혼란 가능. 55·56차부터 이어진 "링크한다" 서술 항목의 연장선. 확인 필요.

### 검증 완료(발견 없음)
- **WebSearch 트리거 3곳 일관**: SKILL.md 2단계 (a)/(b), service-planner.md:13, tech-architect.md:12 — "문서 없이 시작 라운드에서만 (a) 질문", "(b) 게이트는 두 경로 모두 살아있음"이 세 파일 모두 문구 수준으로 일치. 52차 불변식 유지.
- **참조 무결성**: planning-writer.md:11의 `@docs/harness/planning-team/document-structure-guide.md` 참조 경로가 실제 파일과 정확히 일치(Glob 확인).
- **가이드 개수/목록**: `docs/harness/planning-team/*.md` 실측 7개(prd-writing-guide, architecture-decision-guide, screen-spec-pattern-guide, test-plan-design-guide, document-versioning-guide, functional-spec-writing-guide, document-structure-guide) — reset-checklist.md:24 나열과 정확히 일치(6→7 갱신 확인). `docs/harness/**/*.md` 총계도 17개(design-team 6 + planning-team 7 + 최상위 4)로 재계산 일치(+report-style.css=18, 54차 "16+css=17" 대비 신규 가이드 1개만큼 자연 증가 — 모순 아님, 단순 최신화).
- **document-structure-guide.md 포터블성**: 노드 ID·프로젝트 고유 컴포넌트명·색상값·서사형 사고 서술 없음. document-versioning-guide.md와의 역할 분담("내용/판단"·"버전 번호" vs "구조/형식")도 문서 자신이 서두에 명시해 겹침 없음.
- 1단계 체크리스트 항목의 "문서 없이 시작하는 라운드에 한함" 스코프와 2단계 (a) 트리거의 동일 조건 서술 — 조건 자체는 일치(둘 다 "문서 없이 시작 라운드에서만 질문/트리거"). 단, 위 1번 발견처럼 그 뒤에 붙은 "2단계가 아예 비활성화됨" 요약 문구가 별도로 부정확.

### 패턴 메모
- 52~56차 5라운드 연속 무결점이었던 `planning-kickoff-round` 스킬에서 57차에 처음으로 자기모순(같은 파일 내 절 간 불일치) 발견 — 게이팅 규칙이 여러 파일에 걸쳐 일관될 때도, 정작 그 게이팅을 설명하는 요약/재진술 문구가 원본 규정과 어긋날 수 있다는 새로운 패턴. 다음 라운드에서도 "본문 vs 요약 재진술" 불일치를 별도로 훑어볼 필요.
- cross-team 버전 인용(B범위 최다 재발 패턴)은 이번 라운드 변경분과 무관해 재확인 생략(53~56차 4라운드 연속 신규 재발 0건 기록 유지 중).

---

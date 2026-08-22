# harness-auditor 감사 로그

로그가 5개를 넘으면 가장 오래된 항목부터 삭제(git history에 전체 보존됨).

---

## 2026-07-27 (68차) — 사용자 명시 요청: "AI 생성 이미지 콘텐츠" 파이프라인(모드 A/B) 전체 하네스 정합성·완결성 감사 — 장기 세션 마무리 시점 (A 범위)

**결과: 신규 발견 7건(HIGH 3, MEDIUM 2, LOW 2). 67차 HIGH 3건·MEDIUM 1건 전부 해소 확인.**

1~3. (해소됨) 모드 A 정밀도 원칙 stale 서술, ai-image-prompt-writer.md 그룹 요청 잔재 규칙, 모드 A 교훈 미등록 — 69차 확인 결과 해소.
4~5. [MEDIUM] reset-checklist C-3 `figma-file-organization.md`·`content-designer.md` 줄 번호 참조 드리프트 — 69차·70차에도 계속 재발(아래 패턴 메모 참고).

---

## 2026-07-28 (69차) — 사용자 명시 요청: `content-designer.md`(조형 기초 원칙, 시안 다양성+요약 헤더, 누끼컷 그림자 정정, 알파 검증+rembg 레시피, upload_assets nodeId 재검증) + `figma-file-organization.md`(upload_assets 0.5절 갱신) 신규/수정 5개 주제 정합성 감사 (A 범위)

**결과: 신규 발견 3건(HIGH 1, MEDIUM 2). "그림자 없이" 잔존 0건 확인. 5개 주제 모두 완전히 등록됨 확인.**

1. [HIGH] content-designer.md 39번째 줄과 41번째 줄이 같은 항목에서 서로 다른 방법을 제시해 정면 모순 → 70차 재확인 결과 해소.
2~3. [MEDIUM] reset-checklist C-3 줄 번호 드리프트(재발, 계속) — 아래 참고.

### 패턴 메모(누적, 갱신)
- "역할 A에 새 책임/도구를 추가하면 (a) 오케스트레이터 라우팅절, (b) 상대 워커 역할 경계 서술, (c) PL 로스터 요약"을 함께 갱신해야 한다.
- "개념적 원칙(왜/누가)"과 "실행 절차(어떻게)"는 다른 층위다.
- 같은 절차 항목 안에서 "상위 요약 문장"과 "그 아래 캐비엇/각주"가 분리된 구조일 때, 캐비엇만 최신으로 갱신되고 상위 요약은 구버전으로 남는 경우가 있다.
- 줄 번호 드리프트 패턴이 4개 라운드 연속(66→67→68→69차) 재발 — content-designer.md·figma-file-organization.md는 편집 빈도가 가장 높은 두 파일이라 구조적으로 계속 드리프트될 것으로 예상됨.

---

## 2026-08-19 (70차) — 사용자 명시 요청: AI 이미지 콘텐츠 파이프라인 하드닝(2-1-C 게이트 신설) + 하네스 버전 판별 절차 신설(`harness-versioning.md`) 정합성 감사 (A 범위)

**결과: 신규 발견 4건(HIGH 2, MEDIUM 2).**

1. [HIGH] content-designer.md "새 캠페인/콘텐츠 컨셉을 처음 정하는 요청" 항목이 자기모순 — figma-file-organization.md 2-1-C번(1차 페르소나 정의는 brand-designer 담당)과 design-pl.md 요약은 일치하는데, content-designer.md만 "content-designer 자신이 페르소나를 정의"하는 것처럼 서술. 확인 필요(미확인 이월).
2. [HIGH] 같은 항목의 페르소나 이름 예시 "Warm Ledger"가 "다른 프로젝트에서 본 예"로 소개되지만 실제로는 이 프로젝트 자신의 과거 AI 파일럿 확정 컨셉 이름(`docs/design/brand-guide.md`, `claude-harness.md`에 근거) — 포터블 파일에 프로젝트 고유 값이 잘못된 서사로 leak. 확인 필요(미확인 이월). **72차에 별도 인스턴스 재확인: `docs/harness/claude-harness.md` 3번 섹션(문제의 그 파일 자체) 본문에도 "실제 브랜드 컬러(Warm Ledger)"가 그대로 노출돼 있음 — 이번엔 docs/design/이 왜 비포터블인지 설명하는 예시로 쓰였으나, 포터블 문서에 프로젝트 고유 값이 구체적으로 박혀있다는 점은 동일.**
3. [MEDIUM] `ai-image-content-round` SKILL.md가 2-1-C 게이트를 언급하지 않음 — design-pl.md는 이 스킬 로드 지시와 함께 게이트를 요약하지만 스킬 본문 자체엔 없음. 확인 필요(미확인 이월).
4. [MEDIUM, 재발] reset-checklist C-3 줄 번호 참조 드리프트 5회 연속 재발(figma-file-organization.md, content-designer.md). "문구로 찾는 게 안전" 캐비엇으로 기능적 위험은 낮음.

### 확인 필요(LOW, 이월)
5. claude-harness.md가 신설된 `harness-versioning.md`를 인덱스에 언급하지 않음 — 71차 notion-workflow.md 누락과 동일 패턴. **72차 재확인 결과도 여전히 미해소(아래 참고) — 3개 라운드 연속(70→71→72차) 이월.**

### 패턴 메모(누적, 갱신)
- "역할 A에 새 책임/도구를 추가하면 (a) 오케스트레이터 라우팅절, (b) 상대 워커 역할 경계 서술, (c) PL 로스터 요약"을 함께 갱신해야 한다.
- "개념적 원칙(왜/누가)"과 "실행 절차(어떻게)"는 다른 층위다.
- 줄 번호 드리프트 패턴이 5개 라운드 연속(66→70차) 재발 — 근본 해법(줄 번호 대신 앵커/헤딩 참조)을 고려할 시점.
- 새 게이트/절차를 정본 문서에 신설하고 오케스트레이터에는 반영해도, 실행 워커 자기 정의 파일 안의 기존 인접 문단과는 대조·조율하지 않아 같은 파일 안에서 모순이 남는 경우가 있다.
- 오케스트레이션 스킬(SKILL.md)이 실제 사고를 계기로 하드닝된 라운드에서도, 정작 그 사고의 핵심 원인에 대한 언급이 스킬 본문에는 추가되지 않고 개별 에이전트 정의 파일에만 흩어져 반영되는 경우가 있다.

---

## 2026-08-20 (71차) — 사용자 명시 요청: `docs/harness/notion-workflow.md` 신규 생성 + `CLAUDE.md`(테스트 보고서 절 헤딩명 변경, 행동 지침에 notion-workflow.md 참조 추가) + `reset-checklist.md`(A그룹 등록) 정합성 감사 (A 범위)

**결과: 신규 발견 5건(HIGH 1, MEDIUM 3, LOW 2). notion-workflow.md 자체의 자기모순은 발견되지 않음. 72차에 HIGH 1건·LOW 1건(karpathy_skills 목록)·MEDIUM 1건(claude-harness.md 표) 해소 확인, 나머지는 아래 참고.**

1. [HIGH] reset-checklist.md 18번째 줄과 40번째 줄이 CLAUDE.md 헤딩명 갱신을 서로 다르게 반영 → 72차 재확인 결과 해소(양쪽 다 "테스트 보고서 게시(구 …Notion 동기화)"로 일치).
2. [MEDIUM] claude-harness.md 1번 섹션 표에 notion-workflow.md 누락 → 72차 재확인 결과 해소(11번째 줄에 추가됨).
3. [MEDIUM] notion-workflow.md 5번 절과 CLAUDE.md "테스트 보고서 게시" 절 사이 반영 방식(덮어쓰기 vs 새 페이지) 미규정 — 이번 라운드 범위 밖이라 재확인 안 함, 계속 이월.
4. [LOW] reset-checklist.md 39번째 줄 "템플릿으로 그대로 재사용" 목록에 notion-workflow.md 참조 누락 → 72차 재확인 결과 해소.
5. [LOW] `.claude/agent-memory/dev-pl.md`의 옛 헤딩명 잔존 — 72차 재확인 결과도 여전히 남아있음(작업 로그라 엄밀 대상 아님, 계속 참고용 이월).

### 이월 미확인 (70차에서 이월, 72차에도 범위 밖이라 재확인 안 함)
- content-designer.md 페르소나 정의 주체 자기모순(70차 1번), SKILL.md 2-1-C 게이트 미언급(70차 3번).

### 패턴 메모(누적, 갱신)
- "역할 A에 새 책임/도구를 추가하면 (a) 오케스트레이터 라우팅절, (b) 상대 워커 역할 경계 서술, (c) PL 로스터 요약"을 함께 갱신해야 한다.
- "개념적 원칙(왜/누가)"과 "실행 절차(어떻게)"는 다른 층위다.
- 줄 번호 드리프트 패턴이 5개 라운드 연속(66→70차) 재발 — 근본 해법(줄 번호 대신 앵커/헤딩 참조)을 고려할 시점.
- 한 파일 안에서 같은 갱신 사실을 여러 군데서 인용할 때 일부만 갱신되고 나머지가 누락되는 "부분 갱신" 드리프트가 reset-checklist.md 같은 목록형 문서에서 반복될 수 있다.
- `CLAUDE.md` "행동 지침" 절에 `@docs/harness/X.md` 참조 줄을 새로 추가하면 `claude-harness.md` 1번 섹션 표에도 그 파일 행을 추가해야 완결된다.

---

## 2026-08-22 (72차) — 사용자 명시 요청: `harness-auditor.md`(기계적 버전 치환 예외 신설) + `git-workflow.md`(1-1 worktree 운용, 1-2 agent-memory 제외, 6번 자동 감사 신설) + `document-versioning-guide.md`(양방향 인용 갱신 + 예외 언급) + planning-team 4종 가이드(UC-xx, 문서 구성 순서, 메타표+스코프콜아웃 기본뼈대) + `notion-workflow.md`(3-1~3-4, 7번 신설) + `report-format-guide.md`("AI 티 제거" 9번 신설, 절 번호 밀림) + `reset-checklist.md`/`harness-versioning.md`(worktree 전환, 동시 세션 충돌, cp -r/.gitignore 문제) + 루트 `CLAUDE.md`/`.gitignore`(A그룹 untrack, 자동 감사 규칙) 대규모 동시 개정 라운드 정합성 감사 (A 범위 집중, B 범위는 미변경이라 가볍게만 훑음)

**결과: 신규 발견 8건(HIGH 0, MEDIUM 5, LOW 3). 이전 라운드 발견 중 71차 HIGH 1건·LOW 1건·MEDIUM 1건(claude-harness.md notion-workflow.md 누락) 해소 확인. report-format-guide.md 절 번호 밀림으로 인한 깨진 참조는 grep 결과 0건(다른 문서가 그 문서의 구체적 절 번호를 인용하는 사례 자체가 없었음).**

### 신규 발견

1. **[MEDIUM, 신규]** `docs/harness/git-workflow.md` 6절이 "기계적 버전 번호 동기화" 예외의 반복 빈도를 "PRD 개정 이력에서만 10회 넘게 반복된 패턴"이라고 서술하는데, 같은 예외를 설명하는 `docs/harness/planning-team/document-versioning-guide.md`(신규 서술, "이 패턴이 5회 넘게 반복돼")와 `.claude/agents/harness-auditor.md`(기존 서술, "이 프로젝트에서 가장 자주 재발한 패턴이다(5회 이상)")는 "5회"로 적고 있다. "PRD 개정 이력에서만"이라는 더 좁은 범위의 횟수(10회)가 프로젝트 전체 총 횟수로 서술된 다른 두 곳의 수치(5회)보다 크다는 것 자체가 앞뒤가 안 맞는다. 세 곳 모두 이번 라운드에 새로 쓰였거나 인접 라운드에 쓰인 문구라 동시 편집 중 수치가 갈린 것으로 보인다. 확인 필요.
2. **[MEDIUM, 신규]** `docs/harness/notion-workflow.md` 3-1절이 "추후 `report-format-guide.md`에 이 체크리스트가 별도 절로 추가되면 그쪽을 정본으로 참조한다"고 미래형으로 서술하는데, 바로 이번 같은 라운드에 `report-format-guide.md` 9번 절("AI 티 제거")이 실제로 신설되어 이미 존재한다 — 두 파일이 같은 라운드에 동시 편집되면서 한쪽(notion-workflow.md)의 조건부 미래 서술이 다른 쪽(report-format-guide.md)의 실제 완료 사실을 못 따라간 것으로 보인다. 내용 자체(클리셰 어구·문장 길이·과잉 불릿화·헤징·스마트따옴표 등)는 두 문서가 일치한다. 확인 필요.
3. **[MEDIUM, 신규]** `.claude/agents/harness-auditor.md`의 "감사 범위 A" 표제 서술이 `(.claude/agents/**, docs/harness/**)`만 명시하고 `.claude/skills/**`·`.claude/commands/**`를 포함하지 않는데, 바로 같은 라운드에 신설된 자동 실행 트리거(`git-workflow.md` 6절, 루트 `CLAUDE.md` "행동 지침")는 `.claude/agents/**`·`.claude/skills/**`·`docs/harness/**` 세 경로 중 하나라도 바뀌면 harness-auditor를 자동 실행하라고 명시한다. 자동으로 호출되는 상황(스킬만 바뀐 라운드)과 이 에이전트 스스로 규정한 감사 대상 범위가 어긋난다. `reset-checklist.md`의 A그룹 정의(에이전트+스킬+커맨드+docs/harness)는 스킬·커맨드를 포함하므로, harness-auditor 자신의 범위 서술만 더 좁다. 확인 필요.
4. **[MEDIUM, 재발/이월]** `docs/harness/claude-harness.md` 1번 섹션 표에 `docs/harness/harness-versioning.md`가 여전히 없다(70차 5번에서 최초 지적, 71차에도 미해소로 이월). 이번 라운드에 `harness-versioning.md`(worktree 방식 전환 등) 자체와 그걸 참조하는 `git-workflow.md`가 대폭 개정됐는데도 `claude-harness.md`는 이번 라운드에 아예 손대지 않아 격차가 더 벌어졌다. 3개 라운드 연속(70→71→72차) 이월. 확인 필요.
5. **[MEDIUM/가능성 있음, 신규]** `docs/harness/notion-workflow.md` 3-3절이 `docs/harness/planning-team/document-structure-guide.md`의 "메타 표 + 스코프 콜아웃" 패턴을 일반 원칙처럼 인용하는데, 원본(`document-structure-guide.md`)은 이 패턴을 "선례가 전혀 없을 때만 쓰는 기본값"이라고 명시적으로 조건을 좁혀뒀다(기존 문서·전달받은 세트가 있으면 그쪽이 항상 우선). notion-workflow.md 3-3은 이 조건을 언급하지 않아, Notion에 쓰는 모든 문서에 무조건 적용되는 규칙처럼 읽힐 여지가 있다. 확인 필요(가능성 있음 — 실제 운영에서 로컬 선례가 있을 때 이 콜아웃을 생략해도 되는지 불분명).

### LOW

6. **[LOW, 신규]** `docs/harness/planning-team/test-plan-design-guide.md`의 "추적성" 본문은 "PRD에 유스케이스 상세가 있으면 UC-xx도" 매핑 대상에 새로 추가했지만, 바로 아래 체크리스트 항목("모든 케이스가 AC/FR/SCR 중 하나에 매핑되는가?")은 갱신되지 않아 UC-xx가 빠져 있다.
7. **[LOW, 신규]** `docs/harness/reset-checklist.md` A그룹 목록의 `prd-writing-guide.md`(서비스 트라이앵글·스코프 트레이드오프·비목표 감별)·`screen-spec-pattern-guide.md`(화면정의서 4종 세트·오버레이 포함 원칙)·`document-structure-guide.md`(문서 구조 상속) 괄호 설명이 이번 라운드에 각 파일에 추가된 신규 절(유스케이스 UC-xx, 문서 전체 구성 순서, 선례 없을 때 기본 뼈대)을 반영하지 않아 요약이 낡았다. 파일 존재 여부나 분류 자체는 틀리지 않음 — 순수 설명 텍스트 완결성 문제.
8. **[LOW, 재확인/이월]** C-3 줄 번호 드리프트 계속 재발 확인 — `content-designer.md`의 "제품 화면(로그인, 연락처 관리 등)..." 문구가 실제로는 57번째 줄인데 reset-checklist.md는 "현재 50번째 줄"로, `figma-file-organization.md`의 "연락처" 예시 두 곳이 실제로는 55·193번째 줄인데 "53·186번째 줄"로 각각 표기돼 있다. "문구로 찾는 게 안전"이라는 기존 캐비엇 덕에 기능적 위험은 낮음 — 6개 라운드 연속(66→72차) 재발.

### 확인됨(문제 없음)
- `git-workflow.md`·`reset-checklist.md`·`harness-versioning.md` 세 곳의 `.gitignore` 두 버전(main용 A그룹 경로 무시, harness worktree용 agent-memory 무시) 설명이 서로 모순 없이 일치.
- `git-workflow.md` 내부 절 번호 상호 참조("아래 1-1번 참고" 등)가 실제 절 번호와 정확히 일치, 1-1·1-2·6번 신설 후에도 참조 깨짐 없음.
- `.claude/agents/harness-auditor.md`의 새 예외 문구와 `document-versioning-guide.md`의 예외 언급이 (반복 횟수 수치를 제외하면) 조건·범위 면에서 서로 일치.
- `report-format-guide.md` 절 번호가 밀렸음에도(9번 신설로 구 9번→10번), 실제로 이 문서의 구체적 절 번호를 인용하는 다른 파일(`.claude/agents/doc-writer.md` 등)이 없어 깨진 참조 없음(전부 grep 확인).
- `reset-checklist.md`가 이번에 여러 세션에서 동시 수정됐음에도 내부 중복·충돌 서술은 발견되지 않음(다른 세션들이 다룬 절이 서로 겹치지 않게 분리돼 있었던 것으로 보임).

### 패턴 메모(누적, 갱신)
- "역할 A에 새 책임/도구를 추가하면 (a) 오케스트레이터 라우팅절, (b) 상대 워커 역할 경계 서술, (c) PL 로스터 요약"을 함께 갱신해야 한다.
- "개념적 원칙(왜/누가)"과 "실행 절차(어떻게)"는 다른 층위다.
- 줄 번호 드리프트 패턴이 6개 라운드 연속(66→72차) 재발 — 근본 해법(줄 번호 대신 앵커/헤딩 참조)을 고려할 시점.
- **신규 패턴(72차): 같은 사건(신설 규칙)의 반복 횟수·통계 수치를 여러 문서에 나눠 적을 때, 동시 편집 중 수치 자체가 갈리는 경우가 있다 — 버전 문자열뿐 아니라 "N회" 같은 서술적 수치도 인용 정합성 점검 대상에 넣어야 한다.**
- **신규 패턴(72차): 한 문서가 "다른 문서에 이 내용이 추후 추가되면 그쪽을 참조한다"는 조건부 미래 서술을 남겼는데, 바로 그 라운드에 그 다른 문서가 실제로 갱신되며 조건이 이미 충족돼버리는 경우가 있다 — 두 파일이 병렬로 편집될 때 서로의 완료 여부를 확인하지 않으면 미래형 서술이 즉시 stale해진다.**
- **신규 패턴(72차): 에이전트 자신의 "역할/범위" 서술과, 그 에이전트를 호출하는 다른 문서의 "트리거 조건" 서술이 별도로 진화하면서 범위가 어긋나는 경우가 있다(harness-auditor의 감사범위 vs git-workflow.md의 자동실행 스코프) — 자동화 트리거를 새로 추가할 때는 호출되는 쪽의 자기 범위 서술도 같이 넓혀야 한다.**
- claude-harness.md 인덱스 표 누락 패턴이 이제 3라운드 연속(harness-versioning.md, 70→71→72차) 미해소로 이월 중 — 다음 라운드에서 우선 해소 권장.

---

# 하네스 리셋 체크리스트

## 목적

이 프로젝트(연락처 관리 웹 서비스)에서 만든 하네스(에이전트/스킬/절차)를 **다른 프로젝트에서 재사용**하거나, 이 프로젝트를 **"파일럿 종료 → 정식 시작"으로 초기화**할 때, 무엇을 남기고 무엇을 지울지 정리한 문서다.

원칙은 하나다: **절차(procedure, 프로젝트 고유 값이 하드코딩되지 않은 것)는 남기고, 데이터(이 프로젝트가 실제로 만든 산출물)는 지운다.** 이 구분은 `docs/harness/claude-harness.md`에 이미 있는 원칙이고, 이 문서는 그 원칙을 실제 파일 목록에 적용해 체크리스트로 구체화한 것이다.

**이 문서 자체도 A그룹(하네스)이다** — 프로젝트 고유 값 없이 다른 프로젝트에 그대로 복사해서 쓸 수 있어야 한다. 리셋할 때마다 아래 목록에 없는 새 파일이 생겼을 수 있으니, 실행 전 "검증 방법" 섹션으로 한 번 더 확인한다.

## A. 그대로 유지 (하네스 — 포터블)

- `.claude/agents/*.md` — 전체 24개(디자인팀 12 + 기획팀 5 + 개발+QA팀 4[dev-pl, backend-engineer, frontend-engineer, qa-engineer] + code-reviewer, doc-writer, harness-auditor)
- `.claude/skills/*/SKILL.md` — design-concept-round, report-pdf, review, summary
- `.claude/commands/*.md` — summary.md
- `.claude/hooks/stop-failure-notify.sh` — 스크립트 로직 자체는 포터블(단, 아래 C-2 웹훅 파일은 별도 취급)
- `docs/harness/**` — claude-harness.md, git-workflow.md, design-team/figma-file-organization.md, 이 리셋 체크리스트, report-format-guide.md·report-style.css(범용 보고서 HTML/PDF 템플릿 — 프로젝트 브랜드 색이 아니라 남색/호박색 범용 톤이라 포터블. `docs/design/`에 잘못 있던 것을 이번에 이쪽으로 재분류함, 2026-07-16), 그리고 design-team 아래 다음 크래프트/감사 참조 문서들(전부 노드 ID·hex 등 프로젝트 고유 값 미포함, design-systems/graphic-designer/interaction-designer/motion-designer가 만들 때 참조하고 design-qa가 감사할 때 검증 기준으로 삼는 공용 포터블 문서):
  - `design-team/figma-page-format-guide.md`(문서화 페이지 시각 포맷 표준 — 스와치 카탈로그·컴포넌트 스펙 시트 서식 원칙과 체크리스트, 2026-07-16 신설)
  - `design-team/icon-craft-guide.md`(아이콘 Basic/Visual 트랙 구분 — 트랙 판정 기준, 면색 유무, 스트로크 두께 원칙, 2026-07-17 신설)
  - `design-team/component-state-guide.md`(컴포넌트 상태 커버리지·네이밍 — State 축 네이밍, 유형별 필수 상태, Disabled 색 토큰 표현, 아이콘 INSTANCE 조립 원칙, 2026-07-17 신설)
  - `design-team/token-architecture-guide.md`(토큰 아키텍처 — 3계층 구조, elevation 제한 사용, padding+hug 높이, 텍스트 Property 노출 원칙, 2026-07-17 신설)
  - `design-team/motion-timing-guide.md`(모션 타이밍·퍼포먼스 — duration·easing·루프·성능 기준, 2026-07-17 신설)
- `docs/karpathy_skills.md`
- `pdf-maker/make-pdf.js`, `pdf-maker/package.json` — md→PDF 변환 유틸리티(절차/도구), 생성물은 B그룹
- `.gitignore` — 항목 전부가 이 프로젝트 데이터가 아니라 Python 범용 관례(`.venv/`, `__pycache__/`, `.pytest_cache/`)나 A그룹 도구/인프라에 종속된 무시 규칙(`pdf-maker/node_modules/`, `pdf-maker/결과.pdf`, `.claude/settings.local.json`, `.claude/hooks/.slack-webhook-url`)이다. 새 프로젝트에서 일부 경로(예: pdf-maker를 안 쓰는 프로젝트)가 안 맞아도 그냥 매칭 안 될 뿐 해롭지 않으므로 그대로 유지한다

## B. 삭제/초기화 (이 프로젝트 데이터 — 포터블 아님)

- `docs/design/*.md` — brand-guide.md, design-system.md, graphic-assets.md, missing-screens.md
- `docs/design/confirmed/*.md` — 사용자가 확정한 이 프로젝트 디자인 기록
- `docs/planning/**` — 00~06 번호 문서(md·PDF 전부), `old/`, `service-concept.md`, `tech-architecture.md` 전부
- `docs/pdf/**` — 생성된 PDF/HTML 산출물
- `.claude/logs/stop-failures.log`
- `backend/`, `static/`, `frontend/`, `tests/`, `pdf-maker/문서.html`, `pdf-maker/결과.pdf` — 실제 애플리케이션 코드/생성물. **`backend/CLAUDE.md`/`frontend/CLAUDE.md`(이 프로젝트의 확정 스택·파일구조 요약)도 포함** — 삭제해도 문제없다, backend-engineer/frontend-engineer가 새 프로젝트에서 작업을 시작하면 그 프로젝트의 `docs/planning`·`docs/design`을 읽어 그 자리에서 다시 만들어내도록 하네스 규칙(`.claude/agents/backend-engineer.md`·`frontend-engineer.md` "할 일 0번")에 이미 명문화돼 있다 — 수동으로 남겨둘 필요 없음. **`static/`은 실제로 서빙되는 화면 코드(`index.html`/`app.js`)가 들어가는 폴더로, `backend/`·`frontend/`와 형제 폴더다(05 TRD §3) — 가이드 문서가 아니라 이 프로젝트 고유의 구현 산출물이므로 B그룹이 맞다.**
- 루트 `CLAUDE.md` — 이 프로젝트 고유 규칙(들여쓰기, 검증 명령 등). 새 프로젝트는 새로 작성하되, 이 파일의 "행동 지침"·"기본 도구" 절만 템플릿으로 참고 가능
- `.claude/agent-memory/*.md`의 "작업 로그" 섹션 내용 — 파일 자체는 남겨도 되지만 내용은 비우거나 "신설" 상태로 리셋(에이전트가 다음 실행 시 알아서 새로 채움)

## C. 케이스별 검토 필요 (자동 처리 금지 — 리셋 시점에 사람이 직접 확인)

1. **`.claude/settings.local.json`**: `permissions.allow` 안의 Bash 허용 목록 다수가 이 프로젝트의 **절대경로**(`/Users/aydana/dev/big21/project/02_web_phonebook/...`)를 하드코딩하고 있다(실측: 7곳). 다만 이 파일은 `.gitignore` 대상이라 git 기반 하네스 공유(레포 복사 등)로는 애초에 전파되지 않고, Claude Code 자체도 프로젝트 절대경로를 키로 권한을 관리하므로(`~/.claude.json`의 `projects` 항목도 경로별로 분리) **새 프로젝트 폴더를 열면 자동으로 빈 상태로 시작된다 — 별도 리셋 작업이 필요 없다.** 유일하게 신경 쓸 경우는 `.claude/` 폴더를 git을 거치지 않고 파일째로(cp 등) 새 프로젝트에 복사할 때뿐이며, 이때도 옛 경로 항목은 그냥 안 쓰이는 죽은 줄로 남을 뿐 실질적 위험은 없다 — 지저분함이 싫으면 지우는 정도.
2. **`.claude/hooks/.slack-webhook-url`**: `.gitignore` 처리돼 있어 git에는 안 남지만 디스크에는 실제로 남아있다. 이건 프로젝트가 아니라 **사람(작업자)에 연결된 자격증명**이라 오히려 재사용 가능하다 — 지우지 않고 그대로 둬도 된다. 워크스페이스/Slack 채널이 바뀔 때만 재설정.
3. **예시 문장에 프로젝트명·Figma 노드 ID가 하드코딩된 곳**: 프로젝트명(예: "연락처 관리 웹 서비스")보다 **Figma 노드 ID**(예: `259:609`)가 더 조심해야 할 대상이다 — 프로젝트명은 새 프로젝트에서 읽었을 때 "예시구나" 하고 넘어갈 수 있지만, 노드 ID는 새 프로젝트의 Figma 파일에서 완전히 무관한(또는 존재하지 않는) 요소를 가리키므로 그대로 읽으면 혼란을 준다. `.claude/agents/*.md`·`docs/harness/**`(포터블 문서)에 컴포넌트 예시를 들 때는 **노드 ID 없이 이름만** 적는다 — 구체적 ID가 필요하면 `docs/design/design-system.md`(프로젝트 데이터, 매번 새로 채워짐)를 참고하라고 안내한다. — 기능적 로직에는 영향 없지만 새 프로젝트에 그대로 복사하면 예시가 어색해진다. 복사 시점에 프로젝트명만 치환 권장(삭제 대상 아님). **줄 번호는 문서가 수정될 때마다 밀릴 수 있으니, 리셋 실행 시점에 매번 재확인한다(2026-07-17, stale 참조 정정 사례로 아래 항목 갱신):**
   - `.claude/agents/brand-designer.md` 21번째 줄 — "이 프로젝트(연락처 관리 웹 서비스)에 맞게"
   - `.claude/agents/planning-writer.md` 18번째 줄, `.claude/agents/qa-planner.md` 23번째 줄 — `06_연락처관리_웹서비스_테스트계획서_v1.0.md` 예시 파일명
   - `docs/harness/design-team/figma-file-organization.md` 45번째 줄("연락처" 화면 카테고리 예시)과 176번째 줄("이 프로젝트(예: 폼이 있는 연락처 관리 서비스)" — 2-6번 선제적 기본 구성 판단 기준 예시) — 두 곳 모두 "연락처" 예시 언급(2026-07-17, 두 번째 occurrence 신규 반영)
   - `.claude/agents/service-planner.md`·`.claude/agents/tech-architect.md`·`.claude/agents/dev-pl.md` — "이 프로젝트는 FastAPI+DB 과제" 류의 스택 예시 언급. 전부 "지금 이 프로젝트는 X지만 다음 프로젝트는 그 문서를 따라간다" 식으로 명시적으로 비하드코딩 처리돼 있어 기능적으로는 안전하지만, 새 프로젝트 복사 시 예시 문구만 참고용임을 인지할 것
4. **`~/.claude/agents/*.md` (전역)**: 디자인팀 12개 + 개발+QA팀 4개(dev-pl, backend-engineer, frontend-engineer, qa-engineer)는 이미 복사돼 있다. 기획팀 5개(planning-pl, service-planner, tech-architect, qa-planner, planning-writer)는 아직 프로젝트 로컬에만 있다 — 다른 프로젝트에서도 기획팀을 쓰려면 이때 전역으로 복사할지 결정한다(리셋과 별개로, 아직 결정 안 된 사항).

## 검증 방법 (리셋 실행 전 필수)

1. **커밋 먼저**: 이 문서를 작성한 시점 기준으로 `docs/planning/`, `.claude/agents/planning-*.md`를 포함한 다수 파일이 아직 **git에 커밋되지 않은 상태(untracked)**였다. B그룹을 삭제하면 git 히스토리 백업이 없어 복구 불가능하니, 리셋 실행 직전 반드시 `git status`로 미커밋 상태를 확인하고 커밋(또는 최소한 별도 백업)한 뒤 진행한다.
2. **A그룹에 데이터 흔적이 없는지 grep으로 재확인**(리셋 때마다, 이 체크리스트가 최신인지 검증):
   ```bash
   grep -rl "연락처\|phonebook\|<이 프로젝트의 Figma 파일키>" .claude/agents .claude/skills .claude/commands docs/harness docs/karpathy_skills.md
   ```
   결과가 이 문서의 C-3 목록과 다르면(새 파일이 나오면) 새로 생긴 하드코딩이니 이 체크리스트를 갱신한다.
3. **B그룹 삭제 후 A그룹이 정상 동작하는지 확인**: 리셋 후 아무 기획/디자인 요청이나 하나 던져서 planning-pl 또는 design-pl이 정상 기동하고, `docs/planning/service-concept.md` 등 canonical 문서를 스스로 새로 만드는지 확인한다.

## 실행 순서 (요약)

1. `git status`로 미커밋 변경사항 확인 → 커밋
2. B그룹 파일/디렉토리 삭제
3. C그룹 항목 하나씩 사람이 직접 검토·처리
4. 검증 방법의 grep 재확인
5. 새 프로젝트 성격에 맞는 새 루트 `CLAUDE.md` 작성
6. 정상 동작 확인(위 3번 검증)

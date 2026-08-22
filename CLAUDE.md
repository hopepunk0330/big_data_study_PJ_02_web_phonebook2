# 프로젝트 안내

## 개요
이 프로젝트는 연락처 관리 웹 앱이다

## 코딩 규칙
- 들여쓰기는 공백 4칸을 쓴다.
- 함수와 변수 명은 영어 카멜표기법 사용한다.
- SDD, TDD 방식으로 개발한다. 

## 검증 명령
-- 테스트 : python -m pytest
-- 형식 검사 : python -m ruff check backend/ (설정: pyproject.toml)

## 금지
- 내 명시적 허락 없이 원격 저장소로 push 하지 않습니다 — **예외(2026-08-22 명시)**: `harness` 브랜치 → `origin` push는 이번 세션에서 이미 반복적으로 확립된 고정 채널이라, 매번 다시 확인받지 않고 진행한다. `assignment`로의 push와 `main` → `assignment`/`origin` push는 이 예외에 포함되지 않으며 여전히 매번 명시적 확인이 필요하다.
- secrets 폴더와 .env 파일은 절대 수정하지 않는다.

## Git 리모트/브랜치 관례
- 리모트가 두 개다: `assignment`(실제 과제 제출용 저장소) / `origin`(JY_Harness, 사용자의 개인 하네스·템플릿 저장소 — 여러 프로젝트에서 재사용하는 `.claude/agents/**`·`docs/harness/**` 자산을 추적).
- 브랜치+PR 게이트는 **실제 구현 코드**(예: `backend/`, `static/` — TRD가 정한 코드 폴더)에만 적용한다: 브랜치 생성 → code-reviewer 리뷰 → 사용자 승인 → PR 머지.
- **하네스 정의(`.claude/agents/**`·`docs/harness/**`, `reset-checklist.md` A그룹 전체)는 `main`이 아니라 전용 `harness` 브랜치에만 커밋한다**(2026-08-20 신설 — 이전엔 main에 직접 커밋했으나, main은 assignment가 최종적으로 받는 과제 제출 브랜치라 하네스가 섞이면 안 됨). `harness` 브랜치는 별도 worktree 폴더에서만 편집·커밋하는 독립 트랙이다(`main` 폴더 자체에서 checkout으로 오가지 않는다 — 자세한 건 `git-workflow.md` 1-1번). **2026-08-22부터 `main`은 이 경로들을 `.gitignore`로 아예 추적하지 않는다** — 기존에 커밋돼 있던 것도 `git rm --cached`로 인덱스에서 뺐다(파일 자체는 harness 브랜치 동기화로 디스크에 최신 상태로 남아 Claude Code가 계속 읽는다). 과거 커밋 이력 자체(assignment/origin의 main에 이미 들어간 하네스 커밋)를 소급 제거하는 건 별도 작업(`git filter-repo`)이라 사용자가 명시적으로 요청할 때만 진행한다. 상세 절차는 `docs/harness/git-workflow.md` 참고.
- 그 외(기획 문서 `docs/planning/**`, 디자인 산출물 `docs/design/**`, 루트/팀별 `CLAUDE.md`의 프로젝트 고유 섹션, `tests/` 등)는 지금까지처럼 브랜치를 거치지 않고 `main`에 직접 커밋·푸시한다(대화 중 사용자가 그때그때 확인하는 방식).
- push 대상: `harness` 브랜치는 `origin`에만 push한다(`git push origin harness`, 동일 브랜치명) — `assignment`로는 절대 push하지 않는다. `main`은 지금까지처럼 `assignment`·`origin` 양쪽에 push한다(단, main에는 이제 새 하네스 커밋이 안 쌓이므로, origin의 `main`은 과거 이력 스냅샷으로 고정되고 실제 최신 하네스는 origin의 `harness` 브랜치가 담는다).
- 원격 저장소로의 실제 push는 매번 사용자의 명시적 확인을 받은 뒤에만 수행한다(위 "금지" 항목과 동일) — 단, `harness` 브랜치 → `origin` push는 위 "금지" 항목의 예외에 해당해 매번 재확인하지 않는다.

## 테스트 보고서 게시 + 문서 버전관리
- `docs/test-reports/`의 단위/통합 테스트 보고서를 갱신할 때마다, 아래 두 Notion 페이지에도 최신 내용을 반영한다(본문을 매번 최신 내용으로 덮어쓴다 — `docs/harness/notion-workflow.md`의 "기존 콘텐츠 절대 편집 금지" 원칙과는 무관한 이 프로젝트만의 별도 관례다, 2026-08-20 명시):
  - https://app.notion.com/p/3a0ebec5c35780209583f1ab3a044142?source=copy_link
  - https://app.notion.com/p/3a0ebec5c35780f4a977c2bcef334956?source=copy_link
- 버전관리: 새 보고서로 덮어쓰기 전에 이전 버전을 `docs/test-reports/old/`(없으면 생성) 폴더로 옮기고 원본 파일명 그대로 보존한다. `docs/test-reports/`에는 항상 각 종류(단위/통합)의 최신본만 남긴다.
- `docs/screenshot/`도 같은 원칙: 화면 변경으로 더 이상 현재 UI를 반영하지 않는 캡처는 정기적으로 정리한다(같은 스텝 번호라도 설명 접미사가 다르면 서로 다른 시나리오일 수 있으니 내용 확인 후 삭제 — 번호만 보고 일괄 삭제 금지).

## 행동 지침
- 안드레 카파시 행동지침에 아래 문서를 따른다. @docs/harness/karpathy_skills.md
- Notion 작업(MCP로 연결해서 쓰기) 시 아래 문서를 따른다. @docs/harness/notion-workflow.md
- 하네스(`.claude/agents/**`, `.claude/skills/**`, `docs/harness/**`)를 추가·수정하는 작업 라운드가 끝나면, 물어보지 않고 바로 `harness-auditor`를 실행한다(2026-08-22 신설 — 자세한 절차는 `docs/harness/git-workflow.md` 6절). 발견된 문제를 실제로 고칠지는 그 결과를 보고한 뒤 사용자 확인을 받는다 — 자동 실행은 감사 실행 자체에만 적용되고, 수정까지 자동으로 하지는 않는다.

## 소통 방식
- 사용자에게는 항상 존댓말로 응답한다(반말 금지) — 2026-08-20 명시적 요청. 새 프로젝트를 시작할 때마다 반말로 시작하는 문제가 반복돼 전역 규칙으로 고정한다.

## 기본 도구
- 테스트: playwright를 기본으로 사용한다.
- 라이브러리/API 문서 조회: context7 MCP를 기본으로 사용한다(설치 안 돼 있으면 `claude mcp add context7 -s user -- npx -y @upstash/context7-mcp`로 전역 설치).
- playwright로 테스트할때 캡쳐를 해줘. 나중에 메뉴얼을 만들때 사용할거야. 폴더 저장 위치는 docs/screenshot에 화면위치를 스텝순서를 번호를 부여해서 파일명으로 저장해줘.

이 항목들("소통 방식"·"기본 도구")은 전역 `~/.claude/CLAUDE.md`에도 반영돼 있어, 프로젝트별 CLAUDE.md에 별도 명시가 없어도 모든 프로젝트에서 기본으로 적용된다.

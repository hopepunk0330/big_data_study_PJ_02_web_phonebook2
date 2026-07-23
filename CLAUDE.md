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
- 내 명시적 허락 없이 원격 저장소로 push 하지 않습니다
- secrets 폴더와 .env 파일은 절대 수정하지 않는다.

## Git 리모트/브랜치 관례
- 리모트가 두 개다: `assignment`(실제 과제 제출용 저장소) / `origin`(JY_Harness, 사용자의 개인 하네스·템플릿 저장소 — 여러 프로젝트에서 재사용하는 `.claude/agents/**`·`docs/harness/**` 자산을 추적).
- 브랜치+PR 게이트는 **실제 구현 코드**(예: `backend/`, `static/` — TRD가 정한 코드 폴더)에만 적용한다: 브랜치 생성 → code-reviewer 리뷰 → 사용자 승인 → PR 머지.
- 그 외(기획 문서 `docs/planning/**`, 디자인 산출물 `docs/design/**`, 하네스 정의 `.claude/agents/**`·`docs/harness/**`, 루트/팀별 `CLAUDE.md`, `tests/` 등)는 브랜치를 거치지 않고 main에 직접 커밋·푸시한다(대화 중 사용자가 그때그때 확인하는 방식). 자세한 기준은 `docs/harness/git-workflow.md` 참고.
- `.claude/agents/**`·`docs/harness/**`(하네스 파일)을 수정하면, assignment 제출과 별개로 origin(JY_Harness)에도 동일하게 main 직접 커밋으로 반영한다 — 하네스 변경은 두 리모트 모두에 반영하는 게 기본 패턴이다.
- 어느 경로든, 원격 저장소로의 실제 push는 매번 사용자의 명시적 확인을 받은 뒤에만 수행한다(위 "금지" 항목과 동일).

## 테스트 보고서 Notion 동기화 + 문서 버전관리
- `docs/test-reports/`의 단위/통합 테스트 보고서를 갱신할 때마다, 아래 두 Notion 페이지에도 최신 내용을 반영한다:
  - https://app.notion.com/p/3a0ebec5c35780209583f1ab3a044142?source=copy_link
  - https://app.notion.com/p/3a0ebec5c35780f4a977c2bcef334956?source=copy_link
- 버전관리: 새 보고서로 덮어쓰기 전에 이전 버전을 `docs/test-reports/old/`(없으면 생성) 폴더로 옮기고 원본 파일명 그대로 보존한다. `docs/test-reports/`에는 항상 각 종류(단위/통합)의 최신본만 남긴다.
- `docs/screenshot/`도 같은 원칙: 화면 변경으로 더 이상 현재 UI를 반영하지 않는 캡처는 정기적으로 정리한다(같은 스텝 번호라도 설명 접미사가 다르면 서로 다른 시나리오일 수 있으니 내용 확인 후 삭제 — 번호만 보고 일괄 삭제 금지).

## 행동 지침
- 안드레 카파시 행동지침에 아래 문서를 따른다. @docs/karpathy_skills.md

## 기본 도구
- 테스트: playwright를 기본으로 사용한다.
- 라이브러리/API 문서 조회: context7 MCP를 기본으로 사용한다(설치 안 돼 있으면 `claude mcp add context7 -s user -- npx -y @upstash/context7-mcp`로 전역 설치).
- playwright로 테스트할때 캡쳐를 해줘. 나중에 메뉴얼을 만들때 사용할거야. 폴더 저장 위치는 docs/screenshot에 화면위치를 스텝순서를 번호를 부여해서 파일명으로 저장해줘.

이 항목들은 전역 `~/.claude/CLAUDE.md`에도 반영돼 있어, 프로젝트별 CLAUDE.md에 별도 명시가 없어도 모든 프로젝트에서 기본으로 적용된다.

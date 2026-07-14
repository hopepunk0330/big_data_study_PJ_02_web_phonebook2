# 프로젝트 안내

## 개요
이 프로젝트는 연락처 관리 웹 앱이다

## 코딩 규칙
- 들여쓰기는 공백 4칸을 쓴다.
- 함수와 변수 명은 영어 카멜표기법 사용한다.
- SDD, TDD 방식으로 개발한다. 

## 검증 명령
-- 테스트 : python -m pytest
-- 형식 검사 : lint 사용

## 금지
- 내 명시적 허락 없이 원격 저장소로 push 하지 않습니다
- secrets 폴더와 .env 파일은 절대 수정하지 않는다.

## 행동 지침
- 안드레 카파시 행동지침에 아래 문서를 따른다. @docs/karpathy_skills.md

## 기본 도구
- 테스트: playwright를 기본으로 사용한다.
- 라이브러리/API 문서 조회: context7 MCP를 기본으로 사용한다(설치 안 돼 있으면 `claude mcp add context7 -s user -- npx -y @upstash/context7-mcp`로 전역 설치).

- 이 두 가지는 프로젝트별 CLAUDE.md에 별도 명시가 없어도 모든 프로젝트에서 기본으로 적용한다.




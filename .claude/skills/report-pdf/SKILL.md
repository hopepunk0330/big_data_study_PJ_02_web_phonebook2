---
name: report-pdf
description: MD 문서를 docs/design 템플릿 스타일의 HTML로 옮긴 뒤 PDF로 변환합니다 (doc-writer + pdf-maker 오케스트레이션).
---

다음 소스 문서를 사람이 읽는 보고서 PDF로 변환해 주세요: @$ARGUMENTS

절차:

1. **템플릿 쌍을 정한다.** 별도 지정이 없으면 기본값은 `docs/design/report-style.css` + `docs/design/report-format-guide.md`다. (나중에 발표용 등 다른 형식이 생기면 `docs/design/slide-*` 같은 다른 쌍을 추가로 만들어 쓸 수 있다 — 사용자가 어떤 쌍을 쓸지 명시하면 그것을 따른다.) 내용 규칙(사람이 읽는 문서로 작성, 스타일 인라인, 구조 준수, 임의 요약 금지 등)은 doc-writer 자신의 역할 정의에 이미 있으므로 여기서 반복하지 않는다.
2. **doc-writer 서브에이전트를 호출**해, `docs/pdf/html/`(없으면 먼저 생성)에 소스 문서와 같은 파일명으로(`.md` → `.html`) 시각화 문서(보고서 PDF)를 작성하게 한다. 1번에서 정한 템플릿 쌍이 기본값과 다르면 그것만 명시한다.
3. **여기서 멈춘다.** PDF로 곧바로 변환하지 않는다. doc-writer가 만든 HTML 경로를 사용자에게 알리고, 내용을 확인·수정할 시간을 준다. 수정 요청이 있으면 반영하고(doc-writer를 다시 부르거나 직접 Edit), 다시 확인받는다.
4. **사용자가 이 HTML로 PDF를 만들어도 좋다고 명시적으로 확인한 뒤에만**, 메인 세션이 직접 `node pdf-maker/make-pdf.js <docs/pdf/html/ 안의 html 절대경로> <docs/pdf/ 안의 같은 이름의 pdf 절대경로>`를 실행해 PDF로 변환한다. (doc-writer는 Bash 권한이 없어 이 단계를 할 수 없다.)
5. 변환된 PDF 경로를 사용자에게 보고한다.

산출물 위치 규칙: 소스 MD의 위치와 무관하게, 중간 HTML은 `docs/pdf/html/`에, 최종 PDF는 `docs/pdf/`(최상위)에 둔다. pdf-maker/ 폴더에는 아무것도 두지 않는다 — pdf-maker는 변환 도구 전용 폴더다. 파일명은 소스와 동일, 확장자만 다르게 한다.

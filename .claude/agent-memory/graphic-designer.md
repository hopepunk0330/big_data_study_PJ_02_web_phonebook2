# graphic-designer 메모리

이 파일은 graphic-designer의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **그린 그래픽 목록(현재 확정 상태)은 여기 없습니다 — `docs/design/graphic-assets.md`(또는 프로젝트별 `docs/design/{슬러그}/graphic-assets.md`)가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-17 — Pixel/Search 색상 검증(teal→sky/500), 그리기 작업 아님
- 배경: 메인 세션이 확정 main 프레임 안 `PxSearch`(`501:6390`) 13개 벡터를 직접 실측해 전부 sky `#1395e6`임을 확인, 반면 마스터 `Pixel/Search`(`255:26`)는 위 색상 감사 절에서 teal/500(A그룹, 재해석 불필요)로 이미 판정돼 있어 모순 발견 — 신뢰 형식으로 sky/500 리바인딩 승인, 확인/판정만 수행(벡터 직접 수정 없음).
- 트랙 판정: Pixel/Search는 icon-craft-guide의 Icon/* 24px Basic/Visual(스트로크 유무) 이분법이 아니라 별도의 Pixel/* 마이크로 픽셀 블록-실루엣 트랙(스트로크 개념 없음, 항상 solid fill)에 속함 — 이 트랙 안에서는 fill 유무가 Basic/Visual 구분 신호가 아니므로, teal→sky 색상 토큰 교체는 트랙 규칙(strokeWeight·fill 구성)을 전혀 건드리지 않음. 위반 없음.
- `docs/design/graphic-assets.md`에 "Pixel/Search 색상 검증" 절 신규 append. **전달 대상**: design-systems(마스터 `255:26`의 13개 벡터 fill teal/500→sky/500 실제 리바인딩 실행).

### 2026-07-17 — Auth 페이지(`934:2`) BgPixels/ConfettiFooter 컨페티 오브제 불투명도 결함 수정 (사용자 이슈 제보, 직접 수정)
- 사용자 제보: "로그인 화면 뒤에 bg의 블루배경에 있는 오브제들의 컬러가 달라" — 노드 `934:2` 확인 요청.
- `use_figma` 읽기 전용으로 각 프레임의 `BgPixels`/`ConfettiFooter` 전체 fill/opacity/boundVariables 실측 — 실제 결함은 opacity(별만 스펙대로 25~40%, 다이아몬드·십자는 전부 opacity 1)였음.
- `use_figma`로 3개 프레임 총 42개 노드의 opacity 수정. **⚠ 후속: "fill 색 자체는 문제 없다"는 이 판단은 다음 라운드에서 틀린 것으로 정정됨.**
- `docs/design/graphic-assets.md`에 절 신규 append. **전달 대상**: 없음(직접 완료, design-pl 참고 보고).

### 2026-07-17 — Auth 페이지(`934:2`) BgPixels 컬러 자체 오류 정정 (사용자 3차 재확인, 전수 hex 재실측 → 직접 수정)
- 사용자가 opacity 수정 후에도 "컬러 자체가 여전히 원본과 다르다"고 3차 재확인 요청 — 직전 라운드의 "ink/900 바인딩이니 정상" 결론이 틀렸음을 확인.
- 원본은 배치 위치에 따라 다른 색 체계(BgPixels 다이아몬드·십자=흰색, 별=앰버 / ConfettiFooter=잉크)를 쓰고 있었는데, 934:2의 8개 프레임 전체가 예외 없이 잉크색으로 잘못 복제돼 있었음.
- `use_figma`로 8개 프레임 총 122개 노드(색상 112 + opacity 10) 수정. `get_screenshot`으로 재검증 완료.
- `docs/design/graphic-assets.md`에 절 신규 append. **전달 대상**: design-pl(① 이전 결론이 틀렸다는 점, ② 935:33이 공유 컴포넌트가 아니라는 구조적 발견 참고 보고).

### 2026-07-18 — docs/planning 버전 재동기화 (01_구현요구사항 v1.12→v1.13, 02_화면정의서 v1.16→v1.17), 그리기 작업 아님
- 순수 버전 번호 재동기화 요청. `docs/design/graphic-assets.md`가 인용하던 두 문서 버전 문자열을 최신으로 갱신(146행 1곳). 다른 서술·판단은 무변경.
- **전달 대상**: 없음(순수 문서 인용 버전 동기화, 디자인 판단 아님).

### 2026-08-25 — mercari 프로젝트(`SIBLz4S4IZbjabzhMSAgdo`) chevron-right/star-01/shield-check 3종 raw FRAME → 표준 아이콘 프레임 정리 (design-qa HIGH 지적 대응)
- design-qa가 지적한 "확정 화면 안 raw FRAME 조립으로 재사용 불가" 문제 대응. 확정 화면 노드 ID가 브리프에 적힌 것과 달라져 있어(`Concept A_01`류 구 ID 전부 not found) "UI 디자인" 페이지 `SCR-002/SCR-003 가격 제안 화면` 섹션(`187:2673`)에서 이름이 `_SCR-002` 접미사로 바뀐 동일 화면 7개를 재발견 — 확정 화면 자체는 열람만, 수정 없음.
- `icon-craft-guide.md` 기준으로 트랙 새로 판정(브랜드 가이드의 라인/면 서술과 무관하게): `chevron-right`=Basic/Utility(반복되는 순수 방향 기호, 이미 stroke-only), `star-01`·`shield-check`=Visual/Feature(신뢰 신호, 브랜드색). 3종 다 이미 관찰된 형태가 해당 트랙 규칙에 부합해 형태 변경 없이 표준 24×24/12×12/32×32 프레임으로 구조만 이전.
- 신설 "--- GRAPHIC ASSETS ---"(`195:2`)·"Graphic Assets"(`195:3`) 페이지에 3개 아이콘 정리본 완성(`195:14`/`195:15`/`195:16`). `shield-check`는 brand-guide.md의 "파란 방패+흰 체크" 서술과 달리 실제로는 방패 도형 없이 체크마크(파란 stroke)만 존재함을 스크린샷으로 재확인, 형태를 임의로 보완하지 않고 관찰값 그대로 정리.
- `docs/design/mercari/graphic-assets.md` 신규 작성(이 프로젝트는 연락처 앱과 다른 fileKey라 서브폴더 분리). **전달 대상**: design-systems(3종 COMPONENT 승격 + CTA 컴포넌트 비활성 chevron 색상 하드코딩 오류 별도 확인 + B_03/A_04 화면의 raw CTA Button↔컴포넌트 인스턴스 불일치 참고), design-pl/brand-designer(shield-check 실물↔brand-guide 서술 불일치 참고 보고).

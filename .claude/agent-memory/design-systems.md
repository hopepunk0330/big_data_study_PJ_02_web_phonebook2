# design-systems 메모리

이 파일은 design-systems의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **State Ledger(토큰/컴포넌트/아이콘의 현재 확정 상태) 자체는 여기 없습니다 — `docs/design/design-system.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-12 — 파일럿 피드백 수정: elevation 토큰 신설 + Alert 바인딩 + Button 전 variant WCAG 대비 교정
- **오발동 방지**: 새 팔레트/톤을 정하는 컨셉 라운드가 아님(Warm Ledger 이미 확정) — 시안 3개 없이 바로 최종형으로 진행.
- 사전 확인: 기억(메모리)을 그대로 믿지 않고 Alert(`104:2`)/Button(`97:8`) 실제 노드를 `get_design_context` + `use_figma` 읽기 전용 스크립트로 직접 재열람 → Button Primary+Default 2개 variant가 `component/button-text-disabled`에 잘못 바인딩된 실측 버그 확인(대비 1.22:1).
- Phase 1: Elevation 토큰 3계층 신설. Primitive는 기존 Primitives 컬렉션에 shadow color 2개 추가(ink alpha 8%/16%, scopes=[] 기존 컨벤션 유지) + 새 "Elevation" 컬렉션에 blur/offset/spread FLOAT 5개(scope EFFECT_FLOAT). Semantic은 Effect Style 2개(`Elevation/Raised`/`Elevation/Overlay`)로 구현 — Figma는 그림자를 변수로 직접 저장할 수 없어 `setBoundVariableForEffect`로 Effect Style의 color/radius/offsetY/spread 각각을 primitive에 바인딩(alias 원칙 유지). FOUNDATIONS에 "Elevation" 문서 페이지 신설(Colors/Typography/Spacing과 동급), 스크린샷으로 raised/overlay 그림자 시각 차이 확인.
- Phase 2: Alert(`104:6`/`104:14`) 최상위 컴포넌트 노드에 `Elevation/Raised` 바인딩. accent-bar/icon/Message 구조는 그대로. Instance Preview Row로 전/후 확인 — 카드 하단에 은은한 그림자가 생겨 배경과 분리됨.
- Phase 3: Button 8개 variant 전수 대비비 실측(WCAG AA 4.5:1 기준). Primary+Text/IconText+Default 2개만 FAIL(1.22:1, gray/400 텍스트 오바인딩) → `color/text-primary`로 재바인딩해 5.31:1 PASS. 나머지 4개 Default variant는 원래 PASS(5.31~16.57:1), Disabled 4개는 1.93:1로 원래도 미달이지만 WCAG 예외 대상이자 이번 라운드 범위 밖이라 수정하지 않고 언급만 함. 신규 텍스트 토큰은 만들지 않고 기존 semantic(`color/text-primary`) 재사용.
- 범위 확인: `get_metadata`로 전체 페이지 재조회, off-limits 목록(Colors/Typography/Spacing/Icons 페이지, Input/Select/Badge/Table Row/Sidebar Nav Item/Avatar 컴포넌트) 변경 없음 확인. 페이지 순서 재정렬(Elevation을 Spacing 뒤/Icons 앞으로 insertChild) 후 전체 순서 재확인.
- 다음 단계(이 에이전트 범위 아님): ui-designer가 파일럿 3개 화면(Login/Contacts With Data/Contacts Empty — 이미 존재 확인됨)에서 Alert/Button 인스턴스를 이 수정된 컴포넌트로 재조립.

### 2026-07-12 — 토큰·Icons·컴포넌트 8개 정식 생성 (Concept B "Warm Ledger" 시스템화)
- brand-designer/graphic-designer 확정값을 Brand Guide(`52:3`)·Graphic Assets(`90:2`) 원본에서 직접 재확인 후 그대로 사용, 임의 조정 없음.
- docs/planning 화면정의서 원문 직접 대조: SCR-002(카테고리 드롭다운, "잘못된 입력이 불가능한 UI"), SCR-900(401=세션만료, 404/409/422=detail 그대로, 성공=초록 1~2초, 422 배열은 첫 msg만), 이중 제출 방지(요청 중 버튼 비활성화), 모든 입력창 placeholder 필수 — 문서 문구 그대로 반영.
- Phase 1 토큰: Primitives 10 / Semantic Colors 8(전부 alias) / Spacing+Radius 10 / Text Style 4. 전부 scope 명시(ALL_SCOPES 없음), WEB code syntax 전부 설정.
- WCAG AA 검증: text-primary/text-secondary on surface 16.6:1/6.1:1 PASS. success(teal)/error(coral) on white은 3.0~3.1:1로 본문 텍스트 기준 미달 → "브랜드색 배경엔 항상 ink 텍스트"(5.3~11:1 PASS) 규칙 채택, success/error는 아이콘·보더·배경 전용으로 한정.
- Phase 1.5: Icons 페이지에 8개 전부 `createComponentFromNode`로 원본 그대로 등록(재작도 없음), 스크린샷 비교로 원본과 동일 확인.
- Phase 3: Button/Input/Select/Badge/Table Row/Sidebar Nav Item/Alert/Avatar 8개 컴포넌트를 각 전용 페이지에 생성, Component Tokens 10개 신설(필요한 만큼만), Icons 세트 인스턴스로 바인딩(Add/Edit/Delete/Alert/User).
- 버그 2건 처리: (1) ComponentSet 첫 자식의 variable-bound fill이 스크린샷에서 검게 렌더링 — 인스턴스는 정상 렌더링됨을 확인해 MCP 렌더링 한계로 판단, 문제 노드를 정상 clone으로 교체 + 이후 모든 컴포넌트에 Instance Preview Row 추가. (2) 여러 페이지 insertChild 이후 전체 페이지 순서가 뒤섞임 — 8개 컴포넌트 완료 후 전체 페이지 순서를 문서 규칙대로 한 번에 강제 재정렬.

# graphic-designer 메모리

이 파일은 graphic-designer의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **그린 그래픽 목록(현재 확정 상태)은 여기 없습니다 — `docs/design/graphic-assets.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-12 — 기능 아이콘 8종 제작 (Search/Add/Edit/Delete/Category/Logout/Alert/User)
- design-pl 브리프: Concept B "Warm Ledger" 브랜드 1차 확정 + B-2 레이아웃 2차 확정 완료 상태, 이번은 컨셉 라운드 아님 — 최종형 8종 바로 제작 지시.
- 시작 전 Brand Guide `52:3`/`52:10`을 스크린샷+design_context로 실물 재확인(기억 재구성 금지 규칙 준수) — hex 3개와 아웃라인 두께 문구가 브리프 참고값과 정확히 일치함을 확인.
- "Graphic Assets" 페이지 신규 생성(`90:2`), figma.root.children 순서를 Brand Guide 바로 다음(index+1)으로 삽입해 문서 규칙 순서 준수.
- 8개 아이콘을 단계적으로 제작(스켈레톤 1콜 → 1~4번 1콜 → 5~8번 1콜)하며 매 단계 `node.screenshot({scale:12})`로 확대 검증.
- Edit(연필) 아이콘: 처음엔 rectangle+triangle을 rotation/union으로 조합했으나 결과가 화살표 모양처럼 뭉개짐 → 5점 벡터 패스(`M 0 0 L 12 0 L 17 2.2 L 12 4.4 L 0 4.4 Z`)로 재작업해 명확한 연필 실루엣 확보. 회전 후 프레임 밖으로 살짝 클리핑되는 문제는 `absoluteBoundingBox` 측정 후 x/y를 보정해 해결(단순 center-pivot 가정이 틀렸음을 실측으로 확인).
- 최종 8개를 한 화면에 스크린샷 비교해 아웃라인 두께/그리드/채색 규칙 일관성 확인 완료.
- 다음 단계(이 에이전트 범위 아님): design-systems가 이 8개 원화를 "Icons" 페이지에 정식 컴포넌트(variant 포함)로 등록.

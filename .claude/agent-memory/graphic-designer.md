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

### 2026-07-13 — 신규 Pixel 아이콘 9종 카탈로그화 + docs/planning 갭 감사(누락 없음)
- 작업 A: design-systems가 확정 프레임에서 clone해 "Icons" 페이지(`96:7`)에 이미 등록해둔 `Pixel/Star·Search·Plus·Logout·Edit·Delete·Close·Warning·NoResult` 9종을 새로 그리지 않고 관찰만 해서 카탈로그화. get_design_context + use_figma(읽기전용 fills 조회)로 정확한 hex/사이즈/블록 구성 확인. 이 9종은 기존 8종(Icon/*, 24px Basic/Visual strokeWeight 트랙)과 다른 별개 트랙 — Brand Guide 9번의 "마이크로 픽셀 아이콘"(8~15px, 블록 조합 실루엣) 계층. Pixel/Close만 유일하게 블록 조합이 아니라 2px stroke 벡터로 구성된 예외, Pixel/Star는 컴포넌트 설명(흰색)과 실제 마스터 fill(잉크 `#1a1a1a`)이 불일치 — 둘 다 design-systems 참고용으로만 기록, 임의로 고치지 않음.
- 작업 B: docs/planning FR-01~13 전체를 확정 8개 프레임(read-only) + 17종 아이콘과 대조 — 새로 그릴 아이콘 없음("누락 없음"). 다만 확정 login 프레임(`247:6666`)에 이미 그려져 있는 `PixelEye`(비밀번호 표시/숨김, `247:6814`)가 9종 추출 라운드에서 누락된 것을 발견 — docs/planning FR에 없는 기능이라 이번 갭 감사 대상은 아니지만, design-systems가 다른 9종과 같은 방식(clone)으로 마저 추출·등록하도록 design-pl 경유 전달 필요(graphic-designer가 새로 그리면 확정 프레임 원본과 어긋날 위험이 있어 직접 그리지 않음).
- `docs/design/graphic-assets.md`에 두 섹션(Pixel 9종 카탈로그, 갭 감사 결과) 추가(기존 8종 섹션은 덮어쓰지 않음).

### 2026-07-14 — "Graphic Assets" 페이지 사용자 삭제 반영, 문서 동기화 (그리기 작업 아님)
- 배경: 사용자가 Figma에서 "Graphic Assets" 페이지(`90:2`)를 직접 삭제("레거시 아이콘과 겹쳐서 지웠다")했다고 알려와, `docs/design/graphic-assets.md` / `docs/design/design-system.md`를 실제 Figma 상태와 재대조하라는 지시.
- `use_figma`로 전체 페이지 목록 재조회 → `90:2` 완전히 없음(21개 페이지 중)을 확인. "Icons" 페이지(`96:7`)는 그대로(Icon/* 8종 + Pixel/* 10종, get_metadata 결과 문서와 정확히 일치).
- Icon/* 8종의 strokeWeight를 use_figma로 직접 재실측 → 전부 3px 균일. 즉 이전에 문서에 기록돼 있던 "Basic(1.5px)/Visual(3px) 두 트랙 분리" 작업은 등록 컴포넌트에는 한 번도 반영되지 않은 채(design-systems "재바인딩 권고" 대기 상태) 원화(`90:2`)만 삭제되어 사라짐 — 복원하지 않고 그 기록을 문서에서 전부 제거, 대신 현재 실존하는 8종(균일 3px)의 구성/색상표로 대체.
- `docs/design/graphic-assets.md` 전면 재작성(Pixel 10종 섹션·갭 감사 섹션은 실제와 일치해 내용 유지, 표현만 트랙 분리 언급 제거), `docs/design/design-system.md`는 4절에 재확인 한 줄 추가 + 8절 레거시 페이지 순서 표에서 `90:2` 행 제거·삭제 사실 각주 추가(그 외 불변).
- 전달 대상: design-systems — 기존에 남아 있던 "Icon/Search·Edit·Logout 재바인딩 필요" 권고는 근거 원화가 사라졌으므로 진행하지 않음(신규 작업 없음, 후속 트랙 분리가 필요하면 design-pl이 새 라운드로 재요청해야 함).

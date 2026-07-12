# Graphic Assets — 확정 아이콘/오브제 인벤토리

이 문서는 graphic-designer가 그린 아이콘/오브제의 **현재 확정된** 목록이다. Figma "Graphic Assets" 페이지(비주얼 원본)의 텍스트 미러이며, design-systems(등록)·ui-designer(조립)·motion-designer(애니메이션화)가 참조하는 소스 오브 트루스다. graphic-designer가 새로 그리거나 수정할 때마다 이 파일을 **덮어써서** 최신 상태로 유지한다(로그가 아니다).

## 상태: "Graphic Assets" 페이지에 기능 아이콘 8종 완성 (variant 없음, 단일 기본형)

fileKey `zgGlMBwFglaDlaeyP4CkgR`, "Graphic Assets" 페이지 id `90:2` (Brand Guide `52:2` 바로 다음, Foundations 앞).

8개 아이콘 전부 24x24px 프레임, 이름 규칙 `"{기능명 영문} — Icon"`:

| 기능 | frameId | 구성 |
|---|---|---|
| Search | `91:4` | 렌즈(ellipse) + 회전된 손잡이(subFrame, rotation 45) |
| Add | `91:6` | 둥근 사각 배지 + +기호(bar 2개) |
| Edit | `91:8` | 연필(vector path 5-point, rotation -45) |
| Delete | `91:10` | 뚜껑+손잡이+몸통(rectangle 3개) |
| Category | `91:12` | 폴더 몸통 + 탭(rectangle 2개, 탭은 위쪽 코너만 radius) |
| Logout | `91:14` | 문(rectangle) + 화살표(shaft rectangle + vector triangle head) |
| Alert | `91:16` | 원(ellipse, Accent 앰버 fill) + 느낌표(bar+dot, ink) |
| User | `91:18` | 머리(ellipse) + 어깨(큰 ellipse, 프레임 clipsContent로 하단 크롭) |

**스타일 규칙** (8개 전체 동일 적용): 잉크 아웃라인 strokeWeight 3, strokeAlign CENTER, 색 `#1C1F21`(Brand Guide 본문 텍스트 잉크색과 동일) / 주 평면 채색 Primary 틸 `#17A398` / Alert만 예외로 Accent 앰버 `#FFCB47` 사용(Brand Guide "강조색 사용비율 10% — 알림" 근거) / 디테일 마크(플러스바, 연필심 경계, 화살표, 느낌표)는 잉크 flat fill(스트로크 없음).

**값 출처**: `docs/design/brand-guide.md`(색상 hex, Illustration Direction) — 임의 근사치 없음.

**범위 외**: 마스코트/장식 오브제/빈 상태 그래픽/variant/애니메이션 레이어 분리는 아직 미제작(요청 범위 아님, 빈 상태는 ui-designer가 로고 심볼 재사용).

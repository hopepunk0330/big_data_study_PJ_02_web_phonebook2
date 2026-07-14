# Graphic Assets — 확정 아이콘/오브제 인벤토리

이 문서는 graphic-designer가 그린 아이콘/오브제의 **현재 확정된** 목록이다. Figma "Icons" 페이지(`96:7`, 정식 등록 컴포넌트)를 실측해 기록한 텍스트 미러이며, design-systems(등록)·ui-designer(조립)·motion-designer(애니메이션화)가 참조하는 소스 오브 트루스다. graphic-designer가 새로 그리거나 수정할 때마다 이 파일을 **덮어써서** 최신 상태로 유지한다(로그가 아니다).

## 상태: "Graphic Assets" 페이지(`90:2`) 사용자 삭제됨 — 문서 동기화 (2026-07-14)

사용자가 Figma에서 "Graphic Assets" 페이지(id `90:2`)를 직접 삭제했다("그래픽 에셋은 완전사용 안하고 이전 레거시 아이콘과 겹쳐서 내가 지웠어"). `use_figma`로 전체 페이지 목록을 재조회한 결과 `90:2`는 더 이상 파일에 존재하지 않는다(전체 21개 페이지 중 없음, fileKey `zgGlMBwFglaDlaeyP4CkgR`).

이 페이지 안에서만 존재했던 **"기능 아이콘 8종 — Basic(1.5px)/Visual(3px) 두 트랙 분리"** 원화 및 그 기록(트랙 구분표, 재분류 근거, "실제 벡터가 바뀐 아이콘" 표, design-systems 재바인딩 권고)은 이 문서에서 함께 제거한다(사용자가 이미 지운 원화를 복원하지 않는다). `use_figma`로 "Icons" 페이지(`96:7`)의 실제 등록 컴포넌트 8종(`Icon/Search`~`Icon/User`)을 다시 실측해 확인한 결과, 이 트랙 분리는 등록 컴포넌트에는 한 번도 반영된 적이 없다 — 8종 전부 원래 그대로 **strokeWeight 3px 균일**이다(당시 이 문서는 "재바인딩 필요"라는 권고만 남긴 상태였고, design-systems가 실제로 반영하기 전에 원화 자체가 삭제됨). 따라서 그 권고도 함께 폐기한다. **design-systems는 이 재바인딩을 진행하지 않는다.**

### 현재 실존하는 기능 아이콘 8종 (`Icon/*`, Icons 페이지 `96:7`, 변경 없음)

| 이름 | nodeId | 사이즈 | strokeWeight | 구성 |
|---|---|---|---|---|
| Icon/Search | `96:12` | 24×24 | 3px | 렌즈(ellipse) + 회전된 손잡이(subFrame, rotation 45) |
| Icon/Add | `96:17` | 24×24 | 3px | 둥근 사각 배지 + +기호(bar 2개) |
| Icon/Edit | `96:22` | 24×24 | 3px | 연필(vector path 5-point, rotation -45) |
| Icon/Delete | `96:27` | 24×24 | 3px | 뚜껑+손잡이+몸통(rectangle 3개) |
| Icon/Category | `96:31` | 24×24 | 3px | 폴더 몸통 + 탭(rectangle 2개, 탭은 위쪽 코너만 radius) |
| Icon/Logout | `96:36` | 24×24 | 3px | 문(rectangle) + 화살표(shaft rectangle + vector triangle head) |
| Icon/Alert | `96:41` | 24×24 | 3px | 원(ellipse, Accent 앰버 fill) + 느낌표(bar+dot, ink) |
| Icon/User | `96:45` | 24×24 | 3px | 머리(ellipse) + 어깨(큰 ellipse, 프레임 clipsContent로 하단 크롭) |

**색상 규칙**: 색 `#1C1F21`(잉크) / 주 평면 채색 Primary 틸 `#17A398` / Alert만 예외로 Accent 앰버 `#FFCB47` 사용.

**범위 외**: Basic/Visual 두께 트랙 분리는 원화가 삭제되어 더 이상 진행하지 않는다. 재도입이 필요하면 design-pl 판단 하에 새 라운드로 다시 요청해야 한다. 마스코트/장식 오브제/빈 상태 그래픽/variant/애니메이션 레이어 분리는 아직 미제작(요청 범위 아님, 빈 상태는 ui-designer가 로고 심볼 재사용).

**값 출처**: `docs/design/brand-guide.md`(색상 hex, Illustration Direction) — 임의 근사치 없음.

## 상태: Pixel 마이크로 아이콘 10종 — design-systems 등록 카탈로그화 (2026-07-13 / 2026-07-14 갱신, 변경 없음)

design-systems가 사용자 확정 8개 프레임("확정 디자인 - 절대 원본 건들지 말것-", 부모 섹션 `248:11689`)에서 clone해 "Icons" 페이지(`96:7`, y=2000 클러스터)에 이미 정식 컴포넌트로 등록까지 마친 아이콘을 `get_screenshot`/`get_design_context`/`use_figma`(읽기 전용 fills 조회)로 관찰해 카탈로그화했다 — **graphic-designer가 새로 그린 게 아니라 문서화 작업**이다. 최초 라운드(2026-07-13)에서 9종(`Pixel/Star`, `Pixel/Search`, `Pixel/Plus`, `Pixel/Logout`, `Pixel/Edit`, `Pixel/Delete`, `Pixel/Close`, `Pixel/Warning`, `Pixel/NoResult`)을 등록했고, 아래 "누락 아이콘 발견" 절에서 보고된 `PixelEye`를 design-systems가 마저 추출·등록해 **2026-07-14 기준 총 10종**이 됐다(`Pixel/Eye` 추가). 2026-07-14 재조회로 이 10종 전부 Icons 페이지에 그대로 실존함을 재확인했다(변경 없음).

**이 10종은 위 8종(Icon/*, 24px 표준 플랫 트랙, strokeWeight 3px 균일)과는 별개의 트랙이다.** Brand Guide 9번("아이콘·일러스트레이션 방향")에 정의된 **"마이크로 픽셀 아이콘"** 계층(8~15px, `Pixel*`/`Px*` 네이밍, 8비트 픽셀아트, 단색 실루엣, 안티앨리어싱 없는 각진 형태)에 속한다. strokeWeight 대비 개념이 아니라 "작은 정사각형 vector 블록 여러 개를 이어붙인 단색 실루엣"이 구성 원리이므로, 8종의 균일 3px 스트로크 구성과 나란히 비교할 수 없다 — 별도 표로 기록한다.

### Pixel/* 10종 상세

| 이름 | nodeId | 사이즈 | 색상 | 구성 | 용도(컴포넌트 설명 근거) |
|---|---|---|---|---|---|
| Pixel/Star | `255:11` | 12×12 | 잉크 `#1a1a1a` (⚠ 아래 참고) | 8개 사각 vector 블록 | 로고 심볼(코랄 원) 내부 별, `PxStar` 원본 |
| Pixel/Search | `255:26` | 15×15 | Primary 틸 `#17a398` | 13개 블록, 돋보기 실루엣 | 검색 입력창 leading icon, `PxSearch` 원본 |
| Pixel/Plus | `255:30` | 9×9 | 잉크 `#1a1a1a` | 2개 블록(세로 바 + 가로 바) | NeoBtn 추가 버튼 아이콘, `PxPlus` 원본. login 화면 "회원가입" 버튼의 코랄 원형 배지 안에도 흰색 오버라이드로 재사용됨(확정 프레임 관찰) |
| Pixel/Logout | `255:43` | 12×12 | 흰색 `#ffffff` | 11개 블록, 문+화살표 실루엣 | 헤더 로그아웃 NeoBtn 아이콘(틸 배경 위 흰색), `PxLogout` 원본 |
| Pixel/Edit | `255:62` | 14×14 | 잉크 `#1c1f21` | 17개 블록, 대각선 연필 패턴 | 카테고리 관리 RowActionButton(Neutral), `PixelPencil` 원본 |
| Pixel/Delete | `255:104` | 14×14 | 잉크 `#1c1f21` | Group 안 39개 블록, 휴지통 격자 패턴 | 카테고리 관리 RowActionButton(Danger), `PixelTrash` 원본 |
| Pixel/Close | `255:107` | 10×10 | 잉크 `#1a1a1a`, 스트로크 2px (⚠ 구성 예외) | 단일 vector, 8×8 X자, 채움 없이 스트로크만 | 편집/삭제 모달 우상단 닫기(X) 버튼 |
| Pixel/Warning | `255:120` | 16×16 | Secondary 코랄 `#ff5a76`(9블록, 원형 실루엣) + 흰색(2블록, 느낌표) | 11개 블록 | 삭제 확인 모달 경고 박스 전용 — Icon/Alert(24px, Accent 앰버)와 달리 **코랄**을 쓴다. Brand Guide 5번의 "삭제 경고 박스 보더 `#ff5a76`"와 색이 일치하는 의도된 구분(경고 색 ≠ 성공/에러 토스트 앰버) |
| Pixel/NoResult | `255:149` | 40×44 | Primary 틸(21블록) + Secondary 코랄(6블록) 2색 | 27개 블록, 깨진/기울어진 돋보기 실루엣 | `main-검색없음`(빈 검색결과) empty state 전용 — 신규 마스코트가 아니라 기능 아이콘 언어의 확장 |
| Pixel/Eye | `281:405`(등록 컴포넌트, 원본은 확정 login 프레임의 `247:6814`) | 14×10 | 잉크 `#1a1a1a` | 6개 블록(중앙 가로 바 1개 + 상단 코너 블록 3개 + 하단 코너 블록 2개), 눈 실루엣 | login 비밀번호 입력창 표시/숨김 토글 아이콘, `PixelEye` 원본. **2026-07-14 design-systems가 확정 login 프레임(`247:6666`)에서 비파괴적으로 clone해 마저 등록**(최초 9종 추출 라운드에서 누락됐던 것을 보완, 아래 "누락 아이콘 발견" 절 참고) — 원본 `247:6814`는 무수정으로 그대로 존재 |

**⚠ 관찰된 특이사항** (design-systems 참고용 — graphic-designer가 임의로 고치지 않고 관찰 그대로만 기록):
- **Pixel/Star**: 컴포넌트 설명 텍스트는 "흰색(로고 심볼 내부 별)"이라고 적혀 있으나, 실제 마스터 컴포넌트의 vector fill은 잉크 `#1a1a1a`다. 로고 심볼(코랄 원) 안에 배치될 때만 흰색으로 인스턴스 오버라이드되는 것으로 추정되나, 마스터 자체의 기본색이 설명과 다르다 — design-systems가 인스턴스 오버라이드 실태를 확인할 필요가 있다. **(2026-07-14 정정 완료)** design-systems가 `docs/design/design-system.md` 0-2절에 따라 fill 값은 그대로 두고 컴포넌트 description 텍스트만 실측값(잉크 #1a1a1a)에 맞게 정정했다.
- **Pixel/Close**: 다른 8개(순수 사각 블록 채움 실루엣 방식)와 달리, 단일 vector에 stroke(2px, 채움 없음)로 구성된 유일한 아이콘이다. 시각적 톤(픽셀아트)은 동일하게 유지되지만, 이 세트를 향후 확장할 때 두 가지 구성 방식(블록 조합 vs 스트로크 벡터)이 섞여 있다는 점을 참고할 것.

## 상태: docs/planning 아이콘 갭 감사 — 누락 없음, 발견사항 1건 처리 완료 (2026-07-13 / 2026-07-14 갱신, 변경 없음)

docs/planning(`01_구현요구사항`, `02_화면정의서`, `03_기능정의서`)의 FR-01~FR-13 전체를 확정 8개 프레임(read-only로만 재확인, 내용/이름 변경 없음)과 기존 18종 아이콘(Icon/* 8종 + Pixel/* 10종)에 대조했다.

**결론: 새로 그릴 아이콘 없음.** FR-01~13이 요구하는 액션(회원가입/로그인/로그아웃/연락처 CRUD/검색/카테고리 CRUD/사용 중 카테고리 삭제 거부/화면 제공)에 필요한 아이콘은 18종 안에서 전부 커버된다:

| 기능(FR) | 커버 아이콘 |
|---|---|
| 검색(FR-06) | `Icon/Search`, `Pixel/Search` |
| 연락처/카테고리 추가(FR-05, FR-10) | `Icon/Add`, `Pixel/Plus` |
| 연락처/카테고리 수정(FR-07, FR-11) | `Icon/Edit`, `Pixel/Edit` |
| 연락처/카테고리 삭제(FR-08, FR-12) | `Icon/Delete`, `Pixel/Delete` |
| 카테고리 표시 | `Icon/Category` |
| 로그아웃(FR-03) | `Icon/Logout`, `Pixel/Logout` |
| 사용 중 카테고리 삭제 거부(409), 성공/에러 알림 | `Icon/Alert`, `Pixel/Warning` |
| 검색 결과 0건(FR-06) | `Pixel/NoResult` |
| 모달 닫기 | `Pixel/Close` |

회원가입(FR-01)·로그인(FR-02)·내 정보 확인(FR-04)·화면 제공(FR-13)은 docs/planning 어디에도 전용 기능 아이콘이 명시되어 있지 않다(폼 입력 + 버튼 텍스트로 충분한 것으로 확정 프레임에도 반영됨).

**발견사항 처리 완료 (2026-07-14)**: 확정 login 프레임(`247:6666`)을 갭 감사차 다시 확인하는 과정에서, 비밀번호 입력창 안에 `PixelEye`(nodeId `247:6814`, 14×10)라는 비밀번호 표시/숨김 토글 아이콘이 이미 그려져 있는 것을 발견했었다. 이 아이콘은 **docs/planning FR 목록에 없는 기능**(비밀번호 show/hide는 어떤 FR에도 명시되지 않음)이라 이 갭 감사의 "새로 그려야 할 누락"에는 해당하지 않았다. 다만 이미 확정 프레임에 실존하는 아이콘인데 최초 9종 추출 라운드에서 함께 등록되지 않고 누락되어 있었고, **design-systems가 확정 프레임의 원본 벡터를 그대로 clone해 `Pixel/Eye`(등록 컴포넌트 `281:405`)로 마저 추출·등록 완료**했다(위 "Pixel 마이크로 아이콘" 절 참고). 원본 `247:6814`는 무수정으로 그대로 존재한다.

참고로 로그인 버튼 안의 화살표형 "Icon"(nodeId `247:6829`, 14×14)은 재사용 가능한 이름으로 명명되지 않은 장식용 화살표라 이번 보고에서는 관찰만 남기고 조치 대상에서 제외했다(변경 없음, 계속 조치 대상 아님).

**값 출처**: `docs/planning/01_연락처관리_웹서비스_구현요구사항_v1.0.pdf`, `02_...화면정의서...pdf`, `03_...기능정의서...pdf`(FR 목록) + 확정 8개 프레임 직접 재관찰(get_metadata/get_design_context, 읽기 전용).

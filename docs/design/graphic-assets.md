# Graphic Assets — 확정 아이콘/오브제 인벤토리

이 문서는 graphic-designer가 그린 아이콘/오브제의 **현재 확정된** 목록이다. Figma "Icons" 페이지(`96:7`, 정식 등록 컴포넌트)를 실측해 기록한 텍스트 미러이며, design-systems(등록)·ui-designer(조립)·motion-designer(애니메이션화)가 참조하는 소스 오브 트루스다. graphic-designer가 새로 그리거나 수정할 때마다 이 파일을 **덮어써서** 최신 상태로 유지한다(로그가 아니다).

## 상태: "Graphic Assets" 페이지(`90:2`) 사용자 삭제됨 — 문서 동기화 (2026-07-14)

사용자가 Figma에서 "Graphic Assets" 페이지(id `90:2`)를 직접 삭제했다("그래픽 에셋은 완전사용 안하고 이전 레거시 아이콘과 겹쳐서 내가 지웠어"). `use_figma`로 전체 페이지 목록을 재조회한 결과 `90:2`는 더 이상 파일에 존재하지 않는다(전체 21개 페이지 중 없음, fileKey `zgGlMBwFglaDlaeyP4CkgR`).

이 페이지 안에서만 존재했던 **"기능 아이콘 8종 — Basic(1.5px)/Visual(3px) 두 트랙 분리"** 원화 및 그 기록(트랙 구분표, 재분류 근거, "실제 벡터가 바뀐 아이콘" 표, design-systems 재바인딩 권고)은 이 문서에서 함께 제거한다(사용자가 이미 지운 원화를 복원하지 않는다). `use_figma`로 "Icons" 페이지(`96:7`)의 실제 등록 컴포넌트 8종(`Icon/Search`~`Icon/User`)을 다시 실측해 확인한 결과, 이 트랙 분리는 등록 컴포넌트에는 한 번도 반영된 적이 없다 — 8종 전부 원래 그대로 **strokeWeight 3px 균일**이다(당시 이 문서는 "재바인딩 필요"라는 권고만 남긴 상태였고, design-systems가 실제로 반영하기 전에 원화 자체가 삭제됨). 따라서 그 권고도 함께 폐기한다. **design-systems는 이 재바인딩을 진행하지 않는다.**

**주의(2026-07-14 이후 예외)**: 이 페이지가 삭제된 상태이므로, 아래 "Pixel/EyeOff" 항목처럼 새 원화를 그려야 하는 경우 정상 파이프라인(원화 → Graphic Assets 페이지 → design-systems 등록)의 스테이징 단계를 생략하고 "Icons" 페이지(`96:7`)에 raw 벡터로 바로 배치한다(design-pl 승인, 근거는 design-prompter 브리프에 명시).

**⚠ 2026-07-17 갱신**: 위 "8종 전부 strokeWeight 3px 균일" 기록은 이후 두 라운드(같은 날짜, 순서대로 진행)를 거쳐 갱신됐다 — ① "Icons 페이지 색상 바인딩 전수 감사" 절(값 재해석 라운드, 색상만), ② 맨 아래 "Icon/* 8종 Basic/Visual 트랙 재판정" 절(트랙 재판정 + Basic 6종 fill 제거·2px 재드로잉 지시). 이 절 자체의 서술("트랙 분리 원화가 삭제되어 진행 안 함")은 역사적 기록으로 그대로 남겨두되, 8종의 균일 3px 상태는 더 이상 최신이 아니다 — 최신 상태는 맨 아래 절을 따른다.

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

**⚠ 2026-07-17 위 표는 strokeWeight 열이 더 이상 최신이 아니다** — Search/Add/Edit/Delete/Logout/User 6종은 맨 아래 절에서 Basic 트랙(2px, fill 제거)으로 재판정됐다. Category/Alert 2종만 3px+fill 유지(Visual 트랙). 실행 전 상태이므로 이 표 자체는 "등록 당시 구조" 기록으로 보존한다.

**색상 규칙**: 색 `#1C1F21`(잉크) / 주 평면 채색 Primary 틸 `#17A398` / Alert만 예외로 Accent 앰버 `#FFCB47` 사용. **⚠ 2026-07-17 갱신**: 이 색상 규칙은 구 세대(삭제된 `248:11689`) 기준 원문 기록이다. 실제 라이브 값은 아래 "Icons 페이지 색상 감사" 절 참고 — Icon/Alert의 앰버는 이미 `#FFCE2C`(`color/bg-cta-amber`)로 리바인딩되어 있고, `#1C1F21` 잉크값은 프로젝트 전체 기준 ink/900 정정(`#1a1a1a`) 이전의 구값으로 재해석이 필요하다고 판단했다(아래 절 참고). **⚠ 2026-07-17 재갱신**: 위 "주 평면 채색 Primary 틸"이라는 역할 명칭 표현도 이제 최신이 아니다 — `design-system.md` 33절("Primary/Secondary/Accent 역할 재평가", 확정 프레임 `501:2505` 8개를 fill+stroke 면적까지 실측)에서 브랜드 컬러 위계가 재확정됐다: **Primary는 스카이블루** `color/sky/500`(신규 편입, 사이드바 전체 배경/Join·login·login알림창 100% 배경/아바타 원 배경/인증 카드 하단 스트립), **Secondary는 코랄**(변경 없음), **Accent는 앰버**(변경 없음)이며, **틸은 Primary 역할에서 완전히 제외되고 "카테고리 식별색(narrow)"으로 좁게 재정의**됐다(CatBadge 회사 보더/닷 + row 수정 액션 아웃라인만 남음). 이 결론은 `docs/design/brand-guide.md`·`docs/design/confirmed/user-confirmed-final-design.md`·`docs/design/design-system.md`에 이미 반영됐다. **단, 이 각주는 "틸"이라는 역할 명칭 서술만 정정하는 것이지, 이 문서 안에 이미 실측·기록된 개별 Icon/*·Pixel/* 아이콘의 실제 fill 값이나 A/B 분류 판정(아래 "Icons 페이지 색상 바인딩 전수 감사" 절 이하, 예: "6종은 A(틸 유지)로 분류")을 뒤집는 게 아니다** — "이 아이콘이 틸을 쓴다"는 관찰(아이콘 크래프트 층위)과 "틸이 브랜드 Primary 배경색이다"는 주장(브랜드 역할 층위)은 서로 다른 층위이며, 이번 각주는 후자만 정정한다.

**범위 외**: Basic/Visual 두께 트랙 분리는 원화가 삭제되어 더 이상 진행하지 않는다. 재도입이 필요하면 design-pl 판단 하에 새 라운드로 다시 요청해야 한다. 마스코트/장식 오브제/빈 상태 그래픽/variant/애니메이션 레이어 분리는 아직 미제작(요청 범위 아님, 빈 상태는 ui-designer가 로고 심볼 재사용). **⚠ 2026-07-17 갱신**: "Basic/Visual 트랙 분리는 더 이상 진행하지 않는다"는 위 문장은 이제 사실이 아니다 — 맨 아래 절에서 사용자의 직접 지적(`Icon/User` 관찰)을 계기로 트랙 분리가 다시 진행됐다. 이 문단은 당시(2026-07-14) 시점 기록으로 보존한다.

**값 출처**: `docs/design/brand-guide.md`(색상 hex, Illustration Direction) — 임의 근사치 없음.

## 상태: Pixel 마이크로 아이콘 14종 — design-systems 등록 카탈로그화 (2026-07-13 / 2026-07-14 갱신, Pixel/EyeOff 신규 등록 / 2026-07-16 갱신, Pixel/Check 신규 등록)

design-systems가 사용자 확정 8개 프레임("확정 디자인 - 절대 원본 건들지 말것-", 부모 섹션 `248:11689`)에서 clone해 "Icons" 페이지(`96:7`, y=2000 클러스터)에 이미 정식 컴포넌트로 등록까지 마친 아이콘을 `get_screenshot`/`get_design_context`/`use_figma`(읽기 전용 fills 조회)로 관찰해 카탈로그화했다 — **graphic-designer가 새로 그린 게 아니라 문서화 작업**이다. 최초 라운드(2026-07-13)에서 9종(`Pixel/Star`, `Pixel/Search`, `Pixel/Plus`, `Pixel/Logout`, `Pixel/Edit`, `Pixel/Delete`, `Pixel/Close`, `Pixel/Warning`, `Pixel/NoResult`)을 등록했고, 아래 "누락 아이콘 발견" 절에서 보고된 `PixelEye`를 design-systems가 마저 추출·등록해 10종이 됐다(`Pixel/Eye` 추가). 이어서 design-prompter 브리프에 따라 graphic-designer가 그린 `PixelEyeOff`(`414:2`, raw FRAME, Pixel/Eye의 짝)를 design-systems가 이번 라운드에서 `createComponentFromNode`로 `Pixel/EyeOff`(`415:892`)로 정식 등록해 2026-07-14 기준 총 11종이 됐다. **이어서 2026-07-16, Checkbox 체크마크 리토피트 라운드(design-system.md 0-26절)에서 graphic-designer가 그린 `PixelCheck`(`814:2`, raw FRAME)를 design-systems가 `createComponentFromNode`로 `Pixel/Check`(`815:2`)로 정식 등록해 현재 총 12종**이 됐다. **⚠ 2026-07-17 갱신**: 이어서 design-qa HIGH 결함 정정(Button/NeoBtn 아이콘 슬롯 부재) 라운드에서 design-systems가 확정 Join "가입하기"(`501:4855`)/login "로그인"(`501:5103`) 프레임에서 각각 `Pixel/ArrowRight`(`951:2`)/`Pixel/ArrowEnter`(`951:3`)를 clone·등록해 **현재 총 14종**이다. 상세는 아래 표와 `docs/design/design-system.md` 34절 참고.

**이 12종은 위 8종(Icon/*, 24px 표준 플랫 트랙, strokeWeight 3px 균일)과는 별개의 트랙이다.** Brand Guide 9번("아이콘·일러스트레이션 방향")에 정의된 **"마이크로 픽셀 아이콘"** 계층(8~15px, `Pixel*`/`Px*` 네이밍, 8비트 픽셀아트, 단색 실루엣, 안티앨리어싱 없는 각진 형태)에 속한다. strokeWeight 대비 개념이 아니라 "작은 정사각형 vector 블록 여러 개를 이어붙인 단색 실루엣"이 구성 원리이므로, 8종의 균일 3px 스트로크 구성과 나란히 비교할 수 없다 — 별도 표로 기록한다.

### Pixel/* 14종 상세

| 이름 | nodeId | 사이즈 | 색상 | 구성 | 용도(컴포넌트 설명 근거) |
|---|---|---|---|---|---|
| Pixel/Star | `255:11` | 12×12 | 잉크 `#1a1a1a` (⚠ 아래 참고) | 8개 사각 vector 블록 | 로고 심볼(코랄 원) 내부 별, `PxStar` 원본 |
| Pixel/Search | `255:26` | 15×15 | ~~Primary 틸 `#17a398`~~ → **스카이블루 `#1395e6` 리바인딩 승인**(아래 "Pixel/Search 색상 검증" 절 참고, 2026-07-17) | 13개 블록, 돋보기 실루엣 | 검색 입력창 leading icon, `PxSearch` 원본 |
| Pixel/Plus | `255:30` | 9×9 | 잉크 `#1a1a1a` | 2개 블록(세로 바 + 가로 바) | NeoBtn 추가 버튼 아이콘, `PxPlus` 원본. ~~login 화면 "회원가입" 버튼의 코랄 원형 배지 안에도 흰색 오버라이드로 재사용됨(확정 프레임 관찰)~~ **⚠ 2026-07-17 정정(design-system.md 34-3절)**: design-systems가 배지 내부 vector(`501:5140`)를 `use_figma`로 재실측한 결과 실제 fill은 **잉크 `#1a1a1a`**였다 — "흰색 오버라이드" 기록은 부정확했다. main 헤더 "로그아웃"(`Pixel/Logout`)·검색행/사이드바 "추가"(`Pixel/Plus`) NeoBtn 인스턴스는 실측 결과 흰색이 맞다(배경이 어두운/채도 있는 NeoBtn Ink/Coral/Sky/Navy이기 때문) — 이 정정은 회원가입 배지 1건에만 해당한다 |
| Pixel/Logout | `255:43` | 12×12 | 흰색 `#ffffff` | 11개 블록, 문+화살표 실루엣 | 헤더 로그아웃 NeoBtn 아이콘(틸 배경 위 흰색), `PxLogout` 원본. **⚠ 2026-07-17 갱신**: 헤더 로그아웃 버튼은 이후 `design-system.md` 18절에서 Style=Ink(잉크 배경+흰 텍스트, 틸 아님)로 확정됐다 — "틸 배경 위 흰색"이라는 이 설명은 구 세대 기준이며, 흰색 자체의 값은 여전히 유효하나 의미상 "브랜드색 배경 위 흰 아이콘"이 아니라 "어두운 배경 위 인버스 아이콘"으로 재해석해야 한다(아래 감사 절 참고). |
| Pixel/Edit | `255:62` | 14×14 | 잉크 `#1c1f21` | 17개 블록, 대각선 연필 패턴 | 카테고리 관리 RowActionButton(Neutral), `PixelPencil` 원본 |
| Pixel/Delete | `255:104` | 14×14 | 잉크 `#1c1f21` | Group 안 39개 블록, 휴지통 격자 패턴 | 카테고리 관리 RowActionButton(Danger), `PixelTrash` 원본 |
| Pixel/Close | `255:107` | 10×10 | 잉크 `#1a1a1a`, 스트로크 2px (⚠ 구성 예외) | 단일 vector, 8×8 X자, 채움 없이 스트로크만 | 편집/삭제 모달 우상단 닫기(X) 버튼 |
| Pixel/Warning | `255:120` | 16×16 | Secondary 코랄 `#ff5a76`(9블록, 원형 실루엣) + 흰색(2블록, 느낌표) | 11개 블록 | 삭제 확인 모달 경고 박스 전용 — Icon/Alert(24px, Accent 앰버)와 달리 **코랄**을 쓴다. Brand Guide 5번의 "삭제 경고 박스 보더 `#ff5a76`"와 색이 일치하는 의도된 구분(경고 색 ≠ 성공/에러 토스트 앰버) |
| Pixel/NoResult | `255:149` | 40×44 | ~~Primary 틸(21블록)~~ → **스카이블루(21블록, `color/sky/500` 리바인딩 완료)** + Secondary 코랄(6블록) 2색 | 27개 블록, 깨진/기울어진 돋보기 실루엣 | `main-검색없음`(빈 검색결과) empty state 전용 — 신규 마스코트가 아니라 기능 아이콘 언어의 확장. **2026-07-16 design-systems가 리바인딩**(design-system.md 23절 B) — 이 표는 리바인딩 완료 후 최신 상태 반영 |
| Pixel/Eye | `281:405`(등록 컴포넌트, 원본은 확정 login 프레임의 `247:6814`) | 14×10 | 잉크 `#1a1a1a` | descendant vector **14개**(fill 보유), 눈 실루엣. **⚠ 2026-07-17 재실측 정정**: 2026-07-14 최초 관찰 당시 기록된 "6블록"(중앙 가로 바 1개+상단 코너 3개+하단 코너 2개, 노드 `281:399`~`281:404`)은 그 시점엔 정확했으나, 이후 컴포넌트에 8개 블록(`429:38`/`429:40`/`429:42`/`429:44`/`429:46`/`429:48`/`429:50`/`429:52`, 눈 중앙부 디테일)이 추가돼 현재 라이브 값은 14개다 — 아래 "문서 정합성 정정 2건" 절 참고 | login 비밀번호 입력창 표시/숨김 토글 아이콘, `PixelEye` 원본. **2026-07-14 design-systems가 확정 login 프레임(`247:6666`)에서 비파괴적으로 clone해 마저 등록**(최초 9종 추출 라운드에서 누락됐던 것을 보완, 아래 "누락 아이콘 발견" 절 참고) — 원본 `247:6814`는 무수정으로 그대로 존재 |
| **Pixel/EyeOff**(2026-07-14) | `415:892`(등록 컴포넌트, 원본은 raw FRAME `414:2`) | 14×10 | 잉크 `#1a1a1a` | 3개 블록(중앙 가로 바 1개 `x0,y4,w14,h2` + 하단 코너 블록 2개 `x2,y6`/`x10,y6`, 각 2×2) — Pixel/Eye의 상단 코너 3블록(피크)만 제거한 "닫힌 눈" 실루엣 | login 비밀번호 입력창 표시/숨김 토글 아이콘(숨김 상태), Pixel/Eye의 짝. `PixelEyeOff` 원본. graphic-designer가 그린 raw FRAME(`414:2`, Icons 페이지 `x=1241,y=403`)을 design-systems가 `createComponentFromNode`로 그대로 등록(형태 변형 없음, 자식 3개 RECTANGLE `414:3`/`414:4`/`414:5` ID 그대로 승계) — 형태 선택 근거는 아래 "PixelEyeOff 신규 원화" 절 참고 |
| **Pixel/Check**(2026-07-16) | `815:2`(등록 컴포넌트, 원본은 raw FRAME `814:2`) | 8×7 | 잉크 `#1a1a1a`(마스터 원화 값. **⚠ 2026-07-16 후속 정정**: Checkbox `State=Checked` 인스턴스(`815:3`) 안 실제 렌더링 vector는 이후 `docs/design/design-system.md` 21절에서 `color/text-inverse`(#FFFFFF, 흰색)로 재바인딩됐다 — 아래 용도 칸 참고) | 단일 stroke-vector(자식 VECTOR `814:3`→등록 후 `815:3` 내부 vector, `vectorPaths="M 0 4 L 3 7 L 8 0"`, strokeWeight 3, strokeCap/Join ROUND, fills 없음) | Checkbox `State=Checked` 체크마크 아이콘. `PixelCheck` 원본. graphic-designer가 그린 raw FRAME(`814:2`, Icons 페이지 `x=1361,y=403`)을 design-systems가 `createComponentFromNode`로 그대로 등록(형태 변형 없음) → Checkbox Box(`474:886`) 내부 raw VECTOR(`474:888`)를 이 컴포넌트의 INSTANCE(`815:3`)로 교체(교체 당시 색상은 `color/ink/900` 그대로 무변경이었음) — 상세는 아래 "Pixel/Check 정식 등록 완료" 절 참고. **⚠ 2026-07-16 재정정(21절)**: 이후 Checkbox Box가 이미 `color/sky/500`(스카이블루)으로 확정 디자인과 일치해 있었다는 사실이 확인되며, 체크마크도 `color/text-inverse`(흰색)로 재바인딩됐다 — 마스터 원화(`815:2`) 자체의 기본 색은 잉크로 유지되며, 색상 변경은 Checkbox 인스턴스 쪽 재바인딩으로만 반영됐다. 상세는 `docs/design/design-system.md` 21절 참고 |
| **Pixel/ArrowRight**(2026-07-17) | `951:2`(등록 컴포넌트, 원본은 Join "가입하기" `501:4855`) | 14×14 | 잉크 `#1a1a1a`, stroke weight 1.75 | 2개 vector(수평 shaft `vectorPaths="M 0 0 L 9.5 0"` + chevron `vectorPaths="M 0 0 L 3.5 3.5 L 0 7"`, 둘 다 stroke-only, fills 없음) | Join "가입하기"(`501:4854`)/"로그인으로 돌아가기"(`501:4888`), main-수정 "저장하기"(`501:3627`) 3곳의 leading 화살표 아이콘. 3곳 실측 결과 vectorPaths·색·weight가 hex 단위로 완전히 동일해 하나의 아이콘으로 등록. design-systems가 Join "가입하기" 프레임(`501:4855`)에서 비파괴적으로 clone(원본 무수정) → `createComponentFromNode`로 등록. Button(`259:609`)/NeoBtn(`259:126`) Leading Icon 슬롯의 기본 스왑 아이콘(Button 기본값). 상세는 `docs/design/design-system.md` 34절 참고 |
| **Pixel/ArrowEnter**(2026-07-17) | `951:3`(등록 컴포넌트, 원본은 login "로그인" 버튼 `501:5103`) | 14×14 | 잉크 `#1a1a1a`, stroke weight 1.75 | 3개 vector(우측 rounded bracket — cubic bezier 포함 `vectorPaths="M 0 0 L 2.333... C ... L 0 10.5"` + chevron head `"M 0 5.8333 L 2.9167 2.9167 L 0 0"` + 좌측 shaft `"M 7 0 L 0 0"`, 전부 stroke-only) | login "로그인" 버튼(`501:5102`) 전용 leading 아이콘 — Pixel/ArrowRight(2-vector 단순 화살표)와 실측 결과 형태가 명확히 달라 별도 등록("문/입구로 들어가는 화살표" 형상). design-systems가 login "로그인" 프레임(`501:5103`)에서 비파괴적으로 clone(원본 무수정) → `createComponentFromNode`로 등록. NeoBtn(`259:126`)에는 적용하지 않음(NeoBtn 기본 스왑은 Pixel/Plus) — Button Leading Icon 슬롯의 login 전용 대안 스왑 아이콘. 상세는 `docs/design/design-system.md` 34절 참고 |

**⚠ 관찰된 특이사항** (design-systems 참고용 — graphic-designer가 임의로 고치지 않고 관찰 그대로만 기록):
- **Pixel/Star**: 컴포넌트 설명 텍스트는 "흰색(로고 심볼 내부 별)"이라고 적혀 있으나, 실제 마스터 컴포넌트의 vector fill은 잉크 `#1a1a1a`다. 로고 심볼(코랄 원) 안에 배치될 때만 흰색으로 인스턴스 오버라이드되는 것으로 추정되나, 마스터 자체의 기본색이 설명과 다르다 — design-systems가 인스턴스 오버라이드 실태를 확인할 필요가 있다. **(2026-07-14 정정 완료)** design-systems가 `docs/design/design-system.md` 0-2절에 따라 fill 값은 그대로 두고 컴포넌트 description 텍스트만 실측값(잉크 #1a1a1a)에 맞게 정정했다.
- **Pixel/Close**: 다른 8개(순수 사각 블록 채움 실루엣 방식)와 달리, 단일 vector에 stroke(2px, 채움 없음)로 구성된 유일한 아이콘이다. 시각적 톤(픽셀아트)은 동일하게 유지되지만, 이 세트를 향후 확장할 때 두 가지 구성 방식(블록 조합 vs 스트로크 벡터)이 섞여 있다는 점을 참고할 것.

## 상태: `Pixel/EyeOff` 정식 등록 완료 — Pixel/Eye 짝(눈 숨김) 아이콘 (2026-07-14)

design-prompter 브리프(비밀번호 표시/숨김 토글의 "숨김" 상태 아이콘 부재 갭)에 따라 `Pixel/Eye`(`281:405`)의 짝이 되는 신규 아이콘을 그렸다. Pixel/Eye나 원본 `247:6814`, 다른 확정 Pixel 9종은 전혀 건드리지 않았다(읽기 전용 관찰만).

**관찰(실측, 2026-07-14 당시 기준)**: `Pixel/Eye`(`281:405`)의 실제 벡터 구성을 `use_figma`로 직접 읽어 6블록의 좌표를 확인했다(2px 그리드 기준). **⚠ 2026-07-17 갱신**: 이 6블록 기록은 작성 당시(2026-07-14) 라이브 상태와 정확히 일치했던 값이다 — 아래 6개는 현재도 동일 ID·동일 좌표로 그대로 존재한다. 다만 그 이후 컴포넌트에 8개 블록이 추가되어 현재 `281:405`의 총 자식 수는 14개다(상세 재확인은 이 문서 뒤쪽 "문서 정합성 정정 2건 — 2026-07-17" 절 참고). 아래 6블록 좌표 자체는 그 8개 중 원본 6개에 대한 정확한 역사적 기록이므로 수정하지 않는다:
- 중앙 가로 바: `x0,y4,w14,h2`(전체 폭)
- 상단 코너 3블록: `x2,y2` / `x6,y2` / `x10,y2` (각 2×2, 위쪽 피크)
- 하단 코너 2블록: `x2,y6` / `x10,y6` (각 2×2, 중앙 하단은 빈 채로 — 아래쪽은 비대칭)

**신설 아이콘(원화 단계)**: `PixelEyeOff`(raw FRAME, 등록 전) — nodeId `414:2`, Icons 페이지(`96:7`) 내 `x=1241, y=403, w=14, h=10`(Pixel/Eye `x=1121` 바로 옆, 기존 Pixel/* 10종의 120px 간격 규칙을 그대로 연장). 캔버스 14×10, 잉크 `#1a1a1a`, 블록 조합 방식(Pixel/Eye와 동일 트랙, Pixel/Close의 스트로크 방식은 가져오지 않음) 유지. 자식 3개(전부 RECTANGLE, name="Vector"):
- 바 `414:3`: `x0,y4,w14,h2` (Pixel/Eye 중앙 바와 동일 위치/크기)
- 하단 좌 `414:4`: `x2,y6,w2,h2` (Pixel/Eye 하단좌 블록과 동일 위치)
- 하단 우 `414:5`: `x10,y6,w2,h2` (Pixel/Eye 하단우 블록과 동일 위치)

**형태 선택 근거 (닫힌 눈꺼풀 vs 슬래시, (b)안 채택)**: 브리프가 제시한 두 방향 중 (b) "코너 블록 제거 → 평평한 눈꺼풀 실루엣"을 택했다. Pixel/Eye의 상단 코너 3블록(위쪽 피크, 열린 눈의 속눈썹/눈썹 신호)만 제거하고, 중앙 바와 하단 코너 2블록은 Pixel/Eye와 완전히 동일한 좌표로 유지했다(6블록 → 3블록). 이유:
1. **슬래시(a안) 기각 사유**: 14×10(2px 그리드 기준 7×5칸) 캔버스는 이미 6블록(34% 잉크 밀도)로 조밀하다. 대각선 슬래시를 얹으려면 스텝형 블록 3~5개를 추가해야 하는데, 이 초소형 해상도에서는 계단 형태가 매끄러운 사선으로 읽히지 않고 뭉개진 얼룩처럼 보일 위험이 크다고 판단했다(2px 블록 단위로는 사선을 매끄럽게 표현할 해상도가 부족).
2. **(b)안 채택 사유**: 상단 피크만 제거하면 잉크 밀도가 48px²→36px²(75%)로 줄면서 실루엣이 뚜렷하게 "납작"해진다. 이는 Pixel/Eye 옆에 나란히 놓았을 때 "열림(피크 있음) vs 닫힘(피크 없음, 납작)"이라는 형태 자체의 차이로 즉시 구분된다(색상에만 의존하지 않는 접근성 기준 충족). 하단 2블록을 완전히 없애 바 하나(1블록)만 남기는 방안도 검토했으나, 그 경우 눈과의 연관성이 옅어져 단순 "-"(minus/dash) 기호로 오독될 위험이 있다고 판단해 하단 2블록(속눈썹 흔적)은 유지했다.
- `get_screenshot`(scale 10, 각 140×100px)으로 `Pixel/Eye`와 `PixelEyeOff`를 나란히 비교 확인: Pixel/Eye는 상하 피크가 있는 복잡한 실루엣, PixelEyeOff는 상단이 평평하고 하단에만 짧은 다리 2개가 남은 실루엣으로 형태 차이가 명확히 구분됨을 확인했다.

**이름**: 기존 네이밍 컨벤션(`Pixel/Star`, `Pixel/Search`, `Pixel/Close`, `Pixel/NoResult`)에 부합해 `Pixel/EyeOff`를 그대로 채택. raw 레이어 이름은 원본 `PixelEye`와 짝을 맞춰 `PixelEyeOff`로 지정.

**근거 메모**: 새 아이콘 아래 텍스트 노드(`414:6`, `x=1241, y=470, w=360`)에 위 판단 근거를 한글로 요약해 온캔버스에도 남겨뒀다.

**정식 등록 완료(2026-07-14, design-systems)**: `PixelEye`(`247:6814`)가 raw였다가 design-systems가 `createComponentFromNode`로 `Pixel/Eye`(`281:405`)로 등록한 것과 동일한 역할 분리를 따라, design-systems가 `createComponentFromNode(414:2)`로 `Pixel/EyeOff` 정식 컴포넌트(`415:892`)를 등록했다. 원본 raw `414:2`의 좌표·자식 노드 ID(`414:3`/`414:4`/`414:5`)·fill(#1a1a1a)을 그대로 승계했고, 형태 변형은 전혀 없음을 `get_screenshot`/hex 재대조로 확인했다. description은 위 "Pixel/* 11종 상세" 표 참고.

## 상태: `PixelCheck` 신규 원화 — Checkbox 체크마크 정식 아이콘화 준비 (2026-07-16)

design-prompter 브리프(design-systems가 Checkbox 컴포넌트의 체크마크를 "raw VECTOR 직접 그리기"에서 "등록된 Icon 컴포넌트의 INSTANCE"로 재조립하기 전, 그 정식 Icon 원화가 먼저 필요함)에 따라 신규 원화를 그렸다. 완전히 새로운 형태를 창작한 것이 아니라, 기존 Checkbox 컴포넌트 내부에 이미 박혀 있던 체크마크(`474:888`, State=Checked variant 내부, 부모 `474:886` "Box")를 정식 아이콘 원화로 그대로 옮겨 그린 것이다. `474:888`, 다른 확정 Pixel/Icon 컴포넌트는 전혀 건드리지 않았다(읽기 전용 관찰만).

**0단계 라이브 재검증**: 작업 시작 전 Icons 페이지(`96:7`)를 `get_metadata`로 직접 재확인했다 — 체크마크/checkmark/check류 아이콘은 등록 컴포넌트(Icon/* 8종, Pixel/* 11종) 어디에도 없음을 라이브로 재확인했다(문서 기록과 일치).

**관찰(실측, 문서 사전 기록보다 우선)**: `474:888`을 `use_figma`로 직접 읽어 실제 벡터 구성을 확인했다:
- 크기: 8×7 (부모 `474:886` "Box" 내부 상대좌표 `x=3, y=3`)
- `vectorPaths`: `"M 0 4 L 3 7 L 8 0"` (winding NONZERO)
- `strokeWeight`: **3**(브리프의 사전 기록 "weight2"는 문서 오기 — 라이브 재검증 결과 3이 맞다고 확인, 실측값을 채택해 그대로 재현했다)
- `strokeAlign`: CENTER, `strokeCap`: ROUND, `strokeJoin`: ROUND
- 색상: 잉크 `rgb(0.102, 0.102, 0.102)` ≈ `#1a1a1a`(원본은 `color/ink/900` 변수 바인딩, 신규 원화는 브리프 지시대로 변수 바인딩 없이 동일 hex 평값만 사용 — design-systems가 인스턴스 오버라이드 시 변수 바인딩을 새로 정할 것)
- fills: 없음(stroke-only)

**트랙/이름 판단**: 8×7 크기와 stroke-vector 구성(block-fill 아님)을 `Icon/*`(24px 라인, strokeWeight 3px 균일이지만 스케일이 3배 이상 차이)과 `Pixel/*`(특히 `Pixel/Close` — 10×10 프레임에 8×8 stroke-vector, weight 2px, cap SQUARE)에 나란히 대조했다. 스케일과 "채움 없는 단일 stroke vector" 구성 방식이 `Pixel/Close`와 훨씬 가까워 **`Pixel/*` 트랙으로 편입**하기로 했고, 이름은 브리프 권고대로 **`Pixel/Check`**를 채택한다. 단 `Pixel/Close`(weight2/SQUARE cap)와 달리 원본 체크마크는 weight3/ROUND cap이었으므로 그 차이는 임의로 통일하지 않고 원본 그대로 보존했다 — 같은 트랙 안에서도 stroke-vector 구성 방식을 공유하는 `Pixel/Close`와 100% 동일한 스펙일 필요는 없다는 판단(브리프의 "실제로 나란히 비교해보고 다르게 판단되면 근거를 남기고 다르게 정해도 된다" 조항에 따름).

**신설 아이콘(원화 단계, raw FRAME)**: `PixelCheck` — nodeId `814:2`, Icons 페이지(`96:7`) 내 `x=1361, y=403, w=8, h=7`(`Pixel/EyeOff` `x=1241` 바로 옆, 기존 Pixel/* 11종의 120px 간격 배치 규칙을 그대로 연장). 자식 1개: VECTOR `814:3`("Check", `x=0,y=0,w=8,h=7`, `vectorPaths="M 0 4 L 3 7 L 8 0"`, strokeWeight 3, strokeCap/Join ROUND, stroke `#1a1a1a`, fills 없음) — `474:888`과 값 전부 동일.

**배치 절차(예외 재사용)**: "Graphic Assets" 페이지(`90:2`)가 사용자에 의해 삭제된 상태라, 위에 기록된 기존 예외(정상 파이프라인의 스테이징 단계 생략, Icons 페이지에 raw 벡터로 바로 배치)를 그대로 따랐다. `PixelEyeOff` 때와 동일한 raw FRAME + 단일 벡터 자식 패턴을 사용했다.

**형태 동일성 확인**: `get_screenshot`(scale 확대, base64 inline)으로 원본 `474:888`과 신규 `814:2`를 나란히 렌더링해 비교했다 — 둘 다 11×10px 렌더 크기(원본 벡터가 8×7이지만 stroke overflow로 렌더 바운딩이 커짐), 동일한 체크마크 실루엣·동일한 잉크 색으로 시각적으로 일치함을 확인했다.

**근거 메모**: 새 아이콘 아래 텍스트 노드(`814:4`, `x=1361, y=470, w=360`)에 위 실측값·트랙 판단 근거를 한글로 요약해 온캔버스에도 남겨뒀다(`PixelEyeOff` 때와 동일 패턴).

**다음 단계(design-systems)**: `createComponentFromNode(814:2)`로 `Pixel/Check` 정식 컴포넌트 등록 → Checkbox 컴포넌트의 State=Checked variant 안 raw VECTOR(`474:888`)를 이 신규 컴포넌트의 INSTANCE로 교체하는 재조립 작업으로 이어받으면 된다. 원화 자체의 색은 인스턴스 오버라이드로 `color/ink/900` 바인딩이 그대로 유지될 것이므로 원화의 정확한 hex 값 자체는 중요하지 않다(트랙 일관성만 지킴). **⚠ 2026-07-16 후속 정정**: 실제로는 이 인스턴스 오버라이드가 이후 `docs/design/design-system.md` 21절에서 `color/ink/900`(검정)이 아니라 `color/text-inverse`(#FFFFFF, 흰색)로 재바인딩됐다 — Checkbox Box가 이미 `color/sky/500`(스카이블루)이었다는 사실이 뒤늦게 반영된 결과다. 원화(`814:2`/`815:2`) 자체의 기본 hex는 여전히 잉크로 유지되며 변경 대상이 아니다.

## 상태: `Pixel/Check` 정식 등록 완료 — Checkbox 체크마크 아이콘화 (2026-07-16)

`PixelEye`→`Pixel/Eye`, `PixelEyeOff`→`Pixel/EyeOff` 때와 동일한 역할 분리를 따라, design-systems가 위 원화 `PixelCheck`(`814:2`, raw FRAME)를 `createComponentFromNode`로 `Pixel/Check` 정식 컴포넌트(`815:2`)로 등록했다. 원본 raw `814:2`의 좌표·자식 노드 ID(`814:3`)·stroke 속성(weight3/ROUND/`#1a1a1a`)을 그대로 승계했고 형태 변형은 없다.

이어서 design-systems가 Checkbox(`474:899`) `State=Checked` 안 Box(`474:886`)의 raw VECTOR 체크마크(`474:888`)를 `Pixel/Check`의 INSTANCE(`815:3`)로 교체하고 원본 raw VECTOR는 제거했다 — 이 시점 색상은 `color/ink/900` 바인딩 그대로 무변경, 구조만 raw vector→instance로 전환했다(컴포넌트 조립 순서 원칙 준수). 상세 절차·검증은 `docs/design/design-system.md` 0-26절 참고. **⚠ 2026-07-16 재정정(21절)**: 이후 Box(`474:886`)가 이미 `color/sky/500`(스카이블루)으로 확정 디자인과 일치해 있었다는 사실이 확인되며, 이 인스턴스 내부 실제 렌더링 vector(`I815:3;814:3`)의 stroke가 `color/ink/900`(검정)에서 `color/text-inverse`(#FFFFFF, 흰색)로 재바인딩됐다 — 현재 유효한 색상은 흰색이다. 상세 경위는 `docs/design/design-system.md` 21절 참고.

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

**발견사항 처리 완료 (2026-07-14)**: 확정 login 프레임(`247:6666`)을 갭 감사차 다시 확인하는 과정에서, 비밀번호 입력창 안에 `PixelEye`(nodeId `247:6814`, 14×10)라는 비밀번호 표시/숨김 토글 아이콘이 이미 그려져 있는 것을 발견했었다. 이 아이콘은 **docs/planning FR 목록에 없는 기능**(비밀번호 show/hide는 어떤 FR에도 명시되지 않음)이라 이 갭 감사의 "새로 그려야 할 누락"에는 해당하지 않았다. 다만 이미 확정 프레임에 실존하는 아이콘인데 최초 9종 추출 라운드에서 함께 등록되지 않고 누락되어 있었고, **design-systems가 확정 프레임의 원본 벡터를 그대로 clone해 `Pixel/Eye`(등록 컴포넌트 `281:405`)로 마저 추출·등록 완료**했다(위 "Pixel 마이크로 아이콘" 절 참고). 원본 `247:6814`는 무수정으로 그대로 존재한다. 이어서 **2026-07-14 후속 라운드**에서 그 "표시" 상태의 짝인 "숨김" 상태 아이콘(`PixelEyeOff`, 원화 `414:2`)을 새로 그려 인계했고, **같은 날 design-systems가 `Pixel/EyeOff`(`415:892`)로 정식 등록까지 완료**했다(위 "Pixel/EyeOff 정식 등록 완료" 절 참고) — 이 역시 FR 목록에는 없는 기능이지만, 이미 존재하는 토글 UI의 기능적 완결을 위한 짝 아이콘 신설이라 갭 감사가 아닌 별도 브리프로 처리됐다.

참고로 로그인 버튼 안의 화살표형 "Icon"(nodeId `247:6829`, 14×14)은 재사용 가능한 이름으로 명명되지 않은 장식용 화살표라 이번 보고에서는 관찰만 남기고 조치 대상에서 제외했다(변경 없음, 계속 조치 대상 아님).

**값 출처**: `docs/design/brand-guide.md`(색상 hex), `docs/planning/01_연락처관리_웹서비스_구현요구사항_v1.0.pdf`, `02_...화면정의서...pdf`, `03_...기능정의서...pdf`(FR 목록) + 확정 8개 프레임 직접 재관찰(get_metadata/get_design_context, 읽기 전용) + Pixel/Eye 벡터 좌표 실측(use_figma 읽기 전용) + PixelCheck 원본(`474:888`) 벡터 좌표/stroke 속성 실측(use_figma 읽기 전용).

## 상태: Icons 페이지(`96:7`) 색상 바인딩 전수 감사 — Icon/* 8종 + Pixel/* 12종, A/B 분류 (2026-07-17, design-pl 브리프)

design-pl 브리프에 따라 "Icons" 페이지(`96:7`)에 정식 등록된 Icon/* 8종 + Pixel/* 12종 **전부**(자식 벡터 포함, 스팟체크 아님)를 `use_figma` 읽기 전용 스크립트로 순회해 실제 fill/stroke hex와 `boundVariableId` 상태를 재실측했다. 이번 라운드는 **색상 판단·근거 보고까지만**이며, 벡터 형태 수정도 변수 실바인딩도 하지 않았다(그건 design-systems의 다음 단계). 원본 확정 디자인 프레임(`501:2505` 하위)은 이번 작업에서 열람하지 않았다 — 필요한 대조값(아바타 색, Icon/Alert 인스턴스 색)은 신·구 세대 확정 프레임 자체가 아니라 그 인스턴스를 담은 파일럿 페이지(`222:524`)를 통해 읽기 전용으로만 확인했다.

### 배경 정리 — 두 세대, 그리고 이번 판단의 기준선

이 프로젝트는 확정 디자인이 두 세대를 거쳤다(브리프 배경 그대로): 구 세대(`248:11689`, 삭제됨, `brand-guide.md`·이 문서의 원래 색상표가 근거로 삼던 세대)와 신 세대(`501:2505`, Stage2, 현재 유효). Stage2에서 Primary 브랜드색이 다수 요소에서 틸(`#17a398`)→스카이블루(`#1395e6`, `color/sky/500`)로 전환됐지만 **전면 전환이 아니다** — Join "비밀번호 찾기" 링크처럼 재실측 결과 여전히 정당하게 틸을 쓰는 요소도 있다(`design-system.md` 0-20절). 이번 감사도 "틸이면 무조건 구식"으로 기계적으로 판단하지 않고, 각 요소가 실제로 신 세대 확정 프레임(또는 그 인스턴스)에서 어떻게 등장하는지를 근거로 삼았다.

Icon/* 8종 중 신 확정 프레임에 실제로 등장하는 건 `Icon/User`(Avatar 내부)와 `Icon/Alert`(토스트/배너) 둘뿐이다(Brand Guide 9번, `design-system.md` 4절). 나머지 6종(Search/Add/Edit/Delete/Category/Logout)은 화면에서 대신 `Pixel/*` 마이크로 아이콘이 쓰이고 있어 24px `Icon/*` 자체의 색을 신 확정 프레임과 직접 대조할 화면 근거가 없다 — 이 6종은 `Icon/User`·`Icon/Alert`의 실제 처리를 참고 기준으로 삼아 판단했다.

**라이브 재확인 결과(신 세대 근거)**:
- `Icon/User`가 실제로 쓰이는 Avatar(`104:131`)의 INSTANCE(main 확정 프레임 안 `501:6370`)를 읽기 전용으로 재조회한 결과, 두 Ellipse(머리/어깨) 모두 로컬 오버라이드 없이 마스터 그대로 **틸 `#17a398`**로 렌더링되고 있음을 확인했다 — Avatar는 Stage2 전환 대상에 포함된 적이 없고(`design-system.md` 0-20절 표에 Avatar 행 없음), 실제로 지금도 틸이다. 즉 "브랜드 Primary가 틸→스카이블루로 바뀌었다"는 일반 규칙이 **Avatar/Icon/User에는 적용되지 않는다** — Join 링크 사례와 같은 종류의 정당한 예외다. **⚠ 2026-07-17 후속 정정(아래 "Icon/* 8종 Basic/Visual 트랙 재판정" 절 참고)**: 이 결론은 Avatar 안의 **아이콘 글리프(머리/어깨 Ellipse)** 색만 확인한 것이고, Avatar 컴포넌트 자체의 **원 배경 fill**은 이때 확인 대상이 아니었다. 후속 라운드에서 원 배경 fill을 직접 재조회한 결과 실제 인스턴스(`501:6370`)의 원 배경은 마스터(틸, 바인딩됨)와 달리 **스카이블루 `#1395e6`(unbound 로컬 오버라이드)**였다 — "Avatar가 틸이다"는 이 문장은 글리프 색에는 맞지만 원 배경 색에는 틀렸다. 상세는 아래 절 참고.
- `Icon/Alert`가 실제로 쓰이는 인스턴스 2개(login-알림창 확정 프레임의 `501:5434`, main-알림창 확정 프레임의 `501:7088`)를 읽기 전용으로 재조회한 결과, 강조 원(Ellipse)은 마스터와 동일하게 **`#ffce2c`**(앰버, 바인딩 상태는 마스터가 이미 `color/bg-cta-amber`), 느낌표 바/닷은 마스터와 동일하게 **`#1c1f21`**로 렌더링되고 있었다(로컬 오버라이드 없음).

### Icon/Alert 강조 원(Ellipse `96:38`) — 브리프가 지목한 특이사항, 실측 결과

**브리프의 우려(A그룹 후보 vs 값 자체 결함)에 대한 답**: 실측 결과 **A그룹**이다 — `96:38`(Ellipse)의 현재 라이브 fill은 `#ffce2c`이고 `boundVariables.fills[0]`가 `VariableID:615:133`(`color/bg-cta-amber`)를 정확히 가리키고 있다. 값도 구값(`#FFCB47`)으로 되돌아가 있지 않고, 바인딩도 정상이다 — `design-system.md` 0-20절 기록("raw amber(#FFCB47, 미바인딩)→`color/bg-cta-amber`로 리바인딩")과 완전히 일치하는 상태다.

**따라서 "Icons 페이지 전체가 unbound"라는 신규 조사의 블랭킷(포괄) 진술은 이 노드에 한해 부정확하다** — 표본 40개 이상 중 이 노드 1개는 이미 바르게 바인딩돼 있다. Icon/Alert 컴포넌트의 나머지 두 자식(느낌표 바 `96:39`, 닷 `96:40`)은 실제로 raw `#1c1f21` 미바인딩 상태이며, 이는 아래 ink 이중 값 판단에서 B그룹으로 분류했다.

### ink/800 vs ink/900 판단 — 실측 근거와 결론

`color/ink/900`(`#1A1A1A`, `VariableID:95:9`)은 `design-system.md` 1-1절에 "정정: `color/ink/900` 값을 기존 `#1C1F21`에서 확정 디자인의 실측값 `#1a1a1a`로 정정"이라고 명시된 **교정된 주값**이다. `color/ink/800`(`#1C1F21`, 신규 원시값)은 같은 문서 0-1절에서 "Row Action Button(`260:95`) Neutral 보더 전용, `color/ink/900`과 별개 값"으로 **명시적으로 좁게 스코프된 예외**다 — 일반적인 "잉크"의 대체 토큰이 아니다.

**실측으로 확인한 근거 3가지**(design-qa식 자체 재대조):
1. Icon/* 8종·Pixel/Edit·Pixel/Delete가 쓰는 `#1c1f21`은 전부 2026-07-13 최초 추출 라운드(ink/900 교정이 있기 전, 0-1절은 그보다 나중인 design-qa 감사 라운드)에서 확정된 값이다 — 시점상 교정 전 구버전 ink 정의의 잔재일 가능성이 높다.
2. Row Action Button(`260:95`)을 직접 재조회한 결과, **Neutral** Default(`260:34`)의 보더는 정말로 `component/row-action-button-border-neutral`(→ink/800, `#1c1f21`)에 정상 바인딩돼 있다 — ink/800의 선언된 좁은 용도가 실제로 지켜지고 있음을 재확인했다. 그런데 같은 컴포넌트의 **Danger** Default(`260:53`)는 `design-system.md` 13절 P2에서 보더가 `color/ink/900`(`#1A1A1A`)으로 이미 재실측·정정됐는데, 그 안에 인스턴스로 들어가는 `Pixel/Delete` 아이콘의 fill은 여전히 마스터 그대로 `#1c1f21`(미바인딩)이었다 — **같은 버튼 안에서 보더(#1A1A1A)와 아이콘(#1C1F21)이 실측 결과 서로 다른 값으로 어긋나 있는 것을 직접 확인했다.** 이는 `#1c1f21`이 "ink/800을 의도적으로 쓴 것"이 아니라 "아이콘 마스터가 교정 이전 값에 머물러 있어 생긴 우연한 어긋남"이라는 강한 증거다 — ink/800이 정말 의도된 값이었다면 최근 재실측(P2)에서 보더도 함께 `#1c1f21`로 맞춰졌을 것이다.
3. Icon/Alert 인스턴스(`501:5434`/`501:7088`)의 느낌표 바/닷도 `#1c1f21`인데, 같은 Toast 계열 컴포넌트의 본문 텍스트(title `263:44`)는 이미 `color/ink/900`(`#1A1A1A`)에 바인딩돼 있다(`design-system.md` 13절 P14) — 알림 시스템 전체의 "잉크" 기준선이 `#1A1A1A`임을 시사한다.

**결론**: Icon/* 8종·Pixel/Edit·Pixel/Delete가 쓰는 `#1c1f21`은 **(b) 교정 전 구버전 ink 정의의 잔재**로 판단한다 — `color/ink/800`으로 묶지 않고 `color/ink/900`(#1a1a1a)으로 재바인딩할 것을 권고한다. `color/ink/800`은 Row Action Button Neutral 보더라는 좁은 스코프 밖으로 확장하지 않는 것이 design-system.md의 기존 결정과 일치한다.

**⚠ 2026-07-17 후속 확인 완료**: 아래 "Icon/* 8종 Basic/Visual 트랙 재판정" 절에서 이 B그룹 재실측을 다시 수행한 결과, 이 문서 작성 시점 이후 design-systems가 이미 이 권고를 실행에 옮겨 **Icon/* 8종의 모든 stroke·detail fill이 `color/ink/900`(`#1a1a1a`)로 바인딩 완료된 상태**임을 라이브로 확인했다(더 이상 `#1c1f21`이 아니다). 아래 절의 표는 그 갱신된 라이브 값을 반영한다.

### A/B 분류표 — Icon/* 8종

값 자체는 (컴포넌트 내에서) 균일하므로 요소 그룹 단위로 분류한다. "재해석 판단"은 이 라운드에서 내린 그래픽 크래프트 판단이며, 실제 바인딩은 design-systems 몫이다.

| 아이콘 | 요소 | 실측 hex | 현재 바인딩 | 분류 | 제안 토큰·근거 |
|---|---|---|---|---|---|
| Icon/Search(`96:12`) | Ellipse(`96:9`) fill | `#17a398` | 없음(unbound) | **A** | `color/teal/500` — 값 그대로 일치, 재해석 불필요(아래 "틸 유지 판단" 참고) |
| | Ellipse(`96:9`) stroke 3px, Rectangle(`96:11`) fill | `#1c1f21` | 없음 | **B** | `color/ink/900`(#1a1a1a) — 위 ink 판단 근거 참고 |
| Icon/Add(`96:17`) | Rectangle(`96:14`) fill | `#17a398` | 없음 | **A** | `color/teal/500` |
| | Rectangle(`96:14`) stroke, Rectangle(`96:15`/`96:16`) fill | `#1c1f21` | 없음 | **B** | `color/ink/900` |
| Icon/Edit(`96:22`) | Pencil Silhouette(`96:20`) fill | `#17a398` | 없음 | **A** | `color/teal/500` |
| | Pencil Silhouette(`96:20`) stroke, Rectangle(`96:21`) fill | `#1c1f21` | 없음 | **B** | `color/ink/900` |
| Icon/Delete(`96:27`) | Rectangle 뚜껑(`96:24`)/몸통(`96:26`) fill | `#17a398` | 없음 | **A** | `color/teal/500` |
| | 위 2개 stroke, Rectangle 손잡이(`96:25`) fill | `#1c1f21` | 없음 | **B** | `color/ink/900` |
| Icon/Category(`96:31`) | Rectangle 2개(`96:29`/`96:30`) fill | `#17a398` | 없음 | **A** | `color/teal/500` |
| | 위 2개 stroke | `#1c1f21` | 없음 | **B** | `color/ink/900` |
| Icon/Logout(`96:36`) | Rectangle 문(`96:33`) fill | `#17a398` | 없음 | **A** | `color/teal/500` |
| | Rectangle 문 stroke, Rectangle(`96:34`)/Arrow Head(`96:35`) fill | `#1c1f21` | 없음 | **B** | `color/ink/900` |
| Icon/Alert(`96:41`) | **Ellipse(`96:38`) fill** | `#ffce2c` | **`color/bg-cta-amber`(정상)** | **A(이미 완료)** | 재작업 불필요 — 위 "Icon/Alert 강조 원" 절 참고 |
| | Ellipse(`96:38`) stroke, Rectangle(`96:39`)/Ellipse 닷(`96:40`) fill | `#1c1f21` | 없음 | **B** | `color/ink/900` — Toast title이 이미 ink/900인 것과 통일 |
| Icon/User(`96:45`) | Ellipse 2개(`96:43`/`96:44`) fill | `#17a398` | 없음 | **A** | `color/teal/500` — Avatar 인스턴스(`501:6370`) 실측 결과 신 세대에서도 여전히 틸, 재해석 불필요 |
| | 위 2개 stroke | `#1c1f21` | 없음 | **B** | `color/ink/900` |

**틸 유지 판단(Search/Add/Edit/Delete/Category/Logout 6종의 fill)**: 이 6종은 신 확정 프레임에 24px 아이콘으로 직접 등장하지 않아 화면 대조 근거가 없다. 유일하게 직접 대조 가능한 형제(Icon/User)가 Avatar 안에서 신 세대에도 여전히 틸로 확인됐고, Stage2 틸→스카이블루 전환은 "Primary CTA/브랜드 배경" 역할을 하는 특정 요소(사이드바, 추가 버튼, 체크박스, 카드 스트립 등)에 한정된 선택적 전환이었다(design-system.md 0-20/23/25절 — 전면 치환이 아님). 이 6종은 CTA나 브랜드 배경이 아니라 "틸 평면 채색 아이콘"이라는 동일한 역할이라 Icon/User와 같은 취급이 합리적이라고 판단해 **A(틸 유지)**로 분류했다. 다만 이 6종은 신 확정 프레임에 직접 등장하지 않는다는 근거 공백이 있으므로, design-systems가 값을 그대로 바인딩하기 전에 이 판단에 이견이 없는지 design-pl 확인을 권장한다(재해석 여지가 완전히 0은 아님 — 보수적으로 A로 판단했다는 점을 명시).

**⚠ 2026-07-17 후속 갱신 — 이 A/B 분류표는 "값이 맞는가"만 판단한 것이고, 이후 별도 라운드(아래 최신 절)에서 "그 값을 애초에 이 아이콘에 써야 하는가"(Basic/Visual 트랙)를 재판정했다.** 두 판단은 레이어가 다르다 — 이 표는 "현재 라이브 fill/stroke 값이 올바른 토큰을 가리키는가"만 다뤘고(색상 정확성), 트랙 재판정은 "그 fill 자체(면색)를 애초에 유지해야 하는가"를 다룬다(조형 트랙). 트랙 재판정 결과 Search/Add/Edit/Delete/Logout/User 6종은 Basic 트랙으로 분류되어 이 표의 A그룹 fill 바인딩 자체가 무효화(제거 대상)되지만, 이건 이 표가 틀렸다는 뜻이 아니다 — "그 시점까지 라이브였던 teal fill의 색상 값 자체는 정확했다(A그룹 판정 유효)"는 사실과 "그 fill을 애초에 갖고 있으면 안 됐다(Basic 트랙 판정)"는 사실은 모순되지 않는다. design-systems는 이미 완료한 A/B 재바인딩 작업을 "실수"로 여기지 않아도 된다 — 순서대로 (1) 색상 정확성 교정 → (2) 트랙(면 채움 여부) 재설계, 두 단계가 정상적으로 이어진 것뿐이다. 상세는 최하단 절 참고.

### A/B 분류표 — Pixel/* 12종

| 아이콘 | 요소 | 실측 hex | 현재 바인딩 | 분류 | 제안 토큰·근거 |
|---|---|---|---|---|---|
| Pixel/Star(`255:11`) | vector 8개 | `#1a1a1a` | 없음 | **A** | `color/ink/900` — 이미 교정된 값과 정확히 일치 |
| Pixel/Search(`255:26`) | vector 13개 | `#17a398` | 없음 | ~~**A**~~ **재검증 필요 → 실제로는 sky/500, 아래 "Pixel/Search 색상 검증" 절 참고(2026-07-17)** | ~~`color/teal/500`~~ → **`color/sky/500`(리바인딩 승인)** |
| Pixel/Plus(`255:30`) | vector 2개 | `#1a1a1a` | 없음 | **A** | `color/ink/900` |
| Pixel/Logout(`255:43`) | vector 11개 | `#ffffff` | 없음 | **A(값)/제안 토큰 유의**| 값은 흰색으로 정확하나, 흰 배경용 `color/gray/0`이 아니라 **`color/text-inverse`**(#FFFFFF, 어두운/브랜드색 배경 위 인버스 아이콘 의미)로 바인딩할 것을 권고 — Checkbox 체크마크가 동일한 논리(스카이블루 배경 위 흰 체크)로 `color/text-inverse`를 채택한 전례(21절)를 따름. 헤더 로그아웃 버튼이 Style=Ink(잉크 배경)로 확정된 것(18절)도 "브랜드색 배경 위 흰색"이 아니라 "어두운 배경 위 인버스"라는 의미와 부합 |
| Pixel/Edit(`255:62`) | vector 17개 | `#1c1f21` | 없음 | **B** | `color/ink/900` — 위 ink 판단 근거 2번(Row Action Button Danger 보더 vs 아이콘 불일치) 그대로 적용 |
| Pixel/Delete(`255:104`) | vector 39개 | `#1c1f21` | 없음 | **B** | `color/ink/900` — 동일 근거 |
| Pixel/Close(`255:107`) | vector 1개 stroke(weight2) | `#1a1a1a` | 없음 | **A** | `color/ink/900` |
| Pixel/Warning(`255:120`) | vector 9개(원형) | `#ff5a76` | 없음 | **A** | `color/coral/500` |
| | vector 2개(느낌표) | `#ffffff` | 없음 | **A(값)/제안 토큰 유의** | Pixel/Logout과 동일 논리 — `color/text-inverse` 권고(코랄 배경 위 인버스 아이콘) |
| Pixel/NoResult(`255:149`) | vector 21개(몸통) | `#1395e6` | **`color/sky/500`(이미 완료)** | **A(이미 완료)** | design-systems가 2026-07-16(design-system.md 23절 B)에 이미 리바인딩 — 재작업 불필요 |
| | vector 6개(크랙) | `#ff5a76` | 없음 | **A** | `color/coral/500` |
| Pixel/Eye(`281:405`) | descendant **14개**(fill 보유) | `#1a1a1a` | 없음 | **A** | `color/ink/900` — 이 14개 값은 2026-07-17 재확인으로 확정됐다(아래 "문서 정합성 정정 2건" 절 참고, 위 "PixelEyeOff 정식 등록 완료" 절의 6블록 기록과의 단위 차이 아님, 실제 컴포넌트가 늘어난 것) |
| Pixel/EyeOff(`415:892`) | vector 3개 | `#1a1a1a` | 없음 | **A** | `color/ink/900` |
| Pixel/Check(`815:2`) | vector 1개 stroke(weight3) | `#1a1a1a` | 없음 | **A** | `color/ink/900`(마스터 원화 자체는 잉크 유지가 맞음 — Checkbox 인스턴스 쪽만 `color/text-inverse`로 별도 오버라이드된 상태, 21절 기존 결정과 일치, 원화 자체를 바꾸는 게 아님) |

### 요약

- **A그룹(값 정정 불필요, 그대로 바인딩)**: Icon/* teal 계열 7종 fill(Search/Add/Edit/Delete×2/Category×2/Logout/User×2) + Icon/Alert Ellipse(이미 완료) + Pixel/Star·Plus·Close·Warning(coral+흰색)·NoResult(이미 완료 + 크랙)·Eye·EyeOff·Check = 값 불일치 0건. **Pixel/Search는 이 A그룹 판정에서 2026-07-17 후속 검증으로 제외됐다 — 아래 "Pixel/Search 색상 검증" 절 참고.**
- **B그룹(재해석 필요, ink/900로 재바인딩 권고)**: Icon/* 8종의 `#1c1f21` 스트로크·잉크 fill 전체(약 20개 노드) + Pixel/Edit(17개)·Pixel/Delete(39개) = `color/ink/800`이 아니라 `color/ink/900`(#1a1a1a)으로. 근거는 위 "ink/800 vs ink/900 판단" 절.
- **토큰 선택 유의(A그룹 내 세부 권고)**: Pixel/Logout·Pixel/Warning의 흰색 요소는 값은 맞지만 `color/gray/0`이 아니라 `color/text-inverse`로 바인딩할 것을 권고(Checkbox 체크마크 전례와 일관성).
- **Icon/Alert Ellipse(`96:38`)**: 라이브 값 `#ffce2c`, `color/bg-cta-amber`에 정상 바인딩 확인 — design-system.md 0-20절 기록과 일치, 신규 조사의 "전체 unbound" 진술은 이 노드에는 해당하지 않는다.
- **ink 이중 값**: `color/ink/800`(#1C1F21)은 Row Action Button Neutral 보더 전용으로 좁게 유지하고, Icon/*·Pixel/Edit·Pixel/Delete의 `#1c1f21`은 교정 전 구버전 ink 정의의 잔재로 판단해 `color/ink/900`(#1a1a1a)으로 재바인딩 권고.
- 벡터 형태 수정 없음, 변수 실바인딩 없음(순수 조사·판단) — design-pl이 이 결과를 근거로 design-systems에 실제 바인딩 브리프를 별도로 전달할 것.

**값 출처**: `docs/design/brand-guide.md`(구 세대 색상 기준, 대조용) + `docs/design/design-system.md`(1-1/1-2/4/13/18/21/23/25절, 현재 유효한 프리미티브·Stage2 전환 이력) + Icons 페이지(`96:7`) 전수 실측(`use_figma` 읽기 전용, Icon/* 8종+Pixel/* 12종 및 그 자식 전체) + Avatar 인스턴스(`501:6370`)·Icon/Alert 인스턴스(`501:5434`/`501:7088`)·Row Action Button(`260:95`) Neutral/Danger Default 실측(`use_figma` 읽기 전용, 파일럿 페이지 `222:524`/`103:3` 경유) — 임의 근사치 없음.

## 상태: 문서 정합성 정정 2건 — "6종" 라벨 오기, Pixel/Eye 벡터 개수 서술 불일치 (2026-07-17, harness-auditor 발견 / 사용자 승인)

harness-auditor가 이 문서에서 문서 정합성 오류 2건을 발견했고 사용자가 정정을 승인했다. 둘 다 순수 문서 서술 정정이다(디자인 판단이나 벡터 형태·색상 값 변경이 아니다). Figma 쓰기 작업은 하지 않았다(읽기 전용 재확인만).

**1건 — "6종" 라벨 오기**: 위 "Icons 페이지 색상 바인딩 전수 감사" 절 "요약"의 "Icon/* teal 계열 **6종** fill(Search/Add/Edit/Delete×2/Category×2/Logout/User×2)" 표현에서, 실제로 나열된 아이콘 **종류**는 Search/Add/Edit/Delete/Category/Logout/User로 **7종**이다 — Delete·Category·User가 각각 노드 2개씩이라 "×2"로 표기된 것은 요소(노드) 개수 표기이지 종류 수와는 무관하다. "6종"을 "7종"으로 정정했다(위 요약 절 반영 완료). A/B 분류표의 노드 수(10개, 9/14/20/24/26/29/30/33/43/44)는 처음부터 정확했으므로 건드리지 않았다.

**2건 — Pixel/Eye(`281:405`) 벡터 개수 서술 불일치**: "PixelEyeOff 정식 등록 완료" 절의 관찰 기록(2026-07-14 작성, "6블록의 좌표를 확인했다")과 "Icons 페이지 색상 바인딩 전수 감사" A/B 분류표(2026-07-17 작성, "descendant 14개")가 서로 다른 숫자를 쓰고 있어, `281:405`를 `use_figma`(읽기 전용)로 자식 트리 전체를 다시 실측했다.

**실측 결과**: `281:405`(Pixel/Eye 컴포넌트)는 현재 직접 자식(descendant) VECTOR **14개**를 가지며 전부 `#1a1a1a` fill을 보유한다 — 즉 A/B 분류표의 "14개"가 현재 라이브 값과 정확히 일치한다. 자식 ID를 대조한 결과, 원래 "6블록" 기록과 정확히 일치하는 6개(`281:399`~`281:404`, 좌표도 기존 기록의 "중앙 가로 바 1개(`x0,y4,w14,h2`) + 상단 코너 3개(`x2,y2`/`x6,y2`/`x10,y2`) + 하단 코너 2개(`x2,y6`/`x10,y6`)"와 정확히 동일)에, 원래 기록에는 없던 8개(`429:38`/`429:40`/`429:42`/`429:44`/`429:46`/`429:48`/`429:50`/`429:52`, x4~9·y1~7 구간에 밀집)가 추가로 존재한다.

**판단**: 브리프가 제시한 두 가능성 중, "단위 차이"(그룹 vs 하위 노드)가 아니라 **"둘 중 하나가 단순히 틀린 숫자"** 시나리오로 확인됐다 — 정확히는 브리프가 예시로 든 "원래 6블록 관찰 당시엔 정확했는데 이후 컴포넌트가 바뀐" 경우다. 근거: (1) 6블록 기록은 애초에 그룹화 구조가 아니라 개별 vector 6개를 그대로 나열한 것이었고 그룹-하위노드 관계가 존재하지 않는다, (2) 그 6개는 지금도 동일 ID·동일 좌표로 그대로 남아 있다, (3) 추가된 8개는 ID 번호대(`429:xx`)가 원본 6개(`281:39x`)보다 뚜렷하게 나중 생성 순번이라 원래 관찰(2026-07-14) 이후 추가된 것으로 판단된다. 따라서 두 숫자 모두 각자의 시점에서는 정확했지만, 2026-07-14 이후 컴포넌트 자체가 바뀌어 현재 정확한 값은 14다.

**정정 내용**: "6블록" 기록(2026-07-14 관찰 절)은 그 시점의 정확한 역사적 관찰이므로 좌표 목록 자체는 삭제하지 않고 그대로 남기되, 바로 위·아래에 "2026-07-17 재실측 결과 현재는 14개"라는 갱신 주석을 추가했다("PixelEyeOff 정식 등록 완료" 절, "Pixel/* 12종 상세" 표의 Pixel/Eye 행, A/B 분류표의 Pixel/Eye 행 — 총 3곳). A/B 분류표의 "descendant 14개"는 이미 정확한 값이었으므로 숫자 자체는 그대로 두고 근거 각주만 추가했다.

**값 출처**: `281:405`(Pixel/Eye) 자식 트리 전체 직접 재실측(`use_figma` 읽기 전용, 2026-07-17, fileKey `zgGlMBwFglaDlaeyP4CkgR`) — 임의 추측 없음.

## 상태: Icon/* 8종 Basic/Visual 트랙 재판정 + Basic 6종 재드로잉 지시 (2026-07-17, design-pl 브리프 — 사용자가 `Icon/User`를 직접 보고 지적한 것이 계기)

### 인계 문구 — 왜 방금 끝난 A/B 재바인딩을 또 건드리는가 (design-systems가 오인하지 않도록)

**바로 위 "Icons 페이지 색상 바인딩 전수 감사" 절에서 design-systems가 이미 fill(teal/amber, A그룹)·stroke(ink/900, B그룹) 재바인딩을 완료한 것을 라이브로 확인했다**(실측: 아래 표의 모든 요소가 이제 `bound: true`, 값도 `#1a1a1a`로 정정 완료 — 더 이상 `#1c1f21`이 아니다). 이번 라운드는 그 작업이 잘못됐다고 뒤집는 게 아니다. **두 라운드는 서로 다른 질문에 답한다**:
- 직전 라운드(색상 감사): "이 아이콘이 지금 갖고 있는 fill/stroke 값이 올바른 토큰을 정확히 가리키는가?" → 정확했다(A/B 분류 그대로 유효).
- 이번 라운드(트랙 재판정): "이 아이콘이 애초에 그 fill(면색)을 갖고 있어야 하는가, 아니면 순수 스트로크만 있어야 하는가?" → 사용자가 `Icon/User`(`96:45`)를 직접 보고 "라인형이 맞는 아이콘 같다"고 지적하며 이 질문이 처음 제기됐다. 확인해보니 `.claude/agents/graphic-designer.md`에는 애초부터 Basic/Visual 두 트랙 구분 규칙이 있었고(로그아웃=Basic, 카테고리/알림=Visual 예시로 이미 명시), 2026-07-17 "면색을 넣지 않는다" 문장이 명확화됐는데도 Icon/* 8종에는 한 번도 적용된 적이 없었다(위 "Basic(1.5px)/Visual(3px) 트랙 분리" 관련 절 — 그 원화는 2026-07-14 사용자가 페이지째 삭제해서 실행 전에 폐기된 이력이 있다).

즉 **색상 정확성(직전 라운드)과 트랙 여부(이번 라운드)는 서로 다른 층위의 결정**이라 순서대로 두 번 손대는 게 정상이다 — "방금 고친 걸 또 고친다"가 아니라 "방금 색상을 맞춰놨더니, 그 색상 자체(면색)를 아예 빼야 하는 아이콘이 6개 있다는 게 새로 밝혀졌다"는 흐름이다. design-systems는 아래 Basic 6종에 대해 (1) fill 바인딩을 제거하고 (2) stroke를 2px로 낮추는 작업을 하면 되며, 직전 라운드에서 한 색상 교정 작업 자체는 틀리지 않았다(오히려 stroke가 이미 `color/ink/900`로 정확히 바인딩돼 있어서, 이번 라운드는 fill만 제거하고 stroke weight만 낮추면 되는 상태 — 작업량이 오히려 줄었다).

### 판정 기준 (새로 발명하지 않음 — `.claude/agents/graphic-designer.md` 원문 그대로 적용)

- **Basic(기본) 트랙**: "화면 어디서나 자주 반복되고 그 자체로 브랜드를 표현할 필요가 없는 아이콘"(로그아웃/화살표/닫기/펼치기·접기가 원문 예시). 얇고 중립적인 스트로크(1.5~2px), **면색 없음 — 순수 스트로크만**.
- **Visual(비주얼) 트랙**: "카테고리, 알림처럼 브랜드 퍼스낼리티를 실제로 전달해야 하는 아이콘"(원문 예시 그대로). 굵은 잉크 아웃라인 + 브랜드색 평면 채색 유지.

### 8종 판정 결과

| 아이콘 | 트랙 | 판정 근거 |
|---|---|---|
| **Icon/Logout**(`96:36`) | **Basic** (agent doc 원문 예시 — 재발명 안 함) | 로그아웃은 화면 어디서나 반복되는 계정 액션이고 그 자체로 브랜드 개성을 전달할 필요가 없다. 실제로 확정 화면에서도 24px 버전은 안 쓰이고 대신 얇은 `Pixel/Logout`(11블록, 단색)이 헤더 버튼 안에 조용히 들어가 있다 — 실사용 처리 자체가 이미 "배경 소음"급 경량 취급이다. |
| **Icon/Category**(`96:31`) | **Visual** (agent doc 원문 예시 — 재발명 안 함) | 카테고리는 분류 의미를 색으로 전달해야 하는 자리(CatBadge 등 리스트 전반에서 색 코딩된 배지가 이미 핵심 정보 전달 장치, brand-guide 7번)라 브랜드 퍼스낼리티가 실제로 필요하다. |
| **Icon/Alert**(`96:41`) | **Visual** (agent doc 원문 예시 — 재발명 안 함) | 알림은 상태 강조가 핵심 기능이라 굵은 아웃라인+색이 그대로 맞다. Ellipse fill은 이미 `color/bg-cta-amber`에 정상 바인딩 완료 상태(위 절 참고) — 재작업 없음. |
| **Icon/Search**(`96:12`) | **Basic**(신규 판정) | 돋보기 실루엣은 어느 서비스에서나 동일한 범용 기호라 브랜드색 면 채움 없이도 의미가 100% 전달된다. 확정 화면에서도 24px판은 쓰이지 않고, 실제로 쓰이는 `Pixel/Search`(15×15)는 단색 실루엣 하나로만 그려져 있어 "굵은 아웃라인+면채색"이 아니라 얇고 조용한 처리가 이미 이 서비스의 실사용 관례다. |
| **Icon/Add**(`96:17`) | **Basic**(신규 판정) | "+" 배지는 이미 그 자체가 놓이는 컨테이너(추가 버튼 NeoBtn)가 두꺼운 2px 보더+하드 오프셋 그림자로 브랜드 개성을 담당한다(brand-guide 5번) — 아이콘 자체까지 면색으로 중복해 개성을 표현할 필요가 없다. `Pixel/Plus`도 2블록의 얇은 단색 처리다. |
| **Icon/Edit**(`96:22`) | **Basic**(신규 판정) | 연필 아이콘은 수정 액션의 범용 기호이고, row 단위로 반복되는 소형 액션(RowActionButton)에 쓰인다 — "자주 반복되고 그 자체로 브랜드를 표현할 필요가 없는" 원문 정의에 정확히 부합한다. 실사용 `Pixel/Edit`(17블록, 단색 잉크)도 굵은 아웃라인+면색이 아니다. |
| **Icon/Delete**(`96:27`) | **Basic**(신규 판정) | 휴지통 아이콘도 row 단위 반복 액션이며, 위험(destructive) 신호는 아이콘 자체의 색이 아니라 이미 컨테이너(RowActionButton Danger 보더, 삭제 확인 모달의 코랄 경고 박스·`Pixel/Warning`)가 전담하고 있다 — 아이콘 자체에 브랜드색 면 채움까지 얹을 필요가 없다. |
| **Icon/User**(`96:45`) | **Basic**(신규 판정, 이번 지적의 발단) | 사용자가 직접 지적한 아이콘. 실측 결과(아래 "Avatar 검토" 절) 이 아이콘의 fill(틸)은 Avatar 원 배경과 같은 색이라 원래도 "보이지 않는 면색"이었다 — 즉 실제로 시각적 정보를 전달하는 건 fill이 아니라 3px 잉크 stroke뿐이었다. fill을 완전히 제거해도 원래 렌더링 결과와 사실상 동일하고(오히려 최근 Avatar 원 배경이 스카이블루로 로컬 오버라이드되며 생긴 "틸 아이콘 vs 스카이블루 배경" 미묘한 색 불일치까지 해소된다), 사용자 인상("라인형이 맞는 아이콘")과 정확히 일치한다. 사람 실루엣이라는 형태 자체가 이미 범용 기호라 브랜드색 면 채움이 필요하지 않다는 점도 Search/Edit 등과 같은 논리다. |

**결론 요약**: Basic 6종 — Search·Add·Edit·Delete·Logout·User. Visual 2종(유지) — Category·Alert.

### Basic 6종 재드로잉 지시 — design-systems 실행용 (재질문 불필요하도록 노드 단위로 명시)

**공통 규칙(세트 내 일관성)**:
1. **두께**: `2px`로 확정(agent doc 허용 범위 1.5~2px 중 상단값 채택). 근거: 새 임의값을 만들지 않고 brand-guide 4번의 "보더 & Radius 스케일"에 이미 존재하는 **기본 컴포넌트 보더 2px** 값을 그대로 재사용했다 — Visual 트랙의 3px(구조적 강조선)보다 뚜렷이 얇으면서, 1.5px보다는 이 24px 그리드에서 시인성이 안정적이라 판단했다.
2. **색**: 새 원시값을 만들지 않고 이 세트가 이미 쓰고 있는 `color/ink/900`(#1a1a1a)을 그대로 재사용한다. 직전 라운드에서 이미 이 6종의 stroke가 `color/ink/900`으로 바인딩 완료된 상태이므로(라이브 재확인함), **stroke 바인딩 자체는 안 건드려도 된다** — weight 값만 3→2로 낮추면 색 작업은 끝난다.
3. **fill 제거 대상 = "주 실루엣" 도형만**(현재 `color/teal/500`에 바인딩된 fill을 가진 도형). fill을 제거하고(투명/없음), 같은 도형의 stroke weight를 3→2로 낮춘다. **벡터 path(외곽선 형태) 자체는 바꾸지 않는다** — 이번 라운드는 두께/면 채움 트랙 전환이지 형태 재설계가 아니다.
4. 이미 잉크 색 단독 fill로만 존재하는 "디테일" 도형(손잡이·+막대·화살표·연필촉 등, 아래 표의 "디테일" 행)은 원래도 브랜드색이 아니라 잉크색 얇은 요소였으므로 **그대로 둔다** — 새로 stroke를 추가하거나 폭을 조정하지 않는다.

**노드별 실행 표** (2026-07-17 `use_figma` 읽기 전용 재실측 — 라이브 상태 기준, 모든 stroke/detail fill이 이미 `color/ink/900` bound:true 확인 완료):

| 아이콘 | 주 실루엣(fill 제거 + stroke 3→2px) | 디테일(변경 없음) |
|---|---|---|
| Icon/Search(`96:12`) | Ellipse `96:9`(렌즈) | Handle Group(`96:10`) > Rectangle `96:11`(손잡이, ink fill만) |
| Icon/Add(`96:17`) | Rectangle `96:14`(배지) | Rectangle `96:15`/`96:16`(+ 막대 2개, ink fill만) |
| Icon/Edit(`96:22`) | Pencil Group(`96:19`) > Pencil Silhouette `96:20` | Pencil Group(`96:19`) > Rectangle `96:21`(연필촉, ink fill만) |
| Icon/Delete(`96:27`) | Rectangle 뚜껑 `96:24`, Rectangle 몸통 `96:26` | Rectangle 손잡이 `96:25`(ink fill만) |
| Icon/Logout(`96:36`) | Rectangle 문 `96:33` | Rectangle 화살표축 `96:34`, Arrow Head `96:35`(둘 다 ink fill만) |
| Icon/User(`96:45`) | Ellipse 머리 `96:43`, Ellipse 어깨 `96:44` | 없음(디테일 도형 없음, 2도형 전부 주 실루엣) |

**⚠ Icon/User 전용 추가 주의 — Avatar 인스턴스는 마스터 변경을 자동 상속하지 않는다**: 실측 결과 Avatar 인스턴스(`501:6370`)의 icon 자식 안 Ellipse 2개(`I501:6370;104:132;96:43`/`;96:44`)는 **로컬 오버라이드 상태(bound: false, 값은 마스터와 우연히 동일)**다. `Icon/User` 마스터(`96:45`)의 fill을 제거해도, 이 오버라이드가 걸린 인스턴스 속성은 마스터 변경을 자동으로 따라가지 않는다 — design-systems가 마스터 수정 후 **이 인스턴스의 fill 오버라이드도 별도로 초기화(Reset to master value)하거나 동일하게 fill 제거를 수동 적용**해야 실제 화면에도 반영된다. 이 단계를 빠뜨리면 "마스터는 고쳤는데 실제 화면(Avatar)은 그대로"인 상태가 남는다.

### Visual 2종(Category/Alert) — 유지 근거 재검토 결과

- **Icon/Category(`96:31`)**: 굵은 아웃라인+틸 면채색 유지가 맞다고 재확인했다. 근거: 이 프로젝트는 카테고리를 색으로 구분하는 CatBadge가 리스트 화면 전반의 핵심 정보 전달 장치(brand-guide 2번/7번)라, 폴더 아이콘도 같은 "색=분류 의미" 언어 안에 있어야 일관된다. fill은 이미 `color/teal/500`에 정확히 바인딩(A그룹, 재작업 불필요), stroke는 직전 라운드에서 `color/ink/900`으로 이미 재바인딩 완료 — 이번 라운드에서 형태·색 변경 없음.
- **Icon/Alert(`96:41`)**: 굵은 아웃라인+앰버 면채색 유지가 맞다고 재확인했다. 근거: 알림은 "지금 상태가 성공/에러"라는 걸 즉각 각인시켜야 하는 자리라 브랜드 퍼스낼리티(강조색)가 기능적으로 필요하다. Ellipse fill은 이미 `color/bg-cta-amber`에 정상 바인딩(위 절에서 확인 완료), 나머지 stroke·detail도 직전 라운드에서 `color/ink/900`으로 재바인딩 완료 — 이번 라운드에서 변경 없음.

**⚠ 2026-07-17 후속 정정 — Icon/Category "틸 유지" 판정을 뒤집고 sky/500으로 리바인딩함.** 위 "Icon/Category" 불릿의 결론(굵은 아웃라인+틸 면채색 유지)은 "raw teal 값이 유효한 토큰(`color/teal/500`)과 일치하는가"만 확인했을 뿐, "애초에 teal이 이 아이콘에 맞는 색인가"는 검증하지 않았다는 한계가 있었다 — 사용자가 Icon/Category를 블루 메인톤으로 바꿔달라고 직접 요청하며 이 한계가 드러났다. graphic-designer가 재조사한 결과: teal(#17a398)은 CatBadge 팔레트 안에서 "회사" 카테고리 전용 식별색으로 좁게 쓰이는 반면, sky/500(#1395e6, `VariableID:615:122`)은 이 세션에 걸쳐 Card 하단 스트립·Logo 배경 variant·Avatar 원 배경(29-8절) 등 "범용 브랜드/UI 크롬" 요소들이 공통으로 옮겨간 브랜드 메인톤이다. `Icon/Category`는 특정 카테고리(회사)가 아니라 "카테고리"라는 범용 개념을 나타내는 UI 크롬이므로 teal이 아니라 sky/500 버킷에 속하는 게 논리적으로 맞다고 재판단했다. design-systems가 이 판단에 따라 `96:29`/`96:30`의 fill을 `color/teal/500`→`color/sky/500`으로 리바인딩 완료(신규 토큰 없음, 기존 sky/500 재사용), stroke(`color/ink/900`)는 무수정. 상세 실측·재대조 기록은 `docs/design/design-system.md` 30절 참고.

### Avatar(`104:131`) 검토 — Icon/* 판정과 독립적으로 판단, 새로운 실측 발견 포함

**구조 실측(읽기 전용, `use_figma`)**: Avatar는 단순히 Icon/User를 확대한 게 아니라 2겹 구조다 — ① Avatar 컴포넌트(`104:131`) 자신이 원형 배경 fill(`color/teal/500` 바인딩)을 갖는 프레임이고, ② 그 안에 `icon`이라는 이름의 **Icon/User INSTANCE**(`104:132`)가 자식으로 들어가 있다. 즉 "아바타 원 배경"과 "사람 실루엣 아이콘"은 서로 다른 두 레이어다.

**새 발견 — 마스터와 실제 화면 인스턴스의 원 배경 색이 다르다(위 "색상 바인딩 전수 감사" 절의 Avatar 결론을 부분 정정)**:
- Avatar 마스터(`104:131`) 자신의 fill: `#17a398`(틸), `color/teal/500`에 정상 바인딩(bound: true). **⚠ 2026-07-17 갱신 각주**: 이 "정상 바인딩(bound: true)" 서술은 이 절 작성 시점(당시) 기준으로는 정확했던 관찰이다. 같은 날 이후 별도 라운드(design-system.md 29-8절)에서 `component/avatar-bg` 토큰의 alias 자체가 `color/teal/500`→`color/sky/500`으로 교체되며 마스터 fill도 스카이블루(`#1395e6`)로 갱신됐다 — 바인딩 상태는 여전히 정상(bound: true)이고 alias 대상만 바뀐 것이다. 원문(틸 값)은 삭제하지 않고 그대로 보존한다.
- 확정 화면 실제 인스턴스(`501:6370`) 자신의 fill: **`#1395e6`(스카이블루)**, **바인딩 없음(로컬 오버라이드, bound: false)**.
- 위 절의 "Avatar는 신 세대에도 여전히 틸"이라는 결론은 **아이콘 글리프(머리/어깨 Ellipse)의 색만 확인한 것**이었다(그 색은 실제로 여전히 틸 `#17a398`, 마스터와 값 일치 — 이 부분은 정확했다). 이번 라운드에서 Avatar 컴포넌트 자신의 원 배경 fill을 별도로 재조회하니, 실제 화면에서는 마스터와 다르게 **스카이블루로 로컬 오버라이드돼 있었다** — 즉 지금 확정 화면의 아바타는 "스카이블루 원 배경 + 틸 사람 실루엣(ink 3px 아웃라인)"이 실제 라이브 상태다. 이건 이번 브리프 범위(Basic/Visual 트랙 판단)를 벗어나는 색상 바인딩 불일치 발견이라 여기서 직접 고치지 않는다 — design-pl에게 이 사실을 그대로 보고해 design-systems의 다음 색상 바인딩 라운드에서 처리하도록 넘긴다(Avatar를 스카이블루로 통일할지, 마스터처럼 틸로 되돌릴지는 이번 브리프가 결정할 문제가 아니다).

**Avatar 자체의 트랙 판단(Icon/* 8종과 독립)**: Avatar 원 배경의 색 채움 자체는 **유지**가 맞다고 판단한다. 근거: brand-guide 1번이 이 서비스의 포지셔닝을 "로그인 사용자별 데이터 격리(신뢰 요소)를 시각적 경계로 드러낸다"고 명시하는데, 이 신뢰 요소를 실제로 시각화하는 자리가 바로 Avatar의 색 채움이다(사용자 식별용 컬러 코딩) — Category/Alert처럼 "색 자체가 의미를 나른다"는 성격이라 Basic 트랙의 "브랜드 표현이 필요 없는 반복 유틸리티"에 해당하지 않는다. 다만 원 배경 위에 얹히는 **사람 실루엣 자체(Icon/User 인스턴스)**는 위 판정대로 Basic(면색 제거, stroke 2px)이 맞다 — 이 둘은 모순이 아니라 자연스러운 조합이다: "색으로 신원을 표시하는 배경 원" 위에 "형태로만 사람을 나타내는 얇은 잉크 실루엣"이 얹히는 구조가, 오히려 지금의 "배경과 거의 같은 색이라 실루엣이 잘 안 보이는" 상태보다 대비가 또렷해져 더 낫다.

### 요약 (design-systems 실행 순서)

1. Icon/Search·Add·Edit·Delete·Logout·User 6종: 위 "노드별 실행 표"의 "주 실루엣" 도형 fill 제거 + stroke weight 3→2px(색 바인딩은 이미 `color/ink/900`으로 완료돼 있어 그대로 둔다). "디테일" 도형은 무변경.
2. Icon/User 마스터 수정 후, Avatar 인스턴스(`501:6370`)의 icon 자식 오버라이드도 함께 초기화/동일 반영(위 "Icon/User 전용 추가 주의" 참고) — 빠뜨리면 화면에 반영 안 됨.
3. Icon/Category·Alert 2종: 무변경(유지 근거만 재확인 완료).
4. Avatar 원 배경(마스터 틸 vs 인스턴스 스카이블루 불일치)은 이번 라운드 범위 밖 — design-pl에게 별도 보고, 이 브리프에서 결정하지 않음. **⚠ 2026-07-17 갱신 각주**: 이 미결정 상태는 같은 날 메인 세션의 신뢰 형식 명시 승인으로 해소됐다 — `component/avatar-bg` 토큰이 `color/teal/500`→`color/sky/500`으로 리바인딩되어 마스터·인스턴스 모두 스카이블루로 통일됐다. 원문(미결정 서술)은 삭제하지 않고 그대로 보존하며, 상세 경위는 `docs/design/design-system.md` 29-8절 참고.
5. 벡터 형태(path) 자체는 이번 라운드에서 전혀 바꾸지 않았다 — fill 제거·strokeWeight 변경·바인딩 재확인만 대상.

**값 출처**: `.claude/agents/graphic-designer.md`(Basic/Visual 트랙 정의 원문), `docs/design/brand-guide.md`(1번 포지셔닝, 4번 보더 스케일, 7번 장식 모티프/CatBadge), Icons 페이지(`96:7`) Icon/* 8종 전체 자식 노드 실측(`use_figma` 읽기 전용, fill/stroke hex·bound 상태·strokeWeight), Avatar 컴포넌트(`104:131`)·인스턴스(`501:6370`) 및 그 icon 자식 실측(`use_figma` 읽기 전용, `getMainComponentAsync`로 Icon/User 연결 확인), `get_screenshot`(Icons 페이지 전체, Avatar 마스터/인스턴스 개별) — 임의 근사치 없음.

## 상태: Pixel/Search 색상 검증 — teal/500 → sky/500 리바인딩 확인·승인 (2026-07-17, 메인 세션 직접 실측 → design-pl 브리프)

### 배경

메인 세션(사용자)이 확정 디자인의 실제 검색 아이콘 인스턴스 `PxSearch`(`501:6390`, 확정 main 프레임 안)를 직접 실측해, 13개 벡터 전부가 `#1395e6`(sky/500)임을 확인했다. 반면 등록된 마스터 컴포넌트 `Pixel/Search`(`255:26`)는 위 "Icons 페이지 색상 바인딩 전수 감사" 절에서 13개 벡터 전부 `color/teal/500`에 바인딩된 것으로 이미 실측·기록돼 있었다(A그룹 판정, "값 그대로 일치, 재해석 불필요"로 결론 — **이 결론은 확정 디자인 인스턴스 자체와 직접 대조하지 않은 상태에서 내려진 것이었다**). 로그인/main 등 여러 확정 프레임에 걸쳐 일관되게 sky라 인스턴스별 오버라이드가 아니라 마스터 컴포넌트 자체의 색상 바인딩 오류로 판단된다. 메인 세션이 이 수정을 신뢰 형식으로 승인했다 — 신규 토큰 없이 기존 `color/sky/500`을 그대로 재사용.

이번 라운드는 **확인·판정까지만**이다. 실제 Figma 리바인딩(마스터 `255:26`의 13개 벡터 fill을 `color/teal/500`→`color/sky/500`으로 변경)은 design-systems가 다음 단계에서 실행한다 — graphic-designer는 벡터를 직접 수정하지 않았다(읽기 전용 재실측만).

### 1. 형태(패스/구조) 동일성 확인

`use_figma` 읽기 전용으로 확정 프레임 안 `PxSearch`(`501:6390`)와 마스터 `Pixel/Search`(`255:26`)를 나란히 실측했다:

- 프레임 크기: 둘 다 15×15, 자식 개수 둘 다 정확히 13개(VECTOR).
- 13개 벡터를 순서대로 1:1 대조한 결과, **x/y/width/height/vectorPaths가 소수점 단위까지 완전히 동일**하다(예: 렌즈 몸통 `x=3.214,y=2.143,w=6.429,h=7.5`, 렌즈 상단 바 `x=3.214,y=1.071,w=6.429,h=1.071`, 손잡이 코너 블록 `x=12.857,y=12.857,w=2.143,h=2.143` 등 13개 전부 일치). `strokeWeight`(fills 전용 도형이라 실질적으로 의미 없는 값)까지 동일했다.
- **결론: 형태는 100% 동일하다 — 색상 외에는 어떤 차이도 없다.** 별도 형태 이슈로 보고할 사항 없음.

### 2. 트랙 판정 — Basic/Visual 이분법이 아니라 Pixel/* 고유 언어 적용

`docs/harness/design-team/icon-craft-guide.md`의 Basic(면색 없음, 스트로크만)/Visual(굵은 아웃라인+면채색) 구분은 **Icon/* 24px 스트로크 기반 트랙에 적용되는 기준**이다. `Pixel/Search`는 그 트랙이 아니라 위 "Pixel 마이크로 아이콘 12종" 절에서 이미 별도로 분리해둔 **Pixel/* 마이크로 픽셀 아이콘 트랙**(8~15px, 13개의 작은 정사각형 vector 블록을 이어붙인 단색 실루엣, 스트로크 개념 자체가 없음)에 속한다 — 이 판단은 이번에 새로 내리는 게 아니라 기존 문서 판단을 그대로 계승한다.

Pixel/* 트랙은 Pixel/Close·Pixel/Check 2건의 예외(단일 stroke-vector 구성)를 빼면 전부 "13개/17개/39개 등 다수의 solid-fill 블록"으로 구성되며, 이 solid-fill 방식은 **Basic 의도(범용·저채도 반복 기호)로 쓰이는 아이콘(Pixel/Search, Pixel/Plus, Pixel/Edit, Pixel/Logout)이든 Visual 의도로 쓰이는 아이콘(Pixel/Warning, Pixel/NoResult)이든 구조적으로 동일하다** — 즉 Pixel/* 트랙 안에서는 "면색 유무"가 Basic/Visual을 가르는 구조적 신호가 아니다(Icon/* 8종 재판정 때와 달리, fill을 아예 제거하는 선택지 자체가 이 트랙의 스타일 언어에 없다). 실제로 Icon/Search(24px 형제)는 이번 세션 다른 라운드에서 Basic 판정을 받아 fill 제거+stroke 2px로 재드로잉이 지시됐지만, 그건 Icon/* 트랙 한정 조치였고 Pixel/Search(15×15, 별도 트랙)에는 애초에 적용 대상이 아니었다.

**판정**: `sky/500`으로의 리바인딩은 13개 vector의 fill 존재 자체(블록 실루엣 구성), strokeWeight, 형태(vectorPaths)를 전혀 바꾸지 않는 **단일 색상 토큰 교체**다. 이는 Pixel/* 트랙의 스타일 언어(단색 블록 실루엣) 어디에도 어긋나지 않는다 — 트랙 규칙 위반 없음.

### 3. 13개 벡터 전수 바인딩 확인

`use_figma`로 마스터 `255:26`의 자식 13개를 전부 순회해 `fills[0].color`와 `boundVariables.fills[0]`를 개별 조회했다. **13개 전부 예외 없이 `#17a398` + `boundVariables.fills[0]` → 변수명 `color/teal/500`**로 확인됐다(노드 ID `255:13`~`255:25`). 값이 다르거나 미바인딩인 벡터, 즉 "일부만 다른 값"인 벡터는 하나도 없었다 — 완전히 균일한 teal/500 바인딩이다.

대조군인 확정 `PxSearch`(`501:6390`)의 13개 벡터(`501:6391`~`501:6403`)도 전부 예외 없이 raw `#1395e6`(unbound, 확정 프레임 특성상 변수 미바인딩 상태 — 다른 확정 프레임 원본 요소들과 동일한 패턴)로 확인됐다.

### 4. 브랜드 톤 재해석 여부 — 순수 오류 정정으로 판정

이 변경은 **브랜드 톤을 새로 재해석하는 결정이 아니라 순수 오류 정정**이다. 근거:

1. **확정 디자인 자체가 이미 sky를 쓰고 있다.** 이번 판단은 "어느 색이 더 브랜드에 맞는가"를 새로 고민하는 게 아니라, 이미 확정된 원본(`501:6390`)의 실측값을 마스터가 반영하지 못하고 있던 상태를 마스터 쪽에 맞추는 것이다 — Pixel/NoResult가 이미 2026-07-16에 동일한 사유(teal→sky/500)로 리바인딩된 전례(design-system.md 23절 B)와 정확히 같은 성격의 조치다.
2. **기존 세션 전반의 teal→sky 전환 패턴과도 일치한다.** 위 "Icon/* 8종 Basic/Visual 트랙 재판정" 절 말미에서 `Icon/Category`가 "회사 카테고리 전용 식별색(teal)"과 "범용 브랜드/UI 크롬(sky/500)"을 구분해, 검색·카드·로고·아바타처럼 특정 카테고리 정체성이 아닌 범용 UI 요소는 sky/500 버킷에 속한다고 이미 정리해뒀다. `Pixel/Search`는 검색창의 범용 leading icon으로, 특정 카테고리 식별색이 필요한 자리가 아니라 이 sky/500 버킷(Card 스트립·Logo·Avatar bg·Pixel/NoResult와 동일 계열)에 정확히 부합한다.
3. **다른 아이콘과의 색상 일관성에 미치는 영향도 없다.** teal/500은 이 리바인딩 이후로도 CatBadge의 "회사" 카테고리 식별색, Icon/User(Avatar 글리프) 등 각자의 좁은 스코프에서 계속 유효하게 쓰인다 — Pixel/Search 하나를 sky로 바꾼다고 다른 아이콘들의 teal 사용이 흔들리거나 재검토가 필요해지지 않는다.
4. **신규 토큰을 만들지 않는다** — 이미 존재하고 이미 여러 요소(Card 스트립, Logo 배경, Avatar bg, Pixel/NoResult, Icon/Category)에 쓰이고 있는 `color/sky/500`을 그대로 재사용하므로, 팔레트 확장이나 새로운 스타일 결정이 아니다.

### 결론

- 형태 100% 동일 확인, 별도 형태 이슈 없음.
- 트랙 규칙(Pixel/* 마이크로 픽셀 아이콘, 단색 블록 실루엣) 위반 없음 — 색상 토큰 교체만으로 트랙 언어가 바뀌지 않는다.
- 13개 벡터 전수 `color/teal/500` 균일 바인딩 확인, 예외 없음.
- 브랜드 톤 재해석이 아니라 순수 오류 정정이며, 오히려 세션 전반의 sky/500 UI 크롬 통일 패턴과 일치한다.
- **위 "A/B 분류표 — Pixel/* 12종"의 Pixel/Search 행(구 판정: A, `color/teal/500`)은 이 검증으로 대체된다 — 최신 유효 판정은 이 절이다.**

**리바인딩 승인, design-systems 진행 가능.** 실행 대상: 마스터 `Pixel/Search`(`255:26`)의 자식 벡터 13개(`255:13`~`255:25`) fill을 `color/teal/500`에서 `color/sky/500`으로 재바인딩(신규 토큰 없음, 기존 토큰 재사용). vectorPaths·strokeWeight·프레임 크기 등 형태 속성은 전혀 변경하지 않는다.

**값 출처**: 확정 `PxSearch`(`501:6390`) 및 마스터 `Pixel/Search`(`255:26`) 자식 13개 전수 직접 실측(`use_figma` 읽기 전용, fileKey `zgGlMBwFglaDlaeyP4CkgR`, 2026-07-17) — 임의 근사치 없음.

### 리바인딩 실행 완료 (2026-07-17, design-systems)

위 승인에 따라 design-systems가 실제 Figma 리바인딩을 실행했다. 마스터 `Pixel/Search`(`255:26`)의 자식 벡터 13개(`255:13`~`255:25`) 전부의 fill을 `figma.variables.setBoundVariableForPaint`로 `color/teal/500`(`VariableID:95:6`)에서 `color/sky/500`(`VariableID:615:122`, #1395E6)으로 재바인딩했다. vectorPaths·strokeWeight·프레임 크기(15×15) 등 형태 속성은 전혀 변경하지 않았다.

**전수 재검증(13개 전부, 일부만 확인하고 넘어가지 않음)**: 리바인딩 직후 13개 전부를 재조회한 결과 예외 없이 `fills[0].color ≈ {r:0.0745,g:0.5843,b:0.9020}`(`#1395e6`) + `boundVariables.fills[0].id === "VariableID:615:122"`(`color/sky/500`)로 확인. `get_screenshot`으로 최종 렌더 확인: 스카이블루 단색 실루엣 돋보기 아이콘으로 정상 렌더링됨(형태는 이전과 동일, 색만 변경).

**인스턴스 전파 확인**: Icons(`96:7`)·Component Specs(`342:2`)·Input(`100:2`)·파일럿(`222:524`)·UI-design(`15:3`) 5개 페이지를 전수 검색한 결과 `mainComponent.id === '255:26'`인 INSTANCE는 **0건** — 확정 프레임의 `PxSearch`(`501:6390`)는 다른 확정 프레임 원본 요소들과 동일하게 raw FRAME(컴포넌트 인스턴스 연결 없음)이라, 이 마스터를 참조하는 실사용 인스턴스가 파일 어디에도 없다(전파 확인할 대상 자체가 없음, 결함이 아니라 예상된 정상 상태).

**최종 값**: `Pixel/Search`(`255:26`) 13개 벡터 fill = `color/sky/500`(#1395E6). 위 "Pixel/* 12종 상세" 표의 Pixel/Search 행과 위 "A/B 분류표 — Pixel/* 12종"의 Pixel/Search 행 서술("리바인딩 승인")과 이 절의 결론이 이제 완전히 일치한다 — 두 문서(이 문서와 `docs/design/design-system.md` 32절) 서로 다른 결론을 가리키지 않는다.

## 상태: Primary/Secondary/Accent 역할 재확정 반영 — "주 평면 채색 Primary 틸" 표현 정정 (2026-07-17, harness-auditor 발견 MEDIUM / 사용자 승인)

design-system.md 33절("Primary/Secondary/Accent 역할 재평가", 확정 프레임 `501:2505` 8개 fill+stroke 면적 실측)에서 브랜드 컬러 위계가 재확정됐다: Primary는 스카이블루(`color/sky/500`, 신규 편입)로, 틸은 Primary에서 완전히 제외되어 "카테고리 식별색(narrow)"으로 좁게 재정의됐다. 이 결론은 `docs/design/brand-guide.md`·`docs/design/confirmed/user-confirmed-final-design.md`·`docs/design/design-system.md`에는 이미 반영됐으나, 이 문서(graphic-assets.md)의 30번째 줄 근처 "색상 규칙" 문장("주 평면 채색 Primary 틸 `#17A398`")은 소유권 밖이라 그때 정정하지 않고 넘어갔었다(harness-auditor MEDIUM 지적, 사용자 승인).

**정정 내용**: 위 "현재 실존하는 기능 아이콘 8종" 절의 "색상 규칙" 문장 아래에 "⚠ 2026-07-17 재갱신" 각주를 기존 "⚠ 2026-07-17 갱신" 각주에 이어 추가했다. 이 문서의 기존 관행(원문을 삭제하지 않고 각주로 덧붙이는 방식, 5/13/28/30행에 이미 여러 번 쓰인 패턴)을 그대로 따랐다 — 원문("주 평면 채색 Primary 틸 `#17A398`")은 삭제하지 않고 그대로 보존했다.

**각주가 명시하는 내용**: (1) "주 평면 채색 Primary 틸"이라는 원문의 역할 명칭 표현은 더 이상 최신이 아니다. (2) 최신 결론(design-system.md 33절 근거): Primary는 스카이블루(`color/sky/500`)로 재확정됐고, 틸은 "카테고리 식별색(narrow)"으로 역할이 좁혀졌다(CatBadge 회사 보더/닷 + row 수정 액션 아웃라인만 남음). (3) 이 각주는 문장 자체의 낡은 역할 명칭만 정정하는 것이지, 이 문서 안에 이미 실측·기록된 개별 Icon/*·Pixel/* 아이콘의 실제 fill 값이나 A/B 분류 판정(146번째 줄 이하 "Icons 페이지 색상 바인딩 전수 감사" 절, 그 이후 "Icon/* 8종 Basic/Visual 트랙 재판정" 절 등)을 뒤집는 게 아니다 — "아이콘이 틸을 쓴다"는 관찰(아이콘 크래프트 층위)과 "틸이 브랜드 Primary 배경색이다"는 주장(브랜드 역할 층위)은 서로 다른 층위이며, 이번 각주는 후자만 정정한다.

**하단 절들과의 모순 여부 확인 결과 — 모순 없음, 오히려 이미 정합적으로 수렴돼 있었다**: 파일 전체(146번째 줄 이후 "Icons 페이지 색상 바인딩 전수 감사" 절, "Icon/* 8종 Basic/Visual 트랙 재판정" 절, "Pixel/Search 색상 검증" 절)를 다시 읽어 이번 각주와 문면이 어긋나지 않는지 확인했다:

1. **"Icons 페이지 색상 바인딩 전수 감사" 절(152행)은 이미 "Stage2에서 Primary 브랜드색이 다수 요소에서 틸→스카이블루로 전환됐다"고 명시하고 있다** — 이번 각주의 결론(Primary=스카이블루)과 방향이 일치한다. 다만 이 절은 그 전환을 "전면 전환이 아니다"·"특정 요소에 한정된 선택적 전환"(202행)이라는, 33절 재평가 이전 시점의 좁은 프레이밍으로 서술하고 있다 — 이 프레이밍 자체는 33절의 더 포괄적인 재확정과 정확히 같은 온도는 아니지만, 이로 인해 **이 절이 도출한 개별 결론(A/B 분류, 노드별 hex 값)이 틀리게 되는 것은 아니다**(아래 3번 참고).
2. **"Icon/* 8종 Basic/Visual 트랙 재판정" 절은 이미 이 문서 내부에서 스스로 틸→스카이블루 수렴을 완결해뒀다.** 이 절의 흐름을 끝까지 추적한 결과, 이 문서에 등장하는 Icon/*·Pixel/* 컴포넌트 중 현재 시점에 실제로 "Primary 역할의 틸 fill"을 유지하고 있는 요소는 하나도 없다:
   - Icon/Search·Add·Edit·Delete·Logout·User 6종은 Basic 트랙으로 재판정되어 틸 fill이 제거 대상으로 지시됐다(면색 자체가 없어짐, 267~299행).
   - Icon/Category는 "틸 유지" 결론이 한 번 더 뒤집혀 sky/500으로 리바인딩 완료됐다(308행 각주).
   - Avatar 원 배경도 `component/avatar-bg` 토큰이 sky/500으로 리바인딩 완료됐다(315행, 326행 각주).
   - Pixel/NoResult(2026-07-16)·Pixel/Search(맨 아래 절)도 이미 sky/500으로 리바인딩 완료됐다.
   - 남아있는 유일한 라이브 틸 값은 Icon/User 아이콘 글리프(사람 실루엣) 자체인데, 이마저도 위 6종 재판정에 포함돼 fill 제거(투명, stroke만 유지) 대상이다.
   즉 **이 문서의 내부 서술은 이미 "Primary는 틸이 아니다"는 결론 쪽으로 스스로 수렴해 있었다** — 이번 각주가 뒤집어야 할 하위 절의 "현재 유효" 결론은 발견되지 않았다.
3. **A/B 분류표(183~223행)의 개별 "A그룹, `color/teal/500`" 판정 자체는 뒤집을 필요가 없다.** 그 표는 "당시 라이브 fill 값이 어떤 토큰과 일치하는가"(색상 정확성 층위)를 판단한 것이지 "그 fill을 애초에 가져야 하는가"(트랙/역할 층위)를 판단한 게 아니다 — 이 구분은 204행 각주가 이미 명시적으로 못박아 둔 내용이라, 이번 Primary 역할 재정의 각주와도 동일한 논리로 무모순이다.

**발견사항(참고용, 이번 브리프 범위 밖 — 수정하지 않음)**: 152행·202행의 "Stage2 틸→스카이블루 전환은 특정 요소에 한정된 선택적 전환, 전면 치환 아님"이라는 **프레이밍 문장 자체**는 33절의 더 포괄적인 재확정("Primary=스카이블루로 완전히 재확정, 틸은 narrow 카테고리 식별색으로 좁혀짐")과 견주면 다소 예전 시점의 온도로 읽힌다. 다만 이 프레이밍에서 도출된 하위 결론(개별 노드 hex 값, A/B 바인딩 판정)은 위 2·3번처럼 이미 다른 후속 절에서 전부 갱신·수렴됐기 때문에, 현재 문서에 실질적으로 잘못된 "살아있는" 값이나 지시는 남아있지 않다. 이 프레이밍 문장 자체를 추가로 각주 처리할지는 이번 브리프 범위(30행 정정)를 넘는 문서 정리이므로, design-pl 판단 사안으로만 남긴다.

**값 출처**: `docs/design/design-system.md` 33절(Primary/Secondary/Accent 역할 재평가) 및 이 문서 자체의 146행 이후 전체 재독 — 신규 Figma 실측 없음(순수 문서 서술 정정, 문서 내부 정합성 재확인).

## 상태: Auth 페이지(`934:2`) BgPixels/ConfettiFooter 컨페티 오브제 불투명도 결함 수정 완료 (2026-07-17, 사용자 이슈 제보 → 직접 수정)

### 배경 — 사용자 제보와 조사 범위

사용자가 "로그인 화면 뒤에 bg의 블루배경에 있는 오브제들의 컬러가 달라"라고 별도 이슈를 제보하며 Figma 노드 `934:2` 확인을 요청했다. 이건 "누락 8개 화면 조립" 라운드와 무관한 별개 트랙이다.

`get_metadata`로 `934:2`를 조사한 결과, 이 노드는 프레임이 아니라 **"Auth"라는 이름의 캔버스(페이지)** 였다 — 그 아래 `Join`(`935:33`)·`login`(`936:1042`)·`login-알림창`(`936:1191`) 3개 프레임을 담고 있다. 각 프레임은 `BgPixels`(전역 컨페티 산포, brand-guide 7번)와 카드 내부 `ConfettiFooter`(카드 하단 컨페티 한 줄) 두 장식 블록을 갖고 있고, Logo/CornerInput/Button/Checkbox/Link 등 이미 등록된 컴포넌트 INSTANCE로 조립돼 있었다 — 즉 이 페이지는 **사용자가 Figma에서 직접 만든 "확정 디자인 - 절대 원본 건들지 말것-" 원본이 아니라, 그 원본을 컴포넌트로 재조립한 파생 SCREENS 페이지**다(확정 원본의 Join/login/login-알림창 nodeId는 각각 `501:4692`/`501:4940`/`501:5188`로 완전히 다르다 — `docs/design/confirmed/user-confirmed-final-design.md` "확정된 8개 프레임" 표 참고). 따라서 보호 라벨 대상이 아니며, 그래픽 크래프트 도메인 안에서 직접 수정 가능하다고 판단했다.

### 실측 — 무엇이 "색이 다르게" 보였는가

`use_figma` 읽기 전용으로 `BgPixels`의 자식 14개(다이아몬드=회전된 Rectangle, 십자=Rectangle 2개를 담은 Frame, 별=`Pixel/Star` INSTANCE) 전부의 fill·boundVariables·opacity를 순회했다:

- **fill 색 자체는 문제 없었다** — 다이아몬드·십자·별 전부 `color/ink/900`(`VariableID:95:9`, `#1a1a1a`)에 정확히 바인딩돼 있었다. 색상 토큰 불일치가 아니다.
- **실제 결함은 opacity였다.** `Pixel/Star` INSTANCE 5개는 인스턴스 레벨에 0.25~0.4의 랜덤한 불투명도가 이미 정확히 걸려 있어 brand-guide 7번의 "8~20px 크기, 25~40% 불투명도로 무작위 산포" 스펙과 일치했다. 하지만 다이아몬드(Rectangle) 5개와 십자(Frame) 4개는 **전부 opacity 1(완전 불투명)** 이었다 — 즉 같은 잉크 색인데 별만 반투명한 회청색 톤으로 옅게 보이고, 다이아몬드·십자는 완전 불투명한 검정으로 도드라져 보여 사용자에게 "색이 다르다"는 인상을 준 것이다. `ConfettiFooter`(카드 하단 한 줄, Rectangle 3개+`Pixel/Star` 2개)는 brand-guide 7번 스펙("Diamond/Star 5개를 25% 불투명도로")과 반대로 5개 전부 opacity 1이었다 — 여기는 별조차 예외 없이 완전 불투명 상태였다. 이 패턴은 `Join`/`login`/`login-알림창` 3개 프레임 전부에서 동일하게 재현됐다(각 프레임 BgPixels 9개 + ConfettiFooter 5개 = 14개 노드씩, 총 42개).

### 판단 — 토큰 리바인딩이 아니라 직접 수정 대상

fill 자체(`color/ink/900` 바인딩)는 이미 올바르므로 이번 결함은 "이미 등록된 색상 토큰의 리바인딩"이 아니다. opacity는 raw 노드 속성이고 변수 바인딩 대상이 아니었다(boundVariables에 opacity 항목 없음, Figma의 불투명도는 별도 variable-bindable 속성이 아니라 리터럴 값으로만 존재) — 즉 색상 정확성/토큰 문제가 아니라 순수 장식 오브제의 조형 속성(불투명도) 결함이라, design-systems 경유 없이 이 도메인(그래픽 크래프트)에서 직접 수정했다.

### 수정 내용

`use_figma`로 3개 프레임(Join/login/login-알림창) 각각의 BgPixels·ConfettiFooter를 순회해 총 42개 노드의 opacity를 조정했다:
- **BgPixels 다이아몬드+십자 9개/프레임**(별 5개는 이미 정상이라 제외): brand-guide 7번의 25~40% 범위 안에서 0.4/0.3/0.35/0.25를 순환 배정해 인접 별들과 동일한 무작위 산포 느낌을 재현(형태·색·회전각은 전혀 변경하지 않음).
- **ConfettiFooter 5개/프레임**(다이아몬드 3+별 2, 전부): brand-guide 7번 스펙 그대로 **0.25**로 통일.
- 형태(vectorPaths/rotation)·fill 색·boundVariables는 전혀 건드리지 않았다 — opacity 속성만 변경.

`get_screenshot`(login 프레임, base64 inline)으로 수정 전/후를 비교 확인: 수정 후 다이아몬드·십자·별이 배경 위에서 톤 일관된 반투명 잉크색 산포로 통일됐고, 카드 하단 컨페티 푸터도 옅어져 spec대로 은은한 장식으로 보임을 확인했다.

**전달 대상**: 없음(직접 완료). design-pl 참고용으로만 보고 — 확정 원본을 건드린 게 아니라 파생 SCREENS 페이지의 장식 오브제 조형 결함을 그래픽 크래프트 권한 안에서 직접 고쳤다.

**값 출처**: Auth 페이지(`934:2`) `get_metadata` 구조 확인, BgPixels/ConfettiFooter 전체 42개 노드 fill/opacity/boundVariables 실측(`use_figma` 읽기 전용 → 수정), `docs/design/brand-guide.md` 7번(장식 모티프 불투명도 스펙), `docs/design/confirmed/user-confirmed-final-design.md`(확정 원본 nodeId 대조, 934:2가 원본이 아님을 확인한 근거) — 임의 근사치 없음.

## 상태: Auth 페이지(`934:2`) BgPixels 컬러 자체 오류 정정 완료 — 이전 라운드가 놓친 진짜 결함 (2026-07-17, 사용자 3차 재확인 → 전수 hex 재실측 → 직접 수정)

### 배경 — 왜 또 같은 자리를 재작업하는가

바로 위 절("불투명도 결함 수정 완료")에서 opacity만 고치고 "fill 색 자체는 문제 없었다"고 결론 내렸으나, 사용자가 재확인한 결과 **컬러 자체가 여전히 원본과 다르다**고 재차 지적했다(오늘 세 번째 재확인 요청). 원인은 이전 라운드가 다이아몬드/십자/별의 fill이 "`color/ink/900`에 바인딩돼 있다"는 사실만 확인하고, **그 바인딩된 값 자체가 원본과 맞는 색인지는 원본과 직접 대조하지 않았다**는 데 있었다 — "바인딩이 정상이다"와 "그 색이 원본과 같은 색이다"는 서로 다른 질문인데 전자만 확인하고 후자를 생략한 것이 이번 재작업의 원인이다.

### 실측 — 원본(정답) vs 문제(잘못된 예)

**원본 실측(`use_figma` 읽기 전용, 확정 login 프레임 `501:4940` 하위)**: BgPixels 전역 산포 오브제와 카드 내부 ConfettiFooter가 **서로 다른 색 체계**를 쓰고 있음을 처음으로 확인했다:

| 위치 | 오브제 | 원본 hex | 근거 노드 |
|---|---|---|---|
| BgPixels(블루 배경 위 전역 산포) | PixelDiamond | **흰색 `#ffffff`** | `501:4944`~`501:4951`(7 vector) |
| BgPixels(블루 배경 위 전역 산포) | PixelCross | **흰색 `#ffffff`** | `501:4963`/`501:4964`(2 vector) |
| BgPixels(블루 배경 위 전역 산포) | PixelStar | **앰버 `#ffce2c`** | `501:4954`~`501:4960`(7 vector) |
| ConfettiFooter(카드 안, 흰 배경 위) | PixelDiamond | 잉크 `#1a1a1a` | `501:5145`~`501:5151`(7 vector) |
| ConfettiFooter(카드 안, 흰 배경 위) | PixelStar | 잉크 `#1a1a1a` | `501:5153`~`501:5159`(7 vector) |

즉 원본은 "배경이 블루면 흰색/앰버로 도드라지게, 배경이 흰 카드 안이면 잉크로 은은하게"라는 **배치 위치에 따른 의도된 2색 체계**였다 — 다이아몬드/십자는 항상 흰색, 별만 앰버라는 규칙도 이번에 처음 확인했다.

**문제(잘못된 예) 실측(934:2 페이지 8개 프레임 전체, `use_figma` 읽기 전용)**: `935:33`(Join)/`936:1042`(login)/`936:1191`(login-알림창)/`995:303`/`996:376`/`996:2575`/`996:2713`/`996:3014` 전 프레임에서 BgPixels의 다이아몬드(40개)·십자(32개, 64 vector)·별(40개 인스턴스, 320 vector)이 **전부 예외 없이 잉크 `#1a1a1a`**(`color/ink/900`에 bound:true)였다 — 원본의 "흰색/앰버" 2색 체계가 전혀 반영되지 않고 ConfettiFooter의 색(잉크)이 BgPixels에도 잘못 복제돼 있었다. ConfettiFooter 자체(각 프레임 5개, 총 40개)는 원본과 동일하게 잉크로 이미 올바른 상태였다(이 부분은 재작업 불필요).

추가로 Divider("or" 구분선, 5개 프레임 `935:33`/`936:1042`/`936:1191`/`996:2713`/`996:3014`에 존재, 각 2 라인)도 원본은 `#1a1a1a` **10% 불투명도**의 옅은 선(`501:5110` 등, fill 방식)인데, 현재 934:2 쪽은 LINE stroke로 `#1a1a1a` **100% 불투명도**(완전 검정 실선)였다 — 이 역시 컬러 표현 오류(불투명도가 색의 일부인 케이스)로 함께 발견해 수정 대상에 포함했다.

### 수정 내용

`use_figma`로 934:2 페이지 8개 프레임 전체를 순회해 다음을 raw fill로 직접 수정(순수 장식 오브제, 토큰 미바인딩 상태로 그대로 두되 hex만 원본과 일치시킴 — 기존 `color/ink/900` 바인딩은 제거하고 원본과 동일하게 unbound raw로 전환, 원본 자체도 unbound):
- **다이아몬드 40개**: `#1a1a1a` → **흰색 `#ffffff`**
- **십자 32개(64 vector, 각 2개씩)**: `#1a1a1a` → **흰색 `#ffffff`**
- **별 40개 인스턴스(320 vector, 각 8개씩)**: `#1a1a1a` → **앰버 `#ffce2c`**
- **Divider 10개 라인(5프레임 × 2)**: stroke `#1a1a1a` opacity 1 → **opacity 0.1**(색 자체는 동일, 불투명도만 원본과 일치)
- ConfettiFooter(이미 원본과 일치, 잉크)는 무변경.

`get_screenshot`으로 934:2 페이지 전체 및 개별 프레임(login, Join, login-비밀번호재설정-1단계)을 재검증: 흰색 다이아몬드/십자·앰버 별이 블루 배경 위에서 원본과 동일한 톤으로 렌더링되고, "or" 구분선도 원본처럼 옅게 렌더링됨을 확인했다.

### 개수 요약 — "부분만 고치고 완료로 착각"하지 않도록 정확한 수치

- 색상 인벤토리 스캔 대상: 934:2 페이지 8개 프레임 전체(예외 없이 전수 스캔, 스팟체크 아님).
- **컬러 수정한 노드 수**: 다이아몬드 40개 + 십자 64개(vector, 32개 shape) + 별 320개(vector, 40개 instance) = **fill 수정 424개 vector/shape 단위** (shape/instance 단위로는 40+32+40=112개).
- **불투명도 수정한 노드 수**: Divider 라인 10개.
- **총 수정 대상**: 112개 shape/instance(색상) + 10개 line(불투명도) = **122개 노드**, 8개 프레임 전체.
- ConfettiFooter(40개 shape/instance, 프레임당 5개×8)는 이미 원본과 일치해 재작업 불필요 — 스캔은 했으나 수정하지 않음.

### 935:33 공통 배경 관련 확인 — 컴포넌트/인스턴스 아님, 화면별 개별 수정 필요

`get_metadata`로 확인한 결과 `935:33`(Join)은 **컴포넌트도 인스턴스도 아닌 일반 FRAME**이고, 그 안의 `BgPixels`(`936:976`)도 일반 FRAME이다 — 즉 934:2 페이지의 8개 프레임은 마스터 컴포넌트를 공유하는 구조가 아니라, 각 프레임마다 BgPixels/ConfettiFooter가 **독립적으로 복제된 raw 노드 집합**이다(Pixel/Star만 유일하게 실제 컴포넌트 INSTANCE). 따라서 "935:33 마스터 하나만 고치면 전체에 전파된다"는 가정은 성립하지 않아 8개 프레임 전부를 개별적으로 순회 수정했다(위 수정 내용에 이미 반영 완료) — 이 사실 자체가 이번 재작업 범위 밖의 구조적 발견이라 design-pl에게 참고 보고한다(향후 이런 배경 오브제를 컴포넌트화해 재사용하면 이런 전수 재작업이 반복되지 않을 것).

**전달 대상**: 없음(직접 완료). design-pl 참고 보고 — ① 컬러 자체 오류가 실제로 존재했음(이전 라운드의 "색 문제 없음" 결론은 틀렸음), ② 935:33이 공유 컴포넌트가 아니라 8개 프레임에 독립 복제된 raw 구조라는 사실.

**값 출처**: 확정 login 프레임(`501:4940`) 하위 BgPixels(`501:4942`)·ConfettiFooter(`501:5143`)·Divider(`501:5108`) 전체 vector 직접 실측(`use_figma` 읽기 전용) + 934:2 페이지 8개 프레임 전체 BgPixels·ConfettiFooter·Divider 전수 재실측(`use_figma` 읽기 전용 → 수정) + `get_screenshot`(934:2 페이지 전체, login/Join/995:303 개별) — 임의 근사치 없음, fileKey `zgGlMBwFglaDlaeyP4CkgR`.

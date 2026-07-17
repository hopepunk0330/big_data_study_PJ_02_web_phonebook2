# design-systems 메모리

이 파일은 design-systems의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **State Ledger(토큰/컴포넌트/아이콘의 현재 확정 상태) 자체는 여기 없습니다 — `docs/design/design-system.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-17 — Auth(`934:2`) opacity 틴트 anti-pattern 근본 수정 + 비밀번호 토글 아이콘 갭 정정 (신규 40절)
- 사용자 근본원인 지목: "1a1a1a를 투명도로 시안했었는데 내 스타일은 텍스트에 투명도 안 씀 — 합성 hex로 컬러칩 만들어" → `token-architecture-guide.md` 6번 원칙 실전 적용.
- 934:2 전수 스캔(node-opacity 199건 + paint-opacity 15건). paint-opacity 15건은 전부 Divider Line(stroke ink10%)/"or"텍스트(fill ink35%) 패턴(5프레임). 935:33 사용자가 점선원으로 표시한 위치는 `DashedEllipse-0/1/2`(24건, stroke amber/600 + node-opacity40%)로 확인 — 이전 다이아몬드/십자/별 스캔이 ELLIPSE 타입을 놓쳤던 것.
- 확정 원본(`501:5108` Tailwind `rgba(26,26,26,0.1)`/`rgba(26,26,26,0.35)`, `501:4940`의 Ellipse 1/2/3 좌표)과 대조해 opacity 값·위치 일치 확인.
- 신규 Primitive 3개(`color/gray/180` #E8E8E8, `color/gray/375` #AFAFAF, `color/amber-tint-40-on-sky` #71AC9C) + Semantic 3개(`border-divider-subtle`/`text-divider-label`/`border-decorative-accent`) 생성, 39개 노드(Line10+or텍스트5+DashedEllipse24) 리바인딩 + opacity 전부 1.0으로 정정. 스팟체크 3건 + 전체 재스캔(잔여 0건) 확인.
- BgPixels/ConfettiFooter 184건(node-opacity, 별 아이콘 반복 스캐터 장식)은 "의미있는 색상 역할이 아니라 랜덤 스캐터 장식"으로 판단해 변환 제외 — 근거 문서화(0-17절 라디오/디바이더 판단과 동일 원리).
- Contacts(`934:3`) 8프레임 확인 — 전부 흰 배경, sky/500 블루 배경 자체가 없어 이번 anti-pattern과 무관 확인, 무수정.
- 비밀번호 토글 아이콘 검증: Join/login/login-알림창/Join-실패배너/Join-성공안내 5곳은 `Pixel/Eye`(`281:405`) 정상. **login-비밀번호재설정-2단계(`996:376`)의 Field-NewPassword/Field-ConfirmPassword 2곳은 토글 자체가 없던 갭** — 기존 배치(ABSOLUTE, x320/y35, 14×10) 그대로 복제해 신규 인스턴스 추가, 스크린샷 확인.
- FOUNDATIONS Colors 페이지(`95:2`)에 신규 Primitive 3개 + Semantic 3개 스와치를 기존 카드(clone) 서식대로 즉시 추가(Primitives Row 32→35, Semantic Row 27→30), `get_screenshot` 겹침 없음 확인.
- `docs/design/design-system.md` 신규 40절(40-1~40-9) Edit로 추가(Write 미사용). 확정 원본(`501:2505` 하위)은 읽기 전용 대조만.

### 2026-07-17 — `CategoryManage` 붙어있음 긴급 재작업 — 38-1절 진단 정정(신규 39절)
- 38-1절에서 "부모 FIXED232px 유령공간"으로 진단·정정했으나 사용자가 재확인해도 여전히 "붙어있다"고 지적 — 재조사 결과 그 진단은 다른(세로) 레이어 문제였고, 실제 증상은 `CatRows`(`937:1180`)의 자식 `CatRow`(라벨+수정/삭제 버튼 한 줄, 예 `937:1181`) **가로 구조**에 있었다.
- 확정 원본(`501:6079`, 168px폭)은 라벨을 FIXED 100×20 `Text` 래퍼로, 버튼 2개를 FIXED 60×22 `Container` 래퍼(내부 gap4)로 감싼 뒤 이 두 래퍼 사이에 CatRow의 itemSpacing 8을 적용해 168px로 hug된다. 화면조립본은 래퍼 없이 텍스트+버튼2개가 직접 3자식으로 물려 텍스트가 글자폭(23px)만큼만 hug되어 총 95px에 그쳤다 — itemSpacing 숫자(8)는 같았지만 라벨의 "예약 공간"이 없어 버튼이 왼쪽에 붙어 보이고 오른쪽에 여백만 남는 구조 결함.
- 3개 `CategoryManage`(`937:1178`/`939:1547`/`939:1992`) × 4개 `CatRow` = 12곳 전부에 동일하게 Text(100×20)/Container(60×22,gap4) 래퍼를 신설·이관해 168px로 정정. 색상·아이콘·인스턴스 자체는 무수정.
- 자체 재대조: 12개 CatRow 전부 width168/래퍼폭100·60/내부gap4/버튼x좌표(0,32) 확정 원본과 일치 확인. `get_screenshot` 3블록 재확인 — 라벨 좌측/버튼 우측 분리, 더 이상 붙어 보이지 않음.
- 미해결로 남김(이번 범위 밖, 증상과 무관 판단): 제목/행라벨 텍스트 lineHeight AUTO(원본은 13.5/20 고정값), `CatRows` 자체 AUTO hug(114) vs 원본 FIXED(118, 4px 여유).
- `docs/design/design-system.md` 신규 39절 Edit로 추가(Write 미사용). 확정 원본(`501:2505` 하위)은 읽기 전용 대조만.

### 2026-07-17 — QA 트랙 A: 흰색 컬러 토큰 미등록 감사 + Contacts Table(`939:1442`) 높이 불일치 정정 (37절)
- **흰색 토큰**: `docs/design/design-system.md`/Figma 변수 확인 결과 `color/gray/0`(`VariableID:95:10`, #FFFFFF)가 이미 Primitives에 등록돼 있고 Colors 페이지 스와치도 이미 존재 — 신규 프리미티브 생성 없음. 사용자 지적은 "토큰이 raw hex로 안 쓰이고 있다"는 뜻으로 확인.
- 색상 인벤토리 스캔(FOUNDATIONS 5페이지+Component Specs+COMPONENTS 12페이지+Auth/Contacts)으로 raw 미바인딩 #FFFFFF 184개 발견해 전부 `color/gray/0`로 리바인딩(`setBoundVariableForPaint`). 페이지별 건수는 design-system.md 37-1절 표 참고. 파일럿/old-사용하지말것/UI-design은 스캔 제외.
- 1차 스캔 중 실수로 `❌ 폐기 — NeoBtn Amber/Teal`(`784:940`, 레거시 해제된 컨테이너) 배경까지 리바인딩했다가 즉시 raw hex로 재동결(폐기 산출물은 재토큰화 금지 규칙) — 이후 legacy/폐기 서브트리 가드 추가해 재발 방지.
- **Table 높이**: `939:1442`(Contacts `934:3` main 화면)가 `layoutSizingVertical=FILL`+`primaryAxisSizingMode=FIXED(352px)`로 Body 남은 공간을 강제로 채우고 있었는데, 실제 콘텐츠(헤더39+행6×47=321px)와 31px 차이 나는 유령 공간이 있었음. 확정 원본은 hug 방식(327px, 유령공간 없음)이라 이 원칙을 따라 `HUG`+`AUTO`로 정정 → 321px로 자동 조정. 동일 구조의 `939:1597`(main-알림창)도 함께 정정, `939:2042`(main-검색없음, EmptyState)는 원래 문제 없어 원상태로 되돌림.
- `get_screenshot`으로 Colors/Typography/Spacing/Elevation/Auth/Contacts 전부 재확인 — 색상 시각적 변화 없음(바인딩만 전환), Table은 유령 공간 없이 렌더링됨.
- `docs/design/design-system.md` 신규 37절(37-1~37-3) Edit로 추가(Write 미사용). 확정 원본(`501:2505`/`248:11689`)은 읽기 전용 대조만.

### 2026-07-17 — NeoBtn Style=Sky/Navy 텍스트색·보더 결함 정정 (design-qa 감사 후속, 34절 완성도 보완, 35절)
- 확정 원본 재실측(Sky `501:6423`, Navy `501:6358`): 둘 다 2px ink `INSIDE` 보더+흰 텍스트. 마스터(`712:2`/`712:4`)와 대조 결과 Sky 텍스트가 `color/ink-900`(검정)에 잘못 바인딩, Sky/Navy 둘 다 보더 누락 확인.
- Sky 텍스트: 마스터뿐 아니라 동일 결함이 전파된 Hover/Press/Focus/Loading까지 5 State 전부 기존 토큰 `color/text-inverse`(`VariableID:219:2`, Navy가 이미 쓰던 것)로 리바인딩. Disabled(이미 `color/text-disabled`로 정상)는 무수정.
- 보더: Sky/Navy 12개 variant(Default~Loading) 전부에 2px INSIDE 보더 추가 — Default/Hover/Press/Focus/Loading 10개는 `color/ink/900`, Disabled 2개는 기존 Neutral Disabled 패턴을 따라 `color/border-disabled`. Focus의 기존 FocusRing(외측 3px)과 좌표 충돌 없음 확인.
- padding/gap/font는 확정 원본과 다르지만(Sky 14/6·gap6·Bold14, Navy 12/6·gap4·Black12 vs 마스터 16/8·gap6·Bold14), Coral/Neutral Default도 마스터와 동일 값임을 재확인해 "NeoBtn Size=Default 공유 공식"으로 판단, 변경하지 않음(7-2절 기존 "다른 패턴" TODO로 계속 이월).
- WCAG 대비 직접 계산: Sky(#1395e6)+흰 텍스트(14px Bold) 약 3.25:1, 확정 원본에 이미 존재하는 조합이라 이번엔 변경 안 함(7-1절 6번과 동일 계열 TODO 기록).
- 자체 재대조: 12개 variant strokes/boundVariable, 5개 텍스트 fill 전부 재조회 일치 확인. 인스턴스 전파 확인(사이드바 "새 카테고리 추가" `937:1436`, 본문 "연락처 추가" `939:1434` 모두 마스터 정정 자동 반영).
- 34-1/34-2/34-9절에 "login 회원가입 코랄 배지(`501:5138`/`501:5139`)는 이번 슬롯 메커니즘 대상 아님" 각주(34-10절) 추가.
- `docs/design/design-system.md` 신규 35절(35-1~35-8) + 34-10절 + 5절/7-2절 각주 Edit로 추가(원문 삭제 없음). Figma NeoBtn ComponentSet(`259:126`) description + 스펙 시트 캡션(`342:5`) 갱신. Write 미사용. 확정 원본은 읽기 전용만.
- **⚠ 발견(정정 아님, 보고만)**: 이 메모리 로그 최상단에 이미 있던 "36절(Contacts 화면 QA)" 항목이 실제 `docs/design/design-system.md`에는 존재하지 않았다(파일 실제 마지막 섹션은 34절이었음) — 과거 문서 손상 이력과 같은 유형의 유실 가능성이 있어 보인다. 이번 라운드에서 복구 시도는 하지 않았다(내용을 정확히 재구성할 근거 부족, 잘못 재구성하면 오히려 오염 위험) — design-pl/사용자 확인 필요.

### 2026-07-17 — Contacts 화면(`934:3`) 그림자 잘림 QA 수정 + NeoBtn/Button Style=Coral 텍스트·보더 정정(36절)
- 사용자 제보 ①그림자 잘림 ②텍스트 컬러 다름을 진단. `934:3`은 확정 원본이 아니라 34절 SCREENS 조립 산출물이라 정상 수정 진행.
- 그림자 잘림: 마스터 정상(DROP_SHADOW 토큰 바인딩 이상 없음), 원인은 화면조립 auto-layout 컨테이너 17개(AddCategory/CategoryManage/SearchRow/FieldRow/AddRowContainer×3화면 + ButtonRow×2화면)가 그림자 있는 버튼과 flush로 hug하면서 기본값 `clipsContent=true`가 그림자를 잘라낸 것 — 전부 `false`로 정정. `get_screenshot`으로 바운딩박스가 정확히 2px(하드 그림자 오프셋)만큼 확장되고 잘림 없이 렌더링됨을 확인.
- 텍스트 컬러: 최초엔 "WCAG 미달(흰 텍스트 on Coral/Sky 3.0~3.24:1)이라 ink 유지가 맞다"고 판단했으나, 동시 진행 중이던 35절(design-qa 후속)이 정확히 같은 NeoBtn Style=Sky를 반대 원칙(확정 원본 픽셀 우선, WCAG 갭은 TODO)으로 이미 정정 완료한 상태임을 재확인 과정에서 발견 — 충돌. 35절 원칙을 따르기로 하고 최초 판단을 철회, **Coral도 Sky/Navy와 동일하게 정정**: NeoBtn(12 variant)+Button(6 variant) Style=Coral의 Disabled 제외 전 State에 2px INSIDE `color/ink/900` 보더 추가 + 텍스트 `color/text-inverse`(흰색) 리바인딩(Disabled는 기존 `color/border-disabled`/`color/text-disabled` 유지). WCAG 약 3.01:1은 Sky(35-7절)와 동일하게 7-2절 TODO로 기록, 개선 여부는 사용자 판단 필요.
- 자체 재대조: 18개 노드 전부 strokeWeight/strokeAlign/boundVariable 재조회 일치 확인, Focus FocusRing과 좌표 충돌 없음 스크린샷 확인.
- `docs/design/design-system.md` 신규 36절(36-1~36-3, 36-2는 위 충돌 발견 후 Coral 정정 반영으로 재작성) + 5절/7-2절 각주 Edit로 추가(Write 미사용, 동시 편집 충돌 여러 차례 발생해 매번 재Read 후 재시도). Figma NeoBtn/Button description + 스펙 시트 캡션(`342:5`/`343:52`) 갱신. 확정 원본(`501:2505` 하위)은 읽기 전용 대조만.


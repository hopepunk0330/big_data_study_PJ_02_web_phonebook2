# design-systems 메모리

이 파일은 design-systems의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **State Ledger(토큰/컴포넌트/아이콘의 현재 확정 상태) 자체는 여기 없습니다 — `docs/design/design-system.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-18 — `color/bg-page` 신규 등록 + #DCDEDF 확정 (신규 44절)
- 사용자가 "`color/bg-page`(현재 #FFF8EE)를 #DCDEDF로 변경"을 요청 → 전수 검색 결과 Figma에 이 변수 자체가 없었음(CSS `tokens.css`에만 존재, FOUNDATIONS 미등록 갭). 확정 원본(`501:2505`) 대조로 "main 화면 뒤 컨테이너 배경"이 `main`류 5프레임(`501:6008` 등) 최상위 fill `#FFF8EE`임을 확인, SCREENS(`934:3`) 대응 프레임은 `color/gray/0`(흰색)로 잘못 바인딩돼 있었음(37-1절 흰색 일괄 리바인딩 때 편입된 것으로 추정).
- Primitive `color/gray/205`(`VariableID:1103:3`, #DCDEDF) + Semantic `color/bg-page`(`VariableID:1103:4`, alias, scope FRAME_FILL/SHAPE_FILL) 신규 생성 — 원래값(#FFF8EE)을 거치지 않고 사용자가 이미 확정한 #DCDEDF로 직접 등록(코드가 이미 그 값으로 반영 완료 상태였으므로).
- Contacts(`934:3`) "main"류 10개 프레임(5개 파일럿 대응 + 5개 후속 신규화면) 배경을 `color/gray/0`→`color/bg-page`로 리바인딩. Auth(`934:2`)는 확정 원본이 `#FFFFFF`라 대상 아님.
- FOUNDATIONS Colors 페이지(`95:2`)에 기존 스와치(`1025:6`/`1025:14`) clone해 Primitives/Semantic Row에 스와치 2개 추가.
- 대비: 10개 프레임 전부 최상위에 직접 얹힌 텍스트 없음(전부 내부 AppWindow/Card 자식 위) — WCAG 계산 대상 아님, 충돌 없음 확인.
- 자체 재대조: 10개 프레임 boundVariable id + hex `#dcdedf` 재확인(불일치 0), `get_screenshot`(`937:298`/`941:1508`) 렌더링 확인. 확정 원본은 읽기 전용 대조만.
- `docs/design/design-system.md` 신규 44절 Edit로 추가(Write 미사용).

### 2026-07-17 — `941:1508` ButtonRow 42px vs 44px 상충 3차 재확인·최종 확정 (41-2절)
- design-qa("42px, HIGH")와 design-systems 이전 재확인(41-1절, "44px, 정상")이 상충해 재실측. `get_metadata`(`941:1508`) — 버튼 `941:3043`/`941:3045` 둘 다 y=4/height=44, 부모 ButtonRow(`941:3042`) height=48로 정확히 채움(잔여 0). `get_design_context`(`941:3042`) Tailwind 변환도 `h-[44px]`/`pt-[4px]` 일치. 확정 원본(`501:4172`)의 `501:4212`/`501:4215`도 동일 y=4/height=44, 부모 `501:4211` height=48로 픽셀 단위 일치. `get_screenshot`(`941:1508`) 육안 확인도 빈 여백 없음.
- **최종 결론: 44px 확정, design-qa의 42px 보고는 기각.** 42px 값 자체가 어느 노드 속성에도 나타나지 않아 캐시된/오래된 스크린샷 또는 다른 노드 착오로 추정.
- `docs/design/design-system.md` 신규 41-2절 Edit로 추가(Write 미사용). 확정 원본은 읽기 전용 대조만.

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



# brand-designer 메모리

이 파일은 brand-designer의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **브랜드 결정사항 자체(현재 확정 상태)는 여기 없습니다 — `docs/design/brand-guide.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-12 — Brand Guide "만들다 만" 상태 보완: Layout Convention(B-2) 섹션 신설
- 사용자가 Brand Guide를 미완성 상태로 지적 → SCREENS 파일럿(로그인/Contacts)이 확정된 2차 레이아웃 B-2(`62:6`)의 실제 관례를 못 이어받고 컬러·느낌만 재해석해버린 원인 중 하나로 지목됨.
- 기존 메모리 요약을 베끼지 않고 `34:4`(Concept B 톤 프레임)와 `62:6`(B-2)을 `get_screenshot`+`get_design_context`로 다시 직접 관찰. 컬러/폰트값은 기존 확정과 100% 동일 확인(조정 없음).
- 관찰해 새로 기록한 디테일: 보더 두께 위계, 라운드 스케일(16/10/8/5/999), 4px 기반 간격 리듬, 정보 밀도 타이포 크기 5단계, UI 색상 사용 로직(teal=주요액션+데이터강조, coral=파괴적액션+검색, amber=선택상태+CTA), 장식 모티프(로고 원형 배지+pill 카운트 배지뿐, 그림자 전혀 없음).
- Figma "Brand Guide" 루트 프레임(`52:3`)에 새 섹션 "레이아웃 관례 (Layout Convention — B-2)"(`125:2`) 추가. `docs/design/brand-guide.md` 갱신.

### 2026-07-12 — 34:4 재관찰: 브랜드 퍼스낼리티 표현 장치 보강 + 로고 섹션 재작성
- 배경: `62:6`(B-2)만 재관찰했던 지난 보완에서 `34:4`(1차 톤 프레임) 자체의 성격 표현 장치(배지 은유, 정확한 워드마크 레터링, 퍼스낼리티 이중성)는 관찰하지 않은 채 넘어간 것이 드러남.
- `34:4`를 재관찰해 심볼(코랄 `#FF5A76` 채움 + 2px 잉크 스트로크)·워드마크(Baloo 2 Bold 26px `#0F7A6E`)·간격(14px) 정확 스펙 확보. Figma "Brand Guide" 페이지에 "브랜드 퍼스낼리티 표현 장치" 섹션(`142:2`) 추가, `52:9` 내부에 정확한 레터링 스펙 서브 블록 추가. `docs/design/brand-guide.md` 갱신.

### 2026-07-13 — 사용자 직접 확정 디자인(8프레임) 기준 Brand Guide 전면 재작성 (2-4번 적용)
- 배경: 사용자가 Figma에 직접 만든 "확정 디자인 - 절대 원본 건들지 말것-" 섹션(`248:11689`, 8개 프레임)이 AI 파일럿(B-2 등)보다 우선하는 최종 소스임이 확인됨(2-4번). 8개 프레임 전부를 `get_screenshot`+`get_design_context`+`get_metadata`로 새로 관찰. **읽기 전용만 수행.**
- 이전 문서의 핵심 오류 정정: (1) "그림자 전혀 안 씀" → 실제로는 하드 오프셋 스티커 그림자(1/2/6px)와 소프트 블러 그림자(알림 배너 전용) 두 시스템. (2) 워드마크는 Baloo 2 ExtraBold 22px, 색상은 배경에 따라 흰색/ink로 반전. (3) 심볼-워드마크 간격 10px. (4) 로고 심볼은 내부에 흰 픽셀 별(PxStar) 포함.
- 신규 발견: 8bit 픽셀 컨페티(BgPixels 전역 산포 vs MemphisAccents 구석 클러스터), 코너 브래킷 인풋(CornerInput), 카드 상/하단 액센트 스트립, CatBadge 4색 팔레트, 마이크로 픽셀 아이콘(Pixel*/Px*) vs 24px 표준 플랫 아이콘(Icon/*) 이중 계층.
- `docs/design/brand-guide.md`를 8개 프레임 관찰 결과로 전면 덮어씀(13개 섹션 재구성). Figma는 전혀 쓰지 않음.

### 2026-07-17 — Primary/Secondary/Accent 역할 재평가 + Brand Guide 신규 프레임 정식화 + Warm Ledger 폐기 라벨링
- 배경: 세션 중 다수 컴포넌트가 teal(`#17A398`)→sky(`#1395E6`)로 리바인딩됐는데 문서(`brand-guide.md`, `user-confirmed-final-design.md`)는 여전히 "Primary 틸"로 기록돼 있었고, 사용자가 직접 "프라이머리/세컨더리 구분이 바뀌었을 것 같다"고 지적. design-pl의 초기 스팟체크(main 프레임만 대충 셈)를 8개 확정 프레임(`501:2505` 하위) 전체·fill+stroke 양쪽 실측으로 검증.
- **실측 방법**: `use_figma` 읽기 전용 스크립트로 8개 프레임 전체를 순회해 sky/teal/coral/amber 4색의 fill·stroke 매칭 노드를 수집하고 면적(px²)·용도를 집계. teal 32×32 fill의 정체(Avatar 래퍼 Container, 실제 렌더링은 스카이블루 오버라이드에 가려짐)까지 노드 경로 추적으로 확인.
- **결론**: Primary=스카이블루(`#1395E6`, 사이드바 전체·Join/login 풀블리드 배경·아바타 — 실측 면적 압도적 1위, 신규 편입) / Secondary=코랄(변경 없음) / Accent=앰버(변경 없음, 단 count pill·main-삭제 모달 스트립은 구값 `#FFCB47` 잔존 발견) / 틸=Primary에서 제외, "카테고리 식별색(narrow)"으로 재정의(유일한 가시 용도: CatBadge "회사" 보더/닷, row "수정" 액션 아웃라인). 프리미티브 토큰 이름은 변경 없음, Figma 바인딩도 손대지 않음(문서 정정 전용 라운드).
- `docs/design/brand-guide.md` 2절, `docs/design/confirmed/user-confirmed-final-design.md` 2-1절을 정정 각주 방식(원문 보존, 기존 2026-07-16 각주 위에 이어붙임)으로 갱신. `docs/design/graphic-assets.md`는 Read로만 확인(소유권 경계 유지, 이미 "구 세대 원문 기록" 캐비트 있어 충돌 없음).
- Figma에서 옛 "Brand Guide — Warm Ledger"(`52:3` + 하위 9개 섹션)에 `❌ 폐기 —` 라벨 부여(내용/구조 무변경). 같은 페이지(`52:2`)에 신규 프레임 "Brand Guide — Pixel Confetti Brutalism (Stage2 Confirmed, 2026-07-17)"(`920:7`)를 9개 섹션으로 신규 제작(Color Palette에 재평가된 트라이어드 + 카테고리 식별색 콜아웃 + CatBadge 4색, Brand Personality Devices에 하드그림자/코너브래킷/액센트스트립 시각 데모 포함).
- **버그 발견 및 우회**: Baloo 2 ExtraBold 흰색 텍스트가 "2단계 이상 중첩된 auto-layout" 안에서 빈 흰색 박스로 깨지는 Figma 렌더링 버그를 발견(격리 재현으로 확인). 워드마크 데모의 "Lockup"을 auto-layout이 아닌 plain frame(절대좌표)으로 바꿔 우회 — 이후 섹션 제작 시 백색 텍스트는 이 패턴을 유지할 것.

### 2026-07-17 — design-qa MEDIUM 결함 정정: Triad Swatch Row 높이 불균일 (161px/153px → 166px 통일)
- design-qa 감사에서 `920:7`(Brand Guide 신규 프레임) Color Palette 섹션 `921:5` "Triad Swatch Row"의 4개 스와치 컨테이너(`921:6`/`921:10`/`921:14`/`921:18`) 폭은 196px로 동일하지만 설명 텍스트 줄 수 차이(3줄 vs 2줄)로 높이가 166px/153px로 어긋나 있음이 발견됨 — `figma-page-format-guide.md` 1번(스와치 크기 통일) 위반. 같은 라운드 완성도 보완이라 별도 승인 없이 즉시 정정.
- `get_metadata`/`get_design_context`로 `921:5`+4개 자식 먼저 재확인 → 원인이 hug 사이징(`primaryAxisSizingMode='AUTO'`)임을 확인.
- 정정 방식은 텍스트 재작성(줄 수 강제 조정) 대신 **고정 높이**를 선택: 4개 컨테이너 모두 `resize(width, 166)` 후 `primaryAxisSizingMode='FIXED'`로 전환. 이 페이지 스와치는 "내용에 따라 흔들리지 않는 고정 크기"가 포맷 가이드 취지에 맞고, 설명 문구를 인위적으로 줄이거나 늘려 내용을 왜곡할 필요가 없기 때문. 색상 hex·바인딩·텍스트 내용은 전혀 건드리지 않음.
- `get_screenshot`으로 4개 스와치 하단 정렬·잘림/겹침 없음 확인. 상위 Row(`921:5`, 172px)·Color Palette 섹션(`921:2`, 444px)은 원래도 최댓값(166px) 기준으로 계산돼 있어 크기 변화 없음(하위 프레임 위치 재검토 불필요).
- `docs/design/brand-guide.md` 14절에 이 정정을 각주로 추가(원문 삭제 없음).

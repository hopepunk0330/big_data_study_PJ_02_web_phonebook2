# mercari 가격제안 화면 — Brand Guide (확정)

이 문서는 mercari 가격 UX 실험 참여자 앱 대안 디자인 프로젝트의 확정 브랜드 가이드다. 소스는 Figma 파일 `SIBLz4S4IZbjabzhMSAgdo`의 "확정 디자인 컨셉_직접작업" 섹션(`126:2601`) 아래 사용자가 직접 완성한 7개 화면(Concept A_01~04, Concept B_01~03)이다. 이 문서는 그 7개 화면을 그대로 재현할 수 있는 수준까지 수치·모티프를 기록한 것이며, 화면 자체는 전혀 수정하지 않았다(읽기 전용 열람만).

design-systems·ui-designer·graphic-designer가 앞으로 컴포넌트 토큰화·화면 확장·아이콘 제작을 할 때 참고하는 공유 악보다. 이 프로젝트의 다른 문서(`docs/design/brand-guide.md`, `docs/design/design-system.md`, `docs/design/confirmed/*`)는 fileKey `zgGlMBwFglaDlaeyP4CkgR`(연락처 관리 앱) 소유이며 이 프로젝트와 무관하다.

## 0. Concept A / B의 관계 — 하나의 통합 시스템

Concept A와 B는 서로 다른 브랜드 톤이 아니라, **완전히 동일한 하나의 디자인 시스템**이 적용된 두 개의 플로우 변형이다. 색상 hex, 폰트 역할 분담, radius, 보더, 그림자(둘 다 전무), spacing 리듬이 전부 동일하다. 실제 차이는 스타일이 아니라 세 가지 상태/스텝 차이뿐이다.

1. **Hero Price Card variant**: A는 단일가("60,000원"), B는 범위가("44,000 ~ 60,000원") — 물결표(~)를 Noto Sans KR Bold 33px로 숫자 사이에 끼워 넣는다.
2. **Price Input**: B_02·B_03에만 존재한다("아니요, 다르게 하고 싶어요"를 선택했을 때 등장하는 직접입력 필드). A 플로우엔 없다.
3. **전환 연출**: A_02~04는 딤(`bg-black opacity-50`) + White Sheet가 화면 하단(y=380px)에서 얼굴을 내미는(peek) 바텀시트 전환 연출을 쓴다. B는 전부 White Sheet가 완전히 펼쳐진 정착 상태다.

이하 섹션은 A/B를 나누지 않고 하나의 토큰 체계로 서술하며, 위 3가지 차이점만 각 섹션에서 짧게 별도 표기한다.

## 1. 색상 (Color)

| 역할 | Hex / 값 | 용도 |
|---|---|---|
| Dark Hero 배경 | `#1A1D29` | 화면 상단 다크 히어로 섹션, 딤 오버레이 기준색 |
| White Sheet / 카드 배경 | `#FFFFFF` | 바텀시트, 카드, Choice Card 미선택 상태 |
| 뉴트럴 보더/구분선 | `#E2E6EC` | 카드 보더, 구분선(Rectangle), 드래그 핸들, Progress 숫자 opacity 기준 |
| Primary | `#3182F6` | 활성 CTA 배경, 선택된 Choice Card 보더(2px), Price Input 포커스 보더(1.5px), 검색 배지 아이콘 색 |
| Secondary | `#3789FF` | 헤드라인 2행, "AI 추천" 팁 배지 배경, 스텝 숫자("1"), 서브헤드라인("이 가격 그대로"), 유사상품 건수 강조 텍스트 |
| Accent Tint | `#E8F3FF` | 유사상품 분석 배지 배경, 빅데이터 배지 배경, 선택된 Choice Card 배경 |
| Ink (1차 텍스트) | `#1A1D29` | 본문 헤드라인, 카드 타이틀, 가격 숫자 |
| Ink 뮤트 (투명도별) | `rgba(26,29,41,0.55/0.5/0.4/0.35)` | 0.55=서브캡션(추천 판매가, Choice Card 설명), 0.5=상품 서브텍스트, 0.4=스텝 "/2", 0.35=CTA 비활성 텍스트 |
| 흰 텍스트 | `#FFFFFF` / `#F5F5F5` | 다크 히어로 위 헤드라인 1행(#FFFFFF), Eyebrow·AI추천 배지 라벨(#F5F5F5) |
| 상태배지 보더 | `#DEDEDE` | "상태: S급 (A+)" 흰 배지 보더 (단, B_03만 이 보더 클래스가 누락돼 있음 — 확정 화면 자체의 불일치, design-systems에 이미 보고됨. 임의로 고치지 않고 그대로 기록) |
| CTA 비활성 배경 | `#F7F8FA` | "다음 보기" 비활성 상태 배경 |

**Eyebrow 배지 특이사항**: "AI 가격 제안 ENGINE" 라벨을 감싸는 pill(Eyebrow)은 배경색 `#E8F3FF`가 정의돼 있지만 실제 렌더링에는 배경이 적용되지 않은 상태(비가시)다 — 아이콘+텍스트만 다크 배경 위에 떠 있는 형태로 의도된 디자인이다. design-systems가 토큰화할 때 이 배지를 "배경 있는 pill"로 되살리지 않도록 주의.

**컬러가 만드는 성격**: Primary/Secondary 블루 계열은 "신뢰"와 "분석 근거가 있는 제안"이라는 이 화면의 핵심 메시지(AI가 빅데이터로 산출한 가격)를 뒷받침한다. Accent Tint(`#E8F3FF`)는 채도를 낮춘 옅은 블루로, 경고나 강제성 없이 "추천"을 부드럽게 신호하는 역할이다. 다크 히어로(`#1A1D29`)는 상품 사진을 극적으로 부각시키는 무대 장치이자, 화이트 시트와의 명도 대비로 "정보 영역(밝음)과 이미지 영역(어두움)"의 위계를 컬러만으로 분리한다.

## 2. 타이포그래피 (Typography)

**폰트 역할 분리 원칙**: 숫자(가격)만 Inter, 한글이 섞인 모든 텍스트는 Noto Sans KR을 쓴다. 가격 숫자에만 유일하게 음수 자간(-0.38px)이 적용된다 — 이 화면에서 가장 중요한 단일 정보(판매 예상가)를 시각적으로 다른 문자와 구분되는 별도의 서체 질감으로 처리해, 사용자의 시선이 가격 숫자에 먼저 꽂히도록 만드는 의도적 장치다.

| 위계 | 서체/굵기 | 크기 | 색상 | 비고 |
|---|---|---|---|---|
| 히어로 가격 숫자 | Inter Bold | 38px | Ink | 자간 -0.38px (유일한 비-Noto/유일한 자간 지정) |
| 가격 단위 "원" | Noto Sans KR Bold | 29px | Ink | |
| 가격 범위 물결표 "~" | Noto Sans KR Bold | 33px | Ink | B 전용 |
| 헤드라인 1행 | Noto Sans KR Bold | 24px | `#FFFFFF` | 다크 히어로, line-height 1.32 |
| 헤드라인 2행 | Noto Sans KR Bold | 32px | `#3789FF` | 다크 히어로, line-height 1.32 |
| 서브타이틀("이 가격 그대로") | Noto Sans KR Bold | 16px | `#3789FF` | |
| 질문 타이틀("등록하시겠어요?") | Noto Sans KR Bold | 22px | Ink | |
| Choice Card 1차 텍스트 | Noto Sans KR Bold | 16px | Ink | |
| Choice Card 2차 텍스트(설명) | Noto Sans KR Regular | 12px | Ink, opacity 55% | |
| 상품명 | Noto Sans KR Bold | 14px | Ink | |
| 상품 서브텍스트(브랜드·카테고리) | Noto Sans KR Regular | 11px | Ink, opacity 50% | |
| 배지류 텍스트 | Noto Sans KR Bold | 10~12px | 배지별 상이(아래 5절 참고) | |
| 스텝 숫자("1") | Noto Sans KR Bold | 16px | `#3789FF` | |
| 스텝 분모("/2") | Noto Sans KR Bold | 13px | Ink, opacity 40% | |
| CTA 텍스트 | Noto Sans KR Bold | 16px | 활성=`#FFFFFF` / 비활성=Ink opacity 35% | |
| Price Input 값/placeholder | Noto Sans KR Bold | 16px | 입력값=Ink / placeholder=Ink opacity 35% | B 전용 |
| Price Input 통화기호·단위(₩, 원) | Noto Sans KR Bold(₩) / Regular(원) | 16px / 14px | ₩=Ink / 원=Ink opacity 60% | B 전용 |

## 3. 보더 / Radius

| 항목 | 값 |
|---|---|
| 카드·구분선 보더 | 1px `#E2E6EC` |
| 상태배지("S급") 보더 | 1px `#DEDEDE` |
| Price Input 보더(포커스) | 1.5px `#3182F6` |
| 선택된 Choice Card 보더 | 2px `#3182F6` |
| 배지(pill) radius | 999px / 100px(AI추천 팁) — 완전한 캡슐형 |
| White Sheet 상단 radius | 24px, **상단만**(하단은 각짐 — 바텀시트가 화면 하단에 붙는다는 것을 형태로 알려주는 비대칭 처리, 실수가 아니라 의도) |
| CTA 버튼 / HeroPriceCard radius | 16px |
| Choice Card radius | 14px |
| Price Input radius | 12px |
| 상품 썸네일(Thumb) radius | 10px |
| 드래그 핸들 radius | 2px |

## 4. 그림자 (Shadow)

**7개 확정 화면 전체에 그림자가 단 하나도 없다.** 카드와 배경, 선택/미선택 상태의 시각적 계층은 전부 색 대비(흰 카드 vs 옅은 배경)와 1~2px 보더만으로 만든다. 이것은 실측 누락이 아니라 이 컨셉의 핵심 스타일 언어다 — 그림자 없는 완전한 플랫함이 "과장 없이 사실만 전달하는" 신뢰 톤을 만든다. design-systems·ui-designer는 이 화면을 확장할 때 임의로 그림자(box-shadow, elevation)를 추가하지 않는다.

## 5. 간격 (Spacing)

2px 단위 그리드를 쓴다(8px 배수가 아닌 이 컨셉 고유의 그리드 단위 — 6/8/10/12/14/16/18/20/24/28/36px가 실제 등장).

**섹션 레벨 padding**
- Dark Hero: `px-20 py-28`, 내부 세로 gap 20px
- White Sheet: `px-20 pt-14 pb-28`, 내부 세로 gap 14px(핸들-콘텐츠)→36px(대구역 간)

**카드 유형별 padding(14~24px 범위의 구체 배분)**
| 카드 유형 | padding | 비고 |
|---|---|---|
| Choice Card(1차 텍스트만, 첫 카드) | `pl-14 pr-36 py-14` | 우측 pr-36은 "AI 추천" 팁 배지·shield-check 아이콘이 얹히는 여백 |
| Choice Card(2차 텍스트, 두 번째 카드) | `pl-14 pr-36 py-14` | 동일 padding, 내부 아이콘-텍스트 gap만 16px→12px로 축소 |
| HeroPriceCard | `px-18 py-24` | 이 컨셉에서 가장 넓은 카드 padding — 가격이라는 핵심 정보에 가장 넉넉한 여백을 줘 시각적 무게를 싣는다 |
| CTA 버튼 | `px-20 py-16` | |
| Price Input | `px-14 py-12`, 고정 높이 46px | B 전용 |
| Product Row(상품 요약 행) | padding 없음, gap 10px | 썸네일-텍스트 간격만 |

**pill 배지 padding**
| 배지 | padding |
|---|---|
| Eyebrow(AI 가격 제안 ENGINE) | `pl-2 pr-12 py-6` |
| 빅데이터 산출 배지 | `px-8 py-4` |
| 유사상품 분석 배지(HeroPriceCard 내부) | `pl-12 pr-16 py-6` |
| AI추천 팁 | `px-12 py-2`, 고정 높이 24px |
| 판매등록희망상품 / 상태(S급) 배지 | `px-10 py-6` |

## 6. 아이콘 / 장식 모티프 (Icon & Illustration Direction)

7개 화면 재열람으로 확인한 아이콘 스펙이다. 라인아이콘(기능성)과 컬러 일러스트 아이콘(선택 옵션)을 명확히 구분해서 쓰는 이중 체계다.

**A. 기능성 라인 아이콘 (단색, UI 컨트롤용)**
| 아이콘 | 크기 | 색상 | 스트로크/면 | 용도 |
|---|---|---|---|---|
| `chevron-right` | 24×24px | 활성=흰색 / 비활성=Ink 35% | 라인 | CTA 버튼("다음 보기") 우측 화살표. 활성·비활성 상태에 따라 같은 SVG를 다른 색 문맥에서 재사용 |
| `star-01` | 12×12px | Primary 계열(스크린샷상 파란색) | 라인/면 혼합(작은 별) | "빅데이터 산출로 제안" 배지 좌측 |
| `shield-check` | 32×32px | 파란 방패 바탕 + 흰색 체크(Primary 톤) | 면(필) | **선택된 Choice Card에만** 등장 — 카드 우측 padding 영역(pr-36) 안에 절대 위치로 얹힘. "이 선택이 확정·보증됐다"는 신뢰 신호를 형태로 전달하는 장치. 미선택 카드에는 존재하지 않는다 |

**B. 옵션 일러스트 아이콘 (컬러, Choice Card 전용)**
| 아이콘 | 크기 | 구성 | 용도 |
|---|---|---|---|
| "아이콘1"(썸업류) | 40×40px | 자체 SVG, 풀컬러 일러스트(스크린샷상 손 제스처 아이콘, 붉은 톤 포함) | "네, 이대로 좋아요" 카드 좌측 |
| "아이콘2"(edit-02) | 40×40px | 파란 원형(Ellipse) 배경 위에 흰색 연필 아이콘을 -3.22도 회전시켜 마스킹 합성 | "아니요, 다르게 하고 싶어요" 카드 좌측. 원형 배경+회전된 라인 아이콘 조합이 "직접 편집한다"는 행위를 은유 |

이 두 아이콘은 라인 아이콘(A그룹)과 달리 색이 있는 원/일러스트 형태라는 점에서 톤이 다르다 — Choice Card처럼 사용자가 직접 고르는 상호작용 지점에는 더 따뜻하고 구체적인 일러스트를, 상태 표시·진행 정보처럼 배경적인 요소에는 절제된 라인 아이콘을 쓰는 것이 이 컨셉의 아이콘 방향이다. graphic-designer가 신규 아이콘을 그릴 때 이 이중 체계(라인=정보/상태, 컬러 원형 일러스트=선택 행위)를 유지한다.

**C. 기타 장식 모티프**
- 드래그 핸들바: `#E2E6EC`, 40×4px, radius 2px — White Sheet 최상단, 바텀시트임을 알리는 최소한의 제스처 힌트.
- 검색 이모지 🔍: 아이콘 에셋이 아니라 실제 이모지 글리프. HeroPriceCard의 "유사 상품 N건을 분석하였습니다" 배지 좌측, `#3182F6` 텍스트 컬러 컨텍스트 안에 위치.
- "인터랙티브" 아이콘(16×16px): Eyebrow 배지 안, "AI 가격 제안 ENGINE" 텍스트 왼쪽의 작은 포인트 아이콘. Eyebrow 배경 자체는 비가시 처리(위 1절 참고)라 다크 배경 위에 아이콘+텍스트만 떠 있는 형태로 보인다.
- 상품 비주얼: 실사 상품 사진(Product Visual Card, Thumb) — 일러스트가 아니라 사진 콘텐츠. radius 16px(대), 10px(소).

**일러스트레이션 방향 요약**: 이 컨셉은 마스코트나 별도 빈 상태(empty state) 그래픽을 쓰지 않는 실용적·정보 중심 톤이다. 장식이 필요한 지점(선택 카드)에만 컬러 원형+라인 합성 아이콘을 최소한으로 배치하고, 나머지는 전부 단색 라인 아이콘 또는 실사진으로 처리한다. 향후 이 화면군에 빈 상태·에러 상태 그래픽이 필요해지면, 화려한 일러스트보다 이 절제된 톤(라인 아이콘 + 옅은 Accent Tint 배경)을 우선 시도할 것을 권장한다.

## 근거

- Figma `SIBLz4S4IZbjabzhMSAgdo`, 확정 섹션 `126:2601`, 화면 7개: Concept A_01(`110:103`)·A_02(`124:890`)·A_03(`124:1149`)·A_04(`124:991`)·B_01(`124:1455`)·B_02(`126:1771`)·B_03(`126:1951`) — 전부 `get_design_context`+`get_screenshot`으로 이번 라운드에 재확인.
- 색상/타이포/보더·radius/그림자/간격 기본 수치는 `.claude/agent-memory/brand-designer.md` 2026-08-25(7차) 로그에 기록된 이전 실측값을 그대로 채택(이번 라운드에서 재검증 목적 재관찰 없이 신뢰).
- 아이콘 스펙(chevron-right/star-01/shield-check/아이콘1·2/드래그 핸들/이모지)과 카드별 padding 구체값은 이번 라운드에서 신규로 재확인.
- 불일치 발견: B_03(`126:1951`)의 "상태: S급" 배지에 `border-[#dedede]` 클래스 누락(A_01~04·B_01·B_02는 존재) — 7차 로그에서 이미 design-systems에 보고된 건과 동일, 이번에도 재확인됨. 확정 화면 자체는 수정하지 않았다.

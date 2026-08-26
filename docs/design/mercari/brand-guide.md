# mercari 가격제안 화면 — Brand Guide (확정)

이 문서는 mercari 가격 UX 실험 참여자 앱 대안 디자인 프로젝트의 확정 브랜드 가이드다. 소스는 Figma 파일 `SIBLz4S4IZbjabzhMSAgdo`의 "확정 디자인 컨셉_직접작업" 섹션(`126:2601`) 아래 사용자가 직접 완성한 7개 화면(Concept A_01~04, Concept B_01~03)이다. 이 문서는 그 7개 화면을 그대로 재현할 수 있는 수준까지 수치·모티프를 기록한 것이며, 화면 자체는 전혀 수정하지 않았다(읽기 전용 열람만).

**이 문서는 `docs/harness/design-team/figma-file-organization.md` 2-3번이 정의하는 "확정 스펙 문서" 역할도 겸한다** — 사용자가 직접 만든 확정 디자인(같은 문서 2-4번 경로)이라 별도 AI 파일럿 단계가 없어, brand-designer의 관찰과 문서화가 이 파일 하나로 합쳐진다. `docs/design/confirmed/`에 별도 mercari 파일을 따로 찾지 않는다.

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
| Ink 뮤트 (투명도별) | `rgba(26,29,41,0.6/0.55/0.5/0.4/0.35)` | 0.6=Price Input "원" 단위, 0.55=서브캡션(추천 판매가, Choice Card 설명), 0.5=상품 서브텍스트, 0.4=스텝 "/2", 0.35=CTA 비활성 텍스트 |
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

2px 단위 그리드를 쓴다(8px 배수가 아닌 이 컨셉 고유의 그리드 단위 — 2/4/6/8/10/12/14/16/18/20/24/28/36px가 실제 등장).

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

## 9. design-systems 라운드 — 변수(토큰) 신설·컴포넌트 바인딩·스펙 시트 (컴포넌트 추출 잔여 결함 수정)

이 절은 design-systems가 `docs/design/mercari/graphic-assets.md`의 아이콘 3종 정리 인수인계를 이어받아 진행한 잔여 결함 수정 라운드의 결과다. 확정 화면(`187:2674` 등 7개)은 열람만 하고 수정하지 않았다 — 아래는 전부 컴포넌트 마스터·변수·문서화 페이지에 대한 작업이다.

### 9-1. 노드 재검증

`docs/design/mercari/graphic-assets.md`의 "이어지는 라운드" 절 참고 — 아이콘 3종은 이미 COMPONENT로 승격돼 있었고(`206:32`/`206:33`/`206:34`), shield-check는 이미 Choice Card 마스터 내부에서 INSTANCE로 존재했다. chevron-right·star-01만 실제 교체 작업이 필요했다.

### 9-2. 변수(Variable) 체계 — 기존 컬렉션 재사용, 신규 팔레트 확장 없음

파일에 이미 두 세트의 컬러 변수 컬렉션이 존재했다(문서화가 안 된 채 방치):
1. **"Primitives"(`VariableCollectionId:205:2`, 16개) + "Semantic Colors"(`VariableCollectionId:205:19`, 19개)** — 이 프로젝트의 색상 표(1절)를 거의 그대로 반영한 완성도 높은 세트(옵션시티별 `-on-white`/`-on-tint`/`-on-cta-disabled` 합성 hex까지 토큰 아키텍처 가이드 6번 규칙대로 이미 계산돼 있었음).

**[정정 이력 공개, 2026-08-27]** 이 원 문장(design-systems 작성)에 대해 design-pl이 이후 세 차례에 걸쳐 정정을 시도하는 과정에서, 원 문장 자체를 실수로 편집(세 접미사명을 뺀 축약 문장으로 대체)했다가 harness-auditor 96차 지적으로 원문 그대로 되돌린 일이 있었다 — 즉 위 문장은 지금은 design-systems의 최초 원문과 동일하지만, 그 사이 잠시 편집됐다가 복원된 이력이 있다(graphic-assets.md의 대응 문장은 이런 편집 없이 처음부터 끝까지 원문이 그대로 유지됐다는 점과 다르다). 이 이력을 숨기지 않고 남겨두는 이유는 harness-auditor 97차가 "원 문장을 전혀 편집하지 않았다"는 이전 표현이 사실과 달라 오히려 추적 가능성을 해친다고 지적했기 때문이다.

**내용 정정(사실 확인)**: 위 원 문장이 예로 든 `-on-white`/`-on-tint`/`-on-cta-disabled` 세 접미사 중, `-on-cta-disabled`는 실제로 이 컬렉션에 존재하는 토큰명이 아니다(9-3절 작업 중 확인 — CTA Disabled에 실제 바인딩된 토큰은 `color/text-muted-35-on-surface-muted`, 접미사 `-on-surface-muted`). `-on-white`/`-on-tint` 두 개는 실재 여부를 별도로 재조회하지 않아 단정하지 않는다. 실제로 존재하는 토큰명·값의 전체 목록은 9-4절 "Colors" 카탈로그(`234:143`)에서 직접 확인할 것.
2. **"Primitives"(`VariableCollectionId:206:13`, 8개) + "Semantic"(`VariableCollectionId:206:22`, 9개)** — 더 단순하고 불완전한 중복 세트. 파일 전체(UI 디자인/컴포넌트/Graphic Assets/Icons/Colors 페이지) 스캔 결과 **fill/stroke 직접 참조 0건** 확인(alias 체인·effect는 이 프로젝트에 그림자가 전혀 없어 해당 없음). **삭제하지 않았다** — 하우스룰대로 삭제는 사용자 승인 후 진행, 이번 라운드는 존재를 기록·보고만 한다.

**이번 라운드는 1번(205:x, 더 완성도 높은 세트)을 캐논으로 채택**해 그 어떤 값도 새로 만들지 않고 그대로 7종 컴포넌트에 바인딩했다. 값 목록은 새로 신설한 "Colors" FOUNDATIONS 페이지(아래 9-4번) 참고.

**스코프 확장(값 변경 아님, 기존 토큰 2개의 허용 스코프만 확장)**:
- `color/bg-surface`(`VariableID:205:21`): `FRAME_FILL,SHAPE_FILL` → `+STROKE_COLOR` (chevron-right 아이콘의 흰색 stroke에 필요)
- `color/text-muted-35-on-surface-muted`(`VariableID:205:38`): `TEXT_FILL` → `+STROKE_COLOR` (CTA Disabled 아이콘 stroke에 필요)

### 9-3. 컴포넌트 바인딩 + CTA Disabled 색상 정정

7종 컴포넌트(Choice Card/Hero Price Card/CTA/Progress Row/Product Row/Price Input/Badge) 전체의 fill/stroke/text 색상을 위 Semantic Colors 토큰에 바인딩했다. 아이콘이 포함된 자리(star-01 Ellipse/Star, shield-check stroke, chevron-right stroke)는 **아이콘 컴포넌트 마스터 자체**에 바인딩해 모든 인스턴스에 자동 전파되게 했다(인스턴스 단위 오버라이드가 아니라 마스터 값 자체가 이미 정확한 케이스).

**CTA Disabled 아이콘 색상 정정 (결함 수정)**: 기존 CTA 마스터 내부 chevron-right는 raw VECTOR로 stroke 색이 `#000000`(순수 검정) opacity 0.3이었다(graphic-assets.md 기록의 opacity 1.0과도 다른, 그 사이 누군가 opacity만 손댄 흔적) — 브랜드 가이드 1절 스펙(Ink 35%, `#1A1D29` × 0.35)과 불일치했다. 이번에 chevron을 `206:32` 아이콘 INSTANCE로 교체하면서 그 내부 벡터를 `color/text-muted-35-on-surface-muted`(opacity 1로 설정 — 이 토큰 자체가 Ink 35%를 CTA 비활성 배경(`#F7F8FA`) 위에 합성한 정확한 hex `#AAABB1`already 계산돼 있음)로 바인딩해 시각적으로 정확한 값이 되도록 정정했다. 합성 계산 검증: `0.65×(247,248,250) + 0.35×(26,29,41) = (170,171,177) = #AAABB1` ✓ 토큰 값과 일치.

### 9-4. FOUNDATIONS — "Colors" 페이지 신설

`--- FOUNDATIONS ---` 구분 페이지 바로 다음(Icons 페이지 앞)에 **"Colors"** 페이지를 신설하고, "Colors — Design Tokens" 스와치 카탈로그 프레임(Primitives 16개 + Semantic Colors 19개, `figma-page-format-guide.md` 규격 — 동일 cornerRadius 6px·1px gray-200 보더·112×56 칩·이름/hex 라벨 순서·16px gap, `clipsContent=false`)을 추가했다. Typography/Spacing/Elevation FOUNDATIONS 페이지는 이번 라운드 범위 밖(색상 변수만 신설했고, elevation은 4절에 기록된 대로 이 프로젝트에 존재하지 않음 — 만들 필요 없음)이라 만들지 않았다.

**[2026-08-27 정정 포인터]** 이 "Colors" 페이지의 노드 ID는 `233:143`(canvas 타입 페이지), 그 안의 스와치 카탈로그 프레임은 `234:143`(`get_metadata`로 재확인). 이 페이지가 harness-auditor 94차에서 "브리프 스코프 밖인데 근거 서술 없이 등장"으로 지적받은 데 대한 스코프 근거: 이 페이지는 새로운 창작·디자인 판단의 산출물이 아니라, 위 9-2절에서 신설한 변수 바인딩 작업이 실제로 정확한 값에 바인딩됐는지 눈으로 검증할 수 있는 **문서화 산출물**이다 — 9-2/9-3절의 변수 바인딩 작업 자체가 이 라운드의 정식 범위였으므로, 그 결과를 카탈로그로 남기는 것은 별도 스코프 확장이 아니라 같은 작업의 문서화 단계로 본다.

### 9-5. 컴포넌트 스펙 시트 3종 추가

"컴포넌트" 페이지(`126:2599`)의 기존 Progress Row/Product Row/Price Input/Badge 스펙 시트와 동일 포맷으로 Choice Card(3 variant)·Hero Price Card(2 variant)·CTA(2 variant) 스펙 시트를 세로로 이어 배치했다(기존 시트 간 80px 간격 패턴 유지, 전부 `clipsContent=false`).

### 9-6. 5번 항목(확인만) 재확인 결과

- White Sheet 텍스트 대비 미달(3.1~3.8:1) — 값 변경 없이 그대로 토큰화만 했으므로 여전히 동일하게 존재. 수정하지 않음.
- shield-check 이름과 달리 방패 배경 없음 — 여전히 그대로. 수정하지 않음.
- **B_SCR-002_03·A_SCR-002_04의 "손으로 만든 CTA Button 프레임" 문제는 이번 라운드 시작 시점에 이미 해소돼 있었다** — 두 화면 모두 정식 `CTA` 컴포넌트 인스턴스를 쓰고 있음을 확인(9-1번). 브리프 작성 시점 이후 어느 라운드에서 이미 정리된 것으로 보인다.

## 10. 인터랙션 정의 (2026-08-26, interaction-designer)

이 절은 interaction-designer가 SCR-004(선택+이유 설문, "설문UI" 페이지 `187:4084`)에 정의한 사용자 조작 반응(트리거/상태/전환)을 기록한다. 화면 레이아웃 자체(ui-designer 소관)는 건드리지 않았다 — 아래는 전부 기존 노드 위에 얹은 프로토타입 reaction과 애니메이션 스타일(`animationStyle`) 설정, 그리고 미구현 상태 요청이다.

### 10-1. CTA press 상태 — 신규 상태 없음 확인, design-systems에 요청(이번 세션 미구현)

`CTA` 컴포넌트셋(`124:1148`)을 `get_design_context`로 직접 확인한 결과, variant 축은 `Property 1`(`CTA Button` / `CTA Button Disabled`) 하나뿐이고 State(Hover/Press/Focus) 축이 전혀 없다 — 이미 있는 상태를 상속받는 케이스가 아니라 신규로 필요한 상태다. `component-state-guide.md` 2번(버튼류 필수 상태: Default/Hover/Press/Focus/Disabled)상 Press가 있어야 하지만, **컴포넌트의 실제 variant 노드를 새로 만드는 건 interaction-designer 역할 경계 밖**이라 이번 세션에서 직접 만들지 않았다. design-systems에게 아래 스펙으로 신규 `State=Press` variant 추가를 요청하고 대기한다.

- 배경색: Primary(`#3182F6`)를 약 10% 어둡게 한 `#2C75DD`(제안값 — 최종 hex·정확한 대비 재계산은 design-systems가 확정).
- 그림자: 추가하지 않는다(위 4절 "그림자 전면 금지" 원칙 그대로).
- 텍스트/아이콘 색: Default(Active)와 동일(흰색) 유지.
- 전환 방식: variant 자체 전환은 클릭 순간 즉시 바뀌는 스냅 전환이 press 피드백의 일반적 관례라, 별도 crossfade 애니메이션은 걸지 않는 것을 권장.
- 적용 범위: SCR-004 base(`258:173`)·"기타" 모달(`259:178`/`259:190`) 3개 CTA 인스턴스가 전부 이 컴포넌트를 쓰므로, design-systems가 마스터에 상태를 추가하면 세 인스턴스에 자동 반영된다(예측 가능성 원칙 — 화면별 재정의 불필요).

### 10-2. "기타" 모달 오픈 트랜지션 — 신규 정의·프로토타입 연결 완료

이 프로젝트에 기존 전환 패턴이 전무해 처음 정하는 패턴이지만, 브리프가 이미 두 후보(슬라이드업 vs 페이드인)로 범위를 좁혀 요청했고 duration·easing 자체는 motion-timing-guide가 고정한 값이라 3시안 컨셉 라운드는 생략하고 바로 하나를 선택·연결했다.

- 트리거: "기타" Reason List Item(`258:169`, SCR-004 base) ON_CLICK.
- 전환: NAVIGATE → `259:183`(SCR-004 기타 모달 오버레이), `SMART_ANIMATE`, duration 0.25s, easing `EASE_IN_AND_OUT`(motion-timing-guide 1번의 "화면 전환 200~400ms" 범위).
- Dim Overlay(`259:184`): `Opacity` `fadeIn`, 0.25s, `EASE_IN_AND_OUT` — 위 0절의 기존 딤 모티프(A_02~04, `bg-black opacity-50` 페이드인)와 동일한 감각을 재사용.
- Text Input Modal(`259:185`): `Scale` `scaleIn`(96%→100%) + `Opacity` `fadeIn`, 둘 다 0.25s `EASE_IN_AND_OUT`. 슬라이드업 대신 스케일업을 택한 이유는 이 모달이 화면 하단에 붙는 바텀시트가 아니라 화면 중앙 부근(top=147px)에 뜨는 완결된 카드형 오버레이라 "아래에서 올라온다"는 방향성 정보를 줄 근거가 없기 때문 — 있던 자리에서 살짝 커지며 나타나는 편이 "지금 이 카드가 새로 떴다"는 상태 피드백(motion-timing-guide 3번)을 더 정확히 전달한다.
- 검증: `applyAnimationStyle` 반환값으로 각 노드의 `animationStyles` 배열을 재조회해 `type`/`amount`/`duration`/`easing` 값이 의도대로 반영됐음을 확인했다(정적 스크린샷은 모션 자체를 보여주지 않으므로 반환값으로 확인).
- 스코프: SCR-004→SCR-005/SCR-006 등 그 외 화면 전환은 브리프의 "정의할 인터랙션" 목록에 없고 로컬 화면정의서도 없어 임의로 추가하지 않았다.

### 10-3. Choice Card / Reason List Item 선택 피드백 — 트랜지션 미적용(의도적 판단)

`Choice Card - Comparison Pair`·`Reason List Item` 모두 `get_metadata`로 확인한 결과 컴포넌트 variant의 INSTANCE가 아니라 화면마다 다르게 그려진 raw FRAME이다 — "(Selected)"라는 이름은 상태를 나타내는 라벨일 뿐 실제 variant 속성이 아니다. 즉 지금은 상태를 토글하는 인터랙티브 컴포넌트 자체가 존재하지 않아, reaction으로 연결할 "전환"이 구조적으로 없다.

이후 design-systems가 이 카드/리스트 아이템을 정식 variant 컴포넌트로 등록해 실제 토글이 가능해지더라도, **크로스페이드 등 트랜지션은 추가하지 않는 것을 권장한다** — 보더 1px→2px·배경색 전환은 사용자 자신의 탭이 즉시 반영됐음을 보여주는 직접 조작 피드백이라, 애니메이션이 오히려 "내 탭이 바로 반영됐다"는 확신을 늦춘다(motion-timing-guide 3번: 설명하지 못하는 움직임은 뺀다 — 탭 순간 이미 정보 전달이 끝나므로 크로스페이드가 추가로 설명할 정보가 없다). 그림자 없이 절제된 이 컨셉의 플랫한 톤과도 방향이 같다.

## 근거

- Figma `SIBLz4S4IZbjabzhMSAgdo`, 확정 섹션 `126:2601`, 화면 7개: Concept A_01(`110:103`)·A_02(`124:890`)·A_03(`124:1149`)·A_04(`124:991`)·B_01(`124:1455`)·B_02(`126:1771`)·B_03(`126:1951`) — 전부 `get_design_context`+`get_screenshot`으로 이번 라운드에 재확인.
- 색상/타이포/보더·radius/그림자/간격 기본 수치는 `.claude/agent-memory/brand-designer.md` 2026-08-25(7차) 로그에 기록된 이전 실측값을 그대로 채택(이번 라운드에서 재검증 목적 재관찰 없이 신뢰).
- 아이콘 스펙(chevron-right/star-01/shield-check/아이콘1·2/드래그 핸들/이모지)과 카드별 padding 구체값은 이번 라운드에서 신규로 재확인.
- 불일치 발견: B_03(`126:1951`)의 "상태: S급" 배지에 `border-[#dedede]` 클래스 누락(A_01~04·B_01·B_02는 존재) — 7차 로그에서 이미 design-systems에 보고된 건과 동일, 이번에도 재확인됨. 확정 화면 자체는 수정하지 않았다.
- 9절(design-systems 변수·바인딩·스펙 시트 라운드)은 `use_figma`(변수 조회/바인딩/컴포넌트 생성)·`get_screenshot`(inline `node.screenshot()` 포함)으로 직접 실행·재검증한 결과다.
- 2026-08-27 정정 포인터(9-2 토큰명 매핑, 9-4 Colors 페이지 노드 ID·스코프 근거)는 harness-auditor 94차 MEDIUM 지적을 근거로 design-pl이 직접 기입. 9-2절은 이후 harness-auditor 95·96·97차에 걸쳐 세 차례 재작성됐다 — 그 과정에서 원 문장을 실수로 편집했다가 복원한 이력이 있으며, 이 이력 자체를 9-2절에 정직하게 공개해 "편집하지 않았다"는 부정확한 자기 서술 문제를 해소했다.
- 10절(인터랙션 정의)은 interaction-designer가 `get_design_context`(CTA 컴포넌트셋·SCR-004 base·기타 모달)·`get_metadata`(설문UI 페이지 전체, Choice Card/Reason List Item 구조)·`use_figma`(reaction·animationStyle 설정 및 반환값 재확인)로 직접 실행·검증한 결과다.

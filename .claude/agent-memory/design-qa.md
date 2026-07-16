# design-qa 메모리

이 파일은 design-qa가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 작업 로그

### 2026-07-15 (18차) — Checkbox 컴포넌트(`474:899`, 0-17절/14절) 신규 등록분 독립 재감사

**HIGH(신규) — Label 텍스트 paint opacity 0.5가 Default/Checked/Focus 3개 variant 전부에서 누락**: 원본 `247:6825`는 rgba(26,26,26,0.5)인데 등록 컴포넌트는 풀 오퍼시티로 바인딩. **(18-1차, 0-18절에서 design-systems가 raw script 재조회 결과 실제로는 4곳 모두 opacity 0.5로 이미 정확히 반영돼 있었음을 확인 — design-qa의 FAIL 판정은 `get_design_context`(className 기반)에 의존한 오탐으로 정정됨. 이후 감사에서는 opacity 검증 시 codegen보다 raw script/스크린샷을 우선할 것.)**

**HIGH(신규) — Disabled variant Box fill/stroke paint opacity 0.5가 반영되지 않음**: 위와 동일한 오탐 패턴으로 추정, 0-18절에서 정확히 반영돼 있음이 재확인됨.

**PASS — 나머지 항목**: Box 크기/색, Checked 체크마크, Focus 순수성(링 색 자체는 시스템 공통의 raw hex 하드코딩 기존 갭, 9-4절 기 문서화 — Checkbox 신규 결함 아님), TEXT 프로퍼티, 스펙 시트, 라디오/디바이더 판단 근거, 원본 무수정.

**종합(정정 반영)**: opacity 관련 2건은 design-systems 재조회로 실제로는 이상 없음 확인됨 — **codegen(get_design_context)로 opacity를 판정하면 오탐이 난다는 교훈**을 다음 라운드에 반영(19차부터 실제 적용). LOW 1건(페이지 순서 도구 한계로 완전 재확인 불가).

### 2026-07-16 (19차) — Stage2 확정 디자인 세트(8프레임) 토큰 바인딩 반영분(0-20절) 독립 2차 검증

배경: design-systems가 Stage1(실측+diff+토큰 신설)·Stage2(컴포넌트 리바인딩+문서 갱신) 2단계로 새 확정 디자인 세트(`501:2505` 하위 8프레임)를 반영 완료, 자체 재대조도 마쳤다고 보고. 사용자가 "토큰과 스타일은 컴포넌트에 꼭 연결되어 있어야한다"고 강조해 design-qa가 독립적으로 재검증(1건 제외 opacity codegen 오탐 교훈 반영 — 이번엔 raw hex 판정에 `get_design_context`(className) + `get_screenshot`(시각/픽셀 비교) 병행 사용, opacity는 다루지 않는 라운드라 해당 리스크 낮음).

**감사 대상 8건 전부 PASS — hex·바인딩 확정 프레임과 정확히 일치**: Sidebar Nav Item/Card/Icon Alert/NeoBtn/Button/Link/Checkbox/Contact Row 전부 확인(상세는 git 이력 참고).

**의도된 예외 3건 — 정확히 그렇게 처리됐음을 확인(결함 아님)**: main-삭제/main-알림창 구값 잔존(read-only 방침), 헤더 로그아웃 NeoBtn 미토큰화, main-검색없음 "전체 보기" 버튼 신규 variant 보류.

**Colors 카탈로그(`95:2`) 갱신 확인 — PASS(당시)**: "Stage2 신규 Primitives(6개)"/"Stage2 신규 Semantic Colors(7개)" 섹션(`625:1078`/`625:1104`) 존재, 13개 스와치 hex 전부 일치 — **단, 이 섹션은 이후 0-21절에서 임시 섹션으로 재판정되어 정식 Primitives(`95:44`)/Semantic(`95:123`) 그리드로 통합·삭제됨(20차에서 재확인).**

**design-system.md 문서 상태 — PASS**: 845줄, 손상 없음.

**MEDIUM(신규) — NeoBtn/Sidebar Nav Item 스펙 시트 캡션 텍스트, 0-20절의 "갱신 완료" 주장과 실제 불일치**: Link/Checkbox 캡션은 Stage2 문단 반영됐으나 NeoBtn(`342:5`)/Sidebar Nav Item(`343:1108`) 캡션은 구 설명 그대로 — 이후 별도 라운드에서 정정 완료(0-20절 각주에 반영 확인, 20차에서 재확인).

**종합**: 8건 전부 PASS, 의도된 예외 3건 확인, MEDIUM 1건(문서 서술 부정확) — 이후 정정 완료.

### 2026-07-16 (20차) — Disabled 색 토큰화 라운드(Stage2-a/b/c, 0-22/0-23절) 독립 재검증

배경: opacity 기반 Disabled → 색 토큰 기반(bg-disabled/border-disabled/text-disabled) 전환 라운드 완료 보고에 대한 독립 재감사. 특히 "FOUNDATIONS 스와치가 또 다른 별도 임시 섹션에 들어간 것 아니냐"는 사용자 의심 지점을 최우선 검증.

**HIGH(신규, 최우선) — FOUNDATIONS Colors 페이지, 신규 Disabled 토큰 4종이 정식 Primitives(`95:44`)/Semantic(`95:123`) 그리드가 아니라 별도 병렬 섹션("신규 Primitives" `436:3`, "Semantic Colors (Additional)" `436:143`, 둘 다 0-14절 기원)에 추가됨**. 바로 앞선 라운드(0-21절)가 정확히 이 파편화 패턴("Stage2 신규" 임시 섹션 `625:1077~1104`)을 정리해 "신규 토큰은 정식 Primitives/Semantic 그리드에 통합"이라는 원칙을 확립했는데, 0-23절 6항은 "0-21절 관례를 그대로 따랐다"고 서술하면서도 실제로는 0-21절이 정리한 대상이 아닌 별개의 기존 병렬 섹션(`436:3`/`436:143`)에 추가해 동일한 파편화가 재현됐다 — 문서 서술도 이를 "관례 준수"로 잘못 기술. 부수: `436:2` 제목이 gray/425 추가 후에도 "22개"로 카운트 미갱신(실제 23개). **개선안**: gray/425(`650:2`)→`95:44`, bg/border/text-disabled(`650:6/10/14`)→`95:123`으로 재통합, 또는 최소 0-23절 서술과 `436:2` 카운트 정정. **(21차에서 완전히 재통합 완료 확인됨 — 아래 참고.)**

**PASS — 토큰 값**: `color/bg-disabled`(`643:2`)=#929292(gray/425), `border-disabled`(`643:3`)=#5C6366(gray/600), `text-disabled`(`643:4`)=#555555(gray/650) raw 스와치 재조회로 정확히 일치.

**PASS — 4개 컴포넌트 적용**(NeoBtn/Button/Table Row Action/Checkbox Disabled variant): className 바인딩 + 스크린샷 시각 확인 둘 다 통일된 회색 톤, opacity 1 정상 확인.

**PASS — Input 예외**(NeoInput `644:2`/CornerInput `644:963`): 배경/보더만 disabled 토큰, 텍스트는 `color/ink/900` 유지, `text-disabled` 미사용 확인 — 지시대로 정확.

**PASS — 문서 정합성**: design-system.md 900줄 전체 Read, 손상 없음(절 번호 연속 0-1~0-23/1~12절). 9-1/9-4/5절/7-2절 전부 최종값과 Icon Button/Row Action Button 미적용 TODO 정확히 반영.

**참고(HIGH/MEDIUM 아님)**: Icon Button/Row Action Button Disabled 미적용은 문서화는 정확하나, 사용자 원문("버튼, Table Row Action") 범위에 포함될 가능성 있어 design-pl 통해 재확인 권장.

**종합**: HIGH 1건(FOUNDATIONS 섹션 파편화 재발), 나머지 전부 PASS.

### 2026-07-16 (21차) — FOUNDATIONS Colors 섹션 완전 재통합(0-23절 6항 정정분) 재검증

배경: 20차에서 지적한 HIGH(신규 Disabled 4종이 `436:3`/`436:143` 병렬 섹션에 추가됨)에 대해, design-systems가 재조사 결과 이 두 섹션이 이번 라운드가 만든 게 아니라 0-14절부터 존재해온 미통합 레거시(각 22/13개, 총 35개 기존 스와치)였음을 확인하고, 4종만 빼내는 대신 **두 섹션 전체(39개)를 정식 Primitives(`95:44`)/Semantic(`95:123`) 그리드로 완전 통합**하고 빈 섹션 프레임 4개(`436:3`/`436:143`/`436:2`/`436:142`)를 삭제했다고 보고. 독립 재검증 수행.

**PASS(1) — 임시 섹션 표시 완전 제거 확인**: `get_metadata`로 Colors Root(`95:40`) 전체 재조회 — 자식 섹션이 Primitives/Semantic/Contrast Notes/Category Colors/Component Colors 5개뿐, "신규"/"Additional"/"Stage2" 텍스트 노드 0건. `get_screenshot`(전체 페이지)로도 육안 재확인, 잘림/겹침 없음.

**PASS(2) — 4개 노드 삭제 확인**: `436:3`/`436:143`/`436:2`/`436:142` 각각 `get_metadata` 직접 재조회 결과 전부 "not found"(삭제 확인).

**PASS(3) — 39개 스와치 정식 그리드 편입 확인(스팟체크)**: Primitives Row(`95:44`) 39개(기존 16 + 신규 23, gray/425 `650:2` 포함) 전수 나열 확인, Semantic Row(`95:123`) 31개(기존 15 + 신규 16, bg-disabled/border-disabled/text-disabled `650:6`/`650:10`/`650:14` 포함) 전수 나열 확인 — hex·alias 라벨(gray/425=#929292, bg-disabled=alias gray/425 등) 전부 0-23절 문서값과 일치.

**PASS(4) — Variable 실제 바인딩 회귀 없음(대표 3종 스팟체크)**: 기존 정상 작동 토큰(`color/background`=alias gray/50 `95:124`, `color/teal/500` `95:45`)은 여전히 실제 CSS var(`var(--color-background,...)`, `var(--color-teal-500,...)`)로 바인딩 확인. 신규 Disabled 토큰도 실사용 컴포넌트에서 무결 확인 — NeoInput Disabled(`644:2`) bg=`var(--color-bg-disabled,#929292)`/border=`var(--color-border-disabled,#5c6366)`/텍스트는 여전히 `var(--color-ink-900,#1a1a1a)`(text-disabled 미사용 원칙 유지), Checkbox Disabled Box(`474:893`) 동일 패턴 확인. 재통합 과정에서 실제 컴포넌트 바인딩 손상 없음.

**PASS(5) — design-system.md 정합성**: 901줄 전체 Read, 손상 없음(절 번호 연속 0-1~0-23/1~12, 표 깨짐·중복 없음). 0-23절 6항 서술("두 섹션 전체 39개를 정식 그리드로 통합, 헤더+빈 프레임 4개 삭제")이 Figma 실측과 정확히 일치.

**LOW(관찰, 이번 라운드 결함 아님) — FOUNDATIONS 카탈로그 스와치 자체의 바인딩 불균일**: 신규 통합된 레거시 섹션 출신 스와치들(예: `650:6` bg-disabled, `436:4` ink/800, `625:1079` sky/500)은 rectangle fill이 raw hex(`bg-[#929292]` 등, var() 아님)로만 그려져 있고 실제 Figma Variable에 바인딩돼 있지 않다 — 반면 원래부터 있던 핵심 스와치(`95:45` teal/500, `95:124` background)는 CSS var로 정상 바인딩. 단, `625:1079`(0-20/21절, 이번 라운드 이전 생성)도 이미 미바인딩 상태였음을 확인해 **이번 재통합이 새로 만든 문제가 아니라 0-14절부터의 기존 카탈로그 제작 관행**으로 판단됨. 실사용 컴포넌트(NeoInput/Checkbox 등)는 전부 정상 바인딩이라 실질 영향 없음 — 카탈로그 페이지 자체의 스와치를 향후 라이브 바인딩 방식으로 통일할지는 별도 라운드 판단 사항으로 기록만 남김.

**종합**: 20차 HIGH 완전히 해소 확인(전부 PASS). 신규 LOW 1건(카탈로그 스와치 미바인딩, 기존 관행/실질 영향 없음, 결함 아님·참고 기록).

### 2026-07-16 (22차) — 확정 8프레임 전수 대조 후속 반영 P1~P15(13절) 독립 재검증

배경: 34차 전수 대조로 발견된 15건(P1~P15) 중 11건 REFLECT/4건 조치없음 처리 완료 보고에 대한 독립 재감사. `use_figma`(raw script) 도구가 없어 전부 `get_design_context`/`get_metadata`/`get_screenshot` 조합으로 검증(고배율 스크린샷을 raw 색상 판정의 1차 근거로 우선 사용, 18차 opacity 오탐 교훈 반영).

**HIGH(신규, 최우선) — P12 Checkbox 체크마크(`474:888`) 색상, design-system.md의 "ink/900로 정정 완료" 서술과 실제 렌더링 불일치 의심**: State=Checked(`474:896`) 박스를 `get_screenshot`으로 네이티브 해상도(14×14) 확대 확인한 결과, 체크마크가 밝은/흰색 계열로 보이고 ink(#1A1A1A) 검정으로 보이지 않는다. 같은 파이프라인의 State=Default(`474:895`, 2px ink 보더가 뚜렷한 검정으로 렌더링됨)를 대조군으로 삼아 비교했을 때 체크마크 톤이 명백히 더 밝다 — ink 검정이라면 sky/500(#1395E6) 배경 위에서 뚜렷한 어두운 마크로 보여야 하는데 실제로는 반대로 밝게 보인다. `get_design_context`는 이 노드를 boolean 그룹 이미지로 플래튼해 className에 색상 텍스트가 노출되지 않아 hex 자체는 확정할 수 없었다(raw script 부재로 인한 도구 한계) — 그러나 시각적 증거는 P12가 주장하는 "border-divider-cool(옅은 하늘색)→ink/900(검정) 정정"이 실제로 반영되지 않았거나, 반영됐어도 흰색 등 전혀 다른 값으로 렌더링되고 있음을 시사한다. **개선안**: design-systems가 `474:888`의 stroke boundVariable/hex를 raw script로 직접 재조회해 실제 값을 확인하고, ink/900이 아니면 재정정 후 다시 스크린샷 검증할 것 — 이번 항목은 "최우선" 지정 항목이라 재확인 없이 넘기지 않는다.

**PASS — P1**: NeoBtn(`259:126`) ComponentSet에 `712:2`(Sky)/`712:4`(Navy)가 정상 위치(x=3016/3086, 기존 variant열 바로 뒤)로 편입 확인. fill/텍스트 전부 `var(--color-bg-brand-blue)`/`var(--color-ink-900)`/`var(--color-bg-accent-navy)`/`var(--color-text-inverse)` 토큰 바인딩(raw hex 없음). WCAG 상대휘도 공식 독립 재계산 결과 Sky+ink=5.363:1, Navy+white=8.907:1 — 문서 기재값(5.36/8.91)과 소수점까지 일치.

**PASS — P2**: RowActionButton Danger/Default(`260:53`) bg=`var(--color-bg-cta-amber,#ffce2c)`, border=`var(--color-ink-900,#1a1a1a)` 1px 확인. Neutral(`260:34`)은 `var(--component-row-action-button-border-neutral,#1c1f21)` 그대로 무수정 확인.

**PASS — P4**: NeoInput 4개(`261:10`/`378:4`/`398:884`/`398:888`) 전부 drop-shadow Hard-2 확인, Focus(`398:886`/`456:2`)·Disabled(`644:2`) 전부 제외 확인. NeoSelect Default 2개(`261:660`/`401:866`) Hard-2 확인, Open 2개(`387:12`/`401:869`) 트리거는 Hard-2 없이 옵션패널만 Elevation/Raised — 이중 그림자 방지 정확히 반영.

**PASS(값) / MEDIUM(문서 서술) — P5**: CountPill Active(`258:12`)에 drop-shadow Hard-1 실제 적용 확인(PASS). 단 컴포넌트 자체의 Figma description이 "Active=흰 배경, 그림자 없음"으로 이번 변경 이전 서술 그대로 남아 있어 실제 상태와 모순 — 컴포넌트 description 필드 자체가 SoT 중 하나인데 갱신 누락. NeoBtn(`259:126`) description도 P1(Sky/Navy 추가)·P11(Amber ink 보더 추가)을 반영하지 않고 구 서술 그대로.

**PASS — P6/P7**: Icon Button 5 State 중 3개(`259:610`/`284:1040`/`284:1042`) className에 rounded 클래스 없음(radius 0) 확인. Card Modal(`262:6`)/Auth(`262:10`) 동일하게 radius 0 확인.

**PASS — P8**: Modal(`262:7`) border-b-2 ink-900, Auth Top(`262:11`) border-b-2 ink-900, Auth Bottom(`262:14`) border-t-2 ink-900 전부 확인.

**PASS — P9/P3/P13/P15(조치 없음 항목)**: CornerInput 7 variant 전수 조회 결과 CornerBracket 잔존 0건(P9 결론 유지 확인). RowActionButton Neutral 위 P2에서 재확인(무수정). Sidebar Nav Item(`258:29`)은 Active/Inactive/Focus 3 variant만 존재, 신규 이례값 반영 없음 확인(P13). P15는 원본 확정 프레임 대상이라 감사 범위 밖(손대지 않음 원칙) — 마스터 쪽엔 애초에 대응 항목 없음 확인.

**PASS — P10**: CornerInput 7 variant(`261:12`/`378:856`/`398:890`/`398:892`/`398:894`/`456:4`/`644:963`) 전부 text-[13px] 확인.

**PASS — P11**: NeoBtn Amber Default(`259:110`)/Focus Default(`284:115`)/Focus Compact(`284:155`), Button Amber Default(`259:603`)/Focus(`284:1010`) 전부 border-2 ink-900 확인. Focus는 border 추가 후에도 FocusRing 오버레이(ink, border-3) 그대로 유지 — Default와 배경/텍스트 동일, 차이는 보더(모든 State 공통 추가)+링뿐이라 순수성 위반 아님.

**PASS — P14**: Toast Success subtitle(`263:45`) `var(--color-text-muted-toast,#5c6366)` 바인딩 확인, title은 `var(--color-ink-900,#1a1a1a)` 유지 확인.

**PASS — FOUNDATIONS Colors(`95:2`)**: `716:6`(text-muted-toast 스와치)가 정식 Semantic Row(`95:123`) 그리드 안에 위치(마지막 자식), Colors Root(`95:40`)는 여전히 5개 섹션(Primitives/Semantic/Contrast Notes/Category Colors/Component Colors)뿐 — "신규"/"Stage2"/"Additional" 병렬 섹션 재발 없음.

**PASS — 문서 손상 여부**: design-system.md 965줄, 1~230행/230~539행/700~965행 샘플링 결과 절 번호 연속(0-1~0-24, 1~13절), 중복·누락·표 깨짐 없음.

**PASS — `.claude/agents/design-systems.md` 원칙 추가**: "색상 등 시각 속성도 인스턴스 단위 오버라이드로 처리한다" 항목이 기존 판단 기준 불릿 리스트 중간(23번째 줄)에 자연스럽게 삽입돼 있고, 앞뒤 기존 항목 삭제·손상 없음.

**LOW(관찰, 이번 라운드 결함 아님) — Focus 링이 문서(9-1절, 2겹 DROP_SHADOW)와 실제 구현(별도 "FocusRing" 오버레이 자식 노드, border-3 ink solid) 방식이 다름**: NeoBtn/Button/NeoInput/CornerInput/Icon Button Focus variant 전수에서 일관되게 관찰됨 — 이번 라운드(P1~P15) 이전부터의 기존 구현 방식으로 이번 라운드가 새로 만든 회귀는 아니다(모든 Focus에서 색·굵기 일관). 다만 NeoInput/CornerInput의 Error×Focus 조합(`456:2`/`456:4`)도 에러 상태임에도 링이 빨강이 아니라 ink로 렌더링되어, 9-1절이 문서화한 "에러 상태는 흰갭+빨간 링" 표준과 다르다 — 결함이라기보단 문서-구현 표기 불일치이자 향후 점검 후보로만 기록.

**종합**: HIGH 1건(P12 체크마크 색상, 최우선 재확인 필요), MEDIUM 1건(CountPill/NeoBtn description 미갱신), LOW 1건(Focus 링 구현방식 문서 불일치, 결함 아님). 나머지 12개 항목 전부 PASS — hex/바인딩/구조 모두 문서 기재값과 일치 확인.

# design-qa 메모리

이 파일은 design-qa가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 작업 로그

### 2026-07-15 (14차) — 등록된 전체 컴포넌트 토큰 바인딩 전수 재감사(사용자 직접 요청, 스팟체크 아닌 전수 감사)

`docs/design/design-system.md` 5절(컴포넌트 표)을 근거로 삼으려 했으나 **HIGH(신규, 최우선) — design-system.md 소스 오브 트루스 파일이 심각하게 손실된 상태**임을 발견: `Read` 전체 조회 결과 파일이 단 61줄뿐이고, 내용은 문장 중간에서 시작하는 조각 + "9-6절"/"0-11절"/"0-12절" 3개 섹션만 존재 — section 1~4/6~8(컴포넌트 표, 페이지 순서 표 등)/9(인터랙션 상태)가 전부 없음. **(15차 갱신) 이후 design-pl/design-systems가 git 이력+사고 직전 컨텍스트로 624줄 전체 복구 완료 확인, 아래 15차 참고.**

이 손실 때문에 각 컴포넌트의 nodeId를 design-system.md가 아니라 4개 에이전트의 agent-memory 로그를 전수 검색해 재구성한 뒤 대표 variant 1~2개씩만 감사했다(총 13개 중 12개, Contact Row는 nodeId 미확인으로 보류) — 결과: 하드코딩 발견 0건, HIGH 1건(문서 소실).

### 2026-07-15 (15차) — 문서 복구 후 전체 컴포넌트 전수 재감사 + TypeSelector/NeoInput/CornerInput/NeoSelect 독립 재확인 + Focus 순수성 전수 확인(사용자 직접 요청)

design-system.md가 624줄로 복구된 뒤, 사용자 요청으로 "스팟체크가 아닌 진짜 전수 감사"를 수행. 총 16개 컴포넌트를 `get_design_context`로 직접 재조회(TypeSelector·NeoInput·CornerInput·NeoSelect·NeoBtn·Button·Icon Button·Row Action Button·Table Row Action·Sidebar Nav Item·CatBadge·Contact Row·Card·Toast·Logo·Avatar), 대표 spec sheet 3개는 `get_screenshot`으로 시각 재확인.

**최우선 재확인(0-9/0-10절, 문서 복구 후 미커밋 구간) — 전부 PASS, 불일치 없음**:
- TypeSelector(`257:28`): Selected 4종 hex 전부 doc과 정확히 일치(family #ffe4e8/#ff5a76/#a8003b, company #d8fff5/#17a398/#0a4f49, other #ede0ff/#9b72cf/#4b0d9c, friend #e0f0ff/#4a90d9/#1a4c88), Unselected 보더 `component/typeselector-unselected-border`(#ccc) 일치.
- NeoInput(`288:12`)/CornerInput(`288:27`): Error=No/Yes × Focus=No/Yes × Content 매트릭스, nodeId·variant 개수(7개)·색상(border-error #ff5a76, text-error #a8003b, NeoInput placeholder #bbb vs CornerInput placeholder #ccc 분리 유지) 전부 doc과 일치.
- NeoSelect(`387:13`): State=Default/Open × Content=Placeholder/Selected 4 variant, hover 옵션 `color/bg-hover-muted`(#f1f1f1) 바인딩, Elevation/Raised 적용 전부 일치.

**HIGH(신규) — Button(`259:609`) Style=Amber, State=Focus(`284:1010`) 스퓨리어스 보더**: Amber Default/Hover/Press/Disabled/Loading 어디에도 보더가 없는데, Focus 상태에서만 `border border-black border-solid`(1px 검정)가 코드에 추가로 붙어있음을 발견 — `get_screenshot`(스펙 시트 `343:50`)으로 시각 재확인 결과 Amber Focus 버튼에만 실제로 얇은 검은 테두리가 렌더링됨(Default/Hover/Press/Disabled/Loading은 테두리 없음, Coral/Neutral Focus는 이 문제 없음). NeoBtn(`259:126`, 스펙 시트 `342:3`)의 동일 Amber/Focus는 이 문제가 없음을 대조 확인 — Button 컴포넌트 1건에 국한된 버그. Focus 순수성 원칙(9-1절: 링 추가 외 배경/보더/텍스트 불변) 위반. **위치: Button 컴포넌트, Style=Amber, State=Focus, node `284:1010`, Component Specs 페이지 `343:50`.** **(16차 갱신) 이후 12-1절에서 정정 완료.**

**MEDIUM(신규) — 버튼류 5개 컴포넌트 Focus 배경 fill 토큰 미바인딩(하드코딩), 광범위**: NeoBtn/Button/Icon Button/Row Action Button/Table Row Action의 Focus variant는 예외 없이 배경을 raw hex(`bg-white`, `bg-[#ffcb47]`, `bg-[#17a398]` 등)로 직접 지정하고 있고, 같은 Style의 Default 형제는 전부 `var(--color-*)` 토큰으로 바인딩돼 있음. **(16차 갱신) 이후 12-2절에서 정정 완료(design-system.md 5절 표에 반영 확인).**

**LOW(신규) — Contact Row(`351:299`) 루트 배경 `bg-white` 하드코딩**: **(16차 갱신) 12-3절에서 정정 완료(design-system.md 5절 표에 반영 확인).**

**Focus 순수성 전수 확인 결과(위 Button/Amber 1건 제외 전부 PASS)**: TypeSelector·NeoInput/CornerInput·Sidebar Nav Item·NeoBtn·Icon Button/Row Action Button/Table Row Action 전부 배경·보더·텍스트 Focus=No/Yes 동일, 링만 추가.

**나머지 컴포넌트 재확인**: CatBadge/Card/Toast/Logo/Avatar 전부 PASS, 하드코딩 없음.

**종합**: HIGH 1건, MEDIUM 1건, LOW 1건 — 전부 16차 이전 라운드(12-1/12-2/12-3절)에서 정정 완료 확인.

### 2026-07-15 (16차) — Focus 축을 State 열거형 값으로 소급 통합(0-15절, TypeSelector/NeoInput/CornerInput/Sidebar Nav Item 4개) 스팟체크

사용자가 "[메인 세션 확인] 사용자가 실제로 승인함" 형식으로 승인한 순수 구조 재편(시각 변경 없음, 이름/속성만 재편) 작업을 감사.

**PASS(1) — TypeSelector(`257:28`)**: `get_metadata`로 12 variant(Category(4)×State=Selected/Unselected/Focus(3)) 정확히 확인 — Friend/Family/Other/Company 각 3개씩. 스크린샷(스펙시트 `343:1146`)으로 Selected/Unselected 색상 과거와 동일 확인, Focus 4종은 Unselected 룩 + 포커스 링 유지 확인. ComponentSet 설명 필드에 "Focus=No/Yes" 잔재 없음(새 formula로 정확히 갱신됨).

**PASS(2) — NeoInput(`288:12`)/CornerInput(`288:27`)**: 각 5 variant(Content=Filled/Placeholder × Error=No/Yes(4) + 단일 State=Focus(1)) `get_metadata`로 정확히 확인. 스크린샷(스펙시트 `344:721`/`344:740`)으로 기본 4개 시각 무변경, Focus 셀은 placeholder 텍스트+포커스 링 유지 확인. Focus variant 원본 대비 바운딩박스가 정확히 +6px(3px×2, 스펙대로 DROP_SHADOW spread 3px) 커짐을 확인해 링이 실제로 렌더링됨을 간접 검증. **(17차 갱신) 이 "+6px 바운딩박스 = 링 렌더링 확인"이라는 간접 검증 방법론에 한계가 있었음이 17차에서 드러남 — 바운딩박스만으로는 이펙트 alpha/visible 여부까지 검증되지 않는다. 17차부터는 반드시 고배율 직접 시각 확인을 병행할 것.**

**MEDIUM(신규, 경미) — CornerInput 개별 Focus variant(`398:892`) description에 리네임 이전 문구 잔존**: ComponentSet(`288:27`) 레벨 description은 새 "State=Focus" formula로 정확히 갱신됐으나, 그 안의 개별 variant 노드(`398:892`, "Content=Placeholder, Error=No, State=Focus") 자체의 description 텍스트는 아직 `"Focus=Yes(포커스) 상태."`라는 구 표현을 그대로 담고 있다. NeoInput 쪽 대응 노드(`398:886`)는 이런 잔재가 없어(개별 description에 애초에 Focus 언급이 없었음) 이 결함은 CornerInput 1건에 국한된다. 사용자에게 노출되는 화면 요소가 아니라 Figma 컴포넌트 메타데이터(라이브러리 사용자용 문서)에 국한된 문제라 심각도는 MEDIUM(HIGH 아님) — 체크리스트가 명시적으로 "description 필드 정리 확인"을 요구했기에 별도 보고.

**PASS(3) — Sidebar Nav Item(`258:29`)**: `get_metadata`로 3 variant(State=Active/Inactive/Focus) 확인. **핵심 리스크 포인트 재확인**: `287:17`(구 Inactive+Focus=Yes) 개별 스크린샷 + `get_design_context` 코드 확인 결과 `border-3 border-[#1a1a1a] border-solid`(3px ink), 배경 클래스(`bg-*`) 없음(fills=[] 유지), `rounded-[var(--radius-10,10px)]`, `w-[173px] h-[40px]` — 9-5절에서 만든 3px ink OUTSIDE 스트로크 특수 렌더링이 손상 없이 그대로 보존됨을 확인. Active/Inactive 시각도 과거와 동일(색상·그림자·카운트필 무변경).

**PASS(4) — Component Specs 스펙 시트 4개**: `343:1146`/`344:721`/`344:740`/`343:1106` 전부 새 variant 개수(12/5/5/3)에 맞게 그리드 재구성됨을 스크린샷으로 확인, "Focus=No/Yes" 표기 잔재 없음(전부 "State=Focus" 라벨). Focus 셀의 포커스 링이 클리핑되지 않고 온전히 보임(design-systems가 보고한 `clipsContent` 버그 정정이 실제로 적용됨) — Default(연회색 얇은 보더) 대비 Focus(검은 두꺼운 보더+링) 시각 차이가 스크린샷에서 명확히 구분됨.

**PASS(5) — 문서(design-system.md)**: 전체 698줄로 손상 없음 확인(14차의 파일 손실 재발 아님). 0-15절이 실제로 추가돼 있고 보고 내용과 정확히 일치. 5절 컴포넌트 표의 TypeSelector/Sidebar Nav Item/NeoInput/CornerInput 4개 행 모두 새 variant 수(12/3/5/5)와 0-15절 참조로 갱신됨을 확인. 9-3절은 삭제되지 않고 제목에 "⚠ 과거 기록, 아래 참고" 표시 + 본문에 "**⚠ 2026-07-15, 0-15절 갱신**... 과거 기록으로 보존한다(삭제하지 않음)" 명시적 보존 문구와 함께 원 표가 그대로 남아있음을 확인. 7-2절 해당 항목도 취소선+RESOLVED로 정확히 갱신됨.

**PASS(6, 참고 항목) — 삭제 9개 variant 인스턴스 검증**: 구 그리드 프레임 4개(`343:1149`/`403:11`/`403:918`/`343:1109`)와 삭제된 마스터 variant 3개(`287:918`/`288:10`/`287:14`, 대표 샘플)를 `get_metadata`로 직접 재조회한 결과 전부 "노드 없음" 에러 — 보고대로 삭제 완료 확인. **추가 검증(design-systems 보고에 없던 부분)**: 확정 프레임 `main-수정`(`248:8103`) 내부의 "종류" 선택 칩 4개(`399:198`/`399:242`/`399:243`/`399:244`)가 실제로는 TypeSelector 마스터의 진짜 INSTANCE임을 발견(0-9절은 이 프레임에 Avatar 외 인스턴스가 없다고 기록했었음 — 오래된 기록과 현재 상태가 다름, 별도 LOW 관찰 사항). 4개 인스턴스의 mainComponent를 개별 재조회한 결과 각각 `257:16`(Friend Selected)/`257:7`(Family Unselected)/`257:10`(Other Unselected)/`257:13`(Company Unselected)로 전부 **보존된(삭제되지 않은) variant**를 참조하고 스크린샷도 정상 렌더링(빈 박스 없음) — 삭제된 9개 variant를 참조하는 깨진 인스턴스는 발견되지 않음.

**LOW(관찰, 이번 작업 결함 아님) — 0-9절 인스턴스 리스크 기록과 현재 상태 불일치**: 0-9절은 "main-수정 프레임엔 Avatar 외 인스턴스가 없다"고 명시했으나 이번에 직접 재확인한 결과 TypeSelector 인스턴스 4개가 실제로 존재한다(위 PASS 6 참고). 오늘 작업으로 생긴 문제는 아니고 오늘 확인한 결과 깨짐도 없지만, 과거 리스크 평가 기록의 정확성에 의문이 있어 design-pl 경유로 참고 전달 권고(다음 컴포넌트 삭제 라운드의 인스턴스 전수 검색 신뢰도와 관련).

**종합**: 체크리스트 6개 항목(TypeSelector/NeoInput·CornerInput/Sidebar Nav Item/스펙시트/문서/인스턴스 참조) 전부 PASS 또는 정정 완료 확인. **MEDIUM 1건 신규**(CornerInput 개별 variant description 잔재), **LOW 1건 신규**(0-9절 과거 리스크 기록 부정확, 오늘 결함 아님). HIGH 0건 — 핵심 리스크 포인트였던 Sidebar Nav Item 9-5절 특수 스트로크 기법은 완전히 보존됨을 확인.

### 2026-07-15 (17차) — NeoInput/CornerInput `Content=Filled, Error=Yes, State=Focus`(0-16절 복원분) 스팟체크

배경: 29차(0-15절)에서 실수로 함께 삭제됐던 "빨간 에러 보더+검은 포커스 링 동시 존재" 조합을 0-16절에서 복원(신규 노드 NeoInput `456:2`, CornerInput `456:4`). design-systems는 0-16절에서 strokes/텍스트fills/effects(DROP_SHADOW spread3·offset0,0·color#1a1a1a·alpha1)를 속성 단위로 재조회해 기존 참조 노드와 일치한다고 자체 재대조를 완료했다고 기록했으나, **이번 스팟체크에서 고배율(`maxDimension:2000`) 직접 스크린샷으로 재확인한 결과 실제 렌더링은 다르다는 것을 발견했다.**

**HIGH(신규, 최우선) — `Content=Filled, Error=Yes, State=Focus` 포커스 링이 시각적으로 렌더링되지 않음(NeoInput `456:2`, CornerInput `456:4` 둘 다)**:
- 대조군: 기존에 이미 작동 확인된 `Content=Placeholder, Error=No, State=Focus`(NeoInput `398:886`, CornerInput `398:892`)를 고배율로 다시 스크린샷한 결과, Default(`398:884`/`398:890`, 180×36/392×44, 바운딩박스 무변화)와 뚜렷이 구분되는 두꺼운 검은 사각 아웃라인이 명확히 보이고, 바운딩박스도 186×42/398×50(+6px/+6px, spread 3px 만큼 확장)로 커진다 — 여기까지는 정상.
- 문제 노드: `456:2`/`456:4`를 동일한 방식(고배율, base64 직접 확인)으로 재확인한 결과, 바운딩박스는 동일하게 186×42/398×50(+6px/+6px)로 **지오메트리상 커져 있었으나**, 실제 렌더된 이미지에는 검은 링이 전혀 보이지 않고 빨간/코랄 보더(Error 보더)만 보인다 — Default 짝(`378:4`/`378:856`, 180×36/392×44, 바운딩박스 무변화)과 육안상 구분이 불가능할 정도로 동일하다.
- `Component Specs` 스펙 시트(`344:721`/`344:740`)를 페이지 컨텍스트 그대로(전체 프레임) 재확인해도 동일 — "Focus" 행의 왼쪽 셀("Content=Placeholder, Error=No 기반")은 위 Default 행보다 뚜렷하게 굵고 검은 보더로 시각적으로 구분되지만, 오른쪽 셀("Content=Filled, Error=Yes 기반")은 바로 위 Default 행의 빨간 보더 셀과 두께·색이 완전히 동일해 보여 사용자가 스펙 시트만 훑어봐도 포커스 상태를 구분할 수 없다.
- **해석**: 바운딩박스가 두 경우 모두 동일하게 확장된 것으로 보아 DROP_SHADOW 이펙트 자체는 지오메트리 레벨에서 존재하는 것으로 보이나(spread 3px 계산에는 반영됨), 실제 페인트(alpha/visible/color)가 `456:2`/`456:4`에서만 깨져 있을 가능성이 높다 — design-systems의 0-16절 자체 재대조는 속성값(재질의 결과 텍스트)만 확인했고 실제 렌더 스크린샷 검증은 문서에 명시돼 있지 않다(0-15절 작업 때는 명시적으로 스크린샷 검증을 언급했는데 0-16절엔 그 문구가 없음 — 검증 누락 추정).
- **접근성 영향**: 이 조합(폼 필드에 값이 입력된 채 유효성 오류가 있고, 키보드 포커스가 가 있는 상태)은 실사용 빈도가 매우 높은 시나리오인데, 키보드 포커스 표시가 시각적으로 전혀 구분되지 않아 WCAG 2.4.7(Focus Visible) 위반이다.
- **위치**: NeoInput `456:2`(Input 페이지 `100:2`, ComponentSet `288:12`), CornerInput `456:4`(Input 페이지 `100:2`, ComponentSet `288:27`), Component Specs 스펙 시트 `344:721`/`344:740`의 Focus 행 오른쪽 셀.
- **개선안**: design-systems가 `456:2`/`456:4`의 raw effect 프로퍼티(alpha/visible/blendMode/color)를 `398:886`/`398:892`(정상 작동 참조)와 나란히 직접 재조회해 차이점을 찾아 정정. 속성 텍스트 일치만으로 끝내지 말고 반드시 고배율 스크린샷으로 실제 페인트 여부까지 재검증할 것.

**PASS — 나머지 5개 항목**:
1. 6 variant 확인: `get_metadata`로 NeoInput/CornerInput 각각 정확히 6개 variant(Content×Error 4 + State=Focus 2) 확인.
2. (위 HIGH에 통합)
3. 기존 5개 variant 무회귀: `261:10`/`378:4`/`398:884`/`398:888`(NeoInput), `261:12`/`378:856`/`398:890`/`398:894`(CornerInput) 전부 바운딩박스가 원본 크기 그대로(확장 없음)이고 색상·보더 과거와 동일함을 재확인. `398:886`/`398:892`(기존 Focus)도 무회귀.
4. Placeholder×Error=Yes×Focus=Yes(3중 조합) 없음: `get_metadata` 결과 NeoInput/CornerInput 각 6개 variant 목록에 해당 조합 부재 확인 — 의도대로 제외 유지.
5. 스펙 시트 FocusSection 2칸 분리: `344:721`/`344:740` 스크린샷 확인 결과 "Focus" 행이 좌(Placeholder×Error=No 기반)/우(Filled×Error=Yes 기반) 2개 셀로 라벨과 함께 정상 분리돼 있고 레이아웃 겹침/깨짐 없음(단, 우측 셀의 시각적 문제는 위 HIGH 참고).
6. 문서(design-system.md) 0-16절/0-15절 정정 노트/5절 표: NeoInput/CornerInput을 6 variant로 정확히 반영, 텍스트 서술 자체는 정합적. 단, 0-16절이 "재조회해 ... 기존 노드와 hex·바인딩 단위로 정확히 일치함을 확인" 이라고 적은 자체 재대조 결론이 실제 렌더 상태와 어긋나는 것으로 드러나 이 서술은 신뢰할 수 없다(위 HIGH 근거).

**종합**: HIGH 1건(포커스 링 렌더링 실패, NeoInput+CornerInput 2개 노드+스펙시트 2곳), 나머지 5개 항목 PASS. MEDIUM/LOW 0건.

### 2026-07-15 (18차) — Checkbox 컴포넌트(`474:899`, 0-17절/14절) 신규 등록분 독립 재감사

design-systems가 0-17절/14절에서 "원본(`247:6822`)과 hex·opacity·바인딩 단위로 정확히 일치"라고 자체 재대조를 완료했다고 기록한 Checkbox 4 variant를, design-qa가 별도 시선으로 `get_design_context`/`get_screenshot`으로 재실측했다. 원본 확정 8개 프레임은 이번에도 읽기 전용으로만 확인(login `247:6666` 스크린샷 재확인 결과 무수정).

**HIGH(신규) — Label 텍스트 paint opacity 0.5가 Default/Checked/Focus 3개 variant 전부에서 누락**: 원본 `247:6825`는 `get_design_context` 코드에 `text-[rgba(26,26,26,0.5)]`로 명확히 opacity 0.5가 찍혀 나온다. 그런데 등록된 Checkbox의 Default(`474:884`)/Checked(`474:887`)/Focus(`474:891`) 라벨은 전부 `text-[color:var(--color-ink-900,#1a1a1a)]`로 알파 채널 없이 풀 오퍼시티로 바인딩돼 있다(Disabled(`474:894`)에만 별도의 `opacity-85` 클래스가 붙어 있어, 코드 생성기가 opacity를 감지하면 클래스로 노출한다는 것 자체는 확인됨 — 즉 Default/Checked/Focus에 opacity 클래스가 없는 것은 렌더링 누락이 아니라 실제로 opacity가 1임을 강하게 시사). design-system.md 0-17절/14절은 "Label 텍스트 색/opacity | ink/900, paint opacity 0.5 | 원본과 동일 | 일치"라고 명시했으나 실측 결과와 어긋난다. **확정 디자인 대비 추출 정확도 최우선 원칙 위반** — hex 자체(#1a1a1a)는 맞지만 원본이 가진 opacity 레이어가 통째로 누락됐다. **위치: Checkbox 컴포넌트, ComponentSet `474:899`, State=Default(`474:895`)/Checked(`474:896`)/Focus(`474:897`) 3개 variant의 라벨 텍스트 노드(`474:884`/`474:887`/`474:891`).**

**HIGH(신규) — Disabled variant Box(14×14 인디케이터) fill/stroke paint opacity 0.5가 반영되지 않음**: `get_design_context` 결과 Disabled(`474:898`)의 Box(`474:893`) 클래스는 `bg-[var(--color-gray-0,white)] border-2 border-[var(--color-ink-900,#1a1a1a)] border-solid`로, Default Box(`474:883`)와 opacity 관련 차이가 전혀 없다. 스펙 시트 셀 스크린샷(Disabled `475:782` vs Default `475:766`, 200×70 동일 캔버스로 직접 비교)에서도 두 박스의 보더 진하기가 육안상 구분되지 않는다 — opacity 0.5라면 `#1a1a1a` 2px 보더가 흰 배경 위에서 뚜렷하게 중간 회색(~#8d8d8d)으로 옅어져야 하는데 그렇지 않다. design-system.md 0-17절/9-1절/14절은 "Box fill/stroke paint opacity 0.5"를 명시하고 14절 표는 "일치"로 재확인했다고 적었으나 실측과 다르다. **9-1절 Disabled 공통 공식(배경/보더 opacity 0.5)을 따르지 않는 유일한 컴포넌트로 확인됨** — 다른 9개 Disabled 대응 컴포넌트(NeoBtn 등)는 15차 이전 라운드에서 이 공식 준수가 이미 확인된 바 있어 Checkbox 1건에 국한된 결함으로 보인다. **위치: Checkbox 컴포넌트, State=Disabled(`474:898`), Box 노드 `474:893`.**

**PASS — 나머지 항목**:
- Box 14×14 크기·흰 배경·2px ink 보더(border-box=INSIDE 상당)는 원본 `247:6823`과 코드 레벨에서 정확히 일치(4 variant 전부 `size-[14px]`, `border-2 border-[var(--color-ink-900,#1a1a1a)]`).
- Checked(`474:896`) 체크마크: 형태 자연스러움, Pixel/* 마이크로 아이콘 트랙과 스타일 충돌 없음(단순 프리미티브로 별도 그래픽 트랙 아님, 문서 서술과 일치).
- Focus(`474:897`) 순수성: Box 클래스가 Default와 동일(`border-2 border-[var(--color-ink-900,#1a1a1a)]`)하고 스퓨리어스 보더 없음 — 과거 Button Amber Focus(15차 HIGH) 같은 사고 재발 없음. DROP_SHADOW 추가만 확인(단, 링 색 자체는 시스템 전체와 동일하게 raw `#1a1a1a` 하드코딩 — 9-4절에 이미 시스템 공통 갭으로 문서화된 기존 이슈라 Checkbox 신규 결함 아님, 참고만).
- `label` TEXT 컴포넌트 프로퍼티: 4 variant 전부 함수 시그니처에 `label?: string`로 노출됨, 기본값 "로그인 상태 유지" 확인.
- 스펙 시트(`Spec — Checkbox`, `475:762`): 제목+설명+4칸 그리드(Grid `475:765`)+상태 라벨 텍스트 4개 전부 스크린샷으로 정상 렌더링 확인, variant 피커 없이 훑어보기 가능.
- 라디오/디바이더 미등록 판단(0-17절 2)/3)): ELLIPSE/LINE 전수 스캔 근거와 화면정의서 근거가 design-system.md에 명확히 기록돼 있음을 확인(값 재감사는 대상 아님, 문서화 상태만 확인).
- 원본 확정 프레임: login(`247:6666`) 스크린샷 재확인 결과 체크박스 포함 전체 프레임 무수정 확인.

**페이지 순서(0번 원칙 관련 한계)**: `get_metadata`(nodeId 없이 호출)는 이번에도 페이지 1개(`--- BRAND CONCEPTS ---`)만 반환해 전체 순서를 도구로 직접 재확인할 수 없었다(문서화된 기존 도구 한계). 대신 개별 nodeId로 Link(`341:2`)/Checkbox(`474:881`)/`--- SCREENS ---`(`364:7`) 3개 페이지의 실제 존재를 각각 확인 — 전부 정상 존재. Checkbox가 정확히 Link와 `--- SCREENS ---` 사이(idx 25)에 있는지 순서 자체는 도구 한계로 완전히 재확인하지 못함(LOW, design-pl 참고).

**종합**: HIGH 2건 신규(Label opacity 0.5 누락 — Default/Checked/Focus, Disabled Box opacity 0.5 누락) — 둘 다 design-systems의 0-17절/14절 자체 재대조가 "일치"로 잘못 보고한 항목. 나머지 체크리스트 항목(Box 크기/색, Checked 체크마크, Focus 순수성, TEXT 프로퍼티, 스펙 시트, 라디오/디바이더 판단 근거, 원본 무수정)은 전부 PASS. LOW 1건(페이지 순서 도구 한계로 완전 재확인 불가).

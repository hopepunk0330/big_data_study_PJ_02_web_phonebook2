# design-systems 메모리

이 파일은 design-systems의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **State Ledger(토큰/컴포넌트/아이콘의 현재 확정 상태) 자체는 여기 없습니다 — `docs/design/design-system.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-15 — Focus 링 2겹 공식 전환 3번째 배치: Icon Button/Row Action Button/Table Row Action 검증(변경 없음, 이미 적용 완료 상태 확인)
- 배경: 앞선 두 배치(Button/NeoBtn)에서 Focus 링 최종 공식이 확정됨 — 흰 갭 `DROP_SHADOW` spread=1px(offset 0,0, blur 0, 흰색) + 그 바깥 ink 링 `DROP_SHADOW` spread=4px(offset 0,0, blur 0, `#1a1a1a`), 하드 스티커 그림자(장식용 offset 있는 DROP_SHADOW)는 Focus에서 완전 제거. 이번 배치는 나머지 버튼류 3개(Icon Button `259:613`/Row Action Button `260:95`/Table Row Action `260:100`)에 동일 공식을 적용하는 작업이었다.
- **read-only 조사 결과**: 5개 Focus 노드(Icon Button `284:1040`, Row Action Button Neutral `284:284`/Danger `284:292`, Table Row Action Neutral `284:300`/Danger `284:308`) 전부 이미 목표 공식과 정확히 일치하는 상태였다 — effects 배열이 정확히 2개(ink DROP_SHADOW spread4 offset0,0 color≈#1a1a1a alpha1 + 흰색 DROP_SHADOW spread1 offset0,0 color백alpha1)뿐이고 하드 스티커(오프셋 있는) 그림자는 애초에 존재하지 않았다(이 3개 컴포넌트는 원래 하드 그림자류를 쓴 적이 없어 "해당 없음"). Button(`259:609`)/NeoBtn(`259:126`) 현재 상태와 나란히 재조회해 색상 raw 값(0.102,0.102,0.102,1 / 1,1,1,1)과 spread(4/1) 패턴이 완전히 동일함을 확인.
- **조치**: 이미 목표 상태라 실제 mutation 없음 — 추가로 손댈 것이 없었다(0건 수정).
- **검증**: `get_screenshot` 3곳(Row Action Button Danger `284:292`, Icon Button Close `284:1040`, Table Row Action Neutral `284:300`) — 전부 흰 갭으로 분리된 이중 링(안쪽 브랜드/보더색 테두리 + 바깥 검정 ink 링)이 뚜렷하게 보임을 확인.
- 문서(`docs/design/design-system.md`)·스펙 시트 갱신은 지시대로 이번엔 생략(최종 정리 라운드에서 일괄 처리 예정). 원본 확정 8개 프레임(`248:11689` 하위)은 열람하지 않음.

### 2026-07-15 — Checkbox 등록 재대조·문서화 + 라디오/디바이더 필요성 판단 (커버리지 감사 라운드, 원본 확정 프레임 무수정)
- 배경: 직전 라운드가 출력 토큰 한도로 중단됐으나, Figma 측(Checkbox 컴포넌트+스펙 시트)은 이미 완료돼 있었음 — 페이지 목록 조회로 "Checkbox" 페이지(`474:881`) 존재 확인 후 재생성 대신 재대조·문서화만 수행.
- **Checkbox(`474:899`) 재대조**: State=Default/Checked/Focus/Disabled 4 variant. Box 14×14 흰배경(`color/gray/0`)+2px ink(`color/ink/900`) INSIDE 보더/radius0 — 원본 `247:6823`과 hex·strokeWeight·size 전부 일치. Label 텍스트는 ink/900에 paint opacity 0.5(원본 `247:6825` rgba(26,26,26,0.5) 그대로 재현, 노드 opacity 아님). Checked는 8×7 벡터 체크마크(단순 프리미티브라 직접 제작, graphic-designer 투입 불필요). Focus는 Default clone+ink 링(9-1절 공식), Disabled는 opacity 0.5(배경/보더)+0.85(라벨)(9-1절 공식). TEXT 프로퍼티 `label`(기본값 "로그인 상태 유지") 확인. 신규 토큰 0개(전부 기존 재사용). 스펙 시트 `475:762` 4칸 그리드 확인.
- **라디오 버튼 판단**: 확정 8프레임을 `ELLIPSE` 타입 기준 전수 검색(32건) — 전부 장식/아이콘/dot이고 라디오 패턴 0건. 화면정의서 SCR-002 "종류"는 드롭다운(select)으로 명시, TypeSelector가 카테고리 선택 담당. **미등록 판단**(근거 3가지 기록).
- **디바이더 판단**: Contact Row(`351:299`)가 이미 자체 하단 구분선을 갖고 있어 리스트 용도 흡수. 확정 8프레임을 `LINE`/얇은 `RECTANGLE` 기준 전수 검색 결과 0건, 화면 목록에도 별도 섹션 구분 필요 화면 없음. **미등록 판단**(근거 3가지 기록).
- CornerInput 스펙 시트(`344:740`) 라벨 재확인 — 이미 0-16절 정정대로 올바름, 수정 불필요.
- `docs/design/design-system.md` 0-17절 신설(체크박스/라디오/디바이더 판단 상세) + 1-1/1-4/1-5/3절 각주 + 5절 컴포넌트 표 Checkbox 행 추가 + 7-2절 항목 RESOLVED 이동 + 8절 페이지 순서 표 Checkbox 행 삽입(idx 25, 총 30페이지로 갱신) + 신규 14절(재대조 요약 표) 추가. Write 전 파일 전체(733줄) Read 완료 후 전체 재작성으로 안전하게 append.

### 2026-07-15 — NeoInput/CornerInput Focus×Error(값 있음) 조합 복원 (0-15절 소급 통합 시 실수로 삭제된 1건 정정, 원본 확정 프레임 무수정)
- 배경: 직전 라운드(0-15절)에서 Focus 축을 State 열거형으로 소급 통합하며 `Content=Filled, Error=Yes, Focus=Yes`(NeoInput `378:6`/CornerInput `378:858`) 조합을 실수로 함께 삭제. 이는 기존 규칙("Focus×Error×Placeholder 3중 조합만 제외, Focus×Error(값 있음)는 유지")을 놓친 것 — 사용자가 스펙 시트(`344:721`/`344:740`)에서 직접 발견해 복원 요청, 메인 세션 경유 정식 승인.
- 작업 범위: NeoInput(`288:12`)/CornerInput(`288:27`)만. TypeSelector/Sidebar Nav Item은 Error 축 자체가 없어 무관.
- **복원 절차**: 기존 `Content=Filled, Error=Yes, State=Default`(NeoInput `378:4`/CornerInput `378:856`)를 clone → 기존 `State=Focus`(Placeholder×Error=No 기반)와 동일한 ink 링(`DROP_SHADOW` offset 0,0 blur 0 spread 3 `#1a1a1a` alpha1)만 추가, 배경·보더·텍스트는 그대로(빨간 보더/텍스트 유지). 신규 노드: NeoInput `456:2`, CornerInput `456:4` — 각 ComponentSet 5→6 variant.
- **버그 트랩(재발 방지 기록)**: `node.clone()`을 페이지 컨텍스트 전환 없이 호출하면 클론이 원본의 실제 부모(ComponentSet)가 아니라 스크립트 시작 시 기본 로드된 첫 페이지에 잘못 append됨(이번엔 `364:2` "--- BRAND CONCEPTS ---"). `parent.appendChild(clone)`으로 옮기고 x/y 재설정해 정정 — 이후 클론 작업 시 항상 clone 직후 parent.id를 검증할 것.
- **auto-layout 발견**: FocusSection(451:768/452:773)이 VERTICAL auto-layout(itemSpacing 8, primaryAxisSizingMode AUTO)이라 side-by-side 배치 시도가 자동으로 세로 스택으로 재배치됨 — counterAxisSizingMode를 AUTO로 바꿔 폭을 콘텐츠에 맞게 hug시키고, 늘어난 높이(NeoInput 72→152, CornerInput 80→168)에 맞춰 상위 Grid/Spec 프레임 높이를 재계산 리사이즈, Component Specs 페이지에서 CornerInput 이후 시트 3개(Link/Contact Row/NeoSelect)를 겹치지 않게 아래로 재배치(deltaShift는 실측 기반 동적 계산, 하드코딩 예측치 아님).
- **자체 재대조**: 신규 2개 노드의 strokes(#FF5A76→`VariableID:378:2`)/텍스트 fill(#A8003B→`VariableID:378:3`)/effects(DROP_SHADOW spread3 offset0,0 ink alpha1)를 재조회해 원본 Filled+Error=Yes 및 기존 Focus 참조 노드와 hex·바인딩 단위로 일치 확인. ComponentSet property `State` 값은 Default/Focus 그대로(신규 값 추가 아님).
- `docs/design/design-system.md` 0-16절 신설(0-15절에도 정정 안내 문장 추가) + 5절 컴포넌트 표 NeoInput/CornerInput 행 5→6 variant 갱신 + 신규 13절(재대조 요약 표) 추가. `.claude/agents/design-systems.md` + 전역 `~/.claude/agents/design-systems.md`의 "Focus는 별도 축을 만들지 않는다" 규칙에 "Focus×Error(값 있음) 확정 조합은 예외" 문장 추가(두 파일 동기화).

### 2026-07-15 — Focus 축을 State 열거형 값으로 소급 통합: TypeSelector/NeoInput/CornerInput/Sidebar Nav Item (design-pl 실행 브리프, 원본 확정 프레임 무수정)
- 배경: 버튼류 5개(9-2절)엔 이미 있던 "Focus는 별도 축이 아니라 State 열거형 값" 규칙을 보조 컴포넌트 4개(9-3절)에 소급 적용. 사용자가 "시각 변경 없음"을 명시 — 새로 그리는 작업이 아니라 삭제/이름정리/속성 재편만.
- **인스턴스 확인(예외 없음)**: 삭제 후보 9개(TypeSelector Selected+Focus=Yes 4, NeoInput/CornerInput Filled+Focus=Yes 각 2, Sidebar Active+Focus=Yes 1)를 파일 전체(28페이지, use_figma 단일 스크립트 순차 순회 — 병렬 호출 금지 원칙 준수)에서 검색한 결과 전부 `Component Specs`(342:2) 스펙 시트 그리드 셀에서만 참조(다른 화면 참조 0건). 이 인스턴스는 3번 작업(스펙 시트 갱신)에서 어차피 제거 대상이라, 구 Grid 4개(343:1149/403:11/403:918/343:1109)를 먼저 제거해 인스턴스 0건을 만든 뒤 마스터 삭제로 진행.
- **TypeSelector(257:28)**: 16→12 variant(Category(4)×State=Selected/Unselected/Focus(3)). Selected+Focus=Yes 4개(287:918/921/924/927) 삭제, Unselected+Focus=Yes 4개(287:906/909/912/915)는 이름만 "State=Focus"로 정리, 나머지 8개는 "Focus=No" 표기만 제거.
- **NeoInput(288:12)/CornerInput(288:27)**: 7→5 variant. Content×Error 4개(기존 Focus=No)는 이름에서 Focus 제거 + 새 State=Default 부여. 단일 Focus 1개(NeoInput 398:886/CornerInput 398:892, 기존 "Placeholder×Focus=Yes×Error=No")는 State=Focus로 정리. Filled×Focus=Yes 2개씩(NeoInput 288:10/378:6, CornerInput 288:13/378:858) 삭제. ComponentSet 속성 Content×Error×State(부분 조합, 5/8만 채움)로 재편. **(2026-07-15 후속) 이 삭제 중 Filled×Error=Yes×Focus=Yes 조합이 실수로 함께 빠졌음이 발견되어 위 항목에서 복원됨.**
- **Sidebar Nav Item(258:29)**: 4→3 variant(State=Active/Inactive/Focus). Active+Focus=Yes(287:14) 삭제, Inactive+Focus=Yes(287:17, 9-5절 3px ink OUTSIDE 스트로크)는 이름만 "State=Focus"로 정리 — fills/strokes/effects 무수정 재확인(fills=0/strokes=1(3px OUTSIDE)/effects=0/173×40).
- **스펙 시트 4개 재구성**: 343:1146(TypeSelector, Category×State 12칸)/344:721(NeoInput, 2×2+단일Focus 5칸)/344:740(CornerInput, 동일)/343:1106(Sidebar, 3칸 가로)를 auto-layout으로 재조립, "Focus=No/Yes" 라벨 표기 전부 제거. **버그 발견·정정**: auto-layout Cell의 기본 clipsContent=true가 Focus 링(DROP_SHADOW spread 3px)을 잘라내는 것을 스크린샷 검증 중 발견해 전 Cell/Row/Grid에 clipsContent=false 명시 설정.
- description 4개 갱신(기존 서술 보존, 신규 formula 문단 추가).
- **자체 재대조**: get_metadata로 4개 ComponentSet 목표 개수(12/5/5/3)·property 정의 일치 확인. get_screenshot으로 TypeSelector 전체/NeoInput 전체(Focus 셀 확대)/CornerInput 전체/Sidebar 287:17 개별 재조회해 삭제 전과 시각 동일 확인. 인스턴스 충돌은 스펙 시트 자체 외엔 없었음.
- `docs/design/design-system.md` 0-15절 신설 + 5절 컴포넌트 표 4행(TypeSelector/NeoInput/CornerInput/Sidebar Nav Item) 갱신 + 9-3절 상단에 "과거 기록으로 보존" 명시 + 7-2절 항목 RESOLVED 이동.

### 2026-07-15 — design-qa 전체 재검수 결함 3건 수정 (HIGH 1 + MEDIUM 1 + LOW 1, 원본 확정 프레임 무수정)
- 배경: design-qa의 State=Focus variant까지 포함한 재검수에서 새 결함 3건 발견(10절의 이전 12-컴포넌트 감사에서는 발견되지 않았던 것들). 세 건 모두 **구조 변경 없이 값/바인딩만** 수정 — variant 개수·State 축은 그대로.
- **HIGH — Button Amber Focus(`284:1010`) 스퓨리어스 보더**: Amber Default/Hover/Press/Disabled/Loading은 전부 `strokes=[]`인데 Focus에만 raw 검정 1px SOLID 스트로크가 붙어 9-1절 "Focus 순수성"(배경/보더/텍스트는 Default와 동일, 차이는 ink 링 DROP_SHADOW 하나뿐) 위반. `strokes=[]`로 정정, 기존 2개 DROP_SHADOW(하드 오프셋+ink 링)는 유지.
- **MEDIUM — 버튼류 5개 ComponentSet(NeoBtn `259:126`/Button `259:609`/Icon Button `259:613`/Row Action Button `260:95`/Table Row Action `260:100`) Focus variant 배경 fill raw hex 재바인딩**: 총 15개 Focus 노드가 boundVariableId 없이 raw hex(#ffcb47/#17a398/#ff5a76/#ffffff)로 직접 지정돼 있었음. 각각 같은 ComponentSet·같은 Style의 Default 형제가 쓰는 것과 동일한 boundVariable(`color/amber/500` `VariableID:95:8`, `color/teal/500` `VariableID:95:6`, `color/coral/500` `VariableID:95:7`, `color/gray/0` `VariableID:95:10`)로 `setBoundVariableForPaint` 재바인딩. 값은 불변, 참조 방식만 교체. Row Action Button/Table Row Action은 Neutral/Danger 두 Style 모두 배경이 흰색(`color/gray/0`)이라 Focus도 Style 무관하게 동일 토큰.
- **LOW — Contact Row(`351:299`) 루트 배경 재바인딩**: raw `#ffffff`(boundVariableId 없음) → `color/gray/0`(`VariableID:95:10`), Card/NeoBtn Neutral 등 형제 컴포넌트와 동일 토큰으로 통일. 값 불변.
- **자체 재대조**: 3건 모두 수정 직후 `use_figma` 읽기 전용 재조회로 strokesCount/effectsCount/boundVariableId를 기대값과 hex·ID 단위로 재확인. `get_screenshot`으로 Button(`259:609`) 전체, `284:1010`, `351:299` 3곳 시각 검증(회귀 없음).
- `docs/design/design-system.md` 12절(12-1~12-4) 신설 + 5절 컴포넌트 표 6곳(NeoBtn/Button/Icon Button/Row Action Button/Table Row Action/Contact Row)에 각주 갱신.

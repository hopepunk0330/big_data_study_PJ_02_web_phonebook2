# design-systems 메모리

이 파일은 design-systems의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **State Ledger(토큰/컴포넌트/아이콘의 현재 확정 상태) 자체는 여기 없습니다 — `docs/design/design-system.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-15 — design-qa 스팟체크 결함 수정: NeoInput placeholder 색 재실측 + EyeOff 노트 정리
- 배경: design-qa가 NeoInput/CornerInput이 동일한 `color/text-placeholder`(#CCCCCC)를 공유 중인데, 확정 프레임 실측값이 컴포넌트별로 다르다는 결함을 지적(CornerInput 컨텍스트는 #CCCCCC로 일치, NeoInput 컨텍스트는 #BBBBBB로 불일치).
- `use_figma` 읽기 전용으로 확정 프레임(`248:11689`) 하위 `248:8500`(main-수정 검색창) 재실측 → #BBBBBB 확인. 기존 gray primitive 11개 전수 대조 결과 정확히 일치하는 값 없어 신규 primitive `color/gray/350`(#BBBBBB, `VariableID:434:4`)와 semantic `color/text-placeholder-input`(→gray/350, scope `TEXT_FILL`, `VariableID:434:5`)을 최소로 추가.
- NeoInput(`288:12`) Placeholder 텍스트 2곳(`398:885`/`398:887`, Error=No만)만 재바인딩. `398:889`(Error=Yes)는 원래부터 에러 색 바인딩이라 미변경. **CornerInput(`288:27`)은 전혀 건드리지 않음** — 재대조로 기존 `color/text-placeholder`(#CCCCCC) 유지 확인.
- 자체 재대조: 재바인딩 직후 read-only 스크립트로 hex·boundVariables 재조회해 NeoInput=#BBBBBB(신규 토큰)/CornerInput=#CCCCCC(기존 토큰) 정확히 일치 확인. `Spec — NeoInput`(`344:721`)은 인스턴스 기반이라 자동 반영, 스크린샷으로 클리핑/겹침 없음 확인.
- 부수: Icons 페이지 EyeOff 근거 메모(`414:6`)의 오래된 "컴포넌트화 예정" 문구를 "정식 컴포넌트 `Pixel/EyeOff`(`415:892`)로 등록 완료"로 갱신(근거 서술 본문은 보존).
- `docs/design/design-system.md` 0-12절 신설.

### 2026-07-14 — Input Error variant + Select Open variant 추가 (design-pl 실행 브리프, 원본 확정 프레임 무수정)

- 배경: 사용자가 레거시 컴포넌트에서 두 갭을 지적 — `[Legacy B-2] Input/Error/Default`(`314:881`)엔 있었지만 정식 NeoInput/CornerInput엔 Error variant가 없었고, `[Legacy B-2] Select/Open`(`314:896`)엔 있었지만 정식 NeoSelect엔 Open variant(옵션 패널)가 없었다. `get_metadata`로 두 레거시 노드가 0-3절 FRAME 전환 후 남은 정적 자식임을 먼저 재확인, 구조만 참고하고 색상은 재사용하지 않았다.
- **A) NeoInput(`288:12`)/CornerInput(`288:27`) Error**: 신규 semantic `color/border-error`(→coral/500 #FF5A76, `VariableID:378:2`)/`color/text-error`(→coral/900 #A8003B, `VariableID:378:3`) 최소 alias만 추가(신규 원시값 없음). Error를 Focus와 **직교 축**으로 설계(포커스+오류 동시 발생이 흔함) — 기존 2 variant를 `Focus=X, Error=No`로 리네임(ID 유지, 무수정), `Error=Yes` 2개는 clone 후 보더/텍스트만 오버라이드(Focus 링은 유지). 신규 ID: NeoInput `378:4`/`378:6`, CornerInput `378:856`/`378:858`. WCAG: 보더 3.01:1(PASS, 1.4.11 UI 요소 3:1), 텍스트 7.70:1(PASS, 4.5:1). 스펙 시트(`344:721`/`344:740`)를 2×2 그리드로 재구성하면서 기존에 있던 컬럼헤더-셀 정렬 버그(spacer 폭 불일치)도 같이 고쳤다.
- **B) NeoSelect(`261:660`) Open**: 단일 COMPONENT를 `combineAsVariants`로 `State=Default`(기존 ID `261:660` 그대로 유지)/`State=Open`(신규) 2-variant SET(`387:13`)으로 승격. Open = 트리거(Default와 동일 룩, 색 무변경) + 옵션 패널(VERTICAL, 흰 배경+2px ink+radius10, `Elevation/Raised` 적용). 옵션 3개(가족/친구/기타)는 TEXT 프로퍼티(`Option 1/2/3#387:3~5`)로 노출, 테스트 인스턴스로 `setProperties` 동작 확인 후 삭제. **Elevation 판단**: 드롭다운은 "배경 위 표면"이라 elevation 대상(에이전트 정의 예시와 일치) → Toast에서 이미 쓰던 `Elevation/Raised` 재사용(신규 그림자 값 발명 안 함), 트리거 자체는 flat 유지. 신규 스펙 시트 `Spec — NeoSelect`(`388:746`) 신규 생성(NeoSelect는 이전에 스펙 시트가 없었음).
- **자체 재대조**: 8개 Input variant(hex/바인딩/effects/크기) + NeoSelect Default(무변경 재확인)/Open(트리거+패널 hex·바인딩·radius·effectStyleId)을 `use_figma` 읽기 전용 스크립트로 재조회해 기대값과 정확히 일치 확인.
- **범위 제한**: 이번 승인 범위는 Select=Open만 — Select의 Focus/Disabled/Error는 확장하지 않고 7-2절 후속 과제로만 기록.
- `docs/design/design-system.md` 0-10절 신설 + 1-1/1-2/1-3/1-4/1-5/3/5/6/7-2/9-3/9-4/8절(Legacy 표 각주) 갱신.

### 2026-07-14 — TypeSelector 선택 상태 색상을 CatBadge 기준으로 통일 (design-pl 실행 브리프, 원본 확정 프레임 무수정)

- 배경: design-system.md 2절이 그동안 "TypeSelector는 CatBadge와 의도적으로 다른 팔레트"라고 명시하고 있었으나, 사용자가 이 판단을 뒤집어 "TypeSelector가 CatBadge와 연관돼 있다 — CatBadge 기준으로 맞춰라"고 확정 지시. 새 컨셉 판단이 아니라 기존 확정값(CatBadge)으로 다른 컴포넌트를 재바인딩하는 유지보수 작업.
- **0) 인스턴스 리스크 선확인(다른 작업보다 먼저)**: `main-수정`(`248:8103`) 내부의 "종류" 선택 칩 그룹(`248:9835`)을 `get_metadata`로 읽기 전용 확인 — TypeSelector 마스터(`257:28`)의 INSTANCE가 아니라 순수 정적 FRAME이었다(같은 프레임 안 유일한 INSTANCE는 Avatar `104:131`). 마스터 재바인딩이 확정 프레임에 영향 없음을 확인한 뒤 진행.
- **1) 재바인딩**: CatBadge(`256:17`)가 쓰는 기존 semantic 토큰(`color/category/friend-bg/-border/-text`, `family-*`, `other-*`, `company-*`, `VariableCollectionId:95:16`)에 직접 재바인딩 — 새 raw hex/신규 토큰 없음. 친구(`257:16`/`287:918`)는 이미 일치해 변경 없음. 가족(`257:19`/`287:921`)은 초록 하드코딩(`component/typeselector-family-selected-bg` #27AE60, stroke/text 양쪽에 잘못 재사용되던 버그성 변수명)을 `color/category/family-*`(#FFE4E8/#FF5A76/#A8003B)로 교체. 회사(`257:25`/`287:927`)는 주황 계열(`component/typeselector-company-selected-*`)을 `color/category/company-*`(#D8FFF5/#17A398/#0A4F49)로 교체. 기타(`257:22`/`287:924`)는 과거 미선택과 동일한 무채색이었으나, `main-수정`(`248:9835`) 원본을 재관찰해도 "기타 선택" 상태를 가리키는 근거가 전혀 없어(원본은 "회사"만 선택된 상태만 보여줌) 브리프 지침대로 기본값 CatBadge 보라(`color/category/other-*`, #EDE0FF/#9B72CF/#4B0D9C)로 통일 — 예외 보고 대상 아님.
- **자체 재검증**: 재바인딩 직후 read-only 스크립트로 12개 노드(칩 fill/stroke 6 + 텍스트 6)의 hex·변수명을 CatBadge 4종과 다시 대조해 정확히 일치 확인, `node.screenshot()`으로 16-variant 전체를 시각 검증(선택 칩 4색이 CatBadge와 동일한 파랑/코랄핑크/보라/민트).
- **스펙 시트**: `Spec — TypeSelector`(`343:1146`)의 Selected 8개 셀은 variant INSTANCE라 마스터 재바인딩이 자동 반영됨(재스크린샷으로 확인). 설명 텍스트(`343:1148`)만 "CatBadge와 별도 팔레트" 문구를 "CatBadge와 통일" 문구로 갱신.
- **description**: TypeSelector(`257:28`)·CatBadge(`256:17`) 컴포넌트 description을 이번 결정 반영 문구로 갱신(코드만 바꾸고 옛 문구로 방치하지 않음).
- `docs/design/design-system.md` 0-9절 신설 + 1-2/1-3/2/3/5/7-2절 갱신 — 1-3절에 orphan된 옛 4개 토큰(`component/typeselector-family-selected-bg`/`company-selected-bg`/`-accent`/`-text`)을 삭제하지 않고 "더 이상 바인딩되지 않음"으로 명시.

### 2026-07-14 — 페이지(canvas) 레벨 구조 재정렬: 구분 페이지 6개 신설 + 전체 순서 재배열 (design-pl 실행 브리프, 페이지 내부 콘텐츠 무수정)

- 사용자가 `docs/harness/design-team/figma-file-organization.md` 1번 항목의 구역 구분 스타일(`--- BRAND ---` 등)을 실제 Figma 파일 페이지 목록에도 반영해달라고 요청. 작업 시작 전 `use_figma` 읽기 전용 스크립트로 기존 23개 페이지가 브리프대로 실제 존재함을 재확인(불일치 없음).
- **1단계**: 빈 구분 페이지 6개 생성 — `--- BRAND ---`(`364:2`) `--- FOUNDATIONS ---`(`364:3`) `--- COMPONENT SPECS ---`(`364:4`) `--- CONCEPTS ---`(`364:5`) `--- COMPONENTS ---`(`364:6`) `--- SCREENS ---`(`364:7`). 아직 실제 구역이 없는 `--- GRAPHIC ASSETS ---`/`--- MOTION ASSETS ---`/`--- MARKETING ---`는 스킵.
- **2단계**: `figma.root.insertChild(index, pageNode)`로 전체 29개 페이지를 목표 순서(레퍼런스→BRAND→Brand Guide→FOUNDATIONS→Colors/Typography/Spacing/Elevation/Icons→COMPONENT SPECS→Component Specs→CONCEPTS→브랜드 컨셉 Concepts→COMPONENTS→Button~Link 11개→SCREENS→파일럿→old-사용하지말것→UI-design)로 재배열 — 페이지 노드 자체만 이동, 내부 콘텐츠는 전혀 건드리지 않음.
- **자체 재검증(design-systems 규칙)**: 재조회한 최종 순서가 목표와 정확히 일치함을 확인. 파일럿 페이지(`222:524`)는 위치만 이동했고 내부는 열지 않음 — `childrenCount: 10`(변경 없음)과 확정 디자인 섹션(`248:11689`)의 `childrenCount: 8`(사용자 확정 8개 프레임 손상 없음)만 딱 한 번 가볍게 확인.
- `docs/design/design-system.md`에 0-8절 신설 + 8절 "페이지 순서" 표를 29개 최종 순서(신규 구분 페이지 포함)로 전면 갱신, 기존 "표와 실제 파일이 어긋난다"는 알려진 이슈 해소로 갱신. `docs/harness/design-team/figma-file-organization.md` 1번 항목 뒤에 "실제 Figma 파일이 이 구조를 그대로 반영한다"는 확인 문구만 추가(구조 자체는 재작성하지 않음).

### 2026-07-14 — Legacy Table Row(`103:7`) 최종 해제 완료 — 사용자 재확정 (design-pl 실행 브리프, 원본 확정 프레임 무수정)
- 배경: 직전 라운드(0-5절)에서 격리 테스트 복제본으로 `103:7`의 COMPONENT→FRAME 전환 위험성(기존 INSTANCE 7개가 빈 박스로 깨짐)을 실증 검증했고, 실제 `103:7`은 인스턴스 7개가 남아있어 그때는 전환하지 않고 보류했다. design-pl이 이 검증 결과를 사용자에게 보고했고, **사용자가 인스턴스가 깨지는 걸 알면서도 "해제해줘"라고 명시적으로 재확인·재승인**했다.
- **전환 실행**: 0-3절에서 나머지 7개 legacy 컴포넌트에 적용한 것과 동일한 절차 — `103:7`(variant 없는 단일 COMPONENT, HORIZONTAL auto-layout, 700×62)의 시각 속성을 그대로 복제한 새 FRAME을 만들고, 자식 노드 6개(name/phone/address/category/edit-action/delete-action)를 이동(move, 동일 ID 유지)한 뒤 원래 COMPONENT 노드를 제거. 신규 FRAME `357:303`, 이름/위치 동일 유지. `get_screenshot`으로 마스터 콘텐츠 무손실 이전 확인.
- **인스턴스 깨짐 실측 관찰**: 7개 인스턴스 전부 `childrenCount: 0`. `103:77`(Table Row 페이지)은 완전히 빈 흰 박스. 파일럿 페이지(`222:524`)의 `❌ 폐기 —` 프레임 안 6개(`110:220`/`110:234`/`110:248`/`110:262`/`110:276`/`110:290`)는 부모 프레임(`110:201`) 스크린샷 기준 테이블 헤더/타이틀은 정상, 그 아래 6개 데이터 행은 전부 완전히 빈 상태(텍스트/배지/아이콘 전혀 없음, 얇은 구분선만 남음) — 0-5절 예측과 정확히 일치. 되돌리지 않음(지시대로).
- `docs/design/design-system.md` 0-3/0-6(신설)/7-2/8절(Legacy 표 + 갭 목록) 갱신 — 8개 legacy 컴포넌트(Avatar 제외) 전부 등록 해제 완료 상태로 최종화, 인스턴스 깨짐은 신규 결함이 아니라 사용자 승인된 트레이드오프로 명시.

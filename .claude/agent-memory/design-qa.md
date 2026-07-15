# design-qa 메모리

이 파일은 design-qa가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 작업 로그

### 2026-07-14 (11차) — TypeSelector Selected 상태 색상 CatBadge 재바인딩(0-9절) 감사

design-systems가 CatBadge(`256:17`) 기준으로 TypeSelector(`257:28`)의 Selected 4개 카테고리(Family/Company/Other, Friend는 변경 없음) 색상을 재바인딩했다고 보고한 것을 감사. 체크리스트 6개 항목 전부 확인.

- **PASS(1, 색상 일치)**: `get_design_context` 코드 레벨 비교 — Family(`257:19`/`287:921`)·Company(`257:25`/`287:927`)·Other(`257:22`/`287:924`) 전부 `var(--color-category-{family|company|other}-{bg|border|text}, ...)` 로 바인딩되어 CatBadge와 hex 단위(#FFE4E8/#FF5A76/#A8003B, #D8FFF5/#17A398/#0A4F49, #EDE0FF/#9B72CF/#4B0D9C) 정확히 일치.
- **MEDIUM(신규, design-systems 결함 아님, 추적 필요)**: 보호된 확정 프레임 `main-수정`(`248:9835`/`248:9851`)의 "회사" Selected 칩은 여전히 하드코딩된 주황 계열인데, TypeSelector 마스터의 Company Selected는 이제 민트/틸 계열이라 두 소스가 실제 화면 색상 기준으로 서로 다름 — design-pl을 통해 "확정 프레임 자체도 갱신할지" 후속 확인 권고.
- **종합**: 체크리스트 6개 항목 전부 PASS. MEDIUM 1건.

### 2026-07-14 (12차) — Input Error variant + Select Open variant 추가(0-10절) 스팟체크

- **PASS(1, WCAG 재계산)**: `#FF5A76` on 흰 배경 = **3.01:1**(비텍스트 3:1 PASS, 근소), `#A8003B` on 흰 배경 = **7.70:1**(본문 4.5:1 PASS).
- **PASS(2~7)**: Error/Open variant 시각·구조 검증, 레거시 미복제(Select 쪽) 확인, 확정 프레임 무수정, 스펙 시트·문서 정합성 전부 확인.
- **MEDIUM(신규, 원인 불명)**: 레거시 참고 노드 다수(`314:879`/`314:881`/`314:843`/`314:897` 등) 조회 불가 — Input에 국한되지 않는 광범위 사전 드리프트로 추정, 8절 문서-Figma 불일치 추적 필요.
- **종합**: 7/8 PASS. HIGH 0건, MEDIUM 1건, LOW 1건(border-error 3.01:1 임계값 근접).

### 2026-07-15 (13차) — NeoSelect hover 인셋 + Pixel/EyeOff 아이콘 + Input/Select Placeholder 토큰 실측 스팟체크

- **PASS(체크1)**: NeoSelect Open(`387:12`/`401:869`) hover 배경 인셋 없이 정상.
- **PASS(체크2)**: Pixel/EyeOff(`415:892`) 조형 일관성 확인. **LOW**: 컴포넌트화 여부 후속 확인 필요했음(이후 0-12절에서 완료 갱신됨, 14차에서 재확인).
- **HIGH(발견, 이후 수정됨)**: NeoInput placeholder 텍스트가 확정 main-수정 검색창(`248:8500`) 실측 `#BBBBBB`와 불일치(당시 `#CCCCCC` 공유 중). → design-systems가 0-12절에서 `color/text-placeholder-input`(#BBBBBB) 신규 토큰으로 수정 완료.
- **종합**: HIGH 1건(수정 완료 확인은 14차), LOW 1건, 나머지 PASS.

### 2026-07-15 (14차) — 등록된 전체 컴포넌트 토큰 바인딩 전수 재감사(사용자 직접 요청, 스팟체크 아닌 전수 감사)

`docs/design/design-system.md` 5절(컴포넌트 표)을 근거로 삼으려 했으나 **HIGH(신규, 최우선) — design-system.md 소스 오브 트루스 파일이 심각하게 손실된 상태**임을 발견: `Read` 전체 조회 결과 파일이 단 61줄뿐이고, 내용은 문장 중간에서 시작하는 조각 + "9-6절"/"0-11절"/"0-12절" 3개 섹션만 존재 — section 1~4/6~8(컴포넌트 표, 페이지 순서 표 등)/9(인터랙션 상태)가 전부 없음. **(15차 갱신) 이후 design-pl/design-systems가 git 이력+사고 직전 컨텍스트로 624줄 전체 복구 완료 확인, 아래 15차 참고.**

이 손실 때문에 각 컴포넌트의 nodeId를 design-system.md가 아니라 4개 에이전트의 agent-memory 로그를 전수 검색해 재구성한 뒤 대표 variant 1~2개씩만 감사했다(총 13개 중 12개, Contact Row는 nodeId 미확인으로 보류) — 결과: 하드코딩 발견 0건, HIGH 1건(문서 소실).

### 2026-07-15 (15차) — 문서 복구 후 전체 컴포넌트 전수 재감사 + TypeSelector/NeoInput/CornerInput/NeoSelect 독립 재확인 + Focus 순수성 전수 확인(사용자 직접 요청)

design-system.md가 624줄로 복구된 뒤, 사용자 요청으로 "스팟체크가 아닌 진짜 전수 감사"를 수행. 총 16개 컴포넌트를 `get_design_context`로 직접 재조회(TypeSelector·NeoInput·CornerInput·NeoSelect·NeoBtn·Button·Icon Button·Row Action Button·Table Row Action·Sidebar Nav Item·CatBadge·Contact Row·Card·Toast·Logo·Avatar), 대표 spec sheet 3개는 `get_screenshot`으로 시각 재확인.

**최우선 재확인(0-9/0-10절, 문서 복구 후 미커밋 구간) — 전부 PASS, 불일치 없음**:
- TypeSelector(`257:28`): Selected 4종 hex 전부 doc과 정확히 일치(family #ffe4e8/#ff5a76/#a8003b, company #d8fff5/#17a398/#0a4f49, other #ede0ff/#9b72cf/#4b0d9c, friend #e0f0ff/#4a90d9/#1a4c88), Unselected 보더 `component/typeselector-unselected-border`(#ccc) 일치.
- NeoInput(`288:12`)/CornerInput(`288:27`): Error=No/Yes × Focus=No/Yes × Content 매트릭스, nodeId·variant 개수(7개)·색상(border-error #ff5a76, text-error #a8003b, NeoInput placeholder #bbb vs CornerInput placeholder #ccc 분리 유지) 전부 doc과 일치.
- NeoSelect(`387:13`): State=Default/Open × Content=Placeholder/Selected 4 variant, hover 옵션 `color/bg-hover-muted`(#f1f1f1) 바인딩, Elevation/Raised 적용 전부 일치.

**HIGH(신규) — Button(`259:609`) Style=Amber, State=Focus(`284:1010`) 스퓨리어스 보더**: Amber Default/Hover/Press/Disabled/Loading 어디에도 보더가 없는데, Focus 상태에서만 `border border-black border-solid`(1px 검정)가 코드에 추가로 붙어있음을 발견 — `get_screenshot`(스펙 시트 `343:50`)으로 시각 재확인 결과 Amber Focus 버튼에만 실제로 얇은 검은 테두리가 렌더링됨(Default/Hover/Press/Disabled/Loading은 테두리 없음, Coral/Neutral Focus는 이 문제 없음). NeoBtn(`259:126`, 스펙 시트 `342:3`)의 동일 Amber/Focus는 이 문제가 없음을 대조 확인 — Button 컴포넌트 1건에 국한된 버그. Focus 순수성 원칙(9-1절: 링 추가 외 배경/보더/텍스트 불변) 위반. **위치: Button 컴포넌트, Style=Amber, State=Focus, node `284:1010`, Component Specs 페이지 `343:50`.**

**MEDIUM(신규) — 버튼류 5개 컴포넌트 Focus 배경 fill 토큰 미바인딩(하드코딩), 광범위**: NeoBtn/Button/Icon Button/Row Action Button/Table Row Action의 Focus variant는 예외 없이 배경을 raw hex(`bg-white`, `bg-[#ffcb47]`, `bg-[#17a398]` 등)로 직접 지정하고 있고, 같은 Style의 Default 형제는 전부 `var(--color-*)` 토큰으로 바인딩돼 있음(예: Amber Default `var(--color-amber-500,#ffcb47)` vs Amber Focus `bg-[#ffcb47]`). 현재 resolved 색상은 Default와 정확히 같아 시각적 회귀는 없으나, "No token = no component" 원칙 위반이며 향후 팔레트 토큰이 바뀌면 Default만 갱신되고 Focus는 옛 값에 고정되는 드리프트 위험이 있음. 대조군으로 NeoInput/CornerInput/NeoSelect/Sidebar Nav Item의 Focus는 전부 정상적으로 토큰 바인딩을 유지하고 있어(예: Sidebar Nav Item Active+Focus `bg-[var(--color-amber-500,#ffcb47)]`) 이 결함이 9-2절 버튼류 전용 패턴임을 확인. 약 32개+ Focus 노드 영향.

**LOW(신규) — Contact Row(`351:299`) 루트 배경 `bg-white` 하드코딩**: 형제 컴포넌트(Card/NeoBtn Neutral 등)는 `var(--color-gray-0,white)` 토큰을 쓰는데 Contact Row 루트만 raw `bg-white`. 위와 같은 계열의 경미한 바인딩 누락.

**Focus 순수성 전수 확인 결과(위 Button/Amber 1건 제외 전부 PASS)**: TypeSelector(Selected/Unselected 8쌍 전부 배경·보더·텍스트 동일, 링만 추가 — 스크린샷 `343:1146` 확인), NeoInput/CornerInput(스크린샷 `344:721` 확인, 4개 variant 전부 보더색·텍스트색 Focus=No/Yes 동일), Sidebar Nav Item(Active+Focus 토큰 동일 유지, Inactive+Focus는 9-5절 정정된 3px OUTSIDE 스트로크 기법 정상 렌더링 — 스크린샷 `343:1106` 재확인), NeoBtn(Amber Focus 정상, 보더 추가 없음 — 스크린샷 `342:3` 확인), Icon Button/Row Action Button/Table Row Action(보더·텍스트색 Focus=Default 동일 유지, 배경만 위 MEDIUM 항목의 토큰 미바인딩).

**나머지 컴포넌트 재확인**: CatBadge(`256:17`, 4종 전부 CatBadge 팔레트 hex 일치), Card(`262:15`, 전부 토큰 바인딩), Toast(`263:53`, success/error 배경·텍스트 토큰 바인딩 정상), Logo(`263:692`, Teal/White 배경 반전 토큰 정상), Avatar(`104:131`, `component/avatar-bg` 토큰 정상) — 전부 PASS, 하드코딩 없음.

**종합**: 총 16개 컴포넌트 직접 재조회(최우선 4개 + 버튼류 5개 + CatBadge/Contact Row/Card/Toast/Logo/Avatar/Sidebar Nav Item), 3개 스펙시트 스크린샷 재확인. **HIGH 1건**(Button Amber Focus 스퓨리어스 보더), **MEDIUM 1건**(버튼류 5개 Focus 배경 토큰 미바인딩, 광범위), **LOW 1건**(Contact Row 배경 하드코딩). 최우선 재확인 대상 4개(TypeSelector/NeoInput/CornerInput/NeoSelect)는 문서-Figma 불일치 0건으로 전부 PASS — 문서 복구가 정확했음을 확인. Count Pill/Pixel 아이콘 11종/Link는 이번 라운드에서 개별 재조회하지 않음(Link는 14차에 이미 확인, Pixel 아이콘은 13차 EyeOff만 확인 — 다음 라운드에서 나머지 10종 개별 재확인 권고).

# Design System — 확정 토큰/컴포넌트 인벤토리 (State Ledger)

**⚠ ui-designer 등 컴포넌트를 소비하는 모든 에이전트는 반드시 1~7절만 참조하고 8절(Legacy)은 절대 사용하지 않는다.**

이 문서는 design-systems가 만든 토큰(변수)·컴포넌트·아이콘 등록 현황의 **현재 확정 상태**다. Figma FOUNDATIONS/COMPONENTS 구역(비주얼 원본)의 텍스트 미러이며, ui-designer·interaction-designer 등 컴포넌트를 소비하는 모든 에이전트의 소스 오브 트루스다. design-systems가 토큰/컴포넌트를 추가·수정할 때마다 이 파일의 내용을 최신 상태로 유지한다(로그가 아니다 — 만든 과정은 각 에이전트의 `.claude/agent-memory/*.md` 작업 로그와 git 히스토리에 남는다). **⚠ "최신 상태로 유지"는 절대 Write 도구로 파일 전체를 다시 쓰라는 뜻이 아니다 — 이 문장 자체가 과거 두 차례 파일 손상 사고의 원인으로 지목됐다(아래 복구 메모 참고). 반드시 먼저 전체를 Read한 뒤 Edit 도구로 필요한 부분만 바꾸거나 끝에 새 절을 추가한다.**

**fileKey**: `zgGlMBwFglaDlaeyP4CkgR`

**⚠ 2026-07-15 문서 복구 메모 1차(투명성 기록)**: 이 세션 중 서브에이전트가 "파일 끝에 새 절만 append" 지시를 잘못 수행(전체 덮어쓰기)해 파일이 586줄→61줄로 손상되는 사고가 있었고, 이후 복구 과정에서도 한 차례 더 잘못된 번호(0-9/0-10)로 다른 내용이 섞여 들어가는 2차 혼선이 있었다. git 커밋(`4a0db785`, 520줄, 0-1~0-8절/1~9-5절)으로 대부분 복구했고, 커밋되지 않았던 실제 0-9/0-10절은 design-pl이 사고 직전 직접 읽어뒀던 원문으로 복원했다.

**⚠ 2026-07-15 문서 복구 메모 2차(투명성 기록)**: 1차 복구 직후 `.claude/agents/design-systems.md`에 "Write 전체 덮어쓰기 금지, 항상 전체 Read 후 Edit/append" 규칙을 명문화했음에도 불구하고, 같은 세션 안에서 체크박스 등록 라운드 중 **재차 손상**(697줄→372줄, 섹션 1~11 및 12절 전체 소실, 0-1~0-18 하위 항목만 생존)됐다. 근본 원인으로 위 문단의 "덮어써서 최신 상태로 유지한다"는 이 문서 자신의 표현이 지목됐다 — 하네스 규칙집(design-systems.md)만 고치고 정작 이 문서 자체의 자기소개 문장은 그대로 둬서, 서브에이전트가 이 문서를 읽을 때마다 "덮어쓰라"는 지시를 다시 흡수했을 가능성이 높다. 이번엔 git HEAD(`4cdcbc9`, 624줄)를 기준으로 삼되, 커밋되지 않았던 12절(Button Focus 결함 수정)과 0-15~0-18절은 세션 중 직접 읽어뒀던 diff 기록으로 재구성했고, 위 문단 표현 자체도 함께 정정했다.

## 0. 이번 라운드 — 사용자 확정 디자인(8개 프레임)에서 직접 추출 (2-4번 규칙)

이번 라운드는 `docs/harness/design-team/figma-file-organization.md` 2-4번 규칙에 따라, **AI 파일럿을 거치지 않고** 사용자가 Figma에서 직접 만들어 확정한 8개 프레임("확정 디자인 - 절대 원본 건들지 말것-", 부모 섹션 `248:11689`)에서 실제 사용된 값을 직접 관찰(`get_screenshot`/`get_metadata`)해 토큰·컴포넌트로 추출했다. 8개 프레임은 전부 읽기 전용으로만 관찰했고 내용/이름을 전혀 수정하지 않았다.

이 라운드 이전에 존재하던 "B-2 파일럿" 기반 컴포넌트(Button/Input/Select/Badge/Table Row/Sidebar Nav Item — 아래 8절)는 `docs/design/confirmed/user-confirmed-final-design.md`에 따라 **완전히 대체**됐다. 이름이 겹치는 3개 컴포넌트(Button, Row Action Button, Sidebar Nav Item)는 구분을 위해 기존 것을 `[Legacy B-2] ` 접두사로 리네임했다(내용은 전혀 건드리지 않음, 이름만 변경). **(갱신)** 나머지 겹치지 않는 이름(Input/Select/Badge/Table Row/Alert의 옛 컴포넌트) 5개도 동일하게 `[Legacy B-2] ` 접두사로 리네임 완료했다(내용은 전혀 건드리지 않음, 이름만 변경 — 8절 참고). Avatar(`104:131`)만 유일하게 리네임 대상에서 제외됐다 — 확정 디자인과 정확히 일치해 현재도 유효하기 때문이다. 즉 옛 legacy 9개 컴포넌트 중 8개는 `[Legacy B-2] ` 접두사로 구분되고, Avatar 1개만 접두사 없이 그대로 유효 컴포넌트로 남는다. **이 문서의 "1~7절"이 현재 정식 소스이고 "8절 legacy"는 참고용 이력**이다.

### 0-1. design-qa 감사 후 정정 (추가 라운드, 원본 프레임은 무수정)

design-qa 감사에서 등록 컴포넌트 3건이 원본 확정 프레임 실측값과 다르게 잘못 추출되어 있음이 지적되어, 컴포넌트/토큰 쪽만 정정했다(원본 8개 프레임은 이번에도 손대지 않음, 읽기 전용 재확인만 수행). 재확인은 `get_metadata`/`use_figma` 읽기 전용 스크립트로 hex 값까지 재실측했다.

1. **TypeSelector(`257:28`) 색상 불일치** — 미선택 칩 보더가 `component/typeselector-unselected-text`(#888, 텍스트용 토큰)를 잘못 재사용해 텍스트와 보더가 같은 색으로 나오고 있었다. 원본 실측 보더는 `#CCCCCC`. 또한 "회사" 선택 텍스트가 `component/typeselector-company-selected-accent`(#E6800A, 보더/닷 전용 토큰)를 잘못 재사용하고 있었다. 원본 실측 텍스트색은 `#7A3D00`. → 신규 원시값 `color/gray/300`(#CCCCCC), `color/orange/900`(#7A3D00) + 신규 컴포넌트 토큰 `component/typeselector-unselected-border`, `component/typeselector-company-selected-text`를 만들어 TypeSelector 전용으로 재바인딩(4개 미선택 칩 보더 + "기타/선택" 칩 보더 + "회사/선택" 텍스트, 총 6개 노드). 다른 컴포넌트는 이 두 신규 토큰을 참조하지 않는다.
2. **Table Row Action(`260:100`) 텍스트 크기 불일치** — 등록 컴포넌트가 13px였으나 원본(main `214:590`/`214:593` 등)은 10px. → "수정"/"삭제" 텍스트 노드 fontSize를 10px로 직접 정정.
3. **Row Action Button(`260:95`) Neutral 보더 불일치** — `color/ink/900`(#1A1A1A, 2px 기본 컴포넌트 보더용)을 재사용하고 있었으나, 원본(사이드바 "카테고리 관리" 소형 버튼, `215:2365`/`215:2414` 등)과 확정 스펙 문서(§4-1)의 실측값은 `#1C1F21`로 별개 값이다. → 신규 원시값 `color/ink/800`(#1C1F21, ink/900과 별개) + 신규 컴포넌트 토큰 `component/row-action-button-border-neutral`을 만들어 Row Action Button Neutral 보더에만 재바인딩. `component/button-border-neutral`(ink/900, NeoBtn/Button Neutral 아웃라인 2px 보더)은 그대로 유지 — 두 보더 토큰은 굵기·용도가 다른 별개 값이라 통합하지 않는다.

정정 후 `use_figma` 읽기 전용 스크립트로 3건 모두 원본과 hex 단위로 일치함을 재확인했다(아래 1절/5절에 갱신 반영).

### 0-2. 후속 정정 및 추가 (2026-07-14)

design-qa/graphic-designer의 갭 감사에서 발견된 두 건을 처리했다(원본 확정 프레임은 이번에도 전혀 수정하지 않음, 읽기 전용 재확인만 수행).

1. **`Pixel/Star`(`255:11`) description 오기 정정** — description 텍스트가 "흰색"이라고 적혀 있었으나, 마스터 컴포넌트의 실제 vector fill을 재확인한 결과 잉크 `#1a1a1a`였다(graphic-designer가 `docs/design/graphic-assets.md`에 이미 관찰해 기록해둔 특이사항). **fill 값 자체는 정상이라 건드리지 않았고, description 텍스트만 실측값에 맞게 정정**했다: "로고 심볼 내부 별(12px, 잉크 #1a1a1a). 마스터 컴포넌트 fill 실측값 기준(로고 심볼 코랄 원 안에서는 흰색으로 인스턴스 오버라이드되어 사용됨). PxStar 원본."
2. **`Pixel/Eye` 신규 추출·등록** — 9종 추출 라운드(0절)에서 누락됐던 비밀번호 표시/숨김 토글 아이콘. 확정 login 프레임(`247:6666`) 안의 원본 `PixelEye`(`247:6814`, 14×10, 6개 vector 블록, 잉크 `#1a1a1a`)를 비파괴적으로 clone(원본은 무수정, 여전히 `247:6814`에 그대로 존재) → "Icons" 페이지(`96:7`, y=2000 클러스터, x=1080)로 이동 → `createComponentFromNode`로 `Pixel/Eye` 컴포넌트(`281:405`)로 정식 등록했다. 나머지 9종과 동일한 마이크로 픽셀 아이콘 트랙 컨벤션(단색 실루엣, 사각 블록 조합, 안티앨리어싱 없는 각진 형태)을 그대로 따른다. 스크린샷으로 형태 일치 검증 완료. 아래 4절 Icons 목록에 반영.

### 0-3. Legacy 컴포넌트 폐기(컴포넌트 등록 해제) 및 CornerInput 정정 (2026-07-14)

사용자가 "레거시라고 되어 있는것은 폐기처리해줘. 컴포넌트를 해제해야 피그마에 얽히지 않을거 같아"라고 요청해, 8절 Legacy 목록의 컴포넌트 8개(Avatar 제외)를 대상으로 처리했다. 원본 확정 8개 프레임(`248:11689` 하위)은 이번에도 전혀 손대지 않았다.

**절차**: ① 8개 컴포넌트를 참조하는 INSTANCE가 파일 전체(전체 20개 페이지, 확정 8개 프레임 포함 — 읽기 전용 확인만)에 실제로 존재하는지 `use_figma` 읽기 전용 스크립트로 전수 검색했다. ② 인스턴스가 없는 컴포넌트만 COMPONENT/COMPONENT_SET → FRAME 전환(자식 노드를 새 FRAME으로 이동해 시각적 내용을 그대로 유지하고 원래 COMPONENT/COMPONENT_SET 노드는 제거)을 진행했다.

**인스턴스 검색 결과**:
- **`[Legacy B-2] Table Row`(`103:7`) — 인스턴스 7개 발견, 해제하지 않고 보류**: Table Row 페이지(`103:3`)에 1개(`103:77`), 파일럿 페이지(`222:524`)의 `❌ 폐기 — B-2 레이아웃 미반영(재해석됨) — Contacts — With Data — Screen` 프레임 안에 6개(`110:220`/`110:234`/`110:248`/`110:262`/`110:276`/`110:290`). 지시에 따라 이 컴포넌트는 건드리지 않았다.
- 나머지 7개(`[Legacy B-2] Button` `97:47`, `[Legacy B-2] Row Action Button` `166:421`, `[Legacy B-2] Sidebar Nav Item` `103:106`, `[Legacy B-2] Input` `100:46`, `[Legacy B-2] Select` `101:64`, `[Legacy B-2] Badge` `102:65`, `[Legacy B-2] Alert` `104:108`)는 인스턴스 0개 확인 → 아래 표대로 전환 완료.

**전환 결과** (이름은 그대로 유지, 자식 노드/시각 내용 무손실 이전 — 스크린샷으로 개별 검증 완료):

| 컴포넌트 | 페이지 | 기존 ID (COMPONENT_SET, 삭제됨) | 신규 ID (FRAME) |
|---|---|---|---|
| [Legacy B-2] Button | `97:8` | `97:47` | `314:843` |
| [Legacy B-2] Row Action Button | `103:3` | `166:421` | `314:319` |
| [Legacy B-2] Sidebar Nav Item | `103:92` | `103:106` | `314:876` |
| [Legacy B-2] Input | `100:2` | `100:46` | `314:879` |
| [Legacy B-2] Select | `101:3` | `101:64` | `314:893` |
| [Legacy B-2] Badge | `102:3` | `102:65` | `314:897` |
| [Legacy B-2] Alert | `104:2` | `104:108` | `314:902` |

전환된 7개는 이제 FRAME 타입이라 Figma의 Assets/Insert 패널에 컴포넌트로 노출되지 않는다. 전환 과정에서 CatBadge(`256:17`)/TypeSelector(`257:28`)/Toast(`263:53`)/Avatar(`104:131`)/Table Row(`103:7`)와 그 인스턴스(`103:77`)는 전혀 건드리지 않았음을 각 단계마다 재확인했다.

**CornerInput(`261:12`, Focus=Yes 짝 `288:13`) 결함 수정 — 확정 디자인과 불일치**: 메인 세션이 확인한 결함으로, 확정 디자인(로그인 `247:6666`의 `247:6801`/`247:6811`, main-수정 모달 `248:8103`의 `248:9813`/`248:9823`/`248:9833`)의 실제 "각진(radius 0) 입력창"은 순수 2px ink 사각 보더 하나뿐이고 모서리 장식이 없다. 그런데 등록된 CornerInput에는 네 모서리에 8×8 `CornerBracket` 노드가 붙어 있어(확정 프레임에 없는 걸 임의로 추가한 오류) 정정했다.

- Focus=No(`261:12`)에서 `CornerBracket` 4개(`261:14`/`261:17`/`261:20`/`261:23`) 제거.
- Focus=Yes(`288:13`)에서 대응하는 `CornerBracket` 4개(`288:15`/`288:18`/`288:21`/`288:24`) 제거.
- 남은 자식은 텍스트 노드(`261:13`/`288:14`, placeholder "윤아")뿐이며, 시각 요소는 컴포넌트 루트의 흰 배경 + 2px ink(`color/ink/900` 바인딩) `INSIDE` 스트로크 + `radius 0`뿐임을 재확인(스크린샷 검증 완료).
- **폭 처리**: 로그인/가입 입력창 실측 352px, CornerInput 고정 392px(모달 쪽과 일치)로 서로 다르다. 새 variant를 만들지 않고 **392px를 베이스로 유지**하며, 로그인/가입처럼 352px가 필요한 컨텍스트는 인스턴스 리사이즈로 대응하기로 컴포넌트 description에 명시했다.

**후속 검증(0-5절, 2026-07-14)**: 사용자 재검토 요청으로 `103:7` 해제 위험성을 격리된 테스트 복제본으로 실험 — COMPONENT→FRAME 전환 시 기존 INSTANCE가 빈 박스로 깨짐을 실증 확인, 실제 `103:7`은 인스턴스 7개가 남아있어 이번에도 전환하지 않았다. 상세 절차는 0-5절, 최신 상태는 8절 표 참고.

**최종 갱신(0-6절, 2026-07-14)**: 사용자가 인스턴스 깨짐을 알고도 해제를 재확정해 `103:7`도 최종 폐기(컴포넌트 해제) 완료됐다 — FRAME `357:303`으로 전환. 상세 절차와 인스턴스 깨짐 관찰 결과는 0-6절 참고.

### 0-4. Link 텍스트 링크 신규 등록 + Component Specs 페이지 신설 (2026-07-14)

design-prompter 브리프에 따라 두 작업을 진행했다(원본 확정 8개 프레임은 이번에도 무수정, 읽기 전용 관찰만).

**Link 등록 — 관찰 경위**: 브리프가 지목한 login(`247:6666`) 내 "로그인으로 돌아가기"류 텍스트를 먼저 확인했으나, login 프레임 자체에는 그 문구가 없다. 짝을 이루는 Join(`241:1552`) 프레임에서 `241:2144`("로그인으로 돌아가기")를 찾아 실측한 결과, 이는 흰 배경+2px ink 보더+radius10의 **버튼**(`241:2140`, Noto Sans KR Black 14px, 그림자 없음)으로, 이미 등록된 Button 컴포넌트의 Neutral 스타일과 구조가 동일하다 — 확정 스펙 5-1절이 "로그인으로 돌아가기"를 "보조/중립 버튼"으로 분류한 것과 일치한다. 따라서 이 문구 자체는 신규 컴포넌트 없이 기존 Button/Neutral 인스턴스로 커버된다.

브리프의 "짝을 이루는 유사 보조 텍스트 링크" 예외 조항에 따라, login 프레임에서 실제로 순수 텍스트 링크 패턴(배경/보더/그림자 없는 밑줄 텍스트)을 찾아 `247:6827`("비밀번호 찾기")을 실측 근거로 채택했다: Noto Sans KR **Bold** 12px, 색상 `#17A398`(기존 primitive `color/teal/500`과 정확히 일치), letterSpacing 0, lineHeight 18px, textDecoration UNDERLINE, effects 없음(그림자 없음 확인).

**토큰**: 기존 `color/text-accent`(레거시, teal/700 별칭) 발견했으나 실측값(#17A398)과 불일치해 재사용하지 않았다. 신규 semantic `color/text-link`(→teal/500, scope TEXT_FILL, `VariableID:340:3`)를 Semantic Colors 컬렉션(`VariableCollectionId:95:16`)에 추가 — 신규 primitive는 불필요(teal/500 기존 재사용).

**텍스트 스타일**: `Body/Link`(Noto Sans KR Bold 12px, letterSpacing 0, lineHeight 18px, underline) 신규 등록.

**컴포넌트**: "Link" 전용 페이지(`341:2`, Sidebar Nav Item과 Logo 사이에 배치) 신설, `Link` 컴포넌트(`341:3`, 69×18, auto-layout hug, TEXT 컴포넌트 프로퍼티 `Label#341:0`로 라벨 오버라이드 가능) 등록. Default 상태만 등록(브리프 지침대로 이번 라운드는 새 인터랙션 설계 없음 — hover/underline 인터랙션 필요 시 7-2절에 후속 과제로 기록). 사용처: login(현재, "비밀번호 찾기"), SCR-004(예정). **(2026-07-15 갱신)** 사용자가 Figma에서 직접 텍스트를 "비밀번호 재설정"으로 변경 완료 — 팀은 재작업하지 않음.

**Component Specs 페이지**: FOUNDATIONS 구역에 `"Component Specs"` 페이지(`342:2`, Icons `96:7` 바로 뒤에 배치) 신설, 기존 9개 컴포넌트(NeoBtn/Button/Icon Button/Row Action Button/Table Row Action/Sidebar Nav Item/TypeSelector/NeoInput/CornerInput) + 신규 Link까지 총 10개 스펙 시트 프레임을 나란히 배치했다. 각 시트는 제목+설명+전체 variant 그리드(상태별 텍스트 라벨 포함)로 구성되어 variant 피커를 열지 않고도 전체 상태를 훑어볼 수 있다. 상세 프레임 ID는 5절 컴포넌트 표 각주 참고.

### 0-5. Contact Row 컴포넌트 조립 + Legacy Table Row(`103:7`) 해제 위험성 검증 + Link 문서 정리 (2026-07-14, design-pl 실행 브리프)

design-pl이 사용자 승인을 받아 전달한 4개 작업을 처리했다(원본 확정 8개 프레임은 이번에도 전혀 수정하지 않음, 읽기 전용 재관찰만).

**1) Contact Row 컴포넌트 신규 조립** — Table Row 페이지(`103:3`)에는 그동안 "Documentation" 헤더 스펙(`103:4`)만 있었고 실제 조립 컴포넌트가 없었다. main 확정 프레임(`214:349`) 테이블 첫 행(`214:573`)을 `get_design_context`로 재실측한 결과:
- 이름(`214:575`): Noto Sans KR **Bold** 14px, `#1a1a1a` — 기존 등록 `Body/Button` 텍스트 스타일과 정확히 일치. design-prompter가 문서 대조로 제시한 가설을 이번에 직접 관찰로 최종 확정했다.
- 전화번호(`214:578`): Noto Sans KR Regular 14px, `#555555` — `Body/Regular` + `color/text-muted-strong`.
- 주소(`214:581`): Noto Sans KR Regular 14px, `#777777` — `Body/Regular` + `color/text-muted`.
- 행 컨테이너(`214:573`): 흰 배경, 하단 1px `#ede6d8` 보더만(다른 3변은 없음), gap 12px, padding 좌우16/상10/하11.
- CatBadge(`214:584`)·Table Row Action(`214:589`/`214:592`, 41×25, teal/coral 아웃라인)은 기존 등록 컴포넌트(`256:5` 등 CatBadge 4종/`260:96`/`260:98`)와 완전히 동일 — 새로 그리지 않고 그대로 인스턴스화했다.

**신규 토큰**: 구분선 `#ede6d8`이 1-1절에 미등록임을 재확인(grep 0건) → primitive `color/beige/200`(#EDE6D8, scope=[]) + semantic `color/border-divider-warm`(→beige/200, scope STROKE_COLOR, `VariableID:350:3`) 신규 등록.

**컴포넌트**: `Contact Row`(`351:299`, 774×47, HORIZONTAL auto-layout, variant 불필요 — 단일 컴포넌트) 신규 등록. `[Legacy B-2] Table Row`(`103:7`)·"Documentation" 헤더(`103:4~103:6`)와 이름이 겹치지 않게 명명. 이름/전화번호/주소는 TEXT 컴포넌트 프로퍼티(`name#351:0`/`phone#351:1`/`address#351:2`, 기본값 "윤아"/"010-1234-5678"/"서울시 마포구")로 노출해 인스턴스별 값 교체 가능. 하단 구분선은 `color/border-divider-warm` 바인딩(strokeBottomWeight만 1, 나머지 3변 0). 조립 직후 `use_figma` 읽기 전용 스크립트로 재대조했다: 이름 fill이 `color/ink/900`(#1A1A1A), 전화번호가 `color/text-muted-strong`(#555555), 주소가 `color/text-muted`(#777777)에 각각 바인딩됐고, CatBadge/Table Row Action 인스턴스의 `mainComponent`가 각각 `256:5`(Category=Friend)/`260:96`(Style=Neutral)/`260:98`(Style=Danger) — 기존 등록된 정식 컴포넌트 — 로 정확히 연결됐음을 hex·ID 단위로 확인했다(design-systems 자체 재대조 규칙).

**스펙 시트**: `Component Specs` 페이지(`342:2`)에 `Spec — Contact Row`(`352:726`, 기존 10개와 동일한 제목+회색 설명+그리드+라벨 레이아웃) 신규 추가 — 총 11개 스펙 시트.

**2) Legacy Table Row(`103:7`) 해제 위험성 검증** — 사용자 재검토 요청에 따라 격리된 테스트 복제본으로 실험했다(실제 `103:7`과 그 인스턴스 7개는 이 과정에서 전혀 건드리지 않음):
1. `103:7`을 화면 밖 스크래치 좌표(x=3000)로 clone → 테스트 마스터(`353:422`, COMPONENT) 생성, 테스트 인스턴스(`353:429`) 1개 생성.
2. 전환 전 `get_screenshot`: 테스트 인스턴스가 원본과 동일하게 "윤아 / 01012345678 / 서울시 / 가족" 텍스트를 정상 표시함을 확인.
3. **테스트 마스터만** 0-3절과 동일한 절차(자식 6개를 새 FRAME으로 이동, 원 COMPONENT 노드 제거)로 전환.
4. 전환 후 테스트 인스턴스 재확인 — **`childrenCount: 0`, `get_screenshot` 결과 완전히 빈 흰색 박스**로 내용이 전부 소실됨을 확인(detach된 정적 복사본으로 유지되는 것이 아니라 인스턴스 자체가 깨짐).
5. 테스트 마스터·변환된 FRAME·테스트 인스턴스를 전부 삭제해 실제 파일에는 아무 산출물도 남기지 않음(재확인: page.children 개수가 테스트 전후 동일, 이름 검색 0건).

**결론 — 위험함, 전환하지 않음**: 0-3절에서 이미 전환한 7개 legacy 컴포넌트는 전환 당시 인스턴스가 0개라 이 파괴적 부작용이 드러나지 않았을 뿐, COMPONENT(또는 COMPONENT_SET)를 "자식 이동+원 노드 제거" 방식으로 FRAME 전환하면 그 컴포넌트를 참조하는 기존 INSTANCE는 전부 빈 박스로 깨진다는 것이 이번 테스트로 실증됐다. `103:7`은 실제 인스턴스 7개(`103:77` 1개 + 파일럿 `❌ 폐기 —` 프레임 안 6개)가 아직 존재하므로, 지금 전환하면 그 7개 화면이 전부 빈 박스가 된다. **따라서 실제 `103:7`은 이번에도 전환하지 않고 컴포넌트 상태 그대로 유지한다** — 최종 판단(예: `❌ 폐기 —` 프레임 자체를 먼저 정리해 인스턴스를 0개로 만든 뒤 재시도할지 여부)은 design-pl 경유 사용자에게 넘긴다.

**3) Link(`341:3`) 44×44 터치 타겟 미달 문서화** — 7-2절에 독립 항목 추가(아래 참고). 컴포넌트 크기/스타일 변경 없음.

**4) Link WCAG 대비 3.12:1 — TODO→RESOLVED 이동** — 사용자가 "이번에는 3.12:1로 WCAG AA 기준 미달 기준 무시하고 그냥가자. 테스트니깐"이라고 확정 결정. 7-1절 6번 항목으로 이동, 7-2절/3절 문구 갱신(아래 참고). 원본 프레임/토큰 값(#17A398)은 변경하지 않음 — 순수 문서 상태 변경.

### 0-6. Legacy Table Row(`103:7`) 최종 해제 완료 — 사용자 재확정 (2026-07-14, design-pl 실행 브리프)

**배경**: 0-5절에서 격리된 테스트 복제본으로 `103:7`의 COMPONENT→FRAME 전환 위험성을 실증 검증한 결과(기존 INSTANCE 7개가 빈 박스로 깨짐), 실제 `103:7`은 전환하지 않고 컴포넌트 상태로 보류했다. design-pl이 이 검증 결과를 사용자에게 보고했고, **사용자가 "해제해줘"라고 명시적으로 재확인·재승인했다** — 인스턴스가 깨지는 걸 알면서도 해제를 진행하기로 결정한 것이다.

**절차**: 0-3절에서 나머지 7개 legacy 컴포넌트에 적용한 것과 완전히 동일한 절차를 그대로 따랐다. `103:7`(타입은 COMPONENT_SET이 아니라 variant 없는 단일 COMPONENT, HORIZONTAL auto-layout, 700×62)의 시각 속성(fills/strokes/padding 12·9/itemSpacing 16/strokeBottomWeight 1/cornerRadius 0 등)을 그대로 복제한 새 FRAME을 만들고, 원본의 자식 노드 6개(`103:8` name/`103:9` phone/`103:10` address/`167:28` category/`167:29` edit-action/`167:35` delete-action)를 이동(move, 동일 노드 ID 유지 — 클론이 아님)한 뒤 원래 COMPONENT 노드(`103:7`)를 제거했다. 이름은 "[Legacy B-2] Table Row"로 동일하게 유지, 위치(x=40, y=220)도 원본과 동일.

**결과 — 신규 FRAME**: `357:303`(700×62, Table Row 페이지 `103:3`). `get_screenshot`으로 재확인한 결과 이름("윤아")/전화번호/주소/카테고리("가족") 텍스트가 원본과 동일하게 정상 렌더링됨 — 마스터 콘텐츠 자체는 무손실로 이전됐다.

**결과 — 인스턴스 7개 깨짐(예상된 결과, 실측 관찰)**: 전환 직후 7개 인스턴스 전부 `childrenCount: 0`으로 확인됐다.
- `103:77`(Table Row 페이지 `103:3`, 700×62): `get_screenshot` 결과 **완전히 빈 흰색 박스** — 텍스트/아이콘/보더 전혀 없이 텅 빈 사각 영역만 남았다.
- `110:220`/`110:234`/`110:248`/`110:262`/`110:276`/`110:290`(파일럿 페이지 `222:524`의 `❌ 폐기 — B-2 레이아웃 미반영(재해석됨) — Contacts — With Data — Screen` 프레임 안, 각 1024×62): 부모 프레임(`110:201` "Contact List")을 `get_screenshot`으로 재확인한 결과, 상단 타이틀("연락처 목록 — 총 6건")·검색창·테이블 헤더("이름"/"전화번호"/"주소"/"종류")는 정상 표시되지만, 그 아래 데이터 행 6개는 전부 완전히 빈 상태(이름/전화번호/주소 텍스트, 카테고리 배지, 수정·삭제 아이콘 전혀 없음)로 나타났고 행 사이 얇은 회색 구분선만 남았다. 0-5절 격리 테스트가 예측한 것과 정확히 일치하는 깨짐 양상이다.

**결론 — 되돌리지 않음, 알려진 트레이드오프로 문서화**: 이 깨짐은 이번에 새로 발생한 결함이 아니라, 0-5절에서 이미 격리 테스트로 실증되고 design-pl을 통해 사용자에게 보고된 뒤 사용자가 인지하고 승인한 결과다. 지시에 따라 되돌리지 않았다. 참조하는 7개 화면(Table Row 페이지 예시 1곳 + 이미 `❌ 폐기 —` 라벨이 붙어 대체된 파일럿 화면 6곳)이 대상이며, 확정 8개 원본 프레임과 현재 정식 5절 컴포넌트(Contact Row 등)에는 영향이 없다. 상세는 7-1/7-2절과 8절 Legacy 표에 반영.

**(추가 갱신, 0-7절, 2026-07-14) 이 트레이드오프는 이후 사용자가 design-pl을 통해 인스턴스 복구를 재요청해 해소됐다** — 마스터 콘텐츠(`357:303`) 기반으로 7개 인스턴스 전부 시각적으로 복구 완료. 상세는 아래 0-7절 참고.

### 0-7. Legacy Table Row(`103:7`) 해제 순서 실수로 깨진 인스턴스 7개 복구 (2026-07-14, design-pl 실행 브리프)

**배경 — 실수 경위**: 0-6절에서 `103:7`을 FRAME(`357:303`)으로 전환할 때, COMPONENT_SET/COMPONENT를 FRAME으로 바꾸기 전에 **남아있던 인스턴스 7개를 먼저 Detach Instance로 분리하는 절차가 없었다** — 곧바로 "자식 이동 + 원본 COMPONENT 노드 제거" 순서로 진행했다. 사용자가 인스턴스 깨짐 가능성을 알고도 해제를 승인한 것 자체는 0-6절에 이미 기록돼 있으나, "해제해도 된다"는 승인이 "인스턴스 깨짐을 그대로 방치해도 된다"는 뜻은 아니었다 — 이후 design-pl을 통해 사용자가 깨진 인스턴스 7개의 복구를 요청해 이번 라운드가 발생했다.

**1) Undo 가능 여부 확인 — 실제 실증, 통념만으로 판단하지 않음**: "Plugin API에 스크립트로 호출 가능한 undo 함수가 없다"는 통념을 그대로 믿지 않고, 실 콘텐츠와 무관한 격리 스크래치 스크립트로 `figma.commitUndo()`/`figma.triggerUndo()` 두 API를 직접 호출해 실증했다. 결과:
- 타입 정의(`plugin-api-standalone.d.ts` L280-305)에는 `commitUndo()`("Commits actions to undo history")와 `triggerUndo()`("Reverts to the last `commitUndo()` state")가 실제로 선언돼 있다 — 존재 자체는 통념과 다르다.
- 그러나 이 `use_figma` 실행 환경에서 두 메서드를 실제로 호출하면 각각 `"Error: in commitUndo: figma.commitUndo is not yet supported"` / `"Error: in triggerUndo: figma.triggerUndo is not yet supported"` 런타임 오류로 **즉시 거부**됐다. 스크립트 원자성 규칙에 따라 실패한 스크립트는 파일에 아무 변경도 남기지 않아 클린업이 필요 없었다.
- **결론**: 이 환경에서는 undo/history 기반 복구가 API 차원에서 아예 불가능하다는 것이 실증됐다(선언은 있지만 미지원). 따라서 최우선 시도였던 undo는 성립하지 않았고, 2단계(마스터 콘텐츠 기반 재구성)로 진행했다.

**2) 마스터 콘텐츠(`357:303`) 기반 재구성**: 마스터를 clone하여 `103:77`(참고용 인스턴스, 위치만 조정)과 파일럿 6개(`110:220`~`110:290`, 1024px로 resize 후 원래 자식 인덱스에 순서 보존 삽입)를 각각 교체했다. 결과 신규 노드: `360:297`(구 `103:77`), `361:85`/`361:92`/`361:99`/`361:106`/`361:113`/`361:120`(구 `110:220`/`110:234`/`110:248`/`110:262`/`110:276`/`110:290`).

**3) 데이터 정확성**: `103:77`→`360:297`은 마스터 예시 데이터 그대로 사용해 완전 복원(원본과 동일, 참고용이라 실 데이터 이슈 없음). 파일럿 6개는 원본 데이터 단서(노드 이름/description/형제 노드)가 전혀 없어 완벽한 원본 복원이 불가능했다 — 마스터 예시 데이터를 이름/전화번호/주소/카테고리별로 순환시켜(윤아·민준·서연·지호·하은·도윤) 최소한의 시각적 다양성만 부여한 **대체 예시 데이터**다. 실 서비스 데이터가 아님을 은폐하지 않고 명시한다.

**4) 검증**: `360:297`은 마스터와 픽셀 단위로 동일하게 렌더링됨을 확인. 파일럿 부모(`110:201`) 전체 재확인 결과 6개 행이 겹침·깨짐 없이 정상 배치되고 각 행에 서로 다른 예시 데이터가 표시됨을 확인(빈 박스 요소 없음).

**결론**: 완료 최소 기준("빈 박스로 깨진 상태" 해소)은 7개 노드 전부 충족했다. `103:7`은 컴포넌트로 재전환하지 않고 FRAME(`357:303`) 상태 그대로 유지한다. 원본 확정 8개 프레임과 정식 등록된 `Contact Row`(`351:299`) 등 5절 컴포넌트는 이번에도 전혀 건드리지 않았다.

**8) 표준 절차 신설 — 컴포넌트 해제 전 Detach 우선 규칙 (재발 방지)**: 향후 동일 실수를 막기 위해, **COMPONENT/COMPONENT_SET → FRAME 전환(컴포넌트 등록 해제) 작업은 항상 아래 순서를 표준 절차로 따른다**:
1. 전환 대상 컴포넌트를 참조하는 INSTANCE가 파일 전체(모든 페이지)에 존재하는지 `use_figma` 읽기 전용 스크립트로 먼저 전수 검색한다.
2. 인스턴스가 하나라도 있으면, **자식 이동/원본 노드 제거를 하기 전에 그 인스턴스들을 먼저 `instance.detachInstance()`로 분리**해 독립 FRAME으로 만든다.
3. Detach가 끝난 뒤에만 원본 컴포넌트를 "자식 이동 + 원본 노드 제거" 방식으로 FRAME 전환한다.
4. 인스턴스가 0개로 확인된 경우에만 이 Detach 단계를 생략하고 곧바로 전환해도 안전하다.

### 0-8. 페이지(canvas) 레벨 구조 재정렬 — 구분 페이지 6개 신설 + 전체 순서 재배열 (2026-07-14, design-pl 실행 브리프)

design-pl이 사용자 승인을 받아 전달한 순수 **페이지 레벨** 구조 작업이다 — 어떤 페이지의 내부 콘텐츠도 생성/수정하지 않았다(생성/이름변경/순서변경만). 파일럿 페이지(`222:524`) 내부는 이번에도 위치 이동 외에는 전혀 열어보거나 손대지 않았다.

**배경**: 사용자가 `docs/harness/design-team/figma-file-organization.md` 1번 항목의 구역 구분 스타일(`--- BRAND ---` 등)을 실제 Figma 파일 페이지 목록에도 반영해달라고 요청했다.

**1단계 — 구분용 빈 페이지 6개 생성**: `--- BRAND ---`(`364:2`) `--- FOUNDATIONS ---`(`364:3`) `--- COMPONENT SPECS ---`(`364:4`) `--- CONCEPTS ---`(`364:5`) `--- COMPONENTS ---`(`364:6`) `--- SCREENS ---`(`364:7`). 아직 실제로 쓰이는 구역이 없는 `--- GRAPHIC ASSETS ---`(Graphic Assets 페이지는 사용자가 삭제해 현재 존재하지 않음)/`--- MOTION ASSETS ---`/`--- MARKETING ---`는 이번 라운드에서 만들지 않았다.

**2단계 — 전체 29개 페이지 순서 재배열**: `figma.root.insertChild(index, pageNode)`로 각 페이지 노드 자체만 목표 인덱스로 이동했다(페이지의 자식 노드/내용은 전혀 건드리지 않음). 결과는 아래 8절 "페이지 순서" 표 참고.

**3단계 — 안전 원칙 준수 확인**: 파일럿 페이지(`222:524`)는 위치만 이동, 원본 확정 8개 프레임(`248:11689` 하위)은 전혀 건드리지 않았다.

**4단계 — 완료 후 검증**: 최종 페이지 순서가 목표 순서(29개)와 정확히 일치 확인. 파일럿 페이지 `childrenCount: 10`(변경 없음), 확정 디자인 섹션(`248:11689`) `childrenCount: 8`(손상 없음) 확인.

**결론**: 신규 구분 페이지 6개 생성 완료, 전체 29개 페이지가 목표 순서로 재배열 완료. 어떤 페이지의 내부 콘텐츠도 생성/삭제/수정하지 않았다. 최신 페이지 순서는 아래 8절 표로 전면 갱신했다.

### 0-9. TypeSelector 선택 상태 색상을 CatBadge 기준으로 재바인딩 (2026-07-14, design-pl 실행 브리프)

**배경**: 2절(구 버전)은 "TypeSelector는 CatBadge와 의도적으로 다른 팔레트"라고 명시하고 있었다. 사용자가 이 판단을 뒤집어 "TypeSelector가 CatBadge와 연관돼 있다 — CatBadge 기준으로 맞춰라, 디자인 확정에도 반영하겠다"고 확정 지시했다. 새 컨셉을 판단하는 작업이 아니라, 이미 확정한 CatBadge 값으로 다른 컴포넌트를 재바인딩하는 유지보수 작업이다.

**0) 인스턴스 연결 리스크 선확인 (다른 작업보다 먼저 수행)**: `main-수정`(`248:8103`) 내부의 실제 "종류" 선택 칩 그룹(`248:9835`, 이름 "TypeSelector")을 `get_metadata`로 읽기 전용 재확인한 결과, 이 노드는 TypeSelector 마스터(`257:28`)의 INSTANCE가 아니라 순수 정적 FRAME이었다(같은 프레임 안에서 발견된 유일한 INSTANCE는 Avatar `104:131`뿐). 즉 마스터 컴포넌트 색상을 바꿔도 확정 프레임에는 아무 영향이 없음을 확인한 뒤에만 1)로 진행했다. 확정 프레임 자체는 이번에도 전혀 쓰기 작업을 하지 않았다(읽기 전용 관찰만).

**1) 선택(Selected) 상태 4개 카테고리 재바인딩**: 새 raw hex나 새 semantic 토큰을 만들지 않고, CatBadge(`256:17`)가 이미 쓰는 기존 Semantic Colors 토큰(컬렉션 `VariableCollectionId:95:16`)에 TypeSelector의 Selected 칩 fill/stroke/text를 직접 재바인딩했다.
- **친구(Friend, `257:16`/`287:918`)**: 이미 `color/category/friend-bg`(#E0F0FF)/`-border`(#4A90D9)/`-text`(#1A4C88)에 바인딩돼 있어 재확인만 하고 변경하지 않았다.
- **가족(Family, `257:19`/`287:921`)**: 기존 `component/typeselector-family-selected-bg`(#27AE60 초록, stroke와 text 양쪽에 같은 변수가 잘못 재사용되던 버그성 오명명) → `color/category/family-bg`(#FFE4E8)/`color/category/family-border`(#FF5A76)/`color/category/family-text`(#A8003B)로 교체.
- **회사(Company, `257:25`/`287:927`)**: 기존 `component/typeselector-company-selected-bg`(#FFF3E0)/`-accent`(#E6800A)/`-text`(#7A3D00, 주황 계열) → `color/category/company-bg`(#D8FFF5)/`color/category/company-border`(#17A398)/`color/category/company-text`(#0A4F49, 민트/틸 계열)로 교체.
- **기타(Other, `257:22`/`287:924`)**: 기존엔 선택 상태에서도 강조색이 전혀 붙지 않아(`component/typeselector-unselected-border`/`-text`를 그대로 재사용, 미선택과 시각적으로 완전히 동일) 사실상 무채색 처리였다. `main-수정`(`248:9835`) 원본을 재관찰한 결과, 이 프레임 인스턴스는 4개 칩 중 "회사"만 선택된 상태만 보여줄 뿐 "기타 선택"이 실제로 어떻게 디자인됐는지 가리키는 관찰 근거가 전혀 없었다 → 브리프 지침(증거 없으면 기본값으로 CatBadge 색 채택)에 따라 `color/category/other-bg`(#EDE0FF)/`color/category/other-border`(#9B72CF)/`color/category/other-text`(#4B0D9C)로 통일했다.
- Unselected(미선택, 회색 계열, `component/typeselector-unselected-border`/`-text`)는 이번 작업과 무관 — 8개 Unselected variant 전부 변경하지 않았다.
- 재바인딩 직후 `use_figma` 읽기 전용 스크립트로 12개 노드(칩 6개의 fill/stroke + 텍스트 6개, Focus=No/Yes 각 3쌍)의 hex·변수명을 CatBadge 4종 원본과 다시 대조해 hex 단위로 정확히 일치함을 확인했다.

**2) 스펙 시트 갱신**: `Component Specs` 페이지의 `Spec — TypeSelector`(`343:1146`)의 8개 Selected 셀은 컴포넌트 variant의 INSTANCE라 마스터 재바인딩이 자동 반영됐다. 설명 텍스트(`343:1148`)만 "CatBadge와 별도 팔레트" 문구를 제거하고 "CatBadge와 통일" 문구로 갱신했다.

**3) Description 갱신**: TypeSelector(`257:28`)와 CatBadge(`256:17`) 컴포넌트 description을 각각 이번 결정 반영 문구로 갱신했다.

**하위 절 반영(⚠ 복구 메모)**: 이 절이 원래 2절/1-2절/1-3절에 반영했던 편집(2절 결정 반전, 1-2절 "TypeSelector도 공용 카테고리 토큰 공유" 명시, 1-3절 orphan 토큰 표기)은 아래 해당 절에도 이번 복구에서 함께 반영했다.

### 0-10. Input Error variant + Select Open variant 추가 (2026-07-14, design-pl 실행 브리프)

design-qa/design-pl이 사용자와 함께 확인한 두 갭(레거시엔 있었지만 정식 컴포넌트 추출 시 빠뜨린 기본 상태)을 처리했다. 레거시 참고 노드(`314:879`/`314:881`/`314:893`/`314:896`)는 이번에도 구조 참고용으로만 읽기 전용 관찰했고 원본은 무수정, 원본 확정 8개 프레임(`248:11689` 하위)도 전혀 손대지 않았다.

**A) NeoInput(`288:12`)/CornerInput(`288:27`) Error variant 추가**

**선행 조사**: `get_metadata`로 재확인한 결과 `314:879`(`[Legacy B-2] Input`, FRAME)의 자식 `314:881`("[Legacy B-2] Input/Error/Default")은 구 COMPONENT_SET이 FRAME으로 전환된 뒤 남은 정적 자식일 뿐(0-3절), 실측 결과 코랄 보더(1.5px, `#FF5A76` 상당) + **잉크색(#1a1a1a) 텍스트**였다(플레이스홀더 자체가 코랄은 아니었음). 지시대로 이 값을 그대로 베끼지 않고 "구조(보더+텍스트 색을 함께 error로 오버라이드하는 2-요소 신호)"만 참고해 새로 설계했다. 기존 coral 계열 semantic을 전수 확인한 결과 `color/background-error`(coral/100, 배너용)만 있고 보더·텍스트 전용 semantic은 없어 신규 alias 2개만 최소로 추가했다(신규 원시값 없음, 기존 `color/coral/500`/`color/coral/900` 재사용).

- 신규 semantic 토큰(Semantic Colors 컬렉션 `VariableCollectionId:95:16`): `color/border-error`(→coral/500 #FF5A76, scope STROKE_COLOR, `VariableID:378:2`), `color/text-error`(→coral/900 #A8003B, scope TEXT_FILL, `VariableID:378:3`).
- **State 축 설계**: Error를 Focus와 **직교(조합) 축**으로 설계했다(체크리스트가 Focus/Error를 별개 상태로 나열하지만 실무에서 "포커스된 채로 유효성 오류가 표시되는" 조합이 흔하기 때문). NeoInput/CornerInput 모두 기존 `Focus=No/Yes` 2-variant 세트에 `Error=No/Yes` 축을 추가해 2×2=4 variant로 확장 — 기존 2개 variant는 `Focus=No, Error=No`/`Focus=Yes, Error=No`로 리네임만 하고(노드 ID `261:10`/`288:10`/`261:12`/`288:13` 그대로 유지, 화면상 기존 참조 안 깨짐) 시각값은 무수정, `Error=Yes` 2개(`Focus=No, Error=Yes`/`Focus=Yes, Error=Yes`)만 clone 후 보더·텍스트만 오버라이드했다.
- **오버라이드 내용**: Error=Yes 클론 2개는 보더 색만 `color/border-error`, (플레이스홀더/값) 텍스트 색만 `color/text-error`로 교체했다. `Focus=Yes, Error=Yes`는 기존 Focus 링(`DROP_SHADOW` spread 3 ink 100%, offset 0,0)을 그대로 유지. **CornerInput은 0-3절 정정 베이스(모서리 CornerBracket 없는 순수 2px ink 사각 보더) 그대로 유지, Error variant에서도 브래킷을 되살리지 않았다**.
- **신규 노드 ID**: NeoInput `Focus=No, Error=Yes`=`378:4`, `Focus=Yes, Error=Yes`=`378:6` (ComponentSet `288:12`, 이제 408×124, `Focus`×`Error` 2×2). CornerInput `Focus=No, Error=Yes`=`378:856`, `Focus=Yes, Error=Yes`=`378:858` (ComponentSet `288:27`, 이제 856×160).
- **WCAG 재계산**: `color/border-error`(#FF5A76) on 흰색 배경 = **3.01:1** — WCAG 1.4.11 비텍스트(UI 컴포넌트 경계) 최소 3:1 기준 PASS(근소하지만 통과). `color/text-error`(#A8003B) on 흰색 배경 = **7.70:1** — 14px Regular 본문 텍스트 4.5:1 기준 여유 있게 PASS.
- **스펙 시트 갱신**: `Component Specs` 페이지의 `Spec — NeoInput`(`344:721`)/`Spec — CornerInput`(`344:740`)을 각각 2×2 그리드로 재구성했다 — 행 라벨 컬럼("Error=No"/"Error=Yes")을 추가하며 기존 정합성 버그(컬럼 헤더와 실제 셀 x좌표 어긋남)도 함께 바로잡았다.
- **자체 재대조**: 8개 variant(NeoInput 4 + CornerInput 4) 전부 strokeHex/textHex/boundVariable id/effects/cornerRadius/width/height를 재조회해 기대값과 hex 단위로 정확히 일치함을 확인했다.

**B) NeoSelect(`261:660`) Open variant 추가**

**선행 조사**: `314:893`(`[Legacy B-2] Select`, FRAME)의 자식 `314:896`("[Legacy B-2] Select/Open")을 구조 참고용으로만 관찰 — 트리거(180×31) 아래 4px gap을 두고 options-panel(180×100)이 있고, 그 안에 옵션 3개(가족/친구/기타, 각 33px 높이, 좌우 padding12/상하 padding8)가 세로로 배치된 구조였다. 색상(레거시 특유의 팔레트)은 참고하지 않고 버렸다 — NeoSelect(`261:660`)가 이미 쓰는 컴포넌트 톤(흰 배경, 2px ink 보더, radius10)으로 전부 재해석했다.

- **구조**: `State=Open` 신규 variant는 트리거(기존 Default와 **동일한 룩**) + 옵션 패널(VERTICAL auto-layout, hug, 흰 배경+2px ink 보더+radius10)을 4px 간격으로 세로 배치. 옵션 3개(가족/친구/기타)는 각각 좌우12/상하8 padding의 행으로, 텍스트는 `Body/Regular`+`color/ink/900` 바인딩.
- **텍스트 컴포넌트 프로퍼티**: 옵션 3개 라벨을 하드코딩하지 않고 `Option 1#387:3`(기본값 "가족")/`Option 2#387:4`("친구")/`Option 3#387:5`("기타") TEXT 프로퍼티로 노출했다.
- **State 축 승격**: 기존 단일 COMPONENT `261:660`을 `figma.combineAsVariants`로 `State=Default`(원래 `261:660`과 동일 ID 유지, 시각값 무수정)/`State=Open`(신규)의 2-variant COMPONENT_SET(`387:13`, 명칭 "NeoSelect")으로 승격했다.
- **Elevation 판단**: 옵션 패널은 "배경 위에 얹혀 경계가 필요한 표면"(드롭다운)이라 판단해 `Elevation/Raised`(소프트 블러 그림자, 기존 Toast 전용에서 재사용) 효과 스타일을 바인딩했다. 트리거 자체(Default/Open 공통)는 이미 보더로 경계가 분명한 flat 요소라 elevation을 추가하지 않았다.
- **신규 노드 ID**: ComponentSet `387:13`("NeoSelect", 278×171, Select 페이지 `101:3`), `State=Default`=`261:660`(기존 ID 유지), `State=Open`=`387:12`(트리거 `387:2` + 옵션 패널 `387:5`).
- **스펙 시트 신규 생성**: NeoSelect는 5절에 스펙 시트가 없었으므로 `Component Specs` 페이지에 `Spec — NeoSelect`(`388:746`, 764×330)를 신규 생성 — Default/Open 2칸 그리드.
- **자체 재대조**: Default(무수정 확인)와 Open의 트리거·옵션패널(fill/stroke hex `#ffffff`/`#1a1a1a`, radius10, strokeWeight2, effectStyleId가 `Elevation/Raised`와 일치)을 재조회해 기대값과 정확히 일치함을 확인했다.
- **범위 제한 — 준수**: 이번 승인 범위는 Select=Open만이다. Select의 Focus/Disabled/Error 상태는 이번에 확장하지 않았다 — 아래 7-2절에 후속 과제로만 기록했다.

**화면정의서 갱신 필요성 메모(이 팀 소관 아님, 참고용)**: NeoInput/CornerInput Error variant와 NeoSelect Open variant는 이번에 컴포넌트 레벨에서만 신설됐다. 실제 화면에 이 상태를 언제·어떤 트리거로 노출할지는 화면정의서 영역이라 이 라운드에서 건드리지 않았다.

**하위 절 반영(⚠ 복구 메모)**: 이 절이 원래 1-2/1-3/3/5/7-2/8/9-3/9-4절에 반영했던 세부 편집(신규 semantic 토큰, WCAG 계산, 5절 컴포넌트 표 variant 갱신, 7-2 TODO 추가, 9-3/9-4 Error 축 언급)은 아래 해당 절에도 이번 복구에서 함께 반영했다.

### 0-11. NeoInput/CornerInput/NeoSelect Placeholder·Selected 축 확인 및 스펙 시트 대조 (2026-07-15)

기존에 이미 완성돼 있던 Placeholder 축(NeoInput/CornerInput)과 Content=Placeholder/Selected 축(NeoSelect)을 재생성 없이 `get_metadata`/읽기 전용 `use_figma`로 재대조만 수행했다.

**NeoInput(`288:12`) / CornerInput(`288:27`) — 각 7 variant 확인**: Content=Filled × Focus=No/Yes × Error=No/Yes(4개) + Content=Placeholder × Error=No×Focus=No/Yes, Error=Yes×Focus=No(3개) = 7개. Placeholder×Focus=Yes×Error=Yes(3중 조합)는 의도적 제외 — "포커스 중 에러는 blur 후 지연 표시"가 일반적 UX 관례라 실사용 빈도가 없다는 기존 확정 사유가 두 스펙 시트 설명 텍스트에도 그대로 명시돼 있음을 확인했다.

**NeoSelect(`387:13`) — 4 variant 확인**: `261:660`(Placeholder×Default), `387:12`(Placeholder×Open), `401:866`(Selected×Default), `401:869`(Selected×Open). Placeholder 문구는 텍스트 노드 `261:661`에서 "종류선택"으로 실측 확인.

**텍스트 색 바인딩 재대조**(대표 노드 1~2개씩만 확인):
- Placeholder 텍스트(NeoInput `398:885`, CornerInput `398:891`, NeoSelect `261:661`) 3곳 모두 `color/text-placeholder`(semantic, `VariableID:398:3`)에 바인딩돼 있고, 이 semantic은 `color/gray/300`(primitive, `VariableID:269:2`, #CCCCCC)을 alias한다. 사전 가설이었던 `color/text-muted-subtle`(#888)/`color/text-muted`(#777)가 아니라 placeholder 전용 별도 semantic 토큰이 이미 존재함을 확인했다(재바인딩 불필요, 기존 값을 그대로 문서화 — **0-12절에서 NeoInput만 별도 토큰으로 재조정됨**).
- Filled/Selected 텍스트(NeoInput `261:11`, CornerInput `261:13`)는 `color/ink/900`(`VariableID:95:9`, #1A1A1A)에 정상 바인딩 확인.

**스펙 시트 대조 결과 — 전부 이미 갱신 완료 상태, 재작업 불필요**:
- `Spec — NeoSelect`(`388:746`, Component Specs 페이지 `342:2` 하위): 이미 4칸(Content=Placeholder/Selected × State=Default/Open) 2×2 그리드로 구성돼 있고 각 셀에 인스턴스 + 상태 라벨 텍스트가 붙어 있음을 확인.
- `Spec — NeoInput`(`344:721`): Content=Filled/Placeholder(행) × Focus×Error 4열(열) 그리드로 7칸 + 제외 1칸(Placeholder×Focus=Yes×Error=Yes, "제외 — 포커스 중 에러 지연 표시 UX 관례" 라벨) 구성이 이미 반영돼 있음을 확인.
- `Spec — CornerInput`(`344:740`): 동일 구조(7칸 + 제외 1칸)로 이미 반영돼 있음을 확인.

**결론**: 이번 라운드는 순수 확인 작업으로 종료 — 변수·컴포넌트·스펙 시트 어느 것도 신규 생성/수정하지 않았다. 확정 8개 프레임(`248:11689`)은 이번에도 열람하지 않았다.

### 0-12. NeoInput placeholder 텍스트 색 확정 프레임 재실측 결함 수정 (design-qa 스팟체크, 2026-07-15)

design-qa 스팟체크에서 NeoInput/CornerInput이 동일한 `color/text-placeholder`(#CCCCCC)를 공유하고 있었으나, 확정 프레임 실측값이 컴포넌트별로 다르다는 결함이 발견됐다.

**재실측 결과**:
- CornerInput 컨텍스트(로그인 `247:6666`/가입 `241:1552`) 확정 실측값: #CCCCCC — 기존 `color/text-placeholder` 값과 **일치, 수정 불필요**.
- NeoInput 컨텍스트(main-수정 `248:8103`의 검색창, 확정 8개 프레임 `248:11689` 하위 텍스트 노드 `248:8500`)를 `use_figma` 읽기 전용으로 재실측한 결과 fill hex `#BBBBBB`(r=g=b=0.7333..., 미바인딩 raw 값)로 확인 — 기존 컴포넌트 값(#CCCCCC)과 **불일치** 확인.

**토큰 전수 검색**: 기존 `color/gray/*` primitive(0/50/100/150/200/300/400/450/500/600/650) 전수 대조 결과 #BBBBBB와 정확히 일치하는 값 없음(가장 가까운 `gray/300`=#CCCCCC, `gray/400`=#9CA3A6, 둘 다 차이 있음). 근사 재사용 대신 신규 primitive를 최소로 추가했다.

**신규 토큰**:
- Primitive(`VariableCollectionId:95:5`, mode `95:0`): `color/gray/350`(#BBBBBB, scope=[] 숨김, `VariableID:434:4`) — 기존 `gray/300`과 `gray/400` 사이의 신규 스텝.
- Semantic(`VariableCollectionId:95:16`, mode `95:1`): `color/text-placeholder-input`(→gray/350, scope `TEXT_FILL`, `VariableID:434:5`) — **NeoInput 전용** placeholder 텍스트 색. WEB code syntax `var(--color-text-placeholder-input)`.

**바인딩**: NeoInput(`288:12`) 7 variant 중 Placeholder 텍스트 노드 2곳만 재바인딩했다 — `398:885`(Content=Placeholder, Focus=No, Error=No)와 `398:887`(Content=Placeholder, Focus=Yes, Error=No). `398:889`(Content=Placeholder, Focus=No, Error=Yes)는 원래부터 에러 색(`VariableID:378:3`, #A8003B)에 바인딩돼 있어 이번 작업 대상이 아니다 — 손대지 않았다.

**CornerInput 미변경 확인**: CornerInput(`288:27`)의 Placeholder 텍스트 노드 3개(`398:891`/`398:893`/`398:895`)는 재대조 결과 그대로 `color/text-placeholder`(#CCCCCC, `VariableID:398:3`) 바인딩 유지 — 건드리지 않았다.

**결과**: 이제 NeoInput과 CornerInput은 서로 다른 semantic placeholder 토큰을 쓴다 — NeoInput은 `color/text-placeholder-input`(#BBBBBB), CornerInput은 `color/text-placeholder`(#CCCCCC)를 그대로 유지한다. 재대조(읽기 전용) 결과 두 컴포넌트 모두 각자의 확정 실측값과 hex 단위로 일치함을 확인했다. `Spec — NeoInput`(`344:721`)은 이미 인스턴스 기반 그리드라 신규 바인딩이 자동 반영됐다.

**부수 — Icons 페이지 EyeOff 디자인 노트 정리**: graphic-designer가 남긴 근거 메모(`414:6`, Icons 페이지)의 마지막 문장이 "아직 raw, design-systems가 컴포넌트화 예정"으로 오래돼 있던 것을 "정식 컴포넌트 `Pixel/EyeOff`(`415:892`)로 등록 완료"로 갱신했다. 근거 서술 본문(6블록 중 3블록 유지, (b)안 채택 사유 등)은 그대로 보존했다.

확정 8개 프레임(`248:11689`)은 이번에도 읽기 전용으로만 재실측했고 수정하지 않았다.

### 0-13. Pixel/EyeOff 아이콘 정식 등록 (2026-07-15)

`Pixel/Eye`(`281:405`)는 "비밀번호 표시/숨김 토글"로 설명돼 있었으나 짝(숨김 상태) 아이콘이 없던 갭을 처리했다. graphic-designer가 Pixel/Eye의 조형 관례(14×10 캔버스, 잉크 `#1a1a1a`)를 실측해 상단 코너 3블록(피크)만 제거하고 중앙 바+하단 코너 2블록을 유지한 "닫힌 눈" 실루엣을 raw FRAME(`414:2`, 3개 RECTANGLE 자식)으로 그렸고, design-systems가 `createComponentFromNode`로 `Pixel/EyeOff`(`415:892`) 정식 컴포넌트로 등록했다. Icons 페이지(`96:7`)에 `Pixel/Eye` 바로 옆(x=1241, y=403) 배치, 기존 Pixel/* 10종의 120px 간격 규칙을 그대로 연장했다. design-qa 스팟체크에서 형태가 "닫힌 눈/숨김"으로 명확히 읽히고(다른 기호로 오독될 위험 없음) 기존 관례를 따른다고 PASS 판정했다. 아래 4절 Icons 목록에 반영(10종→11종).

### 0-14. FOUNDATIONS 페이지 소급 동기화 완료 (2026-07-15)

이번 세션 동안 1~5절 표에는 이미 등록된 색상/텍스트/이펙트 토큰 중 상당수가 FOUNDATIONS 구역 4개 시각 카탈로그 페이지(Colors/Typography/Spacing/Elevation)에는 반영되지 않은 채 남아 있었다(`docs/harness/design-team/figma-file-organization.md` 2-5번 규칙 소급 적용). 원본 확정 8개 프레임(`248:11689` 하위)은 이번에도 읽기 전용 대조 대상에서 전혀 손대지 않았다.

**Colors(`95:2`, 루트 `95:40`)** — 신규 섹션 4개 추가(기존 Primitives/Semantic/Contrast Notes 섹션은 무수정, 아래에 이어붙임):
- "신규 Primitives" 22개(ink/800, blue/coral/purple/mint/teal 계열 카테고리 원시값, TypeSelector 레거시 원시값, 뮤트 텍스트 3종, beige/200, gray/150, gray/350).
- "Category Colors" 12개(`color/category/*` — CatBadge+TypeSelector Selected 공용, 0-9절 근거).
- "Semantic Colors (Additional)" 13개(text-muted-*, text-link, border-divider-warm, border-neutral, background-success/error, border-error, text-error, text-placeholder(-input), bg-hover-muted).
- "Component Colors" 8개(button-border-neutral 등 4개 활성 + typeselector-*-selected-* orphan 4개, orphan 명시 라벨링).
총 55개 스와치 신규 등록. 각 hex를 1-1~1-3절 원문과 재대조해 전부 일치 확인(`get_screenshot` 검증 완료).

**Typography(`95:3`, 루트 `95:198`)** — 1-5절 11종 텍스트 스타일(Wordmark/Logo, Heading/Page, Heading/Modal, Label/Micro, Label/CountNumber, Label/Badge, Body/Button, Body/Banner, Body/Regular, Body/Caption, Body/Link) 전부 누락 상태였다 → 기존 레이아웃 패턴(라벨+실물 샘플 박스) 그대로 11개 스펙시멘 신규 추가, 폰트/사이즈/트래킹/lineHeight/underline까지 1-5절 값과 일치시켜 실제 폰트로 렌더링(`get_screenshot` 검증 완료, Baloo 2 ExtraBold·Noto Sans KR Black/Bold/Medium/Regular·Inter Black/Semi Bold 스타일명은 `listAvailableFontsAsync`로 사전 확인).

**Elevation(`116:5`, 루트 `116:6`)** — 기존에 `Elevation/Raised`/`Elevation/Overlay` 데모와 적용 가이드는 이미 반영돼 있었음(변경 없음). 누락돼 있던 `Shadow/Hard-1`(1px)/`Shadow/Hard-2`(2px)/`Shadow/Hard-6`(6px) 하드 스티커 그림자 데모 3개와, 9-1절 Hover/Press/Focus/Disabled 블렌드·링 공식 문서 블록(4개 불릿)을 신규 추가.

**Spacing(`95:4`, 루트 `95:162`)** — 기존 legacy spacing(1~8)/radius(sm/md/lg/full)는 무수정. 1-1절에 신규 등록됐던 `radius/none`(0)/`radius/6`(6)/`radius/10`(10)와 `border/hairline`(1)/`border/base`(2)/`border/heavy`(3)가 이 페이지 카탈로그에는 반영되지 않아 신규 섹션 2개(Radius/Border)로 추가.

4개 페이지 전부 스크린샷으로 최종 검증 완료(레이아웃 겹침/잘림 없음, 텍스트·색상 정상 렌더링). 신규 변수/컴포넌트는 생성하지 않았다 — 순수 카탈로그 시각화 보강 라운드다.

### 0-15. Focus 축을 State 열거형 값으로 소급 통합 — TypeSelector/NeoInput/CornerInput/Sidebar Nav Item (2026-07-15, design-pl 실행 브리프)

기존 자기 규칙(9-2절)이 버튼류 5개(NeoBtn/Button/Icon Button/Row Action Button/Table Row Action)에는 이미 적용돼 있었으나, 보조 컴포넌트 4개(9-3절 "Focus 상태만 추가한 보조 컴포넌트")는 여전히 State(또는 그에 준하는 축)와 별개로 `Focus=No/Yes` 직교 축을 갖고 있었다. 이번 라운드는 이 규칙을 4개에 소급 적용한 순수 구조 재편이다 — **사용자가 "시각 변경 없음"을 명시했고, 새로 그리는 작업이 아니다.**

**0) 인스턴스 확인 절차(예외 없음)**: 삭제 후보 9개(TypeSelector Selected+Focus=Yes 4개 `287:918`/`287:921`/`287:924`/`287:927`, NeoInput Filled+Focus=Yes 2개 `288:10`/`378:6`, CornerInput Filled+Focus=Yes 2개 `288:13`/`378:858`, Sidebar Nav Item Active+Focus=Yes 1개 `287:14`)를 `use_figma` 읽기 전용 스크립트로 파일 전체(28개 페이지, 순차 순회 — 병렬 호출 금지 원칙 준수)에서 검색한 결과, **전부 `Component Specs` 페이지(`342:2`)의 스펙 시트 그리드 셀에서만 참조되고 있었다**(9건 모두, 다른 화면·파일럿·확정 8개 프레임에는 참조 0건). 이 인스턴스들은 3번 작업(스펙 시트 갱신 — 삭제된 셀 제거)에서 어차피 제거 대상이므로, 먼저 구 Grid 프레임 4개(`343:1149`/`403:11`/`403:918`/`343:1109`)를 제거해 인스턴스를 0건으로 만든 뒤(재검색으로 확인) 마스터 variant를 삭제하는 순서로 진행했다.

**1) TypeSelector(`257:28`)**: Category(4)×State=Selected/Unselected(2)×Focus=No/Yes(2)=16 → Category(4)×State=Selected/Unselected/Focus(3)=12. 각 카테고리의 "Unselected+Focus=Yes"(`287:906`/`287:909`/`287:912`/`287:915`)는 시각 그대로 이름만 "State=Focus"로 정리, "Selected+Focus=Yes" 4개(`287:918`/`287:921`/`287:924`/`287:927`)는 삭제. "Selected+Focus=No"→"State=Selected", "Unselected+Focus=No"→"State=Unselected"로 이름만 정리(시각 무수정). 재조회 결과 ComponentSet 속성이 `Category`(Friend/Family/Other/Company)×`State`(Unselected/Selected/Focus)로 정확히 재편됨을 확인.

**2) NeoInput(`288:12`)/CornerInput(`288:27`)**: 실사용 매트릭스 7 variant → 5 variant. 기본 4개(Content=Filled/Placeholder × Error=No/Yes, 기존 Focus=No 값 그대로)는 이름에서 Focus 언급을 제거하고 새 `State` 축의 값 "Default"를 부여했다. 단일 Focus variant 1개는 기존 "Content=Placeholder, Focus=Yes, Error=No"(NeoInput `398:886`, CornerInput `398:892` — 문서상 확인됐던 placeholder 텍스트 자식 `398:887`은 `398:886`의 자식 텍스트 노드임을 매핑 표에서 확인)를 그대로 살려 "State=Focus"로 이름만 정리했다. 삭제 대상은 Filled×Focus=Yes×Error=No(NeoInput `288:10`/CornerInput `288:13`), Filled×Focus=Yes×Error=Yes(NeoInput `378:6`/CornerInput `378:858`) 4개 — Placeholder×Focus=Yes×Error=Yes는 애초에 존재하지 않았다(0-11절에서 이미 의도적으로 제외돼 있었음). ComponentSet 속성은 `Content`(Filled/Placeholder)×`Error`(No/Yes)×`State`(Default/Focus) 3개 축으로 재편됐고, State=Focus는 Content=Placeholder·Error=No 조합에서만 존재하는 부분 조합이다(전체 2×2×2=8 그리드가 아니라 5개만 채움). **⚠ 2026-07-15 정정(0-16절)**: 이 삭제 작업 중 `Content=Filled, Error=Yes, Focus=Yes`(NeoInput `378:6`, CornerInput `378:858`) 조합을 실수로 함께 삭제했다 — 기존 규칙("Focus×Error×Placeholder 3중 조합만 제외, Focus×Error(값 있음)는 유지")을 놓친 것으로, 사용자 발견 후 0-16절에서 복원했다. 현재 NeoInput/CornerInput은 각 6 variant다.

**3) Sidebar Nav Item(`258:29`)**: State=Active/Inactive(2)×Focus=No/Yes(2)=4 → State=Active/Inactive/Focus(3)=3. "Inactive+Focus=Yes"(`287:17`, 9-5절 3px ink OUTSIDE 스트로크 특수 구현)는 이름만 "State=Focus"로 정리, fills/strokes/effects는 전혀 건드리지 않았다 — 재대조 결과 `fillsCount:0`, `strokesCount:1`(strokeWeight 3, strokeAlign OUTSIDE), `effectsCount:0`, 173×40 그대로 확인. "Active+Focus=Yes"(`287:14`)는 삭제. "Active+Focus=No"→"State=Active", "Inactive+Focus=No"→"State=Inactive"로 이름만 정리.

**4) 스펙 시트 4개 재구성**: `343:1146`(TypeSelector, Category×State 12칸 그리드)/`344:721`(NeoInput, Content×Error 2×2 기본 그리드 + 별도 라벨된 단일 State=Focus 셀, 총 5칸)/`344:740`(CornerInput, 동일 패턴 5칸)/`343:1106`(Sidebar Nav Item, State=Active/Inactive/Focus 3칸 가로 배치)를 전부 auto-layout 기반으로 다시 조립했다. 라벨에서 "Focus=No/Yes" 표기를 전부 제거하고 새 property 구조에 맞는 라벨(예: "Content=Placeholder, Error=No, State=Focus")로 교체, 캔버스 상 설명 TEXT 노드(`343:1148`/`344:723`/`344:742`/`343:1108`)도 새 variant 공식으로 갱신했다. **주의사항 — 발견 및 정정**: auto-layout Cell 컨테이너의 기본 `clipsContent=true`가 Focus 링(`DROP_SHADOW` spread 3px)을 잘라내는 것을 스크린샷 검증 중 발견해, 전 Cell/Row/Grid 컨테이너에 `clipsContent=false`를 명시적으로 설정해 정정했다(NeoInput/CornerInput 개별 Focus 셀 확대 스크린샷으로 링 렌더링 확인 완료). **NeoInput/CornerInput의 `344:721`/`344:740`은 0-16절에서 다시 2칸으로 확장됐다.**

**5) description 갱신**: 4개 ComponentSet의 `description` 필드(Figma 컴포넌트 메타데이터)에 새 variant 공식과 소급 통합 배경을 추가했다(TypeSelector/CornerInput은 기존 내용 뒤에 신규 문단 추가, NeoInput/Sidebar Nav Item은 formula 문장을 새로 포함해 갱신) — 기존 서술 내용은 삭제하지 않고 보존했다.

**6) 자체 재대조(design-systems 규칙, 생략 불가)**: `get_metadata`로 4개 ComponentSet 전부 목표 개수(12/5/5/3)와 property 정의(`Category`/`State`, `Content`/`Error`/`State`, `State`)가 정확히 일치함을 확인. `get_screenshot`으로 TypeSelector 전체(12칩 — Unselected 4/Selected 4/Focus 4, CatBadge 색 유지), NeoInput 전체(5필드, Focus 셀 확대로 링 확인), CornerInput 전체(5필드, 동일), Sidebar Nav Item `287:17` 개별("전체 6" 카운트필 그대로, 3px ink OUTSIDE 스트로크 시각적으로 보존) 총 6곳을 재조회해 삭제 전과 시각적으로 동일함을 확인했다. 원본 확정 8개 프레임(`248:11689`)은 이번에도 열람하지 않았다 — 이 4개 컴포넌트 자체가 확정 프레임 밖의 인터랙션 상태 확장물(9절)이라 원본과 무관하다.

**결론**: 인스턴스 충돌(다른 화면에서의 예기치 않은 참조)은 없었다 — 유일한 참조처가 스펙 시트 자체였고, 이는 이번 작업의 일부로 함께 정리됐다. 삭제 9개(마스터 variant), 이름 정리 20개(TypeSelector 12 + NeoInput 5 + CornerInput 5 − Sidebar 3, 총 25개 노드가 리네임됨 — 정확히는 TypeSelector 12 + NeoInput 5 + CornerInput 5 + Sidebar 3 = 25개 유지 노드 전부 이름 정리), ComponentSet 4개의 property 축이 각각 재편됨.

### 0-16. NeoInput/CornerInput Focus×Error(값 있음) 조합 복원 — 0-15절 소급 통합 시 실수로 함께 삭제된 1건 정정 (2026-07-15)

**배경**: 0-15절에서 TypeSelector/NeoInput/CornerInput/Sidebar Nav Item의 `Focus=No/Yes` 직교 축을 버튼류(9-2절)와 동일한 단일 State 열거형 값으로 소급 통합하는 작업을 진행하며, NeoInput(`288:12`)/CornerInput(`288:27`)에서 `Content=Filled, Error=Yes, Focus=Yes`(빨간 에러 보더+검은 포커스 링이 함께 있는 조합) 노드를 실수로 같이 삭제했다. 이는 실수다 — 9-1절 Focus 순수성 원칙과는 별개로, 0-10절/디자인팀 판단 기준에 이미 있던 기존 규칙("Focus×Error×Placeholder 3중 조합은 제외하지만, Focus×Error(값 있음/Filled 상태)는 계속 만든다")을 놓친 것이다. 사용자가 실제 화면(`344:721`/`344:740` 스펙 시트)에서 직접 이 갭을 발견해 복원을 요청했고, 메인 세션을 통해 정식 승인받았다.

**작업 범위**: NeoInput(`288:12`)/CornerInput(`288:27`)만. TypeSelector/Sidebar Nav Item은 Error 축 자체가 없어 무관 — 이번에도 건드리지 않았다.

**복원 절차**: 기존 `Content=Filled, Error=Yes, State=Default` 노드(NeoInput `378:4`, CornerInput `378:856` — 빨간 보더 `color/border-error` + 빨간 텍스트 `color/text-error`)를 각각 clone한 뒤, 기존 `State=Focus` variant(Content=Placeholder×Error=No 기반, NeoInput `398:886`/CornerInput `398:892`)와 동일한 ink 포커스 링(`DROP_SHADOW`, offset 0,0, blur 0, spread 3px, `#1a1a1a` 100%, alpha 1)만 추가했다. 배경·보더색·텍스트색은 Filled+Error=Yes 그대로 유지(빨간 보더+빨간 텍스트 유지, 링만 얹음) — 그 외 어떤 속성도 손대지 않았다.

- **신규 노드**: NeoInput `Content=Filled, Error=Yes, State=Focus` = `456:2`(180×36, ComponentSet `288:12` 이제 6 variant). CornerInput `Content=Filled, Error=Yes, State=Focus` = `456:4`(392×44, ComponentSet `288:27` 이제 6 variant).
- **Placeholder×Error=Yes×Focus(3중 조합)는 여전히 만들지 않는다** — 기존 예외(0-11절에서 이미 의도적으로 제외돼 있었음) 그대로 유지, 이번에도 손대지 않았다.
- **자체 재대조(design-systems 규칙, 생략 불가)**: 신규 2개 노드의 `strokes`(hex `#FF5A76`, boundVariable `VariableID:378:2` = `color/border-error`), 텍스트 `fills`(hex `#A8003B`, boundVariable `VariableID:378:3` = `color/text-error`), `effects`(`DROP_SHADOW`, spread 3, offset 0,0, color `#1a1a1a` alpha 1)를 재조회해 기존 `Content=Filled, Error=Yes, State=Default` 노드 및 기존 `State=Focus` 참조 노드와 hex·바인딩 단위로 정확히 일치함을 확인했다. ComponentSet property 정의도 `State` 값이 `Default`/`Focus` 그대로(신규 값 추가 아님, 기존 열거값 재사용) 유지됨을 확인했다.

**Component Specs 스펙 시트 갱신(`344:721`/`344:740`)**: 기존 "State=Focus (단일, Content=Placeholder × Error=No 기반)" 1칸 라벨을 2칸으로 확장했다 — "State=Focus (Content=Placeholder, Error=No 기반)"과 "State=Focus (Content=Filled, Error=Yes 기반)"로 명확히 분리. 두 FocusSection은 VERTICAL auto-layout 프레임(기존 구조 그대로, itemSpacing 8)이라 label+cell 쌍이 세로로 스택되는 형태로 확장됐다(가로 2칸이 아니라 세로로 label1/cell1 아래 label2/cell2가 이어지는 구조). 높이가 늘어난 만큼 상위 Grid/Spec 프레임 높이를 재계산해 리사이즈했고(NeoInput 382→478, CornerInput 438→542), Component Specs 페이지의 CornerInput 이후 시트 3개(Link `344:759`, Contact Row `352:726`, NeoSelect `388:746`)를 겹치지 않도록 아래로 재배치했다(페이지 내 다른 시트 내용은 무수정, 위치만 이동). 설명 텍스트(`344:723`/`344:742`)도 6 variant 공식과 이번 정정 배경으로 갱신했다. `get_screenshot`으로 두 스펙 시트 전체를 재확인해 6칸(기본 4 + Focus 2)이 모두 라벨과 함께 정상 렌더링됨을 확인했다.

**5절 컴포넌트 표 갱신**: NeoInput/CornerInput 행을 5→6 variant로 갱신(아래 5절 참고).

원본 확정 8개 프레임(`248:11689` 하위)은 이번에도 열람하지 않았다 — 이 두 컴포넌트의 Focus 상태 자체가 확정 프레임 밖의 인터랙션 상태 확장물(9절)이라 원본과 무관하다.

### 0-17. Checkbox 등록분 재대조·문서화 + 라디오/디바이더 필요성 판단 (2026-07-15, 커버리지 감사 라운드 + 2-6번 선제적 기본 구성)

**배경**: 직전 라운드가 출력 토큰 한도로 응답 중단됐으나, Figma 측 작업(Checkbox 컴포넌트+스펙 시트)은 중단 전에 이미 완료돼 있었다 — 이번 라운드 시작 시 페이지 목록 조회로 "Checkbox" 페이지(`474:881`) 존재를 확인하고, 신규 생성 대신 재대조·문서화만 수행했다. 원본 확정 8개 프레임(`248:11689`)은 읽기 전용으로만 재실측, 전혀 수정하지 않았다.

**1) Checkbox — 기존 등록분 재대조(신규 생성 없음, 전 항목 원본과 일치 확인)**

| 항목 | 값 |
|---|---|
| 페이지 | Checkbox(`474:881`), COMPONENTS 구역, Link(`341:2`)와 `--- SCREENS ---`(`364:7`) 사이 |
| ComponentSet | `474:899` (555×18, HORIZONTAL 그리드) |
| Variant | State=Default(Unchecked)/Checked/Focus/Disabled = 4 |
| TEXT 프로퍼티 | `label`(기본값 "로그인 상태 유지") |
| Box | 14×14, 흰배경(`color/gray/0`=`VariableID:95:10`) + 2px ink(`color/ink/900`=`VariableID:95:9`) INSIDE 보더, radius0 — 원본 `247:6823`과 hex·strokeWeight·strokeAlign·size 전부 일치 |
| Label 텍스트 | Noto Sans KR Regular 12px, `color/ink/900` fill에 paint opacity 0.5(원본 `247:6825` rgba(26,26,26,0.5) 그대로 재현, 노드 opacity 아님 — paint opacity) |
| Checked | Box 안에 8×7 벡터 체크마크(stroke `color/ink/900`, weight2) 추가 — 단순 프리미티브라 graphic-designer 투입 없이 직접 제작 |
| Focus | Default를 clone + ink 링(`DROP_SHADOW` spread3, offset0,0, `#1a1a1a` alpha1)만 추가(9-1절 공식 그대로) |
| Disabled | Box fill/stroke paint opacity 0.5, Label 노드 opacity 0.85(9-1절 Disabled 공식 그대로) |
| 신규 토큰 | 없음 — `color/gray/0`/`color/ink/900` 전부 기존 토큰 재사용 |
| 스펙 시트 | `Spec — Checkbox`(`475:762`, Component Specs 페이지 `342:2`), 제목+설명+4칸 그리드+상태 라벨(`get_screenshot` 확인) |

**재대조 방법**: `get_design_context`로 원본 `247:6822`(로그인 확정 프레임 내 "☐ 로그인 상태 유지")를 재실측하고, 등록된 4 variant의 fills/strokes/opacity/boundVariables를 `use_figma` 읽기 전용 스크립트로 재조회해 원본과 항목별 대조 — **불일치 0건**, 추가 수정 없음.

**2) 라디오 버튼 — 미등록 판단**

확정 8개 프레임(`248:11689` 하위) 전체를 `ELLIPSE` 타입 기준으로 전수 검색(32건 발견) — 전부 장식용 MemphisAccents 원, Avatar/유저 아이콘 원, `Icon/Alert` 원, TypeSelector 칩 내부 6×6 선택 dot이었고 "원형 보더+원형 채움 다이얼" 형태의 라디오 패턴은 0건. 화면정의서(`02_연락처관리_웹서비스_화면정의서_v1.5.md`) SCR-002 "종류"는 드롭다운(select)으로 명시("종류가 '입력'에서 '선택'으로 바뀐 이유" 절), 편집 모달 카테고리 선택은 TypeSelector(칩, `257:28`)가 이미 담당. 전체 화면 목록(SCR-001/002/003/004/900) 어디에도 단일 선택 그룹(라디오) 흐름 없음. **판단: 미등록(불필요)** — 근거 (a) 확정 프레임에 실물 0건 (b) SCR-002 종류는 Select/TypeSelector가 이미 커버 (c) 화면정의서 전체에 다른 단일선택 그룹 흐름 없음. 이후 실제로 라디오 그룹이 필요한 흐름이 생기면 그때 재검토.

**3) Divider — 미등록 판단**

Contact Row(`351:299`)가 이미 자체 하단 구분선(strokeBottomWeight1, `color/border-divider-warm`)을 갖고 있어 "행 사이 구분선" 용도는 흡수됨. 확정 8개 프레임 전체를 `LINE`/얇은 `RECTANGLE`(폭>30·높이≤3 또는 그 역) 기준으로 전수 검색한 결과 **0건** — 별도 divider 원시 도형 자체가 확정 프레임에 없음. 화면 목록도 SCR-001/002/003/004/900 5개뿐이고, 설정 그룹·모달 내부 섹션 구분처럼 Contact Row가 커버 못하는 별도 divider 필요 맥락이 현재 없음(모달은 Card 쉘 하나, 필드 나열에 섹션 구분 없음). **판단: 미등록(불필요)** — 근거 (a) Contact Row가 유일한 반복 리스트 용도를 이미 커버 (b) 확정 프레임에 독립 divider 도형 0건 (c) 화면정의서에 다른 그룹 구분 필요 화면 없음. 향후 설정 화면·모달 섹션 구분이 실제로 생기면 `color/border-divider-warm` 또는 유사 보더 토큰으로 재검토.

**4) CornerInput 스펙 시트(`344:740`) 라벨 확인** — 전체 텍스트 노드를 `use_figma` 읽기 전용으로 재조회한 결과 이미 0-16절 정정대로 "Content=Placeholder, Error=No, State=Focus"/"Content=Filled, Error=Yes, State=Focus"로 정확히 분리돼 있음을 확인 — 실수로 남은 "Content=Placeholder" 단독 라벨 없음. **수정 불필요, 변경 없음.**

**결론**: 이번 라운드 Figma 신규 생성 0건(전부 직전 라운드에서 이미 완료돼 있었음) — 재대조·문서화만 수행. Checkbox 4 variant 전부 원본과 hex/opacity/바인딩 단위 일치 확인. 라디오/디바이더는 근거를 갖춰 미등록으로 판단·기록.

### 0-18. Checkbox opacity 재대조 — design-qa FAIL과의 불일치 확인, raw script로 실측 결과 이미 정확함을 재확인 (2026-07-15)

design-qa의 스팟체크(Checkbox 라벨/Disabled Box paint opacity)가 "opacity 1(누락)"이라고 FAIL 보고했으나, 이는 코드 변환 결과(className 등)에 의존한 판단으로 추정된다. `use_figma` raw script로 4개 노드(`474:884`/`474:887`/`474:891` 라벨, `474:893` Disabled Box)를 직접 재조회한 결과, **4곳 모두 이미 정확히 반영돼 있었다** — 수정 불필요.

| 노드 | 항목 | 실측값 |
|---|---|---|
| `474:884`(State=Default 라벨) | fills[0].opacity | **0.5** (boundVariable `VariableID:95:9`) |
| `474:887`(State=Checked 라벨) | fills[0].opacity | **0.5** (boundVariable `VariableID:95:9`) |
| `474:891`(State=Focus 라벨) | fills[0].opacity | **0.5** (boundVariable `VariableID:95:9`) |
| `474:893`(State=Disabled Box) | fills[0].opacity / strokes[0].opacity | **0.5 / 0.5** (boundVariable `VariableID:95:10` / `VariableID:95:9`) |

원본 확정 프레임(`247:6666` 등)은 이번에도 손대지 않았다(읽기 전용 재조회 없음, 이미 0-17절에서 대조 완료된 값 재확인만).

### 0-19. TypeSelector 스펙 시트 `clipsContent` 회귀 수정 — Focus 링 잘림 정정 (2026-07-15)

**배경**: design-prompter 브리프가 지적한 대로, 0-15절에는 "TypeSelector/NeoInput/CornerInput/Sidebar Nav Item 스펙 시트 4개 전부의 Cell/Row/Grid 컨테이너에 `clipsContent=false`를 명시적으로 설정해 정정했다"고 기록돼 있었으나, 그 직후 검증 스크린샷 서술은 NeoInput/CornerInput 개별 Focus 셀만 언급하고 TypeSelector는 빠져 있었다 — 실제로 TypeSelector 스펙 시트만 정정이 누락됐거나 이후 재구성(0-16절의 NeoInput/CornerInput 재배치 등) 과정에서 회귀한 것으로 확인됐다.

**노드 ID 확인**: 브리프가 제시한 두 후보 ID(`343:1146`/`450:714`)는 둘 다 실존하며 서로 다른 계층을 가리킨다 — ID 불일치가 아니라 계층 관계였다. `343:1146`은 5절 컴포넌트 표와 정확히 일치하는 스펙 시트 루트 FRAME("Spec — TypeSelector", `Component Specs` 페이지 `342:2` 하위)이고, `450:714`는 그 안의 하위 "Grid" 컨테이너(VERTICAL auto-layout, 464×284)다.

**실측 결과(수정 전)**: `343:1146` 하위 전체를 순회한 결과, TypeSelector 컴포넌트 INSTANCE 12개 자체는 이미 `clipsContent:false`(정상 — 마스터 `257:28`의 effects가 그대로 노출되는 상태)였으나, 그 바깥을 감싸는 auto-layout 컨테이너 26개 — 루트 프레임(`343:1146`), Grid(`450:714`), HeaderRow(`450:715`), ColLabelCell 3개(`450:717`/`450:719`/`450:721`), Row 4개(`450:723`/`450:741`/`450:759`/`450:777`), RowLabel 4개(`450:724`/`450:742`/`450:760`/`450:778`), Cell 12개(`450:729`/`450:734`/`450:739`/`450:747`/`450:752`/`450:757`/`450:765`/`450:770`/`450:775`/`450:783`/`450:788`/`450:793`) — 는 전부 Figma auto-layout 기본값인 `clipsContent:true`로 남아 있어, State=Focus 열(Category별 3번째 칩) 칩의 ink 포커스 링(`DROP_SHADOW`, offset 0,0, blur 0, spread 3px, `#1a1a1a`)이 Cell 경계에서 잘리고 있었다.

**수정**: 위 26개 컨테이너 전부 `clipsContent`를 `false`로 설정. TypeSelector 마스터 컴포넌트(`257:28`)와 그 12개 variant 자체(effects 정의 포함)는 이번에도 전혀 건드리지 않았다 — NeoInput/CornerInput 스펙 시트(`344:721`/`344:740`)에 이미 정상 적용돼 있는 것과 동일한 방식(스펙 시트 컨테이너만 정정, 마스터는 무수정)을 그대로 따랐다.

**검증(자체 재대조, design-systems 규칙)**: `get_screenshot`으로 스펙 시트 전체(`343:1146`, 764×444)와 Category=Friend/State=Focus 셀(`450:739`, 100×55) 확대본을 각각 확인한 결과, 4개 카테고리(Friend/Family/Other/Company) State=Focus 열 칩 전부 ink 링이 셀 경계에 잘리지 않고 온전히 렌더링됨을 확인했다. 나머지 State=Unselected/Selected 열은 애초에 ink 링이 없어(그림자는 Focus에만 적용) 이번 수정으로 시각적 회귀가 없음을 함께 확인했다.

**원본 확정 8개 프레임(`248:11689` 하위)은 이번에도 열람하지 않았다** — TypeSelector Focus 상태 자체가 확정 프레임 밖의 인터랙션 상태 확장물(9절)이라 원본과 무관하다.

## 1. 변수 컬렉션 (최신, 확정 디자인 기준)

### 1-1. Primitives (`VariableCollectionId:95:5`, mode `Value`=`95:0`, scopes=[] 전부 — 피커에서 숨김)

**기존 브랜드 3색 재사용 확인**: `color/teal/500`(#17A398) `color/coral/500`(#FF5A76) `color/amber/500`(#FFCB47) — 이번 확정 디자인에서도 동일 hex로 실제 사용됨을 재확인, 신규 선언 없이 그대로 재사용.

**정정**: `color/ink/900` 값을 기존 `#1C1F21`에서 확정 디자인의 실측값 `#1a1a1a`로 정정(구조선·보더·하드 그림자·기본 텍스트에 실제 쓰인 값). `shadow/color/ink-8`/`ink-16`(소프트 그림자 전용, rgba(28,31,33,...))은 두 문서 모두 원문에 그 rgba를 그대로 명시하고 있어 손대지 않음 — 하드 보더/텍스트용 ink와 소프트 그림자용 ink는 이제 미세하게 다른 두 값이며 의도적으로 분리 유지.

**추가 정정(0-1절, design-qa 감사)**: `color/ink/800`(#1C1F21, alpha=1) 신규 원시값 추가 — Row Action Button(`260:95`) Neutral 보더 전용, `color/ink/900`(#1A1A1A)과 별개 값. 우연히 `shadow/color/ink-8`/`ink-16`의 rgb 성분과 같은 rgb(28,31,33)이지만 이 둘은 alpha가 달라(그림자는 반투명, 이건 alpha=1 하드 보더) 별도 primitive로 유지한다.

**신규 카테고리 색 원시값** (CatBadge 팔레트, main 테이블에서 실측):
- `color/blue/100`(#E0F0FF) `color/blue/500`(#4A90D9) `color/blue/900`(#1A4C88) — 친구
- `color/coral/100`(#FFE4E8) `color/coral/900`(#A8003B) — 가족 (보더는 기존 coral/500 재사용)
- `color/purple/100`(#EDE0FF) `color/purple/500`(#9B72CF) `color/purple/900`(#4B0D9C) — 기타
- `color/mint/100`(#D8FFF5) `color/teal/900`(#0A4F49) — 회사 (보더는 기존 teal/500 재사용)

**TypeSelector 전용 레거시 원시값** (편집 모달에서 실측, 0-9절에서 Selected 상태 재바인딩으로 대부분 미사용됨 — 아래 1-3절 참고):
`color/green/500`(#27AE60) `color/orange/100`(#FFF3E0) `color/orange/500`(#E6800A)

**TypeSelector 전용 추가 원시값(0-1절, design-qa 감사 후 정정)**: `color/gray/300`(#CCCCCC, 미선택 칩 보더 실측값) `color/orange/900`(#7A3D00, 회사 선택 텍스트 실측값, 0-9절에서 미사용으로 전환됨) — 기존 `color/gray/450`(#888, 텍스트용)·`color/orange/500`(#E6800A, 보더/닷용) 토큰과 혼동해 재사용되던 것을 분리.

**뮤트 텍스트 원시값** (main 테이블 실측 — 전화번호 #555/주소 #777/보조 라벨 #888):
`color/gray/450`(#888888) `color/gray/500`(#777777) `color/gray/650`(#555555)

**하드 그림자 전용**: `shadow/color/ink-solid`(#1a1a1a, alpha=1 — 기존 ink-8/ink-16과 별개, 블러 없는 순수 오프셋 그림자용) `shadow/offset/hard-1`(1) `shadow/offset/hard-2`(2) `shadow/offset/hard-6`(6) `shadow/blur/none`(0) — Elevation 컬렉션(`VariableCollectionId:114:4`, mode `114:0`)에 위치.

**Radius/Border 신규 스텝** (Spacing 컬렉션 `VariableCollectionId:95:25`, mode `95:2`): `radius/none`(0) `radius/6`(6) `radius/10`(10) `border/hairline`(1, scope STROKE_FLOAT) `border/base`(2, scope STROKE_FLOAT) `border/heavy`(3, scope STROKE_FLOAT).

**0-4절 신규**: Link 텍스트 링크는 신규 primitive가 필요 없었다 — 기존 `color/teal/500`을 그대로 재사용(아래 1-2절 참고).

**신규(0-5절, 2026-07-14)**: `color/beige/200`(#EDE6D8, scope=[] 숨김) — Contact Row(`351:299`) 행 구분선 전용 원시값, main 테이블 실측(`214:573` 하단 보더). 기존 primitive 전수 검색 결과 동일 hex가 없어 신규 등록.

**신규(0-10절, 2026-07-14)**: 없음 — Input Error 토큰은 기존 `color/coral/500`(#FF5A76)/`color/coral/900`(#A8003B) primitive를 그대로 alias만 했다(신규 원시값 불필요). NeoSelect Open도 신규 primitive 없음(기존 ink/white/Elevation-Raised 재사용).

**신규(9-6절, 2026-07-15)**: `color/gray/150`(#F1F1F1, scope=[] 숨김) — NeoSelect Open 옵션 hover 배경 전용, 기존 gray/50·gray/100 사이 신규 스텝.

**신규(0-12절, 2026-07-15)**: `color/gray/350`(#BBBBBB, scope=[] 숨김) — NeoInput placeholder 텍스트 전용, 기존 gray/300·gray/400 사이 신규 스텝.

### 1-2. Semantic Colors (`VariableCollectionId:95:16`, mode `95:1`)

카테고리 팔레트(CatBadge 정식 채택 — 2절 참고): `color/category/friend-bg/-border/-text` `color/category/family-bg/-border/-text` `color/category/other-bg/-border/-text` `color/category/company-bg/-border/-text` (각 bg=FRAME_FILL/SHAPE_FILL, border=STROKE_COLOR, text=TEXT_FILL). **0-9절 갱신**: 이 4쌍은 이제 CatBadge뿐 아니라 TypeSelector(`257:28`)의 Selected 상태 4종(Friend/Family/Other/Company)에도 직접 바인딩되는 공용 카테고리 색 토큰이다 — 두 컴포넌트가 같은 토큰을 공유한다.

뮤트 텍스트 역할: `color/text-muted-strong`(→gray/650 #555, 전화번호) `color/text-muted`(→gray/500 #777, 주소) `color/text-muted-subtle`(→gray/450 #888, 마이크로 라벨/TypeSelector 미선택 텍스트) — **⚠ WCAG 검증 결과, 아래 3절 대비 계산 참고: muted-strong만 PASS, muted/muted-subtle는 원본 확정 디자인에 이미 내재된 미달값(→7-1절에서 RESOLVED로 종결, 사용자 확정)**.

기타: `color/border-neutral`(→ink, 취소/로그아웃류 아웃라인 버튼 보더) `color/background-success`(→mint/100, 토스트 성공) `color/background-error`(→coral/100, 배너 에러).

**신규(0-4절, 2026-07-14)**: `color/text-link`(→teal/500 #17A398, scope TEXT_FILL, `VariableID:340:3`) — Link 컴포넌트/Body/Link 텍스트 스타일 전용. 기존 `color/text-accent`(teal/700 별칭, 레거시)와는 값이 달라 재사용하지 않고 신규로 만들었다.

**신규(0-5절, 2026-07-14)**: `color/border-divider-warm`(→beige/200 #EDE6D8, scope STROKE_COLOR, `VariableID:350:3`) — Contact Row(`351:299`) 행 하단 구분선 전용(strokeBottomWeight만 1, 나머지 3변 0).

**신규(0-10절, 2026-07-14)**: `color/border-error`(→coral/500 #FF5A76, scope STROKE_COLOR, `VariableID:378:2`), `color/text-error`(→coral/900 #A8003B, scope TEXT_FILL, `VariableID:378:3`) — NeoInput/CornerInput Error variant 전용.

**신규(0-11절, 2026-07-15 재확인)**: `color/text-placeholder`(→gray/300 #CCCCCC, scope TEXT_FILL, `VariableID:398:3`) — NeoInput/CornerInput/NeoSelect Placeholder 텍스트 공용(이미 등록돼 있던 것을 재확인). **0-12절 갱신**: NeoInput만 별도로 `color/text-placeholder-input`(→gray/350 #BBBBBB, scope TEXT_FILL, `VariableID:434:5`)로 분리됐다 — CornerInput/NeoSelect는 `color/text-placeholder`(#CCCCCC) 유지.

**신규(9-6절, 2026-07-15)**: `color/bg-hover-muted`(→gray/150 #F1F1F1, scope `FRAME_FILL`/`SHAPE_FILL`, `VariableID:432:3`) — NeoSelect Open 옵션 hover 배경 전용, 흰 배경류 컴포넌트의 옅은 hover 배경.

### 1-3. Component Tokens (`VariableCollectionId:97:2`, mode `97:0`)

기존 재사용(변경 없음): `component/button-bg-primary`(teal) `component/button-bg-danger`(coral) `component/button-bg-amber`(amber) — 이번 확정 디자인의 NeoBtn/Button Style=Teal/Coral/Amber에 그대로 재사용, 신규 선언 없음.

신규: `component/button-border-neutral`(→ink/900, NeoBtn/Button Neutral 스타일 2px 아웃라인 보더) `component/typeselector-unselected-text`(→gray/450 #888) `component/typeselector-family-selected-bg`(→green/500) `component/typeselector-company-selected-bg`(→orange/100) `component/typeselector-company-selected-accent`(→orange/500, 회사 선택 보더/닷 전용). **0-9절 갱신**: 이 중 `typeselector-family-selected-bg`/`company-selected-bg`/`-accent`와 구 `typeselector-company-selected-text`(1-3절 옛 버전) 4개는 0-9절 재바인딩으로 더 이상 어떤 노드에도 바인딩되지 않는다(orphan) — 삭제하지 않고 이 상태로 명시 보존한다.

**신규(0-1절, design-qa 감사 후 정정)**: `component/typeselector-unselected-border`(→gray/300 #CCCCCC, TypeSelector 미선택 칩 4개 + "기타/선택" 칩 보더 전용, scope STROKE_COLOR) `component/typeselector-company-selected-text`(→orange/900 #7A3D00, TypeSelector "회사/선택" 텍스트 전용, scope TEXT_FILL — **0-9절 갱신**: 이 토큰도 "회사/선택"이 `color/category/company-text`로 재바인딩되며 orphan 전환됨) `component/row-action-button-border-neutral`(→ink/800 #1C1F21, Row Action Button Neutral 보더 전용, scope STROKE_COLOR — `component/button-border-neutral`과는 별개 값·별개 컴포넌트).

### 1-4. Effect Styles

**하드 "스티커" 그림자(신규, neo-brutalist)** — 블러 없음, `drop-shadow(Npx Npx 0px ink)`, 색=`shadow/color/ink-solid`, offsetX=offsetY=해당 오프셋 변수, radius=`shadow/blur/none`, spread=`shadow/spread/none`:
- `Shadow/Hard-1` — count pill(비활성)
- `Shadow/Hard-2` — 주요 CTA 버튼(검색/전체/추가/로그인/가입하기/저장하기/삭제하기), 활성 사이드바 nav, 모달 닫기(X) 버튼
- `Shadow/Hard-6` — 모달 카드, 인증 카드(Join/login) 전체

**소프트 블러 그림자(기존 재사용)** — `Elevation/Raised`(color=ink-8, offsetY=2, blur=8, spread=0 = `0px 2px 8px rgba(28,31,33,0.08)`) — Toast(성공/에러 배너) 전용으로 실사용 시작. **0-10절 갱신**: NeoSelect Open 옵션 패널(드롭다운)에도 재사용. **하드/소프트를 반드시 별개 토큰으로 유지** — 하나로 합치지 않는다.

**Link/Body 텍스트 링크(0-4절)**: 그림자 없음(effects=[]) — 5-1절 "적용 안 됨" 목록과 일치.

**Contact Row(0-5절)**: 그림자 없음(row 아웃라인 버튼/CatBadge와 동일 계열, flat 요소) — 하단 구분선만 존재.

### 1-5. Text Styles (신규 11종, 확정 디자인 5단 위계 그대로 + Link)

`Wordmark/Logo`(Baloo 2 ExtraBold 22, tracking -0.55) `Heading/Page`(Noto Sans KR Black 18, tracking -0.4) `Heading/Modal`(Noto Sans KR Black 16, tracking 0) `Label/Micro`(Inter Black 9, tracking 1) `Label/CountNumber`(Inter Black 12) `Label/Badge`(Inter Semi Bold 11, tracking 0.0645) `Body/Button`(Noto Sans KR Bold 14 — **0-5절 재확인**: Contact Row 이름 텍스트에도 그대로 재사용, main `214:575` 실측과 hex/폰트/크기 전부 일치) `Body/Banner`(Noto Sans KR Medium 13) `Body/Regular`(Noto Sans KR Regular 14) `Body/Caption`(Noto Sans KR Regular 11) `Body/Link`(Noto Sans KR Bold 12, tracking 0, lineHeight 18px, underline — **신규, 0-4절**, 색상은 텍스트 스타일이 아니라 `color/text-link` 변수로 별도 바인딩).

세 폰트 패밀리(Baloo 2/Inter/Noto Sans KR) 역할 분리를 그대로 유지 — 텍스트 스타일 하나가 한 역할만 담당한다.

**참고**: Table Row Action("수정"/"삭제")의 10px 텍스트는 위 11종 텍스트 스타일 어디에도 해당하지 않는 컴포넌트 로컬 fontSize(직접 지정, 스타일 미바인딩)다 — 0-1절 정정으로 13px→10px 직접 수정.

## 2. TypeSelector vs CatBadge 색 불일치 — 결정 및 근거

**⚠ 0-9절 갱신(2026-07-14)으로 이 절의 원래 결정은 뒤집혔다.** 아래 본문은 과거 결정 당시의 근거 기록으로 보존한다. **현재 유효한 결정: TypeSelector의 Selected 상태 4종(친구/가족/기타/회사)은 CatBadge와 동일한 `color/category/*` 토큰을 직접 공유한다(1-2절 참고).** Unselected(미선택) 상태만 여전히 TypeSelector 전용 회색 토큰(`component/typeselector-unselected-*`)을 쓴다 — 이 부분은 0-9절 범위 밖이라 변경되지 않았다.

**과거 결정 기록(더 이상 유효하지 않음, 0-9절로 대체됨)**: CatBadge 팔레트를 이 시스템의 정식(canonical) 카테고리 색으로 채택하되, TypeSelector는 원본 확정 프레임에 실제로 존재하는 별도 팔레트를 그대로 재현해 `component/typeselector-*` 전용 컴포넌트 토큰으로 격리하고 CatBadge와 혼용하지 않는다는 결정이었다. 근거였던 내용: CatBadge는 main 목록 화면에서 4개 카테고리 전부 일관된 공식을 쓰는 반면, TypeSelector는 실측 결과 카테고리 정체성을 일관되게 반영하지 않았다(미선택 전부 회색, 선택 시 accent 로직 불명확). 원본 확정 프레임은 수정 금지 규칙에 따라 관찰값을 그대로 컴포넌트화했었다.

## 3. WCAG 대비 계산 (신규 값 전수 검증)

- CatBadge 4종: bg/text 조합 전부 "연한 배경+짙은 텍스트" 공식이라 7:1 이상 여유 있게 PASS(예: friend #1A4C88 on #E0F0FF).
- NeoBtn/Button Style=Amber/Teal/Coral + ink 텍스트: 기존 "브랜드색 배경 위 텍스트=ink 고정" 규칙 재사용, 기존 검증된 5.3~11:1 범위 그대로 PASS.
- NeoBtn/Button Style=Neutral(흰 배경+ink 텍스트): 21:1 PASS.
- Toast Success(#D8FFF5 bg)/Error(#FFE4E8 bg) + ink(#1a1a1a) 텍스트: 각각 15.8:1 / 14.5:1 PASS.
- **⚠ 뮤트 텍스트 3종 — 흰 배경 위 대비 직접 계산(WCAG 2.1 상대휘도 공식)**:
  - `color/text-muted-strong`(#555555): **7.45:1 PASS** (전화번호 텍스트, Contact Row `351:301`에도 동일 바인딩)
  - `color/text-muted`(#777777): **4.46:1 — AA 4.5:1 기준 근소하게 미달** (주소 텍스트, Contact Row `351:302`에도 동일 바인딩)
  - `color/text-muted-subtle`(#888888): **3.55:1 — AA 4.5:1 기준 미달** (마이크로 라벨/TypeSelector 미선택 텍스트)
  - **이 두 값은 사용자의 확정 원본 프레임에 이미 실측된 값이다. → RESOLVED(7-1절 참고)**: 사용자가 "이번 프로젝트에 한해 무시하고 원본 그대로 유지"하기로 명시적으로 확인·결정했다.
- **TypeSelector "회사/선택" 텍스트**(0-9절 갱신 — 이제 `color/category/company-text` #0A4F49) on 배경 `color/category/company-bg`(#D8FFF5): CatBadge 팔레트와 동일 공식(연한 배경+짙은 텍스트)이라 7:1 이상 PASS(CatBadge 회사 조합과 동일 프로파일).
- **`color/text-link`(#17A398, Body/Link) on 흰 배경**(0-4절 계산): **3.12:1 — AA 본문 텍스트 4.5:1 기준 미달**(12px Bold는 WCAG "큰 텍스트" 기준에도 못 미쳐 3:1 예외도 적용 불가). 원본 확정 실측값 그대로 → **RESOLVED**(사용자 확정, 7-1절 참고).
- **신규(0-10절)**: `color/border-error`(#FF5A76) on 흰색 배경 = **3.01:1** — WCAG 1.4.11 비텍스트(UI 컴포넌트 경계) 최소 3:1 기준 PASS(근소). `color/text-error`(#A8003B) on 흰색 배경 = **7.70:1** — 14px Regular 본문 텍스트 4.5:1 기준 PASS.
- **신규(0-12절)**: `color/text-placeholder-input`(#BBBBBB, NeoInput 전용) on 흰색 배경 — placeholder 텍스트는 원본 확정 프레임 실측값 그대로이며 7-1절 §5(placeholder 텍스트 대비 미달, RESOLVED)의 기존 결정 범위에 포함된다. 별도 신규 계산·보고 불필요.

## 4. Icons (`96:7`)

**기존 8종 유지**(변경 없음): `Icon/Search` `Icon/Add` `Icon/Edit` `Icon/Delete` `Icon/Category` `Icon/Logout` `Icon/Alert` `Icon/User` — 확정 디자인에서도 `Icon/Alert`(토스트/배너)와 `Icon/User`(아바타)가 그대로 재사용됨을 확인. **(2026-07-14 문서 동기화 재확인)** graphic-designer가 "Icons" 페이지를 직접 재실측(`use_figma`)한 결과 8종 전부 strokeWeight 3px 균일로 원상태 그대로다 — 상세는 `docs/design/graphic-assets.md` 참고.

**신규 11종** (`Pixel/*` 네임스페이스, 확정 프레임에서 비파괴적으로 clone 후 `createComponentFromNode`로 컴포넌트화 — 원본은 전혀 수정하지 않음): `Pixel/Star`(12px, 로고 심볼 내부) `Pixel/Search`(15px) `Pixel/Plus`(9px) `Pixel/Logout`(12px) `Pixel/Edit`(14px) `Pixel/Delete`(14px) `Pixel/Close`(10px, 모달 닫기) `Pixel/Warning`(16px, 삭제 경고) `Pixel/NoResult`(40x44, 빈 검색결과 그래픽) `Pixel/Eye`(14x10, login 비밀번호 표시/숨김 토글) `Pixel/EyeOff`(**신규, 0-13절, 2026-07-15**, 14x10, `Pixel/Eye`와 짝을 이루는 "닫힌 눈" 실루엣, `415:892`).

## 5. 컴포넌트 (확정 디자인 기준, 신규 등록)

**스펙 시트 안내(0-4/0-5절)**: 아래 표의 컴포넌트 11개(NeoBtn~CornerInput 9개 + Link + Contact Row) 전부 `"Component Specs"` 페이지(`342:2`, FOUNDATIONS 구역, Icons 바로 뒤)에 제목+설명+전체 variant 그리드+상태별 라벨을 갖춘 스펙 시트 프레임이 있다.

| 컴포넌트 | 페이지 | ComponentSet ID | Variant | 스펙 시트 프레임 ID |
|---|---|---|---|---|
| CatBadge | Badge `102:3` | `256:17` | Category=Friend/Family/Other/Company (4). CatBadge 팔레트(2절) 바인딩. | (스펙 시트 없음) |
| TypeSelector | Badge `102:3` | `257:28` | Category(4) × State=Selected/Unselected/Focus(3) = **12 variant**(**0-15절, 2026-07-15**, 기존 16 variant에서 Focus 축을 State 열거형 값으로 소급 통합 — Selected+Focus=Yes 4개 삭제, Unselected+Focus=Yes 4개는 State=Focus로 이름만 정리). **0-9절**: Selected는 CatBadge 토큰 공유(2절 참고), Unselected/Focus는 전용 회색 토큰 유지. **0-19절**: 스펙 시트 `clipsContent` 회귀 정정(Focus 링 잘림 수정). | `343:1146` |
| Count Pill | Sidebar Nav Item `103:92` | `258:16` | State=Active(흰 배경, 그림자 없음)/Inactive(앰버 배경, Shadow/Hard-1). | (스펙 시트 없음) |
| Sidebar Nav Item | Sidebar Nav Item `103:92` | `258:29` | State=Active/Inactive/Focus = **3 variant**(**0-15절, 2026-07-15**, 기존 4 variant에서 Focus 축을 State 열거형 값으로 소급 통합 — Active+Focus=Yes 1개 삭제). **9-5절**: Focus(구 Inactive+Focus=Yes, `287:17`)는 3px ink OUTSIDE 스트로크로 링 구현, fills/strokes/effects 무수정 유지. | `343:1106` |
| **Checkbox**(0-17절, 신규) | Checkbox(신규 페이지, `474:881`) | `474:899`(555×18) | State=Default(Unchecked)/Checked/Focus/Disabled = 4 variant. 로그인(`247:6666`) "☐ 로그인 상태 유지"(`247:6822`) 실측 기반, 14×14 Box(흰배경+2px ink 보더)+Label(`color/ink/900` opacity 0.5). TEXT 프로퍼티 `label`(기본값 "로그인 상태 유지"). 신규 토큰 없음(기존 재사용). | `475:762` |
| NeoBtn | Button `97:8` | `259:126` | Style=Amber/Teal/Coral/Neutral × Size=Default/Compact × State=Default/Hover/Press/Focus/Disabled/Loading(9-2절) = 48. | `342:3` |
| Button | Button `97:8` | `259:609` | Style=Amber/Coral/Neutral × State=Default/Hover/Press/Focus/Disabled/Loading(9-2절) = 18. **0-4절**: login/Join 보조 버튼도 Neutral variant로 커버. | `343:50` |
| Icon Button | Button `97:8` | `259:613` | Type=Close × State=Default/Hover/Press/Focus/Disabled(9-2절, Loading 제외) = 5. | `343:653` |
| Row Action Button | Table Row `103:3` | `260:95` | Style=Neutral/Danger × State=Default/Hover/Press/Focus/Disabled(9-2절, Loading 제외) = 10. **0-1절**: Neutral 보더=`component/row-action-button-border-neutral`(#1C1F21). | `343:697` |
| Table Row Action | Table Row `103:3` | `260:100` | Style=Neutral/Danger × State=Default/Hover/Press/Focus/Disabled(9-2절, Loading 제외) = 10. **0-1절**: 텍스트 10px 정정. | `343:1044` |
| **Contact Row**(0-5절) | Table Row `103:3` | `351:299`(단일) | 단일. 이름/전화번호/주소/CatBadge/Table Row Action 조합, 774×47. TEXT 프로퍼티 `name`/`phone`/`address`. | `352:726` |
| NeoInput | Input `100:2` | `288:12` | Content=Filled/Placeholder × Error=No/Yes(4, State=Default) + State=Focus 2개(Content=Placeholder×Error=No 기반 1개, Content=Filled×Error=Yes 기반 1개) = **6 variant**(**0-15/0-16절, 2026-07-15**, Focus 축을 State 열거형 값으로 소급 통합 — Filled×Focus=Yes 2개 삭제 후 Error=Yes 조합만 복원). Placeholder 텍스트=`color/text-placeholder-input`(#BBBBBB, NeoInput 전용, 0-12절). | `344:721` |
| CornerInput | Input `100:2` | `288:27` | Content=Filled/Placeholder × Error=No/Yes(4, State=Default) + State=Focus 2개(Content=Placeholder×Error=No 기반 1개, Content=Filled×Error=Yes 기반 1개) = **6 variant**(**0-15/0-16절, 2026-07-15**, 동일 패턴). **0-3절**: 모서리 CornerBracket 제거, 순수 2px ink 보더. Placeholder 텍스트=`color/text-placeholder`(#CCCCCC). 베이스 폭 392px. | `344:740` |
| NeoSelect | Select `101:3` | `387:13`(**0-10절 갱신**, 구 `261:660`) | State=Default/Open(**0-10절**, 트리거 동일 룩+옵션 패널 `Elevation/Raised`) × Content=Placeholder/Selected(**0-11절**, 4 variant). Placeholder 문구 "종류선택". **9-6절**: Open 옵션 hover 배경=`color/bg-hover-muted`(#F1F1F1), 패널 전체 폭 채움(인셋 없음, PASS 확인). | `388:746` |
| Card | **Card**(신규 페이지) | `262:15` | Type=Modal/Auth = 2. 2px ink 보더+radius8+Shadow/Hard-6. | (스펙 시트 없음) |
| Toast | Alert `104:2` | `263:53` | Type=Success/Error = 2. `Elevation/Raised`. 플로팅 오버레이 패턴(6절). | (스펙 시트 없음) |
| Logo | **Logo**(신규 페이지) | `263:692` | Background=Teal/White = 2. | (스펙 시트 없음) |
| Avatar | Avatar `104:127` | `104:131`(기존 재사용) | 변경 없음. | (스펙 시트 없음) |
| Link(0-4절) | Link(신규 페이지, `341:2`) | `341:3`(단일) | Default 단일(69×18). Body/Link + `color/text-link`. **(2026-07-15)** 텍스트 "비밀번호 재설정"으로 사용자 직접 변경 완료. | `344:759` |
| **Pixel/EyeOff**(0-13절, 신규) | Icons `96:7` | `415:892`(단일 컴포넌트) | 단일. `Pixel/Eye`와 짝, "닫힌 눈" 실루엣, 14×10. | (스펙 시트 없음 — Icons 페이지 자체가 카탈로그) |

## 6. 알림/토스트 오버레이 — 컴포넌트 설명에 명시된 배치 규칙

`Toast`(Type=Success/Error) 컴포넌트 설명에 "플로팅 오버레이" 성격을 명시했다: main-알림창/login-알림창은 각각 main/login 화면 위에 최상위 z-index로 절대 위치(absolute)로 뜨며 하단 콘텐츠를 밀어내지 않는다(레이아웃 버그 아님, 사용자 확정 의도). ui-designer가 화면에 조립할 때 이 배치 방식을 그대로 유지해야 한다. 자동 소멸 타이밍/애니메이션은 interaction-designer·motion-designer 몫이며 이 컴포넌트는 정적 배치·스타일까지만 규정한다.

## 7. 알려진 갭 / 후속 필요 사항

### 7-1. 종결된 결정 (RESOLVED) — 사용자 확정, 이번 프로젝트 범위에서 개선하지 않음

design-qa 감사에서 발견되어 이전에는 이 절에 열린 이슈(TODO)로 기록되어 있었으나, 사용자가 아래 6건을 **"이번 프로젝트에 한해 무시하고 원본 그대로 유지"**하기로 명시적으로 결정했다. 원본 확정 프레임(8개, `248:11689` 하위)은 이 결정 과정에서도 전혀 손대지 않았다.

1. **뮤트 텍스트 WCAG 대비 미달 2건**(3절 참고) — `color/text-muted`(#777777, 4.46:1, 주소 텍스트), `color/text-muted-subtle`(#888888, 3.55:1, 마이크로 라벨/TypeSelector 미선택 텍스트). AA 4.5:1 기준 미달. **사용자 확인 후 이번 프로젝트 범위에서 개선하지 않기로 결정.**
2. **사이드바 비활성 nav 텍스트 대비 미달**, **사이드바 라벨 대비 미달**. **개선하지 않기로 결정.**
3. **Table Row Action(`260:100`) 텍스트 대비 미달**(수정/삭제 라벨). **개선하지 않기로 결정.** (9-5절: Disabled variant의 텍스트 대비도 이 미해결 기준선을 그대로 승계함.)
4. **터치 타겟 44×44px 미달 다수** — Row Action Button(`260:95`), Table Row Action(`260:100`), 헤더 로그아웃 NeoBtn, 검색/전체 NeoBtn, 사이드바 nav, TypeSelector 칩(`257:28`). **개선하지 않기로 결정.** (7-2절: Link의 터치 타겟 미달도 이 §4와 같은 계열.)
5. **placeholder 텍스트 대비 미달**. **개선하지 않기로 결정** — 0-12절에서 NeoInput/CornerInput/NeoSelect 각각의 확정 실측 hex(#BBBBBB/#CCCCCC)를 정확히 반영했으나, 대비 자체를 개선하는 결정은 아니다(원본 그대로 유지 원칙 계승).
6. **`color/text-link`(Body/Link) WCAG 대비 미달**(0-5절에서 TODO→RESOLVED 이동) — #17A398 on 흰 배경, 3.12:1. **개선하지 않기로 결정.**

### 7-2. 열린 이슈 (TODO, 미해결 — 위 6건과는 별개)

- **TypeSelector 친구/기타 선택 상태 accent 미관찰** — 0-9절로 CatBadge 토큰 공유가 확정되며 사실상 해소됐다(친구/기타 모두 이제 CatBadge 색을 그대로 쓴다). 원본에서 실제로 다르게 디자인되어 있었다면 재확인 필요하나, 현재는 CatBadge 통일 결정이 우선한다.
- **Card 컴포넌트는 쉘까지만** — 실제 필드/버튼 조합은 ui-designer가 SCREENS 단계에서 조립한다.
- **Table Header, EmptyState 조립체는 컴포넌트화하지 않음** — 화면 레이아웃 조립의 영역이라 판단해 범위에서 제외.
- ~~**Button Disabled variant 없음**~~ — **RESOLVED**(9절 참고).
- ~~**Legacy Table Row(`103:7`) 컴포넌트 해제**~~ — **RESOLVED**(0-6/0-7절 참고, 해제+복구 완료).
- **신규(0-4절): Link 컴포넌트는 Default 상태만 등록** — hover 인터랙션은 범위 밖. 필요 시 interaction-designer가 후속 추가.
- **신규(0-5절): Link(`341:3`, 69×18) 44×44px 터치 타겟 미달** — LOW, 원본 그대로. 7-1절 §4와 같은 계열.
- **신규(0-7절): 파일럿 6개 데이터 행의 연락처 데이터는 원본이 아닌 대체 예시값** — 상세는 0-7절.
- **신규(0-10절): NeoSelect의 Focus/Disabled/Error 상태 미확장** — 이번 승인 범위는 Open만이었다. 필요 시 후속 라운드에서 NeoInput/CornerInput과 동일한 패턴으로 확장 검토.
- **신규(0-10절): NeoInput/CornerInput의 Disabled 상태 미확장** — Placeholder/Error/Focus 축은 완료됐으나 Disabled는 아직 없다.
- ~~**⚠ 신규(2026-07-15, 문서 복구 메모)**: 이 세션의 문서 손상·복구 사고로 2/3/5/7-2절 일부가 design-pl의 재구성에 의존한다~~ — **RESOLVED(0-14절)**: FOUNDATIONS 4개 페이지 소급 동기화 라운드에서 1~5절 표를 Figma 라이브 상태와 재대조 완료, 불일치 없음 확인.
- ~~**신규(0-15절): TypeSelector/NeoInput/CornerInput/Sidebar Nav Item의 Focus=No/Yes 직교 축**~~ — **RESOLVED(0-15절, 2026-07-15)**: 9-2절과 동일한 State-열거형 단일값 패턴으로 소급 통합 완료(TypeSelector 12, NeoInput/CornerInput 각 6[0-16절 Focus×Error 복원 포함], Sidebar Nav Item 3 variant).
- **신규(0-17절): 라디오 버튼/Divider 컴포넌트 미등록** — 확정 프레임 전수 검색 결과 실물 0건, 화면정의서에도 별도 필요 흐름 없어 등록하지 않기로 판단(근거는 0-17절 2/3항 참고). 실제로 필요한 흐름이 생기면 재검토.
- **신규(2026-07-15, 두 번째 문서 손상 사고)**: `docs/design/design-system.md`가 세션 중 재차 손상(697→372줄, 섹션 1~11 및 12절 전체 소실)됐다가 git HEAD(commit `4a0db785`/`4cdcbc9`)+세션 중 확보해둔 각 라운드 diff 기록을 근거로 전체 재구성해 복구했다 — 상세 경위는 이 문서 최상단 복구 메모 참고. 원인은 design-systems.md에 이미 명문화된 "Write 전체 덮어쓰기 금지" 규칙이 있었음에도 재발했다는 점이라, design-pl/design-systems 운영 절차 자체(커밋 타이밍, 백그라운드 라운드 사이 git 커밋 주기)를 재점검할 필요가 있다.
- ~~**신규(design-prompter 브리프): TypeSelector 스펙 시트 `clipsContent` 회귀**~~ — **RESOLVED(0-19절, 2026-07-15)**: 26개 auto-layout 컨테이너를 `clipsContent=false`로 정정, Focus 링 잘림 없이 렌더링 확인.

## 8. Legacy — B-2 파일럿 기반 컴포넌트 (참고용, 더 이상 정식 소스 아님)

아래는 이전 B-2 파일럿 라운드에서 추출한 컴포넌트 인벤토리다. `docs/design/confirmed/user-confirmed-final-design.md`에 따라 8개 사용자 확정 프레임이 이를 완전히 대체했으므로 **더 이상 정식 소스가 아니다**. 삭제하지 않고 이력으로 보존하며, 이름이 겹쳤던 3개(`Button`/`Row Action Button`/`Sidebar Nav Item`)에 이어 나머지 5개(`Input`/`Select`/`Badge`/`Table Row`/`Alert`)도 `[Legacy B-2] ` 접두사로 리네임해 위 5절의 신규 컴포넌트와 구분했다. Avatar(`104:131`)만 확정 디자인과 완전히 일치해 현재도 유효하므로 접두사 없이 그대로 둔다.

**(갱신, 0-3절) 컴포넌트 등록 해제(폐기) 진행**: 사용자 요청으로 Avatar를 제외한 8개를 컴포넌트 등록 해제 대상으로 검토했다. 인스턴스가 없는 7개는 COMPONENT/COMPONENT_SET → FRAME으로 전환 완료. Table Row는 인스턴스 7개가 남아 있어 해제하지 않고 보류했다가, **(0-5절) 해제 위험성을 격리 테스트로 검증** 후 **(0-6절) 사용자 재확정으로 최종 해제 완료**(FRAME `357:303`) — 인스턴스 7개가 예상대로 빈 박스로 깨졌으나 **(0-7절) 마스터 콘텐츠 기반으로 전부 시각적으로 복구 완료**. 이제 Avatar를 제외한 8개 전부 컴포넌트 등록 해제(폐기) 완료 상태다.

### 페이지 순서 (전체 파일, 0-8절 재정렬 완료 — 2026-07-14 최신 기준)

**이번 라운드(0-8절)에서 페이지(canvas) 레벨 구조를 확정했다** — `docs/harness/design-team/figma-file-organization.md` 1번 항목의 구역 구분 스타일을 실제 Figma 파일 페이지 목록에 그대로 반영해, 구역 경계마다 빈 구분용 페이지를 만들고 전체 29개 페이지 순서를 아래 표대로 재배열했다.

| idx | pageId | name | 비고 |
|---|---|---|---|
| 0 | `15:2` | 레퍼런스 | |
| 1 | `364:2` | **--- BRAND ---** | 신규 구분 페이지(0-8절), 빈 페이지 |
| 2 | `52:2` | Brand Guide | |
| 3 | `364:3` | **--- FOUNDATIONS ---** | 신규 구분 페이지(0-8절), 빈 페이지 |
| 4 | `95:2` | Colors | |
| 5 | `95:3` | Typography | |
| 6 | `95:4` | Spacing | |
| 7 | `116:5` | Elevation | |
| 8 | `96:7` | Icons | |
| 9 | `364:4` | **--- COMPONENT SPECS ---** | 신규 구분 페이지(0-8절), 빈 페이지 |
| 10 | `342:2` | Component Specs | |
| 11 | `364:5` | **--- CONCEPTS ---** | 신규 구분 페이지(0-8절), 빈 페이지 |
| 12 | `34:2` | 브랜드 컨셉 Concepts | |
| 13 | `364:6` | **--- COMPONENTS ---** | 신규 구분 페이지(0-8절), 빈 페이지 |
| 14 | `97:8` | Button | |
| 15 | `100:2` | Input | |
| 16 | `101:3` | Select | |
| 17 | `102:3` | Badge | |
| 18 | `103:3` | Table Row | |
| 19 | `103:92` | Sidebar Nav Item | |
| 20 | `104:2` | Alert | |
| 21 | `104:127` | Avatar | |
| 22 | `262:5` | Card | |
| 23 | `263:665` | Logo | |
| 24 | `341:2` | Link | |
| 25 | `364:7` | **--- SCREENS ---** | 신규 구분 페이지(0-8절), 빈 페이지 |
| 26 | `222:524` | 파일럿 | 내부 콘텐츠 무수정, 위치만 이동 |
| 27 | `242:2330` | old-사용하지말것 | 구분자 없음, 맨 끝 |
| 28 | `15:3` | `UI-design ` | 빈 페이지, 구분자 없음, 맨 끝. 실제 이름 끝에 트레일링 스페이스 1칸 포함. |

**아직 만들지 않은 구분 페이지**: `--- GRAPHIC ASSETS ---`(Graphic Assets 페이지는 사용자가 삭제해 현재 존재하지 않음), `--- MOTION ASSETS ---`, `--- MARKETING ---`.

### Legacy 변수 컬렉션 요약

- **Primitives**: `color/teal/500` `color/coral/500` `color/amber/500` `color/ink/900`(1절에서 값 정정됨) `color/gray/0,50,100,200,400,600` `color/mint/tint` `color/border-hairline-value` `shadow/color/ink-8,ink-16` `color/teal/700`
- **Semantic Colors**: `color/background` `color/surface` `color/text-primary` `color/text-secondary` `color/border` `color/success` `color/error` `color/warning` `color/background-info` `color/border-ink` `color/text-accent` `color/border-hairline` `color/text-inverse`
- **Spacing**: `spacing/1,1-75,2,2-25,2-5,3,4,6,8` `radius/sm,xs,md,lg,full`
- **Elevation(legacy)**: `shadow/blur/sm,lg` `shadow/offset-y/sm,lg` `shadow/spread/none`, Effect Styles `Elevation/Raised` `Elevation/Overlay`(미바인딩)
- **Component Tokens(legacy)**: `component/button-bg-primary,secondary,border-secondary,bg-disabled,text-disabled,bg-danger,bg-amber` `component/select-border-open` `component/badge-bg-tag` `component/table-row-border` `component/navitem-bg-active` `component/avatar-bg`

### Legacy 컴포넌트 (`[Legacy B-2]` 리네임됨)

| 컴포넌트 | 페이지 | ID | 비고 | 상태 |
|---|---|---|---|---|
| [Legacy B-2] Button | `97:8` | `97:47` | Style×Content×State×Size = 32 | **폐기 완료** — FRAME `314:843` |
| [Legacy B-2] Input | `100:2` | `100:46` | State×Size = 4 | **폐기 완료** — FRAME `314:879` |
| [Legacy B-2] Select | `101:3` | `101:64` | State = 3 | **폐기 완료** — FRAME `314:893` |
| [Legacy B-2] Badge | `102:3` | `102:65` | Type×State = 4 | **폐기 완료** — FRAME `314:897` |
| [Legacy B-2] Table Row | `103:3` | `103:7` | variant 없음 | **폐기+인스턴스 복구 완료**(0-6/0-7절) — FRAME `357:303`, 인스턴스 7개 시각 복원(`360:297`, `361:85`/`361:92`/`361:99`/`361:106`/`361:113`/`361:120`) |
| [Legacy B-2] Row Action Button | `103:3` | `166:421` | Style = 2 | **폐기 완료** — FRAME `314:319` |
| [Legacy B-2] Sidebar Nav Item | `103:92` | `103:106` | State = 2 | **폐기 완료** — FRAME `314:876` |
| [Legacy B-2] Alert | `104:2` | `104:108` | Type = 2 | **폐기 완료** — FRAME `314:902` |
| Avatar | `104:127` | `104:131` | 확정 디자인에서도 재사용 — 유일한 예외, 접두사 없음 | 대상 아님 |

### Legacy 알려진 갭 (미해결 상태 그대로 이월)

- Button Disabled variant 6종 WCAG 대비 미달 — legacy 한정, 신규 Button/NeoBtn에는 Disabled variant 없음. 봉인됨(FRAME 전환).
- Heading/Label 텍스트 스타일 토큰, Table Header 컴포넌트 없음 — 미해결.
- radius/lg(12) 불일치 — `radius/10` 신규 추가로 해소.
- 화면상 버튼 색 스왑 문제 — legacy 파일럿 화면 한정, 확정 디자인에는 해당 없음.
- Table Row 인스턴스 깨짐 — **해소됨**(0-7절, 마스터 기반 시각 복구, 데이터는 대체 예시값 한계 있음).

## 9. 인터랙션 상태 (Hover/Press/Focus/Disabled/Loading) — interaction-designer 추가 (2026-07-14)

이 절은 interaction-designer가 추가한 상태·트리거 정의다. 8개 사용자 확정 프레임은 정적 스크린샷이라 이 상태들이 원본에 없다 — 아래 값은 브랜드 톤(1-4절 하드 스티커 그림자, ink 보더, teal/coral/amber 팔레트)을 확장해 새로 설계한 것이며, 원본 프레임(`248:11689` 하위 8개)은 이번에도 전혀 수정하지 않았다.

### 9-1. 공통 규칙 (모든 컴포넌트에 동일 적용)

- **State 속성**: 각 컴포넌트 세트에 기존 Style/Size/Category 등 속성은 그대로 두고, 새 변형 속성 `State`(값: Default/Hover/Press/Focus/Disabled/[Loading])를 추가했다.
- **Hover** — 배경을 ink(#1A1A1A) 쪽으로 소폭 블렌드(`mix(base, ink, t) = base + (ink-base)×t`). 브랜드색 배경은 t=12%, 흰 배경+아웃라인류는 t=6%.
- **Press** — Hover보다 진하게 블렌드(브랜드색 t=24%, 흰 배경류 t=12%) + 하드 그림자 완전 제거(`effects=[]`).
- **Focus** — **(2026-07-15 개정)** 2겹 `DROP_SHADOW` 스택(보더와 색이 같은 컴포넌트에서 단일 링이 안 보이는 문제 해결): 바깥쪽 ink 링(offset 0,0, blur 0, spread **4px**, `#1A1A1A` alpha 1) + 안쪽 흰 갭(offset 0,0, blur 0, spread **1px**, `#FFFFFF` alpha 1, effects 배열에서 ink 뒤에 위치해 안쪽을 덮음) — 밴드 폭(ink만 보이는 영역) 3px. NeoBtn/Button 전 Style에서 스크린샷 검증 완료(검은 보더 Neutral 포함). **배경/보더/텍스트는 Default와 완전히 동일해야 하며(Focus 순수성), 차이는 이 2겹 그림자뿐이다 — 12-1절에서 이 원칙 위반 1건을 정정했다.** **예외 1건(9-5절)**: Sidebar Nav Item Inactive+Focus=Yes는 3px ink OUTSIDE 스트로크로 대체.
  - **장식 효과 제거 조항(2026-07-15, 사용자 지적으로 확정)**: Focus variant의 effects 배열에는 위 2겹 링 스택만 남긴다 — Default/Hover 등에 있던 하드 스티커 그림자(offset 있는 장식용 `DROP_SHADOW`, 예: `Shadow/Hard-1`/`Hard-2`류) 같은 기존 장식 효과는 Focus에서 전부 제거한다. 대각선으로 삐져나온 비대칭 장식 그림자가 좌우대칭 링과 뒤섞이면 지저분해 보이기 때문이다(실제 사고 사례: Button Amber Focus에 하드 스티커 그림자가 링과 함께 남아 있었음, 사용자가 스크린샷으로 발견해 정정 요청). 갭도 애초 3px 시도에서 사용자 요청으로 1px로 좁혔다 — 원 버튼 보더에 바짝 붙게.

**Focus 2겹 링 적용 확인(2026-07-15)**: 버튼류 5개 컴포넌트(NeoBtn `259:126` 8 + Button `259:609` 3 + Icon Button `259:613` 1 + Row Action Button `260:95` 2 + Table Row Action `260:100` 2 = 총 16 variant) 전부 위 2겹 공식(흰 1px+ink 4px, 장식 효과 없음)으로 재확인 완료 — `use_figma` 읽기 전용 스크립트로 16개 variant의 effects 배열을 전수 재조회해 정확히 일치함을 확인했다(9-2절 표 참고).
- **Disabled** — **(9-5절에서 정정됨)** 컨테이너 opacity=1 유지, 배경 fill/보더 stroke 페인트 opacity만 0.5, 텍스트·아이콘 자식 opacity 0.85.
- **Loading**(NeoBtn·Button만 해당) — `opacity=0.7` + 그림자 제거. 스피너 애니메이션은 motion-designer 담당.

### 9-2. 버튼류 5개 컴포넌트 — Hover/Press/Focus/Disabled(+Loading) 적용 현황

| 컴포넌트 | ComponentSet ID | 기존 축 | 추가 축 | 추가된 State | Loading 포함 여부 |
|---|---|---|---|---|---|
| NeoBtn | `259:126` | Style(4)×Size(2) | State | Hover/Press/Focus/Disabled/Loading | **O** |
| Button | `259:609` | Style(3) | State | Hover/Press/Focus/Disabled/Loading | **O** |
| Icon Button | `259:613` | Type(1) | State | Hover/Press/Focus/Disabled | X |
| Row Action Button | `260:95` | Style(2) | State | Hover/Press/Focus/Disabled | X |
| Table Row Action | `260:100` | Style(2) | State | Hover/Press/Focus/Disabled | X |

**Hover/Press 블렌드 비율 상세**:
- NeoBtn/Button 브랜드색: Hover 12% / Press 24%, ink로 블렌드.
- NeoBtn/Button/Icon Button Neutral: Hover 6% / Press 12%, ink로 블렌드.
- Row Action Button: 자기 보더색(Neutral=ink/800, Danger=coral) 쪽으로 Hover 10% / Press 20%.
- Table Row Action: 자기 보더/텍스트색 쪽으로 Hover 12% / Press 24%.

### 9-3. Focus 상태만 추가한 보조 컴포넌트 (필요 판단, 2026-07-14) — ⚠ 과거 기록, 아래 참고

**⚠ 2026-07-15, 0-15절 갱신**: 이 4개 컴포넌트(Sidebar Nav Item/TypeSelector/NeoInput/CornerInput)는 9-2절과 동일한 State-열거형 단일값 패턴으로 소급 통합됐다 — 아래 표는 통합 이전 상태의 **과거 기록**으로 보존한다(삭제하지 않음). 현재 유효한 variant 구조는 5절 컴포넌트 표와 0-15/0-16절을 참고할 것 — TypeSelector 12(Category×State=Selected/Unselected/Focus), NeoInput/CornerInput 각 6(Content×Error 4 + State=Focus 2), Sidebar Nav Item 3(State=Active/Inactive/Focus).

| 컴포넌트 | ComponentSet ID | 기존 축 | 추가 축 | 비고 |
|---|---|---|---|---|
| Sidebar Nav Item | `258:29` | State=Active/Inactive | Focus=No/Yes | 총 4 variant. **9-5절**: Inactive+Focus=Yes(`287:17`)만 스트로크 기법. |
| TypeSelector | `257:28` | Category(4)×State=Selected/Unselected | Focus=No/Yes | 총 16 variant. |
| NeoInput | `288:12`(신규 ComponentSet, 기존 `261:10`은 그 안의 `Focus=No` 변형으로 그대로 보존) | 단일 컴포넌트 | Focus=No/Yes | `figma.combineAsVariants`로 승격. 기존 인스턴스 노드 ID(`261:10`) 유지. **(0-10절 갱신)** Error=No/Yes 축이 추가돼 현재 4 variant. **(0-11/0-12절 갱신)** Content=Placeholder/Filled 축까지 추가돼 실사용 매트릭스 7 variant. |
| CornerInput | `288:27`(신규 ComponentSet, 기존 `261:12`은 `Focus=No`) | 단일 컴포넌트 | Focus=No/Yes | 원본 `261:12` 보존. **0-3절 정정**: CornerBracket 장식 제거. **(0-10절 갱신)** Error=No/Yes 축 추가, 4 variant. **(0-11절 갱신)** Content=Placeholder/Filled 축 추가, 실사용 매트릭스 7 variant. |

**Hover/Press/Disabled를 제외한 이유**: Sidebar Nav Item·TypeSelector는 색상 자체가 선택 신호라 hover 시 혼동 위험. NeoInput/CornerInput은 focus가 우선순위가 높아 먼저 처리했다(**0-10/0-11/0-12절에서 Error/Placeholder 축 추가로 보완**).

### 9-4. 알려진 갭 (후속 필요)

- Sidebar Nav Item/TypeSelector의 Hover/Press/Disabled 상태는 다루지 않았다. **NeoInput/CornerInput의 Disabled 상태와 NeoSelect의 Focus/Disabled/Error 상태도 마찬가지로 미해결**(0-10절/7-2절 참고).
- Loading 상태의 실제 스피너 애니메이션은 motion-designer 담당 — 정적 컨테이너 톤까지만 정의.
- 포커스 링(2026-07-15 개정: 흰 갭 spread 1px + ink spread 4px 2겹)은 컴포넌트 로컬 raw 값 — design-systems가 필요 시 `component/focus-ring-*` 토큰으로 승격 검토 가능.
- Disabled opacity(0.5/0.85)도 로컬 raw 값 — `component/disabled-*` 토큰 승격 검토 가능.
- Table Row Action Disabled 텍스트 대비는 7-1절 §3의 기존 수용된 미달을 승계.
- 화면 간 전환 애니메이션은 다음 라운드 대상.

### 9-5. design-qa 감사 후 정정 (2026-07-14 추가 라운드, 원본 8개 프레임은 이번에도 무수정)

design-qa가 인터랙션 상태 라운드(9절)에서 두 건의 HIGH 결함을 발견해 정정했다.

**결함 1 — Sidebar Nav Item Inactive+Focus=Yes(`287:17`) 포커스 링 미렌더링**

- **증상**: `287:17`이 Focus=No 변형과 동일한 173×40으로 렌더링(정상 179×46), 포커스 링이 보이지 않았다.
- **근본 원인**: `287:17`은 Inactive 상태 스펙대로 `fills=[]`(완전 투명). Figma의 DROP_SHADOW는 프레임 자신의 불투명 실루엣 기준으로 계산되므로 fills가 비어 있으면 렌더링되지 않는다.
- **1차 시도(기각)**: opacity 0.02 흰색 SOLID fill 추가 — 바운딩박스는 맞았지만 시각적으로 완전히 잘못됨(잉크색 그림자가 가려지지 않고 블록 전체가 까맣게 렌더링).
- **최종 정정**: ghost fill/DROP_SHADOW 제거, 3px ink `strokeAlign=OUTSIDE` 스트로크로 대체 — 배경이 완전 투명해도 동일한 시각 결과를 재현.
- **재검증**: 바운딩박스 179×46 일치, 인라인 렌더로 시각 결과 확인. 4-variant 세트 전체 일관된 톤 확인.
- **범위**: `287:17` 1건에만 적용. 나머지 8쌍은 불투명 전경이라 기존 DROP_SHADOW 기법 유지.

**결함 2 — Disabled 상태(균일 opacity=0.45)가 WCAG 최소 대비 미달**

- **증상**: 5개 컴포넌트 Disabled variant(16개)에 균일 opacity=0.45 적용 결과 최유리 조합도 2.89:1, 최불리 조합 1.73~1.76:1로 AA 기준(4.5:1/3:1) 전부 미달.
- **검토한 두 옵션과 선택**: 순수 opacity 상향(α≈0.72 이상 필요)은 Amber+ink가 5.59:1까지 진해져 "비활성으로 안 보이는" 문제 발생 — 기각. **배경/텍스트 분리** 채택: 컨테이너 opacity=1, 배경 fill/보더 stroke 페인트 opacity만 0.5, 텍스트/아이콘 자식 opacity 0.85.
- **재계산 결과**: Amber bg+ink 8.88:1 PASS / Teal bg+ink 6.31:1 PASS / Coral bg+ink 6.22:1 PASS / Neutral bg+ink 10.97:1 PASS / Icon Button·Row Action Button 아이콘 약 9~11:1 PASS / Table Row Action 텍스트(teal/coral on 흰) 약 2.60~2.62:1로 3:1 미달.
- **Table Row Action은 별도 취급**: 배경이 항상 흰색이라 배경-opacity 분리가 대비에 기여하지 못하고, 텍스트 색 자체가 7-1절 §3의 기존 수용된 미달값이다. 이번 정정은 opacity=0.45 균일 적용으로 인한 추가 악화분만 제거(1.6:1대→2.6:1대 개선) — 근본 원인은 건드리지 않음, 신규 회귀 아님.
- **적용 범위**: Disabled top-level variant 16개 전체(NeoBtn 8, Button 3, Icon Button 1, Row Action Button 2, Table Row Action 2)에 동일 공식 일괄 적용.
- **재검증**: 대표 variant 스크린샷으로 배경은 파스텔톤, 텍스트/아이콘은 선명하게 읽히는 것을 시각 확인 + 대비 수치 재계산 확인.

### 9-6. NeoSelect Open 패널 hover 배경 하드코딩 결함 수정 (2026-07-15)

`get_design_context`로 NeoSelect(`387:13`) Open 패널의 "친구 (Hover example)" 옵션 노드(Content=Placeholder 변형 `387:8`)가 배경을 `bg-[#f1f1f1]` raw hex로 하드코딩하고 있고 `boundVariables`가 `null`임을 발견했다 — 같은 노드의 텍스트 색은 `color/ink/900`에 정상 바인딩돼 있어 배경만 토큰 누락 상태였다("No token = no component" 위반). Content=Selected 변형(`401:869`)에도 동일한 이름의 hover 예시 노드(`401:876`)가 있어 같은 결함이 복제돼 있었다.

**값 검증**: 하드코딩 값(r=g=b=0.946117639541626, hex `#F1F1F1`)을 9-1절의 hover 블렌드 공식(흰 배경류 t=6%, `mix(white, ink, 0.06)`)으로 역산한 결과 255×0.94 + 26×0.06 = 241.26 ≈ `#F1F1F1`로 정확히 일치 — 임의값이 아니라 이미 문서화된 브랜드 hover 공식이 그대로 적용된 값임을 확인했다.

**토큰 재검토**: 기존 `color/gray/*` primitive(0/50/100/200/300/400/450/500/600/650) 전수 대조 결과 정확히 일치하는 값이 없었다(가장 가까운 `gray/50`≈#F7F8F8, `gray/100`≈#EDEFEF, 둘 다 몇 hex포인트 차이). 근사 재사용 대신 원본 값을 그대로 보존하는 신규 토큰을 최소로 추가했다.

**신규 토큰**:
- Primitive(`VariableCollectionId:95:5`, mode `95:0`): `color/gray/150`(#F1F1F1, scope=[] 숨김, `VariableID:432:2`) — 기존 gray 스텝(50/100) 사이의 신규 스텝.
- Semantic(`VariableCollectionId:95:16`, mode `95:1`): `color/bg-hover-muted`(→gray/150, scope `FRAME_FILL`/`SHAPE_FILL`, `VariableID:432:3`) — 흰 배경류 컴포넌트의 옅은 hover 배경 전용. WEB code syntax `var(--color-bg-hover-muted)`.

**바인딩**: `387:8`/`401:876` 2개 노드 fill을 `color/bg-hover-muted`로 재바인딩 완료. 재대조(`use_figma` 읽기 전용) 결과 `node.boundVariables.fills`가 `VariableID:432:3`을 가리키고 resolved color가 하드코딩 이전 값과 hex 단위로 동일함(#F1F1F1 그대로 유지, 시각적 회귀 없음)을 확인했다. 원본 확정 8개 프레임(`248:11689` 하위)은 이번에도 건드리지 않았다 — NeoSelect는 확정 프레임 밖의 컴포넌트 전용 예시 노드다. **design-qa 재확인 결과 hover 배경이 패널 좌우 끝까지 채워져(인셋 없음) PASS.**

## 10. 전체 컴포넌트 토큰 바인딩 전수 감사 (design-qa, 2026-07-15)

사용자 요청으로 등록된 전체 컴포넌트(5절 기준)의 fill/stroke/텍스트 색이 raw hex가 아니라 토큰(`var(--...)`)으로 바인딩돼 있는지 전수 재검사했다(이전까지는 라운드별 변경분만 스팟체크했었음). NeoBtn/Button/Icon Button/Row Action Button/Table Row Action/Sidebar Nav Item/TypeSelector/NeoInput/CornerInput/NeoSelect/Link/CatBadge 12개 컴포넌트 대표 variant를 감사한 결과 **하드코딩 raw hex 0건, 전부 PASS**(9-6절 hover 배경, 0-12절 NeoInput placeholder 수정 건도 정상 토큰 바인딩 유지 확인됨). Contact Row는 이 감사 라운드 진행 중 문서 손상 사고(위 복구 메모 참고)로 nodeId를 일시적으로 찾지 못해 보류됐다 — 다음 라운드에서 `351:299` 기준으로 재확인 필요.

## 11. FOUNDATIONS 페이지 재대조 완료 (design-systems, 2026-07-15, 0-14절 관련)

0-14절 소급 동기화 라운드에서 Colors(`95:2`)/Typography(`95:3`)/Elevation(`116:5`)/Spacing(`95:4`) 4개 페이지를 실제 Figma 라이브 상태와 재조회해 대조했다. 대조 결과 1~5절 표에 기록된 값과 실제 Figma 변수/스타일 값 사이에 불일치는 발견되지 않았다 — 문서 손상 사고(위 상단 메모, 0-9/0-10절)로 우려됐던 2/3/5/7-2절 세부 표는 이번 재조회로 라이브 상태와 일치함이 확인됐다. Contact Row(`351:299`)도 존재를 재확인했다(10절의 보류 사항 해소).

## 12. design-qa 전체 재검수 후속 결함 3건 수정 (design-systems, 2026-07-15)

design-qa의 전체 재검수(10절의 12-컴포넌트 대표 variant 감사와는 별개로, 이번에는 State=Focus variant까지 포함해 더 넓게 다시 훑은 재검수)에서 새로 발견된 결함 3건(HIGH 1, MEDIUM 1, LOW 1)을 수정했다. 세 건 모두 **구조 변경 없이 값/바인딩만 수정**했다 — variant 개수, State 열거형 축, 보더/텍스트/ink 링 등 다른 속성은 전혀 건드리지 않았다. 원본 확정 8개 프레임(`248:11689` 하위)은 이번에도 열람만 했고 전혀 수정하지 않았다.

### 12-1. HIGH — Button(`259:609`) Amber Focus(`284:1010`) 스퓨리어스 보더 제거

- **문제**: Amber Default(`259:603`)/Hover(`284:1006`)/Press(`284:1008`)/Disabled(`284:1012`)/Loading(`284:1014`) 전부 `strokes=[]`(보더 없음)인데, Focus(`284:1010`)에만 raw 검정(`{r:0,g:0,b:0}`, boundVariableId 없음) 1px `SOLID` 스트로크가 붙어 있었다 — 9-1절 "Focus 순수성" 원칙(배경/보더/텍스트는 Default와 완전히 동일, 차이는 ink 링 DROP_SHADOW 하나뿐) 위반.
- **조치**: `284:1010.strokes`를 빈 배열로 정정. 기존 두 개의 `DROP_SHADOW`(하드 스티커 오프셋 2,2 + ink 링 spread 3, offset 0,0)는 그대로 유지, 배경 fill은 12-2절 재바인딩과 함께 처리.
- **수정 전/후**: strokes `[{type:SOLID, color:#000000, boundVariableId:null}]` → `[]`.
- **검증**: 재조회 결과 `strokesCount: 0`(Amber Default와 동일), `effectsCount: 2`(변경 없음) 확인. `get_screenshot`으로 검정 테두리 없이 정상 렌더링됨을 시각 확인.

### 12-2. MEDIUM — 버튼류 5개 ComponentSet Focus variant 배경 fill raw hex → boundVariable 재바인딩

대상 5개 ComponentSet의 모든 Focus variant(총 15개)를 같은 Style의 Default 형제가 쓰는 것과 동일한 boundVariable로 재바인딩했다. 값(hex) 자체는 변경 없음 — 참조 방식만 raw → 토큰으로 교체.

| ComponentSet | Focus 노드 | Style | 수정 전 | 수정 후 boundVariable |
|---|---|---|---|---|
| NeoBtn(`259:126`) | `284:115`/`284:155` | Amber | raw `#ffcb47`, boundVariableId null | `color/amber/500`(`VariableID:95:8`) |
| NeoBtn(`259:126`) | `284:125`/`284:165` | Teal | raw `#17a398`, boundVariableId null | `color/teal/500`(`VariableID:95:6`) |
| NeoBtn(`259:126`) | `284:135`/`284:175` | Coral | raw `#ff5a76`, boundVariableId null | `color/coral/500`(`VariableID:95:7`) |
| NeoBtn(`259:126`) | `284:145`/`284:185` | Neutral | raw `#ffffff`, boundVariableId null | `color/gray/0`(`VariableID:95:10`) |
| Button(`259:609`) | `284:1010` | Amber | raw `#ffcb47`, boundVariableId null | `color/amber/500`(`VariableID:95:8`) |
| Button(`259:609`) | `284:1020` | Coral | raw `#ff5a76`, boundVariableId null | `color/coral/500`(`VariableID:95:7`) |
| Button(`259:609`) | `284:1030` | Neutral | raw `#ffffff`, boundVariableId null | `color/gray/0`(`VariableID:95:10`) |
| Icon Button(`259:613`) | `284:1040` | Close(단일) | raw `#ffffff`, boundVariableId null | `color/gray/0`(`VariableID:95:10`) |
| Row Action Button(`260:95`) | `284:284` | Neutral | raw `#ffffff`, boundVariableId null | `color/gray/0`(`VariableID:95:10`) |
| Row Action Button(`260:95`) | `284:292` | Danger | raw `#ffffff`, boundVariableId null | `color/gray/0`(`VariableID:95:10`) |
| Table Row Action(`260:100`) | `284:300` | Neutral | raw `#ffffff`, boundVariableId null | `color/gray/0`(`VariableID:95:10`) |
| Table Row Action(`260:100`) | `284:308` | Danger | raw `#ffffff`, boundVariableId null | `color/gray/0`(`VariableID:95:10`) |

- 참고: Row Action Button/Table Row Action은 Neutral/Danger 두 Style 모두 배경이 흰색(`color/gray/0`)이고 보더 색만 Style별로 달라지는 구조라, Focus도 Style에 무관하게 동일한 흰색 토큰에 바인딩된다(원래 Default 구조와 일치).
- Neutral 계열 Focus(NeoBtn `284:145`/`284:185`, Button `284:1030`, Icon Button `284:1040`)는 배경 재바인딩과 별개로 기존 2px ink 보더(`VariableID:95:9`)를 그대로 유지 — 이는 스퓨리어스 보더가 아니라 Neutral 스타일 고유의 정상 보더이므로 이번 작업에서 건드리지 않았다.
- 변경하지 않은 것: strokes(Neutral 외 없음, 그대로 유지), effects(하드 그림자+ink 링), variant 개수/State 축.

### 12-3. LOW — Contact Row(`351:299`) 루트 배경 토큰 재바인딩

- **문제**: 루트 COMPONENT 배경이 raw `#ffffff`(boundVariableId 없음)로 하드코딩. Card, NeoBtn Neutral 등 형제 컴포넌트는 `color/gray/0` 토큰을 씀.
- **조치**: `351:299` 배경 fill을 `color/gray/0`(`VariableID:95:10`, WEB `var(--color-gray-0)`)로 재바인딩. 값(흰색) 자체는 변경 없음.
- **수정 전/후**: fill `{hex:#ffffff, boundVariableId:null}` → `{hex:#ffffff, boundVariableId:"VariableID:95:10"}`.
- **검증**: 재조회 결과 `boundVariableId: "VariableID:95:10"` 확인, `get_screenshot` 결과 이전과 동일하게 렌더링됨(시각적 회귀 없음) 확인.

### 12-4. 자체 재대조 (design-systems, 2026-07-15)

위 3건 모두 수정 직후 `use_figma` 읽기 전용 스크립트로 재조회해 확인했다:
- `284:1010`: `strokesCount:0`(Amber Default와 동일), `effectsCount:2`(변경 없음), fill boundVariableId `VariableID:95:8` — 기대값과 일치.
- 15개 Focus 배경 fill 전부 표에 명시한 boundVariableId와 정확히 일치, hex는 전부 재바인딩 전과 동일값 유지(회귀 없음).
- `351:299`: boundVariableId `VariableID:95:10` — 기대값과 일치.

`get_screenshot`으로 Button(`259:609`) ComponentSet 전체, `284:1010`(Amber Focus 개별), `351:299`(Contact Row) 3곳을 시각 검증해 회귀 없음을 확인했다.

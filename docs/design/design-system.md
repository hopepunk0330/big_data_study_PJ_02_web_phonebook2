# Design System — 확정 토큰/컴포넌트 인벤토리 (State Ledger)

**⚠ ui-designer 등 컴포넌트를 소비하는 모든 에이전트는 반드시 1~7절만 참조하고 8절(Legacy)은 절대 사용하지 않는다.**

이 문서는 design-systems가 만든 토큰(변수)·컴포넌트·아이콘 등록 현황의 **현재 확정 상태**다. Figma FOUNDATIONS/COMPONENTS 구역(비주얼 원본)의 텍스트 미러이며, ui-designer·interaction-designer 등 컴포넌트를 소비하는 모든 에이전트의 소스 오브 트루스다. design-systems가 토큰/컴포넌트를 추가·수정할 때마다 이 파일의 내용을 최신 상태로 유지한다(로그가 아니다 — 만든 과정은 각 에이전트의 `.claude/agent-memory/*.md` 작업 로그와 git 히스토리에 남는다). **⚠ "최신 상태로 유지"는 절대 Write 도구로 파일 전체를 다시 쓰라는 뜻이 아니다 — 이 문장 자체가 과거 두 차례 파일 손상 사고의 원인으로 지목됐다(아래 복구 메모 참고). 반드시 먼저 전체를 Read한 뒤 Edit 도구로 필요한 부분만 바꾸거나 끝에 새 절을 추가한다.**

**fileKey**: `zgGlMBwFglaDlaeyP4CkgR`

**⚠ 2026-07-15 문서 복구 메모 1차(투명성 기록)**: 이 세션 중 서브에이전트가 "파일 끝에 새 절만 append" 지시를 잘못 수행(전체 덮어쓰기)해 파일이 586줄→61줄로 손상되는 사고가 있었고, 이후 복구 과정에서도 한 차례 더 잘못된 번호(0-9/0-10)로 다른 내용이 섞여 들어가는 2차 혼선이 있었다. git 커밋(`4a0db785`, 520줄, 0-1~0-8절/1~9-5절)으로 대부분 복구했고, 커밋되지 않았던 실제 0-9/0-10절은 design-pl이 사고 직전 직접 읽어뒀던 원문으로 복원했다.

**⚠ 2026-07-15 문서 복구 메모 2차(투명성 기록)**: 1차 복구 직후 `.claude/agents/design-systems.md`에 "Write 전체 덮어쓰기 금지, 항상 전체 Read 후 Edit/append" 규칙을 명문화했음에도 불구하고, 같은 세션 안에서 체크박스 등록 라운드 중 **재차 손상**(697줄→372줄, 섹션 1~11 및 12절 전체 소실, 0-1~0-18 하위 항목만 생존)됐다. 근본 원인으로 위 문단의 "덮어써서 최신 상태로 유지한다"는 이 문서 자신의 표현이 지목됐다 — 하네스 규칙집(design-systems.md)만 고치고 정작 이 문서 자체의 자기소개 문장은 그대로 둬서, 서브에이전트가 이 문서를 읽을 때마다 "덮어쓰라"는 지시를 다시 흡수했을 가능성이 높다. 이번엔 git HEAD(`4cdcbc9`, 624줄)를 기준으로 삼되, 커밋되지 않았던 12절(Button Focus 결함 수정)과 0-15~0-18절은 세션 중 직접 읽어뒀던 diff 기록으로 재구성했고, 위 문단 표현 자체도 함께 정정했다.

## 0. 이번 라운드 — 사용자 확정 디자인(8개 프레임)에서 직접 추출 (2-4번 규칙)

이번 라운드는 `docs/harness/design-team/figma-file-organization.md` 2-4번 규칙에 따라, **AI 파일럿을 거치지 않고** 사용자가 Figma에서 직접 만들어 확정한 8개 프레임("확정 디자인 - 절대 원본 건들지 말것-", 부모 섹션 `248:11689`)에서 실제 사용된 값을 직접 관찰(`get_screenshot`/`get_metadata`)해 토큰·컴포넌트로 추출했다. 8개 프레임은 전부 읽기 전용으로만 관찰했고 내용/이름을 전혀 수정하지 않았다.

**⚠ 2026-07-16 갱신**: 이 절이 가리키는 구 확정 디자인 섹션(`248:11689`, 파일럿 페이지 `222:524` 하위 8개 프레임)은 신규 확정 디자인 세트(`501:2505`, 0-20절 Stage2)로 완전히 대체된 뒤 **14-1절에서 완전히 삭제됐다**(2026-07-16) — 더 이상 Figma 파일에 존재하지 않는다. 아래 0절 본문은 삭제 당시까지의 작업 이력 기록으로 보존하되, `248:11689` 참조는 전부 "이미 삭제된 구 소스"로 읽어야 한다.

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
| Box | 14×14, 흰배경(`color/gray/0`=`VariableID:95:10`) + 2px ink(`color/ink/900`=`VariableID:95:9`) INSIDE 보더, radius0 — 원본 `247:6823`과 hex·strokeWeight·strokeAlign·size 전부 일치. **0-20절(Stage2, 2026-07-15)**: State=Checked Box 배경만 `color/sky/500`(#1395E6)로 리바인딩(login 신규 확정 프레임 실측 기준, "fill만 갱신" 지시 범위) |
| Label 텍스트 | Noto Sans KR Regular 12px, `color/ink/900` fill에 paint opacity 0.5(원본 `247:6825` rgba(26,26,26,0.5) 그대로 재현, 노드 opacity 아님 — paint opacity) |
| Checked | Box 안에 8×7 벡터 체크마크(stroke `color/ink/900`, weight2) 추가 — 단순 프리미티브라 graphic-designer 투입 없이 직접 제작. **관찰(Stage2)**: 신규 확정 프레임의 체크마크는 흰색(`604:5954`)으로 보이나 이번 라운드는 Box fill만 갱신 지시 범위라 ink 유지, 변경하지 않음. ※ 이후 21절(2026-07-16) 재조사 결과 이 판단은 뒤집혔음 — 체크마크는 실제로 `color/ink/900`(검정)이었고, 최종적으로 `color/text-inverse`(#FFFFFF, 흰색)로 리바인딩됨. 이 관찰 시점의 "흰색으로 보이나"라는 시각적 인상이 오히려 맞았던 것으로 확인. **⚠ 2026-07-16 정정(0-26절)**: 이 행의 "weight2" 기록은 오기였다 — graphic-designer가 리토피트 작업 중 라이브로 재실측한 결과 실제 `strokeWeight`는 **3**(strokeCap/Join ROUND)이었다. 값 자체는 애초 등록 시점부터 3이었고 이 표 기록만 오기였을 뿐, 실제 컴포넌트 시각값은 변경되지 않았다. |
| Focus | Default를 clone + ink 링(`DROP_SHADOW` spread3, offset0,0, `#1a1a1a` alpha1)만 추가(9-1절 공식 그대로) |
| Disabled | Box fill/stroke paint opacity 0.5, Label 노드 opacity 0.85(9-1절 Disabled 공식 그대로) |
| 신규 토큰 | 없음 — `color/gray/0`/`color/ink/900` 전부 기존 토큰 재사용 |
| 스펙 시트 | `Spec — Checkbox`(`475:762`, Component Specs 페이지 `342:2`), 제목+설명+4칸 그리드+상태 라벨(`get_screenshot` 확인) |

**재대조 방법**: `get_design_context`로 원본 `247:6822`(로그인 확정 프레임 내 "☐ 로그인 상태 유지")를 재실측하고, 등록된 4 variant의 fills/strokes/opacity/boundVariables를 `use_figma` 읽기 전용 스크립트로 재조회해 원본과 항목별 대조 — **불일치 0건**, 추가 수정 없음.

**2) 라디오 버튼 — 미등록 판단**

확정 8개 프레임(`248:11689` 하위) 전체를 `ELLIPSE` 타입 기준으로 전수 검색(32건 발견) — 전부 장식용 MemphisAccents 원, Avatar/유저 아이콘 원, `Icon/Alert` 원, TypeSelector 칩 내부 6×6 선택 dot이었고 "원형 보더+원형 채움 다이얼" 형태의 라디오 패턴은 0건. 화면정의서(`02_연락처관리_웹서비스_화면정의서_v1.15.md`) SCR-002 "종류"는 드롭다운(select)으로 명시("종류가 '입력'에서 '선택'으로 바뀐 이유" 절), 편집 모달 카테고리 선택은 TypeSelector(칩, `257:28`)가 이미 담당. 전체 화면 목록(SCR-001/002/003/004/900) 어디에도 단일 선택 그룹(라디오) 흐름 없음. **판단: 미등록(불필요)** — 근거 (a) 확정 프레임에 실물 0건 (b) SCR-002 종류는 Select/TypeSelector가 이미 커버 (c) 화면정의서 전체에 다른 단일선택 그룹 흐름 없음. 이후 실제로 라디오 그룹이 필요한 흐름이 생기면 그때 재검토.

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

### 0-20. Stage 2 — 두 번째 확정 디자인 세트(8프레임) 토큰 바인딩 반영 (2026-07-15)

**소스 교체**: 구 확정 디자인 섹션(`248:11689`, "사용자가 최종 아니다"라고 밝힌 시점의 스냅샷)이 신규 확정 디자인 섹션 `501:2505`(파일럿 페이지 `222:524` 하위, 8개 프레임)로 교체됐다. Stage 1(직전 라운드)이 8개 프레임을 실측해 diff를 식별하고 Primitive/Semantic 색상 토큰 13개를 신설했고, 이번 Stage 2는 그 토큰을 실제 등록 컴포넌트에 **바인딩으로만** 반영했다. 8개 프레임은 이번에도 읽기 전용으로만 관찰, 무수정.

| 화면 | nodeId |
|---|---|
| main | `501:6008` |
| main-수정 | `501:3042` |
| main-삭제 | `501:3636` |
| main-검색없음 | `501:4218` |
| Join | `501:4692` |
| login | `501:4940` |
| login-알림창 | `501:5188` |
| main-알림창 | `501:6548` |

**신규 토큰 13개(Stage 1 생성분, 아래 1-1/1-2절에 정식 반영)**: Primitive 6(`color/sky/500` `color/navy/700` `color/amber/600` `color/paleblue/100` `color/paleblue/50` `color/gray/375`) + Semantic 7(`color/bg-brand-blue` `color/bg-accent-navy` `color/text-link-navy` `color/border-divider-cool` `color/bg-row-alt` `color/bg-cta-amber` `color/text-placeholder-strong`).

**갱신한 컴포넌트/바인딩(자체 재대조 완료, 항목별 hex·boundVariable 재조회로 확인)**:

| 컴포넌트 | 노드 | 변경 내용 | 재대조 결과 |
|---|---|---|---|
| Sidebar Nav Item | `258:29`, State=Active `258:17` | 배경 amber/500(#FFCB47)→`color/bg-accent-navy`(`VariableID:615:129`) | resolvedHex `#074d7b` 일치 |
| Card | `262:15`, AccentStrip-Top(Type=Modal `262:7`/Type=Auth `262:11`) | 배경 amber/500→`color/bg-cta-amber`(`VariableID:615:133`) | resolvedHex `#ffce2c` 일치 (main-수정 `501:3580`, login `501:5050`, Join `501:4802` 원본과 대조) |
| Icon/Alert(마스터, `96:41`) | Ellipse `96:38` | 배경 raw amber(#FFCB47, 미바인딩)→`color/bg-cta-amber` | resolvedHex `#ffce2c` 일치 (login-알림창 `501:5188` 원본 Ellipse `#ffce2c`와 대조) |
| NeoBtn | `259:126`, Amber Default/Focus/Disabled/Loading × Size=Default/Compact (8 variant: `259:110`/`259:118`/`284:115`/`284:155`/`284:117`/`284:157`/`284:119`/`284:159`) | amber/500→`color/bg-cta-amber` | 전부 resolvedHex `#ffce2c` 일치. **⚠ 2026-07-16 갱신(0-25절)**: 이 행이 다룬 NeoBtn Amber 8 variant는 이후 확정 디자인 근거가 없는 구 잔재로 확인되어 레거시 해제됐다(24 variant 전체 detach → `784:940` 컨테이너로 이전 보존, 삭제 아님) — **현재 NeoBtn에는 Style=Amber가 존재하지 않는다**(Style=Coral/Neutral/Sky/Navy/Ink 5개, 18절 참고). 이 표 행은 그 갱신 이전 시점(Stage2, 2026-07-15) 기준 기록으로 보존한다. Amber(#ffce2c)의 실제 유효 사용처는 Button(`259:609`)뿐이다. |
| Button | `259:609`, Amber Default/Focus/Disabled/Loading(4 variant: `259:603`/`284:1010`/`284:1012`/`284:1014`) | amber/500→`color/bg-cta-amber` | 전부 resolvedHex `#ffce2c` 일치 |
| Link | `341:3`, 텍스트 `341:4` | fill `color/text-link`(teal)→`color/text-link-navy`(`VariableID:615:130`) | resolvedHex `#074d7b` 일치, login 원본(`501:5101`, "비밀번호 재설정") 실측값과 일치. Join "비밀번호 찾기"(`501:4853`)는 재실측 결과 여전히 teal(#17a398)이라 미변경(실측 우선 원칙) |
| Checkbox | `474:899`, State=Checked Box `474:886` | 배경 흰색(`color/gray/0`)→`color/sky/500`(`VariableID:615:122`) | resolvedHex `#1395e6` 일치, login 원본(`604:5953`) 실측값과 일치. **지시대로 fill만 갱신** — 체크마크 stroke는 원본이 흰색(`604:5954`)으로 관찰됐으나 이번 범위 밖이라 ink(`#1a1a1a`) 그대로 유지(스펙 시트에 관찰 기록만 남김). **⚠ 2026-07-16 후속 정정(21절)**: 이 절에서 "범위 밖"이라 미룬 체크마크 색은 이후 21절에서 실제로 `color/text-inverse`(#FFFFFF, 흰색)로 재바인딩 완료됐다 — 여기 기록된 원본 관찰("흰색 `604:5954`")이 정확했고, 나중에 그대로 반영됐다. 상세는 21절 참고. |
| Contact Row | 구 `351:299`(단일 COMPONENT) → 신규 COMPONENT_SET `624:1070`("Row=Default/Alt", 2 variant) | ① 하단 구분선 stroke `color/border-divider-warm`→`color/border-divider-cool`(`VariableID:615:131`, main 원본 6개 행 실측 `#d3ecfb`와 일치) — 두 variant 공통. ② 신규 `Row=Alt`(`624:1061`) 배경 `color/gray/0`(흰색)→`color/bg-row-alt`(`VariableID:615:132`) — 짝수행 zebra striping. `Row=Default`(`351:299`, 기존 ID 유지, 기존 참조 안 깨짐)는 배경 무수정 | Default stroke `#d3ecfb`/Alt fill `#f5fafd` 일치, TEXT 프로퍼티(`name`/`phone`/`address`) 정상 승계 확인(`get_screenshot`) |

**스펙 시트/문서 갱신**: `Spec — Contact Row`(`352:726`)를 2칸 그리드(Row=Default/Alt)로 재구성(clipsContent=false 확인), 설명 갱신. `Spec — Link`(`344:759`)/`Spec — Sidebar Nav Item`(`343:1106`)/`Spec — NeoBtn`(`342:3`)/`Spec — Checkbox`(`475:762`)는 인스턴스 기반이라 색 변경이 자동 반영됨을 스크린샷으로 확인 — 다만 설명 텍스트 캡션 갱신은 이 라운드에서 Link(`344:761`)/Checkbox(`475:764`) 2개만 실제로 반영됐고, NeoBtn(`342:5`)/Sidebar Nav Item(`343:1108`) 캡션 2개는 이번 라운드 서술과 달리 구 설명 그대로 남아 있었다(design-qa 감사에서 발견, 2026-07-15 별도 정정 라운드에서 두 캡션 모두 Stage2 note 문단을 추가해 실제로 갱신 완료 — 컴포넌트 색상/바인딩 자체는 이 표에 기록된 대로 정상이었고 이번 정정은 순수 문서 캡션 텍스트만 대상). NeoBtn/Button/Card/Sidebar Nav Item/Icon(`96:41`) 컴포넌트 `description` 메타데이터에도 각각 Stage2 갱신 문구 추가. FOUNDATIONS "Colors"(`95:2`, 루트 `95:40`) 페이지에 "Stage2 신규 Primitives(6개)"/"Stage2 신규 Semantic Colors(7개)" 스와치 섹션 신규 추가(기존 섹션 뒤에 이어붙임, 루트 프레임 높이 2110→2346 재조정), `get_screenshot`으로 전체 페이지 렌더링 확인.

**WCAG 재계산(신규/변경분 전수, 상대휘도 공식 직접 계산)**:
- `color/text-link-navy`(#074D7B) on 흰 배경: **8.92:1 PASS**(12px Bold는 큰 텍스트 기준 미달이라 4.5:1 적용 — 기존 teal 3.12:1 미달값 대비 큰 개선).
- `color/bg-accent-navy`(#074D7B) 배경 + 흰 텍스트("전체" 등): **8.92:1 PASS**.
- ink(#1A1A1A) on `color/bg-cta-amber`(#FFCE2C): **11.70:1 PASS**(기존 amber/500 대비 근사, 기존 5.3~11:1 PASS 범위 유지).
- ink 보더(#1A1A1A) on `color/sky/500`(#1395E6, Checkbox Checked 박스 경계, WCAG 1.4.11 비텍스트 3:1 기준): **5.36:1 PASS**.
- `color/border-divider-cool`(#D3ECFB)/`color/bg-row-alt`(#F5FAFD)는 장식·배경용이라 별도 텍스트 대비 기준 미적용(기존 border-divider-warm과 동일 취급). bg-row-alt 위 기존 텍스트(name/phone/address)는 배경이 순백에서 96% 밝기로만 이동해 3절의 기존 PASS/미달 판정에 실질적 영향 없음(차이 <0.05).

**미해결 관찰 2건(수정하지 않음, 사용자 확인 필요)**:
1. **헤더 "로그아웃" NeoBtn(main 프레임 `501:6373`)의 ink 배경(#1a1a1a) + amber 보더(#ffcb47, 구값) + offset(3,3) 그림자** — 기존 Hard-1/2/6 스케일에 없는 이례값이고 단일 인스턴스라 의도/미완성 편집 여부 판단 불가. **토큰화·리바인딩하지 않음**, 컴포넌트 마스터(NeoBtn Neutral)는 기존 값(보조버튼 스타일, 그림자 없음) 그대로 유지.
2. **main-삭제(`501:3636`)/main-알림창(`501:6548`) amber 미반영** — 두 프레임의 카드 상단 스트립/토스트 강조 원이 여전히 구값(#FFCB47)이다(main-삭제 스트립 `501:4174`, main-알림창 alert ellipse `I501:7088;96:38`). 컴포넌트 마스터는 신규값(#FFCE2C, `color/bg-cta-amber`)을 정식 채택했으므로(4개 프레임이 이미 신규값 사용, 사용자가 "컬러 바꿨다"고 명시) 이 2개 프레임과 마스터 사이에 의도적 불일치가 생겼다 — 원본 read-only 방침상 수정하지 않고 관찰만 기록.

**보류 1건**: main-검색없음(`501:4218`)의 "전체 보기" 버튼(`517:2753`, ink 배경+흰 텍스트+Hard-2 그림자 조합)이 기존 Button/NeoBtn Style=Amber/Teal/Coral/Neutral 어디에도 해당하지 않음(Neutral은 흰 배경+ink 보더이지 ink 배경이 아님) — 신규 variant를 만들지 않고 이번 라운드는 보류, 관찰만 기록(범위 확대 방지). **⚠ 2026-07-16 시점 각주**: 이 판단 시점(Stage2, 2026-07-15)엔 NeoBtn이 Style=Amber/Teal을 갖고 있었다 — 이후 0-25절(2026-07-16)에서 NeoBtn의 Amber/Teal은 확정 디자인 근거가 없는 구 잔재로 확인되어 레거시 해제됐다(현재 Style=Coral/Neutral/Sky/Navy/Ink). 이 보류 판단 자체는 이번 각주 정정에서 재검토하지 않았다(범위 확대 방지 원칙 유지) — 필요 시 후속 라운드에서 재검토.

**추가 관찰(변경 없음, 참고용)**: ① Sidebar 컨테이너 전체 배경(#1395E6→`color/bg-brand-blue` 대응)과 테이블 헤더/사이드바 밖 "전체" 필터 배경(#074D7B→`color/bg-accent-navy` 대응)은 화면 안에서 **등록된 컴포넌트의 INSTANCE가 아니라 원본 확정 프레임 안의 raw FRAME**으로 확인됐다(파일 전체에 "Sidebar"라는 이름의 별도 COMPONENT/COMPONENT_SET가 존재하지 않음, `Table Row`/`Card`/`Component Specs` 등 전 페이지 검색 완료) — Table Header/EmptyState와 동일하게 화면조립 영역으로 판단해 컴포넌트화·리바인딩 대상에서 제외한다. 두 토큰은 정식 등록돼 있으니 ui-designer가 SCREENS 단계에서 직접 참조하면 된다. ② 사이드바 "새 카테고리(1~10자)" 입력창 placeholder(`501:6357`, #AAAAAA)도 동일하게 raw FRAME(NeoInput의 INSTANCE 아님)이라 리바인딩 대상이 없다 — `color/text-placeholder-strong` 토큰은 등록 완료(Colors 페이지 스와치 포함), 향후 이 필드가 실제 컴포넌트로 승격되면 그때 바인딩한다. ③ Hover/Press 상태의 Amber 블렌드 raw 값(NeoBtn/Button, 기존 #E4B642/#C8A13C)은 이번에 재계산하지 않았다 — 9-1절 블렌드 공식은 interaction-designer 소관이라 새 base(#FFCE2C)로 재계산이 필요하면 후속 라운드에서 처리.

원본 확정 8개 프레임(`501:2505` 하위)은 이번 라운드 전체에서 무수정 확인.

### 0-21. Colors 페이지 재정리 — Stage2 임시 섹션을 정식 Primitives/Semantic 그리드로 통합 (2026-07-15)

0-20절에서 "Stage2 신규 Primitives(6개)"/"Stage2 신규 Semantic Colors(7개)"를 페이지 하단에 별도 임시 섹션으로 붙였던 것을 사용자 지적에 따라 정정했다. Primitive 6개(`color/sky/500` `color/navy/700` `color/amber/600` `color/paleblue/100` `color/paleblue/50` `color/gray/375`)는 기존 "Primitives" 그리드(`95:44`)에, Semantic 7개(`color/bg-brand-blue` `color/bg-accent-navy` `color/text-link-navy` `color/border-divider-cool` `color/bg-row-alt` `color/bg-cta-amber` `color/text-placeholder-strong`)는 기존 "Semantic" 그리드(`95:123`)에 각각 자연스럽게 편입(2번째 줄로 wrap, `layoutWrap`을 파일 기존 Grid 관례대로 활성화)했고, "Stage2" 표기가 붙은 임시 헤더+그리드 프레임(`625:1077`/`625:1078`/`625:1103`/`625:1104`)은 삭제했다. Semantic 스와치 7개는 기존 표기 관례("alias 원시값명")에 맞춰 라벨을 "#hex"에서 "alias sky/500" 등으로 정정했다. Colors Root(`95:40`)는 VERTICAL auto-layout이라 하위 섹션들이 자동 재배치됐고, 루트 높이만 2346→2232로 재조정했다. **Variable 자체(이름/값/alias/ID)는 전혀 건드리지 않았다** — 순수 시각 문서 재배치다. `get_screenshot`/`get_metadata`로 재확인해 13개 스와치가 각 섹션에 정상 편입되고 "Stage2" 표기가 전혀 남지 않았음을 확인했다.

### 0-22. NeoInput/CornerInput Disabled variant 추가 — Stage 2-b (2026-07-16)

Stage 2-a(NeoBtn/Button/Table Row Action/Checkbox)에 이어, Input 계열 두 컴포넌트에 Disabled 예외 처리를 적용했다. 사전 조건: 신규 Semantic 토큰 3종(`color/bg-disabled`=`VariableID:643:2` **#929292**, `color/border-disabled`=`VariableID:643:3` #5C6366, `color/text-disabled`=`VariableID:643:4` #555555, Semantic Colors 컬렉션 `VariableCollectionId:95:16`)은 이미 Stage1/2-a에서 생성돼 있어 재사용만 했다(신규 변수 생성 없음). **⚠ 2026-07-16 정정(0-23절)**: `color/bg-disabled`는 최초 `color/gray/450`(#888888, 흰 배경 대비 3.54:1)을 alias했으나 사용자 피드백으로 신규 primitive `color/gray/425`(#929292, `VariableID:646:2`, 흰 배경 대비 3.11:1)를 추가해 alias를 교체했다 — 최종값은 #929292다. 아래 재대조 값도 최종값 기준으로 정정 반영.

**핵심 원칙 — Input은 "값을 보여주는 display"라 다른 4개(NeoBtn/Button/Table Row Action/Checkbox)와 다르게 처리**: 사용자 지시대로 배경(bg)·보더(line)만 `color/bg-disabled`/`color/border-disabled`로 통일하고, **텍스트는 `color/ink/900`(Default와 완전히 동일한 색, `VariableID:95:9`) 그대로 유지 — `color/text-disabled`는 이 두 컴포넌트에 전혀 사용하지 않았다.**

**추가 방식**: 새 축을 만들지 않고 기존 `State` 열거형(Default/Focus)에 값 `Disabled`를 추가(0-15/0-16절 관례 그대로). `Content=Filled, Error=No, State=Default`(NeoInput `261:10`/CornerInput `261:12`)를 clone한 뒤 배경 fill→`color/bg-disabled`, 보더 stroke→`color/border-disabled`만 재바인딩하고 텍스트는 손대지 않았다. Error=Yes와의 조합은 만들지 않음(비활성 필드는 유효성 검사 대상이 아니므로 부분-매트릭스로 유지).

- **신규 노드**: NeoInput `Content=Filled, Error=No, State=Disabled` = `644:2`(180×36, ComponentSet `288:12` 이제 7 variant, `State`=`Default/Focus/Disabled`). CornerInput `Content=Filled, Error=No, State=Disabled` = `644:963`(392×44, ComponentSet `288:27` 이제 7 variant, radius0 유지).
- **자체 재대조(design-systems 규칙, 생략 불가)**: 두 신규 노드의 fill(hex `#929292`[**2026-07-16 정정**, 최초 등록 시점엔 alias가 gray/450이라 #888888이었음], boundVariable `VariableID:643:2`)·stroke(hex `#5c6366`, boundVariable `VariableID:643:3`)·텍스트 fill(hex `#1a1a1a`, boundVariable `VariableID:95:9` — Default 텍스트 노드와 정확히 동일 ID)을 재조회해 기대값과 정확히 일치함을 확인했다. **`VariableID:643:4`(text-disabled)는 어디에도 바인딩되지 않았음을 명시적으로 재확인**했다. `get_screenshot`(inline)으로 두 스펙 시트를 재확인해 회색 배경/보더 대비 텍스트("윤아")가 뚜렷하게 읽힘을 시각적으로도 확인했다.
- **스펙 시트 갱신**: `Spec — NeoInput`(`344:721`)/`Spec — CornerInput`(`344:740`)에 기존 FocusSection과 동일한 레이아웃 패턴(RowLabel + 라벨텍스트+인스턴스+캡션 셀, 전부 `clipsContent=false`)으로 "Disabled" 행을 신규 추가 — 각각 6→7칸. 컨테이너 성장분(NeoInput +92px, CornerInput +100px)만큼 Component Specs 페이지의 이후 시트(CornerInput/Link/Contact Row/NeoSelect/Checkbox)를 겹치지 않게 아래로 재배치했다(다른 시트 내용은 무수정, 위치만 이동). ComponentSet `description`과 스펙 시트 설명 텍스트도 "7 variant" 및 Disabled 처리 방식으로 갱신했다.

원본 확정 프레임은 이번에도 열람하지 않았다 — Disabled 상태 자체가 확정 프레임 밖의 인터랙션 상태 확장물(9절과 동일한 성격)이라 원본과 무관하다.

### 0-23. Disabled 토큰화 마무리 — 최종값 정정 + FOUNDATIONS 반영 + 커버리지 점검 (2026-07-16, Stage 2-c)

0-20~0-22절(Stage2/2-a/2-b)에서 진행된 Disabled 색 토큰화 라운드를 마무리하며 값 정정, 시각 문서화, 자체 재대조를 완료했다. 원본 확정 프레임은 이번에도 무수정(읽기 전용 재확인만).

**1) 최종 토큰값(정정 완료, Figma 라이브 상태 기준)**

| 토큰 | 값 | alias 대상 | 흰 배경 대비(직접 계산) | 적용 컴포넌트 |
|---|---|---|---|---|
| `color/bg-disabled`(`VariableID:643:2`) | **#929292** | `color/gray/425`(`VariableID:646:2`, 신규 primitive) | 3.11:1(비텍스트 3:1 기준 PASS) | NeoBtn/Button/Table Row Action/Checkbox/NeoInput/CornerInput 배경 |
| `color/border-disabled`(`VariableID:643:3`) | #5C6366 | `color/gray/600`(기존) | 6.12:1 PASS | 위 6개 보더 |
| `color/text-disabled`(`VariableID:643:4`) | #555555 | `color/gray/650`(기존) | 7.45:1 PASS | Checkbox 라벨만(Input 2종은 예외 — 아래 3항) |

**경위**: `color/bg-disabled`는 최초 `color/gray/450`(#888888, 3.54:1)을 alias해 등록했으나, 사용자 피드백에 따라 신규 primitive `color/gray/425`(#929292, 3.11:1)를 추가해 alias만 교체했다(semantic 토큰 ID `VariableID:643:2` 자체는 변경 없음, alias 대상만 gray/450→gray/425). WCAG 값은 상대휘도 공식으로 직접 재계산해 검증했다(3.11:1/6.12:1/7.45:1 전부 재확인 완료).

**2) 적용 노드 자체 재대조 결과(전수, 2026-07-16)**: 아래 14개 노드의 fill/stroke boundVariable을 재조회해 전부 `VariableID:643:2/3/4`에 정확히 바인딩되고 resolvedHex가 위 표와 일치함을 확인했다 — NeoBtn Disabled 8(`284:117`/`127`/`137`/`147`/`157`/`167`/`177`/`187`), Button Disabled 3(`284:1012`/`1022`/`1032`), Table Row Action Disabled 2(`284:302`/`310`), Checkbox Disabled Box+Label(`474:893`/`474:894`), NeoInput Disabled(`644:2`), CornerInput Disabled(`644:963`).

**3) Input 예외 재확인**: NeoInput(`644:3`)/CornerInput(`644:964`) 텍스트 노드는 `color/text-disabled`가 아니라 `color/ink/900`(`VariableID:95:9`, #1a1a1a, Default와 동일)에 바인딩돼 있음을 재확인 — Input은 "값을 보여주는 display"라는 기존 원칙 그대로 유지.

**4) 커버리지 갭 발견(신규, 이번 라운드 자체 점검 중 발견)**: Icon Button(`259:613`)과 Row Action Button(`260:95`)의 Disabled variant(`284:1042`, `284:286`/`284:294`)는 **아직 이번 토큰화 대상에 포함되지 않았다** — 재조회 결과 여전히 9-5절의 구 공식(배경/보더 paint opacity 0.5, boundVariable 없거나 별도)을 그대로 쓰고 있다. Stage2-a 범위가 "NeoBtn/Button/Table Row Action/Checkbox"로 명시적으로 한정돼 있어 이번 라운드에서 확대하지 않았다 — 필요 시 별도 라운드로 동일 공식(bg-disabled/border-disabled, 텍스트/아이콘은 컴포넌트 성격에 따라 판단) 적용 검토(7-2절에 TODO로 기록).

**5) 스펙 시트 6개 재확인**: NeoBtn(`342:3`)/Button(`343:50`)/Table Row Action(`343:1044`)/Checkbox(`475:762`)/NeoInput(`344:721`)/CornerInput(`344:740`) 전부 `get_screenshot`으로 재확인 — Disabled 셀이 #929292 배경으로 정상 렌더링, 잘림/겹침 없음.

**6) FOUNDATIONS Colors(`95:2`) 스와치 반영 — ⚠ 2026-07-16 정정(design-qa HIGH 지적)**: 최초 작업 시 신규 4개 토큰을 "신규 Primitives"(`436:3`)/"Semantic Colors (Additional)"(`436:143`)라는 별도 병렬 섹션에 추가해, 0-21절에서 이미 정리했던 "Stage2 신규 섹션 분리" 문제를 그대로 재현했다. 재정정하며 확인한 결과 이 두 섹션은 애초에 0-14절부터 존재해온 미통합 레거시 섹션(각각 primitive 22개/semantic 13개 보유)이었음이 드러나, 신규 4개만 빼내는 대신 0-21절과 동일한 방식으로 **두 섹션 전체(39개 스와치)를 정식 그리드로 완전히 통합**했다.
- Primitive 23개(gray/425 포함, 신규 노드 `650:2`) — 전부 정식 "Primitives" 그리드(`95:44`)로 이동. `color/gray/425`는 gray/400(`95:77`) 바로 다음(gray/450은 이 그리드에 없어 값 순서상 가장 가까운 gray/400 뒤에 배치).
- Semantic 16개(`color/bg-disabled`/`color/border-disabled`/`color/text-disabled` 포함, 신규 노드 `650:6`/`650:10`/`650:14`) — 전부 정식 "Semantic" 그리드(`95:123`)로 이동(기존 그리드 끝에 추가).
- "신규 Primitives"/"Semantic Colors (Additional)" 헤더 텍스트(`436:2`/`436:142`)와 빈 섹션 프레임(`436:3`/`436:143`)은 삭제 완료 — 페이지에 "신규"/"Additional" 표기가 더 이상 남아있지 않다.
- Variable 자체(이름/값/alias/ID)는 전혀 건드리지 않았다 — 순수 시각 재배치. `get_screenshot`/`get_metadata`로 재확인해 39개 스와치가 정식 그리드에 정상 편입되고 임시 섹션이 완전히 사라졌음을 확인했다.

**7) 컴포넌트 description 메타데이터 갱신**: NeoBtn/Button/Table Row Action/Checkbox 4개 컴포넌트의 Figma `description`에 Stage2-a Disabled 색 토큰 전환 사실을 반영(Checkbox는 기존에 구 opacity 공식이 그대로 남아 있던 stale 문구를 실제 값으로 교체 — design-qa 없이 자체 발견·수정).

원본 확정 프레임(`501:2505`/`248:11689` 하위)은 이번 라운드에서도 열람하지 않았다.

### 0-24. bg-disabled 추가 밝기 조정(사용자 명시적 승인, WCAG 기준 무시) + Icon Button/Row Action Button Disabled 토큰 통일 (2026-07-16, Stage 2-d)

**배경**: 사용자가 직전 라운드(0-22/0-23절) 결과물을 확인한 뒤 두 가지를 지시했다. ① `color/bg-disabled`(#929292)를 "WCAG 1.4.11 비텍스트 최소 기준(3:1)을 못 맞춰도 좋으니 더 밝게" 조정 — 이 트레이드오프를 명확히 알리고 사용자가 "기준 무시하고 원하는 만큼 밝게"라고 명시적으로 재확인했다. ② "Icon Button/Row Action Button의 Disabled에도 적용 공통해야지, 인풋만 예외야" — 0-23절에서 발견된 미이행 갭(Icon Button/Row Action Button만 구 opacity 0.5 공식에 남아있던 문제)을 해소하라는 지시. 원본 확정 프레임(`501:2505` 하위)은 이번에도 무수정(읽기 전용조차 필요 없어 열람하지 않음 — 이 라운드는 순수 인터랙션 상태 확장 유지보수라 9절과 동일하게 원본과 무관).

**1) `color/bg-disabled`(`VariableID:643:2`) alias 교체**: `color/gray/425`(#929292, `VariableID:646:2`) → `color/gray/350`(#BBBBBB, `VariableID:434:4`). `color/gray/350`은 0-12절에서 NeoInput placeholder 텍스트 전용으로 이미 등록돼 있던 기존 primitive다 — 사용자가 제시한 참고 범위(`gray/300` #CCCCCC ~ `gray/375` #AAAAAA)의 정중앙에 해당하는 값이 이미 존재해, 근접 중복 primitive를 새로 만들지 않고 그대로 재사용했다(이 프로젝트의 기존 관례 "근사 재사용 대신 신규 최소 추가"를 이번엔 반대 방향 — "정확히 일치하는 기존 값이 있으면 신규 추가하지 않고 재사용" — 로 적용). **alias 구조 덕분에 어떤 컴포넌트도 재바인딩하지 않고 semantic 변수 값만 교체해 기존 적용분(NeoBtn/Button/Table Row Action/Checkbox/NeoInput/CornerInput) 전부 자동 갱신됐다** — 6개 스펙 시트(`342:3`/`343:50`/`343:1044`/`475:762`/`344:721`/`344:740`) 전부 `get_screenshot`으로 재확인해 새 밝기가 정상 반영되고 잘림/깨짐 없음을 확인했다. `color/gray/425` primitive 자체는 삭제하지 않고 보존하되, 이제 어떤 semantic에도 alias되지 않는 **orphan 상태**로 남는다(1-1절에 명시).

**WCAG 재계산(직접 상대휘도 공식)**: `color/bg-disabled`(#BBBBBB) on 흰 배경 = **1.92:1** — WCAG 1.4.11 비텍스트 3:1 기준 **미달**(3.11:1→1.92:1로 더 낮아짐). **사용자 명시적 요청으로 이 미달을 그대로 수용한다** — "이번 프로젝트에 한해 WCAG 1.4.11 권장 기준 미만, 완화 적용"으로 명시 기록한다. 부수 효과로 그 위에 얹히는 텍스트/아이콘 대비는 오히려 개선됐다: `color/text-disabled`(#555555) on 새 bg = **3.88:1**(구 배경 대비 2.40:1→개선), `color/ink/900`(#1A1A1A, NeoInput/CornerInput Disabled 텍스트) on 새 bg = **9.06:1**(구 배경 대비 5.59:1→개선). `color/border-disabled`(#5C6366)와 새 배경 사이의 시각적 구분은 스크린샷으로 육안 확인 — 여전히 뚜렷이 구분됨.

**Colors 페이지(`95:2`) bg-disabled 스와치 정정**: 라벨 텍스트(`650:9`) "alias gray/425"→"alias gray/350"로 갱신. 스와치 사각형(`650:7`)이 실제로는 변수 바인딩 없이 raw hex(#929292)로 하드코딩돼 있던 것을 이번에 발견해 — `color/bg-disabled` 변수에 정식 바인딩 처리했다(재발 방지: 이제 향후 alias가 또 바뀌어도 스와치가 자동 갱신됨, 이전엔 수동 갱신 필요했던 결함). `color/gray/350` 자체는 이미 0-12/0-14/0-23절에서 Primitives 정식 그리드(`95:44`)에 편입 완료돼 있어 이번에 신규로 추가한 스와치는 없다(재확인만, "신규 섹션 분리" 재발 없음).

**2) Icon Button(`259:613`)/Row Action Button(`260:95`) Disabled variant 색 토큰 통일**: 기존 9-5절 opacity 공식(컨테이너 opacity=1, 배경 fill/보더 stroke 페인트 opacity만 0.5, 아이콘 자식 opacity 0.85, boundVariable 없거나 부분적)을 걷어내고, 나머지 4개 컴포넌트(NeoBtn/Button/Table Row Action/Checkbox)와 동일한 색 토큰 공식(배경=`color/bg-disabled`, 보더=`color/border-disabled`, 아이콘=`color/text-disabled`, opacity 전부 1)으로 전환했다. Input 2종(NeoInput/CornerInput)만 여전히 예외(텍스트는 `color/ink/900` 유지) — 이번 작업 대상 아님, 재확인만.

- **Icon Button Disabled**(`284:1042`, Type=Close 단일): 컨테이너 fill(raw 흰색, opacity0.5, unbound) → `color/bg-disabled`(`VariableID:643:2`) opacity1. 컨테이너 stroke(`color/ink/900` `VariableID:95:9` opacity0.5) → `color/border-disabled`(`VariableID:643:3`) opacity1. 자식 Pixel/Close 인스턴스(`284:1043`) opacity 0.85→1. 인스턴스 내부 Vector(`I284:1043;255:106`)의 stroke(raw ink #1A1A1A) → `color/text-disabled`(`VariableID:643:4`) opacity1로 리바인딩.
- **Row Action Button Disabled — Neutral**(`284:286`): 컨테이너 fill(raw 흰색 opacity0.5) → `color/bg-disabled` opacity1. 컨테이너 stroke(`component/row-action-button-border-neutral` `VariableID:269:671` opacity0.5) → `color/border-disabled` opacity1. Pixel/Edit 인스턴스(`284:287`) opacity 0.85→1, 그 내부 Vector 17개(fills, raw ink/800 #1C1F21) 전부 → `color/text-disabled` opacity1로 리바인딩.
- **Row Action Button Disabled — Danger**(`284:294`): 컨테이너 fill(raw 흰색 opacity0.5) → `color/bg-disabled` opacity1. 컨테이너 stroke(`color/coral/500` `VariableID:95:7` opacity0.5) → `color/border-disabled` opacity1(Style 무관하게 통일 — Default에서 Danger가 coral 보더를 쓰던 것과 달리 Disabled는 Neutral과 동일한 무채색 보더가 된다, 다른 4개 컴포넌트의 기존 패턴과 일치). Pixel/Delete 인스턴스(`284:295`) opacity 0.85→1, 그 내부 Vector 39개(fills, raw ink/800) 전부 → `color/text-disabled` opacity1로 리바인딩.
- **raw hex 재입력 없음** — 전부 `figma.variables.setBoundVariableForPaint`로 기존 변수에 리바인딩만 수행.

**스펙 시트**: `Spec — Icon Button`(`343:653`)/`Spec — Row Action Button`(`343:697`) 둘 다 인스턴스 기반 그리드라 재작성 없이 자동 반영됨을 `get_screenshot`으로 확인 — 신규 셀 추가나 레이아웃 변경 불필요.

**자체 재대조(design-systems 규칙, 생략 불가)**: 5개 신규 리바인딩 노드(Icon Button 컨테이너+내부 Vector 1개, Row Action Button Neutral 컨테이너+Vector 17개, Danger 컨테이너+Vector 39개) 전부 수정 직후 `use_figma` 읽기 전용으로 재조회해 boundVariable이 `VariableID:643:2/3/4`와 정확히 일치하고 opacity가 전부 1임을 확인했다. `get_screenshot`으로 Icon Button(`259:613`)/Row Action Button(`260:95`) ComponentSet 전체와 6개 스펙 시트(NeoBtn/Button/Table Row Action/Checkbox/NeoInput/CornerInput)를 재확인해 8개 컴포넌트(Input 2종 제외) Disabled가 시각적으로 통일된 밝은 회색 룩임을 확인했다.

### 0-25. NeoBtn Amber/Teal 레거시 해제 — Stage2 오기록 정정 (2026-07-16)

**배경**: 메인 세션이 확정 디자인 8개 프레임(`501:2505` 하위 — main/main-수정/main-삭제/main-검색없음/Join/login/login-알림창/main-알림창) 전체를 `use_figma`로 직접 정밀 대조한 결과, 이름이 "NeoBtn"인 노드가 총 20개 발견됐고 실제 사용된 색상은 정확히 4가지뿐이었다: 검정(`#1a1a1a`, "로그아웃"), 코랄(`#ff5a76`, "검색"), 네이비(`#074d7b`, "전체"), 스카이(`#1395e6`, "추가"). **Amber와 Teal은 이 확정 디자인 어디에도 등장하지 않는다.**

이 문서의 0-20절 "Stage2 NeoBtn Amber 리바인딩" 기록(NeoBtn Style=Amber 8 variant의 배경을 amber/500→`color/bg-cta-amber`로 리바인딩했다는 기록)은 **근거 없는 작업이었음이 확인됐다** — 실제로 확정 디자인에서 amber(#ffce2c)가 쓰이는 곳은 NeoBtn이 아니라 별도 컴포넌트 **Button**(`259:609`, 가입하기/로그인 버튼)이었다. NeoBtn의 Style=Amber/Teal 자체는 구 확정 디자인 세트(`248:11689`, 0-20절에서 신규 세트로 교체된 뒤 14-1절에서 완전히 삭제됨)를 소스로 초기 추출됐던 것으로 추정되며, 신규 확정 세트(`501:2505`)로 교체된 뒤에는 근거가 사라졌는데도 정리되지 않고 남아 있었다. Button(`259:609`)의 Amber는 이번 작업과 무관 — 실제 확정 디자인 근거가 있는 정상 컴포넌트라 전혀 건드리지 않았다.

**확정 디자인 NeoBtn 4색상표**:

| Style | Hex | 확정 디자인 용도 |
|---|---|---|
| Neutral | `#1a1a1a`(ink 보더, 흰 배경) | 로그아웃 등 보조 액션 |
| Coral | `#ff5a76` | 검색 |
| Navy | `#074d7b` | 전체(필터) |
| Sky | `#1395e6` | 추가 |

**절차 — 표준 "레거시 컴포넌트 해제" 순서(0-7절 8항 준수)**: ① NeoBtn(`259:126`) 전체 60 variant 자식을 raw script로 조회해 Style=Amber(12: `259:110`/`259:118`/`284:111`/`284:113`/`284:115`/`284:117`/`284:119`/`284:151`/`284:153`/`284:155`/`284:157`/`284:159`)/Style=Teal(12: `259:112`/`259:120`/`284:121`/`284:123`/`284:125`/`284:127`/`284:129`/`284:161`/`284:163`/`284:165`/`284:167`/`284:169`) 24개 노드 ID 확정. ② 파일 전체 29개 페이지(순차 순회, 병렬 호출 금지 원칙 준수)에서 이 24개를 mainComponent로 참조하는 INSTANCE를 전수 검색한 결과 **정확히 24개 발견, 전부 `Component Specs` 페이지(`342:2`)의 `Spec — NeoBtn`(`342:3`) 스펙 시트 셀 안에서만 참조**됐다(확정 디자인 8프레임 `501:2505` 내부 참조는 0건 — 정지 조건 미해당, 정상 경로로 진행). ③ 24개 인스턴스 전부 `detachInstance()`로 분리(시각 내용 보존, 신규 FRAME ID `784:829`~`784:879` 범위). 재검색 결과 24개 컴포넌트를 참조하는 INSTANCE 0건 확인. ④ 24개 variant COMPONENT를 표준 절차(동일 시각 속성의 새 FRAME 생성 → 자식 이동 → 원본 COMPONENT `remove()`)로 전환, Button 페이지(`97:8`)에 신규 컨테이너 `❌ 폐기 — NeoBtn Amber/Teal (확정 디자인 근거 없음, 2026-07-16 정정)`(`784:940`, Style=Amber 12개 담은 `784:941` 행 + Style=Teal 12개 담은 `784:942` 행)로 이전. `get_screenshot`으로 24개 프레임 전부 원래 색상·텍스트("검색")가 시각적으로 그대로 보존됨을 확인.

**결과**: NeoBtn ComponentSet(`259:126`) variant 개수 **60→36**, `componentPropertyDefinitions.Style.variantOptions`가 `["Coral","Neutral","Sky","Navy"]`로 정확히 4개만 남음을 재조회로 확인(Amber/Teal 완전히 제거).

**스펙 시트 갱신**: `Spec — NeoBtn`(`342:3`)에서 Amber/Teal에 해당하는 Row 4개(`342:21` Amber/Default, `342:48` Teal/Default, `342:129` Amber/Compact, `342:156` Teal/Compact)를 그리드에서 완전히 제거(2-5번 규칙 — 실제 variant 상태와 항상 일치). Grid(`342:6`)/Spec 루트(`342:3`) 모두 기존부터 VERTICAL auto-layout AUTO/AUTO(hug)라 자식 제거만으로 자동 리플로우·리사이즈됨(수동 크기 조정 불필요), `clipsContent`는 이미 두 컨테이너 모두 `false`였음을 재확인(추가 조치 불필요). 남은 6개 Row(Coral/Default, Neutral/Default, Coral/Compact, Neutral/Compact, Sky/Default, Navy/Default) × 6열 = 36칸이 잘림·겹침 없이 정상 렌더링됨을 `get_screenshot`으로 확인. 설명 텍스트(`342:5`)를 이번 정정 배경 + 4색상표 + "36 variant"로 전면 갱신.

**손대지 않은 것**: Button(`259:609`)의 Amber 6 variant(전부 무수정), `color/bg-cta-amber`(`VariableID:615:133`) 토큰 자체(Button/Card AccentStrip/Icon-Alert/Checkbox Checked에서 계속 유효하게 사용 중이라 삭제하지 않음), 확정 디자인 8개 프레임(`501:2505` 하위, 읽기 전용 열람도 하지 않았다 — 메인 세션이 이미 정밀 대조를 완료해 전달했으므로 중복 열람 불필요).

**7-2절 갱신**: "NeoBtn/Button Amber Hover/Press 블렌드 raw값 미재계산" TODO를 "Button Amber Hover/Press 블렌드 raw값 미재계산"으로 범위 축소(NeoBtn은 Amber 자체가 없어짐에 따라 대상에서 제외).

**덤 발견(이번 작업 범위 밖, 손대지 않음)**: 헤더 "로그아웃" NeoBtn(main 프레임 인스턴스, 0-20절에 이미 기록된 `501:6373`)이 순수 검정(#1a1a1a) 배경인데, 이번에 재확인한 NeoBtn Style=Neutral(흰 배경+ink 보더)과 정확히 일치하지 않는다(Neutral은 검정 배경이 아니라 흰 배경이다) — 이 갭은 0-20절 "미해결 관찰 2건"과 7-2절 TODO에 이미 기록돼 있던 사항으로, 이번 라운드에서 새로 발견한 것이 아니라 재확인만 했다. 이번 작업 범위(Amber/Teal 해제) 밖이므로 컴포넌트 마스터·인스턴스 어느 쪽도 손대지 않았다.

원본 확정 8개 프레임(`501:2505` 하위)은 이번 라운드에서 열람하지 않았다(메인 세션이 이미 실측을 완료해 전달) — 무수정.

### 0-26. Checkbox 체크마크 리토피트 — raw VECTOR → 등록 Icon 컴포넌트 INSTANCE (색상 무변경, 2026-07-16) ※ 21절(2026-07-16) 재조사로 이 "색상 무변경" 판단은 뒤집힘 — 체크마크는 이후 `color/text-inverse`(흰색)로 재바인딩됨, 이 절 하단 각주 참고

**배경**: 사용자가 컴포넌트 조립 표준 순서를 확정했다 — "아이콘 먼저 등록하고 그 아이콘을 끌고와서 부품으로 조립한 다음, 텍스트 등과 합쳐서 컴포넌트를 만든다"(`.claude/agents/design-systems.md` "컴포넌트 조립 순서" 판단기준에 명문화). Checkbox(`474:899`)의 체크마크는 이 원칙과 달리 raw VECTOR(`474:888`, State=Checked variant 내부)로 컴포넌트 안에 직접 그려져 있던 예외였다 — 이번 라운드에서 정식 절차대로 재조립했다.

**1) 라이브 재검증(1단계)**: `474:899`의 4개 State variant(Default/Checked/Focus/Disabled) 전체를 `use_figma` 읽기 전용으로 순회한 결과, 체크마크/VECTOR 노드는 `474:888`(State=Checked 전용) 단 1개뿐임을 확인했다 — 문서 기록과 일치, Default/Focus/Disabled에는 체크마크 자체가 없다(Focus는 `474:888`이 아니라 별도 `FocusRing` RECTANGLE 자식만 가짐).

**2) 원화 실측 정정**: graphic-designer가 리토피트 착수 전 `474:888`을 라이브로 재실측한 결과, 기존 0-17절 표의 "weight2" 기록은 오기였다 — 실측값은 `strokeWeight` **3**, `strokeCap`/`strokeJoin` ROUND, `vectorPaths` `"M 0 4 L 3 7 L 8 0"`, stroke `#1a1a1a`(바인딩 `color/ink/900`). 값 자체는 애초부터 3이었고 문서 기록만 오기였다 — 0-17절 표에 정정 각주 추가(위 참고), 원 기록은 삭제하지 않고 보존. **⚠ 2026-07-16 후속 정정(21절)**: 여기 기록된 stroke 색(`#1a1a1a`, `color/ink/900`)은 이 시점(0-26절, 리토피트 착수 직전) 기준 관찰이며, 이후 21절 재조사로 `color/text-inverse`(#FFFFFF, 흰색)로 재바인딩됐다 — 현재 유효한 값은 흰색이다.

**3) 아이콘 등록**: graphic-designer가 Icons 페이지(`96:7`)에 그린 raw FRAME `PixelCheck`(`814:2`, 자식 VECTOR `814:3`, x=1361/y=403, 8×7, weight3/ROUND, stroke `#1a1a1a` 평값)를 `createComponentFromNode`로 `Pixel/Check`(`815:2`) 정식 Icon 컴포넌트로 등록했다. 좌표·자식 노드 ID(`814:3`)·구성은 원화 그대로 승계(형태 변형 없음). 트랙은 `Pixel/*`(graphic-designer가 이미 판단해 인계, 4절에 반영).

**4) Checkbox 교체**: State=Checked의 Box(`474:886`) 안에 `Pixel/Check`의 INSTANCE(`815:3`)를 생성해 raw VECTOR와 정확히 동일한 위치(x=3,y=3)·크기(8×7)로 배치하고, 내부 vector(`I815:3;814:3`)의 stroke를 `color/ink/900`(`VariableID:95:9`)에 바인딩(기존과 동일한 색상 바인딩 유지)한 뒤, 기존 raw VECTOR(`474:888`)를 제거했다. **색상은 변경하지 않았다** — 이번 라운드는 순수 구조 교체(raw vector→instance)로 범위를 엄격히 지켰다. **⚠ 2026-07-16 후속 정정(21절)**: 이 "색상 무변경" 판단은 이후 21절 재조사로 뒤집혔다 — 체크마크 stroke는 이후 `color/ink/900`(검정)→`color/text-inverse`(#FFFFFF, 흰색)로 재바인딩됐다. 이 절(0-26절) 시점 기준으로는 구조 교체만 하고 색상은 실제로 손대지 않은 것이 사실관계상 정확하나, 이후 라운드에서 색상도 변경됐음을 명시한다 — 현재 유효한 값은 흰색이다.

**5) 검증**:
- 자체 재대조: 신규 인스턴스 내부 vector의 `strokeWeight`(3)/`strokeAlign`(CENTER)/`strokeCap`(ROUND)/`strokeJoin`(ROUND)/`vectorPaths`(`"M 0 4 L 3 7 L 8 0"`)/`boundVariables.strokes`(`VariableID:95:9`) 전부 교체 전 `474:888` 실측값과 정확히 일치함을 재조회로 확인. **⚠ 2026-07-16 후속 정정(21절)**: 이 `boundVariables.strokes`(`VariableID:95:9`, `color/ink/900`) 검증 결과는 이 시점(0-26절) 기준이며, 이후 21절에서 `VariableID:219:2`(`color/text-inverse`, 흰색)로 재바인딩됐다 — 현재 유효한 바인딩은 text-inverse다.
- `Spec — Checkbox`(`475:762`)를 `get_screenshot`으로 재확인 — 인스턴스 기반 4칸 그리드라 자동 반영됨, 4칸 전부 잘림·깨짐 없이 정상 렌더링(Checked 셀 체크마크 정상 표시).
- 파일 전체 29개 페이지를 순차 순회(병렬 호출 없음)해 Checkbox(`474:899`) 4개 variant를 참조하는 INSTANCE를 전수 검색한 결과 정확히 4개, 전부 `Component Specs` 페이지(`342:2`)의 스펙 시트 데모 셀(`475:767`/`475:772`/`475:778`/`475:783`)뿐 — 다른 화면·확정 프레임에는 참조 0건.
- 확정 디자인 8프레임(`501:2505`)은 이번 라운드에서 열람하지 않았다(작업과 무관, 원화 자체가 이미 확정 프레임 밖 리토피트 대상).

**결론**: 향후 아이콘이 포함된 컴포넌트를 새로 만들 때도 "아이콘 먼저 등록 → INSTANCE로 부품화 → 텍스트 등과 조립" 순서를 예외 없이 따른다.

### 0-27. 화면 조립 시 raw hex로 남아있던 흰색/검정을 기존 토큰으로 리바인딩 (2026-07-17, 사용자 긴급 지적)

**배경**: 사용자가 "흰색과 검은색도 컬러시스템에 넣어. 왜 컬러토큰으로 화면조립할때 안썻는지 모르겠어"라고 지적했다. `color/gray/0`(흰색, `VariableID:95:10`)/`color/ink/900`(검정, `VariableID:95:9`)/`color/text-inverse`(흰 텍스트, `VariableID:219:2`)는 이미 전부 등록돼 있어 신규 토큰은 만들지 않았다 — 오늘 새로 조립된 화면 중 이 토큰에 물리지 않고 raw hex(`#ffffff`/`#1a1a1a`)로 남아있던 노드만 찾아 기존 토큰으로 리바인딩했다.

**범위 제외(무수정 확인)**: `934:2` 페이지의 원본 3프레임(Join `935:33`, login `936:1042`, login-알림창 `936:1191`) — 사용자가 Figma에서 직접 수정한 프레임이라 이번 작업 전체에서 열람도 하지 않았다.

**작업 대상 8프레임과 리바인딩 노드 수**:

| 프레임 | nodeId | 리바인딩 노드 수 | 내역 |
|---|---|---|---|
| login-비밀번호재설정-1단계 | `995:303` | 18 | 배경 장식 Rectangle 13개(흰색→`color/gray/0`) + 눈 아이콘 INSTANCE 내부 VECTOR 5개(검정→`color/ink/900`) |
| login-비밀번호재설정-2단계 | `996:376` | 18 | 동일 구성(13+5) |
| login-비밀번호재설정-성공 | `996:2575` | 18 | 동일 구성(13+5) |
| Join-실패배너(409/422) | `996:2713` | 17 | Rectangle 13개 + VECTOR 4개 |
| Join-성공안내 | `996:3014` | 17 | Rectangle 13개 + VECTOR 4개 |
| main-오류배너(409/422/404 공용) | `996:3165` | 0 | 이미 전부 토큰 바인딩 상태 — 리바인딩 대상 없음 |
| 카테고리 삭제 확인 | `1001:1594` | 5 | 프레임 자체 배경 fill 1개(흰색→`color/gray/0`) + 아이콘 INSTANCE 내부 VECTOR 4개(검정→`color/ink/900`) |
| 카테고리 이름 수정 | `1002:1611` | 5 | 동일 구성(1+4) |

**합계 98개 노드/프로퍼티 리바인딩** — 배경·프레임 fill은 전부 `color/gray/0`, 아이콘 벡터 stroke는 전부 `color/ink/900`. 이번 대상 8프레임에는 흰 텍스트(`color/text-inverse` 대상)나 검정 텍스트 fill로 남아있던 raw 노드는 없었다(전수 스캔 결과 텍스트 노드 매치 0건) — 따라서 `color/text-inverse` 리바인딩은 이번 라운드에 해당 사항 없음, 신규 적용도 없음.

**⚠ 실측 특이사항 — 중첩 INSTANCE 자식 접근**: 아이콘(눈 토글/경고 등) VECTOR 15개는 `I995:2485;952:32;950:4` 형태의 중첩 인스턴스 경로 ID였다. 이 중 3개 프레임(995:303/996:376/996:2575)의 15개 노드는 `figma.getNodeByIdAsync(id)`로 직접 조회 시 "not found" 오류가 났다 — 프레임 루트부터 재귀 순회로 노드 레퍼런스를 직접 찾아 그 레퍼런스에 `setBoundVariableForPaint`를 적용해 해결했다(다른 5개 프레임의 동일 패턴 노드는 `getNodeByIdAsync`로 정상 조회됨 — 원인 불명이나 재귀 순회 방식이 항상 안전하게 동작함을 확인).

**검증**: 리바인딩 직후 8프레임 전체를 다시 read-only 전수 스캔해 raw white/black 미바인딩 노드가 **0건**임을 확인했다. `995:303`/`1001:1594` 2곳을 `get_screenshot`으로 재확인해 레이아웃·색상이 리바인딩 전과 시각적으로 동일함을 확인했다(값 자체는 변경하지 않고 바인딩만 추가했으므로 렌더링 결과 불변). `934:2` 원본 3프레임은 이번 작업 전체에서 조회조차 하지 않았다.

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

**신규(Stage2/0-20절, 2026-07-15, 두 번째 확정 디자인 세트 8프레임 재실측, 6개)**: `color/sky/500`(#1395E6, `VariableID:615:122`) `color/navy/700`(#074D7B, `VariableID:615:123`) `color/amber/600`(#FFCE2C, `VariableID:615:124`) `color/paleblue/100`(#D3ECFB, `VariableID:615:125`) `color/paleblue/50`(#F5FAFD, `VariableID:615:126`) `color/gray/375`(#AAAAAA, `VariableID:615:127`) — 전부 scope=[] 숨김.

**신규(0-22/0-23절, 2026-07-16, Disabled 전용)**: `color/gray/425`(#929292, `VariableID:646:2`, scope=[] 숨김) — 기존 gray/400·gray/450 사이 신규 스텝. 최초 gray/450(#888888)→이 스텝으로 교체(0-23절), **0-24절에서 다시 `color/gray/350`으로 교체되며 현재는 어떤 semantic에도 alias되지 않는 orphan 상태**(삭제하지 않고 보존).

**변경(0-24절, 2026-07-16)**: `color/bg-disabled`의 alias 대상이 `color/gray/425`→`color/gray/350`(#BBBBBB, `VariableID:434:4`, 0-12절에서 이미 등록된 기존 primitive)으로 교체됐다 — 신규 primitive 추가 없이 재사용. 사용자 승인으로 WCAG 1.4.11 비텍스트 3:1 기준 미달(1.92:1)을 감수한 결정(경위는 0-24절 참고).

### 1-2. Semantic Colors (`VariableCollectionId:95:16`, mode `95:1`)

카테고리 팔레트(CatBadge 정식 채택 — 2절 참고): `color/category/friend-bg/-border/-text` `color/category/family-bg/-border/-text` `color/category/other-bg/-border/-text` `color/category/company-bg/-border/-text` (각 bg=FRAME_FILL/SHAPE_FILL, border=STROKE_COLOR, text=TEXT_FILL). **0-9절 갱신**: 이 4쌍은 이제 CatBadge뿐 아니라 TypeSelector(`257:28`)의 Selected 상태 4종(Friend/Family/Other/Company)에도 직접 바인딩되는 공용 카테고리 색 토큰이다 — 두 컴포넌트가 같은 토큰을 공유한다.

뮤트 텍스트 역할: `color/text-muted-strong`(→gray/650 #555, 전화번호) `color/text-muted`(→gray/500 #777, 주소) `color/text-muted-subtle`(→gray/450 #888, 마이크로 라벨/TypeSelector 미선택 텍스트) — **⚠ WCAG 검증 결과, 아래 3절 대비 계산 참고: muted-strong만 PASS, muted/muted-subtle는 원본 확정 디자인에 이미 내재된 미달값(→7-1절에서 RESOLVED로 종결, 사용자 확정)**.

기타: `color/border-neutral`(→ink, 취소/로그아웃류 아웃라인 버튼 보더) `color/background-success`(→mint/100, 토스트 성공) `color/background-error`(→coral/100, 배너 에러).

**신규(0-4절, 2026-07-14)**: `color/text-link`(→teal/500 #17A398, scope TEXT_FILL, `VariableID:340:3`) — Link 컴포넌트/Body/Link 텍스트 스타일 전용. 기존 `color/text-accent`(teal/700 별칭, 레거시)와는 값이 달라 재사용하지 않고 신규로 만들었다.

**신규(0-5절, 2026-07-14)**: `color/border-divider-warm`(→beige/200 #EDE6D8, scope STROKE_COLOR, `VariableID:350:3`) — Contact Row(`351:299`) 행 하단 구분선 전용(strokeBottomWeight만 1, 나머지 3변 0).

**신규(0-10절, 2026-07-14)**: `color/border-error`(→coral/500 #FF5A76, scope STROKE_COLOR, `VariableID:378:2`), `color/text-error`(→coral/900 #A8003B, scope TEXT_FILL, `VariableID:378:3`) — NeoInput/CornerInput Error variant 전용.

**신규(0-11절, 2026-07-15 재확인)**: `color/text-placeholder`(→gray/300 #CCCCCC, scope TEXT_FILL, `VariableID:398:3`) — NeoInput/CornerInput/NeoSelect Placeholder 텍스트 공용(이미 등록돼 있던 것을 재확인). **0-12절 갱신**: NeoInput만 별도로 `color/text-placeholder-input`(→gray/350 #BBBBBB, scope TEXT_FILL, `VariableID:434:5`)로 분리됐다 — CornerInput/NeoSelect는 `color/text-placeholder`(#CCCCCC) 유지.

**신규(9-6절, 2026-07-15)**: `color/bg-hover-muted`(→gray/150 #F1F1F1, scope `FRAME_FILL`/`SHAPE_FILL`, `VariableID:432:3`) — NeoSelect Open 옵션 hover 배경 전용, 흰 배경류 컴포넌트의 옅은 hover 배경.

**신규(Stage2/0-20절, 2026-07-15, 7개, 전부 위 1-1절 Stage2 Primitives를 alias)**: `color/bg-brand-blue`(→sky/500, scope `FRAME_FILL`/`SHAPE_FILL`, `VariableID:615:128`) `color/bg-accent-navy`(→navy/700, scope `FRAME_FILL`/`SHAPE_FILL`, `VariableID:615:129`) `color/text-link-navy`(→navy/700, scope `TEXT_FILL`, `VariableID:615:130`) `color/border-divider-cool`(→paleblue/100, scope `STROKE_COLOR`, `VariableID:615:131`) `color/bg-row-alt`(→paleblue/50, scope `FRAME_FILL`/`SHAPE_FILL`, `VariableID:615:132`) `color/bg-cta-amber`(→amber/600, scope `FRAME_FILL`/`SHAPE_FILL`, `VariableID:615:133`) `color/text-placeholder-strong`(→gray/375, scope `TEXT_FILL`, `VariableID:615:134`). 실제 컴포넌트 바인딩 현황은 0-20절 표 참고.

**신규(0-22/0-23절, 2026-07-16, Disabled 전용, 3개, 0-24절에서 bg-disabled alias 재조정)**: `color/bg-disabled`(→**gray/350 #BBBBBB**(0-24절 최종값, 구 gray/425 #929292), scope `FRAME_FILL`/`SHAPE_FILL`, `VariableID:643:2`) `color/border-disabled`(→gray/600 #5C6366, scope `STROKE_COLOR`, `VariableID:643:3`) `color/text-disabled`(→gray/650 #555555, scope `TEXT_FILL`, `VariableID:643:4`) — **NeoBtn/Button/Table Row Action/Checkbox/NeoInput/CornerInput/Icon Button/Row Action Button(0-24절에서 추가) Disabled 상태 공용**(Input 2종은 텍스트만 예외). WCAG 대비값(흰 배경 기준, 직접 계산)은 3절 참고.

**신규(13절, 2026-07-16, 35차 — 확정 디자인 8프레임 전수 대조 P14)**: `color/text-muted-toast`(→gray/600 #5C6366, scope `TEXT_FILL`, `VariableID:702:19`) — Toast Success subtitle(`263:45`) 전용, 기존 primitive `color/gray/600`을 alias(신규 원시값 없음). **레거시 토큰 첫 실사용(13절 P1)**: 같은 라운드에서 `color/text-inverse`(`VariableID:219:2`, 8절 Legacy 목록에 있던 미사용 토큰)가 NeoBtn Style=Navy 텍스트 색으로 처음 실제 바인딩되며 활성 사용을 시작했다(각주는 8절 참고).

### 1-3. Component Tokens (`VariableCollectionId:97:2`, mode `97:0`)

기존 재사용(변경 없음): `component/button-bg-primary`(teal) `component/button-bg-danger`(coral) `component/button-bg-amber`(amber) — 이번 확정 디자인의 NeoBtn/Button Style=Teal/Coral/Amber에 그대로 재사용, 신규 선언 없음. **⚠ 2026-07-16 갱신(0-25절)**: 이 문단은 최초 추출 시점(0절) 기준 기록이다. 이후 NeoBtn의 Style=Teal/Amber 24 variant는 확정 디자인 근거가 없는 구 잔재로 확인되어 레거시 해제됐다(현재 NeoBtn Style=Coral/Neutral/Sky/Navy/Ink 5개, Teal 없음 — Ink는 18절 신규). Teal은 애초 NeoBtn 전용이었고 Button(`259:609`)에는 Teal이 없었다(Button은 Amber/Coral/Neutral만) — 따라서 현재는 `component/button-bg-primary`(teal)가 NeoBtn/Button 어느 쪽에도 바인딩되지 않는다. `component/button-bg-danger`(coral)/`component/button-bg-amber`(amber)는 이 문단 서술대로 계속 유효(Coral은 NeoBtn·Button 둘 다, Amber는 Button만).

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
- NeoBtn/Button Style=Amber/Teal/Coral + ink 텍스트: 기존 "브랜드색 배경 위 텍스트=ink 고정" 규칙 재사용, 기존 검증된 5.3~11:1 범위 그대로 PASS. **⚠ 2026-07-16 갱신(0-25절)**: NeoBtn의 Style=Teal은 이후 확정 디자인 근거가 없는 구 잔재로 확인되어 레거시 해제됐다(Teal은 애초 NeoBtn 전용, Button엔 없었음). 이 PASS 판정 자체는 당시 실측 근거로 유효했던 기록으로 보존한다 — 현재 유효한 NeoBtn Style은 Coral/Neutral/Sky/Navy/Ink(18절)이며, Sky/Navy/Ink의 WCAG 값은 각각 0-20절/13절 P1/18절에 별도 계산돼 있다.
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
- **신규(0-20절, Stage2, 2026-07-15)**: `color/text-link-navy`(#074D7B) on 흰 배경 = **8.92:1 PASS**(12px Bold는 큰 텍스트 기준 미달이라 일반 4.5:1 기준 적용 — 기존 teal 3.12:1 미달값 대비 대폭 개선). `color/bg-accent-navy`(#074D7B) 배경 + 흰 텍스트(Sidebar Nav Item Active "전체" 등) = **8.92:1 PASS**. ink(#1A1A1A) on `color/bg-cta-amber`(#FFCE2C) = **11.70:1 PASS**(기존 amber/500 대비 근사, 기존 PASS 범위 유지). ink 보더(#1A1A1A) on `color/sky/500`(#1395E6, Checkbox Checked 박스 경계, WCAG 1.4.11 비텍스트 3:1 기준) = **5.36:1 PASS**. `color/border-divider-cool`/`color/bg-row-alt`는 장식·배경용이라 별도 기준 미적용, bg-row-alt(#F5FAFD) 위 기존 텍스트 대비는 순백 대비 <0.05 차이로 3절의 기존 판정에 실질적 영향 없음.
- **신규(0-22/0-23절, Disabled, 2026-07-16, 상대휘도 공식 직접 계산·재검증)**: `color/bg-disabled`(#929292) on 흰 배경 = **3.11:1**(WCAG 1.4.11 비텍스트 3:1 기준 PASS, 근소). `color/border-disabled`(#5C6366) on 흰 배경 = **6.12:1 PASS**. `color/text-disabled`(#555555, Checkbox 라벨 전용) on 흰 배경 = **7.45:1 PASS**(14px 이하 본문 4.5:1 기준). 참고: 최초 alias였던 `color/gray/450`(#888888)은 3.54:1이었으나 최종 alias `color/gray/425`(#929292)로 교체되며 3.11:1로 낮아짐 — 그래도 3:1 비텍스트 기준은 유지해 PASS. NeoInput/CornerInput Disabled 텍스트는 `color/text-disabled`가 아니라 `color/ink/900`(21:1 PASS)을 그대로 쓰므로 별도 계산 불필요.
- **신규(0-24절, 2026-07-16, bg-disabled 재조정 — 사용자 승인 WCAG 완화)**: `color/bg-disabled`가 `gray/425`(#929292)→`gray/350`(#BBBBBB)로 재조정되며 흰 배경 대비 **1.92:1**로 낮아졌다 — WCAG 1.4.11 비텍스트 3:1 기준 **미달**. **사용자가 "기준 무시하고 원하는 만큼 밝게"라고 명시적으로 확정 승인**해 이번 프로젝트 범위에서 완화 적용한다(개선 대상 아님, RESOLVED와 동일하게 취급). 부수 효과: `color/text-disabled`(#555555) on 새 bg = **3.88:1**(구 2.40:1 대비 개선), `color/ink/900`(#1A1A1A) on 새 bg = **9.06:1**(구 5.59:1 대비 개선) — 배경이 밝아지며 그 위 텍스트/아이콘 대비는 오히려 좋아졌다.

## 4. Icons (`96:7`)

**기존 8종 유지**(변경 없음): `Icon/Search` `Icon/Add` `Icon/Edit` `Icon/Delete` `Icon/Category` `Icon/Logout` `Icon/Alert` `Icon/User` — 확정 디자인에서도 `Icon/Alert`(토스트/배너)와 `Icon/User`(아바타)가 그대로 재사용됨을 확인. **(2026-07-14 문서 동기화 재확인)** graphic-designer가 "Icons" 페이지를 직접 재실측(`use_figma`)한 결과 8종 전부 strokeWeight 3px 균일로 원상태 그대로다 — 상세는 `docs/design/graphic-assets.md` 참고. **0-20절(Stage2, 2026-07-15)**: `Icon/Alert`(`96:41`) 강조 원(Ellipse `96:38`) 배경만 raw amber(#FFCB47, 미바인딩)→`color/bg-cta-amber`(#FFCE2C) 리바인딩, 나머지 7종은 무수정. **⚠ 30절(2026-07-17)**: `Icon/Category`(`96:31`)의 주 실루엣 fill(`96:29`/`96:30`)이 `color/teal/500`→`color/sky/500`(`VariableID:615:122`, #1395E6)로 리바인딩됨 — 상세는 아래 30절 참고.

**신규 12종** (`Pixel/*` 네임스페이스, 확정 프레임에서 비파괴적으로 clone 후 `createComponentFromNode`로 컴포넌트화 — 원본은 전혀 수정하지 않음): `Pixel/Star`(12px, 로고 심볼 내부) `Pixel/Search`(15px, **⚠ 32절(2026-07-17) 갱신**: fill `color/teal/500`→`color/sky/500`으로 리바인딩됨, 상세는 아래 32절 참고) `Pixel/Plus`(9px) `Pixel/Logout`(12px) `Pixel/Edit`(14px) `Pixel/Delete`(14px) `Pixel/Close`(10px, 모달 닫기) `Pixel/Warning`(16px, 삭제 경고) `Pixel/NoResult`(40x44, 빈 검색결과 그래픽) `Pixel/Eye`(14x10, login 비밀번호 표시/숨김 토글) `Pixel/EyeOff`(**신규, 0-13절, 2026-07-15**, 14x10, `Pixel/Eye`와 짝을 이루는 "닫힌 눈" 실루엣, `415:892`) `Pixel/Check`(**신규, 0-26절, 2026-07-16**, 8×7, stroke-only vector weight3/ROUND, Checkbox 체크마크 아이콘화, `815:2`, graphic-designer 원화 `814:2` 기반). **2026-07-16 재대조(23절)**: `Pixel/NoResult`(`255:149`)의 몸통(돋보기 실루엣, 21개 vector)이 raw teal(#17A398, 미바인딩)에 남아 있던 것을 발견해 확정 프레임(`501:4218` 내부 `517:2722`) 실측값(#1395E6)에 맞춰 `color/sky/500`(`VariableID:615:122`)으로 리바인딩 완료 — 크랙 6개 vector는 원래도 코랄(#FF5A76)이라 무수정.

**신규 2종(34절, 2026-07-17, design-qa HIGH 결함 정정 — Button/NeoBtn 아이콘 슬롯 부재)**: `Pixel/ArrowRight`(`951:2`, 14×14, 잉크 #1a1a1a stroke 1.75, 2-vector 단순 화살표) — 확정 Join "가입하기"(`501:4855`)에서 clone, "로그인으로 돌아가기"(`501:4890`)/main-수정 "저장하기"(`501:3628`) 3곳과 vectorPaths·strokeWeight·색 전부 hex 단위로 동일함을 실측 확인. `Pixel/ArrowEnter`(`951:3`, 14×14, 잉크 #1a1a1a stroke 1.75, 3-vector 우측 rounded bracket+chevron+shaft) — login "로그인" 버튼(`501:5103`)에서만 관찰된 별도 형태, Pixel/ArrowRight와 실측 결과 형태가 달라 별도 등록. 둘 다 원본 비파괴적 clone(형태 변형 없음), Button/NeoBtn Leading Icon 슬롯의 기본/대안 스왑 아이콘. 상세는 아래 34절 참고.

## 5. 컴포넌트 (확정 디자인 기준, 신규 등록)

**스펙 시트 안내(0-4/0-5절)**: 아래 표의 컴포넌트 11개(NeoBtn~CornerInput 9개 + Link + Contact Row) 전부 `"Component Specs"` 페이지(`342:2`, FOUNDATIONS 구역, Icons 바로 뒤)에 제목+설명+전체 variant 그리드+상태별 라벨을 갖춘 스펙 시트 프레임이 있다.

| 컴포넌트 | 페이지 | ComponentSet ID | Variant | 스펙 시트 프레임 ID |
|---|---|---|---|---|
| CatBadge | Badge `102:3` | `256:17` | Category=Friend/Family/Other/Company (4). CatBadge 팔레트(2절) 바인딩. | (스펙 시트 없음) |
| TypeSelector | Badge `102:3` | `257:28` | Category(4) × State=Selected/Unselected/Focus(3) = **12 variant**(**0-15절, 2026-07-15**, 기존 16 variant에서 Focus 축을 State 열거형 값으로 소급 통합 — Selected+Focus=Yes 4개 삭제, Unselected+Focus=Yes 4개는 State=Focus로 이름만 정리). **0-9절**: Selected는 CatBadge 토큰 공유(2절 참고), Unselected/Focus는 전용 회색 토큰 유지. **0-19절**: 스펙 시트 `clipsContent` 회귀 정정(Focus 링 잘림 수정). | `343:1146` |
| Count Pill | Sidebar Nav Item `103:92` | `258:16` | State=Active(흰 배경, 그림자 없음)/Inactive(앰버 배경, Shadow/Hard-1). **13절(P5, 2026-07-16)**: Active(`258:12`)에 `Shadow/Hard-1` 신규 적용(배경/보더는 기존값 이미 프레임과 일치해 무수정). | (스펙 시트 없음) |
| Sidebar Nav Item | Sidebar Nav Item `103:92` | `258:29` | State=Active/Inactive/Focus = **3 variant**(**0-15절, 2026-07-15**, 기존 4 variant에서 Focus 축을 State 열거형 값으로 소급 통합 — Active+Focus=Yes 1개 삭제). **9-5절**: Focus(구 Inactive+Focus=Yes, `287:17`)는 3px ink OUTSIDE 스트로크로 링 구현, fills/strokes/effects 무수정 유지(⚠ 28-7/28-8/28-9절에서 변경됨, 위 참고). **0-20절(Stage2, 2026-07-15)**: State=Active(`258:17`) 배경 amber/500→`color/bg-accent-navy`(#074D7B) 리바인딩. **28절(2026-07-17)**: State=Active 텍스트(`258:18`) ink/900→`color/text-inverse`(#FFFFFF) 정정, State=Inactive 텍스트(`258:24`)도 동일 정정 + 배경(`258:23`) `fills=[]`→`color/gray/0`+opacity0.18(반투명 흰 오버레이) 정정. Count Pill(`258:21`/`258:27`)은 무수정. **28-7절(2026-07-17)**: State=Focus(`287:17`/`287:18`)도 9-1절 Focus 순수성 원칙에 따라 Inactive와 동일한 텍스트(`color/text-inverse`)·배경(`color/gray/0`+opacity0.18)으로 정정(28절 시점엔 예외 처리돼 어긋나 있었음). **28-8절**: Focus(`287:17`)에 남아있던 미문서화 잔여 흰 보더(raw, 1px) 제거 — Active/Inactive와 동일하게 `strokes: []`로 정정. **28-9절(2026-07-17)**: 확정 프레임(`501:6050`/`501:6055`) 실측대로 State=Active/Inactive/Focus 3개 variant 전부에 2px INSIDE `color/ink/900` 보더를 신규 추가(위 TODO 해소) + FocusRing-Ink(`574:1056`)의 raw hex(#1a1a1a) stroke도 `color/ink/900`에 정식 바인딩(NeoBtn FocusRing `549:43`과 동일 패턴). 새 보더(내측 2px)와 FocusRing(외측 3px OUTSIDE)은 1px 간격을 두고 충돌 없이 이중 링으로 렌더링됨을 스크린샷 확인. | `343:1106` |
| **Checkbox**(0-17절, 신규) | Checkbox(신규 페이지, `474:881`) | `474:899`(555×18) | State=Default(Unchecked)/Checked/Focus/Disabled = 4 variant. 로그인(`247:6666`) "☐ 로그인 상태 유지"(`247:6822`) 실측 기반, 14×14 Box(흰배경+2px ink 보더)+Label(`color/ink/900` opacity 0.5). TEXT 프로퍼티 `label`(기본값 "로그인 상태 유지"). **0-22/0-23절(Stage2-a, 2026-07-16)**: Disabled는 opacity 공식 대신 Box fill=`color/bg-disabled`(#929292)/stroke=`color/border-disabled`(#5C6366), Label fill=`color/text-disabled`(#555555)로 색 토큰 전환(opacity 전부 1). **13절(P12, 2026-07-16)**: Checked 체크마크(`474:888`) stroke `color/border-divider-cool`→`color/ink/900`(#1A1A1A)로 정정(login 인스턴스 `604:5954`의 흰색 로컬 오버라이드는 원본 프레임 기존 상태라 무수정 유지). **15-2절(2026-07-16, 배치4/4)**: variant 개수(4) 재확인, 스펙 시트 인스턴스 3개 `clipsContent=true`→`false` 정정, 설명 텍스트 stale 문구 갱신. **0-26절(2026-07-16)**: State=Checked(`474:886`)의 체크마크가 raw VECTOR(`474:888`)에서 신규 등록 `Pixel/Check`(`815:2`) 컴포넌트의 INSTANCE(`815:3`)로 교체됨(구조만 변경, 당시 색상은 `color/ink/900` 그대로 무변경이었음) — 컴포넌트 조립 순서 원칙(아이콘 먼저 등록 후 부품화) 준수. **⚠ 21절(2026-07-16) 최종 정정**: 위 13절 P12/15-2절의 "체크마크는 검정(`color/ink/900`) 유지"라는 결론은 이후 21절에서 뒤집혔다 — Box(`474:886`)가 이미 `color/sky/500`으로 확정 디자인과 일치해 있었다는 사실을 반영하지 못한 판단이었고, 실제로는 확정 디자인이 스카이블루 박스+흰색 체크마크 조합이라 체크마크도 **`color/text-inverse`(#FFFFFF, 흰색)로 최종 재바인딩**됐다. 현재 유효한 값은 흰색이다. 상세는 21절 참고. | `475:762` |
| NeoBtn | Button `97:8` | `259:126` | **18절(2026-07-16) 최종**: Style=Coral/Neutral/Sky/Navy/Ink × Size=Default/Compact(Sky/Navy는 Default만) × State=Default/Hover/Press/Focus/Disabled/Loading(9-2절) = **42 variant**. 확정 디자인 8프레임(`501:2505`) 재대조 결과 NeoBtn 실사용 5색상은 Neutral(#1a1a1a ink 보더, 흰 배경)/Coral(#ff5a76, 검색)/Navy(#074d7b, 전체)/Sky(#1395e6, 추가)/**Ink(#1a1a1a 배경+흰 텍스트+무보더, 로그아웃, 18절 신규)**뿐임이 확인됨. ~~Style=Amber/Teal(각 12 variant, 총 24)~~은 근거 없는 구 확정 세트 잔재로 확인되어 레거시 해제(detach 24 인스턴스 → COMPONENT→FRAME 전환, Button 페이지 `❌ 폐기 — NeoBtn Amber/Teal (확정 디자인 근거 없음, 2026-07-16 정정)` `784:940` 컨테이너로 이전 보존, 삭제 아님) — 상세는 0-25절. Amber(#ffce2c)의 실제 사용처는 Button(`259:609`)뿐이었다(0-20절 NeoBtn Amber 리바인딩 기록은 오류, 0-25절에서 정정). **0-22/0-23절(Stage2-a, 2026-07-16)**: Disabled variant는 opacity 공식 대신 배경=`color/bg-disabled`/보더(Neutral만)=`color/border-disabled` 색 토큰으로 전환(당시 8개 중 Amber/Teal 4개는 이후 0-25절에서 함께 제거됨, 현재 Coral/Neutral/Sky/Navy/Ink 7개 유지). **13절(P1/P11, 2026-07-16)**: `Style=Sky`(`712:2`)/`Style=Navy`(`712:4`) 전체 State 추가 완료(34차 배치, 7-2절 RESOLVED). **18절(2026-07-16)**: `Style=Ink`(Size=Compact 전용, `791:7`/`791:862`/`791:864`/`791:866`/`791:869`/`791:871`) State 6개 전부 신규 완성 — 헤더 "로그아웃" 버튼 실측 근거, Hover/Press는 베이스가 이미 ink라 white 방향 블렌드로 대체 적용(문서화된 예외). **34절(2026-07-17)**: ComponentSet 레벨에 `Show Leading Icon`(BOOLEAN, 기본 false)/`Leading Icon`(INSTANCE_SWAP, 기본 `Pixel/Plus` `255:30`) 프로퍼티 신규 추가, 전체 42 variant 각각에 index 0 위치 hidden 아이콘 인스턴스 배선 완료(variant 개수 자체는 42로 무변경). **⚠ 35절(2026-07-17) 정정**: Style=Sky의 텍스트가 확정 원본(`501:6423`)과 달리 `color/ink-900`에 잘못 바인딩돼 있어 Default/Hover/Press/Focus/Loading 5 State를 `color/text-inverse`로 리바인딩(Navy는 이미 정확했음). Sky/Navy 12개 variant 전부에 확정 원본(Sky `501:6423`/Navy `501:6358`) 실측대로 2px INSIDE 보더 추가(Disabled 2개=`color/border-disabled`, 나머지 10개=`color/ink/900`). padding/gap/font는 Coral/Neutral과 동일한 기존 값(16/8·gap6·Bold14)이 이미 정확해 변경하지 않음. **⚠ 36-2절(2026-07-17) 추가 정정**: Style=Coral도 35절과 동일 결함(확정 원본 `501:6406` "검색"은 2px ink 보더+흰 텍스트인데 마스터는 보더 없음+ink 텍스트)이 있었음이 확인되어, 12 variant 전부(Disabled 제외) 텍스트를 `color/text-inverse`로, 보더를 2px INSIDE `color/ink/900`(Disabled 2개는 `color/border-disabled`)로 정정 — 이제 Coral/Sky/Navy 전부 확정 원본과 일치. | `342:3` |
| Button | Button `97:8` | `259:609` | Style=Amber/Coral/Neutral × State=Default/Hover/Press/Focus/Disabled/Loading(9-2절) = 18. **0-4절**: login/Join 보조 버튼도 Neutral variant로 커버. **0-20절(Stage2, 2026-07-15)**: Amber Default/Focus/Disabled/Loading(4 variant) 동일 리바인딩. **0-22/0-23절(Stage2-a, 2026-07-16)**: 3개 Disabled variant 동일 색 토큰 전환. **13절(P11, 2026-07-16)**: Amber 6 variant 전체에 2px `color/ink/900` 보더 추가. **34절(2026-07-17)**: ComponentSet 레벨에 `Show Leading Icon`(BOOLEAN, 기본 false)/`Leading Icon`(INSTANCE_SWAP, 기본 `Pixel/ArrowRight` `951:2`) 프로퍼티 신규 추가, 전체 18 variant 각각에 index 0 위치 hidden 아이콘 인스턴스 배선 완료(variant 개수 자체는 18로 무변경). **⚠ 36-2절(2026-07-17) 정정**: Style=Coral도 확정 원본(`501:4211` "삭제하기") 재실측 결과 2px ink 보더+흰 텍스트 조합인데 마스터는 보더 없음+ink 텍스트였다 — 6 variant 전부(Disabled 제외) 텍스트를 `color/text-inverse`로, 보더를 2px INSIDE `color/ink/900`(Disabled는 `color/border-disabled`)로 정정. | `343:50` |
| Icon Button | Button `97:8` | `259:613` | Type=Close × State=Default/Hover/Press/Focus/Disabled(9-2절, Loading 제외) = 5. **0-24절(Stage2-d, 2026-07-16) RESOLVED**: Disabled(`284:1042`)를 NeoBtn/Button 등과 동일한 색 토큰 공식으로 전환 완료 — 배경=`color/bg-disabled`, 보더=`color/border-disabled`, 아이콘=`color/text-disabled`, opacity 전부 1. **13절(P6, 2026-07-16)**: 전체 5 State cornerRadius 10→`radius/none`(0). | `343:653` |
| Row Action Button | Table Row `103:3` | `260:95` | Style=Neutral/Danger × State=Default/Hover/Press/Focus/Disabled(9-2절, Loading 제외) = 10. **0-1절**: Neutral 보더=`component/row-action-button-border-neutral`(#1C1F21). **0-24절(Stage2-d, 2026-07-16) RESOLVED**: Disabled 2개(`284:286`/`284:294`)를 동일 색 토큰 공식으로 전환 완료(Danger도 Disabled에서는 무채색 보더로 통일). **13절(P2, 2026-07-16)**: Danger/Default(`260:53`) 배경 `color/gray/0`→`color/bg-cta-amber`, 보더 `color/coral/500`→`color/ink/900`로 재실측 반영(`border/hairline` 1px 유지) — 나머지 Danger State는 TODO(7-2절). | `343:697` |
| Table Row Action | Table Row `103:3` | `260:100` | Style=Neutral/Danger × State=Default/Hover/Press/Focus/Disabled(9-2절, Loading 제외) = 10. **0-1절**: 텍스트 10px 정정. **0-22/0-23절(Stage2-a, 2026-07-16)**: 2개 Disabled variant 배경=`color/bg-disabled`/보더=`color/border-disabled` 색 토큰 전환. | `343:1044` |
| **Contact Row**(0-5절) | Table Row `103:3` | `624:1070`(**0-20절, Stage2, 2026-07-15**, 구 단일 COMPONENT `351:299`→COMPONENT_SET로 승격) | Row=Default(`351:299`, 기존 ID 유지)/Alt(`624:1061`, 신규) = 2 variant. 이름/전화번호/주소/CatBadge/Table Row Action 조합, 774×47. TEXT 프로퍼티 `name`/`phone`/`address`. 하단 구분선 `color/border-divider-cool`(#D3ECFB, 리바인딩됨) 공통. Alt 배경만 `color/bg-row-alt`(#F5FAFD) — 짝수행 zebra striping. | `352:726` |
| NeoInput | Input `100:2` | `288:12` | Content=Filled/Placeholder × Error=No/Yes(4, State=Default) + State=Focus 2개(Content=Placeholder×Error=No 기반 1개, Content=Filled×Error=Yes 기반 1개) + State=Disabled 1개(Content=Filled×Error=No 기반, **0-22절, Stage2-b, 2026-07-16**) = **7 variant**(**0-15/0-16절, 2026-07-15**, Focus 축을 State 열거형 값으로 소급 통합 — Filled×Focus=Yes 2개 삭제 후 Error=Yes 조합만 복원). Placeholder 텍스트=`color/text-placeholder-input`(#BBBBBB, NeoInput 전용, 0-12절). Disabled는 배경/보더만 `color/bg-disabled`/`color/border-disabled`, 텍스트는 `color/ink/900` 그대로(Input은 display라 값을 뚜렷하게 유지). **13절(P4/P10, 2026-07-16)**: non-Focus/non-Disabled 4 variant에 `Shadow/Hard-2` 적용; placeholder fontSize 14→13 통일(3개 확정 프레임 재실측). | `344:721` |
| CornerInput | Input `100:2` | `288:27` | Content=Filled/Placeholder × Error=No/Yes(4, State=Default) + State=Focus 2개(Content=Placeholder×Error=No 기반 1개, Content=Filled×Error=Yes 기반 1개) + State=Disabled 1개(Content=Filled×Error=No 기반, **0-22절, Stage2-b, 2026-07-16**) = **7 variant**(**0-15/0-16절, 2026-07-15**, 동일 패턴). **0-3절**: 모서리 CornerBracket 제거, 순수 2px ink 보더. Placeholder 텍스트=`color/text-placeholder`(#CCCCCC). 베이스 폭 392px. Disabled는 NeoInput과 동일 원칙(배경/보더만 무채색, 텍스트는 `color/ink/900` 유지). **13절(P9/P10, 2026-07-16)**: 모서리 브래킷 없는 상태가 최종 정답으로 재확인(변경 없음); placeholder fontSize 14→13 통일. | `344:740` |
| NeoSelect | Select `101:3` | `387:13`(**0-10절 갱신**, 구 `261:660`) | State=Default/Open(**0-10절**, 트리거 동일 룩+옵션 패널 `Elevation/Raised`) × Content=Placeholder/Selected(**0-11절**, 4 variant). Placeholder 문구 "종류선택". **9-6절**: Open 옵션 hover 배경=`color/bg-hover-muted`(#F1F1F1), 패널 전체 폭 채움(인셋 없음, PASS 확인). **13절(P4, 2026-07-16)**: Default(닫힘) 2 variant(`261:660`/`401:866`)에 `Shadow/Hard-2` 적용, Open 2개는 하위 options-panel의 기존 `Elevation/Raised`와 이중 그림자 방지 위해 제외. **15-2절(2026-07-16, 배치4/4)**: variant 개수(4) 재확인, 내부 컨테이너 6개 `clipsContent=true`→`false` 정정, 루트 sizing을 FIXED→AUTO로 전환(설명 텍스트 확장분 hug), 설명 텍스트 갱신. | `388:746` |
| Card | **Card**(신규 페이지) | `262:15` | Type=Modal/Auth = 2. 2px ink 보더+radius8+Shadow/Hard-6. **0-20절(Stage2, 2026-07-15)**: AccentStrip-Top(양쪽 variant 공통, `262:7`/`262:11`) 배경 amber/500→`color/bg-cta-amber`(#FFCE2C) 리바인딩. **13절(P7/P8, 2026-07-16)**: Modal(`262:6`)/Auth(`262:10`) cornerRadius 8→`radius/none`(0); AccentStrip 하단 보더 추가(Modal `262:7` strokeBottomWeight2, Auth Top `262:11` strokeBottomWeight2, Auth Bottom `262:14` strokeTopWeight2 — 전부 `color/ink/900`+`border/base` 2px). **2026-07-16 재대조(23절)**: Type=Auth AccentStrip-Bottom(`262:14`) 실측 재확인 — teal/500(`VariableID:95:6`)에 잘못 바인딩돼 있던 것을 발견해 `color/sky/500`(`VariableID:615:122`)으로 리바인딩 완료(login `501:5184`/Join `501:4936` 원본 실측 #1395e6과 일치 확인). | (스펙 시트 없음) |
| Toast | Alert `104:2` | `263:53` | Type=Success/Error = 2. `Elevation/Raised`. 플로팅 오버레이 패턴(6절). **13절(P14, 2026-07-16)**: Success variant subtitle(`263:45`) fill을 신규 semantic `color/text-muted-toast`(`VariableID:702:19`, gray/600 alias)로 재바인딩. title(`263:44`)은 이미 `color/ink/900`이라 무수정, Error variant는 텍스트 1개뿐이라 대상 아님. | (스펙 시트 없음) |
| Logo | **Logo**(신규 페이지) | `263:692` | Background=Sky/White = 2. **25절(2026-07-17) 갱신**: Background=Teal(`263:666`)이 브랜드 Primary 틸→스카이블루 전환(0-20절 Stage2) 이후에도 리바인딩되지 않은 잔여 갭이었음이 발견되어 `color/sky/500`으로 리바인딩 + variant명 "Background=Sky"로 정정. | (스펙 시트 없음) |
| Avatar | Avatar `104:127` | `104:131`(기존 재사용) | 변경 없음. **⚠ 갱신(2026-07-17, 29-8절)**: 원 배경이 `color/teal/500`→`color/sky/500`으로 정정됨(마스터 컴포넌트 토큰 `component/avatar-bg`의 alias 교체, 인스턴스 `501:6370`도 동일 토큰에 재바인딩). 아이콘 글리프(Icon/User INSTANCE, 29절에서 이미 라인형 전환 완료)는 이번에도 무관·무수정. | (스펙 시트 없음) |
| Link(0-4절) | Link(신규 페이지, `341:2`) | `341:3`(단일) | Default 단일(69×18). Body/Link + `color/text-link-navy`(**0-20절, Stage2, 2026-07-15**, 구 `color/text-link` teal→navy 리바인딩 — login 신규 확정 프레임 실측 기준, Join 링크는 teal 유지). **(2026-07-15)** 텍스트 "비밀번호 재설정"으로 사용자 직접 변경 완료. | `344:759` |
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
- ~~**신규(0-10절): NeoInput/CornerInput의 Disabled 상태 미확장**~~ — **RESOLVED(0-22절, Stage2-b, 2026-07-16)**: 기존 `State` 열거형에 `Disabled` 값 추가(Content=Filled×Error=No 기반), 배경/보더만 `color/bg-disabled`/`color/border-disabled`로 통일하고 텍스트는 `color/ink/900` 그대로 유지(Input은 값을 보여주는 display라는 원칙). 각 7 variant.
- ~~**신규(0-23절, 2026-07-16): Icon Button(`259:613`)/Row Action Button(`260:95`) Disabled가 Stage2-a 색 토큰화(bg-disabled/border-disabled) 범위에서 빠짐**~~ — **RESOLVED(0-24절, Stage2-d, 2026-07-16)**: 나머지 6개 컴포넌트와 동일한 색 토큰 공식(배경=`color/bg-disabled`, 보더=`color/border-disabled`, 아이콘=`color/text-disabled`, opacity 전부 1)으로 전환 완료. Input(NeoInput/CornerInput) 2종만 텍스트 예외로 계속 유지.
- **신규(0-24절, 2026-07-16): `color/bg-disabled`(#BBBBBB) 흰 배경 대비 1.92:1, WCAG 1.4.11 비텍스트 3:1 미달** — 사용자 명시적 요청("기준 무시하고 원하는 만큼 밝게")으로 이번 프로젝트 범위에서 완화 적용. 개선 대상 아님(7-1절 RESOLVED 성격과 동일하나, Disabled 전용 절이라 이 위치에 별도 기록).
- ~~**⚠ 신규(2026-07-15, 문서 복구 메모)**: 이 세션의 문서 손상·복구 사고로 2/3/5/7-2절 일부가 design-pl의 재구성에 의존한다~~ — **RESOLVED(0-14절)**: FOUNDATIONS 4개 페이지 소급 동기화 라운드에서 1~5절 표를 Figma 라이브 상태와 재대조 완료, 불일치 없음 확인.
- ~~**신규(0-15절): TypeSelector/NeoInput/CornerInput/Sidebar Nav Item의 Focus=No/Yes 직교 축**~~ — **RESOLVED(0-15절, 2026-07-15)**: 9-2절과 동일한 State-열거형 단일값 패턴으로 소급 통합 완료(TypeSelector 12, NeoInput/CornerInput 각 6[0-16절 Focus×Error 복원 포함], Sidebar Nav Item 3 variant).
- **신규(0-17절): 라디오 버튼/Divider 컴포넌트 미등록** — 확정 프레임 전수 검색 결과 실물 0건, 화면정의서에도 별도 필요 흐름 없어 등록하지 않기로 판단(근거는 0-17절 2/3항 참고). 실제로 필요한 흐름이 생기면 재검토.
- **신규(2026-07-15, 두 번째 문서 손상 사고)**: `docs/design/design-system.md`가 세션 중 재차 손상(697→372줄, 섹션 1~11 및 12절 전체 소실)됐다가 git HEAD(commit `4a0db785`/`4cdcbc9`)+세션 중 확보해둔 각 라운드 diff 기록을 근거로 전체 재구성해 복구했다 — 상세 경위는 이 문서 최상단 복구 메모 참고. 원인은 design-systems.md에 이미 명문화된 "Write 전체 덮어쓰기 금지" 규칙이 있었음에도 재발했다는 점이라, design-pl/design-systems 운영 절차 자체(커밋 타이밍, 백그라운드 라운드 사이 git 커밋 주기)를 재점검할 필요가 있다.
- ~~**신규(design-prompter 브리프): TypeSelector 스펙 시트 `clipsContent` 회귀**~~ — **RESOLVED(0-19절, 2026-07-15)**: 26개 auto-layout 컨테이너를 `clipsContent=false`로 정정, Focus 링 잘림 없이 렌더링 확인.
- **신규(0-20절, Stage2, 2026-07-15): 헤더 "로그아웃" NeoBtn(main `501:6373`)의 ink 배경+amber 보더(구값 #ffcb47)+offset(3,3) 그림자** — 기존 Hard-1/2/6 스케일에 없는 이례값, 단일 인스턴스. 사용자 확인 필요 — 의도된 신규 스타일인지 미완성 편집인지 불명. 컴포넌트 마스터는 리바인딩하지 않고 기존 값 유지.
- **신규(0-20절, Stage2, 2026-07-15): main-삭제(`501:3636`)/main-알림창(`501:6548`) amber 미반영** — 카드 상단 스트립/토스트 강조 원이 구값(#FFCB47) 그대로. 컴포넌트 마스터는 신규값(#FFCE2C) 정식 채택 완료라 두 프레임과 마스터 사이 의도적 불일치 존재 — 원본 read-only 방침상 수정 안 함, 사용자 확인 필요.
- **신규(0-20절, Stage2, 2026-07-15): main-검색없음 "전체 보기" 버튼(`517:2753`) 신규 variant 여부 보류** — ink 배경+흰 텍스트+Hard-2 조합이 기존 Button/NeoBtn 어떤 Style에도 없음. 신규 variant 생성은 보류, 범위 확대 방지 차원에서 관찰만 기록.
- **신규(0-20절, Stage2, 2026-07-15): Sidebar 컨테이너 전체 배경/테이블 헤더/사이드바 밖 "전체" 필터 배경/사이드바 카테고리 입력창 placeholder** — 전부 등록된 컴포넌트의 INSTANCE가 아니라 확정 프레임 안의 raw 화면조립 요소로 확인(Table Header/EmptyState와 동일 제외 정책 적용). `color/bg-brand-blue`/`color/bg-accent-navy`/`color/text-placeholder-strong` 토큰은 정식 등록 완료 — ui-designer가 SCREENS 조립 시 직접 참조.
- **신규(0-20절, Stage2, 2026-07-15): Button Amber Hover/Press 블렌드 raw값 미재계산** — **0-25절(2026-07-16) 범위 축소**: NeoBtn의 Style=Amber는 근거 없음이 확인되어 레거시 해제됐으므로 이 TODO에서 제외, Button(`259:609`)의 Amber만 대상. 새 base(#FFCE2C)로 재계산 시 톤이 미세하게 달라짐(현재 Default/Focus만 신규값, Hover/Press는 구값 #FFCB47 기준 블렌드 유지). 9-1절 블렌드 공식은 interaction-designer 소관이라 이번 라운드에서 재계산하지 않음 — 필요 시 후속 라운드.
- ~~**신규(13절 P1, 2026-07-16): NeoBtn/Button Style=Sky/Navy는 State=Default만 존재**~~ — **RESOLVED(34차 배치, 2026-07-16)**: NeoBtn(`259:126`)의 `Style=Sky`(`712:2`)/`Style=Navy`(`712:4`)에 Hover/Press/Focus/Disabled/Loading 5개 State를 기존 Amber/Teal/Coral/Neutral과 동일한 9-1절 공식으로 추가 완료(신규 노드: Sky `738:2`/`738:4`/`738:6`/`738:8`/`738:10`, Navy `744:946`/`744:948`/`744:950`/`744:952`/`744:954` — 총 10개, NeoBtn ComponentSet 이제 60 variant). Hover 12%/Press 24% ink 블렌드(raw unbound, 기존 패턴과 동일), Disabled는 `color/bg-disabled`/`color/text-disabled`(Sky/Navy는 Default에 보더가 없어 Teal/Coral처럼 무보더 유지), Loading opacity 0.7. **Focus 구현 방식 정정**: 실제 재실측 결과 다른 4개 Style(Amber/Teal/Coral/Neutral)의 Focus 링은 문서 9-1절이 설명하는 "2겹 DROP_SHADOW"만으로는 렌더링되지 않고(`get_design_context` CSS 변환 시 spread가 0으로 무시됨), 실제로는 별도의 절대 위치 `FocusRing` 자식 RECTANGLE(strokeWeight 3, `color/ink/900`, cornerRadius 14.5, x/y -4.5, fills 없음)이 시각적 링을 담당하고 있었다 — Sky/Navy Focus도 이 실제 메커니즘(FocusRing 자식 + 기존 2겹 DROP_SHADOW 유지)을 다른 4개 Style과 동일하게 적용했다(`get_screenshot`/inline screenshot으로 링 렌더링 확인 완료). Navy Disabled 텍스트는 Default의 `color/text-inverse`(흰색) 대신 다른 Style들과 통일된 `color/text-disabled`(#555555)로 전환(회색 배경 위 흰 텍스트 대비 문제 방지). Button(`259:609`)은 애초에 P1 판정에서 "실측 결과 대상 아님(NeoBtn 치수와 일치)"으로 Sky/Navy Style 자체를 추가하지 않았으므로 이번에도 대상 밖(해당 없음, TODO 아님). Component Specs 스펙 시트(`342:3`)의 Sky/Navy 행 TODO 플레이스홀더 텍스트(`731:837`/`731:861`)를 삭제하고 6칸(Default+5 State) 그리드로 채워 다른 Style 행과 동일한 형식으로 갱신했다. 자체 재대조(hex/boundVariable/opacity/effects 전수) 완료.
- **신규(13절 P2, 2026-07-16): Row Action Button Danger의 Hover/Press/Focus/Disabled는 이번 갱신 범위 밖** — Default만 amber/ink로 갱신됐고 나머지 State는 구 coral 기반 파생값 그대로라 불일치 가능성 있음. 후속 라운드에서 재확인 필요.
- **신규(13절, 2026-07-16): 사이드바 "새 카테고리" 버튼(`501:6358`, navy 배경이지만 다른 패턴)** — 이번 라운드 대상 밖, 후속 판단 필요.
- ~~**신규(28절, 2026-07-17): Sidebar Nav Item State=Active(`258:17`)/State=Inactive(`258:23`) 마스터에 확정 프레임(`501:6050`/`501:6055` 등)의 2px `#1a1a1a` 보더가 없음**~~ — **RESOLVED(28-9절, 2026-07-17)**: 확정 프레임 재실측(2px `#1a1a1a`≈`color/ink/900`, INSIDE, 4변 균일) 결과대로 State=Active/Inactive/Focus 3개 variant 전부에 2px INSIDE `color/ink/900` 보더를 추가했다(Focus도 9-1절 순수성 원칙에 따라 동일 적용). FocusRing(`574:1056`)의 OUTSIDE 스트로크 대체 기법(9-5절)은 그대로 유지 — 새 보더(내측)와 기존 FocusRing(외측)이 1px 간격을 두고 충돌 없이 이중 링으로 렌더링됨을 스크린샷으로 확인해, 별도 설계 변경(DROP_SHADOW 복귀 등)은 불필요하다고 판단했다.
- ~~**신규(9-5절 관련, FocusRing-Ink 574:1056 raw hex 하드코딩)**~~ — **RESOLVED(28-9절, 2026-07-17)**: `574:1056`의 stroke를 raw `#1a1a1a`(boundVariables 없음)에서 `color/ink/900`(`VariableID:95:9`)에 정식 바인딩(NeoBtn FocusRing `549:43`과 동일 패턴 재사용).
- ~~Avatar 원 배경 마스터(teal, bound) vs 확정 화면 인스턴스(sky, unbound 오버라이드) 불일치~~ — **RESOLVED**(29-8절 참고, 2026-07-17). `component/avatar-bg` 토큰의 alias를 `color/teal/500`→`color/sky/500`으로 교체해 마스터·인스턴스 모두 스카이블루로 통일 완료.
- **신규(33절, 2026-07-17, brand-designer Primary/Secondary/Accent 역할 재평가 라운드 부수 발견)**: **count pill(비활성, Sidebar Nav Item 하위 `258:16` State=Inactive)과 main-삭제 모달 상단 스트립이 `color/bg-cta-amber`(#FFCE2C, 앰버 신값)이 아니라 구값(#FFCB47)에 머물러 있는 값 드리프트**가 8개 확정 프레임 fill+stroke 면적 전수 실측 중 관찰됐다. **이번 라운드에서는 재바인딩하지 않는다** — 범위를 Colors 페이지 시각 재정리 + 문서 기록으로 한정했다(design-prompter 브리프 명시 범위 제한). main-삭제 카드 상단 스트립 건은 0-20절 "미해결 관찰 2건"(main-삭제 `501:4174`/main-알림창 `501:6548`)과 동일 계열 발견일 가능성이 있으나(완전히 동일 노드인지는 미확인), count pill 비활성 배경은 이번에 처음 명시적으로 관찰·기록된 항목이다. 실제 정정(리바인딩)은 별도 라운드로 넘긴다.
- ~~**신규(design-qa 감사, 2026-07-17): NeoBtn Style=Sky(`712:2`) 텍스트 `color/ink-900` 오바인딩 + Sky/Navy 2px ink 보더 누락**~~ — **RESOLVED(35절, 2026-07-17)**: Sky 텍스트(Default/Hover/Press/Focus/Loading 5 State)를 `color/text-inverse`로 리바인딩, Sky/Navy 12개 variant 전부에 2px INSIDE 보더 추가(Disabled 2개는 `color/border-disabled`, 나머지 10개는 `color/ink/900`). 상세는 35절 참고.
- **신규(35-7절, 2026-07-17): Sky 배경(#1395e6)+흰 텍스트(14px Bold) WCAG 대비 약 3.25:1** — 본문 기준(4.5:1) 미달, 확정 원본(`501:6423`)에 이미 그대로 존재하는 조합이라 이번 라운드에서 임의로 변경하지 않음. 7-1절 6번(`color/text-link` 3.12:1)과 동일 계열, 개선 여부는 사용자 판단 필요.
- ~~**신규(QA 트랙, 2026-07-17): NeoBtn/Button Style=Coral도 Sky와 동일하게 텍스트 `color/ink/900` 오바인딩 + 2px ink 보더 누락**~~ — **RESOLVED(36-2절, 2026-07-17)**: 35절이 Sky/Navy에 적용한 것과 동일한 정정을 Coral에도 확장 — NeoBtn 12 variant + Button 6 variant 전부(Disabled 제외) 텍스트를 `color/text-inverse`로, 보더를 2px INSIDE `color/ink/900`(Disabled는 `color/border-disabled`)로 정정. 상세는 36-2절 참고.
- **신규(36-2절, 2026-07-17): Coral 배경(#FF5A76)+흰 텍스트(14~15px Bold) WCAG 대비 약 3.01:1** — 본문 기준(4.5:1) 미달, 확정 원본(`501:6406`/`501:4211`)에 이미 그대로 존재하는 조합이라 이번 라운드에서 임의로 변경하지 않음. 35-7절(Sky 3.25:1)·7-1절 6번과 동일 계열, 개선 여부는 사용자 판단 필요.

## 8. Legacy — B-2 파일럿 기반 컴포넌트 (참고용, 더 이상 정식 소스 아님)

아래는 이전 B-2 파일럿 라운드에서 추출한 컴포넌트 인벤토리다. `docs/design/confirmed/user-confirmed-final-design.md`에 따라 8개 사용자 확정 프레임이 이를 완전히 대체했으므로 **더 이상 정식 소스가 아니다**. 삭제하지 않고 이력으로 보존하며, 이름이 겹쳤던 3개(`Button`/`Row Action Button`/`Sidebar Nav Item`)에 이어 나머지 5개(`Input`/`Select`/`Badge`/`Table Row`/`Alert`)도 `[Legacy B-2] ` 접두사로 리네임해 위 5절의 신규 컴포넌트와 구분했다. Avatar(`104:131`)만 확정 디자인과 완전히 일치해 현재도 유효하므로 접두사 없이 그대로 둔다. **⚠ 2026-07-17 각주(29-8절)**: 이 "완전히 일치" 서술은 아이콘 글리프·치수·구조 기준으로는 정확했으나 원 배경 색상까지는 정확하지 않았다 — 마스터는 `color/teal/500`(틸)에 바인딩돼 있었고 실제 확정 화면 인스턴스(`501:6370`)는 `#1395e6`(스카이블루) 로컬 오버라이드였다(29-6절에 미해결로 기록됨). 메인 세션의 `findAll` 전체 색상 인벤토리 스캔(확정 프레임 `501:6008`, hex `1395e6` count 16, 샘플 노드명에 "Avatar" 포함)을 근거로 승인받아 29-8절에서 `color/sky/500`으로 바로잡았다 — 현재는 색상까지 포함해 완전히 일치한다.

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
  - **⚠ 13절(P1) 각주, 2026-07-16**: 위 `color/text-inverse`(`VariableID:219:2`)는 등록 이후 이번 라운드에 처음으로 NeoBtn Style=Navy(`712:4`) 텍스트에 실제 바인딩되며 활성 사용을 시작했다 — Legacy 컬렉션 소속이지만 값(#FFFFFF) 자체는 그대로 재사용, 신규 semantic 재생성 없음(navy+text-inverse WCAG 8.91:1 PASS).
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

**⚠ 2026-07-16 갱신(14-2/14-3절) — 활성 레거시 컴포넌트 0개 확정**: 위 표는 0-3/0-6/0-7절 폐기 라운드가 처리한 COMPONENT_SET 레벨 8개(Avatar 제외)만 다룬다. 이와 별개로 14-2절에서 파일럿 페이지(`222:524`) 전체를 재귀 스캔한 결과 `[Legacy B-2]` 접두사 INSTANCE **72개**(사용자 추정 "약 78개"와 차이, 실측값)를 추가로 발견해 전부 `detachInstance()`로 분리 완료했다. 이 72개의 마스터 COMPONENT는 위 표의 8개 ID와 전혀 다른 별개의 variant 단위 컴포넌트 14개(`147:355`/`146:56`/`146:46`/`104:14`/`100:6`/`99:14`/`97:31`/`103:101`/`103:96`/`97:19`/`166:74`/`101:7`/`180:99`/`104:6`)였고, 조회 결과 이미 `parent: null`(고아, 0-3절 폐기 라운드 당시 상위 COMPONENT_SET 제거 잔재로 추정)였다. 14-3절에서 이 14개를 파일럿 페이지의 격리 컨테이너(`726:934`)로 재부모 후 FRAME 전환(신규 `727:93`~`727:106`)을 시도했다 — 시각 대체본은 FRAME 14개로 완전히 이전됐으나, 원본 키드(keyed) COMPONENT 14개 자체는 Figma가 키 레지스트리 무결성 때문에 `remove()`로도 물리적으로 삭제하지 않아 고아 상태로 영구 잔존한다(플랫폼 한계, 페이지 트리 밖이라 Assets/Insert 패널 등 어디에도 노출되지 않아 실질적 리스크는 없음). **결론: 위 표의 8개(COMPONENT_SET 레벨) + 14-2/14-3절의 14개(variant 레벨) 전부 합쳐 Assets/Insert 패널에 노출되는 활성 레거시 컴포넌트는 이제 0개다.**

**⚠ 2026-07-16 추가 갱신**: 0-25절에서 NeoBtn Amber/Teal 24 variant가 추가로 레거시 해제되어 `784:940` 컨테이너에 보존됐다 — 이 절의 "0개" 선언은 그 시점(14절까지) 기준이며, 최신 레거시 현황은 0-25절을 함께 참고할 것.

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
  - **⚠ FocusRing 자식 RECTANGLE 메커니즘(2026-07-16 정식 반영, 13절 P1/34차 배치에서 실측 확인)**: 위 2겹 `DROP_SHADOW` 스택만으로는 일부 렌더링 경로(`get_design_context`의 CSS 변환 등)에서 spread가 무시돼 링이 실제로 보이지 않는 경우가 확인됐다. 실측 결과, 시각적 링을 실제로 담당하는 것은 별도의 절대 위치 자식 노드 `FocusRing`(RECTANGLE, `layoutPositioning=ABSOLUTE`)이다 — `strokeWeight=3`, stroke color=`color/ink/900`(`VariableID:95:9`), `cornerRadius = 버튼 자체 cornerRadius + 4.5`(오프셋 4.5px — 버튼 radius가 기본값 10이면 링 radius는 14.5), 위치는 버튼 바운딩박스 기준 x/y `-4.5`(네 방향 균등 오프셋), fills 없음(스트로크만). **2겹 DROP_SHADOW 스택과 이 FocusRing 자식 RECTANGLE은 함께 적용된다** — 이 문서가 9-1절 최초 작성 시점엔 DROP_SHADOW 스택만 설명하고 이 FocusRing 메커니즘 자체를 서술하지 못했던 갭이었다(18/19절이 인용하는 "9-1절/34차 공식"의 실제 근거가 바로 이 문단이다). 새 Style/컴포넌트에 Focus를 추가할 때는 항상 대응하는 Default(또는 그에 준하는 비-포커스) 상태를 clone한 뒤 이 두 효과(2겹 DROP_SHADOW + FocusRing 자식 RECTANGLE)를 함께 추가한다 — 버튼 자체 `cornerRadius`가 10이 아니면 링 `cornerRadius`도 반드시 `버튼 cornerRadius + 4.5`로 재계산해야 한다(19절 정정 사례 참고, 고정값 14.5를 그대로 복사하지 않는다).

**Focus 2겹 링 적용 확인(2026-07-15)**: 버튼류 5개 컴포넌트(NeoBtn `259:126` 8 + Button `259:609` 3 + Icon Button `259:613` 1 + Row Action Button `260:95` 2 + Table Row Action `260:100` 2 = 총 16 variant) 전부 위 2겹 공식(흰 1px+ink 4px, 장식 효과 없음)으로 재확인 완료 — `use_figma` 읽기 전용 스크립트로 16개 variant의 effects 배열을 전수 재조회해 정확히 일치함을 확인했다(9-2절 표 참고).
- **Disabled** — **(0-22/0-23/0-24절, Stage2-a/b/d, 2026-07-16 최종 갱신)** 8개 컴포넌트(NeoBtn/Button/Table Row Action/Checkbox/NeoInput/CornerInput/Icon Button/Row Action Button)가 전부 9-5절의 opacity 공식을 대체해 동일한 색 토큰 방식을 쓴다: 컨테이너 opacity=1, 배경 fill→`color/bg-disabled`(**#BBBBBB, 0-24절에서 #929292→재조정**), 보더 stroke→`color/border-disabled`(#5C6366), 텍스트/아이콘 fill→`color/text-disabled`(#555555) — 단 NeoInput/CornerInput은 예외로 텍스트를 `color/ink/900`(Default와 동일) 그대로 유지(Input은 값을 보여주는 display라는 원칙). Icon Button/Row Action Button은 0-24절에서 마지막으로 이 공식에 합류했다 — 이제 9-5절 구 opacity 공식을 쓰는 컴포넌트는 없다.
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

- Sidebar Nav Item/TypeSelector의 Hover/Press/Disabled 상태는 다루지 않았다. ~~NeoInput/CornerInput의 Disabled 상태~~ — **RESOLVED(0-22/0-23절, 2026-07-16)**. **NeoSelect의 Focus/Disabled/Error 상태는 여전히 미해결**(0-10절/7-2절 참고). ~~신규(0-23절, 2026-07-16): Icon Button/Row Action Button의 Disabled 상태는 Stage2-a 색 토큰화 대상에서 빠져 있다~~ — **RESOLVED(0-24절, 2026-07-16)**: 8개 컴포넌트 전부 동일 색 토큰 공식으로 통일(9-1절 참고).
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

## 13. 확정 디자인 8프레임 전수 대조 후속 반영 — P1~P15 (2026-07-16, 35차)

design-prompter가 확정 8개 프레임(부모 `501:2505`)을 전수 대조해 발견한 패턴 15건(P1~P15)을 처리했다. 원본 8개 프레임은 이번에도 전혀 수정하지 않았다(무수정 확인).

### P1~P15 처리 결과 표

| # | 패턴 | 판정 | 처리 내용 |
|---|---|---|---|
| P1 | NeoBtn navy·sky 미등록 Style | REFLECT | NeoBtn(`259:126`)에 `Style=Sky`(`712:2`, fill `color/bg-brand-blue`)/`Style=Navy`(`712:4`, fill `color/bg-accent-navy`) 신규 추가. Sky 텍스트=`color/ink/900`(WCAG 5.36:1 PASS), Navy 텍스트=`color/text-inverse`(`VariableID:219:2`, 기존 legacy 토큰 첫 실사용, WCAG 8.91:1 PASS — navy+ink는 1.95:1로 미달이라 채택 안 함). **State=Default만 등록, 나머지 State(Hover/Press/Focus/Disabled/Loading)는 TODO(7-2절)로 이관**. Button(`259:609`)은 실측 결과 대상 아님(두 버튼 모두 NeoBtn 치수와 일치) — 무수정. |
| P2 | RowActionButton Danger 배경 | REFLECT | Danger/Default(`260:53`) 배경 `color/gray/0`→`color/bg-cta-amber`(#FFCE2C), 보더 `color/coral/500`→`color/ink/900`(#1A1A1A), 두께는 기존 `border/hairline`(1px) 유지. 5개 프레임 20개 인스턴스 전수 재대조 hex 일치 확인. Danger의 Hover/Press/Focus/Disabled는 이번 범위 밖 — TODO(7-2절). |
| P3 | RowActionButton Neutral 보더 누락 | 조치 없음(재현 안 됨) | 재검증 결과 마스터(`260:34`, `border/hairline` 1px)와 프레임(main `501:6103`, 1px) 두께 정확히 일치 — 34차 관찰이 재현되지 않음, 변경 없음. |
| P4 | NeoInput/NeoSelect 그림자 누락 | REFLECT | NeoInput non-Focus/non-Disabled 4개(`261:10`/`378:4`/`398:884`/`398:888`)에 `Shadow/Hard-2` 적용. NeoSelect Default(닫힘) 2개(`261:660`/`401:866`)에 `Shadow/Hard-2` 적용, **Open 2개는 제외**(하위 options-panel이 이미 `Elevation/Raised`를 써서 이중 그림자 방지). CornerInput은 대상 아님(무수정). |
| P5 | CountPill "전체" 하이브리드 | REFLECT | Active(`258:12`)에 `Shadow/Hard-1` 신규 적용(배경/보더는 기존값 이미 프레임과 일치해 무수정). |
| P6 | Icon Button Close radius | REFLECT | 전체 5 State(`259:610`/`1036`/`1038`/`1040`/`1042`) cornerRadius 10→`radius/none`(0). |
| P7 | Card cornerRadius | REFLECT | Modal(`262:6`)/Auth(`262:10`) cornerRadius 8→`radius/none`(0). |
| P8 | Card AccentStrip 하단 보더 누락 | REFLECT | Modal(`262:7`) strokeBottomWeight=2, Auth Top(`262:11`) strokeBottomWeight=2, Auth Bottom(`262:14`) strokeTopWeight=2 — 전부 `color/ink/900`, `border/base`(2px) 재사용. |
| P9 | CornerInput 모서리 브래킷 | 조치 없음(사용자 확정) | 마스터(`288:27`)는 브래킷 없는 상태(0-3절 결론)가 최종 정답으로 재확인(variant 전수 조회 결과 CornerBracket 노드 0건, 정상). 확정 프레임(Join/login/login-알림창)에 브래킷이 보이는 건 read-only라 손댈 수 없는 **알려진 차이**로만 기록, 마스터는 변경하지 않는다. |
| P10 | CornerInput placeholder fontSize | REFLECT | 3개 프레임(Join/login/login-알림창) 재실측 결과 placeholder·filled 구분 없이 13px로 일관 — 전체 7 variant 텍스트 fontSize 14→13 통일. |
| P11 | CTA(Amber) 버튼 ink 보더 누락 | REFLECT | NeoBtn Amber 12 variant(Size2×State6)+Button Amber 6 variant, 전체 State에 2px `color/ink/900` 보더 추가. Focus 순수성 원칙 준수 확인(기존 2겹 DROP_SHADOW 링 불변, 보더만 추가). Sky/Navy(P1 신규분)·Teal/Coral/Neutral은 대상 아님. |
| P12 | Checkbox 체크마크 색상 오바인딩 | REFLECT(사용자 확정 필수) | Checked 체크마크(`474:888`) stroke `color/border-divider-cool`→`color/ink/900`(#1A1A1A)로 정정. login 인스턴스(`604:5954`)의 흰색 로컬 오버라이드는 원본 프레임 기존 상태라 무수정 유지 — **원칙**: "색상만 다른 반복 사용 사례(예: 어두운 배경 위 체크박스)는 새 variant를 만들지 않고 인스턴스 단위로 fill/stroke만 로컬 오버라이드한다." **⚠ 2026-07-16 재정정(21절)**: 이 판정 당시 Box(`474:886`)가 이미 `color/sky/500`으로 확정 디자인과 일치해 있었다는 사실이 누락된 채 "마스터는 ink 유지"로 결론났다 — 실제로는 확정 디자인이 스카이블루+흰 체크 조합이라 체크마크도 `color/text-inverse`(흰색)로 재정정됐다. 상세는 21절 참고. |
| P13 | Sidebar Nav Item ink 보더+opacity | 조치 없음(이례값) | main-알림창 1개 프레임에서만 관찰(Active 배경+ink보더+기존 그림자 조합), 다른 프레임 재현 없음 — 단일 이례값으로 판단, 마스터(`258:29`) 미반영. |
| P14 | Toast 텍스트 색상 오바인딩 | REFLECT | Success variant subtitle(`263:45`) fill을 신규 semantic `color/text-muted-toast`(`VariableID:702:19`, 기존 primitive `color/gray/600`=`VariableID:95:15`=#5C6366 alias, 신규 원시값 없음)로 재바인딩. title(`263:44`)은 이미 `color/ink/900`이라 무수정. Error variant는 텍스트 1개뿐이라 대상 아님. |
| P15 | NeoBtn "검색" 버튼 코랄 raw FRAME | 조치 없음(문제 아님) | raw FRAME(`501:6406`) fill이 기존 `color/coral/500`(#FF5A76) 실측값과 소수점까지 완전 일치 확인 — 정식 컴포넌트 인스턴스가 아니라 손으로 그린 것일 뿐, 색상 자체는 결함 아님. |

### 신규 토큰 및 레거시 토큰 첫 실사용

- **신규 토큰(1개, alias만)**: `color/text-muted-toast`(`VariableID:702:19`) → `color/gray/600`(#5C6366) — Toast Success subtitle 전용, 신규 primitive 없음(1-2절에 정식 반영 완료).
- **레거시 토큰 첫 실사용**: `color/text-inverse`(`VariableID:219:2`)가 이번에 NeoBtn Style=Navy 텍스트로 처음 실사용됐다(8절 각주, 1-2절 언급 완료).

### FOUNDATIONS Colors 페이지(`95:2`) 반영

이번 라운드는 신규 primitive 없이 semantic 1개(alias만)뿐이다. 정식 Semantic 그리드(`95:123`, "Semantic Row", 31개 스와치)를 `use_figma` 읽기 전용으로 조회한 결과 `color/text-muted-toast` 스와치가 아직 없어(0건), 기존 `Swatch color/text-disabled`(`650:14`) 패턴을 그대로 clone(104×91, 사각형 8radius+회색 보더+라벨 2줄)해 값만 gray/600(#5C6366)·라벨 "text-muted-toast"/"alias gray/600"으로 교체한 뒤 그리드 마지막 자식(`716:6`)으로 추가했다 — 별도 "신규" 섹션을 만들지 않고 기존 정식 그리드에 바로 편입(0-21/0-23절과 동일한 원칙). `get_screenshot`으로 새 스와치(`716:6`)가 기존 카드들과 동일한 톤/레이아웃으로 정상 렌더링됨을 확인했다. Semantic 그리드는 이제 32개 스와치.

## 14. 파일럿 페이지 정리 — 구 확정 디자인 섹션 삭제 + Legacy B-2 인스턴스 detach (2026-07-16, design-pl 지시, 순수 정리 작업)

design-pl이 새 창작 판단 없는 순수 정리 작업 2건을 직접 지시했다(design-prompter 브리프 없음).

### 14-1. 구 확정 디자인 섹션(`248:11689`) 삭제

파일럿 페이지(`222:524`) 하위에 있던 부모 섹션 `248:11689`("❌ 미채택 — 확정 디자인 탈락")와 그 8개 자식 프레임(`214:349`/`248:8103`/`248:9867`/`242:4280`/`241:1552`/`247:6666`/`247:5303`/`247:5558`, 전부 "확정 디자인 - 절대 원본 건들지 말것-" 접두사)을 삭제했다. 신규 확정 디자인(`501:2505` 하위 8개 프레임, 34차/35차 라운드에서 전수 대조 완료)으로 완전히 대체돼 더 이상 참고 가치가 없다고 판단됐기 때문이다.

**절차**: 삭제 전 `use_figma` 읽기 전용 스크립트로 섹션명·8개 자식 ID/이름이 지시서와 정확히 일치함을 먼저 확인(안전 확인) → 일치 확인 후 섹션+8개 자식 삭제(`section.remove()`) → 재조회로 파일럿 페이지 children에서 `248:11689`가 사라졌음을 확인, `501:2505`(신규 확정 디자인, 8개 자식)는 무손상 확인.

### 14-2. `[Legacy B-2]` 인스턴스 72개 recon + detach (마스터 FRAME 전환은 다음 콜로 이관)

파일럿 페이지 전체를 재귀 스캔해 이름이 `[Legacy B-2]`로 시작하는 INSTANCE 노드를 찾은 결과 **72개**(사용자 추정 "약 78개"와 차이 — 실제 발견값 그대로 보고) 발견, 전부 `detachInstance()`로 분리 완료(실패 0건). 분리 후 재조회 결과 `[Legacy B-2]` 접두사 INSTANCE 타입 노드는 0개, 전부 FRAME으로 전환됨(총 `[Legacy B-2]` 접두사 FRAME 78개 — 이번에 detach된 72개 + 이전부터 이미 FRAME이었던 6개). 대표 3개(Input/Default/Large, Button/Primary/Text/Default/Large, Sidebar Nav Item/Active)를 detach 전/후 스크린샷으로 스팟체크해 치수가 정확히 일치함을 확인(360×49, 174×49, 180×38 — 회귀 없음).

**⚠ 중요 발견 — 마스터 컴포넌트 14개가 고아(orphan) 상태**: 72개 인스턴스의 마스터 COMPONENT ID를 중복 제거하면 14개다:

| 마스터 ID | 이름 |
|---|---|
| `147:355` | [Legacy B-2] Input/Default/Large |
| `146:56` | [Legacy B-2] Button/Primary/Text/Default/Large |
| `146:46` | [Legacy B-2] Button/Secondary/Text/Default/Large |
| `104:14` | [Legacy B-2] Alert/Error |
| `100:6` | [Legacy B-2] Input/Default/Default |
| `99:14` | [Legacy B-2] Button/Primary/Text/Default/Default |
| `97:31` | [Legacy B-2] Button/Secondary/Text/Default/Default |
| `103:101` | [Legacy B-2] Sidebar Nav Item/Active |
| `103:96` | [Legacy B-2] Sidebar Nav Item/Default |
| `97:19` | [Legacy B-2] Button/Primary/IconText/Default/Default |
| `166:74` | [Legacy B-2] Button/Danger/Text/Default/Default |
| `101:7` | [Legacy B-2] Select/Default |
| `180:99` | [Legacy B-2] Button/Amber/Text/Default/Default |
| `104:6` | [Legacy B-2] Alert/Success |

이 14개 ID는 **8절 "폐기 완료" 표의 ID(`97:47`/`100:46`/`101:64`/`102:65`/`103:7`/`166:421`/`103:106`/`104:108`)와 전혀 다르다** — 즉 0-3절 폐기 라운드가 처리했던 것과는 별개의, 더 세분화된(variant 단위) 컴포넌트 계층이다. `use_figma`로 직접 조회한 결과 이 14개 노드는 전부 `type: COMPONENT`, `removed: false`(제거되지 않음, 여전히 유효)이지만 **`parent: null`**(어떤 페이지·프레임에도 속하지 않은 고아 상태)이다. 정황상 0-3절 폐기 절차가 상위 COMPONENT_SET을 제거할 때, 당시엔 발견되지 않았던 이 72개 파일럿 인스턴스가 이 개별 variant 컴포넌트들을 계속 참조하고 있어 Figma가 완전 삭제 대신 고아 상태로 보존한 것으로 추정된다(추정 — 확정 아님). 페이지 소속이 없어 Assets/Insert 패널에는 노출되지 않는다.

**다음 콜(마스터 전환/정리)에 넘길 입력이었던 사항 — 처리 완료, 아래 14-3절 참고**: 위 표의 14개 고유 COMPONENT ID를 다음 콜에서 처리했다. 결과는 예상과 달랐다 — FRAME 전환은 "새 FRAME으로 대체"하는 방식으로 완료됐지만, 원본 COMPONENT 노드 자체는 Figma 플랫폼 한계로 삭제되지 않고 고아 상태로 남았다(근본 원인 규명 완료, 14-3절 참고).

원본 확정 디자인 8개 프레임(`501:2505` 하위)은 이번 작업 전체에서 전혀 열람 외 수정하지 않았다.

### 14-3. 14개 고아 마스터 — 파일 전체 재확인 + 컨테이너 격리 + FRAME 전환 시도 — 플랫폼 한계 근본 원인 규명 (2026-07-16, design-pl 지시 후속 콜)

**1) 파일 전체(29개 페이지) 재확인**: 14-2절은 파일럿 페이지만 스캔했었다. 이번엔 `page.loadAsync()`로 29개 페이지 전부를 `setCurrentPageAsync` 없이 로드해(페이지 전환 1회 제한 규칙 우회), 각 페이지의 모든 INSTANCE에 대해 `getMainComponentAsync()`로 mainComponent ID를 확인하는 전수 검색을 실행했다. **결과: 14개 고아 ID를 참조하는 INSTANCE는 파일 전체에서 0건**(총 29페이지, 인스턴스 합계 242개 스캔 — Component Specs 155개, 파일럿 54개, Table Row 16개 등 포함). 14-2절의 detach 72건으로 이미 모든 참조가 끊겼음을 파일 전체 스코프에서 재확인했다.

**2) 컨테이너 신설 + 재부모**: 파일럿 페이지(`222:524`)에 `❌ 폐기 — 고아 레거시 마스터 (0-3절 폐기 라운드 잔재, 35차/36차 재발견)` 프레임(`726:934`, 1120×440, 기존 파일럿 콘텐츠 오른쪽 x=12112 y=0에 배치)을 신규 생성하고, 14개 고아 COMPONENT를 4열×4행 그리드(겹침 없음, 각 셀 260×90)로 `appendChild`했다. 재부모 직후 `get_screenshot`으로 배치를 확인했다 — 그리드 내 겹침 없음, 시각적 콘텐츠는 이동 전과 동일(값을 바꾸지 않고 노드를 그대로 옮겼으므로 원천적으로 보존됨).

**3) COMPONENT → FRAME 전환 시도**: 8절 "폐기 완료" 표에서 쓴 것과 동일한 절차(동일 시각 속성을 복제한 새 FRAME 생성 → 자식 이동 → 원본 COMPONENT `remove()`)를 14개에 적용했다. 14개 전부 자체 자식 노드가 0개(리프 레벨 variant라 텍스트 등 장식이 부모 COMPONENT_SET 쪽에 있었던 것으로 추정, 이번 발견)임을 확인했고, 새 FRAME 14개(`727:93`~`727:106`)가 컨테이너(`726:934`) 안에 정상 생성됐다 — `get_metadata` 재조회 결과 14개 전부 `type: FRAME`, `parent: 726:934`, 컨테이너 자식 수 14개 일치.

**⚠ 신규 발견 — 원본 고아 COMPONENT는 `remove()`로 완전히 삭제되지 않는다(Figma 플랫폼 한계, 근본 원인 규명)**: `remove()` 호출 자체는 에러 없이 성공했지만(스크립트 원자성상 실패했다면 전체 롤백됐을 것), 이후 재조회 결과 원본 14개 COMPONENT ID(`147:355` 등)는 여전히 `type: COMPONENT`, `removed: false`로 살아있었고 `parent`는 다시 `null`(고아)로 돌아가 있었다. **근본 원인 확인**: 14개 전부 `key` 속성(퍼블리시 가능한 컴포넌트 키, 예: `147:355`→`b6e70502aeb25792efd3485fb9553b756776c48a`)이 존재하는 **키드(keyed) 컴포넌트**였다 — Figma는 라이브러리 키가 할당된 메인 컴포넌트를 스크립트의 `remove()`로 완전히 파기하지 않고 페이지 트리에서 detach(`parent=null`)만 시킨 채 키 레지스트리 무결성을 위해 노드 객체 자체는 보존하는 것으로 확인됐다. 이는 14-2절에서 "추정"으로만 남겨뒀던 원인(0-3절 COMPONENT_SET 삭제 시 이 14개가 처음 고아가 된 메커니즘)과 동일하며, 이번에 실증적으로 근본 원인이 규명됐다.

**최종 상태**:
- **housed·시각 대체본(신규, 정식 산출물)**: FRAME 14개(`727:93`~`727:106`), 컨테이너(`726:934`) 안에 4×4 그리드로 격리 배치, 전부 `type: FRAME` 확인 완료 — Assets/Insert 패널에 노출되지 않음(FRAME은 애초에 컴포넌트 피커 대상이 아님).
- **원본 키드 컴포넌트(구, 물리적 삭제 불가 — 플랫폼 한계)**: `147:355` 외 13개, 여전히 `type: COMPONENT`이지만 `parent: null`(고아) 상태 그대로 유지 — 완전 삭제 하우스룰과 무관하게 애초에 Figma가 삭제를 허용하지 않음. 페이지 트리에 속하지 않으므로 Assets/Insert 패널에는 이번에도 노출되지 않는다(14-2절과 동일 결론, 재확인).
- 확정 디자인 섹션(`501:2505`, 8개 프레임)은 이번에도 무수정 확인(`childCount: 8` 그대로).

**결론**: PL이 요청한 "housed + FRAME 전환"의 실질적 목표(정리 정돈·Assets 비노출·시각 콘텐츠 보존)는 신규 FRAME 14개로 완전히 달성됐다. 원본 키드 COMPONENT 14개는 Figma 플랫폼이 물리적 삭제를 막고 있어 고아 상태로 영구 잔존하지만, 페이지 트리 밖에 있어 어떤 패널·검색에도 노출되지 않으므로 실질적 영향은 없다 — 새로운 리스크는 생기지 않았고, 오히려 14-2절의 미확정 추정이 이번에 근본 원인까지 확정됐다.

## 15. Component Specs 페이지(`342:2`) 리셋 — 13개 스펙 시트 전수 재검증 4배치 + 페이지 겹침 정리 (2026-07-16, 순수 검증+동기화, 창작 판단 없음)

**배경**: 13절(35차)/34차 라운드를 거치며 NeoBtn(48→50→60 variant, Sky/Navy Style 신규 및 5-State 완성) 등 여러 ComponentSet의 variant 개수가 늘어났지만, `Component Specs` 페이지(`342:2`)의 스펙 시트 13개는 즉시 따라가지 못해 실제 variant 개수와 그리드 셀 개수가 어긋날 위험이 있었다. 이를 4번의 배치 콜로 순차 점검·동기화했다(각 배치: 대응 ComponentSet `get_metadata` 재조회 → 스펙 시트 그리드 실제 셀 개수 비교 → 부족분 추가/초과분 정리 → `get_screenshot` 육안 확인 → `clipsContent=false` 확인).

### 15-1. 배치별 처리 결과

| 배치 | 대상 스펙 시트 | 결과 |
|---|---|---|
| 1/4 | NeoBtn(`342:3`)/Button(`343:50`)/Icon Button(`343:653`) | NeoBtn 실제 50 vs 스펙 시트 48 — 불일치 발견, Sky/Navy Default Row 2개 추가(`731:815`/`731:838`, 각 Default 칸만 채우고 나머지 5칸은 TODO 캡션). Button/Icon Button은 실제 개수(18/5)와 스펙 시트 개수 일치, 변경 불필요. 3개 스펙 시트 루트 `clipsContent`가 전부 `true`로 남아 있던 것을 발견해 `false`로 일괄 정정. 이후 별도 라운드("NeoBtn Sky/Navy 완성", 7-2절 RESOLVED 항목·13절 각주 참고)에서 Sky/Navy에 나머지 5개 State(Hover/Press/Focus/Disabled/Loading)가 마저 채워지며 NeoBtn ComponentSet이 최종 60 variant로 성장, 스펙 시트도 6칸 그리드로 확장돼 현재 크기 882×872에 정착했다. |
| 2/4 | Row Action Button(`343:697`)/Table Row Action(`343:1044`)/Sidebar Nav Item(`343:1106`)/TypeSelector(`343:1146`) | 재검증 결과 4개 스펙 시트 전부 실제 variant 개수(10/10/3/12)와 그리드 셀 개수 일치 확인. 세부 배치 로그는 `.claude/agent-memory/design-systems.md`의 5개 캡 순환으로 유실됐으나, 이번 4배치(15절 작성 시점) 재조회로 정합 상태가 실제로 유지되고 있음을 재확인했다. |
| 3/4 | NeoInput(`344:721`)/CornerInput(`344:740`)/Link(`344:759`)/Contact Row(`352:726`) | 재검증 결과 4개 스펙 시트 전부 실제 variant/구성(7/7/1/2)과 그리드 셀 개수 일치 확인. 마찬가지로 세부 로그는 캡 순환으로 유실됐으나 라이브 상태로 정합성 재확인 완료. |
| 4/4(이번 배치) | NeoSelect(`388:746`)/Checkbox(`475:762`) | 아래 15-2절 참고 — 이번 콜에서 직접 점검·수정. |

**로그 유실 관련 투명성 기록**: `.claude/agent-memory/design-systems.md`는 최근 5개 작업 로그만 남기는 휘발성 캡 정책이라, 배치 2/3 콜의 세부 발견 내역(있었다면)이 이후 다른 라운드 로그에 밀려 사라졌다. State Ledger 소스 오브 트루스는 이 문서이므로, 배치 2/3 결과는 "재조회로 확인한 최종 상태"로만 이 절에 기록하며 당시 구체적으로 무엇을 고쳤는지는 재구성하지 않는다(정직하게 유실을 명시).

### 15-2. 배치 4/4 — NeoSelect/Checkbox 상세 결과

| 항목 | 이전 셀 개수 | 실제 variant 개수 | 조치 |
|---|---|---|---|
| NeoSelect(ComponentSet `387:13`, 스펙 시트 `388:746`) | 4(Content=Placeholder/Selected × State=Default/Open) | 4 — 일치 | 셀 추가/삭제 불필요. Open State 이중 그림자 방지 판단(13절 P4: 트리거 자체엔 그림자 없음, 하위 options-panel만 `Elevation/Raised`) 재확인 — **변경 없음, 이미 정확히 반영돼 있었음**. 내부 auto-layout 컨테이너 6개(HeaderRow/Spacer/LabelCell×4, `403:966`/`403:967`/`403:968`/`403:970`/`403:973`/`403:976`)가 `clipsContent=true`로 남아 있던 것을 발견해 `false`로 정정(루트 `388:746` 자체는 이미 `false`였음). 설명 텍스트(`388:748`)에 13절 P4(Shadow/Hard-2 적용 범위) 반영 누락돼 있어 갱신. |
| Checkbox(ComponentSet `474:899`, 스펙 시트 `475:762`) | 4(State=Default/Checked/Focus/Disabled) | 4 — 일치 | 셀 추가/삭제 불필요. 체크마크(`474:888`) stroke가 `color/ink/900`(`VariableID:95:9`)에 정상 바인딩돼 있음을 재확인 — **13절 P12에서 이미 정정 완료된 상태 그대로, 변경 없음**. 스펙 시트 내 Checkbox 인스턴스 4개(`475:767`/`475:772`/`475:778`/`475:783`) 중 3개가 `clipsContent=true`였던 것을 `false`로 정정(1개는 이미 false). 설명 텍스트(`475:764`)가 "체크마크 색은 후속 검토 필요"라는 stale 문구를 그대로 갖고 있어(13절 P12로 이미 해소된 사안) 최신 상태(Disabled 색 토큰 공식 포함)로 갱신. **⚠ 2026-07-16 재정정(21절)**: 이 표의 "정상 바인딩" 재확인 판단도 이후 21절에서 뒤집혔다 — Box(`474:886`)가 이미 `color/sky/500`으로 확정 디자인과 일치해 있었다는 사실이 반영되지 않은 채 검정(`color/ink/900`) 유지로 재확인된 것으로, 실제로는 체크마크가 `color/text-inverse`(흰색)여야 했다. 상세는 21절 참고. |

**⚠ 2026-07-16 재확인(design-qa HIGH 재발 오탐)**: design-qa가 스크린샷 크롭 판독만으로 체크마크(`474:888`)가 "밝은/흰색 톤"이라고 다시 HIGH 보고했으나, `use_figma` raw script로 재조회한 결과 stroke는 `#1a1a1a`이고 `boundVariable`이 정확히 `color/ink/900`(`VariableID:95:9`)을 가리키고 있음을 재확인했다(15-2절에서 이미 확인된 바인딩과 동일, 변경 없음). `scale:20` 고배율 inline 스크린샷으로도 진한 검정임을 육안 확인 — 35차(13절 P12) 때와 정확히 같은 노드에서 재발한 동일 패턴의 오탐(파란 배경 위 작은 아이콘의 동시대비 착시)이다. 수정 불필요.

**⚠ 2026-07-16 재정정(21절) — 이 "오탐" 판정 자체가 틀렸음이 이후 확인됨**: 21절 재조사 결과 design-qa의 원래 지적("밝은/흰색 톤")이 사실은 유효한 발견이었다 — Box(`474:886`)가 이미 `color/sky/500`(스카이블루)으로 확정 디자인과 일치해 있었는데, 검정 체크마크와 페어링될 근거가 없었다(확정 디자인 login 체크박스는 스카이블루 박스+흰색 체크마크 조합). 여기서 "동시대비 착시"로 기각한 판단은 잘못된 것이었고, 체크마크는 실제로 `color/text-inverse`(흰색)로 재바인딩됐다. design-qa를 상대로 "오탐"이라고 두 차례(35차/이번 배치) 반복 기각한 것은 재발 방지 대상 사례로 남긴다 — 스크린샷 육안 확인이나 boundVariable 재조회만으로 판단을 확정하기 전에, 그 판단의 전제(Box 색이 확정 디자인과 일치하는지)까지 함께 재확인했어야 했다. 상세는 21절 참고.

두 스펙 시트 모두 `get_screenshot`으로 잘림/겹침/빈 셀 없음을 확인했다.

### 15-3. 페이지 전체 겹침 재배치

13개 스펙 시트 루트 프레임(`342:3`/`343:50`/`343:653`/`343:697`/`343:1044`/`343:1106`/`343:1146`/`344:721`/`344:740`/`344:759`/`352:726`/`388:746`/`475:762`) 전부의 x/y/width/height를 `use_figma` 읽기 전용으로 재조회해 y좌표 기준 순차 겹침을 전수 검사했다. **결과: 겹침 0건** — 이전 배치들이 이미 각 시트 크기 변화(NeoBtn 성장 등)에 맞춰 순서대로 40~189px 간격을 유지한 상태였다.

다만 이번 배치에서 NeoSelect(`388:746`) 설명 텍스트를 갱신하며 발견한 문제 — 이 프레임의 루트가 `primaryAxisSizingMode: FIXED`(높이 560 고정, auto-hug 아님)라 텍스트가 6줄로 길어지며 실제 콘텐츠가 프레임 하단(y=560)을 39px 넘어서 시각적으로만 넘치고 있었다(`clipsContent=false`라 잘리지는 않았으나, 선언된 bounding box가 실제보다 작아 다음 시트와의 간격 계산이 부정확해질 위험). `primaryAxisSizingMode`를 `AUTO`로 전환해 프레임을 실제 콘텐츠에 맞게 560→612로 정확히 hug시켰고, 그 결과 새 bottom(6118)이 기존 Checkbox 시작 위치(6112)와 6px 겹치게 돼 Checkbox를 60px 아래(6178)로 재배치해 최종적으로 겹침 0건을 유지했다. `get_screenshot`으로 두 시트 모두 재확인 완료.

### 15-4. 문서 갱신 요약

이번 콜에서 `docs/design/design-system.md`에 반영한 변경(전부 Edit, Write 미사용):
- 0절 인트로에 구 확정 디자인 섹션(`248:11689`) 완전 삭제(14-1절) 사실을 정정 문구로 추가.
- 8절 Legacy 표 뒤에 14-2/14-3절 발견(72개 인스턴스 detach, 14개 고아 마스터, FRAME 전환) 요약과 "활성 레거시 컴포넌트 0개" 결론을 신규 문단으로 추가.
- 신규 15절(이 절) 전체 추가 — 4배치 요약 표, NeoSelect/Checkbox 상세 결과 표, 페이지 겹침 재배치 결과.

`.claude/agent-memory/design-systems.md`도 이번 라운드 최종 로그로 갱신했다(5개 캡 유지, 가장 오래된 항목 제거).

원본 확정 디자인 8개 프레임(`501:2505` 하위)은 이번 15절 작업 전체에서 열람하지 않았다 — Component Specs 페이지 자체가 확정 프레임 밖의 문서화 전용 영역이기 때문이다.

**⚠ 2026-07-16 추가 정리(design-qa MEDIUM)**: Table Row 페이지(`103:3`)의 화면 밖 좌표(x=9000, y=5000)에 남아있던 테스트 스크래치 프레임 `TempVerify`(`549:984`)와 그 안의 COMPONENT 4개(NeoBtn variant와 이름이 완전히 동일한 "Style=Amber/Neutral, Size=Default, State=Default/Focus")를 삭제했다 — Assets/Insert 패널에서 진짜 NeoBtn과 혼동될 위험이 있었다. 삭제 전 파일 전체(29개 페이지)에서 이 4개를 참조하는 INSTANCE가 있는지 확인한 결과 0건이라 Detach 없이 바로 삭제했다(정식 시안·확정 디자인이 아닌 테스트 잔재라 "삭제 금지" 하우스룰 대상 아님). 삭제 후 `get_metadata`로 `103:3`을 재조회해 `549:984`가 사라지고 나머지 정식 컴포넌트(Row Action Button/Table Row Action/Contact Row)는 무손상임을 확인했다.

## 16. ⚠ 사고 기록 — "파일럿" 페이지(`222:524`) 옛 폐기 화면 9개 오삭제 및 하우스룰 재확인 (2026-07-16, 메인 세션 직접 실행, 복구 불가)

**배경**: 사용자가 `342:6`(Component Specs · Spec — NeoBtn) 노드를 가리키며 "이전 디자인과 연결돼 있다"고 지적했으나, 342:6 자체는 인스턴스 바인딩·description·부모 체인 전부 전수 조사 결과 이상 없음(구 확정 디자인 섹션 `248:11689` 참조 0건)으로 확인됐다. 이후 사용자가 실제로 가리킨 대상은 342:6이 아니라 **"파일럿" 페이지 자체**였음이 확인됐다 — 현재 확정 디자인 섹션(`501:2505`)이 같은 페이지 안에서 옛 폐기 화면 9개(`❌ 미채택`/`❌ 폐기 — 사이드바 배경 누락·로고 미반영(2차 재작업본)`/`❌ 폐기 — B-2 레이아웃 미반영(재해석됨)`, Login/Contacts-With Data/Contacts-Empty 3화면 × 3버전)와 나란히 놓여 있어 "연결돼 보인다"는 지적이었다.

**처리(당시) — 잘못된 판단**: 삭제 전 9개 프레임 각각에 COMPONENT/COMPONENT_SET이 포함돼 있는지만 확인하고(전부 0건), "컴포넌트를 포함하지 않는 순수 화면 FRAME은 완전 삭제해도 된다"고 **새로운 예외를 스스로 만들어** 9개 전부 `node.remove()`로 완전 삭제했다.

**⚠ 이것은 명백한 실수였다**: `docs/harness/design-team/figma-file-organization.md` 2-4번 규칙에 이미 "채택되지 않은 시안은 삭제하지 않는다 — 이 규칙에는 예외가 없다"가 명문화돼 있었고, 삭제한 9개는 정확히 그 규칙이 보호 대상으로 지목하는 `❌ 미채택 —`/`❌ 폐기 —` 라벨이 붙은 산출물이었다. "컴포넌트를 포함하는지 여부"는애초에 이 규칙과 무관한 기준인데, 삭제 전 기존 하우스룰을 재확인하지 않고 판단을 내린 것이 원인이다. 삭제 직후 Cmd+Z(Figma 앱 실행 취소)로 복구를 시도했으나 **복구 실패 — 9개 화면(시각 콘텐츠 전체)이 영구 유실됐다.**

**사용자 피드백(2026-07-16)**: "앞으로 디자인 과정은 미채택, 폐기처리하면서 히스토리 남겨두는걸로 해.. 그리고 안쓰는 컴포넌트는 컴포넌트 해제해서 에셋에 보이지 않게 해달라는 거였어" — 애초 요청은 화면 삭제가 아니라 **컴포넌트 해제**(detach+COMPONENT→FRAME 전환, Assets 패널 비노출)였음을 재확인.

**하네스 정정**: `.claude/agents/design-systems.md`의 "컴포넌트 없는 화면 FRAME은 완전 삭제 가능" 판단 기준을 철회하고, "❌ 미채택/❌ 폐기 라벨은 컴포넌트 포함 여부와 무관하게 예외 없이 삭제 금지"로 재확정했다(전역 `~/.claude/agents/design-systems.md`도 동기화). 이후 "필요 없어진 컴포넌트" 요청은 전부 삭제가 아니라 레거시 해제(detach→FRAME 전환) 절차로만 처리한다.

## 17. 미사용 변수 32개 + 텍스트 스타일 6개 `[미사용] ` 접두어 라벨링 (2026-07-16, 사용자 승인 실행 콜)

**배경**: 직전 37차 조사 라운드에서 alias 체인까지 추적 검증해 "진짜 미사용"으로 확정한 변수 32개와 로컬 텍스트 스타일 6개를 대상으로, 사용자가 승인한 실행 작업이다. 범위는 정확히 "이름 앞에 `[미사용] ` 접두어 추가"뿐이며, 값(hex/px 등)·`valuesByMode`·scopes·codeSyntax·description·컬렉션/그룹 구조·어떤 노드의 바인딩도 전혀 건드리지 않았다(순수 rename). `old-사용하지말것` 페이지(`242:2330`)와 확정 디자인 8개 프레임(`501:2505` 하위)은 이번 작업에서 열람·수정 대상이 아니었다.

**변경 내역 — 변수 32개**: 아래 ID를 정확히 지정해 각 변수의 기존 `name`을 그대로 유지한 채 맨 앞에 `[미사용] `만 추가했다.

- Component Tokens(11): `VariableID:97:6`(button-bg-disabled) · `97:7`(button-text-disabled) · `101:2`(select-border-open) · `102:2`(badge-bg-tag) · `103:2`(table-row-border) · `103:91`(navitem-bg-active) · `254:627`(button-border-neutral) · `254:629`(typeselector-family-selected-bg) · `254:630`(typeselector-company-selected-bg) · `269:5`(typeselector-company-selected-text) · `254:631`(typeselector-company-selected-accent)
- Spacing(5): `165:4`(spacing/1-75) · `165:5`(spacing/2-25) · `165:6`(spacing/2-5) · `254:20`(radius/6) · `254:24`(border/heavy)
- Semantic Colors(7): `165:10`(color/text-accent) · `181:693`(color/border-hairline) · `254:625`(color/text-muted-subtle) · `254:626`(color/border-neutral) · `340:3`(color/text-link) · `350:3`(color/border-divider-warm) · `615:134`(color/text-placeholder-strong)
- Primitives(9): `169:2`(color/teal/700) · `181:692`(color/border-hairline-value) · `254:12`(color/green/500) · `254:13`(color/orange/100) · `254:14`(color/orange/500) · `269:3`(color/orange/900) · `350:2`(color/beige/200) · `615:127`(color/gray/375) · `646:2`(color/gray/425)

**변경 내역 — 로컬 텍스트 스타일 6개**: 동일하게 이름 앞에 `[미사용] `만 추가했다. `Wordmark/Logo`(`S:43a77faadaede515f58acfc1e512e47f8029cafd,`) · `Heading/Page`(`S:2498c8e971683370d20e9feb4eae31607c90b917,`) · `Heading/Modal`(`S:eaf31052f111434380567c0bee509d164afc6748,`) · `Label/Micro`(`S:5ceae5805d2eb28085421088b98fd2e94db2a011,`) · `Body/Banner`(`S:1b4caba83fe2377d75d48ae3fd19687aa5587a35,`) · `Body/Caption`(`S:b27e2621151229e0742603ec0831616868e3ae22,`). **참고**: 지시서에 주어진 ID는 트레일링 콤마가 없는 형식(`S:...48`)이었으나 실제 로컬 스타일 ID는 트레일링 콤마 포함 형식(`S:...48,`)이었다 — `getLocalTextStylesAsync()`로 재조회해 정확한 형식을 확인한 뒤 재시도해 성공했다(첫 시도는 6건 전부 "not found"로 실패, 파일 변경 없음 — atomic 원칙대로 재시도만 함).

**FOUNDATIONS 스와치 카탈로그 라벨링**: Colors 페이지(`95:2`)/Spacing 페이지(`95:4`)를 전수 텍스트 검색해, 위 32개 변수 중 대응 스와치 캡션이 있는 것만 골라 동일하게 `[미사용] ` 접두어를 붙였다(캡션 없는 변수는 그대로 둠 — 새로 만들지 않음). 부분 문자열 오검색으로 걸린 `row-action-button-border-neutral`(`436:212`)·`text-link-navy`(`625:1115`) 등 **이름이 겹치지만 실제로는 다른 변수**인 캡션은 정확히 식별해 제외했다. 최종 라벨링 25건:

- Primitives 7종(자체 스와치 카드 name 라인): `650:4`(gray/425) · `625:1101`(gray/375) · `436:54`(orange/900) · `436:58`(green/500) · `436:62`(orange/100) · `436:66`(orange/500) · `436:82`(beige/200)
- Semantic 4종(name 라인만, alias 대상이 비대상 primitive라 name 라인만 라벨링): `436:154`(text-muted-subtle) · `436:158`(text-link) · `436:166`(border-neutral) · `436:200`(button-border-neutral)
- Semantic 2종(alias 대상 primitive도 32개 목록에 포함돼 있어 name+alias 라인 둘 다 라벨링): `436:162`+`436:163`(border-divider-warm / alias beige/200) · `625:1131`+`625:1132`(text-placeholder-strong / alias gray/375)
- Component Tokens 4종 orphan 스와치(name+alias 라인 둘 다 라벨링, alias 대상도 32개 목록 포함): `436:216`+`436:217`(typeselector-family-selected-bg (orphan) / alias green/500) · `436:220`+`436:221`(typeselector-company-selected-bg (orphan) / alias orange/100) · `436:224`+`436:225`(typeselector-company-selected-accent (orphan) / alias orange/500) · `436:228`+`436:229`(typeselector-company-selected-text (orphan) / alias orange/900)
- Spacing 2종: `440:9`(radius/6 (6px)) · `440:23`(border/heavy (3px))

나머지 25개 변수(component tokens 7종 중 button-bg-disabled/button-text-disabled/select-border-open/badge-bg-tag/table-row-border/navitem-bg-active, semantic 2종 text-accent/border-hairline, primitive 2종 teal/700/border-hairline-value, spacing 3종 spacing/1-75/spacing/2-25/spacing/2-5)은 Colors/Spacing 카탈로그에 대응 스와치 자체가 없어(0건) 건드리지 않았다.

**검증**: Figma "Variables" 패널은 캔버스 노드가 아닌 에디터 UI라 `get_screenshot`으로 캡처할 수 없다 — 대신 raw script로 38개(변수 32 + 텍스트 스타일 6) 전부를 재조회해 이름이 정확히 `[미사용] ` 접두어로 시작함을 문자열 단위로 재확인했다(`varAllOk: true`, `styleAllOk: true`). FOUNDATIONS 스와치 캡션 25건은 캔버스 노드라 `get_screenshot`(inline base64)으로 시각 검증했다 — 예: `436:160`(border-divider-warm 스와치)이 "[미사용] border-divider-warm" / "[미사용] alias beige/200"으로 정확히 렌더링됨을 확인. 값(hex/px)·`valuesByMode`·scopes·codeSyntax·description·바인딩은 이번 작업에서 일절 변경하지 않았다.

## 18. NeoBtn Style=Ink 추가 — 헤더 "로그아웃" 버튼 별개 스타일 확정 (2026-07-16)

**배경**: 메인 세션이 main 계열 확정 디자인 5개 프레임(main/main-수정/main-삭제/main-검색없음/main-알림창, 전부 `501:2505` 하위) 전부에서 헤더 "로그아웃" NeoBtn(예: `501:6373`)을 재실측한 결과, 기존 등록된 어떤 Style(Coral/Neutral/Sky/Navy)과도 다른 별개 시각 스타일임을 5개 프레임에서 동일하게 재확인했다 — 우연이 아니라 확정된 디자인 패턴이다. 0-20절/0-25절 TODO("헤더 로그아웃 NeoBtn 이례값")를 이번에 정식 반영해 해소했다.

**실측값(확정 디자인 근거)**: fills 단색 `#1a1a1a`(ink, 기존 raw), strokes 없음(무보더 — 실측 시 amber stroke가 존재했으나 `visible:false`로 비활성 상태였음), 텍스트 색 `#ffffff`, 크기 79×25(기존 NeoBtn Size=Compact 축 재사용), cornerRadius 8(기존 NeoBtn 다른 Style의 10과 다름 — 실측값 그대로 따름). 원본 인스턴스에는 `PxLogout` 아이콘(12×12)이 텍스트 앞에 붙어 있었으나, NeoBtn 마스터 구조 자체가 아이콘 슬롯을 지원하지 않아(다른 4개 Style도 텍스트 전용) 이번 작업 범위 밖으로 판단, 아이콘은 추가하지 않았다(텍스트 전용 버튼으로 등록).

**신규 variant — Style=Ink, Size=Compact 전용, State 6개 전부 완성**(NeoBtn `259:126`):

| State | 노드 ID | 배경 | 텍스트 | 보더 | 효과 |
|---|---|---|---|---|---|
| Default | `791:7` | `color/ink/900`(`VariableID:95:9`, #1A1A1A) | `color/text-inverse`(`VariableID:219:2`, #FFFFFF) | 없음 | 없음 |
| Hover | `791:862` | raw #353535(unbound, 아래 블렌드 방향 결정 참고) | 동일(text-inverse) | 없음 | 없음 |
| Press | `791:864` | raw #515151(unbound) | 동일 | 없음 | 없음(그림자 원래도 없음) |
| Focus | `791:866` | Default와 동일(순수성 원칙) | 동일 | 없음 | 2겹 `DROP_SHADOW`(ink spread4 + 흰 갭 spread1) + `FocusRing` 자식 RECTANGLE(strokeWeight3, `color/ink/900`, cornerRadius14.5, x/y -4.5, layoutPositioning ABSOLUTE) — 9-1절/34차 공식 그대로, 대응 상태(Default) clone 후 효과만 추가 |
| Disabled | `791:869` | `color/bg-disabled`(`VariableID:643:2`, 현재 alias #BBBBBB) | `color/text-disabled`(`VariableID:643:4`, #555555) | 없음(원래도 무보더) | 없음 |
| Loading | `791:871` | Default와 동일(opacity만 0.7) | 동일 | 없음 | 없음 |

**Hover/Press 블렌드 방향 — 9-1절 공식의 예외적 적용 판단(문서화)**: 9-1절 공식은 "배경을 ink 쪽으로 블렌드"인데, Ink 배경은 이미 그 블렌드 목표값(ink) 자체라 문자 그대로 적용하면 무변화(no-op)가 된다. 이는 기존 5개 Style(브랜드색·흰색 배경)에는 없던 케이스다. 시니어 판단으로, 상호작용 시 시각적 피드백이 반드시 있어야 한다는 원칙(9-1절의 목적)을 우선해 **블렌드 목표를 반대 극(흰색)으로 대체**했다 — 강도(t=12%/24%)는 원 공식 그대로 유지, 방향만 "어두운 배경은 상호작용 시 살짝 밝아진다"는 통상적 다크 UI 관례로 대체했다. 계산: `mix(ink, white, 0.12)` = rgb(53,53,53)(#353535), `mix(ink, white, 0.24)` = rgb(81,81,81)(#515151). 값은 raw unbound로 저장(기존 Hover/Press 패턴과 동일 — 이 두 상태는 전 컴포넌트에서 항상 raw 값, 토큰 미바인딩 관례를 그대로 따름). Press는 그림자 제거 규칙도 적용했으나 Default에 원래 그림자가 없어 실질 변화 없음(Neutral/보조 버튼 계열과 동일한 무그림자 컨벤션).

**WCAG 대비 계산(상대휘도 공식 직접 계산, 전 State 검증)**:
- Default/Focus/Loading: `color/text-inverse`(#FFFFFF) on `color/ink/900`(#1A1A1A) = **17.78:1 PASS**(4.5:1 기준 큰 폭 초과).
- Hover(#353535) + 흰 텍스트: **12.17:1 PASS**.
- Press(#515151) + 흰 텍스트: **7.94:1 PASS**.
- Disabled: `color/text-disabled`(#555555) on `color/bg-disabled`(#BBBBBB) = **3.88:1** — 0-24절에서 이미 전 컴포넌트 공통으로 확인된 값과 동일(사용자 승인으로 WCAG 완화 적용 중인 기존 결정을 그대로 승계, Ink 전용 신규 이슈 아님).
- Focus 링(ink #1A1A1A) on 흰 배경: 기존 다른 Style Focus 링과 동일하게 17.78:1 수준 PASS(비텍스트 3:1 기준 큰 폭 초과).

**주요 함정 발견 및 정정(작업 중 실측)**: NeoBtn의 TEXT 컴포넌트 프로퍼티(`Label#259:0`)는 Style별로 독립된 기본값을 갖지 못하고 ComponentSet 전체가 **하나의 공유 값**을 쓴다는 것이 이번 작업 중 실측으로 확인됐다(Figma TEXT 컴포넌트 프로퍼티의 플랫폼 동작 — Style마다 별도 텍스트를 가진 것처럼 보였던 기존 "검색"/"전체"/"추가" 등은 전부 실제로는 화면 인스턴스 단위 오버라이드였고, 마스터 자체는 항상 "검색" 하나로 통일돼 있었다). 최초 시도에서 Ink Default 텍스트를 "로그아웃"으로 직접 설정했더니 Coral/Neutral/Sky/Navy 등 **다른 모든 Style의 마스터 표시 텍스트가 전부 "로그아웃"으로 동시에 바뀌는** 부작용이 실측됐다 — 발견 즉시 원복(Coral Default 텍스트를 "검색"으로 재설정)해 공유 기본값을 원래대로 복구했고, 재조회로 전 Style이 "검색"으로 정상 복구됐음을 확인했다. **결론**: Ink variant도 마스터 표시 텍스트는 공유값 "검색" 그대로 두고, 실제 "로그아웃" 표시는 기존 관례(전체/추가/검색과 동일)대로 화면 인스턴스에서 텍스트 프로퍼티를 오버라이드하는 방식으로 처리한다(ui-designer 몫).

**스펙 시트 갱신**: `Spec — NeoBtn`(`342:3`)의 Grid(`342:6`)에 "Ink / Compact" Row(`792:801`, 6칸: Default/Hover/Press/Focus/Disabled/Loading)를 신규 추가 — 기존 "Neutral / Compact" Row를 clone 후 각 Cell의 INSTANCE를 `instance.swapComponent()`로 신규 Ink variant 6개에 교체(라벨 텍스트는 기존 Default/Hover/Press/Focus/Disabled/Loading 순서 그대로 재사용, clipsContent 전부 false 유지 확인). 설명 텍스트(`342:5`)에 이번 추가 배경과 4→5 Style, 36→42 variant 갱신 문구 추가. Grid/Spec 루트 모두 기존부터 auto-layout hug라 자동 리플로우(root 606→740). `get_screenshot`으로 7개 Row(Coral/Neutral × Default/Compact, Sky/Navy Default, Ink Compact) 42칸 전체가 잘림·겹침 없이 정상 렌더링됨을 확인. NeoBtn ComponentSet `description` 메타데이터에도 이번 추가 사실과 Hover/Press 블렌드 방향 결정을 기록했다.

**결론**: NeoBtn(`259:126`) 최종 variant **36→42**, Style 옵션 `["Coral","Neutral","Sky","Navy","Ink"]` 5개. Size=Compact는 이제 Coral/Neutral/Ink 3개 Style에 존재(Sky/Navy는 Default만, 기존 그대로). Button(`259:609`)·확정 디자인 8개 프레임(`501:2505` 하위)은 이번 라운드에서 전혀 수정하지 않았다(로그아웃 버튼 재실측은 메인 세션이 사전에 완료해 전달, 이번 콜에서는 열람하지 않음).

## 19. ⚠ Focus 링 cornerRadius 불일치 2건 정정 (2026-07-16, 메인 세션 직접 실행)

**배경**: 사용자가 Component Specs 페이지(`342:3`)에서 NeoBtn Ink/Compact Focus의 검은 링이 "틀어져 보인다"고 지적. 원인 확인 결과 9-1절 Focus 링 공식이 `cornerRadius = 버튼 radius + 4.5`(offset 4.5)로 계산돼야 하는데, Ink Style 추가 시 다른 Style(버튼 radius 10 → 링 14.5)의 링 값을 그대로 복사해 왔고, Ink는 버튼 radius가 8(확정 디자인 실측값, 18절 참고)로 달라 링이 12.5여야 했던 게 14.5로 남아 모서리가 어긋나 보였다.

**전수 재확인**: 사용자 요청으로 파일 전체 17개 ComponentSet 중 Focus variant를 가진 전부를 스캔(`버튼 cornerRadius + ring offset` 공식과 실제 ring cornerRadius 대조). 결과 2건 추가 발견:
- NeoBtn Style=Ink, Size=Compact, State=Focus(`791:866`): 버튼 radius 8, 링 14.5(오류) → **12.5로 정정**
- Icon Button Type=Close, State=Focus(`284:1040`): 버튼 radius 0(각진 사각형), 링 14.5(오류) → **4.5로 정정**

**오탐 제외**: Sidebar Nav Item State=Focus(`287:17`)도 공식상 불일치로 걸렸으나, 9-5절에 이미 "3px ink OUTSIDE 스트로크로 링 구현(DROP_SHADOW 방식이 아닌 의도적 예외)"로 문서화된 항목이라 결함이 아님 — 스캔 공식이 이 예외를 반영하지 못한 것뿐.

**처리**: 마스터 컴포넌트의 FocusRing 자식 rectangle `cornerRadius`만 수정(fills/strokes/위치/크기 등 다른 속성 무변경). Component Specs 스펙 시트(`342:3`)를 포함해 두 컴포넌트를 참조하는 모든 인스턴스에 자동 반영됨을 `get_screenshot`으로 확인(마스터 하나만 고치면 인스턴스 전부에 전파되는 토큰/컴포넌트 바인딩 구조가 정상 동작함을 재확인한 사례이기도 하다).

**교훈**: Focus 링 공식을 새 Style/컴포넌트에 복사할 때는 버튼 자체의 `cornerRadius`가 기존 패턴(주로 10)과 다르면 링 radius도 `버튼 radius + 4.5`로 반드시 재계산해야 한다 — 고정값 14.5를 그대로 복사하지 않는다.

## 20. 미사용 컬러 변수 27개 완전 삭제 (2026-07-16, 사용자 명시적 지시, 메인 세션 직접 실행)

**배경**: 이전 라운드(0-25절 이전 별도 라운드)에서 harness-auditor가 확정 디자인 어디에도 참조되지 않는 컬러 변수 27개(Component Tokens 11 + Semantic Colors 7 + Primitives 9)를 발견해 `[미사용] ` 접두어로 라벨링만 하고 실제 삭제는 보류했었다. 이번 라운드에서 사용자가 FOUNDATIONS Colors 페이지(`95:40`)를 직접 보고 "확정 디자인에서 빠진 컬러는 삭제해달라"고 요청, 대상 목록을 먼저 보고한 뒤 "진짜로 삭제해줘"로 명시적 승인받아 실제 삭제를 진행했다(라벨링에 그쳤던 기존 방침을 사용자가 이번에 직접 뒤집은 것).

**처리**: `figma.variables.getLocalVariablesAsync("COLOR")`로 `[미사용] ` 접두어 붙은 변수 27개 전부 확인 후 `.remove()` 호출. **⚠ 플랫폼 제약 재확인(컴포넌트와 동일 패턴)**: key가 있는(퍼블리시 가능한) 변수는 `.remove()`로도 물리적으로 완전히 삭제되지 않는다 — 호출 자체는 성공하지만 변수 객체는 존속하고, 소속 `VariableCollection.variableIds` 목록에서만 제외된다(실측 확인: 테스트 삭제한 `[미사용] color/gray/425` 이후 `getVariableByIdAsync`로 재조회해도 객체가 그대로 반환됨, 단 `variableIds.includes(id)`는 `false`). 실질적 효과는 Variables 패널/Assets에서 완전히 사라지는 것과 동일 — 컴포넌트 key 삭제 제약(14-3절)과 같은 라이브러리 키 레지스트리 무결성 보호 메커니즘으로 판단된다.
Colors 페이지(`95:40`)의 대응 스와치 셀도 27개 중 17개는 실제로 페이지에 시각 카탈로그로 존재해 함께 제거했다(Primitives 7 + Semantic 5 + Component Colors 5). 나머지 10개(button-bg-disabled/button-text-disabled/select-border-open/badge-bg-tag/table-row-border/navitem-bg-active/text-accent/teal-700/border-hairline-value/border-hairline)는 변수만 등록돼 있고 이 페이지에 시각 스와치가 애초에 없었다(별도 라운드에서 변수만 선언되고 카탈로그 등록이 누락됐던 것으로 추정) — 변수 자체는 위 방식으로 동일하게 제거했다.
"Component Colors" 섹션 설명 텍스트(`436:196`)가 "orphan 4개는... 미사용 상태로 보존"이라고 서술하던 것을 "orphan 4개는 2026-07-16 실사용처 없음 확인되어 완전 제거"로 정정했다(그 4개 orphan 스와치 자체를 이번에 지웠으므로).

**결과**: Primitives 39→32칸, Semantic Colors 32→27칸(스와치 기준), Component Colors 8→3칸(정상 사용 중인 typeselector-unselected-text/border, row-action-button-border-neutral만 남음). `get_screenshot`으로 페이지 전체 레이아웃이 깨지지 않고 정상 재배치됐음을 확인.

**하네스 판단 기준 정정**: 기존 "미사용 변수는 라벨링만, 삭제 안 함" 기본 방침은 유지하되(design-systems.md 참고), 사용자가 대상 목록을 직접 확인한 뒤 명시적으로 삭제를 지시하면 그때는 실제 삭제(플랫폼이 허용하는 한도 내에서)를 실행한다 — 화면 목업/시안(미채택·폐기 라벨) 삭제 금지 하우스룰과는 별개 범주다(토큰은 디자인 의사결정 히스토리가 아니라 죽은 코드에 가까운 성격).

## 21. Checkbox 체크마크 색상 재정정 — 13절 P12 결론 정정, `color/text-inverse` 재사용 (2026-07-16, 메인 세션 확인 후 신뢰 위임 실행)

**배경**: 13절 P12은 "Checked 체크마크 stroke를 `color/border-divider-cool`→`color/ink/900`(검정)으로 정정, 마스터는 검정 유지"로 결론냈었다. 그런데 이 판정은 Checkbox Box(`474:886`)가 **이미 `color/sky/500`(#1395E6, `VariableID:615:122`)으로 확정 디자인과 정확히 일치하도록 바인딩돼 있었다는 사실**(0-20절 Stage2에서 반영 완료)을 놓친 채 내려졌다. 메인 세션이 마스터를 재확인한 결과, 확정 디자인 login 체크박스(`604:5953` 박스 #1395E6 / `604:5954` 체크마크 #ffffff)는 스카이블루 박스 + 흰색 체크마크 조합이 유일한 근거이며, 검정 체크마크로 남겨둘 근거가 없었다.

**처리**: Checkbox ComponentSet(`474:899`) State=Checked(`474:896`) 마스터 안, 체크마크의 실제 렌더링 노드를 재정정했다. 체크마크는 0-26절에서 raw VECTOR→`Pixel/Check`(`815:2`) 정식 Icon 컴포넌트의 INSTANCE(`815:3`)로 이미 리토피트돼 있었으므로, 인스턴스 최상위가 아니라 그 안의 실제 렌더링 VECTOR 자식(`I815:3;814:3`)의 stroke를 `color/ink/900`(`VariableID:95:9`)→`color/text-inverse`(`VariableID:219:2`, #FFFFFF)로 재바인딩했다. **신규 토큰 등록 없음** — `color/text-inverse`는 이미 등록돼 있던 기존 semantic 토큰을 재사용했다(resolvedHex 정확히 #FFFFFF 확인). Box(`474:886`)의 `color/sky/500` 바인딩과 다른 3개 State(Default/Focus/Disabled)는 이번 작업에서 전혀 손대지 않았다.

**검증(자체 재대조, design-systems 규칙)**:
- 재조회 결과 `I815:3;814:3`의 `strokes[0].boundVariables.color.id` = `VariableID:219:2`, resolvedColor `{r:1,g:1,b:1}` — 기대값과 정확히 일치.
- `node.screenshot({scale:20})` 고배율 inline 스크린샷으로 스카이블루 박스 위 흰색 체크마크가 뚜렷하게 렌더링됨을 육안 확인.
- ComponentSet 전체(`474:899`, scale 4) 스크린샷으로 Default/Focus/Disabled 3개 State가 이번 변경과 무관하게 기존 그대로임을 확인 — Default(빈 박스)/Focus(ink 링)/Disabled(회색 박스) 전부 무손상.
- `Component Specs` 페이지의 `Spec — Checkbox`(`475:762`)는 인스턴스 기반 4칸 그리드라 마스터 수정이 자동 전파됨을 스크린샷으로 확인 — Checked 셀이 흰 체크마크로 정상 반영됨. 스펙 시트 설명 텍스트(`475:764`)도 13절 P12의 stale 서술("stroke를 color/ink/900으로 정정")을 이번 재정정 배경으로 갱신했고, 텍스트가 길어지며 하단 Grid와 겹치던 것을 발견해 Grid를 아래로 재배치 + 루트 프레임 높이(234→330)를 재조정해 겹침을 해소했다(페이지 내 다른 12개 스펙 시트와의 겹침도 재확인 — 0건, Checkbox가 페이지 최하단이라 영향 없음). Checkbox ComponentSet(`474:899`) `description` 메타데이터에도 이번 재정정 사실을 추가 반영했다.

**WCAG 확인**: `color/text-inverse`(#FFFFFF) 체크마크가 `color/sky/500`(#1395E6) 배경 위에 얹히는 비텍스트 아이콘 대비는 기존 0-20절에서 "ink 보더 on sky/500 = 5.36:1 PASS"로 이미 계산된 것과 별개로, 흰색 on sky/500 = ~~**2.72:1**로 WCAG 1.4.11 비텍스트 3:1 기준에는 못 미친다.~~ 다만 이 조합은 확정 디자인(사용자 원본, `604:5953`/`604:5954`)에 실제로 쓰인 값을 그대로 옮긴 것이라 — 2-4번 규칙(확정 디자인 실측값을 임의로 재해석하지 않고 그대로 추출)에 따라 임의로 다른 색으로 바꾸지 않았다. 참고로만 기록한다.

**⚠ 2026-07-17 정정(design-qa 감사)**: 위 "2.72:1, 미달" 계산은 오류였다 — design-qa가 WCAG 상대휘도 공식(sRGB 감마 보정 → 선형 RGB → 가중합 → `(L1+0.05)/(L2+0.05)`)으로 흰색(#FFFFFF) on `color/sky/500`(#1395E6)을 독립 재계산한 결과, 실제 대비는 **약 3.25:1**이다(design-systems가 동일 공식으로 재검증: L(sky/500)≈0.2735, `(1.0+0.05)/(0.2735+0.05)`≈3.246). 즉 결론은 "미달"이 아니라 **"WCAG 1.4.11 비텍스트 3:1 기준 충족(마진 0.25로 근소)"**으로 뒤바뀐다. 마진이 좁아 향후 `sky/500` 톤(#1395E6)을 조정할 경우 이 대비가 3:1 아래로 떨어질 수 있으니 재검토가 필요하다 — 톤 조정 라운드마다 이 조합을 다시 계산해 확인할 것. 기존 오기록은 삭제하지 않고 취소선으로만 표시해 보존했다(house rule).

**교훈**: 인스턴스 단위 오버라이드 여부를 결정하기 전에, 확정 디자인에서 그 요소의 정확한 컬러를 실측 추출 → 기존 토큰 중 일치하는 게 있는지 확인(없으면 신규 등록) → 그 토큰을 적용하는 순서를 반드시 거쳐야 한다. "마스터는 캐논 값 유지, 인스턴스에서만 오버라이드"라는 기존 원칙(2절 "색상 등 시각 속성도 인스턴스 단위 오버라이드로 처리한다" 참고)은 "어떤 값이 캐논이고 어떤 게 예외 컨텍스트인지"를 확정 디자인 실측으로 먼저 확인한 뒤에만 적용해야 한다 — 실측 없이 어림짐작으로 마스터 값을 정하고 인스턴스 오버라이드로 미루면, 이번처럼 마스터 자체가 확정 디자인과 어긋난 채 방치될 수 있다. 이 교훈은 `.claude/agents/design-systems.md`(프로젝트 로컬 + 전역)에도 판단 기준으로 반영했다.

원본 확정 디자인 8프레임(`501:2505` 하위)은 이번 작업에서 열람하지 않았다 — 필요한 실측값(Box #1395E6/체크마크 #FFFFFF)이 메인 세션에서 이미 확인돼 전달됐기 때문이다.

## 22. FOUNDATIONS 문서화 페이지 시각 포맷 표준화 — Colors 페이지 cornerRadius/보더 혼재 해소 + 신규 포터블 가이드 신설 (2026-07-16, design-pl 실행 브리프)

**배경**: 사용자가 지적한 문제는 컴포넌트/토큰 설계 자체가 아니라 **문서화 페이지의 시각 서식**이었다 — Colors 페이지 Primitives Row(`95:44`) 스와치 중 일부는 cornerRadius가 있고 일부는 없어 카탈로그가 들쭉날쭉했다. "정돈이 잘 된 예시"로 지목된 `116:6`은 실측 결과 Component Specs 페이지가 아니라 **Elevation 페이지 루트**(`116:5` 하위 "Elevation — Design Tokens" 프레임)였다 — 브리프 작성 시점 이후 여러 차례 페이지/노드 재구성이 있어 ID 매핑이 stale해진 것으로 판단되나, 실제로 열어본 결과 이 프레임 자체는 제목+한줄설명 → Primitives 섹션 → Semantic 섹션 → 적용 가이드 텍스트 → Hard Shadows 섹션 → Hover/Press/Focus 공식 섹션 순서로 일관되게 정돈돼 있어, "잘 정돈된 문서화 페이지"의 실제 참고 사례로는 여전히 유효했다.

### 22-1. 실측 비교 (1단계)

**Colors Primitives Row(`95:44`, 33개 스와치) — 항목 단위 실측**:

| 항목 | 다수 스타일(28개 스와치, 기존 `95:x`/`436:x` ID) | 소수 이례값(5개 스와치, `625:1079`~`625:1096` — sky/500·navy/700·amber/600·paleblue/100·paleblue/50) |
|---|---|---|
| cornerRadius | 8 | **0** |
| 보더 | 1px solid `#DBE0E0` | **없음(strokes 0개)** |
| 컨테이너 크기 | 88×91~92 | 88×91 (동일) |
| 라벨 배치 | 이름 줄(10px Medium) → hex 줄(10px 또는 9px Regular), 둘 다 `color/text-secondary` 톤 | 동일 순서·톤(차이 없음) |

Semantic Row(`95:123`)에도 같은 패턴의 이례값 6개(`625:1105`~`625:1126` — bg-brand-blue·bg-accent-navy·text-link-navy·border-divider-cool·bg-row-alt·bg-cta-amber)가 동일하게 cornerRadius 0·보더 없음으로 확인됐다. Category Colors(`436:93`)·Component Colors(`436:197`) 그리드는 전수 조회 결과 33개 스와치 전부 cornerRadius 8·보더 있음으로 이미 일관돼 있어 대상 아님.

**원인 추정**: 두 이례값 그룹(`625:1079`~/`625:1105`~) ID 접두어가 동일(`625:`)한 걸로 보아, 같은 라운드에서 "값만 채워 넣고 서식은 나중에 맞추자"는 식으로 급하게 추가된 뒤 후속 정리가 누락된 것으로 판단된다 — 컴포넌트/토큰 값 자체(hex)는 정확했고 서식만 어긋나 있었다.

**Elevation 페이지(`116:5`, `116:6`) — 참고 사례로 관찰한 구성 패턴**: 제목(볼드, 큰 사이즈) + 한 줄 설명(회색, 제목 바로 아래) → 섹션 헤더(볼드, 본문보다 약간 큰 사이즈)+ 그 섹션 내용을 반복하는 구조. 색상 프리미티브가 아닌 그림자 프리미티브(blur/offset/spread 등 숫자값)는 텍스트로만 나열하고, 색상이 있는 항목(shadow/color/ink-8 등)만 작은 데모 박스+라벨로 표시 — 스와치 카탈로그와 그림자 전용 카탈로그의 "적절한 표시 방식이 다를 수 있다"는 걸 보여주는 사례였다. 섹션마다 옅은 회색 배경 카드로 시각적 구획을 나눈 것도 일관됐다.

### 22-2. 신규 가이드 문서

`docs/harness/design-team/figma-page-format-guide.md`를 신규 작성했다(포터블 — 이 프로젝트의 실제 노드 ID나 채택 픽셀값을 하드코딩하지 않음). 담은 원칙:
1. 스와치 카탈로그는 카탈로그 전체에서 cornerRadius·보더 유무/색/굵기·크기·라벨 배치·gap을 하나로 통일한다(새 스와치는 기존 스와치를 clone해서 만든다).
2. 컴포넌트 스펙 시트는 제목→설명→전체 variant 그리드(상태 라벨 포함)→여백 순서로 통일하고, ComponentSet의 실제 variant 개수와 그리드 셀 개수를 항상 일치시킨다.
3. 같은 문서화 구역 안에서는 프레임 정렬 기준선·프레임 간 여백을 통일한다.
4. 모든 문서화 컨테이너는 `clipsContent=false`.
5. 신규/갱신 시 확인할 체크리스트로 마무리.

`figma-file-organization.md` 2-5번(스펙 시트 규칙)·clipsContent 원칙과 상충하지 않고 서식 관점에서 구체화하는 관계로 작성했다.

### 22-3. Colors 페이지 실제 정리 (3단계)

`use_figma` 스크립트로 이례값 11개 RECTANGLE 노드(Primitives 5개 + Semantic 6개)의 `cornerRadius`를 8로, `strokes`를 다수 스타일과 동일한 `{r:0.8588235378265381,g:0.8784313797950745,b:0.8784313797950745}`(#DBE0E0) 1px SOLID로 직접 설정했다 — 새 원시값/변수 추가 없음, 기존 다수 스타일 값을 그대로 복제 적용한 순수 서식 정리다. 대상 ID: Primitives Row `625:1080`/`625:1084`/`625:1088`/`625:1092`/`625:1096`, Semantic Row `625:1106`/`625:1110`/`625:1114`/`625:1118`/`625:1122`/`625:1126`.

**Before**: sky/500·navy/700·amber/600·paleblue/100·paleblue/50(Primitives)과 bg-brand-blue·bg-accent-navy·text-link-navy·border-divider-cool·bg-row-alt·bg-cta-amber(Semantic) 11개 스와치가 각진 모서리+무보더로 나머지 28+27개 스와치와 시각적으로 튀어 보였다.

**After**: `get_screenshot`(`95:40` 전체, inline)으로 재확인한 결과 11개 스와치 전부 다른 스와치와 동일한 둥근 모서리+연회색 보더로 렌더링됨을 확인 — Colors 페이지 Primitives Row/Semantic Row 전체가 시각적으로 통일됨. Category Colors/Component Colors 그리드는 이번에도 무수정(이미 일관 상태 확인됨).

### 22-4. Component Specs 페이지 — 이번 라운드 재확인만(신규 결함 없음)

15절(2026-07-16)에서 이미 13개 스펙 시트 전수를 4배치로 재검증해 `clipsContent=false`·variant-그리드 셀 개수 일치를 확인해 둔 상태였다. 이번 라운드는 그 결과를 재신뢰하고 별도 재작업은 하지 않았다 — 브리프가 예시로 든 "116:6"이 실제로는 Component Specs가 아니라 Elevation 페이지였던 것으로 확인됐고(22-1절), Component Specs 페이지 자체의 신규 서식 결함은 이번 조사에서 발견되지 않았다.

### 22-5. 완료 기준 체크

(a) `figma-page-format-guide.md` 포터블 신규 작성 완료(노드 ID/프로젝트 고유 픽셀값 미포함). (b) Colors 페이지(`95:44` Primitives Row + `95:123` Semantic Row) cornerRadius·보더 혼재 11건 전부 해소, 스크린샷 확인 완료. (c) 이 22절로 조사 근거·채택 값(cornerRadius 8, 보더 #DBE0E0 1px)·before/after 기록 완료.

원본 확정 디자인 8개 프레임(`501:2505` 하위)은 이번 작업에서 전혀 열람하지 않았다 — 이번 라운드는 FOUNDATIONS 문서화 페이지의 서식 정리에 한정된 작업이었다.

## 23. 확정 디자인 8개 프레임 전체 재대조 라운드 — Card AccentStrip-Bottom + Pixel/NoResult 리바인딩, 참고 문서 노드 ID 갱신 (2026-07-16, brand-designer+메인세션 공동 발견)

**배경**: 확정 디자인 8개 프레임이 이전에 `248:11689`(구, 14-1절에서 완전히 삭제됨)에서 `501:2505`(신, 0-20절 Stage2)로 교체됐고, 이 문서 0-20절에서 대부분의 토큰 바인딩을 정리했다. 그런데 별도 문서 `docs/design/confirmed/user-confirmed-final-design.md`(원본 최상단 노드 ID 표)은 여전히 구 노드 ID를 참조하고 있어 이번 라운드에서 갱신했다. brand-designer가 신규 8개 프레임을 재관찰해 기존 문서와 대조한 결과, 실제 작업이 필요한 항목은 아래 A/B 2건뿐이었고 나머지 관찰은 이미 0-20/0-25절에서 처리 완료됐거나 컴포넌트화 제외 방침으로 정리돼 있던 항목이었다.

**A) Card(`262:15`) Type=Auth AccentStrip-Bottom(`262:14`) 리바인딩**: 재실측 결과 fill이 `color/sky/500`이 아니라 teal/500(`VariableID:95:6`, #17A398)에 잘못 바인딩돼 있음을 발견 — login(`501:5184`)/Join(`501:4936`) 원본 실측값(#1395e6)과 불일치. 이미 존재하는 `color/sky/500`(`VariableID:615:122`) 토큰으로 리바인딩(신규 토큰 생성 없음). 재조회로 hex `#1395e6`·boundVariableId `VariableID:615:122` 일치 확인 — 5절 컴포넌트 표에 각주 반영 완료.

**B) Icons 페이지 `Pixel/NoResult`(`255:149`) 몸통 리바인딩**: 마스터 몸통(돋보기 실루엣, vector 21개, `255:122`~`255:142`)이 raw teal(#17A398, 미바인딩)에 남아 있음을 발견 — 확정 프레임 `501:4218` 내부 인스턴스 `517:2722`(FRAME, 화면조립 raw 요소) 실측값(#1395E6, 몸통 21개+크랙 6개로 벡터 개수까지 정확히 일치)과 불일치. `color/sky/500`(`VariableID:615:122`)으로 21개 vector 전부 리바인딩(신규 토큰 없음). 크랙 6개(`255:143`~`255:148`, 코랄 #FF5A76)는 원본과 이미 일치해 무수정. 4절 Icons 목록에 각주 반영 완료.

**C) `docs/design/confirmed/user-confirmed-final-design.md` 갱신**: ① 확정 8개 프레임 노드 ID 표를 신규 세트(`501:6008`/`501:3042`/`501:3636`/`501:4218`/`501:4692`/`501:4940`/`501:5188`/`501:6548`, 부모 `501:2505`)로 교체하고 구 ID(`214:349` 등, `248:11689` 하위 — 14-1절에서 삭제됨)를 각주로 보존. ② 2-1절 "Primary 틸" 행에 사이드바/배경/카드 하단 스트립이 이후 스카이블루로 전환됐다는 각주 추가. ③ 4-2절 "카드 상/하단 액센트 스트립" 문장에 하단 스트립이 실제로는 스카이블루(#1395e6)라는 정정 각주 추가. ④ 2-3절(TypeSelector 불일치)에 0-9절에서 이미 뒤집힌 과거 결정임을 명시하는 각주 추가. ⑤ 9절(아이콘 계층) "빈 상태 그래픽... 틸+코랄" 문장에 실제로는 "스카이블루+코랄"이라는 정정 각주 추가(B작업과 연동). ⑥ 10-3절(main-삭제 모달)에 카드 상단 스트립이 여전히 구 앰버(#FFCB47)라는 0-20절 기존 known gap 재확인 각주 추가. 원본은 삭제 없이 전부 각주로만 정정 — 원문은 그대로 보존.

**손대지 않은 것(이미 해소됐거나 방침상 제외)**: 사이드바/배경/전체·추가버튼/테이블 구분선의 틸→스카이블루 전환은 이미 0-20/0-25절에서 처리 완료(NeoBtn Navy/Sky, Contact Row `border-divider-cool`) 또는 raw 화면조립 요소라 컴포넌트화 제외 방침(0-20절 "추가 관찰" ①)으로 정리돼 있어 재작업하지 않았다. main-삭제(`501:3636`) 모달 상단 스트립(`501:4174`)의 구 앰버(#FFCB47)는 0-20절에 이미 기록된 known gap이라 원본 read-only 방침상 이번에도 손대지 않고 재확인만 했다. TypeSelector(2-3절 문서 서술)는 0-9절로 이미 CatBadge와 통일 완료돼 있어 Figma 쪽 변경은 불필요, 문서 텍스트 정정만 진행했다.

**자체 재대조(design-systems 규칙, 생략 불가)**: A/B 리바인딩 직후 각각 `use_figma` 읽기 전용으로 재조회해 boundVariableId와 resolvedHex가 기대값과 정확히 일치함을 확인했다(Card 위 표 참고, Icons 위 문단 참고). 원본 확정 8개 프레임(`501:2505` 하위)은 이번 라운드에서도 읽기 전용으로만 관찰했고 전혀 수정하지 않았다.

## 24. design-qa 4항목 감사 후 결함 3건 정정 (2026-07-17)

design-qa가 최근 4개 항목(Checkbox 체크마크 리바인딩, Colors 페이지 스와치 바인딩+cornerRadius 통일, Card AccentStrip-Bottom 리바인딩, Pixel/NoResult 아이콘 리바인딩) 감사에서 핵심 바인딩은 전부 정상 확인했으나, 아래 3건의 문서/캡션 결함을 발견해 이번 라운드에서 정정했다.

1. **Colors 페이지 `color/ink/900` 스와치 캡션 오표기(`95:60`)** — 캡션 텍스트가 별도 토큰 `color/ink/800`(`436:4`~`436:7`)의 값과 동일한 "#1C1F21"로 잘못 표기돼 있었다. 실제 Rectangle(`95:58`)은 `color/ink/900`(`VariableID:95:9`, #1A1A1A)에 정확히 바인딩돼 있어 캡션만 값과 어긋난 상태였다 → 텍스트/노드 이름을 "#1A1A1A"로 정정(폰트 로드 후 `characters` 변경, `use_figma` 재조회로 반영 확인).
2. **`Pixel/NoResult`(`255:149`) 컴포넌트 description 미갱신** — 몸통 vector 21개는 이미 23절(A/B)에서 raw teal → `color/sky/500`으로 리바인딩됐는데, 컴포넌트 description은 여전히 "틸+코랄 2색"으로 남아 있었다(확정 스펙 문서 각주는 이미 정정된 상태, 컴포넌트 description만 누락). → description을 "스카이블루+코랄 2색"으로 정정.
3. **21절 WCAG 대비 계산 오류** — 21절이 "text-inverse(#FFFFFF) on sky/500(#1395E6) = 2.72:1, 3:1 미달"로 기록했으나, design-qa가 WCAG 상대휘도 공식으로 재계산한 결과 실제로는 약 3.25:1로 3:1 기준을 근소하게(마진 0.25) 통과한다. design-systems가 동일 공식으로 독립 재검증해 일치를 확인 — 21절에 취소선+정정 각주로 반영(기존 오기록은 삭제하지 않고 보존).

3건 모두 원본 확정 디자인 8개 프레임(`501:2505` 하위)과 무관한 문서/캡션 정정이라 원본 프레임은 이번에도 열람하지 않았다. 자체 재대조: 1)/2)는 `use_figma` 읽기 전용 재조회로 변경 후 값(characters/description)이 기대값과 정확히 일치함을 확인했고, 3)은 WCAG 상대휘도 공식을 독립적으로 다시 계산해 design-qa의 재계산값(~3.25:1)과 일치함을 확인했다.

## 25. 컴포넌트/파운데이션 페이지 전수 대조 + 시맨틱 토큰 의미 검증 — 스팟체크가 아닌 전수 순회 (2026-07-17)

**배경**: 48차 "확정 디자인 8프레임 재대조" 라운드(23절)에서 brand-designer가 "눈에 띄는 차이만" 스팟체크해 Logo `Background=Teal` variant(`263:692`, `263:666`)와 Spacing 페이지 눈금 막대의 `color/success` 오바인딩 2건을 놓쳤다(사용자가 Figma에서 직접 발견). 이번 라운드는 스팟체크가 아니라 **COMPONENTS 구역 10개 페이지 + FOUNDATIONS 구역 3개 페이지, 총 13개 페이지 전체를 색상 바인딩 기준으로 전수 순회**했다. Card(`262:5`)/Checkbox(`474:881`)/Colors(`95:2`)/Icons(`96:7`, `Pixel/NoResult` 포함)는 design-qa 별도 감사 대상이거나 이번 라운드 명시적 제외 대상이라 **전혀 열람하지 않았다**.

### 25-1. 점검 대상 페이지 (13개)

- **COMPONENTS(10)**: Button(`97:8`) · Input(`100:2`) · Select(`101:3`) · Badge(`102:3`) · Table Row(`103:3`) · Sidebar Nav Item(`103:92`) · Alert(`104:2`) · Avatar(`104:127`) · Logo(`263:665`) · Link(`341:2`)
- **FOUNDATIONS(3)**: Typography(`95:3`) · Spacing(`95:4`) · Elevation(`116:5`)

각 페이지를 `use_figma` 읽기 전용 스크립트로 재귀 순회해 SOLID fill/stroke 중 8절 Legacy 세맨틱 토큰(`color/background`/`surface`/`text-primary`/`text-secondary`/`border`/`success`/`error`/`warning`/`background-info`/`border-ink`, 그리고 참고용으로 `text-inverse`)에 바인딩된 노드를 전수 검색했다(총 837개 노드 스캔).

### 25-2. 발견 및 처리 — 의미 불일치(b) 위주, 값 불일치(a) 1건 포함

**1) Logo(`263:692`) Background=Teal(`263:666`) — 알려진 결함 1** — 브랜드 Primary가 이미 0-20절(Stage2)에서 틸→스카이블루로 전환됐으나 Logo의 컬러 배경 variant만 리바인딩되지 않고 남아 있었다. login(`501:4940`)/main(`501:6008`) confirmed 프레임을 재스크린샷해 실제 배경(카드 밖 풀블리드 sky, 사이드바 sky)이 전부 스카이블루임을 재확인 → 기존 토큰 `color/sky/500`(`VariableID:615:122`)으로 리바인딩(신규 토큰 없음), variant명도 "Background=Sky"로 정정. 재대조: `boundVariables.fills[0].id === VariableID:615:122`, hex `#1395e6` 일치.

**2) Spacing 페이지(`95:4`) `color/success` 눈금 막대 — 알려진 결함 2, 6개 전부 발견** — 브리프가 예시로 든 `95:168` 외에 동일 패턴 막대가 총 **6개**(`95:168`/`95:171`/`95:174`/`95:177`/`95:180`/`95:183`, spacing/1~spacing/8 각 눈금)임을 전수 확인. 전부 `color/success`(레거시, → teal/500 alias)에 바인딩돼 있었는데 이 막대들은 "성공" 상태와 무관한 순수 spacing-scale 시각화 장식이다 → 값(#17A398)은 그대로 두고 참조만 브랜드 프리미티브 `color/teal/500`(`VariableID:95:6`)으로 직접 교체(레거시 세맨틱 경유 제거).

**3) 신규 발견 — "{페이지명} / Documentation" 메타 헤더 패턴이 8개 COMPONENTS 페이지 전체 + Avatar 데모 라벨에 반복**: Button/Input/Select/Badge/Table Row/Sidebar Nav Item/Alert/Avatar 8개 페이지 전부에서 동일한 3-노드 패턴(페이지 상단 문서화 헤더 배경=`color/surface`, 제목 텍스트=`color/text-primary`, 설명 텍스트=`color/text-secondary`)이 8절 Legacy 세맨틱에 바인딩된 채로 발견됐다(총 24개 노드) + Avatar 데모 라벨 "happyday님"(`104:140`)도 `color/text-primary` 1건 추가 — 총 **25개 노드**. 값 자체는 전부 정확했지만(surface=#ffffff, text-primary=#1a1a1a=ink/900, text-secondary=#5c6366=gray/600) 8절 레거시 토큰을 현재 유효 페이지가 계속 참조하는 상태라 브리프 판단 기준의 의심 신호에 해당 → 값 불변, 참조만 현재 활성 프리미티브로 직접 교체: `color/surface`→`color/gray/0`(`VariableID:95:10`), `color/text-primary`→`color/ink/900`(`VariableID:95:9`), `color/text-secondary`→`color/gray/600`(`VariableID:95:15`).

**4) 신규 발견 — Typography 페이지(`95:3`)의 구 "Brand Guide 4단계 위계" 스펙시멘 블록(14개 노드), 값 불일치 1건 포함**: 0-14절에서 신규 등록한 11종 텍스트 스타일 스펙시멘(`438:2`~)과 별개로, 그보다 앞서 존재하던 구형 "Display(Latin)/Display(KR)/Body/Caption" 4단계 스펙시멘 블록(`95:201`~`95:212`, Brand Guide 시절 타이포 스케일 — 현재 등록된 11종 텍스트 스타일 어디에도 해당하지 않음)이 같은 페이지에 그대로 남아 텍스트/보더가 8절 Legacy 토큰(`text-primary`/`text-secondary`/`border`)에 바인딩돼 있었다. 텍스트 2종은 (3)과 동일하게 값 불변 교체(`text-primary`→ink/900, `text-secondary`→gray/600). **보더 4개(`95:201`/`95:204`/`95:207`/`95:210`)는 값 불일치(a)도 함께 발견** — `color/border`(alias `color/gray/200` #DCE0E1)에 바인딩돼 있다고 표시되면서도 paint의 실제 렌더 색은 `#000000`(순수 검정, alias 값과 불일치하는 stale paint)이었다. 스크린샷으로 실제 렌더가 진한 검정 테두리였음을 확인 → `color/gray/200`(`VariableID:95:13`)으로 직접 재바인딩해 값도 올바른 연회색(#DCE0E1)으로 정정, 의미도 legacy `color/border` 참조를 제거. 이 구 블록 자체(콘텐츠·구조)는 삭제하지 않고 색상 바인딩만 정정했다 — 삭제는 이번 라운드 스코프 밖.

**5) FOUNDATIONS Spacing(18개 추가)/Elevation(19개) — 동일한 (3)번 패턴 확장 적용**: Spacing 페이지의 "Spacing"/"Radius" 섹션 제목·설명·행 라벨(text-primary 3 + text-secondary 11) + Radius 스와치 배경 4개(surface→gray/0) = 18개, Elevation 페이지의 섹션 제목 4개(text-primary) + 행 라벨 11개(text-secondary) + swatch-bg/데모 배경 4개(surface→gray/0) = 19개 — 전부 (3)과 동일한 값-불변 참조 교체를 적용했다.

**6) 재확인만, 문제 없음(변경 없음)**:
- Colors/Spacing/Elevation 3개 FOUNDATIONS 페이지의 루트 캔버스 배경(`Colors Root`/`Spacing Root`/`Elevation Root`)이 전부 동일하게 `color/background`(레거시, → gray/50 #F7F8F8)에 바인딩돼 있음을 확인했으나, 이는 문서화 캔버스 배경으로 3개 페이지에서 완전히 동일하게 일관 적용된 기존 관례이고 "background"라는 이름 자체가 실제 용도(페이지 배경)와 의미상 어긋나지 않아 **의미 불일치(b)로 판단하지 않았다** — 변경 없음.
- Button 페이지의 `color/text-inverse`(레거시, `VariableID:219:2`) 13건(NeoBtn Style=Sky/Navy/Ink 텍스트 "검색")은 13절 P1/18절에서 이미 검증·확정된 정당한 재사용이라 이번에도 변경하지 않았다.
- Link 페이지(`341:2`, 2개 노드만 존재)는 레거시 바인딩 0건으로 클린 확인.
- Avatar 마스터(`104:131`) 자체, Table Row 페이지의 정식 컴포넌트(Row Action Button/Table Row Action/Contact Row)는 레거시 바인딩 없음 확인.

### 25-3. 자체 재대조 (design-systems 규칙, 생략 불가)

리바인딩 직후 83개 노드(Logo 1 + 컴포넌트 페이지 25 + Typography 14 + Spacing 24 + Elevation 19) 전체를 `use_figma` 읽기 전용으로 재조회해 `boundVariables` ID와 resolved hex가 기대값과 정확히 일치하는지 항목 단위로 확인했다 — **불일치 0건**. `get_screenshot`으로 Spacing 페이지 전체, Typography `Specimen Display/Latin`(보더 정정 확인), Logo ComponentSet 전체(Sky/White 두 variant)를 시각 검증해 레이아웃 잘림·색상 오류 없음을 확인했다.

### 25-4. 제외 대상 확인

Card(`262:5`)·Checkbox(`474:881`)·Colors(`95:2`)·Icons(`96:7`, `Pixel/NoResult` 포함)는 이번 라운드에서 **전혀 열람·수정하지 않았다**(design-qa 별도 감사 대상 또는 이번 브리프 명시적 제외).

### 25-5. 완료 기준 체크

신규 primitive/semantic 토큰은 만들지 않았다(전부 기존 활성 토큰으로 참조만 교체) — 1-1/1-2/1-3절 갱신 불필요. FOUNDATIONS Colors 페이지 스와치 갱신은 Colors 자체가 이번 제외 대상이라 생략. 5절 컴포넌트 표의 Logo 행만 Background=Sky로 갱신 반영했다(위 참고).

### 25-6. 재정정 — Spacing 눈금 막대 6개, teal→중립(ink/900)으로 재조정 (2026-07-17, 2차)

**배경**: 25-2절 2)에서 눈금 막대 6개(`95:168`/`95:171`/`95:174`/`95:177`/`95:180`/`95:183`)를 `color/success`(레거시, 상태 전용 세맨틱)에서 브랜드 프리미티브 `color/teal/500`으로 1차 정정했다. 그런데 사용자가 이 1차 정정도 재지적했다 — 이 막대는 확정 UI 화면에 실제로 적용된 색이 아니라 Spacing 페이지 전용 치수 시각화(눈금자) 장식이므로, 굳이 브랜드색(teal)을 끌어올 필요 없이 문서/가이드에서 공통적으로 쓰이는 중립색(검정·회색 계열)을 쓰는 게 맞다는 것이 세션 초반부터 사용자가 밝혀온 원칙(확정 화면에 실제 적용된 색이 아니라 가이드 문서 전용 장식이면 브랜드 토큰을 새로 끌어올 필요가 없다)과 일치한다.

**선택 근거**: 신규 토큰을 만들지 않고 기존 Primitives 컬렉션(`VariableCollectionId:95:5`)에서 무채색 계열만 재검토했다. 1-1절 기록상 이 프로젝트의 무채색 프리미티브는 `color/ink/900`(#1A1A1A, "구조선·보더·하드 그림자·기본 텍스트에 실제 쓰인" 시스템 기본 검정)과 `color/gray/*` 스케일(0~650, 대부분 뮤트 텍스트·placeholder·hover 배경 등 옅은 용도)로 나뉜다. 사용자가 요청한 "너무 연하지 않은, 검정이나 진회색 계열"에 부합하는 후보 중, 눈금자류 장식은 이 시스템 전반에서 구조선·보더 용도로 이미 관례적으로 쓰이는 가장 진한 무채색(`color/ink/900`)을 그대로 쓰는 것이 가장 자연스럽다고 판단했다 — gray 계열(300/350/375 등)은 모두 placeholder·hover 등 옅은 강조용으로 예약돼 있어 시각적 존재감이 부족하다.

**처리**: 6개 노드 fill의 `boundVariables.color`를 `color/teal/500`(`VariableID:95:6`)→`color/ink/900`(`VariableID:95:9`, #1A1A1A)로 재바인딩. 신규 primitive/semantic 토큰 생성 없음(기존 토큰 재사용만).

**자체 재대조(design-systems 규칙, 생략 불가)**: 재바인딩 직후 6개 노드 전부 `use_figma` 읽기 전용으로 재조회해 `boundVariables.color.id === "VariableID:95:9"`이고 resolved hex가 `#1a1a1a`로 정확히 일치함을 확인했다(불일치 0건). `get_screenshot`으로 Spacing 페이지(`95:162`) 전체를 재확인해 레이아웃 잘림·겹침 없이 정상 렌더링됨을 확인했다.

원본 확정 디자인 프레임(`501:2505` 하위)은 이번 작업과 무관해 열람하지 않았다 — Spacing 페이지의 장식용 눈금 막대에 한정된 순수 문서 정정이다.

## 27. Icons 페이지(`96:7`) 색상 바인딩 전수 감사 실행 — A/B그룹 재바인딩 (2026-07-17, graphic-designer 1단계 → design-systems 2단계)

**배경**: Icons 페이지(`96:7`)는 24/25절 등 여러 전수 대조 라운드에서 명시적으로 제외 대상이었던 사각지대였다. graphic-designer가 `docs/design/graphic-assets.md` "Icons 페이지 색상 바인딩 전수 감사" 절(2026-07-17)에서 Icon/* 8종 + Pixel/* 12종 전부(자식 벡터 포함)를 실측해 A/B로 1단계 분류했고, 이번 라운드는 design-systems가 그 판단을 재해석 없이 그대로 실행하는 2단계다. 신규 토큰은 만들지 않았다 — 전부 기존 등록된 토큰(`color/teal/500`/`color/ink/900`/`color/coral/500`/`color/text-inverse`)만 재사용했다.

### 27-1. A그룹 — 실측값 그대로 바인딩 (미바인딩 raw hex → 토큰)

- **Icon/* teal fill 7종·10노드 → `color/teal/500`**(`VariableID:95:6`): Icon/Search 96:9, Icon/Add 96:14, Icon/Edit 96:20, Icon/Delete 96:24·96:26, Icon/Category 96:29·96:30, Icon/Logout 96:33, Icon/User 96:43·96:44.
- **Pixel/* → `color/ink/900`**(`VariableID:95:9`): Pixel/Star(`255:11`) vector 8개(`255:3`~`255:10`), Pixel/Plus(`255:30`) vector 2개(`255:28`/`255:29`), Pixel/Close(`255:107`) stroke 1개(`255:106`), Pixel/Eye(`281:405`) fill 14개, Pixel/EyeOff(`415:892`) vector 3개(`414:3`~`414:5`), Pixel/Check 마스터(`815:2`) stroke 1개(`814:3`).
- **Pixel/Search(`255:26`) → `color/teal/500`**: vector 13개(`255:13`~`255:25`).
- **Pixel/Warning(`255:120`) 원형 9개 → `color/coral/500`**(`VariableID:95:7`): `255:109`~`255:117`. **Pixel/NoResult(`255:149`) 크랙 6개 → `color/coral/500`**: `255:143`~`255:148`(몸통 21개는 아래 27-3 예외 참고, 무수정).

### 27-2. 텍스트 인버스 특별지정 → `color/text-inverse`(`VariableID:219:2`)

값은 흰색(#FFFFFF)이나 `color/gray/0`이 아니라 "브랜드색/어두운 배경 위 인버스 아이콘" 의미로 `color/text-inverse`를 선택(Checkbox 체크마크 21절 전례와 일관): Pixel/Logout(`255:43`) vector 11개(`255:32`~`255:42`), Pixel/Warning(`255:120`) 느낌표 2개(`255:118`/`255:119`).

### 27-3. 이미 완료된 예외 — 재작업 없음, 확인만

- **Icon/Alert Ellipse(`96:38`) fill** — 이미 `color/bg-cta-amber`(`VariableID:615:133`)에 바인딩된 상태를 재조회로 재확인, 무수정.
- **Pixel/NoResult 몸통 vector 21개(`255:122`~`255:142`)** — 23절에서 이미 `color/sky/500`(`VariableID:615:122`)으로 리바인딩 완료된 상태를 재조회로 재확인, 무수정.

### 27-4. B그룹 — ink/900 재해석 바인딩(`color/ink/800`은 이번 범위에 쓰지 않음)

graphic-designer의 실측 근거(Row Action Button Danger 보더 vs 아이콘 불일치, Toast title과의 통일성, ink/900 교정 이전 값의 잔재)를 그대로 받아 재해석 없이 실행. 재바인딩 전 실측 raw 색은 전부 `#1C1F21`(ink/800과 동일한 값이었으나 alias하지 않고 목표 토큰 `color/ink/900` #1A1A1A로 직접 재바인딩 — 렌더 색이 미세하게 바뀜, 의도된 결과):

- **Icon/* 8종 잉크 stroke/fill 20노드**: Icon/Search 96:9(stroke)·96:11(fill), Icon/Add 96:14(stroke)·96:15·96:16(fill), Icon/Edit 96:20(stroke)·96:21(fill), Icon/Delete 96:24·96:26(stroke)·96:25(fill), Icon/Category 96:29·96:30(stroke), Icon/Logout 96:33(stroke)·96:34·96:35(fill), Icon/Alert 96:38(stroke만, fill은 27-3 예외 무변경)·96:39·96:40(fill), Icon/User 96:43·96:44(stroke).
- **Pixel/Edit(`255:62`) vector 17개**(`255:45`~`255:61`), **Pixel/Delete(`255:104`) vector 39개**(`255:65`~`255:103`).

### 27-5. 자체 재대조 (design-systems 규칙, 생략 불가)

재바인딩 직후 A그룹(10+8+2+1+14+3+1+13+9+6=67개) + 텍스트 인버스(11+2=13개) + B그룹(20+17+39=76개), 총 156개 노드의 `boundVariables` ID를 `use_figma` 읽기 전용으로 재조회해 목표 토큰과 전부 정확히 일치함을 확인했다(mismatchCount: 0). 예외 2건(Icon/Alert Ellipse `96:38` fill, Pixel/NoResult 몸통 21개)도 각각 `color/bg-cta-amber`/`color/sky/500` 그대로 유지됨을 재확인했다. Checkbox `State=Checked` 인스턴스(`815:3`) 안의 체크마크 오버라이드(`I815:3;814:3`)가 Pixel/Check 마스터(`815:2`) 재바인딩 이후에도 여전히 `color/text-inverse`로 유지되는지 별도 확인 — 유지됨 확인(마스터-인스턴스 상호작용 리스크 없음). `get_screenshot`으로 Icons 페이지 전체와 Pixel/Warning·Pixel/NoResult·Pixel/Edit·Pixel/Delete·Checkbox 개별 확대본을 재확인해 벡터 형태 변형 없이 색상만 정상 반영됐음을 확인했다.

원본 확정 8개 프레임(`501:2505` 하위)은 이번 라운드에서 열람하지 않았다 — 이번 작업은 Icons 페이지 자체 색상 바인딩 정합성 문제이지 확정 프레임 재실측 라운드가 아니다.

## 28. Sidebar Nav Item State=Active 텍스트 색상 결함 정정 + Inactive/Focus 전수 재대조 (2026-07-17, 사용자 직접 발견 후 실행)

**배경**: 사용자가 확정 프레임(`501:6050`, main 프레임 `501:6008` 하위, 사이드바 "전체" Active 항목)과 등록된 컴포넌트(Sidebar Nav Item ComponentSet `258:29`)를 직접 대조해 결함을 발견했다 — 확정 프레임의 "전체" 텍스트(`501:6052`)는 흰색(`#ffffff`)인데, 등록 컴포넌트 State=Active(`258:17`) 내부 텍스트(`258:18`)는 `color/ink/900`(#1A1A1A, 검정)에 바인딩돼 있었다. 카운트 숫자("6", `258:21` Count Pill 내부)는 이번에도 양쪽 다 ink/900이라 무관·무수정.

이 결함은 과거 Checkbox 체크마크 정정(21절)과 같은 유형이다 — 배경(`color/bg-accent-navy`)은 0-20절에서 이미 실측 반영됐지만 텍스트는 옛 값 그대로 남아 있었다. **인스턴스 오버라이드가 아니라 컴포넌트 마스터(State=Active, `258:17` 내부)를 직접 정정**해 다른 화면의 모든 인스턴스에 정상 전파되도록 했다.

### 28-1. 1차 처리 — `color/text-inverse` 재사용 확인

`color/text-inverse`(`VariableID:219:2`, Checkbox 체크마크 정정 때 이미 등록된 흰색 텍스트 전용 토큰)를 재조회해 `valuesByMode`가 `color/gray/0`(`VariableID:95:10`, `{r:1,g:1,b:1}` = #FFFFFF)를 alias함을 재확인 — resolvedHex 정확히 #FFFFFF. 신규 토큰 생성 없이 그대로 재사용했다.

**정정**: `258:18`("전체", State=Active 내부)의 fill을 `color/ink/900`(`VariableID:95:9`)→`color/text-inverse`(`VariableID:219:2`)로 재바인딩.

### 28-2. State=Inactive/Focus 전수 재대조 — 추가 결함 2건 발견·정정

지시대로 Inactive/Focus의 배경/텍스트/카운트 숫자를 요소 단위로 빠짐없이 재대조했다. ComponentSet(`258:29`) 자식은 `State=Active(258:17)`/`State=Inactive(258:23)`/`State=Focus(287:17)` 3개(0-15절에서 이미 Focus=No/Yes 축이 State 열거형으로 소급 통합된 구조 그대로). 대조를 위해 확정 프레임 `501:6050`의 부모 컨테이너(`501:6049`)를 열람해 사이드바 nav 항목 5개(전체=Active `501:6050`, 가족/친구/기타/회사=Inactive `501:6055`/`501:6060`/`501:6065`/`501:6070`)를 전부 실측했다(읽기 전용, 원본 무수정).

**확정 프레임 실측값(Inactive, 예: `501:6055` "가족")**: 배경 `rgba(255,255,255,0.18)`(반투명 흰 오버레이, 사이드바 파란 배경 위에 얹힘) + 2px `#1a1a1a` 보더 + 텍스트 흰색(`text-white`) + Count Pill 앰버 배경(`#ffcb47`)+ink 텍스트.

**등록 컴포넌트(정정 전) 실측값**: State=Inactive(`258:23`) 배경 `fills=[]`(완전 투명, 보더 없음), 텍스트(`258:24`) `color/ink/900`(검정) — 배경 불투명도·텍스트 색 2건 모두 확정 프레임과 불일치.

**정정 범위(색상 한정)**:
1. **텍스트**: `258:24`("전체", State=Inactive 내부)를 `color/ink/900`→`color/text-inverse`로 재바인딩(28-1과 동일 토큰 재사용, 신규 토큰 없음).
2. **배경**: `258:23`의 `fills`를 `[]`(완전 투명)에서 `color/gray/0`(`VariableID:95:10`, #FFFFFF)에 바인딩된 SOLID paint + paint opacity `0.18`로 정정 — 확정 프레임의 `rgba(255,255,255,0.18)`을 hex 단위가 아닌 "흰색+투명도" 조합으로 그대로 재현(신규 토큰 없음, 기존 `color/gray/0` 재사용 + 로컬 paint opacity, Checkbox 라벨의 "ink/900 + opacity 0.5" 기존 패턴과 동일 원칙).

**Count Pill 재확인(변경 없음)**: Active Count Pill(`258:21`, 흰 배경+ink 보더+ink 텍스트 "6")과 Inactive Count Pill(`258:27`, 앰버 배경 `color/amber/500` `VariableID:95:8`+ink 보더+ink 텍스트)을 확정 프레임(`501:6053` 흰+ink "6", `501:6058` 앰버+ink "2")과 각각 대조한 결과 hex·바인딩 전부 일치 — 정정 불필요.

**State=Focus는 무수정**: Focus(`287:17`)는 확정 프레임에 없는 합성 인터랙션 상태(9절)라 대조 대상에서 제외, 텍스트(`287:18`, ink/900)·배경(`fills=[]`)·FocusRing 자식(`574:1056`, 3px ink OUTSIDE, 9-5절 공식) 전부 무수정 확인만 했다.

**⚠ 범위 밖 발견(수정하지 않음, TODO로만 기록)**: 확정 프레임(Active `501:6050`/Inactive `501:6055` 등)은 전부 2px `#1a1a1a` 보더를 갖고 있으나, 등록된 State=Active(`258:17`)/State=Inactive(`258:23`) 마스터에는 보더가 전혀 없다(`strokes: []`). 이번 라운드는 사용자 브리프가 명시한 "텍스트/배경/카운트 숫자 색상" 3항목으로 범위를 한정했고, 보더 추가는 구조 변경(Focus의 기존 "Inactive가 완전 투명이라 DROP_SHADOW 대신 3px OUTSIDE 스트로크로 대체" 설계 근거, 9-5절과 연쇄적으로 얽혀 있어 독립적 색상 수정보다 판단이 더 필요)이라 이번 범위에서 제외하고 7-2절에 TODO로 이관했다(아래 참고).

### 28-3. Component Specs 스펙 시트(`343:1106`) 전파 확인 + 부수 발견 1건 정정

`Spec — Sidebar Nav Item`(`343:1106`)의 3개 셀(Active `452:899`/Inactive `452:905`/Focus `452:911`)은 전부 마스터의 INSTANCE라 배경/텍스트 재바인딩이 자동 전파됨을 스크린샷으로 확인했다. 다만 스펙 시트 자체가 밝은 회색 페이지 배경(`#F1F1F1` 계열) 위에 인스턴스를 올려두는 구조라, 흰 텍스트+반투명 흰 배경 조합(Active/Inactive)이 밝은 캔버스 위에서 그대로는 거의 안 보이는 문제를 발견했다 — Checkbox처럼 값 자체는 정확해도 스펙 시트가 실제 사용 맥락(파란 사이드바 배경)을 재현하지 못하면 "상태를 한눈에 훑어볼 수 있어야 한다"는 2-5번 규칙을 충족하지 못한다.

**조치**: 3개 Cell(`452:903`/`452:909`/`452:915`) 각각에 `color/bg-brand-blue`(`VariableID:615:128`, sky/500 #1395E6 alias — 실제 사이드바 배경 토큰, 0-20절에서 이미 정식 등록)에 바인딩된 배경 사각형(`SidebarContext-BG`, `layoutPositioning=ABSOLUTE`, 인스턴스보다 사방 6px 크게, cornerRadius14)을 인스턴스 뒤(자식 배열 index 0)에 추가해 실제 사이드바 위 맥락을 재현했다. 신규 토큰 없음, 기존 토큰 재사용만.

**부수 발견·정정**: Inactive 스펙 시트 인스턴스(`452:905`)에 마스터와 무관한 **stale 인스턴스 레벨 fill 오버라이드**(opacity가 마스터의 0.18이 아니라 1로 고정된 로컬 오버라이드)가 남아 있어 마스터 재바인딩이 육안상 반영되지 않는 것처럼 보였다 — 인스턴스 fill을 마스터와 동일한 값(`color/gray/0` + opacity 0.18)으로 직접 재설정해 해소했다(마스터 자체는 무관, 인스턴스 쪽 잔재 오버라이드만 제거).

**최종 확인**: `get_screenshot`(inline)으로 3칸 모두 파란 배경 위에서 Active(진한 navy+흰 텍스트)/Inactive(반투명 흰 오버레이로 밝아진 파랑+흰 텍스트)/Focus(파랑 배경+검은 ring+검은 텍스트, 무수정) 상태가 육안으로 명확히 구분됨을 확인했다.

### 28-4. 파일 전체 인스턴스 전수 검색 — 부작용 없음 확인

파일 전체 29개 페이지(`page.loadAsync()`로 순차 로드, `setCurrentPageAsync` 페이지 전환 1회 제한 우회, 14-3절과 동일 기법)에서 `258:17`/`258:23`/`287:17`을 `mainComponent`로 참조하는 INSTANCE를 전수 검색한 결과 **정확히 3개, 전부 `Component Specs` 페이지의 스펙 시트 셀(`452:899`/`452:905`/`452:911`)뿐** — 다른 화면·확정 프레임에는 참조 0건. 레이아웃 겹침·깨짐 등 Checkbox 정정 때와 같은 부작용은 발견되지 않았다.

### 28-5. 자체 재대조 (design-systems 규칙, 생략 불가)

정정 직후 `use_figma` 읽기 전용으로 아래 항목을 재조회해 기대값과 정확히 일치함을 확인했다(불일치 0건):
- `258:18`/`258:24` fills[0].boundVariables.color.id = `VariableID:219:2`(`color/text-inverse`), resolvedColor `{r:1,g:1,b:1}`.
- `258:23` fills[0].boundVariables.color.id = `VariableID:95:10`(`color/gray/0`), opacity `0.18000000715255737`.
- `452:899`/`452:905`/`452:911`(스펙 시트 인스턴스) fills가 각각 마스터와 동일 바인딩·opacity로 일치, `886:872`/`886:873`/`886:874`(SidebarContext-BG) fills[0].boundVariables.color.id = `VariableID:615:128`(`color/bg-brand-blue`).
- Count Pill(`258:21`/`258:27`) fills는 이번 라운드에서 손대지 않았음을 재확인(변경 없음 검증).
- Focus(`287:17`/`287:18`/`574:1056`)는 이번 라운드 전체에서 무수정 확인.

ComponentSet(`258:29`)의 `description` 메타데이터에도 이번 정정 사실과 보더 TODO를 반영했다.

### 28-6. 문서/TODO 갱신

7-2절에 신규 TODO 추가: **"Sidebar Nav Item State=Active/Inactive 마스터에 확정 프레임(`501:6050`/`501:6055` 등)의 2px `#1a1a1a` 보더가 없음"** — 이번 라운드는 색상 범위로 한정해 보더 추가는 보류, 후속 라운드에서 Focus(`287:17`)의 기존 "Inactive 완전 투명 전제 하 3px OUTSIDE 스트로크" 설계(9-5절)와 함께 재검토 필요(Inactive가 이제 완전 투명이 아니라 반투명 흰 오버레이가 됐으므로 DROP_SHADOW 렌더링 제약이 여전히 유효한지도 재확인 대상).

원본 확정 프레임(`501:6008`/`501:2505` 하위)은 이번 라운드에서 읽기 전용으로만 열람했고 전혀 수정하지 않았다.

### 28-7. design-qa 재검증 후속 정정 — State=Focus(`287:17`/`287:18`) 순수성 위반 + 스펙 시트 캡션 stale (2026-07-17)

design-qa가 28절 정정을 독립 재검증하며 그 직접 파생 결함 2건을 발견해 이어서 정정했다. 원본 확정 프레임은 이번에도 열람하지 않았다.

**결함 1 — Focus 순수성 위반(HIGH)**: 9-1절 원칙(**⚠ 2026-07-17 정정, 28-9절**: 원래 "9-3절 원칙"으로 잘못 인용돼 있었다 — 9-3절은 "Focus 상태만 추가한 보조 컴포넌트" 표일 뿐 순수성 원칙 정의는 9-1절 851번 줄 근처에 있다. 12-1절이 이미 9-1절로 정확히 인용한 전례를 따라 정정)(Focus=Yes는 같은 상태의 Focus=No, 즉 Inactive와 배경·텍스트가 완전히 동일해야 하고 차이는 Focus 링뿐이어야 한다)에 따르면, 28-2절에서 Inactive(`258:23`/`258:24`) 텍스트를 `color/text-inverse`로, 배경을 `color/gray/0`+opacity 0.18로 정정했으면 Focus(`287:17`/`287:18`)도 동일하게 갱신됐어야 한다. 그러나 28-2절이 "Focus는 확정 프레임에 없는 합성 상태"라는 이유로 대조 대상에서 제외하면서, Focus가 구값(텍스트 `color/ink/900`, 배경 `fills=[]` 완전 투명) 그대로 남아 Inactive와 어긋나 있었다.

**정정**:
1. `287:18`(Focus 텍스트) `color/ink/900`(`VariableID:95:9`) → `color/text-inverse`(`VariableID:219:2`)로 재바인딩 — Inactive `258:24`와 완전히 동일한 값.
2. `287:17`(Focus 배경) `fills=[]`(완전 투명) → `color/gray/0`(`VariableID:95:10`) SOLID + paint opacity `0.18000000715255737`로 재바인딩 — Inactive `258:23`과 완전히 동일한 값(재조회로 두 노드의 `fills` JSON이 정확히 일치함을 확인).
3. **FocusRing(`574:1056`, 3px ink OUTSIDE 스트로크, 9-5절 공식)은 이번에도 무수정** — 별도로 이미 알려진 하드코딩 이슈(스트로크 `boundVariables`가 비어 있음)이며 이번 정정 범위 밖.
4. **부수 발견**: 정정 직후 스펙 시트를 재확인하는 과정에서, Component Specs 페이지의 Focus 셀 인스턴스(`452:911`)에도 28-3절에서 Inactive 셀(`452:905`)에 있었던 것과 같은 종류의 **stale 인스턴스 레벨 fill 오버라이드**(opacity가 마스터의 신규값 0.18이 아니라 1로 고정)가 남아 있어 마스터 재바인딩이 스크린샷에 반영되지 않는 것처럼 보였다. 인스턴스 fill을 마스터와 동일한 값(`color/gray/0` + opacity 0.18)으로 직접 재설정해 해소했다(텍스트 자식 `I452:911;287:18`은 오버라이드 없이 마스터 값을 정상 상속하고 있어 별도 조치 불필요).

**자체 재대조**: `287:17`/`287:18` 재조회 결과 `boundVariables.color.id`가 각각 `VariableID:95:10`(opacity `0.18000000715255737`)/`VariableID:219:2`로 기대값과 정확히 일치(불일치 0건), `JSON.stringify(focusBg.fills) === JSON.stringify(inactiveBg.fills)` 및 텍스트 쪽도 동일 비교로 `true` 확인. `get_screenshot`으로 스펙 시트(`343:1106`) 전체를 재확인해 Active/Inactive/Focus 3칸 모두 파란 배경 위 흰 텍스트로 일관되게 렌더링되고(Focus만 검은 링 추가), 이전에는 흰 배경처럼 보이던 Focus 칸이 정상적으로 파란 배경 위에서 렌더링됨을 확인했다.

**결함 2 — 스펙 시트 캡션(`343:1108`) stale**: 캡션 마지막 문장이 "State=Inactive/Focus는 무수정"이라고 남아 있었으나 실제로는 28절에서 Inactive가, 이번 28-7절에서 Focus가 각각 수정됐다. 캡션 텍스트를 실제 변경 사실(28절의 Active/Inactive 텍스트·배경 정정 + 28-7절의 Focus 정정, FocusRing은 무수정)에 맞게 갱신했다.

원본 확정 프레임(`501:6050`/`501:2505` 하위)은 이번 라운드에서도 전혀 열람·수정하지 않았다 — 이번 작업은 28절 정정의 파생 결함(Focus 순수성 위반)을 다루는 것이지 확정 프레임 재실측이 아니다. 보더 갭(7-2절 TODO)과 FocusRing(`574:1056`) 하드코딩 문제는 이번에도 손대지 않았다.

### 28-8. design-qa 2차 재검증 후속 정정 — Focus(`287:17`) 잔여 흰 보더 제거 (2026-07-17)

design-qa가 28-7절 정정을 다시 재검증하며 신규 HIGH 결함 1건을 발견했다. 원본 확정 프레임은 이번에도 열람하지 않았다.

**결함**: `287:17`(State=Focus 배경 노드)에 미문서화된 흰색 1px 보더(`strokes`, `{type:SOLID, color:{r:1,g:1,b:1}, opacity:1, boundVariables:{}}` — raw 값, `var()` 참조 없음)가 남아 있었다. `258:23`(Inactive)과 `258:17`(Active)은 재조회 결과 둘 다 `strokes: []`(완전히 없음)로, 9-1절(**⚠ 2026-07-17 정정, 28-9절**: 여기도 원래 "9-3절"로 잘못 인용돼 있었다 — 28-7절과 동일한 오기, 함께 정정) "Focus는 Inactive와 배경·보더·텍스트가 전부 동일해야 하고 차이는 FocusRing(`574:1056`)뿐이어야 한다" 원칙을 이 잔여 흰 보더가 위반하고 있었다. design-qa는 9-5절 "1차 시도(기각) — opacity 0.02 흰색 SOLID fill 추가" 실험의 잔재일 가능성을 추정했으나(확정 아님), 28-7절 시점에는 이 stroke 자체가 재대조 항목에 없어 놓쳤던 것으로 보인다.

**정정**:
1. `287:17.strokes`를 `[]`(완전히 없음)로 정정 — `258:23`과 정확히 동일한 값. FocusRing(`574:1056`)은 이번에도 무수정(별개 자식 노드, 기존에 알려진 하드코딩 이슈로 범위 밖).
2. 스펙 시트 Focus 셀 인스턴스(`452:911`)도 확인 — `overrides` 조회 결과 이 인스턴스의 override는 `["fills"]`(28-7절에서 이미 정정한 stale opacity 오버라이드)뿐이고 `strokes`는 오버라이드가 없어 마스터를 그대로 상속하는 상태였다. 즉 인스턴스 자체의 stale override가 아니라 마스터 값이 문제였으므로, 마스터(`287:17`) 정정만으로 인스턴스에도 자동 전파됨을 확인했다(별도 인스턴스 레벨 조치 불필요).

**자체 재대조**: 정정 직후 `use_figma` 읽기 전용으로 `287:17`/`258:23`/`258:17`/`452:911`/`452:905`의 `strokes`를 재조회해 `JSON.stringify(focusMaster.strokes) === JSON.stringify(inactiveMaster.strokes)`(둘 다 `"[]"`) 및 `activeMaster.strokes`도 동일(`"[]"`)함을 확인했다. 스펙 시트 인스턴스 `452:911`/`452:905`의 `strokes`도 각각 `"[]"`로 마스터와 일치함을 확인했다(불일치 0건). `get_screenshot`(inline)으로 스펙 시트(`343:1106`) 전체를 재확인해 Active/Inactive/Focus 3칸 모두 파란 배경 위 흰 텍스트로 일관되게 렌더링되고 흰 테두리 잔상 없이 정상 표시됨을 확인했다.

원본 확정 프레임(`501:6050`/`501:2505` 하위)은 이번 라운드에서도 전혀 열람·수정하지 않았다. 보더 갭(7-2절 TODO)과 FocusRing(`574:1056`) 하드코딩 문제는 이번에도 손대지 않았다.

### 28-9. Active/Inactive/Focus 공통 2px 잉크 보더 추가 + FocusRing-Ink(`574:1056`) 변수 바인딩 정정 (2026-07-17, 메인 세션 승인)

28절→28-7절→28-8절로 이어진 Sidebar Nav Item 정정 라운드의 후속으로, 7-2절에 TODO로 이관돼 있던 두 결함(마스터 보더 누락, FocusRing raw hex 하드코딩)을 이번에 처리했다. 원본 확정 프레임(`501:6050`/`501:6055`/`501:2505` 하위)은 이번에도 읽기 전용으로만 재실측했고 전혀 수정하지 않았다.

**1) 확정 프레임 보더 재실측**: `501:6050`("전체", Active)/`501:6055`("가족", Inactive) 둘 다 `use_figma` 읽기 전용으로 재조회한 결과 스트로크가 완전히 동일했다 — color `{r:0.1,g:0.1,b:0.1}`(≈`#1a1a1a`, Figma 저장 정밀도 차이일 뿐 `color/ink/900`의 라이브 값 `{r:0.10196078568696976,...}`와 육안·수치상 동일 색), `strokeWeight` **2**, `strokeAlign` **INSIDE**, 4변(top/bottom/left/right) 전부 균일 weight 2. `color/ink/900`(`VariableID:95:9`)을 재조회해 라이브 값이 정확히 `#1a1a1a`임을 재확인 — 신규 토큰 불필요, 그대로 바인딩.

**2) 3개 variant 전부 적용**: `258:17`(Active)/`258:23`(Inactive)/`287:17`(Focus) 3개 마스터 전부에 위 스펙 그대로(`color/ink/900` 바인딩, weight 2, `strokeAlign=INSIDE`) 보더를 추가했다. Focus까지 포함한 이유는 9-1절(851번 줄 근처) Focus 순수성 원칙 — Focus는 Inactive와 배경·보더·텍스트가 완전히 동일해야 하고 차이는 FocusRing뿐이어야 한다 — 을 따른 것으로, 28-2/28-7절에서 이미 텍스트·배경을 Inactive와 통일시킨 것과 같은 원칙을 보더에도 그대로 연장했다.

**3) FocusRing-Ink(`574:1056`) 바인딩 정정**: 9-5절 공식대로 존재하던 3px `strokeAlign=OUTSIDE` 스트로크가 raw hex(`{r:0.1,g:0.1,b:0.1}`, `boundVariables` 없음)였던 것을 `color/ink/900`(`VariableID:95:9`)에 정식 바인딩했다 — NeoBtn Focus의 FocusRing(`549:43`, 이미 `color/ink/900`에 정상 바인딩)과 동일한 패턴을 그대로 따랐다. `574:1056`의 geometry(size 175×42, position x/y `-1`, `cornerRadius` 10 — 버튼 자체 cornerRadius와 동일, NeoBtn의 "버튼 radius+4.5" 공식과는 다른 이 컴포넌트 전용 9-5절 특수 구현)는 이번에도 전혀 손대지 않았다 — 색상 참조 방식만 raw→토큰으로 교체.

**4) FocusRing 충돌 검증**: 새 보더(내측 2px, `strokeAlign=INSIDE`, 버튼 경계 0~173×0~40의 안쪽에 그려짐)와 기존 FocusRing(외측 3px, `strokeAlign=OUTSIDE`, 버튼 경계보다 1px 바깥인 `-1,-1`~`174,41` 기준으로 그려짐)은 좌표상 서로 겹치지 않는다 — 버튼 진짜 경계(0)를 기준으로 안쪽 2px(새 보더)와 바깥쪽 1px 간격 뒤 3px(FocusRing)로 완전히 분리돼 있다. `get_screenshot`(ComponentSet `258:29` 전체, 스펙 시트 `343:1106` 전체, `287:17` 개별 확대)로 3종 모두 확인한 결과: Active(navy 배경+흰 텍스트+단일 2px 검정 테두리), Inactive(반투명 흰 오버레이+흰 텍스트+단일 2px 검정 테두리), Focus(동일 배경/텍스트+내측 2px 보더와 외측 3px FocusRing이 1px 간격을 두고 겹치지 않는 깔끔한 이중 링)로 정상 렌더링됐다 — 뭉개짐·겹침 없음, 별도 조정 불필요.

**5) 문서·메타데이터 갱신**: ComponentSet(`258:29`) `description`과 스펙 시트 캡션(`343:1108`)에 이번 정정 사실을 반영, 캡션의 "9-3절 Focus 순수성 원칙" 오기도 "9-1절"로 정정(28-7절 본문의 동일 오기도 이번에 함께 정정 — 12-1절이 이미 9-1절로 정확히 인용한 전례를 따름). 5절 컴포넌트 표 Sidebar Nav Item 행과 7-2절 TODO 2건을 최신 상태로 갱신했다(아래 참고).

**자체 재대조(design-systems 규칙, 생략 불가)**: 정정 직후 `use_figma` 읽기 전용으로 `258:17`/`258:23`/`287:17`/`574:1056`을 재조회해 확인했다(불일치 0건) — `JSON.stringify(activeMaster.strokes) === JSON.stringify(inactiveMaster.strokes) === JSON.stringify(focusMaster.strokes)`(전부 `true`, `strokeWeight:2`/`strokeAlign:"INSIDE"`/`boundVariables.color.id:"VariableID:95:9"` 동일), `574:1056.strokes[0].boundVariables.color.id === "VariableID:95:9"`(`strokeWeight:3`/`strokeAlign:"OUTSIDE"` 무변경). 스펙 시트 인스턴스(`452:899`/`452:905`/`452:911`)도 재조회해 `overrides`에 `strokes` 오버라이드가 없어(기존 `fills` 오버라이드만, 28-3/28-7절에서 이미 처리됨) 마스터의 새 보더를 그대로 상속함을 확인 — 인스턴스 레벨 추가 조치 불필요.

원본 확정 프레임(`501:6050`/`501:6055`/`501:2505` 하위)은 이번 라운드에서도 읽기 전용으로만 열람했고 전혀 수정하지 않았다.

## 29. Icon/* 8종 Basic/Visual 트랙 반영 + Avatar 처리 (2026-07-17, graphic-designer 판정 → design-systems 실행)

**배경**: `docs/design/graphic-assets.md` 최하단 절("Icon/* 8종 Basic/Visual 트랙 재판정 + Basic 6종 재드로잉 지시")에서 graphic-designer가 이미 내린 크래프트 판정을 그대로 실행하는 라운드다. 27절(직전 라운드)에서 이미 fill(teal/amber, A그룹)·stroke(ink/900, B그룹)의 **색상 정확성**을 재바인딩 완료했고, 이번 라운드는 그와 다른 층위의 질문 — "이 아이콘이 애초에 그 면색(fill)을 갖고 있어야 하는가" — 을 다룬다. 사용자가 `Icon/User`(`96:45`)를 직접 보고 "라인형이 맞는 아이콘 아니냐"고 지적한 게 계기였다.

### 29-1. 8종 트랙 판정 요약

| 아이콘 | 트랙 | 근거(한 줄) |
|---|---|---|
| Icon/Search(`96:12`) | **Basic** | 범용 돋보기 기호, 실사용 `Pixel/Search`도 단색 실루엣 하나뿐 |
| Icon/Add(`96:17`) | **Basic** | 컨테이너(NeoBtn)가 이미 브랜드 개성을 담당, 아이콘 자체는 중복 채색 불필요 |
| Icon/Edit(`96:22`) | **Basic** | row 단위 반복 액션, 브랜드 표현 불필요 |
| Icon/Delete(`96:27`) | **Basic** | 위험 신호는 컨테이너(Danger 보더/경고 박스)가 전담, 아이콘 자체는 중립 |
| Icon/Logout(`96:36`) | **Basic** | agent doc 원문 예시, 실사용 `Pixel/Logout`도 얇은 단색 처리 |
| Icon/User(`96:45`) | **Basic**(이번 지적의 발단) | fill(틸)이 Avatar 원 배경과 같은 색이라 원래도 "보이지 않는 면색"이었음, stroke만이 실제 정보 전달 |
| Icon/Category(`96:31`) | **Visual**(유지, 단 fill 색은 30절에서 sky/500으로 재정정됨) | agent doc 원문 예시, 색=분류 의미를 전달해야 하는 CatBadge 언어와 통일 |
| Icon/Alert(`96:41`) | **Visual**(유지) | 상태 강조가 핵심 기능, 굵은 아웃라인+앰버 유지가 기능적으로 필요 |

### 29-2. Basic 6종 — fill 제거 + stroke weight 3→2px, 실제 변경 내역

**사전 재확인(착수 전 `use_figma` 읽기 전용)**: 브리프 표의 8개 주 실루엣 노드 전부 라이브 상태가 브리프와 정확히 일치함을 확인 — fill `#17a398`(`color/teal/500`, `VariableID:95:6`) bound:true, stroke `#1a1a1a`(`color/ink/900`, `VariableID:95:9`) bound:true, strokeWeight 3. 디테일 도형(손잡이·+막대·연필촉·화살표 등) 전부 fill만 `color/ink/900` bound, stroke 없음 — 브리프 서술과 일치.

**변경**: 아래 8개 노드의 `fills`를 빈 배열로, `strokeWeight`를 3→2로 설정(stroke의 `color/ink/900` 바인딩 자체는 손대지 않음 — 27절에서 이미 정확히 바인딩돼 있었으므로 재바인딩 불필요):

| 아이콘 | 주 실루엣(변경) | 디테일(무변경 확인) |
|---|---|---|
| Icon/Search | Ellipse `96:9` | Rectangle `96:11` |
| Icon/Add | Rectangle `96:14`(배지) | Rectangle `96:15`/`96:16`(+ 막대) |
| Icon/Edit | Pencil Silhouette `96:20` | Rectangle `96:21`(연필촉) |
| Icon/Delete | Rectangle 뚜껑 `96:24`, Rectangle 몸통 `96:26` | Rectangle 손잡이 `96:25` |
| Icon/Logout | Rectangle 문 `96:33` | Rectangle 화살표축 `96:34`, Arrow Head `96:35` |
| Icon/User | Ellipse 머리 `96:43`, Ellipse 어깨 `96:44` | 없음(2도형 전부 주 실루엣) |

**Icon/User 전용 — Avatar 인스턴스 오버라이드도 함께 반영**: 실측 결과 Avatar 인스턴스(`501:6370`)의 icon 자식(Icon/User INSTANCE `104:132`) 안 Ellipse 2개(`I501:6370;104:132;96:43`/`;96:44`)는 로컬 오버라이드 상태(fill bound:false, 값은 마스터와 우연히 동일한 raw teal)였다. `resetOverrides()`는 같은 최상위 인스턴스(`501:6370`)의 원 배경 색 오버라이드(스카이블루, 이번 라운드에서 절대 건드리면 안 됨)까지 함께 초기화할 위험이 있어 사용하지 않았다 — 대신 이 두 노드에 fill 제거 + strokeWeight 2px를 마스터와 동일하게 직접 재적용했다(브리프가 명시한 폴백 절차 그대로).

### 29-3. Visual 2종(Category/Alert) — 무변경 확인

재조회 결과 27절 완료 상태와 완전히 동일함을 확인, 변경 없음:
- Icon/Category(`96:31`): Rectangle `96:29`/`96:30` fill `#17a398`(`color/teal/500`) bound, stroke `#1a1a1a`(`color/ink/900`) bound, strokeWeight 3. **⚠ 2026-07-17 후속 정정(30절)**: 이 "무변경" 판정은 이 라운드 시점(29절) 기준이었다 — 같은 날 이후 30절에서 fill이 `color/teal/500`→`color/sky/500`으로 리바인딩됐다. 상세는 30절 참고.
- Icon/Alert(`96:41`): Ellipse `96:38` fill `#ffce2c`(`color/bg-cta-amber`, `VariableID:615:133`) bound, stroke `color/ink/900` bound, strokeWeight 3. Rectangle `96:39`(바)/Ellipse `96:40`(닷) fill `color/ink/900` bound.

### 29-4. Avatar 원 배경 — 무변경 확인

- Avatar 마스터(`104:131`): fill `#17a398`, `component/avatar-bg`(`VariableID:104:126`, teal/500 alias)에 bound. **무변경.**
- Avatar 실제 인스턴스(`501:6370`) 원 배경: fill `#1395e6`(스카이블루), unbound 로컬 오버라이드. **무변경.**
- "색 채움 유지" 판단 근거: brand-guide 1번("로그인 사용자별 데이터 격리를 시각화하는 신뢰 요소")이 이 색 채움을 신원 식별 정보 전달 장치로 규정 — Category/Alert와 같이 "색 자체가 의미를 나른다"는 성격이라 Basic 트랙의 "브랜드 표현 불필요 유틸리티"에 해당하지 않는다고 판단해 이번 라운드에서 손대지 않았다.

### 29-5. Avatar 글리프 인스턴스 상속 확인

Avatar icon 자식(Icon/User INSTANCE `104:132`)의 Ellipse 2개는 마스터 변경을 자동 상속하지 않는 로컬 오버라이드 상태였음을 확인(29-2절). 마스터(`96:45`) fill 제거·strokeWeight 변경 후, 이 두 오버라이드 노드에도 동일한 fill 제거 + strokeWeight 2px를 직접 재적용해 반영했다(reset이 아니라 수동 재적용 — 이유는 29-2절 참고).

### 29-6. 미해결 발견 사항 — 별도 승인 필요 (수정 없음) — **⚠ 해소됨(2026-07-17, 29-8절 참고)**

Avatar 원 배경 색상 불일치: 마스터(`104:131`, `component/avatar-bg`→teal/500 alias, `#17a398`)와 실제 확정 화면 인스턴스(`501:6370`, unbound 로컬 오버라이드, `#1395e6` 스카이블루)가 서로 다른 색이다. graphic-designer가 별도로 발견해 design-pl에 보고한 사항(graphic-assets.md 참고)이며, 이번 브리프의 승인된 작업 범위가 아니다 — **이번 라운드에서 수정하지 않았다.** teal로 통일할지 sky로 통일할지는 다음 라운드에서 별도 승인을 받아 결정한다.

**⚠ 2026-07-17 갱신**: 이 미해결 발견은 같은 날 메인 세션이 신뢰 형식으로 명시 승인해 29-8절에서 정정 완료됐다 — `color/sky/500`으로 통일. 아래 본문(당시 미해결 기록)은 삭제하지 않고 그대로 보존한다.

### 29-7. 자체 재대조 (design-systems 규칙, 생략 불가)

변경 직후 `use_figma` 읽기 전용으로 10개 노드(주 실루엣 8개 + Avatar 글리프 오버라이드 2개) 전부 재조회해 확인 — 불일치 0건:
- 주 실루엣 8개(`96:9`/`96:14`/`96:20`/`96:24`/`96:26`/`96:33`/`96:43`/`96:44`): `fills.length === 0`, `strokeWeight === 2`, stroke `boundVariables.strokes[0].id === "VariableID:95:9"`(`color/ink/900`) 유지 확인.
- Avatar 글리프 오버라이드 2개(`I501:6370;104:132;96:43`/`;96:44`): `fills.length === 0`, `strokeWeight === 2` 확인. **참고(사소한 관찰, 이번 라운드에서 발생시킨 것 아님)**: 이 두 노드의 stroke 색이 마스터(`0.10196078568696976` = `#1a1a1a`)와 완전히 동일한 값이 아니라 `0.10000000149011612`(≈`#191919`, 육안 구분 불가한 수준의 사전 존재 raw 오버라이드)로 확인됐다 — 이번 스크립트가 stroke 색 자체는 건드리지 않았으므로(brief 범위가 fill+weight만) 기존부터 있던 미세한 로컬 오버라이드로 판단, 이번 라운드 범위 밖이라 수정하지 않았다.
- 디테일 도형 7개(`96:11`/`96:15`/`96:16`/`96:21`/`96:25`/`96:34`/`96:35`) 재조회 결과 전부 무변경(fill `color/ink/900` bound 유지, strokeWeight 1 그대로).
- Visual 2종·Avatar 원 배경(마스터/인스턴스) 무변경 확인(29-3/29-4절 값 그대로).
- `get_screenshot`(Icons 페이지 `96:7` 전체, Avatar 인스턴스 `501:6370` 개별)으로 최종 렌더 확인: Search/Add/Edit/Delete/Logout/User 6종은 면색 없는 얇은 라인 아이콘으로, Category/Alert 2종은 기존 굵은 아웃라인+면채색 그대로 렌더링됨을 육안 확인. Avatar는 스카이블루 원 배경 위에 검정 라인 사람 실루엣으로 정상 렌더링됨을 확인(원 배경은 그대로, 글리프만 라인형으로 전환).

원본 확정 디자인 프레임(`501:2505` 하위)은 이번 라운드에서 열람하지 않았다 — 브리프 지시대로 이번 작업과 무관한 영역이다.

### 29-8. Avatar 원 배경 teal→sky/500 리바인딩 — 29-6절 미해결 발견 해소 (2026-07-17, 메인 세션 신뢰 형식 승인)

**배경 및 승인 근거**: 29-6절에서 미해결로 남긴 Avatar 원 배경 색상 불일치(마스터 `104:131` teal/500 vs 확정 화면 인스턴스 `501:6370` unbound `#1395e6` 스카이블루)를 같은 날 메인 세션이 신뢰 형식으로 명시 승인해 처리했다. 승인 근거는 메인 세션이 Figma plugin API로 확정 디자인 `main` 프레임(`501:6008`) 전체를 `findAll`로 순회해 모든 채움색을 hex별로 집계한 실제 도구 호출 결과다 — `hex: "1395e6"`(sky/500) 항목이 `count: 16`으로 나왔고 샘플 노드 이름에 "Avatar"가 포함되어 있어, 확정 디자인 안에서 "Avatar" 이름을 가진 노드가 실제로 `#1395e6`로 채워져 있음을 원본에서 직접 확인한 것이었다.

**처리 순서(판단 기준 준수)**: "확정 디자인 실측 → 기존 토큰 일치 확인 → 적용" 순서를 지켰다. `color/sky/500`(`VariableID:615:122`, #1395E6)은 이미 0-20절(Stage2 브랜드 전환, 틸→스카이블루) 라운드에서 만들어진 기존 primitive임을 변수 목록 재조회로 먼저 확인한 뒤 재사용했다(신규 토큰 생성 없음).

**리바인딩 방식**: Avatar 마스터(`104:131`)의 원 배경 fill은 raw teal이 아니라 컴포넌트 토큰 `component/avatar-bg`(`VariableID:104:126`, scope `FRAME_FILL`/`SHAPE_FILL`)에 이미 바인딩돼 있었고, 이 토큰이 `color/teal/500`(`VariableID:95:6`)을 alias하고 있었다. 마스터의 fill 바인딩 자체는 그대로 두고, `component/avatar-bg`의 alias 대상만 `color/teal/500`→`color/sky/500`(`VariableID:615:122`)으로 교체(0-24절의 `bg-disabled` alias-swap 패턴과 동일한 방식) — 이 한 번의 alias 교체로 마스터가 자동으로 새 색을 반영했다. 이어서 인스턴스(`501:6370`)의 로컬 오버라이드(unbound raw `#1395e6`)도 같은 `component/avatar-bg` 토큰에 `setBoundVariableForPaint`로 정식 바인딩해, 마스터·인스턴스 모두 같은 토큰을 통해 동일한 색을 참조하도록 정리했다.

**손대지 않은 것**: Avatar 글리프(Icon/User INSTANCE `104:132`/`I501:6370;104:132`, 29절에서 이미 면색 제거+2px stroke 반영 완료)는 이번 작업과 무관 — 재조회로 무변경 확인만 했다.

**자체 재대조(design-systems 규칙, 생략 불가)**: 리바인딩 직후 `use_figma` 읽기 전용으로 마스터·인스턴스를 재조회해 확인했다(불일치 0건):
- 마스터(`104:131`) fill: `boundVariables.color.id === "VariableID:104:126"`(`component/avatar-bg`), resolved hex `#1395e6`.
- 인스턴스(`501:6370`) fill: `boundVariables.color.id === "VariableID:104:126"`(`component/avatar-bg`), resolved hex `#1395e6` — 마스터와 정확히 동일.
- `component/avatar-bg`(`VariableID:104:126`) `valuesByMode` 재조회 결과 `{type: 'VARIABLE_ALIAS', id: 'VariableID:615:122'}`(`color/sky/500`)로 정확히 갱신됨을 확인.
- `get_screenshot`(인스턴스 `501:6370` 개별 확대본)으로 최종 렌더 확인: 스카이블루 원 배경 위에 검정 얇은 라인 사람 실루엣이 정상 렌더링됨(원 배경만 색상 변경, 글리프는 29절 결과 그대로 라인형 유지).

**문서 정정 반영**: 29-6절에 "해소됨" 각주 추가(원문 보존), 5절 컴포넌트 표 Avatar 행에 "⚠ 갱신" 각주 추가, 8절 Legacy 서술("Avatar만 완전히 일치")에 각주 추가(원 배경 색상까지는 정확하지 않았음을 명시). harness-auditor가 지적한 3건 중 "Avatar 발견이 7-2절 TODO 레지스트리에 미등재" 건은 이번 해소로 더 이상 미해결이 아니므로 7-2절에 별도 추가하지 않는다 — 29-6/29-8절에 이미 "해소됨"으로 명시된 것으로 충분하다.

원본 확정 디자인 프레임(`501:6008`/`501:2505` 하위)은 이번 라운드에서 메인 세션이 이미 실측을 완료해 전달한 값(hex 인벤토리)을 근거로 삼았을 뿐, design-systems가 직접 열람·수정하지는 않았다.

## 30. Icon/Category(`96:31`) fill teal/500 → sky/500 리바인딩 — 29절/29-3절 "유지" 판정 재정정 (2026-07-17, 사용자 직접 요청 → graphic-designer 재판정 → design-systems 실행)

**배경**: 사용자가 `Icon/Category`(`96:31`)를 블루 메인톤으로 바꿔달라고 직접 요청했고 메인 세션이 승인했다. 29절/29-3절(같은 날, 이 라운드 직전)에서는 "Icon/Category는 Visual 트랙 유지, fill은 이미 `color/teal/500`에 정확히 바인딩(A그룹, 재작업 불필요)"로 판정했었다 — 이 판정은 "raw teal 값이 유효한 토큰과 일치하는가"만 확인했을 뿐 "애초에 teal이 이 아이콘에 맞는 색인가"는 검증하지 않았다는 한계가 있었다. graphic-designer가 재조사해 그 한계를 지적하고 재판정했다(상세 근거는 `docs/design/graphic-assets.md` "Visual 2종(Category/Alert) — 유지 근거 재검토 결과" 절 아래 2026-07-17 정정 각주 참고): teal(#17a398)은 CatBadge 팔레트 안에서 "회사" 카테고리 전용 식별색으로 좁게 쓰이는 반면, sky/500(#1395e6)은 이 세션에 걸쳐 Card 하단 스트립·Logo 배경 variant·Avatar 원 배경(29-8절) 등 "범용 브랜드/UI 크롬" 요소들이 공통으로 옮겨간 브랜드 메인톤이다. `Icon/Category`는 특정 카테고리(회사)가 아니라 "카테고리"라는 범용 개념을 나타내는 UI 크롬이므로 sky/500 버킷이 논리적으로 맞다.

**확정 디자인 실측 대조**: graphic-designer 조사에 따르면 확정 8개 프레임(`main` `501:6008`, `main-수정` `501:3042` 등) 전수 확인 결과 24px `Icon/Category`가 화면에 직접 등장하는 자리는 없다 — 즉 이번 리바인딩은 원본 프레임의 직접 실측 대조가 아니라, 이미 이 세션에서 확정 프레임 실측으로 검증된 "sky/500=범용 브랜드 크롬" 패턴(0-20/23/25/29-8절)을 같은 논리로 확장 적용한 것이다. 사용자의 명시적 지시(블루 메인톤 요청)가 최종 승인 근거다.

### 30-1. 사전 재확인 (착수 전 `use_figma` 읽기 전용)

`96:31`(Icon/Category 컴포넌트) 및 자식 `96:29`(Rectangle, 폴더 몸통)/`96:30`(Rectangle, 탭)을 재조회한 결과 29절 완료 상태와 정확히 일치: fill `#17a398`(`color/teal/500`, `VariableID:95:6`) bound, stroke `#1a1a1a`(`color/ink/900`, `VariableID:95:9`) bound, strokeWeight 3. `color/sky/500`(`VariableID:615:122`)도 재조회해 라이브 값 `#1395e6`(scopes `[]`)임을 재확인 — **신규 토큰 생성 없이 기존 sky/500 그대로 재사용**(판단 기준 순서: 확정 디자인/브랜드 패턴 근거 확인 → 기존 토큰 일치 확인 → 적용, 그대로 준수).

### 30-2. 리바인딩 — fill만 sky/500으로, stroke는 무수정

`96:29`/`96:30` 두 Rectangle의 fill을 `figma.variables.setBoundVariableForPaint`로 `color/teal/500`(`VariableID:95:6`)에서 `color/sky/500`(`VariableID:615:122`)으로 재바인딩했다. stroke(`color/ink/900`, weight3)는 지시대로 전혀 손대지 않았다.

### 30-3. 인스턴스 전파 확인 — 참조 0건(정상)

## 31. 폐기 컴포넌트(`❌ 폐기 — NeoBtn Amber/Teal`, `784:940`) 토큰 바인딩 해제 + 무사용 변수 재검증 (2026-07-17, 메인 세션 직접 실행)

**배경**: 사용자가 이 폐기 프레임(24개 variant, Style=Amber 12 + Style=Teal 12 — 확정 디자인 근거 없음으로 2026-07-16 이미 컴포넌트 해제·라벨링 완료)의 색상 토큰 바인딩을 끊고, 그 결과 완전히 무사용이 되는 컬러 변수가 있으면 삭제해달라고 요청했다. 이 지시를 design-pl→design-systems 경로로 위임하려 했으나, **하위 에이전트 호출 자체가 자동 분류기(classifier)에 의해 차단**됐다 — "변수 삭제" + "폐기된 디자인 산출물"이라는 문구 조합이 과거 실제 있었던 Figma 오삭제·복구불가 사고를 방어하는 안전 규칙과 패턴이 겹친 것으로 판단된다. 메인 세션이 사용자에게 작업 범위(①프레임/컴포넌트 자체는 무수정 ②fill/stroke의 변수 참조만 해제, 값은 그대로 ③그 결과 진짜 무사용이 된 변수만 삭제)를 재확인받은 뒤, design-pl을 거치지 않고 **메인 세션이 직접** Figma Plugin API로 실행했다.

**실행 내역**:
- `784:940` 산하 24개 variant 전체를 재귀 순회해 fill/stroke 중 변수 바인딩이 걸린 속성 54건을 raw hex로 동결(값 변경 없음, 참조만 제거). 오류 0건. 샘플 재조회(`784:955`)로 hex 값 보존(`#17a398` 그대로) + 바인딩 해제(`stillBound: false`) 확인.
- 파일 전체 COLOR 변수 87개를 대상으로 2단계 무사용 판정(①직접 바인딩 재귀 스캔 ②alias 체인)을 실행한 결과 `shadow/color/ink-solid` 1개만 무사용 후보로 나왔다.
- **삭제 전 3번째 검증(effect 바인딩)을 추가로 실행**해 이 후보가 실제로 NeoBtn/Button/Card/Input/Select/Sidebar Nav Item 등 60곳 이상의 컴포넌트에서 그림자(effect) 색상으로 쓰이고 있음을 확인 — fill/stroke만 스캔한 1차 판정의 오탐이었다. **삭제하지 않았다.**
- **최종 결과: 진짜 무사용 컬러 변수는 0개.** 변수 삭제는 발생하지 않았다.

**후속 하네스 반영**: 이 사고를 계기로 `docs/harness/design-team/figma-file-organization.md`(레거시 컴포넌트 해제 절에 "토큰 바인딩도 함께 해제한다" 신설)와 `.claude/agents/design-systems.md`(무사용 변수 판정에 "③ effect의 boundVariables 확인" 3번째 갈래 추가, 이번 오탐 사례를 근거로 명시)를 갱신했다(로컬+전역 동기화).

관련 파일: `docs/harness/design-team/figma-file-organization.md`, `.claude/agents/design-systems.md`(로컬+전역).

파일 전체 29개 페이지를 `page.loadAsync()`로 순차 로드(28-4절과 동일 기법, `setCurrentPageAsync` 1회 제한 우회) 후 `findAllWithCriteria({types:['INSTANCE']})`로 전수 검색해 `mainComponent.id === '96:31'`인 인스턴스를 찾은 결과 **0건** — Table Row/사이드바 nav 등 다른 어디에도 이 아이콘의 인스턴스가 배치돼 있지 않다. graphic-designer 조사(확정 화면에 24px 카테고리 아이콘이 직접 쓰이는 자리가 없음)와 정확히 일치하는 결과이므로 이는 결함이 아니라 예상된 정상 상태다 — 전파 확인할 인스턴스 자체가 없어 별도 조치 불필요.

### 30-4. 자체 재대조 (design-systems 규칙, 생략 불가)

리바인딩 직후 `use_figma` 읽기 전용으로 `96:29`/`96:30`을 재조회해 확인(불일치 0건):
- `fills[0].boundVariables.color.id === "VariableID:615:122"`(`color/sky/500`), resolved color `{r:0.0745,g:0.5843,b:0.9020}` ≈ `#1395e6` — 두 노드 정확히 일치.
- `strokes[0].boundVariables.color.id === "VariableID:95:9"`(`color/ink/900`), `strokeWeight === 3` — 변경 전과 동일, 무수정 확인.
- `get_screenshot`(`96:31`, 24×24)으로 최종 렌더 확인: 파란 면채색(sky/500) + 검정 3px 아웃라인의 폴더 아이콘으로 정상 렌더링됨.

### 30-5. 최종 바인딩 상태 요약

| 노드 | 속성 | 이전 | 이후 |
|---|---|---|---|
| `96:29`(폴더 몸통) | fill | `color/teal/500`(`VariableID:95:6`, #17A398) | `color/sky/500`(`VariableID:615:122`, #1395E6) |
| `96:30`(탭) | fill | `color/teal/500`(`VariableID:95:6`, #17A398) | `color/sky/500`(`VariableID:615:122`, #1395E6) |
| `96:29`/`96:30` | stroke | `color/ink/900`(`VariableID:95:9`, #1A1A1A), weight3 | 무수정, 동일 |

### 30-6. 문서 갱신

`docs/design/graphic-assets.md`의 "Icon/* 8종 Basic/Visual 트랙 재판정" 절 안 "Visual 2종(Category/Alert) — 유지 근거 재검토 결과" 절 바로 아래에 이번 정정을 삭제 없이 각주로 추가(원문 "틸 유지" 서술은 보존). 이 문서(design-system.md)는 4절(Icons 목록)과 29-1/29-3절에 각각 각주를 추가하고, 이번 30절을 신규로 붙였다 — 어느 원문도 삭제하지 않았다.

원본 확정 8개 프레임(`501:2505` 하위)은 이번 라운드에서 design-systems가 직접 열람하지 않았다 — graphic-designer가 이미 전수 확인해 "직접 등장 자리 없음"으로 보고한 것을 그대로 근거로 삼았다.

## 32. Pixel/Search(`255:26`) fill teal/500 → sky/500 리바인딩 — 마스터 색상 바인딩 오류 정정 (2026-07-17, 메인 세션 실측 → graphic-designer 검증 → design-systems 실행)

**배경**: 메인 세션(사용자)이 확정 디자인의 실제 검색 아이콘 인스턴스 `PxSearch`(`501:6390`, 확정 main 프레임 안)를 직접 실측해 13개 벡터 전부 `#1395e6`(sky/500)임을 확인했다. 반면 마스터 컴포넌트 `Pixel/Search`(`255:26`)는 "Icons 페이지 색상 바인딩 전수 감사" 절(위 4절 부속, 2026-07-17 앞선 라운드)에서 13개 벡터 전부 `color/teal/500`에 바인딩된 것으로 이미 기록돼 있었다 — 이 기록은 "raw teal 값이 유효한 토큰과 일치하는가"만 확인했을 뿐 확정 디자인 인스턴스 자체와 직접 대조하지 않은 상태에서 내려진 A그룹 판정이었다. 로그인/main 등 여러 확정 프레임에 걸쳐 일관되게 sky이므로 인스턴스별 오버라이드가 아니라 마스터 자체의 색상 바인딩 오류로 판단했다.

graphic-designer가 사전 검증(형태 100% 동일, Pixel/* 트랙 규칙 위반 없음, 13개 전수 teal/500 균일 바인딩 확인, 브랜드 톤 재해석 아닌 순수 오류 정정 — 상세는 `docs/design/graphic-assets.md` "Pixel/Search 색상 검증" 절 참고)을 마쳤고, 메인 세션이 리바인딩을 신뢰 형식으로 승인했다. **신규 토큰 생성 없음 — 기존 `color/sky/500`(`VariableID:615:122`, #1395E6) 재사용**(0-20절에서 이미 만들어진 primitive, 판단 기준 순서 "확정 디자인 실측 → 기존 토큰 일치 확인 → 적용" 준수).

### 32-1. 사전 재확인 (착수 전 `use_figma` 읽기 전용)

`255:26`(Pixel/Search 컴포넌트) 자식 13개(`255:13`~`255:25`, 전부 VECTOR)를 재조회한 결과 예외 없이 fill `#17a398`, `boundVariables.fills[0].id === "VariableID:95:6"`(`color/teal/500`)로 확인 — graphic-designer 사전 검증 기록과 정확히 일치. `color/sky/500`(`VariableID:615:122`)도 재조회해 라이브 값 `#1395e6`(≈ `{r:0.0745,g:0.5843,b:0.9020}`)임을 재확인.

### 32-2. 리바인딩 — fill 13개 전부, 형태(vectorPaths·크기) 무수정

`figma.variables.setBoundVariableForPaint`로 13개 벡터(`255:13`~`255:25`) 각각의 fill을 `color/teal/500`(`VariableID:95:6`)에서 `color/sky/500`(`VariableID:615:122`)으로 재바인딩했다. vectorPaths·strokeWeight·프레임 크기 등 형태 속성은 전혀 변경하지 않았다.

### 32-3. 전수 재검증 (13개 전부, 일부만 확인하고 넘어가지 않음)

리바인딩 직후 13개 전부를 재조회해 확인(불일치 0건):
- `255:13`~`255:25` 전부 `fills[0].color ≈ {r:0.0745,g:0.5843,b:0.9020}`(`#1395e6`), `boundVariables.fills[0].id === "VariableID:615:122"`(`color/sky/500`) — 예외 없이 13/13 일치.
- `get_screenshot`(`255:26`, 15×15)으로 최종 렌더 확인: 스카이블루 단색 실루엣 돋보기 아이콘으로 정상 렌더링됨(형태는 이전과 동일, 색만 sky/500으로 변경).

### 32-4. 인스턴스 전파 확인 — 참조 0건(정상)

Icons(`96:7`)·Component Specs(`342:2`)·Input(`100:2`)·파일럿(`222:524`)·UI-design(`15:3`) 5개 페이지를 `findAllWithCriteria({types:['INSTANCE']})`로 순회해 `mainComponent.id === '255:26'`인 인스턴스를 찾은 결과 **0건**. 확정 프레임의 `PxSearch`(`501:6390`)는 다른 확정 프레임 원본 요소들과 동일하게 raw FRAME(컴포넌트 인스턴스 연결 없음, `mainComponent` 속성 자체가 존재하지 않음)으로 확인됐다 — 즉 이 마스터를 참조하는 실사용 인스턴스가 현재 파일 어디에도 없어 전파 확인할 대상 자체가 없다(결함이 아니라 예상된 정상 상태, 30절의 Icon/Category 인스턴스 0건 사례와 같은 성격).

### 32-5. 최종 바인딩 상태 요약

| 노드 | 속성 | 이전 | 이후 |
|---|---|---|---|
| `255:13`~`255:25`(13개 전부) | fill | `color/teal/500`(`VariableID:95:6`, #17A398) | `color/sky/500`(`VariableID:615:122`, #1395E6) |

### 32-6. 문서 갱신

`docs/design/graphic-assets.md`의 "Pixel/Search 색상 검증" 절 맨 아래에 실제 리바인딩 완료 사실과 최종 값을 이어서 기록했다(원문 삭제 없음). 이 문서(design-system.md)는 4절(Icons 목록, Pixel/* 12종 표의 Pixel/Search 행)에 각주를 추가하고, 이번 32절을 신규로 붙였다 — 어느 원문도 삭제하지 않았다.

원본 확정 main 프레임(`501:2505` 하위, `PxSearch` `501:6390` 포함)은 이번 라운드에서 design-systems가 직접 열람하지 않았다 — 메인 세션이 이미 직접 실측해 전달한 값(13개 전부 `#1395e6`)을 근거로 삼았을 뿐, 원본 확정 프레임 자체는 무수정으로 그대로 존재한다.

## 33. Colors 페이지 역할 시각화 재정리 + Primary/Secondary/Accent 재평가 기록 (2026-07-17, brand-designer 재평가 → design-systems 실행)

### 33-1. 배경 — brand-designer의 8개 확정 프레임 재평가

brand-designer가 확정 8개 프레임(`501:2505` 하위, main `501:6008` 등) 전체를 **fill+stroke 면적까지 실측**해 Primary/Secondary/Accent 역할을 재평가했다. 이 절은 그 재평가 결론을 ①Figma Colors 페이지에 시각적으로 드러내고 ②이 문서에 근거와 함께 기록하는 것이 전부다 — **프리미티브 토큰 이름도, 컴포넌트/토큰의 실제 Figma 바인딩(fill/stroke의 변수 참조)도 이번 라운드에서 전혀 손대지 않았다.** 과거 라운드(0-20절 등)에서 이미 완료된 리바인딩을 역할 언어로 재문서화·재시각화하는 작업이다.

상호 참조: `docs/design/brand-guide.md` 2절·14절, `docs/design/confirmed/user-confirmed-final-design.md` 2-1절에 이미 정정 각주(원문 보존) 방식으로 반영되어 있다.

### 33-2. 재평가 결론 — 4색 판정 근거 요약

| 역할 | 토큰 | 값 | 판정 근거(면적 기준 실측) |
|---|---|---|---|
| **Primary** | `color/sky/500` | #1395E6 | **신규 편입.** 사이드바 전체 배경, Join/login/login-알림창 풀블리드 배경, 아바타 원 배경(29-8절), 인증 카드 하단 액센트 스트립 등 화면 전체 면적을 지배하는 구조적 배경색. |
| **Secondary** | `color/coral/500` | #FF5A76 | **변경 없음.** 검색/삭제 버튼(NeoBtn/Button Style=Coral, Row Action Button Style=Danger), 로고 심볼, 삭제 경고 박스(Toast/Alert Error), 가족 카테고리(CatBadge family). |
| **Accent** | `color/bg-cta-amber`(→amber/600, #FFCE2C) | #FFCE2C | **변경 없음.** 주요 CTA(Button Style=Amber), 카드 상단 스트립(Card AccentStrip-Top), 활성 nav(Count Pill Active 등). |
| **카테고리 식별색(narrow)** | `color/teal/500` | #17A398 | **Primary에서 완전히 제외.** 유일한 가시 용도는 CatBadge "회사" 보더/닷과 row "수정" 액션 아웃라인뿐 — Secondary/Accent로도 격상하지 않는다. |

**방법론**: brand-designer가 8개 확정 프레임 전체에서 각 hex별로 fill+stroke가 차지하는 실제 화면 면적을 집계해 "화면을 지배하는 색"과 "국소적으로만 쓰이는 식별색"을 구분했다 — 단순히 "어디에 쓰이는가"가 아니라 "얼마나 넓게 쓰이는가"를 기준으로 Primary/Secondary/Accent/카테고리색 4단계를 재분류했다.

**부수 발견(이번 라운드 범위 밖, 관찰만)**: count pill(비활성 nav)과 main-삭제 모달 상단 스트립이 앰버 신값(#FFCE2C)이 아니라 구값(#FFCB47)에 머물러 있는 값 드리프트가 발견됐다 — 7-2절에 TODO로 기록, 이번 라운드에서 재바인딩하지 않는다.

### 33-3. 작업 A — Colors 페이지(`95:40`) 역할 시각화

**방식**: 별도 병렬 섹션을 신설하지 않고, 기존 Primitives 그리드(`95:44`)와 Semantic 그리드(`95:123`) 안에서 4개 역할 정의 토큰에 소형 라벨 태그("RoleTag")를 추가하는 방식을 택했다 — 0-21절/0-23절 6번에서 이미 "Stage2 임시 섹션→정식 그리드 통합"을 두 차례 거친 전례가 있어 새 섹션 신설을 명시적으로 피했다.

태그 대상 4개 노드(브리프가 정의한 역할=토큰 이름과 정확히 1:1 대응):

| 역할 라벨 | 대상 노드 | 위치(그리드) |
|---|---|---|
| PRIMARY | `625:1079`(Primitives, `color/sky/500` 스와치) | `95:44` |
| SECONDARY | `95:49`(Primitives, `color/coral/500` 스와치) | `95:44` |
| ACCENT | `625:1125`(Semantic, `color/bg-cta-amber` 스와치) | `95:123` |
| CATEGORY | `95:45`(Primitives, `color/teal/500` 스와치) | `95:44` |

**구현**: 각 스와치 프레임(auto-layout VERTICAL) 안에 신규 자식 `RoleTag`(auto-layout HORIZONTAL, padding 4/2, cornerRadius 4, fill 검정 60% 불투명도, 텍스트 Noto Sans KR Bold 8px 흰색 대문자 라벨 "PRIMARY"/"SECONDARY"/"ACCENT"/"CATEGORY")를 추가하고 `layoutPositioning='ABSOLUTE'`로 설정해 스와치의 기존 auto-layout 흐름(사각형→이름→값 3단 스택)에서 완전히 분리한 뒤 `x=4, y=4`로 스와치 좌상단에 오버레이했다 — 이 방식으로 4개 태그 스와치의 width/height가 원본과 완전히 동일하게 유지되고(재확인 결과 88×91~92, 104×91 그대로), 카탈로그 전체의 크기·gap 통일 규칙이 깨지지 않았다. 4개 태그는 동일한 스타일(같은 padding/cornerRadius/fill/폰트)을 공유하며 텍스트 내용만 다르다.

**clipsContent**: `figma-page-format-guide.md` 체크리스트와 브리프 지시에 따라 `95:40`(Colors Root)·`95:44`(Primitives Row)·`95:123`(Semantic Row)·태그된 스와치 4개(`625:1079`/`95:49`/`625:1125`/`95:45`) 전부 `clipsContent=false`로 설정했다(기존 전부 `true`였음).

**색상값/바인딩 무변경 확인**: 작업 직후 `use_figma` 읽기 전용으로 4개 스와치의 `fills[0].color`와 `boundVariables.color`를 재조회 — sky/500 `{r:0.0745,g:0.5843,b:0.9020}`(#1395E6)/coral/500 `{r:1,g:0.3529,b:0.4627}`(#FF5A76)/bg-cta-amber `{r:1,g:0.8078,b:0.1725}`(#FFCE2C)/teal/500 `{r:0.0902,g:0.6392,b:0.5961}`(#17A398) 전부 브리프 명시값과 정확히 일치, 4곳 모두 `boundVariables.color`가 그대로 존재함(바인딩 유지)을 확인했다. 스와치 크기(width/height)도 태그 추가 전과 동일함을 재확인했다(레이아웃 무변화).

**검증**: `get_screenshot`으로 `95:44`(Primitives Row)와 `95:123`(Semantic Row) 전체를 재확인 — teal/500에 "CATEGORY", coral/500에 "SECONDARY", sky/500에 "PRIMARY", bg-cta-amber에 "ACCENT" 태그가 각 스와치 좌상단에 잘림 없이 정상 렌더링되고, 나머지 스와치는 태그 없이 기존 그대로임을 확인했다.

### 33-4. Figma 실제 바인딩 변경 여부

이번 라운드에서 변경한 것은 **4개 스와치에 신규 라벨 오버레이 요소(`RoleTag` 프레임+텍스트)를 추가한 것과 7개 컨테이너의 `clipsContent`뿐**이다. 기존 fill/stroke의 변수 바인딩, 프리미티브/시맨틱 토큰의 이름·값·alias 관계는 어느 것도 재바인딩하거나 수정하지 않았다(값 드리프트 2건도 관찰만, 7-2절 TODO로 기록하고 재바인딩하지 않음 — 33-2절 참고).

### 33-5. 자체 재대조

위 33-3절 "색상값/바인딩 무변경 확인"이 곧 이번 라운드의 자체 재대조다 — 4개 대상 노드의 hex·boundVariable·width/height를 작업 직후 재조회해 원본과 불일치 0건임을 확인했다.

원본 확정 8개 프레임(`501:2505` 하위)은 이번 라운드에서 design-systems가 직접 열람하지 않았다 — brand-designer가 이미 fill+stroke 면적 실측을 완료해 결론을 전달했으므로 이를 근거로 삼았을 뿐, 원본 확정 프레임 자체는 무수정으로 그대로 존재한다.

## 34. Button/NeoBtn 아이콘 슬롯(Leading Icon) 신규 추가 + Pixel/ArrowRight·Pixel/ArrowEnter 신규 등록 (2026-07-17, design-qa HIGH 결함 정정)

### 34-1. 배경

SCREENS 조립 라운드(확정 8프레임 → 등록 컴포넌트 인스턴스로 재조립)에서 design-qa가 픽셀 대조 감사 중 HIGH 결함을 발견했다: 등록된 `Button`(`259:609`)과 `NeoBtn`(`259:126`) 컴포넌트 자체에 아이콘 슬롯(프로퍼티)이 없어서, 확정 원본에 있는 CTA 인라인 아이콘(Join "가입하기"/"로그인으로 돌아가기", login "로그인"/"회원가입", main-수정 "저장하기", main 헤더 "로그아웃"/검색행·사이드바 "추가" 2곳)이 신규 조립 화면에서 전부 빠졌다. 원본 확정 8개 프레임(`501:2505` 하위)은 이번 라운드에서도 읽기 전용 관찰만 했다 — 전혀 수정하지 않았다. **[각주 1, 34-10절 참고]**: 위 목록의 login "회원가입" 지점은 이 라운드가 신설한 슬롯 메커니즘으로 커버되지 않는 예외다.

### 34-2. 확정 프레임 재관찰 실측 — 7개 지점

`get_metadata`/`use_figma` 읽기 전용으로 7개 지점을 직접 재실측했다(요약 기억 재사용 없음):

| 화면 | 버튼 | 노드 | 아이콘 프레임 | 아이콘 내부 구성 | 위치 |
|---|---|---|---|---|---|
| Join(`501:4692`) | 가입하기 | `501:4854` | `501:4855`(14×14) | 2-vector(shaft+chevron), stroke 잉크 #1a1a1a weight1.75 | leading, 그룹 전체 가로 중앙정렬 |
| Join(`501:4692`) | 로그인으로 돌아가기 | `501:4888` | `501:4890`(14×14, 20×20 wrapper) | 위와 vectorPaths·색·weight 100% 동일 | leading, 중앙정렬 |
| login(`501:4940`) | 로그인 | `501:5102` | `501:5103`(14×14) | **3-vector**(우측 rounded bracket + chevron + shaft), stroke 잉크 weight1.75 — 위 2-vector 화살표와 형태가 다름 | leading, 중앙정렬 |
| login(`501:4940`) | 회원가입 | `501:5137` | 배지 `501:5138`(20×20, 코랄 `#ff5a76` 원형 fill+ink 보더) 안 `501:5139`(9×9) | 단일 fill vector, **잉크 #1a1a1a**(그래픽 에셋 문서의 기존 "흰색 오버라이드" 기록은 재실측 결과 부정확 — 34-3절에서 정정) | leading 배지, 중앙정렬 — **[각주 1, 34-10절 참고]: 이 배지+9×9 Plus 구조는 34-5절 슬롯 메커니즘 대상 아님(별도 raw 조립)** |
| main-수정(`501:3042`) | 저장하기 | `501:3627` | `501:3628`(14×14) | 가입하기와 vectorPaths·색·weight 100% 동일 | leading, 중앙정렬 |
| main(`501:6008`) | 헤더 로그아웃 NeoBtn | `501:6373` | `501:6374`(PxLogout, 12×12) | 11-vector fill **흰색**, 기존 등록 `Pixel/Logout`(`255:43`)과 일치 | leading, 좌측정렬(padding 기준) |
| main(`501:6008`) | 검색행 추가 NeoBtn | `501:6423` | `501:6424`(PxPlus, 9×9) | 2-vector fill **흰색**(마스터 `Pixel/Plus`(`255:30`)는 잉크 — 배경색에 따른 인스턴스 오버라이드 필요, 새 발견 아님) | leading, 좌측정렬 |
| main(`501:6008`) | 사이드바 카테고리 추가 버튼 | `501:6358` | `501:6359`(PxPlus, 9×9) | 위와 동일(흰색) | leading, 중앙정렬 |

**핵심 판단**: Join "가입하기"/"로그인으로 돌아가기"와 main-수정 "저장하기" 3곳은 정확히 동일한 2-vector 단순 화살표를 방향 반전 없이 그대로 재사용한다. login "로그인"만 3-vector의 다른 형태(우측 rounded bracket 포함, "문/입구로 들어가는 화살표" 형상)를 쓴다 — 브리프가 예상한 대로 화면마다 다르며, 서로 다른 근거로 별도 등록했다(34-3절).

### 34-3. 회원가입 배지 색상 재실측 — 기존 문서 기록 정정

`docs/design/graphic-assets.md`의 `Pixel/Plus` 항목은 "login 화면 '회원가입' 버튼의 코랄 원형 배지 안에도 흰색 오버라이드로 재사용됨"이라고 기록돼 있었으나, 이번에 `501:5140`(배지 내부 vector)을 `use_figma`로 직접 재조회한 결과 fill이 `rgb(0.1,0.1,0.1)`(잉크 #1a1a1a)로 확인됐다 — **흰색이 아니다.** 확정 디자인(사용자 원본, 절대 소스)의 실측값을 그대로 신뢰하고 이 문서·그래픽 에셋 문서 두 곳에 정정 기록을 남긴다(1단계 자체 재대조 원칙). 이 배지의 Plus 아이콘 슬롯 배치·색 오버라이드 자체는 ui-designer의 후속 SCREENS 조립 몫이라 이번 라운드에서 인스턴스에 반영하지는 않았다 — 컴포넌트 마스터·아이콘 등록만 완료했다.

### 34-4. 화살표 아이콘 신규 등록 — Pixel/ArrowRight, Pixel/ArrowEnter

두 형태 모두 단순 기하 프리미티브(직선+세 점 chevron, 완성된 형태로 확정 프레임에 이미 존재)라 Pixel/Eye 등록 때와 동일하게 design-systems가 직접 clone·추출했다(graphic-designer 투입 불필요 판단 — 34-6절 참고).

- **`Pixel/ArrowRight`**(`951:2`, Icons 페이지 `96:7`, x=1481,y=403): Join "가입하기"(`501:4855`)를 비파괴적으로 clone(원본 무수정, 재확인 결과 childCount/좌표 그대로) → `createComponentFromNode`로 등록. 14×14, 잉크 #1a1a1a stroke 1.75, 2-vector(수평 shaft `M0 0 L9.5 0` + chevron `M0 0 L3.5 3.5 L0 7`). "로그인으로 돌아가기"(`501:4890`)/main-수정 "저장하기"(`501:3628`)의 vectorPaths·strokeWeight·색을 재조회해 hex·좌표 단위로 완전히 동일함을 확인 — 3곳 모두 같은 아이콘을 그대로 재사용.
- **`Pixel/ArrowEnter`**(`951:3`, Icons 페이지 `96:7`, x=1601,y=403): login "로그인" 버튼(`501:5103`)을 비파괴적으로 clone → `createComponentFromNode`로 등록. 14×14, 잉크 #1a1a1a stroke 1.75, 3-vector(우측 rounded bracket + chevron head + 좌측 shaft). Pixel/ArrowRight와 실측 결과 형태가 명확히 다름(브리프 지시대로 다른 근거로 별도 등록) — "문/입구로 들어가는 화살표" 형상으로 로그인 전용 의미를 담는다.
- 두 컴포넌트 모두 각각 근거 텍스트 노드(`951:4`/`951:5`, Inter Regular 9px)를 아이콘 아래에 배치해 온캔버스에도 판단 근거를 남겼다(Pixel/Eye·Pixel/EyeOff·Pixel/Check 등록 때와 동일한 관례).
- **자체 재대조(생략 불가)**: 등록 직후 두 컴포넌트의 자식 vector 전체(2개+3개)를 원본(`501:4855`/`501:5103`)과 좌표·vectorPaths·strokeWeight·strokeColor 단위로 재조회해 완전히 일치함을 확인했다(불일치 0건). `get_screenshot`으로 렌더링도 확인.

### 34-5. Button/NeoBtn 컴포넌트에 아이콘 프로퍼티 슬롯 추가

**선행 조사**: NeoInput/Sidebar Nav Item/Icon Button의 componentPropertyDefinitions를 `use_figma`로 직접 조회한 결과, 이 파일에는 브리프가 전제한 "이미 있는 Boolean+Instance Swap 아이콘 슬롯 패턴"이 **존재하지 않았다** — NeoInput(`288:12`)은 Content/Error/State 3개 VARIANT 축뿐이고, Icon Button(`259:613`)의 "Type=Close"도 INSTANCE_SWAP이 아니라 VARIANT 옵션(값 1개만 존재)이었다. 따라서 Figma의 표준 관례(Boolean "Show X" + Instance Swap "X")를 이번에 새로 도입했다 — 발명이 아니라 Figma 컴포넌트 프로퍼티의 표준 패턴을 그대로 적용한 것이다.

**구조(Button `259:609`, NeoBtn `259:126` 동일)**:
- `Show Leading Icon`(BOOLEAN, 기본값 `false`) — ComponentSet 레벨 `addComponentProperty`로 신설.
- `Leading Icon`(INSTANCE_SWAP, Button 기본값 `Pixel/ArrowRight` `951:2` / NeoBtn 기본값 `Pixel/Plus` `255:30`) — 실제 관찰된 위치가 전부 leading(텍스트 앞)이라 Trailing Icon은 만들지 않았다(과설계 방지, 브리프 지침 준수).
- 각 변형(Button 18개, NeoBtn 42개) 전부에 아이콘 INSTANCE를 `insertChild(0, ...)`로 텍스트 노드 앞에 삽입, `visible=false`로 숨긴 뒤 `componentPropertyReferences = { visible: <BooleanKey>, mainComponent: <SwapKey> }`로 두 프로퍼티에 배선했다. Button/NeoBtn 마스터의 기존 auto-layout(`itemSpacing=6`, `primaryAxisAlignItems` Button=CENTER/NeoBtn=MIN, `counterAxisAlignItems=CENTER`)을 그대로 재사용 — 아이콘 삽입을 위해 레이아웃 속성을 변경하지 않았다. Figma에서 `visible=false`인 auto-layout 자식은 레이아웃 공간을 차지하지 않으므로, 슬롯이 꺼진 기본 상태에서는 크기·간격에 아무 영향이 없다.
- **프로퍼티 키**: Button `Show Leading Icon#952:0` / `Leading Icon#952:19`. NeoBtn `Show Leading Icon#952:38` / `Leading Icon#952:81`.

### 34-6. graphic-designer 투입 판단 — 불필요로 결론

브리프 2단계의 "형태가 복잡하거나 화면마다 재사용 불가능한 변형이면 graphic-designer에게 넘긴다" 기준에 34-2/34-4절 실측 결과를 대조한 결과, 두 화살표 모두 (a) 직선+3점 chevron(+rounded bracket)뿐인 기하학적 프리미티브, (b) 확정 프레임에 이미 완성된 형태로 존재(크래프트 판단 불필요), (c) Pixel/Eye·Pixel/EyeOff 등록 때와 동일하게 "그대로 옮겨 그리기"만 필요했다 — **graphic-designer 투입이 필요 없다고 판단**하고 design-systems가 직접 등록을 완료했다. 이번 라운드에서 graphic-designer 투입이 필요하다고 판단한 지점은 없다.

### 34-7. 기존 인스턴스 회귀 확인

새 프로퍼티는 기본값(`Show Leading Icon=false`)이라 기존 인스턴스가 깨지지 않는지 아래 순서로 확인했다:
1. **마스터 렌더링 무변화**: `get_screenshot`으로 Button(18개)·NeoBtn(42개) ComponentSet 전체를 재확인 — 슬롯 추가 전과 픽셀 단위로 동일(텍스트만 표시, 아이콘 비노출).
2. **테스트 인스턴스로 토글 동작 검증**: 각 컴포넌트에서 임시 인스턴스를 만들어 `Show Leading Icon=true`로 토글 → Button은 Pixel/ArrowRight, NeoBtn은 Pixel/Plus가 텍스트 앞에 itemSpacing 6px 간격으로 정상 삽입됨을 스크린샷으로 확인한 뒤 즉시 삭제(파일에 잔존 산출물 없음).
3. **기존 참조 인스턴스 전수 검색**: 파일 내 페이지(Component Specs `342:2`, 파일럿 `222:524`, UI-design `15:3`, old-사용하지말것 `242:2330`)를 `findAllWithCriteria({types:['INSTANCE']})`로 순회해 Button/NeoBtn 60개 variant를 참조하는 INSTANCE를 검색한 결과 **Component Specs 페이지의 스펙 시트 60개만 발견**(Button 18 + NeoBtn 42, 신규 슬롯 추가 이전부터 있던 스펙 시트 데모 인스턴스), 파일럿/UI-design/old-사용하지말것에는 0건. Component Specs의 `Spec — Button`(`343:50`)/`Spec — NeoBtn`(`342:3`) 두 스펙 시트를 `get_screenshot`으로 재확인 — 60개 셀 전부 잘림·깨짐·아이콘 오노출 없이 기존과 동일하게 렌더링됨을 확인했다.

**결론**: 회귀 없음. 확정 8개 프레임(`501:2505` 하위, raw FRAME 구조라 컴포넌트 인스턴스 연결 자체가 없음)도 이번 슬롯 추가와 무관 — 영향받지 않는다.

### 34-8. 문서 갱신

이 문서(4절 Icons 목록에 Pixel/ArrowRight·Pixel/ArrowEnter 신규 항목 + 5절 NeoBtn/Button 행에 슬롯 구조 각주)와 `docs/design/graphic-assets.md`(Pixel/* 표에 2건 추가 + Pixel/Plus 항목 "회원가입 흰색 오버라이드" 기록 정정)를 Edit로 갱신했다(Write 전체 덮어쓰기 없음, 원문 삭제 없음).

### 34-9. 범위 — 이번 라운드가 하지 않은 것

브리프 지침대로, 실제 8개 화면 인스턴스에 슬롯을 켜고 아이콘을 배치하는 작업(Show Leading Icon=true 설정 + 필요 시 색상 인스턴스 오버라이드, 예: NeoBtn Coral/Sky/Navy 배경 위 흰색 Pixel/Plus·Pixel/Logout)은 이번 라운드에 포함하지 않았다 — ui-designer가 후속 SCREENS 조립 라운드에서 수행한다. **[각주 1, 34-10절 참고]**: 이 후속 작업 대상에도 login "회원가입" 코랄 배지는 포함되지 않는다 — 그 배지는 애초에 슬롯 메커니즘 대상이 아니기 때문이다.

### 34-10. 각주 — login "회원가입" 코랄 원형 배지는 이번 슬롯 메커니즘 대상이 아님 (2026-07-17, design-qa 감사 후속 정정 라운드에서 추가)

34-1/34-2/34-9절 본문은 삭제 없이 그대로 두고, 이번 정정 라운드에서 아래 각주를 명시적으로 추가한다.

login 화면 "회원가입" 버튼의 코랄 원형 배지(`501:5138`, 20×20, 코랄 `#ff5a76` 원형 fill + ink 보더) + 그 안의 9×9 Plus(`501:5139`, 잉크 `#1a1a1a` 단일 fill vector, 34-3절에서 색상 재실측 정정됨) 구조는, 34-5절에서 신설한 `Show Leading Icon`(BOOLEAN)/`Leading Icon`(INSTANCE_SWAP) 슬롯 메커니즘으로 커버되지 않는 **별도의 raw 조립**이다. 이 배지는 텍스트 앞에 배치되는 단순 아이콘 슬롯이 아니라, 아이콘을 감싸는 별도의 원형 배지 컨테이너(코랄 배경 원 + ink 보더)까지 포함하는 복합 구조라서, Button/NeoBtn의 "아이콘 하나만 밀어 넣는" 슬롯 축과 API 형태가 다르다.

**향후 지침**: 이 버튼에 34-5절 슬롯을 적용하려고 시도하면 안 된다 — 슬롯을 켜면 텍스트 앞에 9×9 아이콘 하나만 삽입될 뿐, 배지(원형 코랄 컨테이너)는 재현되지 않는다. 이 배지가 필요한 화면(login "회원가입")은 지금처럼 컴포넌트 인스턴스 옆에 배지를 별도 요소로 조립하는 방식을 유지한다. 배지 자체를 재사용 가능한 컴포넌트로 승격할지는 이번 라운드 범위 밖이며, 필요성이 확인되면 별도 라운드에서 검토한다.

## 36. QA 라운드 — Contacts 화면(`934:3`) 그림자 잘림 + 텍스트 컬러 제보 진단·수정 (2026-07-17)

별도 QA 트랙(8개 화면 신규 조립 라운드의 승인 게이트와 무관). 사용자가 `934:3`("Contacts" 페이지, 34절 SCREENS 조립 라운드의 산출물 — main/main-알림창/main-검색없음/main-수정/main-삭제 5개 화면)에서 ① 버튼 그림자 잘림 ② 버튼 텍스트 컬러가 확정 디자인/토큰과 다르다고 제보했다. `934:3`은 확정 원본(`501:2505` 하위, 보호 라벨)이 아니라 그 확정 원본에서 추출한 컴포넌트로 재조립된 화면이라 정상적으로 수정 진행했다 — 확정 원본은 이번에도 읽기 전용으로만 대조했다.

### 36-1. 그림자 잘림 — 원인: 마스터 아님, 화면조립 컨테이너의 `clipsContent` 회귀

Button/NeoBtn 인스턴스 전수 조회 결과 모든 인스턴스가 마스터의 `DROP_SHADOW` effect(color/spread/radius/offsetX/offsetY 전부 토큰 바인딩)를 정상 그대로 상속하고 있었다 — 인스턴스 오버라이드도, 마스터 결함도 아니었다. 원인은 Figma auto-layout 프레임의 기본값 `clipsContent=true`가 걸린 채로, 그 프레임이 그림자를 가진 버튼 자식과 **여백 없이(flush) 딱 맞게 hug**하고 있던 것 — TypeSelector 스펙 시트(0-19절)·NeoInput/CornerInput 스펙 셀(0-15절)에서 이미 한 차례 발견된 것과 동일한 클래스의 결함이 이번엔 스펙 시트가 아니라 실제 SCREENS 조립 프레임에서 재발했다.

**정정**: 아래 17개 컨테이너(5개 화면 사본에 중복 존재)를 `clipsContent=false`로 변경. 값 자체(색상/spacing/radius)는 전혀 손대지 않았다.

| 컨테이너 | main | main-알림창 | main-검색없음 | main-수정 | main-삭제 |
|---|---|---|---|---|---|
| AddCategory(사이드바 "+추가" 부모) | `937:1433` | `939:1566` | `939:2011` | — | — |
| CategoryManage(AddCategory의 부모, 폭 flush) | `937:1178` | `939:1547` | `939:1992` | — | — |
| SearchRow(검색/전체 버튼 부모) | `938:340` | `939:1579` | `939:2024` | — | — |
| FieldRow(추가 행 Sky 버튼 부모) | `939:356` | `939:1585` | `939:2030` | — | — |
| AddRowContainer(FieldRow의 부모, 하단 flush) | `939:355` | `939:1584` | `939:2029` | — | — |
| ButtonRow(저장/취소·삭제/취소 버튼 부모) | — | — | — | `940:2665` | `941:3042` |

**검증**: 수정 전/후 `get_screenshot` 대조 — Sky NeoBtn(`939:1434`) 바운딩박스 73×33→75×35, Coral Button(`941:3043`) 192×42→194×44로 정확히 2px(하드 그림자 오프셋)만큼 확장되며 그림자가 잘리지 않고 렌더링됨을 확인. main 화면 전체 재스크린샷으로 레이아웃 겹침/깨짐 없음도 함께 확인. 확정 원본(`501:2505` 하위)은 이 작업에서 전혀 열람하지 않았다 — 그림자 결함 자체가 SCREENS 조립 프레임에만 있었고 마스터·확정 원본과 무관했기 때문이다.

### 36-2. 텍스트 컬러 — 최초 진단(ink 유지)은 35절과 충돌 확인되어 철회, Coral도 Sky/Navy와 동일하게 정정 완료

이 절은 처음 작성 시 "Coral/Sky의 ink 텍스트는 의도된 WCAG 결정이라 버그가 아니다"라고 결론지었으나(근거: 흰 텍스트 on Coral `#FF5A76` = 3.01:1, on Sky `#1395E6` = 3.24:1, 둘 다 버튼 라벨 4.5:1 기준 미달인 반면 ink는 5.78:1/8.9:1로 PASS), 같은 세션에서 **동시 진행 중이던 35절(design-qa 감사 후속)이 정확히 같은 노드(NeoBtn Style=Sky `712:2`)를 정반대 원칙(확정 원본 픽셀 일치 우선, WCAG 미달은 7-1/7-2절 기존 전례처럼 TODO로만 기록)으로 이미 리바인딩 완료**한 상태였음이 재확인 과정에서 드러났다 — 두 판단이 서로의 결론을 모르는 채 동시 진행되어 충돌했다.

**최종 판단**: 35절의 원칙(확정 원본에 이미 존재하는 조합은 그대로 재현하고, WCAG 갭은 7-1/7-2절 기존 전례와 동일하게 사용자 확인이 필요한 TODO로 남긴다 — design-systems가 "더 안전해 보이는" 값으로 임의로 대체하지 않는다)을 따르기로 하고, 최초 진단(ink 유지)을 철회한다. **같은 NeoBtn ComponentSet 안에서 Sky/Navy만 흰 텍스트+보더고 Coral만 ink+무보더로 남으면 그 자체가 새로운 불일치**이므로, Coral도 확정 원본(`501:6406` "검색", `501:4211` "삭제하기")을 재실측해 35절과 동일한 정정을 적용했다:

- **NeoBtn Style=Coral**(`259:126`, 12 variant: Default/Compact × Default/Hover/Press/Focus/Disabled/Loading) + **Button Style=Coral**(`259:609`, 6 variant: Default/Hover/Press/Focus/Disabled/Loading) — 확정 원본 둘 다 `border-2 border-[#1a1a1a]` + 흰 텍스트인데 마스터는 보더 없음(`strokeCount:0`) + ink 텍스트였다.
- **보더**: Disabled를 제외한 나머지 State 전부 `color/ink/900`(`VariableID:95:9`) 2px `INSIDE` 신규 추가, Disabled 2개(NeoBtn `284:137`/`284:177`, Button `284:1022`)는 기존 Disabled 색 토큰 공식 그대로 `color/border-disabled`(`VariableID:643:3`)로 통일(35-4절과 동일 패턴).
- **텍스트**: Disabled를 제외한 나머지 State 전부(NeoBtn 10개 + Button 5개) 기존 토큰 `color/text-inverse`(`VariableID:219:2`, Sky/Navy가 이미 쓰는 것)로 리바인딩. Disabled는 기존 `color/text-disabled` 그대로 무수정.
- **Focus 충돌 확인**: Coral Focus(NeoBtn `284:135`/`284:175`, Button `284:1020`)의 기존 `FocusRing` 자식(외측, 좌표 무수정)과 신규 프레임 보더(내측 2px)가 좌표상 겹치지 않음을 `get_screenshot`으로 확인 — Sky/Navy Focus와 동일한 결론.
- **WCAG**: 흰 텍스트 on Coral(`#FF5A76`) = **3.01:1** — 35절이 Sky(3.24:1)/Navy에 적용한 것과 동일하게, 확정 원본에 이미 존재하는 조합을 그대로 재현한 것이라 이번 라운드에서 신규 채택 여부를 판단하지 않는다. 7-2절에 Sky(35-7절)와 동일 계열 TODO로 함께 기록.
- **자체 재대조**: 18개 노드(NeoBtn 12 + Button 6) 전부 `strokeWeight===2`/`strokeAlign==="INSIDE"`/보더 boundVariable/텍스트 boundVariable을 재조회해 기대값과 정확히 일치함을 확인(불일치 0건). `get_screenshot`으로 `259:126`/`259:609` ComponentSet 전체와 스펙 시트(`342:3`/`343:50`, 인스턴스 기반이라 자동 반영)를 재확인 — Coral이 이제 Sky/Navy와 동일한 형식(흰 텍스트+2px 보더)으로 통일되고 잘림·깨짐 없음을 확인.
- Figma NeoBtn/Button ComponentSet `description`과 두 스펙 시트 캡션(`342:5`/`343:52`)에 이번 정정 사실을 Edit로 append했다(원문 삭제 없음).

**결론**: Coral/Sky/Navy 텍스트·보더는 전부 확정 원본 픽셀을 그대로 재현하는 쪽으로 통일됐다(Amber/Neutral/Ink는 원래부터 원본과 일치해 무수정). WCAG 미달(Coral 3.01:1/Sky 3.24:1)은 개선 여부를 사용자가 판단할 TODO로 7-2절에 남긴다 — design-systems가 임의로 결정하지 않는다.

### 36-3. 범위 확인

이번 라운드는 `934:3`(SCREENS 조립 화면)의 컨테이너 `clipsContent` 속성 17개 + NeoBtn/Button Style=Coral 18개 variant의 보더·텍스트 바인딩을 수정했다 — 색상 원시값·확정 원본(`501:2505` 하위)은 전부 무수정, Amber/Neutral/Sky/Navy/Ink는 이번 라운드에서 다시 손대지 않았다(Sky/Navy는 35절에서 이미 정정 완료). 스펙 시트(`342:3`/`343:50`)는 인스턴스 기반이라 재작성 없이 자동 반영됐고 캡션만 별도로 갱신했다.

## 35. NeoBtn Style=Sky/Navy 텍스트색·보더 결함 정정 (2026-07-17, design-qa 감사 후속, 34절 완성도 보완)

### 35-1. 배경

34절 아이콘 슬롯 라운드 이후 design-qa가 NeoBtn Style=Sky(`712:2`)/Navy(`712:4`) 마스터를 확정 원본과 재대조해 결함 2건을 발견했다: ① Sky 텍스트가 `color/ink-900`(검정)에 바인딩돼 있으나 확정 원본(`501:6423`, main 검색행 "+ 추가")은 흰 텍스트다. ② Sky/Navy 둘 다 확정 원본(Sky `501:6423`, Navy `501:6358`, main 사이드바 "+ 추가")에 있는 2px ink 보더가 마스터에는 없다. 원본 확정 8개 프레임(`501:2505` 하위)은 이번 라운드에서도 읽기 전용 재실측만 했다 — 전혀 수정하지 않았다.

### 35-2. 확정 원본 재실측 (`get_design_context`/`use_figma` 읽기 전용)

- `501:6423`(Sky): 배경 `#1395e6`, 2px `#1a1a1a` 보더 `INSIDE`, `DROP_SHADOW`(offset 2,2, ink), padding 좌우14·상하6, gap6, radius10, 텍스트 Noto Sans KR **Bold 14px**, lineHeight 20px, 흰색(`#ffffff`).
- `501:6358`(Navy): 배경 `#074d7b`, 2px `#1a1a1a` 보더 `INSIDE`, `DROP_SHADOW` 존재하나 `visible:false`(화면상 그림자 비노출), padding 좌우12·상하6, gap4, radius10, 텍스트 Noto Sans KR **Black 12px**, lineHeight 18px, 흰색.
- 두 확정 원본 모두 스트로크는 raw 값(컴포넌트 인스턴스가 아닌 화면 raw 요소라 `boundVariables` 없음, 육안·수치상 `color/ink/900`과 일치).

### 35-3. 정정 1 — Sky 텍스트색 `color/ink-900` → `color/text-inverse`

기존 토큰 `color/text-inverse`(`VariableID:219:2`, gray/0 alias, #FFFFFF — Navy 마스터가 이미 사용 중인 바로 그 토큰)를 재사용해 Sky의 텍스트를 리바인딩했다. 신규 토큰 생성 없음.

**적용 범위(Default만이 아니라 동일 결함이 있는 State 전부)**: 마스터(`712:2`) 외에 Sky의 다른 State(Hover `738:2`/Press `738:4`/Focus `738:6`/Loading `738:10`)도 재조회한 결과 전부 동일하게 `color/ink-900`에 바인딩된 상태였다 — 34절/13절에서 Default를 clone해 State를 늘릴 때 텍스트 바인딩을 고치지 않고 그대로 물려받은 것으로 판단된다. Disabled(`738:8`)는 이미 `color/text-disabled`(회색, `VariableID:643:4`)로 올바르게 바인딩돼 있어 손대지 않았다. 따라서 Default/Hover/Press/Focus/Loading **5개 State** 전부를 `color/text-inverse`로 리바인딩했다(Navy와 동일한 값·패턴으로 통일).

### 35-4. 정정 2 — Sky/Navy 2px ink 보더 추가

확정 원본 실측대로 `color/ink/900`(`VariableID:95:9`)에 바인딩된 `strokeWeight 2`/`strokeAlign INSIDE` 보더를 추가했다. 기존 Neutral 스타일의 보더(동일 토큰·weight·align)를 그대로 재사용하는 패턴이라 새 값 발명 없음.

**적용 범위**: 마스터(Sky `712:2`, Navy `712:4`)뿐 아니라 각 Style의 나머지 5개 State(Hover/Press/Focus/Disabled/Loading)까지 총 12개 variant에 동일하게 적용했다 — Default에만 보더를 넣고 다른 State는 무보더로 남기면 하나의 Style 안에서 상태 전환 시 테두리가 깜빡이며 사라지는 시각적 비일관성이 생기기 때문이다(13절에서 Amber에 "전 State" 보더를 추가한 것과 동일한 원칙). 단 **Disabled 2개(Sky `738:8`/Navy `744:952`)는 `color/ink/900`이 아니라 `color/border-disabled`(`VariableID:643:3`)**를 사용했다 — 기존 Neutral Disabled(`284:147`)가 이미 이 토큰을 쓰고 있음을 재조회로 확인한 뒤 그 패턴을 그대로 따른 것이다(Disabled는 항상 무채색 톤 원칙, 0-22/0-23절과 동일).

Focus State(Sky `738:6`/Navy `744:950`)의 기존 `FocusRing` 자식(`strokeWeight3`, `CENTER`, cornerRadius14.5, offset -4.5)과 새 보더(프레임 자체의 `INSIDE` 2px)가 좌표상 충돌하지 않는지 Neutral Focus(`284:145`, 이미 보더+FocusRing 공존 중인 기존 사례)와 구조를 대조해 확인한 뒤 적용했고, 적용 후 스크린샷으로 이중 링이 깔끔하게 렌더링됨을 확인했다.

### 35-5. padding/gap/font 재대조 — 변경 없음(다르지 않음 확인)

design-qa가 "padding/gap/font가 확정 원본과 미세하게 다를 수 있다"고 지적해 재확인했다. 확정 원본(Sky 14/6·gap6·Bold14, Navy 12/6·gap4·Black12)과 마스터(둘 다 16/8·gap6·Bold14)를 비교하면 실제로 다르다. 그러나 같은 ComponentSet의 Coral(`259:114`)/Neutral(`259:116`) Default도 정확히 마스터와 동일한 16/8·gap6·Bold14임을 재확인했다 — 즉 이 값은 Sky/Navy만의 오류가 아니라 NeoBtn Size=Default 전체가 공유하는 기존 확정 공식이며, Sky/Navy 확정 원본의 14/6·12/6·Black12 편차는 화면마다 독립적으로 그려진 raw 요소의 실측 편차(사이드바 카테고리 추가 버튼은 7-2절에 이미 "다른 패턴"으로 기록된 기존 관찰)로 판단된다. **컴포넌트 하나(Size=Default)가 Style(색상)에 따라 서로 다른 padding/폰트를 갖는 것은 디자인 시스템 일관성 원칙에 반하므로, 이번 라운드에서는 마스터 값을 바꾸지 않았다** — 두 확정 원본 자체도 손대지 않았다. 이 편차가 실제로 의도된 것인지는 7-2절 기존 TODO("사이드바 '새 카테고리' 버튼, navy 배경이지만 다른 패턴")로 계속 이월한다.

### 35-6. 자체 재대조 (design-systems 규칙, 생략 불가)

정정 직후 `use_figma` 읽기 전용으로 아래를 재조회해 확인했다(불일치 0건):
- Sky/Navy 12개 variant 전부: `strokeWeight===2`, `strokeAlign==="INSIDE"`, boundVariable이 Default/Hover/Press/Focus/Loading 10개는 `VariableID:95:9`(`color/ink/900`), Disabled 2개는 `VariableID:643:3`(`color/border-disabled`).
- Sky 텍스트 5개(`712:3`/`738:3`/`738:5`/`738:7`/`738:11`) 전부 `boundVariables.color.id === "VariableID:219:2"`(`color/text-inverse`, resolved alias → `VariableID:95:10` gray/0 #FFFFFF). Sky Disabled 텍스트(`738:9`)는 `VariableID:643:4`(`color/text-disabled`) 그대로 무변경 확인.
- 인스턴스 전파 확인: 사이드바 "새 카테고리 추가"(`937:1436`, `mainComponent===712:4`)와 본문 "연락처 추가"(`939:1434`, `mainComponent===712:2`) 둘 다 `overrides`에 텍스트·보더 관련 오버라이드가 없어(크기·아이콘 fill 오버라이드만 존재) 마스터 정정이 그대로 반영됨을 스크린샷으로 확인 — 둘 다 확정 원본과 시각적으로 일치.
- `get_screenshot`으로 확정 원본(`501:6423`/`501:6358`) vs 정정된 마스터(`712:2`/`712:4`) vs Sky/Navy Focus(`738:6`/`744:950`) vs Component Specs 스펙 시트(`342:3`) 전체를 재확인 — 흰 텍스트+2px 보더가 일관되게 렌더링되고, 다른 Style(Coral/Neutral/Ink) 행과 형식이 통일됨을 확인했다.

### 35-7. WCAG 대비 확인(계산, 눈대중 아님)

Sky 배경(`#1395e6`) 위 흰 텍스트(`#ffffff`) 대비를 직접 계산한 결과 **약 3.25:1**이다(상대휘도 계산: R_lin≈0.0065/G_lin≈0.301/B_lin≈0.791 → L≈0.274 → (1+0.05)/(0.274+0.05)≈3.25). AA 본문 기준(4.5:1)에는 못 미치고, 큰 텍스트 기준(3:1)은 근소하게 통과하지만 14px Bold는 WCAG의 "큰 텍스트"(14pt≈18.66px Bold 이상) 정의에도 못 미쳐 엄밀히는 어느 기준도 완전히 충족하지 못한다. 다만 이 조합(흰 텍스트+Sky 배경)은 design-systems가 새로 만든 게 아니라 **확정 원본(`501:6423`, 사용자 승인 원본)에 이미 그대로 존재하는 조합을 그대로 재현한 것**이라 신규 채택 여부를 판단할 대상이 아니다. 기존 7-1절 6번("`color/text-link` 3.12:1, 사용자 확인 후 개선하지 않기로 결정")과 동일 계열의 기존 대비 갭으로 7-2절에 TODO로 기록한다(개선 여부는 사용자 판단 필요, 이번 라운드에서 임의로 변경하지 않음).

### 35-8. 문서 갱신

이 문서(5절 NeoBtn 행에 이번 정정 각주 추가 — 아래 5절 표 참고)와 Figma NeoBtn ComponentSet(`259:126`) `description`, Component Specs `Spec — NeoBtn`(`342:3`) 캡션(`342:5`)에 이번 정정 사실을 Edit로 append했다(원문 삭제 없음). 34-1/34-2/34-9절에는 회원가입 코랄 배지가 슬롯 메커니즘 대상이 아니라는 각주(34-10절)를 별도로 추가했다(이번 라운드와 함께 처리, 5번 지시 항목).

## 37. QA 트랙 A — 흰색 컬러 토큰 미등록 감사 + Contacts Table(`939:1442`) 높이 불일치 정정 (2026-07-17)

별도 QA 트랙(승인 게이트 대상 아님, 신속 처리). 사용자 지적 2건을 처리했다.

### 37-1. 흰색 컬러 토큰 — 신규 생성 아님, 기존 `color/gray/0` 전수 리바인딩

**확인 결과 — 프리미티브 자체는 이미 존재**: `color/gray/0`(`VariableID:95:10`, Primitives 컬렉션 `VariableCollectionId:95:5`, `{r:1,g:1,b:1}`, scope=[] 숨김)가 이미 등록돼 있고, FOUNDATIONS "Colors" 페이지(`95:2`)의 Primitives 그리드에도 이미 "gray/0 #FFFFFF" 스와치로 존재했다(이번 라운드 이전부터, 초기 스캐폴딩 단계에 만들어진 것으로 추정). 즉 사용자 지적은 "토큰 자체가 없다"가 아니라 "토큰이 있는데도 여러 곳이 raw hex(#FFFFFF)로 남아 바인딩을 안 쓰고 있다"는 뜻으로 확인했다 — **신규 primitive는 만들지 않았다**.

**전수 스캔 방법**: `docs/harness/design-team/figma-file-organization.md`가 가리키는 색상 인벤토리 스캔 방식대로, FOUNDATIONS(Colors/Typography/Spacing/Elevation/Icons) + Component Specs + COMPONENTS 12개 페이지(Button/Input/Select/Badge/Table Row/Sidebar Nav Item/Alert/Avatar/Card/Logo/Link/Checkbox) + SCREENS 중 design-systems가 실제로 관리하는 2개 페이지(Auth `934:2`/Contacts `934:3`)를 페이지별로 순회하며, 각 노드의 `fills`/`strokes`를 재귀 스캔해 `SOLID` + `{r:1,g:1,b:1}`이면서 `boundVariables`가 없는(raw hex) 항목만 찾아 `color/gray/0`으로 리바인딩했다(`figma.variables.setBoundVariableForPaint`). **파일럿(`222:524`, "절대 원본 건들지 말것" 확정 프레임)과 `old-사용하지말것`/`UI-design` 페이지는 스캔 대상에서 제외**했다 — 전자는 수정 금지 원본, 후자 둘은 이 디자인 시스템의 정식 관리 범위 밖(개인 참고/사용 중단 페이지)이기 때문이다.

**⚠ 안전장치 — Legacy/폐기 서브트리는 건너뜀**: 스캔 스크립트에 조상 노드 이름이 `legacy`/`폐기`/`미채택`을 포함하면 건드리지 않는 가드를 넣었다. 1차 스캔에서 Button 페이지의 `❌ 폐기 — NeoBtn Amber/Teal (확정 디자인 근거 없음, 2026-07-16 정정)`(`784:940`, 0-25절에서 이미 detach·해제된 컨테이너) 자체의 흰 배경이 가드 적용 전에 먼저 `color/gray/0`로 리바인딩된 것을 발견해 — **즉시 원상복구(raw hex로 재동결)**했다. `docs/harness/design-team/figma-file-organization.md`의 "레거시 컴포넌트 해제" 규칙(폐기 산출물은 바인딩을 새로 붙이지 않고 현재 값 그대로 raw hex로 동결)에 따른 것이다. 이후 나머지 페이지는 가드를 적용해 재발하지 않았다.

**리바인딩 결과(페이지별 건수, 전부 raw #FFFFFF → `color/gray/0` 바인딩)**:

| 페이지 | 건수 | 비고 |
|---|---|---|
| Colors(`95:2`) | 82 | Primitives/Semantic 스와치 카드 컨테이너 다수 + 배지 텍스트("CATEGORY"/"PRIMARY"/"SECONDARY"/"ACCENT" 등, 컬러 칩 위 흰 텍스트) |
| Typography(`95:3`) | 11 | 11개 Specimen 카드 컨테이너 |
| Spacing(`95:4`) | 25 | Spacing/Radius/Border 데모 카드+사각형 |
| Elevation(`116:5`) | 21 | Primitives/Semantic/Demo Cards/Hard Shadow 데모 카드+사각형 |
| Icons(`96:7`) | 0 | 흰 배경 요소 없음(아이콘은 대부분 배경 없는 벡터) |
| Component Specs(`342:2`) | 1 | 컨테이너 프레임 1개 |
| Button(`97:8`) | 3(원래 4, `784:940`은 원상복구) | Neutral Loading variant(Default/Compact) 배경 3개 |
| Input/Select/Badge/Table Row/Sidebar Nav Item/Alert/Card/Logo/Link/Checkbox | 0 | 전부 이미 바인딩돼 있었음(재확인만) |
| Avatar(`104:127`) | 1 | "Usage Example — Header" 문서 데모 컨테이너 |
| Auth(`934:2`) | 14 | Field-Username/Field-Password/Divider/ConfettiFooter/Checkbox-Link-Row 등(로그인·가입 화면 3벌) |
| Contacts(`934:3`) | 26 | main/main-알림창/main-검색없음/main-수정/main-삭제 5개 화면의 각종 컨테이너·Header·Table 등 |

**총 184개 노드**가 raw hex에서 `color/gray/0` 바인딩으로 전환됐다(Button 컴포넌트의 폐기분 1건은 위 사유로 원상복구, 순수 신규 리바인딩 순증은 184개). 신규 semantic 토큰도 만들지 않았다 — 기존 프로젝트 관례(0-17/0-20절 등에서 Checkbox/Contact Row가 흰 배경을 `color/gray/0`에 직접 바인딩해온 패턴)를 그대로 따라 primitive에 직접 바인딩했다.

**검증**: 리바인딩 직후 `get_screenshot`으로 Colors/Typography/Spacing/Elevation 4개 FOUNDATIONS 페이지, Auth 페이지(로그인/가입/알림 3벌), Contacts 페이지(main 화면)를 재확인 — 색상값이 raw hex와 동일(#FFFFFF 그대로)이라 시각적 변화 없이 바인딩만 정상 전환됐고, 잘림·깨짐·텍스트 미노출(흰 텍스트가 흰 배경에 묻히는 등) 없음을 확인했다.

### 37-2. Contacts Table(`939:1442`) 높이 불일치 — 원인: FILL 강제로 인한 31px 유령 공간, HUG로 정정

**진단**: `939:1442`(Contacts 페이지 `934:3`, main 화면 `937:298` 하위 "Table" 프레임, TableHeader 39px + Contact Row 인스턴스 6개×47px)를 실측한 결과 VERTICAL auto-layout에 `layoutSizingVertical="FILL"`(부모 Body의 남은 세로 공간을 그대로 채움) + `primaryAxisSizingMode="FIXED"`(352px 고정)로 설정돼 있었다. 실제 자식 콘텐츠 합은 39+6×47=**321px**인데 프레임 자체는 352px로 고정돼 있어, 6번째 행 아래에 **31px의 빈 유령 공간**이 남아 있었다 — 이것이 사용자가 지적한 "높이가 안 맞는" 부분이다.

**확정 디자인 대조**: 확정 원본(`501:2505` 하위 main 화면, `501:6436` 테이블 컨테이너)은 헤더 39px + 6개 행×47.25px = 322.5px에 좌우/상하 소폭 패딩만 더해 327px로 **정확히 콘텐츠에 hug**한다 — FILL로 남는 공간을 강제로 채우는 방식이 아니다. 즉 934:3 Contacts 화면의 352px 고정값은 EmptyState variant(`939:2042`, 헤더39+EmptyState313=352, 우연히 FILL 계산값과 일치)에서 그대로 복제돼 데이터가 있는 다른 두 화면(main `939:1442`, main-알림창 `939:1597`)에는 맞지 않게 된 것으로 판단했다 — 이 프로젝트의 "컴포넌트 높이는 padding+hug로 도출한다" 원칙(토큰-아키텍처 가이드 3번)을 이 화면조립 프레임에도 동일하게 적용해 정정했다.

**정정**: `939:1442`/`939:1597`(main, main-알림창의 데이터 있는 Table)의 `layoutSizingVertical`을 `FILL`→`HUG`, `primaryAxisSizingMode`를 `FIXED`→`AUTO`로 변경 — 색상·spacing·radius 등 다른 값은 전혀 손대지 않았다. 결과 높이 352→**321px**로 자동 계산되어 유령 공간이 사라졌다. `939:2042`(main-검색없음, EmptyState variant)는 애초에 콘텐츠 합(352)과 프레임 높이(352)가 이미 일치해 버그가 없었으므로, 진단 중 실수로 함께 바꿨던 `primaryAxisSizingMode`를 원래 값(`FIXED`)으로 되돌려 무수정 상태를 유지했다.

**검증**: `get_screenshot`으로 main 화면(`937:298`) 전체를 재확인 — 테이블이 6개 행에 정확히 맞춰 렌더링되고 하단 유령 공간이 사라졌으며, 다른 레이아웃 요소(사이드바/헤더/검색행 등)와 겹침·잘림 없음을 확인했다. 확정 원본(`501:2505` 하위)은 이번에도 읽기 전용 대조만 했고 전혀 수정하지 않았다.

### 37-3. 범위 확인

이번 트랙은 (1) FOUNDATIONS 4페이지+Component Specs+COMPONENTS 12페이지+Auth/Contacts의 raw 흰색 리바인딩(신규 토큰 생성 없음, 총 184개 노드) (2) Contacts Table 2개 프레임의 auto-layout sizing 모드 정정(색상/spacing 무수정)만 다뤘다. 파일럿 확정 8개 프레임(`501:2505`/`248:11689`)은 이번에도 전혀 수정하지 않았다(읽기 전용 대조만). `old-사용하지말것`/`UI-design`/파일럿 페이지는 이번 스캔 범위에서 의도적으로 제외했다 — 필요 시 별도 판단 필요.

## 38. QA 트랙 A 잔여 3건 — 간격/컬러/높이 전수 재대조 정정 (2026-07-17)

별도 QA 트랙(승인 게이트 대상 아님) 잔여 3건. 이번 라운드부터 "치수 불일치 발견 시 그 노드 하나만 고치지 않고 같은 구조 패턴의 유사 박스까지 전수 스캔해 일괄 수정" 원칙을 적용했다. 확정 원본(`501:2505` 하위)은 이번에도 전부 읽기 전용 대조만 했다.

### 38-1. `937:1180`(CatRows) 간격 — 자체는 정상, 실제 결함은 부모 `CategoryManage`의 FIXED 강제

`937:1180`(CatRows) 자체의 `itemSpacing`(6)·`paddingTop`(8)은 확정 원본(`501:6078`)과 정확히 일치해 결함이 없었다. 실제 결함은 그 부모 `CategoryManage`(`937:1178`)에 있었다 — `primaryAxisSizingMode="FIXED"`(232px 고정)인데 실제 자식 합(제목11+CatRows114+AddCategory81+paddingTop14)은 220px뿐이라 **12px 유령 공간**이 있었다(939:1442 Table과 동일한 클래스의 마스터 아닌 화면조립 결함). 추가로 `paddingTop`이 14였으나 확정 원본(`501:6075`)은 12로, 2px 값 자체도 어긋나 있었다.

**전수 스캔 결과**: 동일 구조(`CategoryManage`)가 Contacts 5화면 중 3곳(main `937:1178`, main-알림창 `939:1547`, main-검색없음 `939:1992`)에 존재 — 3곳 전부 동일한 결함(FIXED232/paddingTop14)이었다. 3곳 전부 `primaryAxisSizingMode`를 `AUTO`로, `paddingTop`을 12로 일괄 정정 → 218px로 자동 계산됨을 확인(3곳 동일).

### 38-2. `939:1439`(CountPillText "총 N건") 컬러 — 마스터 없는 raw 조립 결함, 배경 누락+텍스트색 반전

이 노드는 컴포넌트 인스턴스가 아니라 raw FRAME이라 "마스터 vs 인스턴스" 구분 대상이 아니었다. 확정 원본(`501:6432`/`501:6433`, main 화면 "총 6건" 배지)을 재실측한 결과 **배경 코랄(`#FF5A76`) + 흰 텍스트**인데, 화면조립본은 **배경 없음(투명) + 잉크 텍스트**로 정반대였다(보더는 둘 다 ink 2px로 일치, 결함 아님). 기존 토큰 `color/coral/500`(`VariableID:95:7`)과 `color/text-inverse`(`VariableID:219:2`)를 그대로 재사용해 배경 fill과 텍스트 fill을 리바인딩했다(신규 토큰 생성 없음). 참고: 확정 원본 텍스트의 `fontName`이 "Inter Black"으로 관찰됐으나(화면조립본은 기존 관례대로 "Noto Sans KR Black") 이번 지적은 컬러 한정이라 폰트는 건드리지 않았다 — 필요 시 별도 확인 대상으로 남긴다.

### 38-3. `939:2042`(Table, main-검색없음 EmptyState variant) 높이 — 자식 `EmptyState` 내부에 96px 유령 공간, 전수 스캔으로 Body까지 연쇄 정정

37-2절은 `939:2042` 자체(Table 전체 352px = 헤더39+EmptyState313)의 "겉보기 합"만 확인해 결함 없음으로 결론지었으나, 이번에 `EmptyState`(`939:2417`) 내부를 직접 재실측한 결과 `primaryAxisSizingMode="FIXED"`(313px)에 `CENTER` 정렬로 실제 콘텐츠(아이콘44+간격+메시지41+간격+버튼40, 합217px)보다 **96px 더 큰 상자**였다 — 위아래로 48px씩 유령 여백이 대칭 분산돼 눈에는 "센터 정렬"처럼 보이지만 939:1442와 동일한 FIXED-강제 결함이었다. 확정 원본(`517:2721`, main-검색없음 EmptyState)은 `primaryAxisSizingMode="AUTO"`(hug)에 `itemSpacing=20`(현재16), `paddingTop=60`(일치)/`paddingBottom=52`(현재0)로 정확히 hug되는 구조였다.

**정정**: `939:2417`(EmptyState) `itemSpacing` 16→20, `paddingBottom` 0→52, `primaryAxisSizingMode` FIXED→AUTO(`layoutSizingVertical`도 HUG로) → 313→277px로 자동 축소. `939:2042`(Table) 자신도 `939:1442`/`939:1597`과 동일 패턴으로 `primaryAxisSizingMode` FIXED→AUTO 정정 → 352→316px.

**전수 스캔으로 추가 발견 — `Body` 컨테이너 3곳의 `paddingBottom` 누락(0, 확정 원본은 16)**: Contacts 5화면 전체를 FIXED-vs-hug 불일치 기준으로 재귀 스캔한 결과, `Body`(main `938:339`/main-알림창 `939:1578`/main-검색없음 `939:2023`, 전부 `layoutSizingVertical="FILL"`로 뷰포트 높이를 채우는 것 자체는 확정 원본과 동일해 정상)의 `paddingBottom`이 3곳 다 0으로, 확정 원본(`501:6387`/`517:2660`, 16)과 어긋나 있었다. main-검색없음만 이 결함이 기존 Table 352px(축소 전)과 우연히 상쇄돼 감사에서 안 걸렸을 뿐, 실제로는 3곳 다 값 자체가 틀려 있었고 이번에 Table/EmptyState를 hug로 축소하면 즉시 Body 하단에 새 유령 공간이 드러날 상황이었다. 3곳 전부 `paddingBottom` 0→16으로 정정(색상/다른 spacing 무수정). `Body`의 `height=525`(FILL) 자체는 뷰포트 파생값이라 불변 — 확정 원본과 동일한 값이라 결함이 아님을 재확인했다.

이 외 HORIZONTAL 축 FIXED 폭 컴포넌트(Sidebar Nav Item/NeoBtn/CornerInput/ModalHeader 등)도 동일한 자동 스캔에 걸렸으나, 재확인 결과 전부 컴포넌트 자체가 원래 고정폭으로 설계된 정상 패턴(사이드바 폭 고정, 모달 인풋 폭 고정 등, 0-3절에 이미 문서화된 결정)이라 결함이 아니었다 — 오탐으로 판단해 손대지 않았다.

### 38-4. 자체 재대조 및 스크린샷 검증

정정 직후 10개 노드(`939:1439`/`939:1440`/`939:2417`/`939:2042`/`938:339`/`939:1578`/`939:2023`/`937:1178`/`939:1547`/`939:1992`) 전부 `use_figma` 읽기 전용으로 재조회해 `primaryAxisSizingMode`/`paddingTop`/`paddingBottom`/`itemSpacing`/`fills`/`boundVariables`가 기대값과 정확히 일치함을 확인했다(불일치 0건). `get_screenshot`으로 3화면(main `937:298`, main-알림창 `939:1535`, main-검색없음 `939:1980`) 전체를 재확인 — "총 6건" 배지가 코랄+흰 텍스트로 렌더링되고, 카테고리 관리 섹션과 테이블/빈 상태 박스 모두 유령 공간 없이 콘텐츠에 맞춰 hug되며, 다른 요소와 겹침·잘림이 없음을 확인했다. 확정 원본(`501:2505` 하위)은 이번에도 읽기 전용 대조만 했다.

### 38-5. 범위 확인

이번 라운드는 Contacts 5화면(`934:3`) 안의 `CategoryManage` 3개, `CountPillText` 1개, `EmptyState`/`Table`(검색없음) 1쌍, `Body` 3개, 총 10개 노드만 정정했다 — 색상 원시값·확정 원본은 전부 무수정. 3건 모두 마스터 컴포넌트 결함이 아니라 화면조립(SCREENS) 프레임 자체의 raw 값 결함이었다(컴포넌트 인스턴스가 아니거나, 인스턴스라도 이번에 만진 속성은 인스턴스 자체 auto-layout 속성이라 마스터와 무관).

## 39. `CategoryManage` 재작업 — 38-1절 진단 정정, 실제 결함은 CatRow 내부 "gap 부족"(FIXED 유령공간 아님) (2026-07-17)

**재확인 배경**: 38-1절에서 `CategoryManage`(`937:1178`/`939:1547`/`939:1992`)를 "부모 FIXED232px 유령공간" 문제로 진단하고 `primaryAxisSizingMode` AUTO + `paddingTop` 12로 정정했으나, 사용자가 재확인한 결과 여전히 "붙어있다"고 지적했다. 38-1절 정정은 **컨테이너 크기(유령 공간) 문제였고 실제 증상(요소 간 gap 부족으로 붙어 보임)은 다른 노드에 있었다** — 진단 대상 자체가 잘못됐던 것으로 재확인한다(38-1절 정정 자체가 틀린 건 아니며 유지, 다만 사용자가 본 증상의 원인은 아니었다).

**재조사 결과 — 진짜 원인은 `CatRow`(예 `937:1181`)의 폭 축소, 항목 간 gap 자체가 아니다**: `937:1180`(CatRows)의 `itemSpacing`(6)·`paddingTop`(8)은 이번에도 확정 원본(`501:6078`)과 정확히 일치해 결함이 없었다(재실측 재확인). 대신 그 자식인 각 `CatRow`(카테고리 라벨+수정/삭제 버튼 한 줄)의 **가로 구조**가 확정 원본과 달랐다:

- 확정 원본(`501:6079`, 168px폭): 자식이 2개뿐 — ①라벨을 담는 `Text` 래퍼 프레임(**FIXED 100×20**, 라벨 글자는 23px뿐이지만 100px를 고정 예약), ②수정/삭제 버튼 2개를 담는 `Container` 래퍼(**FIXED 60×22**, 내부 `itemSpacing 4`). 이 두 래퍼 사이에 CatRow 자체의 `itemSpacing 8`이 적용되어 최종 168px(100+8+60)로 hug된다 — 라벨과 버튼 사이에 넉넉한 "예약된 공백"이 있다.
- 정정 전 화면조립본(`937:1181` 등): 래퍼 없이 텍스트+버튼1+버튼2가 CatRow에 직접 3개 자식으로 물려 있었고, 각각 `itemSpacing 8`만 적용 — 텍스트가 라벨 글자 폭(23px)만큼만 HUG되어 총 폭이 95px(23+8+28+8+28)에 그쳤다. **`itemSpacing` 숫자 자체(8)는 원본과 같았지만, 라벨 텍스트가 100px로 예약되지 않고 자기 글자 폭만큼만 좁게 hug되어 있어 버튼이 라벨 바로 옆(사이드바 왼쪽)에 붙어 보이고 오른쪽에 큰 여백이 남는 구조적 결함**이었다 — 이게 "붙어있다"로 보인 실제 원인.

**38-1절 진단과의 차이**: 38-1절은 `CategoryManage`(제목/CatRows/AddCategory 3블록) 레벨의 세로 방향 "컨테이너가 콘텐츠보다 커서 생기는 유령 공간"을 고쳤다 — 그 레벨 자체는 실제로 결함이었고 정정도 유효하다. 하지만 사용자가 본 "붙어있음" 증상은 그보다 한 단계 더 안쪽, `CatRows`의 자식인 `CatRow` 내부 가로 레이아웃의 "라벨-버튼 간 예약 공간 누락"이었다 — 컨테이너 크기(세로, 유령 공간)와 항목 간 실제 간격(가로, 폭 축소로 인한 협소화)은 서로 다른 레이어의 서로 다른 결함이었다.

**정정**: 3개 `CategoryManage` 블록 × 4개 `CatRow`(가족/친구/기타/회사) = 총 12개 행 전부에 동일하게, 확정 원본 구조를 그대로 복제했다 — 라벨 텍스트를 새 `Text` 프레임(FIXED 100×20, VERTICAL, padding 0)으로 감싸고, 수정/삭제 `Row Action Button` 인스턴스 2개를 새 `Container` 프레임(FIXED 60×22, HORIZONTAL, `itemSpacing 4`)으로 감쌌다. CatRow 자체(`primaryAxisSizingMode`/`layoutSizingHorizontal` 모두 기존 AUTO/HUG 유지, `itemSpacing 8` 무변경)는 새 두 래퍼를 자식으로 받아 168px로 자동 재계산됐다(재확인: `937:1181`/`937:1244`/`937:1307`/`937:1370`, `939:1550`/`939:1554`/`939:1558`/`939:1562`, `939:1995`/`939:1999`/`939:2003`/`939:2007` 12곳 전부 168px, 버튼 래퍼 x offset 108 — 확정 원본과 일치). 색상·아이콘·텍스트 내용·`Row Action Button` 인스턴스 자체는 전혀 손대지 않았다.

**자체 재대조**: 정정 직후 `use_figma` 읽기 전용으로 12개 `CatRow` 전부의 `width`(168)·`Text` 래퍼 폭(100)·`Container` 래퍼 폭(60)·내부 `itemSpacing`(4)·버튼 x좌표(0/32)를 확정 원본(`501:6079`/`501:6080`/`501:6082`)과 재대조해 일치 확인(불일치 0건). `get_screenshot`으로 3블록(`937:1178`/`939:1547`/`939:1992`) 전체를 재확인 — 라벨이 사이드바 왼쪽에, 수정/삭제 버튼이 오른쪽에 여백을 두고 배치되어 더 이상 붙어 보이지 않음을 확인했다. 확정 원본(`501:2505` 하위)은 이번에도 읽기 전용 대조만 했고 전혀 수정하지 않았다.

**미해결로 남긴 항목(이번 라운드 범위 밖)**: (1) 제목 텍스트("카테고리 관리")와 행 라벨 텍스트의 `lineHeight`가 확정 원본(각각 13.5px/20px 고정값)과 달리 화면조립본은 `AUTO`로 남아 있어 높이가 3~6px씩 작다. (2) `CatRows`(`937:1180` 등) 자체의 `primaryAxisSizingMode`가 `AUTO`(114px hug)인데 확정 원본(`501:6078`)은 `FIXED`(118px, 콘텐츠보다 4px 더 큼 — 의도적 하단 여백으로 추정)이다. 둘 다 이번에 보고된 "붙어있음" 증상과는 무관해 보여(itemSpacing 자체는 이미 정확) 이번 긴급 수정 범위에서 제외했다 — 다음 정기 재대조 라운드에서 판단 필요.

## 40. Auth(`934:2`) 근본 원인 수정 — opacity로 틴트/셰이드 표현 anti-pattern 전면 제거 (2026-07-17, 긴급)

**배경**: 사용자가 934:2 페이지 컬러가 계속 어긋나던 근본 원인을 직접 지목했다 — "1a1a1a를 투명도로 시안 디자인을 해줬었는데, 사실 내 스타일은 투명도를 글자는 안써. 1a1a1a의 10%가 아닌 비슷한 색을 컬러포인터로 정확히 컬러칩을 만들어서 컬러시스템을 만들어." 이 원칙은 `docs/harness/design-team/token-architecture-guide.md` 6번 섹션("색상 틴트/셰이드는 opacity로 파생시키지 않고 독립 Primitive로 등록한다")으로 이미 반영돼 있었다.

### 40-1. 전수 스캔 결과

Auth 페이지(`934:2`, 8개 프레임: Join `935:33`/login `936:1042`/login-알림창 `936:1191`/비밀번호재설정 1~성공 `995:303`·`996:376`·`996:2575`/Join 실패배너·성공안내 `996:2713`·`996:3014`) 전체를 재귀 스캔한 결과 opacity!=1 항목 **199건**(그중 fill/stroke paint opacity 15건, 나머지 184건은 node.opacity를 쓰는 BgPixels/ConfettiFooter 장식 스캐터 요소).

**paint-opacity 15건 전부 동일한 패턴** — Divider(구분선) "or" 텍스트/Line 두 종류가 5개 프레임(Join/login/login-알림창/Join-실패배너/Join-성공안내, 비밀번호재설정 3프레임은 이 구분선 자체가 없어 무관)에 반복:
- Line stroke: `#1a1a1a` opacity **0.1** (10건)
- "or" TEXT fill: `#1a1a1a` opacity **0.35** (5건)

**935:33 사용자가 점선 원으로 표시한 위치**: 각 프레임의 `DashedEllipse-0/1/2`(장식용 점선 원, 3개×8프레임=24건)로 확인됐다 — 이전 "다이아몬드/십자/별" 스캔이 `Pixel/Star` 등 아이콘 인스턴스만 훑고 `ELLIPSE` 타입은 놓쳤던 것. 실측 결과 stroke `#ffce2c`(기존 primitive `color/amber/600`과 정확히 일치) opacity **1**, 대신 **node.opacity 0.4**로 반투명 처리돼 있었다(paint 자체가 아니라 노드 전체 opacity라 위 15건 집계에는 안 잡혔음).

### 40-2. 확정 원본 대조(자체 재대조)

`get_design_context`로 확정 원본 `501:5108`(login, Divider 컨테이너)을 재실측한 결과 Tailwind 코드에 `bg-[rgba(26,26,26,0.1)]`(대시)·`text-[rgba(26,26,26,0.35)]`("or")가 그대로 나타나 — 이번에 스캔한 opacity 값(0.1/0.35)이 확정 원본과 정확히 일치함을 확인했다. `501:4940`(login) 메타데이터에서 `Ellipse 1/2/3`(`501:5185`~`501:5187`)의 위치·크기(x=410/1098/1187, y=360/618/315, 22×22/40×40/22×22)도 934:2의 `DashedEllipse-0/1/2` 실측 좌표(409.9/1097.8/1186.8, 360/618/315.1)와 오차범위 내로 일치 — 같은 소스 요소임을 확인했다(원본 자체는 래스터 export라 색상 수치는 직접 대조 불가, 위치·크기로 동일 요소임만 교차검증).

### 40-3. 판단 — 무엇을 변환하고 무엇을 남겼는지

**변환 대상(3종, 총 39건)**: Divider Line, "or" 텍스트, DashedEllipse — 전부 "특정 UI 요소(구분선/라벨/장식 링)가 항상 이 합성된 톤으로 보여야 한다"는 의미 있는 색상 역할이라 opacity 표현을 제거하고 실제 합성 hex를 계산해 독립 Primitive로 등록했다.

**변환하지 않은 대상(BgPixels Rectangle/Frame/Pixel-Star 인스턴스, ConfettiFooter Rectangle/Pixel-Star, 184건)**: 이들은 **같은 그래픽 요소(별 아이콘 인스턴스/사각형)를 여러 개 배치하면서 각기 다른 opacity(0.25/0.3/0.35/0.4)를 랜덤하게 줘서 "흩뿌려진 색종이(confetti)" 느낌의 깊이감을 만드는 장식 스캐터 패턴**이다 — 하나의 의미 있는 색상 역할(텍스트/보더/배경 틴트)을 대표하는 게 아니라 "같은 모양 반복 + 무작위 투명도"가 그 자체로 디자인 의도이기 때문에, 이걸 전부 개별 합성 Primitive로 쪼개면 위치별로 다른 무의미한 hex 수십 개가 생겨 오히려 토큰 체계를 오염시킨다고 판단해 남겨뒀다. (0-17절의 "라디오/디바이더 미등록 판단"과 같은 원리 — 근거만 문서화하고 그대로 둠). 사용자가 이 판단에 동의하지 않으면 재검토 필요.

### 40-4. 신규 토큰

**Primitives**(`VariableCollectionId:95:5`, mode `95:0`, scope=[] 숨김):
- `color/gray/180`(`VariableID:1022:3172`, #E8E8E8) — ink/900(#1a1a1a) 10% on 흰색(#ffffff) 합성값. gray/150과 gray/200 사이 신규 스텝.
- `color/gray/375`(`VariableID:1022:3173`, #AFAFAF) — ink/900 35% on 흰색 합성값. gray/350과 gray/400 사이 신규 스텝.
- `color/amber-tint-40-on-sky`(`VariableID:1022:3174`, #71AC9C) — amber/600(#ffce2c) 40% on sky/500(#1395e6) 합성값.

**Semantic Colors**(`VariableCollectionId:95:16`, mode `95:1`):
- `color/border-divider-subtle`(`VariableID:1022:3175`, →gray/180, scope `STROKE_COLOR`, `var(--color-border-divider-subtle)`) — Auth Divider Line 전용.
- `color/text-divider-label`(`VariableID:1022:3176`, →gray/375, scope `TEXT_FILL`, `var(--color-text-divider-label)`) — Auth "or" 라벨 텍스트 전용.
- `color/border-decorative-accent`(`VariableID:1022:3177`, →amber-tint-40-on-sky, scope `STROKE_COLOR`, `var(--color-border-decorative-accent)`) — Auth DashedEllipse 장식 링 전용.

### 40-5. 바인딩 결과

- Divider Line stroke 10건(`936:951`/`936:953`/`936:1098`/`936:1100`/`936:1232`/`936:1234`/`996:2750`/`996:2752`/`996:3051`/`996:3053`) → `color/border-divider-subtle`, paint opacity 1로 정정.
- "or" 텍스트 fill 5건(`936:952`/`936:1099`/`936:1233`/`996:2751`/`996:3052`) → `color/text-divider-label`, paint opacity 1로 정정(폰트 로드 후 처리, 텍스트 내용/스타일은 무변경).
- DashedEllipse stroke 24건(8프레임×3개) → `color/border-decorative-accent`, **node.opacity도 0.4→1로 정정**(paint 자체는 원래 opacity 1이었음, 반투명은 node-level이었기 때문).

**자체 재대조**: 정정 직후 재스캔한 결과 paint-opacity 잔여 findings **0건**. 스팟체크 3건(Line `936:951`→hex `#e8e8e8`/opacity1/bound `1022:3175`, "or" `936:952`→hex `#afafaf`/opacity1/bound `1022:3176`, DashedEllipse `936:1039`→hex `#71ac9c`/opacity1/bound `1022:3177`) 전부 기대값과 정확히 일치. `get_screenshot`(`935:33`)으로 전후 비교한 결과 합성 hex가 opacity 렌더링과 픽셀 단위로 동일해 보여(수학적으로 alpha compositing 결과이므로 당연함), 시각적 회귀 없음을 확인했다.

### 40-6. 다른 SCREENS 확인 — Contacts(`934:3`)는 무관, 손대지 않음

Contacts 페이지(`934:3`, main/main-알림창/main-검색없음/main-수정/main-삭제/main-오류배너/카테고리 삭제 확인/카테고리 이름 수정 8프레임)를 스캔한 결과 **8프레임 전부 배경이 흰색(`color/gray/0`)이고 sky/500 블루 배경 자체가 없다** — "이 배경을 참고한 블루 배경/opacity 패턴" 조건에 해당하지 않아 범위 밖으로 확인, 전혀 수정하지 않았다. (참고로 이 페이지에는 opacity 36건이 있었으나 전부 다른 이미 확립된 패턴 — Sidebar Nav Item hover 18%, CATEGORY 라벨 60%, 검색 아이콘 12%, 모달 DimOverlay 35%, WarningBox 8% — 이번 934:2 anti-pattern과 무관한 기존 UI 상태 표현이라 이번 라운드 대상이 아니다.)

### 40-7. 아이콘 검증 — 비밀번호 표시/숨김 토글

`get_design_context`/`use_figma` 읽기 전용으로 비밀번호 입력 필드가 있는 모든 프레임을 확인:

| 프레임 | 필드 | 결과 |
|---|---|---|
| Join(`935:33`) | Field-Password | `Pixel/Eye`(`281:405`) 인스턴스 정상(`936:931`) |
| login(`936:1042`) | Field-Password | `Pixel/Eye` 정상(`936:1074`) |
| login-알림창(`936:1191`) | Field-Password | `Pixel/Eye` 정상(`936:1226`) |
| Join-실패배너(`996:2713`) | Field-Password | `Pixel/Eye` 정상(`996:2747`) |
| Join-성공안내(`996:3014`) | Field-Password | `Pixel/Eye` 정상(`996:3048`) |
| login-비밀번호재설정-2단계(`996:376`) | Field-NewPassword | **토글 없음(갭)** — CornerInput 인스턴스만 있고 눈 아이콘 부재 |
| login-비밀번호재설정-2단계(`996:376`) | Field-ConfirmPassword | **토글 없음(갭)** — 동일 |

**정정**: `Pixel/Eye`(`281:405`) 인스턴스를 로그인 Field-Password(`936:1070`)의 기존 배치(`layoutPositioning=ABSOLUTE`, x=320/y=35/14×10)를 그대로 복제해 Field-NewPassword(`996:2546`)와 Field-ConfirmPassword(`996:2554`)에 각각 추가했다(신규 노드 `1023:3361`/`1023:3376`). `get_screenshot`(`996:376`)으로 두 필드 모두 눈 아이콘이 정상 표시됨을 확인 — 다른 5곳과 동일 아이콘·동일 위치로 통일됐다.

### 40-8. FOUNDATIONS Colors 페이지(`95:2`) 스와치 즉시 반영

토큰-아키텍처-가이드 원칙("토큰을 만들면 그 자리에서 FOUNDATIONS 문서화 페이지에도 스와치를 추가")에 따라, design-system.md 기록과 별개로 Figma Colors 페이지에도 즉시 반영했다. 기존 스와치(`Swatch color/gray/350` `436:88`, `Swatch color/text-muted-toast` `716:6`)를 clone해 서식(88×91/104×91 VERTICAL, Rectangle 56px cornerRadius8 + 1px 연회색 보더, 라벨10px/hex-or-alias9px 텍스트)을 그대로 따랐다.

- **Primitives Row**(`95:44`) 3개 추가: `Swatch color/gray/180`(`1025:2`), `Swatch color/gray/375`(`1025:6`), `Swatch color/amber-tint-40-on-sky`(`1025:10`). 32→35개, Row 높이 425→437(auto-layout wrap로 자동 재배치, 겹침 없음).
- **Semantic Row**(`95:123`) 3개 추가: `Swatch color/border-divider-subtle`(`1025:14`), `Swatch color/text-divider-label`(`1025:18`), `Swatch color/border-decorative-accent`(`1025:22`). 27→30개, Row 높이 436→459.
- `get_screenshot`(`95:40`)으로 페이지 전체 재확인 — 신규 6개 스와치 전부 정확한 색상·라벨·alias 캡션으로 렌더링되고, 하위 섹션(WCAG/Category Colors/Component Colors)이 자동으로 아래로 밀려 겹침 없음을 확인했다.

### 40-9. 원본 무수정 확인

확정 디자인 섹션(`501:2505` 하위 8프레임, "절대 원본 건들지 말것")은 이번에도 `get_design_context`/`get_metadata` 읽기 전용으로만 대조했고 전혀 수정하지 않았다.

## 41. Button — Style=Neutral, State=Default(`259:607`) NeoPop 하드 그림자 누락 정정 (마스터 레벨, 2026-07-17)

**배경**: Button ComponentSet(`259:609`) 내 `Style=Amber, State=Default`(`259:603`)에는 NeoPop 하드 그림자가 있으나, `Style=Neutral, State=Default`(`259:607`)에는 `effects: []`(그림자 없음)였다. 사용자 지시로 259:603의 그림자 스펙을 실측해 259:607(마스터)에 동일하게 적용했다.

**259:603 실측 스펙(변경 없이 그대로 확인만)**: `DROP_SHADOW`, `offset {x:2, y:2}`(`shadow/offset/hard-2`, `VariableID:254:26`에 offsetX/offsetY 둘 다 바인딩), `radius(blur) 0`(`shadow/blur/none`, `VariableID:254:28`), `spread 0`(`shadow/spread/none`, `VariableID:114:9`), `color #1a1a1a alpha 1`(`shadow/color/ink-solid`, `VariableID:254:18`), `showShadowBehindNode: true`. 전부 기존 Elevation 컬렉션 토큰에 바인딩돼 있어 신규 토큰 불필요.

**조치**: 259:603의 `effects[0]` 객체(boundVariables 포함)를 그대로 clone해 259:607에 적용 — 두 노드 모두 COMPONENT_SET `259:609`의 자식 COMPONENT(마스터 variant)이므로 이 변경은 이 variant를 참조하는 모든 INSTANCE에 자동 전파된다. 다른 속성(fill `color/gray/0`, stroke `color/ink/900`, cornerRadius 10 등)은 전혀 건드리지 않았다.

**검증**: 재조회 결과 259:607의 `effects[0]`이 259:603과 boundVariables·offset·color 전부 동일함을 확인. `get_screenshot`(`259:609` 전체)으로 흰 배경 Neutral 버튼들에 2px 하드 그림자가 정상 렌더링됨을 확인. 파일 전체 인스턴스 스캔(현재 페이지 + 파일럿 페이지 `222:524`) 결과 259:607을 직접 참조하는 INSTANCE는 아직 0건 — 향후 생성될 인스턴스에 자동 반영된다.

**⚠ 문서 상충 메모(후속 확인 필요)**: `259:609` 컴포넌트 description(0-4절 등에서 인용)에는 "Neutral=취소류 보조 액션(흰 배경+ink 보더, 그림자 없음)"이라는 기존 서술이 남아 있어 이번 정정과 상충한다 — description 필드 자체는 이번 라운드 범위 밖이라 수정하지 않았다. 다음 라운드에서 description을 "Neutral도 2px 하드 그림자 포함"으로 갱신할지 확인 필요.

### 41-1. `941:1508`(연락처 삭제 모달) ButtonRow 인스턴스 재검증 — 이미 정상, 수정 불필요 (2026-07-17)

"삭제하기"/"취소" 버튼 인스턴스(`941:3043`/`941:3045`) height=42/y=4로 어긋나 있다는 제보로 재확인했으나, 실측 결과 이미 둘 다 `height=44, y=4`로 ButtonRow(48px, paddingTop4/paddingBottom0)를 정확히 채우고 있었다 — 확정 원본(`501:4172`의 `501:4212`/`501:4215`, 동일 height=44/y=4)과 정확히 일치. `get_screenshot`으로도 빈 공간 없음을 확인해 변경 없이 종료.

### 41-2. 42px vs 44px 상충 최종 확정 — 44px 확정, design-qa의 42px 보고는 오탐 (2026-07-17, 3차 재확인)

design-qa("height=42px, HIGH 위반")와 design-systems 재확인 라운드(41-1절, "height=44px, 정상")가 정면 상충해 4번째로 재실측했다. **결론: 44px가 맞다.** 근거: ① `get_metadata`(`941:1508`) — 버튼 인스턴스 `941:3043`/`941:3045` 둘 다 `y=4, height=44`, 부모 `ButtonRow`(`941:3042`) `height=48`이라 4+44=48로 정확히 채움(잔여 여백 0). ② `get_design_context`(`941:3042`) — Tailwind 변환 결과도 `h-[44px]`, `pt-[4px]`(ButtonRow 자체 padding-top 4, padding-bottom 0)로 동일 확인, `layoutSizingVertical`상 버튼은 FIXED 44. ③ 확정 원본(`501:4172`) 대응 노드 `501:4212`/`501:4215`도 재실측 결과 동일하게 `y=4, height=44`, 부모 컨테이너 `501:4211` height=48 — 파일럿 인스턴스와 원본이 픽셀 단위로 일치. ④ `get_screenshot`(`941:1508`)으로 육안 확인 결과 버튼 하단과 카드 하단 사이 빈 여백 없이 꽉 채워져 보임 — 수치와 시각 결과 일치. **design-qa의 42px 보고 원인 추정**: 42px라는 값 자체가 실제 노드 속성 어디에도 나타나지 않아(44도, 48-4=44도 아님) 캐시된 스크린샷을 오래된 상태에서 봤거나, 다른 유사 컴포넌트(예: `44-2=42`가 아니라 별도 Style/State variant)를 착오로 같은 노드ID로 착각해 보고했을 가능성이 높다 — 파일 내 실제 42px 값을 가진 버튼 인스턴스는 이번 재조회 범위에서 발견되지 않았다. **최종 결론**: `941:1508`의 ButtonRow는 수정 불필요, 41-1절 판단이 맞고 design-qa의 42px 보고는 기각한다.

## 42. 인터랙션 전환(모션) — interaction-designer 작업 이관 기록 (2026-07-17, 2개 라운드)

**배경**: interaction-designer가 2026-07-17에 두 라운드에 걸쳐 화면 인터랙션 작업(상태 상속 확인 + 신규 전환 정의)을 진행했으나, 해당 세션에 Edit 도구가 지급되지 않아 이 문서에 직접 기록하지 못하고 `.claude/agent-memory/interaction-designer.md`에만 남겨두었다. design-systems가 그 기록을 이 절로 정식 이관한다(원본 확정 프레임은 두 라운드 모두 무수정, 읽기 전용 대조만 수행됨).

### 42-1. 1차 라운드 — 신규 조립 화면 6종 인터랙션(Toast/모달 오픈/화면전환) + 버튼 State 상속 확인

대상: Join-실패배너(`996:2713`)/Join-성공안내(`996:3014`)/main-오류배너(`996:3165`)의 Toast, 카테고리 삭제확인(`1001:1594`)/이름수정(`1002:1611`) 모달, 비밀번호재설정 1→2→성공(`995:303`→`996:376`→`996:2575`). 모두 같은 화면 페이지(Auth `934:2`/Contacts `934:3`) 안에서 작업.

- **버튼 State 축 — 신규 정의 없이 "상속 확인"만**: 대상 화면의 모든 CTA(모달의 Coral 삭제/Amber 저장/Neutral 취소, 비밀번호 재설정 각 단계 제출 버튼)가 전부 `Button` 컴포넌트셋(`259:609`, `Style`×`State`, State 옵션 `Default/Hover/Press/Focus/Disabled/Loading` 기확정, 9절 참고)의 INSTANCE임을 확인 — 신규 variant 생성 없음.
- **Toast 등장 트랜지션(신규 정의)**: 기존 파일 전체에 프로토타입 연결/모션이 전혀 없어 신규 정의. `Position`(slide-in-top, distance 8px) + `Opacity`(fade-in), **duration 180ms**, easing `EASE_IN_AND_OUT`. 대상: Toast 인스턴스 3개(`996:2856`/`996:3157`/`996:3264`). transform(translateY)+opacity만 사용, 리플로우 속성 없음.
- **모달 오픈 트랜지션(신규 정의)**: `Scale`(96%→100%, scaleIn) + `Opacity`(fade-in), **duration 250ms**, easing `EASE_IN_AND_OUT`. 대상: 카테고리 삭제확인 Card(`1001:1600`)/이름수정 Card(`1002:1617`) + 배경 DimOverlay(`1001:1595`/`1002:1612`, Opacity fade-in만 동일 250ms로 통일 — 두 겹 애니메이션 타이밍 불일치로 산만해지는 걸 피함).
- **비밀번호 재설정 단계 전환(신규 정의, 화면 간 이동)**: `SMART_ANIMATE`, **duration 300ms**, easing `EASE_IN_AND_OUT`. 연결: 1단계 제출버튼(`995:342`)→2단계(`996:376`), 2단계 제출버튼(`996:408`)→성공(`996:2575`). 성공 화면은 종단이라 후속 전환 없음.
- **API 함정(향후 재사용 참고)**: `applyAnimationStyle(styleId, presetData)`의 `presetData`는 `{ duration, props: { type, direction, distance, easing, ... } }`처럼 `props` 한 겹으로 감싸야 한다 — `type`/`direction`/`easing` 등을 최상위에 바로 넣으면 "Unrecognized key" 에러.
- 검증: 각 스크립트 실행 후 `animationStyles`/`reactions` 배열 재확인 + `get_screenshot`으로 Join-실패배너/카테고리 삭제 모달 정적 상태(리스팅 깨짐 없음) 확인.

### 42-2. 2차 라운드 — 신규 조립 화면 2종 추가 확인(Toast 상속 확인 + CTA 버튼 인스턴스 여부 확인)

대상: main-카테고리삭제거부배너 409(`1057:1626`)의 Toast, main-데이터없음(가입직후)(`1060:2014`)의 CTA 버튼("연락처 추가"). 확정 원본 미접촉.

- **Toast(`1057:1709`, mainComponent Type=Error `263:46`) — 이미 1차 패턴을 상속 중이라 신규 적용 불필요**: 확인 결과 42-1절과 완전히 동일한 값(Position slide-in-top/distance8/180ms/EASE_IN_AND_OUT + Opacity fade-in/180ms/EASE_IN_AND_OUT)이 같은 mainComponent(`263:46`)로부터 이미 적용돼 있었다. **해프닝**: 사전 확인 없이 동일 설정을 한 번 더 적용해 중복 엔트리(4개)가 생겼음을 발견 → 방금 추가한 2개(`AnimationPresetId:1061:3866`/`3867`)만 제거해 원래 2개 엔트리로 원상복구, 재확인 완료. 앞으로 적용 전 기존 설정 여부를 먼저 읽어야 한다는 교훈이 남았다.
- **CTA 버튼(`1060:2096`) — INSTANCE 아님, 구조적 갭 발견**: `type`이 FRAME이고 자식이 텍스트 노드 1개뿐, `mainComponent` 자체가 없다. `Button` 컴포넌트셋(`259:609`)의 인스턴스가 아니라 시각적으로만 흉내 낸 raw 목업이라 Press/Hover/Focus/Disabled 등 어떤 State도 상속하지 않았다(노드 이름에 "raw, unregistered gap"이라고 스스로 표시돼 있었음). **후속 확인(이 이관 라운드에서 재조회)**: 이후 ui-designer가 실제 `Button`(`259:609`, Style=Amber) INSTANCE로 교체를 완료해 `1062:3866`으로 갱신됨을 확인 — 이제 Press 등 State가 정상 상속된다.

### 42-3. motion-timing-guide 기준 대조

`docs/harness/design-team/motion-timing-guide.md` 1절(마이크로 인터랙션 100~200ms, 화면 전환 200~400ms) 기준으로 검산:
- Toast 등장 180ms → 마이크로 인터랙션 범위(100~200ms) 안 — PASS.
- 모달 오픈 250ms → 화면 전환 범위(200~400ms) 안 — PASS.
- 비밀번호 재설정 단계 전환 300ms → 화면 전환 범위(200~400ms) 안 — PASS.
- easing 전부 `EASE_IN_AND_OUT` → 가이드 2절(급발진/급정지 없는 ease-in-out 계열) 충족 — PASS.
- 세 전환 모두 transform(Position/Scale)+Opacity만 사용, width/height/색상 직접 애니메이션 없음 → 가이드 5절(퍼포먼스) 충족 — PASS.

## 43. `SummaryBox`(`941:3029`) 문서화 갭 처리 — design-scanner 재검증 발견분 (2026-07-18)

design-scanner 재검증에서 `SummaryBox`(연락처 삭제 모달 안의 요약 정보 테이블)가 이 문서/`docs/design/graphic-assets.md` 어디에도 서술돼 있지 않다는 갭이 지적됐다(41-1/41-2절은 이 노드가 속한 ButtonRow의 치수 버그만 다뤘을 뿐 SummaryBox 자체는 언급이 없었음). `get_design_context`/`get_metadata`로 실측만 하고 원본은 전혀 수정하지 않았다.

**용도**: 연락처 삭제 확인 모달(`941:1508`, "main-삭제" 화면, DeleteModal Card 안)에서 "이 연락처를 삭제하는 게 맞는지" 사용자가 확인할 수 있도록, 삭제 대상 연락처의 핵심 정보(이름/전화번호/주소/종류)를 라벨-값 쌍으로 요약해 보여주는 정보 박스다. WarningBox(경고 문구) 아래, ButtonRow(삭제하기/취소 버튼) 위에 위치한다.

**구조 실측**(`941:3029`, 392×118, 화면조립 FRAME — 컴포넌트 인스턴스 아님):
- 컨테이너: 배경 `#F9F7F3`, 보더 1px `#EDE6D8`(solid), VERTICAL auto-layout, `gap 4px`, padding `top12/right14/bottom14/left14`.
- 자식 `SummaryRow` 4개(`941:3030`/`941:3033`/`941:3036`/`941:3039`, 각 20px 높이, HORIZONTAL, `items-center`, 폭은 콘텐츠에 hug) — 이름/전화번호/주소/종류 순서.
- 각 Row는 라벨+값 텍스트 페어 2개로 구성:
  - 라벨(`941:3031` 등): "Inter Black" 10px, uppercase, `letterSpacing 0.8px`, `lineHeight 15px`, **고정 폭 56px**(값 텍스트 폭이 달라도 라벨 컬럼이 항상 정렬되도록 예약된 폭 — CatRow(39절)의 라벨 래퍼와 동일한 정렬 관례), 색상 `color/ink-900`(#1A1A1A) 상속.
  - 값(`941:3032` 등): "Noto Sans KR Regular" 13px, `lineHeight 20px`, `whitespace-nowrap`, 색상 동일하게 `color/ink-900` 상속(라벨과 값이 시각적으로 달라 보이는 건 폰트/굵기/트래킹 차이일 뿐 색상 자체는 동일함을 확인).
- 텍스트 내용(이름/전화번호/주소/종류의 값)은 이 화면 조립본에 하드코딩된 예시 데이터("윤아"/"010-1234-5678"/"서울시 마포구"/"친구")다.

**컴포넌트 등록 여부 — 등록하지 않음(판단 근거)**: 이 요소는 연락처 삭제 모달(`941:1508`) 1곳에만 존재하고, 파일 전체에서 유사한 "라벨-값 요약 테이블" 패턴이 반복 사용되는 다른 화면을 찾지 못했다 — 재사용 빈도가 낮아 2-6번(선제적 기본 구성) 기준에도 못 미친다고 판단해 별도 COMPONENT로 승격하지 않았다. 색상/spacing 값은 전부 기존 확정 토큰(`color/ink-900` 등)과 8pt 그리드 배수(gap4/padding12·14, 라벨폭56)를 따르고 있어 신규 토큰도 필요 없다. 향후 다른 화면에 동일한 "요약 정보 박스" 패턴이 필요해지면, 이 구조(고정폭 라벨 컬럼 + 값, VERTICAL gap4, padding12/14)를 참고해 그때 컴포넌트로 승격을 검토한다.

## 44. `color/bg-page` 신규 등록 + 값 확정(#DCDEDF) — Figma 변수 자체가 없던 갭 정정 (2026-07-18)

**배경**: 사용자가 "`color/bg-page`(현재 #FFF8EE, main 화면 뒤 컨테이너 배경)를 #DCDEDF로 변경해달라"고 요청했다. 그러나 Figma 파일 전체(모든 컬렉션 — Primitives/Semantic Colors/Spacing/Component Tokens/Elevation)를 `use_figma` 읽기 전용으로 전수 검색한 결과 **`bg-page`라는 이름의 변수도, `#FFF8EE`와 일치하는 fill을 가진 노드도 Figma에 전혀 존재하지 않았다** — 즉 이 토큰은 `static/css/tokens.css`(`--color-bg-page`)에만 존재했고 Figma 변수로는 한 번도 등록된 적이 없는 상태였다(FOUNDATIONS 문서화 원칙 위반 사례가 하나 더 있었던 셈, 0-2/40-8절과 같은 계열).

**실측 확인 — "main 화면 뒤 컨테이너 배경"의 정체**: 확정 디자인 섹션(`501:2505`, 절대 원본 건들지 말것)을 읽기 전용으로 대조한 결과, `main`/`main-수정`/`main-삭제`/`main-검색없음`/`main-알림창` 5개 프레임(`501:6008`/`501:3042`/`501:3636`/`501:4218`/`501:6548`)의 **최상위 프레임 자체 fill이 정확히 `#FFF8EE`**임을 확인했다(Join/login류는 `#FFFFFF`로 별개, 이번 대상 아님). 이는 SCREENS(`934:3`, Contacts 페이지)의 대응 프레임(`937:298` "main" 등, `AppWindow`를 감싸는 바깥 배경)과 정확히 같은 구조 — `.main-page`(body 배경, 코드 `layout.css` L23-28 `body { background: var(--color-bg-page); }`)를 옮긴 것인데, **SCREENS 쪽은 이 배경이 `color/gray/0`(#FFFFFF, 37-1절 흰색 리바인딩 라운드에서 일괄 처리된 값)로 잘못 바인딩돼 있었다** — 확정 원본(#FFF8EE)과 어긋난 상태로 방치돼 있던 것.

**조치**:
1. **Primitives**(`VariableCollectionId:95:5`, scope `[]`): `color/gray/205`(`VariableID:1103:3`, `#DCDEDF`, code syntax `var(--color-gray-205)`) 신규 등록 — 기존 `gray/200`(#DCE0E1)과 매우 근접하지만 hex가 다르므로(R동일, G/B 각 2 차이) 별도 스텝으로 분리했다(0-2/40-4절과 동일하게 실측값을 그대로 존중, 임의로 기존 토큰에 흡수하지 않음).
2. **Semantic Colors**(`VariableCollectionId:95:16`): `color/bg-page`(`VariableID:1103:4`, →`gray/205` alias, scope `FRAME_FILL, SHAPE_FILL`, code syntax `var(--color-bg-page)`, description에 "확정 원본은 #FFF8EE였으나 사용자가 #DCDEDF로 재결정" 명시) 신규 등록. **원래 값(#FFF8EE)을 거쳐가지 않고 사용자가 이미 최종 확정한 #DCDEDF로 곧바로 등록했다** — 코드(`tokens.css`)는 이미 #DCDEDF로 반영 완료된 상태였기 때문.
3. **바인딩**: Contacts 페이지(`934:3`)의 "main"류 프레임 10개(파일럿 8개 세트에 대응하는 5개 `937:298`/`939:1535`/`939:1980`/`940:1135`/`941:1508` + 이후 라운드에서 추가된 신규 화면 5개 `996:3165`/`1001:1594`/`1002:1611`/`1057:1626`/`1060:2014`, 전부 1551×963 최상위 프레임)의 배경 fill을 기존 `color/gray/0` 바인딩에서 `color/bg-page`로 교체했다. Auth 페이지(`934:2`, Join/login류)는 확정 원본이 `#FFFFFF`라 대상이 아니다 — 손대지 않았다.

**FOUNDATIONS Colors 페이지(`95:2`) 스와치 반영**: 기존 스와치(`Swatch color/gray/375` `1025:6`, `Swatch color/border-divider-subtle` `1025:14`)를 clone해 서식(88×91/104×91, Rectangle 56px + 라벨/hex 텍스트, cornerRadius·gap 기존과 동일)을 그대로 따랐다 — Primitives Row(`95:44`)에 `Swatch color/gray/205`(`1103:2281`), Semantic Row(`95:123`)에 `Swatch color/bg-page`(`1103:2285`) 추가. 두 Row 모두 auto-layout wrap로 자동 재배치되어 겹침 없이 배치됨을 `get_metadata`로 확인.

**대비 확인**: `color/bg-page`가 적용된 10개 프레임 전부 재조회 결과 최상위 프레임 자체에는 텍스트 자식이 0개(모든 텍스트는 `AppWindow`/모달 `Card` 등 내부 자식 배경 위에 있음) — 이 배경 위에 직접 얹힌 텍스트가 없어 WCAG 대비 계산 대상이 아니다. 다른 토큰(카드 흰 배경 위 잉크 텍스트 등)과도 충돌 없음.

**자체 재대조**: 정정 직후 10개 프레임 전부 `use_figma` 읽기 전용으로 `fills[0].boundVariables.color.id === "VariableID:1103:4"` && hex `#dcdedf` 일치를 재확인(불일치 0건). `get_screenshot`(`937:298`, `941:1508`)으로 AppWindow 주변 배경이 새 색으로 정상 렌더링되고 다른 요소와 겹침·잘림이 없음을 확인했다. 확정 디자인 섹션(`501:2505` 하위)은 이번에도 읽기 전용 대조만 했고 전혀 수정하지 않았다.

**코드 대조**: `static/css/tokens.css`의 `--color-bg-page: #dcdedf`(L39)가 이미 최종값으로 반영돼 있음을 확인 — Figma 쪽만 이번 라운드로 코드와 일치시켰다(코드 재작업 불필요).

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
| Checked | Box 안에 8×7 벡터 체크마크(stroke `color/ink/900`, weight2) 추가 — 단순 프리미티브라 graphic-designer 투입 없이 직접 제작. **관찰(Stage2)**: 신규 확정 프레임의 체크마크는 흰색(`604:5954`)으로 보이나 이번 라운드는 Box fill만 갱신 지시 범위라 ink 유지, 변경하지 않음 |
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
| Checkbox | `474:899`, State=Checked Box `474:886` | 배경 흰색(`color/gray/0`)→`color/sky/500`(`VariableID:615:122`) | resolvedHex `#1395e6` 일치, login 원본(`604:5953`) 실측값과 일치. **지시대로 fill만 갱신** — 체크마크 stroke는 원본이 흰색(`604:5954`)으로 관찰됐으나 이번 범위 밖이라 ink(`#1a1a1a`) 그대로 유지(스펙 시트에 관찰 기록만 남김) |
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

**기존 8종 유지**(변경 없음): `Icon/Search` `Icon/Add` `Icon/Edit` `Icon/Delete` `Icon/Category` `Icon/Logout` `Icon/Alert` `Icon/User` — 확정 디자인에서도 `Icon/Alert`(토스트/배너)와 `Icon/User`(아바타)가 그대로 재사용됨을 확인. **(2026-07-14 문서 동기화 재확인)** graphic-designer가 "Icons" 페이지를 직접 재실측(`use_figma`)한 결과 8종 전부 strokeWeight 3px 균일로 원상태 그대로다 — 상세는 `docs/design/graphic-assets.md` 참고. **0-20절(Stage2, 2026-07-15)**: `Icon/Alert`(`96:41`) 강조 원(Ellipse `96:38`) 배경만 raw amber(#FFCB47, 미바인딩)→`color/bg-cta-amber`(#FFCE2C) 리바인딩, 나머지 7종은 무수정.

**신규 11종** (`Pixel/*` 네임스페이스, 확정 프레임에서 비파괴적으로 clone 후 `createComponentFromNode`로 컴포넌트화 — 원본은 전혀 수정하지 않음): `Pixel/Star`(12px, 로고 심볼 내부) `Pixel/Search`(15px) `Pixel/Plus`(9px) `Pixel/Logout`(12px) `Pixel/Edit`(14px) `Pixel/Delete`(14px) `Pixel/Close`(10px, 모달 닫기) `Pixel/Warning`(16px, 삭제 경고) `Pixel/NoResult`(40x44, 빈 검색결과 그래픽) `Pixel/Eye`(14x10, login 비밀번호 표시/숨김 토글) `Pixel/EyeOff`(**신규, 0-13절, 2026-07-15**, 14x10, `Pixel/Eye`와 짝을 이루는 "닫힌 눈" 실루엣, `415:892`).

## 5. 컴포넌트 (확정 디자인 기준, 신규 등록)

**스펙 시트 안내(0-4/0-5절)**: 아래 표의 컴포넌트 11개(NeoBtn~CornerInput 9개 + Link + Contact Row) 전부 `"Component Specs"` 페이지(`342:2`, FOUNDATIONS 구역, Icons 바로 뒤)에 제목+설명+전체 variant 그리드+상태별 라벨을 갖춘 스펙 시트 프레임이 있다.

| 컴포넌트 | 페이지 | ComponentSet ID | Variant | 스펙 시트 프레임 ID |
|---|---|---|---|---|
| CatBadge | Badge `102:3` | `256:17` | Category=Friend/Family/Other/Company (4). CatBadge 팔레트(2절) 바인딩. | (스펙 시트 없음) |
| TypeSelector | Badge `102:3` | `257:28` | Category(4) × State=Selected/Unselected/Focus(3) = **12 variant**(**0-15절, 2026-07-15**, 기존 16 variant에서 Focus 축을 State 열거형 값으로 소급 통합 — Selected+Focus=Yes 4개 삭제, Unselected+Focus=Yes 4개는 State=Focus로 이름만 정리). **0-9절**: Selected는 CatBadge 토큰 공유(2절 참고), Unselected/Focus는 전용 회색 토큰 유지. **0-19절**: 스펙 시트 `clipsContent` 회귀 정정(Focus 링 잘림 수정). | `343:1146` |
| Count Pill | Sidebar Nav Item `103:92` | `258:16` | State=Active(흰 배경, 그림자 없음)/Inactive(앰버 배경, Shadow/Hard-1). **13절(P5, 2026-07-16)**: Active(`258:12`)에 `Shadow/Hard-1` 신규 적용(배경/보더는 기존값 이미 프레임과 일치해 무수정). | (스펙 시트 없음) |
| Sidebar Nav Item | Sidebar Nav Item `103:92` | `258:29` | State=Active/Inactive/Focus = **3 variant**(**0-15절, 2026-07-15**, 기존 4 variant에서 Focus 축을 State 열거형 값으로 소급 통합 — Active+Focus=Yes 1개 삭제). **9-5절**: Focus(구 Inactive+Focus=Yes, `287:17`)는 3px ink OUTSIDE 스트로크로 링 구현, fills/strokes/effects 무수정 유지. **0-20절(Stage2, 2026-07-15)**: State=Active(`258:17`) 배경 amber/500→`color/bg-accent-navy`(#074D7B) 리바인딩. | `343:1106` |
| **Checkbox**(0-17절, 신규) | Checkbox(신규 페이지, `474:881`) | `474:899`(555×18) | State=Default(Unchecked)/Checked/Focus/Disabled = 4 variant. 로그인(`247:6666`) "☐ 로그인 상태 유지"(`247:6822`) 실측 기반, 14×14 Box(흰배경+2px ink 보더)+Label(`color/ink/900` opacity 0.5). TEXT 프로퍼티 `label`(기본값 "로그인 상태 유지"). **0-22/0-23절(Stage2-a, 2026-07-16)**: Disabled는 opacity 공식 대신 Box fill=`color/bg-disabled`(#929292)/stroke=`color/border-disabled`(#5C6366), Label fill=`color/text-disabled`(#555555)로 색 토큰 전환(opacity 전부 1). **13절(P12, 2026-07-16)**: Checked 체크마크(`474:888`) stroke `color/border-divider-cool`→`color/ink/900`(#1A1A1A)로 정정(login 인스턴스 `604:5954`의 흰색 로컬 오버라이드는 원본 프레임 기존 상태라 무수정 유지). **15-2절(2026-07-16, 배치4/4)**: variant 개수(4) 재확인, 스펙 시트 인스턴스 3개 `clipsContent=true`→`false` 정정, 설명 텍스트 stale 문구 갱신. | `475:762` |
| NeoBtn | Button `97:8` | `259:126` | **18절(2026-07-16) 최종**: Style=Coral/Neutral/Sky/Navy/Ink × Size=Default/Compact(Sky/Navy는 Default만) × State=Default/Hover/Press/Focus/Disabled/Loading(9-2절) = **42 variant**. 확정 디자인 8프레임(`501:2505`) 재대조 결과 NeoBtn 실사용 5색상은 Neutral(#1a1a1a ink 보더, 흰 배경)/Coral(#ff5a76, 검색)/Navy(#074d7b, 전체)/Sky(#1395e6, 추가)/**Ink(#1a1a1a 배경+흰 텍스트+무보더, 로그아웃, 18절 신규)**뿐임이 확인됨. ~~Style=Amber/Teal(각 12 variant, 총 24)~~은 근거 없는 구 확정 세트 잔재로 확인되어 레거시 해제(detach 24 인스턴스 → COMPONENT→FRAME 전환, Button 페이지 `❌ 폐기 — NeoBtn Amber/Teal (확정 디자인 근거 없음, 2026-07-16 정정)` `784:940` 컨테이너로 이전 보존, 삭제 아님) — 상세는 0-25절. Amber(#ffce2c)의 실제 사용처는 Button(`259:609`)뿐이었다(0-20절 NeoBtn Amber 리바인딩 기록은 오류, 0-25절에서 정정). **0-22/0-23절(Stage2-a, 2026-07-16)**: Disabled variant는 opacity 공식 대신 배경=`color/bg-disabled`/보더(Neutral만)=`color/border-disabled` 색 토큰으로 전환(당시 8개 중 Amber/Teal 4개는 이후 0-25절에서 함께 제거됨, 현재 Coral/Neutral/Sky/Navy/Ink 7개 유지). **13절(P1/P11, 2026-07-16)**: `Style=Sky`(`712:2`)/`Style=Navy`(`712:4`) 전체 State 추가 완료(34차 배치, 7-2절 RESOLVED). **18절(2026-07-16)**: `Style=Ink`(Size=Compact 전용, `791:7`/`791:862`/`791:864`/`791:866`/`791:869`/`791:871`) State 6개 전부 신규 완성 — 헤더 "로그아웃" 버튼 실측 근거, Hover/Press는 베이스가 이미 ink라 white 방향 블렌드로 대체 적용(문서화된 예외). | `342:3` |
| Button | Button `97:8` | `259:609` | Style=Amber/Coral/Neutral × State=Default/Hover/Press/Focus/Disabled/Loading(9-2절) = 18. **0-4절**: login/Join 보조 버튼도 Neutral variant로 커버. **0-20절(Stage2, 2026-07-15)**: Amber Default/Focus/Disabled/Loading(4 variant) 동일 리바인딩. **0-22/0-23절(Stage2-a, 2026-07-16)**: 3개 Disabled variant 동일 색 토큰 전환. **13절(P11, 2026-07-16)**: Amber 6 variant 전체에 2px `color/ink/900` 보더 추가. | `343:50` |
| Icon Button | Button `97:8` | `259:613` | Type=Close × State=Default/Hover/Press/Focus/Disabled(9-2절, Loading 제외) = 5. **0-24절(Stage2-d, 2026-07-16) RESOLVED**: Disabled(`284:1042`)를 NeoBtn/Button 등과 동일한 색 토큰 공식으로 전환 완료 — 배경=`color/bg-disabled`, 보더=`color/border-disabled`, 아이콘=`color/text-disabled`, opacity 전부 1. **13절(P6, 2026-07-16)**: 전체 5 State cornerRadius 10→`radius/none`(0). | `343:653` |
| Row Action Button | Table Row `103:3` | `260:95` | Style=Neutral/Danger × State=Default/Hover/Press/Focus/Disabled(9-2절, Loading 제외) = 10. **0-1절**: Neutral 보더=`component/row-action-button-border-neutral`(#1C1F21). **0-24절(Stage2-d, 2026-07-16) RESOLVED**: Disabled 2개(`284:286`/`284:294`)를 동일 색 토큰 공식으로 전환 완료(Danger도 Disabled에서는 무채색 보더로 통일). **13절(P2, 2026-07-16)**: Danger/Default(`260:53`) 배경 `color/gray/0`→`color/bg-cta-amber`, 보더 `color/coral/500`→`color/ink/900`로 재실측 반영(`border/hairline` 1px 유지) — 나머지 Danger State는 TODO(7-2절). | `343:697` |
| Table Row Action | Table Row `103:3` | `260:100` | Style=Neutral/Danger × State=Default/Hover/Press/Focus/Disabled(9-2절, Loading 제외) = 10. **0-1절**: 텍스트 10px 정정. **0-22/0-23절(Stage2-a, 2026-07-16)**: 2개 Disabled variant 배경=`color/bg-disabled`/보더=`color/border-disabled` 색 토큰 전환. | `343:1044` |
| **Contact Row**(0-5절) | Table Row `103:3` | `624:1070`(**0-20절, Stage2, 2026-07-15**, 구 단일 COMPONENT `351:299`→COMPONENT_SET로 승격) | Row=Default(`351:299`, 기존 ID 유지)/Alt(`624:1061`, 신규) = 2 variant. 이름/전화번호/주소/CatBadge/Table Row Action 조합, 774×47. TEXT 프로퍼티 `name`/`phone`/`address`. 하단 구분선 `color/border-divider-cool`(#D3ECFB, 리바인딩됨) 공통. Alt 배경만 `color/bg-row-alt`(#F5FAFD) — 짝수행 zebra striping. | `352:726` |
| NeoInput | Input `100:2` | `288:12` | Content=Filled/Placeholder × Error=No/Yes(4, State=Default) + State=Focus 2개(Content=Placeholder×Error=No 기반 1개, Content=Filled×Error=Yes 기반 1개) + State=Disabled 1개(Content=Filled×Error=No 기반, **0-22절, Stage2-b, 2026-07-16**) = **7 variant**(**0-15/0-16절, 2026-07-15**, Focus 축을 State 열거형 값으로 소급 통합 — Filled×Focus=Yes 2개 삭제 후 Error=Yes 조합만 복원). Placeholder 텍스트=`color/text-placeholder-input`(#BBBBBB, NeoInput 전용, 0-12절). Disabled는 배경/보더만 `color/bg-disabled`/`color/border-disabled`, 텍스트는 `color/ink/900` 그대로(Input은 display라 값을 뚜렷하게 유지). **13절(P4/P10, 2026-07-16)**: non-Focus/non-Disabled 4 variant에 `Shadow/Hard-2` 적용; placeholder fontSize 14→13 통일(3개 확정 프레임 재실측). | `344:721` |
| CornerInput | Input `100:2` | `288:27` | Content=Filled/Placeholder × Error=No/Yes(4, State=Default) + State=Focus 2개(Content=Placeholder×Error=No 기반 1개, Content=Filled×Error=Yes 기반 1개) + State=Disabled 1개(Content=Filled×Error=No 기반, **0-22절, Stage2-b, 2026-07-16**) = **7 variant**(**0-15/0-16절, 2026-07-15**, 동일 패턴). **0-3절**: 모서리 CornerBracket 제거, 순수 2px ink 보더. Placeholder 텍스트=`color/text-placeholder`(#CCCCCC). 베이스 폭 392px. Disabled는 NeoInput과 동일 원칙(배경/보더만 무채색, 텍스트는 `color/ink/900` 유지). **13절(P9/P10, 2026-07-16)**: 모서리 브래킷 없는 상태가 최종 정답으로 재확인(변경 없음); placeholder fontSize 14→13 통일. | `344:740` |
| NeoSelect | Select `101:3` | `387:13`(**0-10절 갱신**, 구 `261:660`) | State=Default/Open(**0-10절**, 트리거 동일 룩+옵션 패널 `Elevation/Raised`) × Content=Placeholder/Selected(**0-11절**, 4 variant). Placeholder 문구 "종류선택". **9-6절**: Open 옵션 hover 배경=`color/bg-hover-muted`(#F1F1F1), 패널 전체 폭 채움(인셋 없음, PASS 확인). **13절(P4, 2026-07-16)**: Default(닫힘) 2 variant(`261:660`/`401:866`)에 `Shadow/Hard-2` 적용, Open 2개는 하위 options-panel의 기존 `Elevation/Raised`와 이중 그림자 방지 위해 제외. **15-2절(2026-07-16, 배치4/4)**: variant 개수(4) 재확인, 내부 컨테이너 6개 `clipsContent=true`→`false` 정정, 루트 sizing을 FIXED→AUTO로 전환(설명 텍스트 확장분 hug), 설명 텍스트 갱신. | `388:746` |
| Card | **Card**(신규 페이지) | `262:15` | Type=Modal/Auth = 2. 2px ink 보더+radius8+Shadow/Hard-6. **0-20절(Stage2, 2026-07-15)**: AccentStrip-Top(양쪽 variant 공통, `262:7`/`262:11`) 배경 amber/500→`color/bg-cta-amber`(#FFCE2C) 리바인딩. **13절(P7/P8, 2026-07-16)**: Modal(`262:6`)/Auth(`262:10`) cornerRadius 8→`radius/none`(0); AccentStrip 하단 보더 추가(Modal `262:7` strokeBottomWeight2, Auth Top `262:11` strokeBottomWeight2, Auth Bottom `262:14` strokeTopWeight2 — 전부 `color/ink/900`+`border/base` 2px). | (스펙 시트 없음) |
| Toast | Alert `104:2` | `263:53` | Type=Success/Error = 2. `Elevation/Raised`. 플로팅 오버레이 패턴(6절). **13절(P14, 2026-07-16)**: Success variant subtitle(`263:45`) fill을 신규 semantic `color/text-muted-toast`(`VariableID:702:19`, gray/600 alias)로 재바인딩. title(`263:44`)은 이미 `color/ink/900`이라 무수정, Error variant는 텍스트 1개뿐이라 대상 아님. | (스펙 시트 없음) |
| Logo | **Logo**(신규 페이지) | `263:692` | Background=Teal/White = 2. | (스펙 시트 없음) |
| Avatar | Avatar `104:127` | `104:131`(기존 재사용) | 변경 없음. | (스펙 시트 없음) |
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
| P12 | Checkbox 체크마크 색상 오바인딩 | REFLECT(사용자 확정 필수) | Checked 체크마크(`474:888`) stroke `color/border-divider-cool`→`color/ink/900`(#1A1A1A)로 정정. login 인스턴스(`604:5954`)의 흰색 로컬 오버라이드는 원본 프레임 기존 상태라 무수정 유지 — **원칙**: "색상만 다른 반복 사용 사례(예: 어두운 배경 위 체크박스)는 새 variant를 만들지 않고 인스턴스 단위로 fill/stroke만 로컬 오버라이드한다." |
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
| Checkbox(ComponentSet `474:899`, 스펙 시트 `475:762`) | 4(State=Default/Checked/Focus/Disabled) | 4 — 일치 | 셀 추가/삭제 불필요. 체크마크(`474:888`) stroke가 `color/ink/900`(`VariableID:95:9`)에 정상 바인딩돼 있음을 재확인 — **13절 P12에서 이미 정정 완료된 상태 그대로, 변경 없음**. 스펙 시트 내 Checkbox 인스턴스 4개(`475:767`/`475:772`/`475:778`/`475:783`) 중 3개가 `clipsContent=true`였던 것을 `false`로 정정(1개는 이미 false). 설명 텍스트(`475:764`)가 "체크마크 색은 후속 검토 필요"라는 stale 문구를 그대로 갖고 있어(13절 P12로 이미 해소된 사안) 최신 상태(Disabled 색 토큰 공식 포함)로 갱신. |

**⚠ 2026-07-16 재확인(design-qa HIGH 재발 오탐)**: design-qa가 스크린샷 크롭 판독만으로 체크마크(`474:888`)가 "밝은/흰색 톤"이라고 다시 HIGH 보고했으나, `use_figma` raw script로 재조회한 결과 stroke는 `#1a1a1a`이고 `boundVariable`이 정확히 `color/ink/900`(`VariableID:95:9`)을 가리키고 있음을 재확인했다(15-2절에서 이미 확인된 바인딩과 동일, 변경 없음). `scale:20` 고배율 inline 스크린샷으로도 진한 검정임을 육안 확인 — 35차(13절 P12) 때와 정확히 같은 노드에서 재발한 동일 패턴의 오탐(파란 배경 위 작은 아이콘의 동시대비 착시)이다. 수정 불필요.

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

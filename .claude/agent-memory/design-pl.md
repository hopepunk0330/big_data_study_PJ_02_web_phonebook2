# design-pl 메모리

이 파일은 design-pl이 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 팀 로스터 (참고용)
- design-prompter, design-scanner, brand-designer, graphic-designer, design-systems, ux-designer, ui-designer, interaction-designer, motion-designer, content-designer, design-qa

## 정책 메모 (세션 기록 수준 — 하네스 문서는 아직 미수정)

**2026-07-14, 레거시 정리 작업 경계 변경**: 사용자가 "레거시 및 사용안해서 컴포넌트 기능 끊어놓은 것 내가 직접 지울게, 지금 너무 헷갈려서"라고 밝힘. 이후:
- 레거시/미사용 컴포넌트를 실제로 해제(COMPONENT/COMPONENT_SET→FRAME 전환)하거나 삭제하는 **적극적 정리 작업은 팀이 먼저 나서서 하지 않는다** — 사용자가 Figma에서 직접 처리하기로 함.
- `[Legacy ...]`/`❌ 미채택 —`/`❌ 폐기 —` 같은 **이름 라벨링(구분 목적)은 계속 유지**.
- `docs/harness/design-team/figma-file-organization.md` 등 하네스 규칙 문서는 아직 고치지 않는다(세션 기록 수준으로만 반영). **(2026-07-15 갱신)** 이후 실제로 이 문서와 `.claude/agents/design-systems.md`/`.claude/agents/graphic-designer.md`를 design-pl이 직접 수정하는 라운드가 발생했다(2-6번 선제적 기본 구성 규칙 신설, 아래 30차 참고) — 순수 프로세스/에이전트 정의 문서 편집은 design-pl이 직접 Read 후 Write로 처리해도 된다는 실무 선례가 생겼다.

**도구 제약 메모**: design-pl에게는 백그라운드 실행 중인 하위 에이전트에게 메시지를 이어붙이는 SendMessage 도구가 실제로는 제공되지 않는다 — 진행 중인 에이전트에 추가 지시가 필요하면 완료를 기다렸다가 새 Agent 호출로 후속 지시를 보낸다.

**승인 판단 기준(이번 세션에서 확립된 실무 기준)**: "[메인 세션 확인] 사용자가 실제로 승인함" 형식이 아닌 코디네이터 메시지는 곧바로 실행하지 않고 계획/보고에만 포함한다 — 단, 이미 승인받아 진행 중인 작업의 완성도 버그 수정은 예외로 즉시 반영한다.

**사용자가 Figma에서 직접 처리한 항목은 팀이 재작업하지 않는다**: 사용자가 시간이 없어 특정 값(예: 텍스트 콘텐츠)을 직접 Figma에서 바꾼 경우, 그 항목은 "이미 완료된 상태"로 간주하고 design-systems가 다시 만들지 않는다 — 다음 design-qa 스팟체크 때 반영 여부만 가볍게 확인한다(별도로 재작업하지 않음).

**문서 손상 재발 방지(2026-07-15 재확인)**: `docs/design/design-system.md`처럼 긴 누적 문서에 새 절을 추가할 때는 Write로 통째로 덮어쓰지 말고, 반드시 먼저 전체를 Read한 뒤 그 내용 뒤에 새 절을 붙인 전체 버전을 쓰거나 Edit로 append하라고 워커에게 매번 명시한다 — 과거 Write 오사용으로 586줄→61줄 손상 사고가 있었다.

**구체적 지시는 design-prompter를 생략해도 되는 사례(2026-07-15)**: 노드ID·수정 전/후 값·범위 제한이 이미 100% 명시된 값/바인딩 교정(구조 변경 없음)은 design-prompter를 거치지 않고 design-systems를 바로 호출해도 된다 — 새로운 창작 판단이 없기 때문. **단, "컴포넌트 구조(variant 축) 변경"은 지시가 아무리 구체적이어도 이 예외에서 제외한다(2026-07-15 재확인)** — 삭제/유지 대상까지 사용자가 다 정해줬어도 variant property 재편은 design-prompter를 거쳐 실행 브리프로 구조화한다.

**서브에이전트 출력 토큰 한도 초과 대응(2026-07-15 신규)**: design-systems처럼 Figma 조회/조작 스텝이 많은 워커는 "출력 토큰 한도 초과"로 응답이 도중에 끊기는 사고가 반복됐다(같은 라운드에서 3회 발생). 이럴 때: (1) 먼저 관련 문서(`docs/design/design-system.md` 등)를 다시 읽어 실제로 어디까지 반영됐는지 확인한다(Write는 대개 끝까지 못 갔지만 Figma 쪽 `use_figma` 조작은 이미 끝났을 수 있음). (2) 재호출할 때 "먼저 기존 산출물이 이미 있는지 확인하고, 있으면 이어받고 없으면 처음부터 진행"하도록 명시한다. (3) 문서화 단계는 장황한 서술 대신 표/불릿 위주로 간결하게 쓰도록 지시해서 재발을 줄인다. **도구 간 판정 불일치도 함께 발견됨**: `get_design_context`(코드 변환/className 기반)로 opacity(paint alpha)를 검증하면 실제로는 정상인데도 "누락"으로 오탐하는 사례가 있었다(바인딩된 변수 fill의 paint opacity가 codegen 출력에서 클래스로 노출되지 않는 것으로 추정) — opacity/paint alpha류 검증은 `get_screenshot` 시각 비교나 `use_figma` raw script(`node.fills[0].opacity` 직접 조회)를 우선하고, className 파생값은 참고용으로만 쓴다(design-qa에게도 이 교훈 전달 완료).

## 작업 로그

### 2026-07-15 실행 라운드 — TypeSelector/NeoInput/CornerInput/Sidebar Nav Item Focus 구조 단순화 (29차)
- 배경: 버튼류 5개(NeoBtn/Button/Icon Button/Row Action Button/Table Row Action)는 이미 Focus를 State 열거형 값 하나로 취급(직교 축 없음). 반면 이 4개는 9-3절에서 `Focus=No/Yes` 별도 직교 축으로 설계돼 조합 variant가 늘어나 있었음. 사용자가 "주목적이 Focus가 아니다"라며 버튼류 패턴대로 단순화 요청, 조합 소실(정보 손실)은 명시적으로 감수하기로 확인.
- **"[메인 세션 확인] 사용자가 실제로 승인함" 형식 승인 받음** — 삭제/유지 대상·이름 규칙까지 전부 구체적으로 지정된 지시였으나, "컴포넌트 구조(variant 축) 변경"이라 판단해 design-prompter를 거쳐 실행 브리프로 구조화한 뒤 design-systems 호출(신규 정책 메모 참고).
- **design-systems 실행 결과**: TypeSelector 16→12(Selected+Focus=Yes 4개 삭제, Unselected+Focus=Yes 4개는 이름만 State=Focus로 정리). NeoInput/CornerInput 각 7→5(Filled×Focus=Yes 2개씩 삭제, Placeholder×Error=No×Focus=Yes 1개는 State=Focus로 유지). Sidebar Nav Item 4→3(Active+Focus=Yes 1개 삭제, Inactive+Focus=Yes=`287:17`의 9-5절 3px ink OUTSIDE 스트로크 특수 렌더링은 무수정으로 이름만 State=Focus 정리). 총 삭제 9개 variant, 유지 25개는 시각 무수정. 삭제 후보 9개는 전부 Component Specs 스펙 시트 그리드에서만 참조되고 있어(다른 화면/확정 프레임 참조 0건) 스펙 시트 재구성 시 구 그리드를 먼저 제거해 인스턴스 0건을 만든 뒤 마스터 삭제(design-pl 보고 대기 없이 처리, 스펙 시트 자체가 갱신 대상이었으므로). 스펙 시트 4개 재구성 중 auto-layout Cell `clipsContent=true`가 Focus 링을 잘라내는 버그 발견해 정정. design-system.md 0-15절 신설, 5절 표 갱신, 9-3절은 삭제 않고 "과거 기록" 라벨로 보존.
- **design-qa 스팟체크**: 5개 항목 PASS(variant 개수·이름·`287:17` 특수 스트로크 보존·스펙 시트·문서). MEDIUM 1건(CornerInput 개별 노드 `398:892` description이 리네임 이전 문구 잔존 — ComponentSet 레벨은 정상), LOW 1건(0-9절 과거 리스크 기록이 TypeSelector 인스턴스 존재를 놓쳤음 — 오늘 작업과 무관, 참고 전달만). 확정 프레임 `main-수정`(`248:8103`) 내 TypeSelector 인스턴스 4개는 전부 보존된 variant 참조, 깨진 인스턴스 없음 확인.
- **MEDIUM 즉시 반영**: 이미 승인된 작업의 완성도 버그로 판단해 design-systems 재호출, `398:892` description을 ComponentSet 레벨 문구와 일치하도록 정정(구조/시각 변경 없음).
- 상태: 완료. LOW 1건(0-9절 기록 부정확)은 사용자에게 참고 보고만 하고 별도 조치 없음.

### 2026-07-15 실행 라운드 — Checkbox 등록 + 선제적 기본 구성(2-6번) 규칙 신설 (30차)
- 배경: 사용자가 로그인 확정 프레임(`247:6666`)의 "☐ 로그인 상태 유지" 체크박스(`247:6822`)가 여러 커버리지 감사 라운드를 거치고도 정식 컴포넌트로 등록되지 않았다고 직접 지적("규칙만 쓰고 실행을 빠뜨린 상태"). 동시에 라디오 버튼 필요 여부 확인과, "확정 프레임에 없어도 이 프로젝트가 실제로 쓸 법한 기본 구성 요소(디바이더 등)를 미리 갖추는" 선제적 규칙 신설을 요청.
- **"[메인 세션 확인] 사용자가 실제로 승인함" 형식 승인 받음**.
- **하네스 갱신(design-pl 직접)**: `docs/harness/design-team/figma-file-organization.md`에 **2-6번(선제적 기본 구성)** 신설 — 기존 2-4번 "빠진 표준 폼 컨트롤"(반응형, 확정 프레임에서 발견됐을 때만)과 구분되는 상위 규칙으로, 확정 프레임에 안 보여도 이미 확정된 토큰·패턴만으로 이 프로젝트가 실제로 쓸 법한 기본 구성 요소를 design-systems/graphic-designer가 먼저 갖춘다는 내용. `.claude/agents/design-systems.md`(판단 기준에 2-6번 항목 추가, 할 일에 커버리지 점검 항목 추가, 하지 말 것에 "단순 벡터 프리미티브는 직접 만들어도 됨" 예외 추가)와 `.claude/agents/graphic-designer.md`(커스텀 그래픽 협업 흐름 추가)에도 반영.
- **design-prompter 브리프 → design-systems + ux-designer 병렬 호출**(2-4번 규칙대로 ux-designer 병행, Figma 쓰기는 design-systems만이라 충돌 없음).
- **design-systems 실행 결과**(2회 출력 토큰 한도 초과 후 재시도로 완료): Checkbox 컴포넌트(`474:899`, 신규 페이지 `474:881`) State=Default/Checked/Focus/Disabled 4 variant 등록, 라벨은 TEXT 프로퍼티(`label`, 기본값 "로그인 상태 유지"), 원본(`247:6822`/`247:6825`)과 hex/opacity/바인딩 단위 일치. 신규 토큰 0개(기존 `color/gray/0`/`color/ink/900` 재사용). 스펙 시트 `475:762` 신설. **라디오**: 확정 8프레임 ELLIPSE 32건 전수 스캔 결과 라디오 패턴 0건 + SCR-002가 Select/TypeSelector로 이미 커버 → 미등록 판단(근거 기록). **디바이더**: Contact Row가 이미 자체 구분선 보유 + 확정 프레임에 독립 divider 도형 0건 → 미등록 판단(근거 기록). CornerInput 스펙 시트(`344:740`) 라벨은 이미 정상이라 수정 불필요. `docs/design/design-system.md` 0-17절/14절 append(문서 손상 없음, 헤더·기존 절 보존 확인).
- **ux-designer 병행 검토 결과**: "로그인 상태 유지" 체크박스가 01/02/04 기획 문서 어디에도 대응 기능 요구사항(세션 지속 로직)이 없음을 확인·보고(삭제/추가 판단은 하지 않음, 발견 사실만). 8개 확정 프레임 재스캔에서 신규 불일치 3건 발견: (1) main-검색없음 헤더가 "검색결과 총 6건" 고정 표시(실제 0건과 불일치), (2) "전체" 카테고리(비검색) 상태에서도 헤더가 "검색결과" 접두어 유지(02문서는 "총 N건"만 정의), (3) main-삭제 모달이 커스텀 모달인데 02문서 SCR-002는 여전히 native confirm()으로 서술 — 처리 여부는 사용자 확인 필요, 이번 라운드에서 조치하지 않음.
- **design-qa 감사 — 우여곡절 있었으나 최종 PASS**: 1차 감사에서 HIGH 2건(Label 3개 variant + Disabled Box의 paint opacity 0.5 누락) 지적 → design-systems 재호출(2회 토큰 한도 초과 후 재시도) → design-systems가 raw script로 "이미 0.5 정상"이라 반박 → design-qa 재검증도 여전히 FAIL(코드 변환 결과 기반) → **스크린샷 순수 시각 비교로 최종 판정**한 결과 실제로는 opacity 정상 반영돼 있었음이 확인돼 PASS로 철회. 원인은 `get_design_context`(className 기반 코드 변환)가 바인딩된 변수 fill의 paint opacity를 codegen 출력에 반영하지 않는 도구 한계로 추정(위 정책 메모에 교훈 기록).
- 상태: 완료. ux-designer가 발견한 신규 불일치 3건은 사용자 확인 필요 항목으로 메인 세션에 보고, 이번 라운드에서 조치하지 않음.

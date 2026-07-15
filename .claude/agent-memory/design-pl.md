# design-pl 메모리

이 파일은 design-pl이 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 팀 로스터 (참고용)
- design-prompter, design-scanner, brand-designer, graphic-designer, design-systems, ux-designer, ui-designer, interaction-designer, motion-designer, content-designer, design-qa

## 정책 메모 (세션 기록 수준 — 하네스 문서는 아직 미수정)

**2026-07-14, 레거시 정리 작업 경계 변경**: 사용자가 "레거시 및 사용안해서 컴포넌트 기능 끊어놓은 것 내가 직접 지울게, 지금 너무 헷갈려서"라고 밝힘. 이후:
- 레거시/미사용 컴포넌트를 실제로 해제(COMPONENT/COMPONENT_SET→FRAME 전환)하거나 삭제하는 **적극적 정리 작업은 팀이 먼저 나서서 하지 않는다** — 사용자가 Figma에서 직접 처리하기로 함.
- `[Legacy ...]`/`❌ 미채택 —`/`❌ 폐기 —` 같은 **이름 라벨링(구분 목적)은 계속 유지**.
- `docs/harness/design-team/figma-file-organization.md` 등 하네스 규칙 문서는 아직 고치지 않는다(세션 기록 수준으로만 반영).

**도구 제약 메모**: design-pl에게는 백그라운드 실행 중인 하위 에이전트에게 메시지를 이어붙이는 SendMessage 도구가 실제로는 제공되지 않는다 — 진행 중인 에이전트에 추가 지시가 필요하면 완료를 기다렸다가 새 Agent 호출로 후속 지시를 보낸다.

**승인 판단 기준(이번 세션에서 확립된 실무 기준)**: "[메인 세션 확인] 사용자가 실제로 승인함" 형식이 아닌 코디네이터 메시지는 곧바로 실행하지 않고 계획/보고에만 포함한다 — 단, 이미 승인받아 진행 중인 작업의 완성도 버그 수정은 예외로 즉시 반영한다.

**사용자가 Figma에서 직접 처리한 항목은 팀이 재작업하지 않는다**: 사용자가 시간이 없어 특정 값(예: 텍스트 콘텐츠)을 직접 Figma에서 바꾼 경우, 그 항목은 "이미 완료된 상태"로 간주하고 design-systems가 다시 만들지 않는다 — 다음 design-qa 스팟체크 때 반영 여부만 가볍게 확인한다(별도로 재작업하지 않음).

## 작업 로그

### 2026-07-14 실행 라운드 — NeoInput/CornerInput Error 상태 + NeoSelect Open 상태 신설 (26차)
- 배경: 사용자가 레거시 `[Legacy B-2] Input/Error/Default`(`314:881`)/`[Legacy B-2] Select/Open`(`314:896`)을 직접 확인 — 정식 NeoInput(`288:12`)/CornerInput(`288:27`)엔 Error, NeoSelect(`261:660`)엔 Open 상태가 빠져 있었음.
- **design-systems 실행 결과**: A(Error) 신규 semantic `color/border-error`(→coral/500)/`color/text-error`(→coral/900), Error를 Focus와 독립 축으로 설계, 각 2→4 variant, WCAG 3.01:1/7.70:1 통과. B(Open) `261:660`→ComponentSet `387:13`, State=Default(원ID)/Open(`387:12`, 옵션 3개 텍스트 프로퍼티), elevation `Elevation/Raised` 적용. 스펙 시트 3개 갱신, design-system.md 0-10절 신설.
- **design-qa 검증**: 7/8 PASS. MEDIUM 1건: legacy 참고 노드 조회 불가(사전 드리프트 추정, 별도 후속 라운드 승인 대기).
- 상태: 실행+검증 완료.

### 2026-07-14 계획→실행 라운드 — NeoInput/CornerInput/NeoSelect Placeholder 상태 신설 + 부수 항목들 (27차, 진행 중, 최신)
- 배경: 사용자가 "인풋과 셀렉인풋창은 Default, 에러화면, 플레이스홀더 화면, 포커스로 만들잖아?" — 26차에서 빠졌던 **Placeholder** 상태 지적.
- **구체 계획**: NeoInput/CornerInput에 독립 축 `Content=Placeholder/Filled` 추가, 실사용 매트릭스로 7variant(Placeholder×Error=Yes×Focus=Yes만 제외)/컴포넌트. NeoSelect에 `Content=Placeholder/Selected` 추가, 4variant. 신규 원시값 없음(기존 뮤트/ink 토큰 재사용).
- **"[메인 세션 확인] 사용자가 실제로 승인함" 형식 승인 받음**, 사용자 3가지 조정 확정: (1) Focus×Error×Placeholder 3중 조합 제외, (2) NeoSelect Open 옵션에 hover 필수(9절 기존 블렌드 공식 재사용), (3) NeoSelect Placeholder 문구 "종류선택" 직접 확정.
- design-prompter가 브리프 완성(0단계 선행확인 포함, hover는 신규+기존 Selected×Open 둘 다 적용) → **design-systems 실행 중(백그라운드, 완료 대기)**.
- **진행 중 추가/변경 지시 — 최신 상태**:
  - (a) **버그 수정, 같은 승인 범위(즉시 반영 예정)**: NeoSelect Open 옵션 hover 배경이 패널 좌우 끝까지 안 채워지고 인셋됨 — design-systems 완료 알림 받는 대로 후속 Agent 호출로 즉시 수정.
  - (b) **신규 작업, 별도 승인 필요(미실행)**: `Pixel/Eye`(`281:405`) 짝(눈 감음/슬래시) 아이콘 없음. `figma-file-organization.md` 2-2절에 "토글/짝 상태 아이콘은 세트로 완성" 일반 규칙 반영됨. 계획: graphic-designer(짝 아이콘 크래프트) → design-systems(Icons 등록) → design-qa(세트 일관성).
  - (c) **취소됨**: `Link`(`341:3`) 기본 텍스트 "비밀번호 찾기"→"비밀번호 재설정" 변경 작업은 사용자가 시간이 없어 Figma에서 직접 처리 완료 — design-systems가 다시 건드리지 않는다. **다음 design-qa 스팟체크 때 Component Specs Link 스펙 시트(`344:759`)에 최신 텍스트가 반영돼 있는지만 가볍게 확인**(재작업 아님, 확인만).
- 상태: Placeholder 본작업(+hover 버그 수정 포함) design-systems 실행 중. (b) 별도 승인 대기, (c) 취소·완료 처리.

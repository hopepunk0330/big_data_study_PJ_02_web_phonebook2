# design-pl 메모리

이 파일은 design-pl이 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 팀 로스터 (참고용)
- design-prompter, design-scanner, brand-designer, graphic-designer, design-systems, ux-designer, ui-designer, interaction-designer, motion-designer, content-designer, design-qa

## 정책 메모 (세션 기록 수준 — 하네스 문서는 아직 미수정)

**2026-07-14, 레거시 정리 작업 경계 변경**: 사용자가 "레거시 및 사용안해서 컴포넌트 기능 끊어놓은 것 내가 직접 지울게, 지금 너무 헷갈려서"라고 밝힘. 이후:
- 레거시/미사용 컴포넌트를 실제로 해제(COMPONENT/COMPONENT_SET→FRAME 전환)하거나 삭제하는 **적극적 정리 작업은 팀이 먼저 나서서 하지 않는다** — 사용자가 Figma에서 직접 처리하기로 함. 이후 사용자가 명시적으로 "팀이 직접 처리하라"고 지시하면 이 유보는 해제되고 표준 절차(2-4번, 분리 후 전환)를 그대로 따라 처리한다.
- `[Legacy ...]`/`❌ 미채택 —`/`❌ 폐기 —` 같은 **이름 라벨링(구분 목적)은 계속 유지**.
- `docs/harness/design-team/figma-file-organization.md` 등 하네스 규칙 문서는 순수 프로세스/에이전트 정의 문서 편집이면 design-pl이 직접 Read 후 Write로 처리해도 된다. **이 원칙은 `.claude/agents/*.md`(에이전트 정의)와 `docs/harness/reset-checklist.md` 같은 절차 문서 전체에 동일하게 적용된다** — design-pl에게는 Edit 도구가 없어 항상 전체 Read 후 Write(전체 재작성)로 처리하되, 기존 내용을 빠짐없이 보존하고 필요한 부분만 삽입/수정한다. **단 `docs/design/design-system.md`처럼 "Edit-only, Write 금지"가 명시적으로 요구되는 문서는 design-pl이 손대지 않고 소유 에이전트(design-systems)에게 위임한다.**

**도구 제약 메모**: design-pl에게는 백그라운드 실행 중인 하위 에이전트에게 메시지를 이어붙이는 SendMessage 도구가 실제로는 제공되지 않는다 — 완료를 기다렸다가 새 Agent 호출로 후속 지시를 보낸다. design-pl 자체 도구셋에는 Edit이 없다(Read/Glob/Agent/Write/Skill만). 백그라운드 호출은 완료 통지 없이 조용히 무반영될 수 있어 실제 반영 여부를 재확인해야 한다(65차) — 이후 후속 위임 작업은 포그라운드로 호출한다(66~69차). design-pl/content-designer 둘 다 Bash가 없어 실제 파일 업로드(curl POST)를 못한다 — "필요한 nodeId·파일 매핑 조사→메인 세션이 Bash로 업로드 실행→배치 확인 후 다음 단계"의 2단계 핸드오프로 처리한다(68차 확인). Figma를 쓰는 워커(content-designer, graphic-designer)와 Figma를 안 쓰는 워커(ai-image-prompt-writer)는 서로 독립적인 작업이면 한 메시지에 병렬로 호출해도 된다 — "Figma 쓰는 에이전트는 동시에 하나만" 제약은 Figma를 실제로 쓰는 에이전트끼리에만 적용된다(68차 확인). **단, graphic-designer(오브제 원화)→content-designer(배치)처럼 한쪽 산출물이 다른쪽 입력이 되는 경우는 반드시 순차 호출**(68차 재확인). **69차 재확인**: design-prompter(브리프 작성, Figma 미사용)와 content-designer(조사·정리 작업, Figma 사용) 조합도 서로 독립적이면 한 메시지에 병렬 호출 가능함을 재확인. **70차 신규**: design-prompter를 `subagent_type: "fork"`로 잘못 부르면 Figma MCP 도구가 전혀 배정되지 않는다(fork는 design-pl 자신의 도구셋을 상속하므로 Figma 도구 없음) — Figma 조사가 필요한 작업은 반드시 `subagent_type: "design-scanner"`(또는 해당 워커) 그대로 불러야 한다. 또한 **design-prompter가 "브리프를 위(자신의 이전 응답)에 출력했다"고 요약만 반환하고 실제 본문이 design-pl에게 전달 안 되는 사례가 반복됨** — design-prompter 호출 시 "최종 응답 메시지 자체에 브리프 본문 전체를 그대로 써라, 참조만 하지 마라"를 명시적으로 요구해야 실제 본문을 받을 수 있었다(2회 연속 요약만 반환 후 3번째 명시적 재요청에서 성공). **72차 재확인·강화**: 같은 실패가 또 반복됨(design-prompter가 "위 응답에 전문 포함"이라고만 답함) — 이때 design-pl 자신을 `fork`로 재호출해 "이전 서브에이전트의 출력을 복원해달라"고 시도했으나, **fork는 다른 서브에이전트(design-prompter)의 트랜스크립트에 접근할 방법이 없어 실패한다**(fork는 상위 design-pl의 대화 맥락만 상속받을 뿐, design-prompter가 실제로 만든 출력 그 자체는 design-prompter 자신의 트랜스크립트에만 있음) — 복구 방법은 fork가 아니라 **design-prompter를 처음부터 다시 호출**하되, 지시문 맨 앞과 맨 끝 두 곳에 "본문 전체를 출력해라, 요약 금지, 이 응답=산출물"을 강조 배치하는 것뿐이다. 이번엔 이 방식으로 3번째 시도에서 성공.

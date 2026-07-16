# design-pl 메모리

이 파일은 design-pl이 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 팀 로스터 (참고용)
- design-prompter, design-scanner, brand-designer, graphic-designer, design-systems, ux-designer, ui-designer, interaction-designer, motion-designer, content-designer, design-qa

## 정책 메모 (세션 기록 수준 — 하네스 문서는 아직 미수정)

**2026-07-14, 레거시 정리 작업 경계 변경**: 사용자가 "레거시 및 사용안해서 컴포넌트 기능 끊어놓은 것 내가 직접 지울게, 지금 너무 헷갈려서"라고 밝힘. 이후:
- 레거시/미사용 컴포넌트를 실제로 해제(COMPONENT/COMPONENT_SET→FRAME 전환)하거나 삭제하는 **적극적 정리 작업은 팀이 먼저 나서서 하지 않는다** — 사용자가 Figma에서 직접 처리하기로 함. 이후 사용자가 명시적으로 "팀이 직접 처리하라"고 지시하면 이 유보는 해제되고 표준 절차(2-4번, 분리 후 전환)를 그대로 따라 처리한다.
- `[Legacy ...]`/`❌ 미채택 —`/`❌ 폐기 —` 같은 **이름 라벨링(구분 목적)은 계속 유지**.
- `docs/harness/design-team/figma-file-organization.md` 등 하네스 규칙 문서는 순수 프로세스/에이전트 정의 문서 편집이면 design-pl이 직접 Read 후 Write로 처리해도 된다.

**도구 제약 메모**: design-pl에게는 백그라운드 실행 중인 하위 에이전트에게 메시지를 이어붙이는 SendMessage 도구가 실제로는 제공되지 않는다 — 완료를 기다렸다가 새 Agent 호출로 후속 지시를 보낸다. design-pl 자체 도구셋에는 Edit이 없다(Read/Glob/Agent/Write/Skill만) — `docs/design/design-system.md`처럼 "Edit-only, Write 금지"가 명시적으로 요구되는 문서는 design-pl이 직접 손대지 않고 Edit 도구를 가진 소유 에이전트(design-systems)에게 위임한다.

**승인 판단 기준(확립된 실무 기준)**: "[메인 세션 확인] 사용자가 실제로 승인함" 형식이 아닌 코디네이터 메시지는 곧바로 실행하지 않고 계획/보고에만 포함한다 — 단, 이미 승인받아 진행 중인 작업의 완성도 버그 수정/중간 정정 지시는 즉시 반영 대상이다. **"실제 변경(해제/전환/라벨링) 실행" 자체가 별도 게이트로 요청된 작업(예: "조사→보고→확인→실행" 4단계 요청)은 조사·보고까지만 먼저 하고, 실행은 신뢰 형식의 별도 승인이 온 뒤에만 진행한다.** 이 세션에서 "신뢰 형식 승인 → 실행 → 그 실행 도중 또 다른 신뢰 형식 승인이 도착해 별개 작업 추가 처리"가 여러 차례 반복됐다(37차 조사→38차 라벨링+Amber/Teal 정정→39차 Ink 추가→40차 harness-auditor 발견분 3건 정정) — 매번 이전 작업과 무관한 새 작업인지 확인하고, 형식이 맞으면 지체 없이 실행하되 작업 간 경계(무엇을 건드리고 무엇은 건드리지 않는지)를 브리프에 명확히 구분해 섞이지 않게 하는 패턴이 안정적으로 작동했다.

**서브에이전트 출력 토큰 한도 초과 대응**: design-systems처럼 Figma 조회/조작 스텝이 많은 워커는 "출력 토큰 한도 초과"로 응답이 도중에 끊기는 사고가 반복됐다. 대응: (1) 관련 문서를 다시 읽어 실제 반영 범위 확인. (2) 재호출 시 "재개 확인" 명시. (3) 문서화는 표/불릿 위주로 간결하게. design-scanner(haiku)는 `get_metadata`로 대형 페이지(파일럿·Component Specs처럼 자식이 많은 페이지)를 통째로 조회하면 토큰 초과로 실패한다 — 이런 페이지는 design-systems가 raw script(`use_figma`)로 "1단계 자식만" 순회하는 방식(재귀 없이 `id`/`name`/`type`만 출력)으로 우회해야 한다. design-scanner는 표면 조사에는 적합하지만, 변수 `boundVariableId` 참조 카운트나 alias 체인처럼 깊은 스크립트 순회가 필요한 조사는 애초에 도구셋에 `use_figma`가 없어 불가능 — 이런 조사는 design-systems를 "읽기 전용 조사 콜"(mutation 없음을 스스로 확인·보고하도록 명시)로 호출해 보완한다.

**변수 미사용 판정은 "직접 참조 0회"만으로 끝내면 오탐이 난다**: Primitive 계층은 Semantic이 alias로 가리키기만 해도 "간접 사용 중"이라 직접 참조 0회여도 진짜 미사용이 아닐 수 있다. **변수 미사용 감사는 반드시 두 단계(①노드 직접 바인딩 재귀 스캔 ②전체 변수의 `valuesByMode`에서 VARIABLE_ALIAS 체인 확인)를 다 거쳐야 신뢰할 수 있다.**

**"문서(design-system.md) 기록"과 "실제 확정 프레임 실측"이 어긋날 수 있다 — 구조가 비슷한 컴포넌트로 착오 전파 위험**: design-system.md에 "NeoBtn Amber를 리바인딩했다"고 기록돼 있었으나, 실제로는 별도 컴포넌트 Button(`259:609`)에 대한 정당한 작업이 이름·구조가 비슷한 NeoBtn에도 잘못 전파되어 기록된 것으로 드러났다. "다른 컴포넌트와 구조가 비슷하다"는 이유로 작업을 동일 적용할 때는 항상 대상 컴포넌트 이름으로 정확히 재확인하고, 문서 기록을 실측 없이 그대로 신뢰하지 않는다. 특정 Style variant 일부만(전체 ComponentSet이 아니라) 해제/추가하는 절차도 기존 "COMPONENT_SET 전체 FRAME 전환" 절차와 동일 패턴으로 개별 variant 단위에 그대로 일반화됨을 확인.

**ComponentSet의 TEXT 컴포넌트 속성(예: NeoBtn `Label`)은 Style 전체가 공유하는 단일 값일 수 있다(39차 신규 발견)**: 새 Style variant를 추가하며 그 Style 전용 기본 라벨("로그아웃" 등)을 넣으려고 마스터 컴포넌트 속성을 바꿨더니, 같은 ComponentSet의 **다른 모든 Style의 기본 텍스트까지 한꺼번에 바뀌는** 사고 직전 상황이 있었다(design-systems가 스크린샷으로 즉시 발견해 원래 공유 기본값 "검색"으로 되돌리고 전체 Style 무손상 재확인함, 재작업 없이 같은 콜에서 자체 교정). **교훈: ComponentSet에 새 Style을 추가할 때 텍스트/기타 컴포넌트 속성을 그 Style 전용으로 착각해 편집하지 말고, 먼저 그 속성이 ComponentSet 전체 공유인지 variant별 개별인지 확인한 뒤 손댄다.** 앞으로 유사 브리프에 이 확인 절차를 기본 포함.

**대규모 소스 교체(재추출) 라운드는 Stage 분리가 유효했다**: Stage를 작게 쪼개고 각 Stage 호출마다 "재개 확인" 지침을 넣는 관행이 유효함이 반복 확인됨.

**"컴포넌트로 보이는 노드가 실제로는 INSTANCE가 아니라 raw FRAME"인 구조적 문제**: 확정 디자인 섹션의 8개 프레임에서 컴포넌트와 동명인 노드 대다수가 raw FRAME/TEXT/VECTOR였다. 유사 검증/실측 작업을 지시할 때는 INSTANCE 여부를 먼저 type으로 확인하는 절차를 기본 포함한다.

**레거시 컴포넌트가 "키드(published key)"라 물리적 삭제가 원천적으로 불가능할 수 있다**: detach 이후 완전히 `remove()`하려 해도, 라이브러리에 퍼블리시된 적 있는 key를 가진 컴포넌트는 Figma가 key 레지스트리 무결성을 위해 물리적 삭제를 막고 `parent: null` 고아 상태로 되돌린다. 대안: 새 컨테이너(`❌ 폐기 —` 라벨)를 만들어 시각적으로 동일한 FRAME 사본을 그 안에 넣어 Assets 패널 노출을 제거.

**❌ 미채택/❌ 폐기 라벨 산출물은 무엇이든(화면·컴포넌트·토큰) 예외 없이 삭제 금지 — 2026-07-16 오삭제 사고로 재확정**: "컴포넌트를 포함하지 않는 화면은 삭제해도 된다"는 자체 판단으로 파일럿 페이지의 옛 폐기 화면 9개를 완전 삭제해 영구 유실된 사고가 있었다(Cmd+Z 복구 실패). 이후 "필요 없어진 컴포넌트"에 대한 유일한 정당 처리는 컴포넌트 해제(detach→FRAME 전환)뿐이고, 삭제가 필요해 보이면 반드시 메인 세션에 먼저 보고한다. 이 사고 이후 민감한 정리 작업은 "조사 → 보고 → 확인 → 실행" 게이트를 기본 적용한다.

**하네스 규칙 13번(harness-auditor 호출) — B 범위(`docs/design/**`) 누락 정정 확립**: 처음 이 규칙을 만들 때 A 범위(`.claude/agents/**`, `docs/harness/**`)만 넣고 design-pl/design-systems가 가장 자주 건드리는 B 범위(`docs/design/**`, 특히 `design-system.md`)를 빠뜨린 사고가 있었다(2026-07-16, 발견 즉시 정정). 지금은 A 또는 B 어느 쪽을 건드려도 라운드 종료 전 harness-auditor를 호출하는 것으로 확정.

## 작업 로그

### 2026-07-16 실행 라운드 — NeoBtn Style=Ink 신규 추가 (39차)
- 배경: 38차의 "로그아웃 버튼 덤 발견"을 메인 세션이 직접 재조사 — 확정 디자인 main 계열 5개 프레임 전부에서 로그아웃 NeoBtn이 기존 Neutral(흰배경+ink보더)과 배경/보더/텍스트가 전부 반전된 별개 스타일(검정 배경 `#1a1a1a`+무보더+흰 텍스트, Compact 79×25, radius8)임을 확인, AskUserQuestion으로 "Style=Ink 신규 추가" 승인받음.
- design-systems에 직접 실행 지시(설계 판단 필요 없이 13절 Sky/Navy 추가 절차를 그대로 재사용하는 기계적 작업이라 design-prompter 생략). Size=Compact만, State 6개(Default/Hover/Press/Focus/Disabled/Loading) 한 번에 완성 — TODO 이월 없음.
- 진행 중 두 가지 이슈를 design-systems가 자체 발견·해결: (1) 9-1절 Hover/Press 공식("ink 방향 블렌드")이 배경 자체가 이미 ink라 무의미해 흰색 방향 블렌드로 대체(문서화된 판단), (2) ComponentSet의 `Label` 텍스트 속성이 Style 전체 공유값이라 편집 시 다른 Style 기본 텍스트까지 바뀔 뻔한 걸 스크린샷으로 즉시 발견해 원복(위 정책 메모 참고).
- 결과: NeoBtn variant 36→42(Style 옵션: Coral/Neutral/Sky/Navy/Ink). WCAG 전부 PASS(Disabled 3.88:1은 기존 프로젝트 표준과 동일). 스펙 시트(`342:3`)에 Ink/Compact 행 추가, `docs/design/design-system.md` 18절 신규 기록.
- 상태: 완료. 확정 디자인 8개 프레임은 이번 라운드에서 열람도 하지 않음(메인 세션이 이미 실측값을 넘겨줘서 재열람 불필요).

### 2026-07-16 harness-auditor 첫 B범위 감사 — design-system.md 내부 정합성 3건 발견·보고 (턴 종료)
- 배경: 13번 규칙에 B 범위(`docs/design/**`)가 누락돼 있던 걸 발견 즉시 정정(위 정책 메모 참고). 정정 직후 첫 B 범위 감사를 harness-auditor에게 요청.
- 발견 3건: (1) 9-1절 본문에 Focus 링의 FocusRing 자식 RECTANGLE 메커니즘 서술이 없는데 18/19절이 "9-1절 공식 그대로"라며 인용하는 앞뒤 불일치. (2) NeoBtn Amber/Teal이 0-25절에서 이미 해제됐는데 컴포넌트 표/보류 문단이 현재형으로 남아있는 stale 서술. (3) 8절 "활성 레거시 0개" 선언이 0-25절 이후 추가 해제분(24 variant)을 반영 못한 스코프 문제.
- 메인 세션이 1건(구 Style 언급)을 직접 grep으로 재확인해 실제 결함임을 확정 → 사용자 승인("응") → 신뢰 형식 승인으로 재개.

### 2026-07-16 실행 라운드 — harness-auditor 발견 3건 문서 정정 + 재검증 (40차)
- 전부 `docs/design/design-system.md` 텍스트 정정, Figma 조작 없음. 지시가 이미 구체적(줄 번호/원인/조치 방식 명시)이라 design-prompter 생략, design-systems에 직접 지시.
- design-systems 결과: (1) 9-1절 Focus 항목에 FocusRing 자식 RECTANGLE 메커니즘(offset -4.5, cornerRadius=버튼 radius+4.5, strokeWeight 3, `color/ink/900`) 정식 서술 추가, 7-2절 각주 원문 수치와 일치 확인. (2) 컴포넌트표/보류문단 2곳 + grep 재점검으로 추가 발견한 1-3절/3절 2곳, 총 4곳에 "0-25절 참고"/시점 각주 추가(원 기록은 삭제하지 않고 보존, 이 문서 관례 준수). (3) 8절 결론에 "이 절의 '0개' 선언은 14절까지 기준" 스코프 각주 추가(기존 "0개" 문구·숫자는 무변경).
- harness-auditor 재검증 결과: **3건 모두 해소, 새 불일치 없음**. 수치·컨테이너ID(`784:940`) 교차검증 일치, 목차/절 번호/앵커 손상 없음, 미각주 잔여 Amber/Teal 언급 없음(문서 전체 재grep 확인), variant 개수 산술(48→50→60→36→42)로 시간순 정합성까지 교차검증.
- 상태: 완료. Figma 노드는 이번 라운드에서 전혀 건드리지 않음.

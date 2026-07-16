# design-systems 메모리

이 파일은 design-systems의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **State Ledger(토큰/컴포넌트/아이콘의 현재 확정 상태) 자체는 여기 없습니다 — `docs/design/design-system.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-16 — Component Specs 스펙 시트 리셋 4/4(마지막) 배치 — NeoSelect/Checkbox + 페이지 겹침 재배치 + 문서 최종 정리 (순수 검증+동기화, 창작 판단 없음)
- **NeoSelect(`387:13`, 스펙 시트 `388:746`)**: 실제 4 variant(Content=Placeholder/Selected × State=Default/Open) vs 스펙 시트 4셀 — 일치, 셀 변경 없음. Open State 이중 그림자 방지 판단(13절 P4: 트리거는 그림자 없음, options-panel만 `Elevation/Raised`)이 그대로 유지돼 있음을 재확인(변경 없음). 내부 auto-layout 컨테이너 6개(HeaderRow/Spacer/LabelCell×4)가 `clipsContent=true`로 남아있던 것을 발견해 `false`로 정정. 설명 텍스트에 13절 P4(Shadow/Hard-2 적용 범위) 반영이 누락돼 있어 갱신.
- **Checkbox(`474:899`, 스펙 시트 `475:762`)**: 실제 4 variant(State=Default/Checked/Focus/Disabled) vs 스펙 시트 4셀 — 일치, 셀 변경 없음. 체크마크(`474:888`) stroke가 `color/ink/900`에 정상 바인딩돼 있음을 재확인(13절 P12에서 이미 정정 완료, 변경 없음). 스펙 시트 인스턴스 4개 중 3개가 `clipsContent=true`였던 것을 `false`로 정정. 설명 텍스트가 "체크마크 색은 후속 검토 필요"라는 stale 문구를 갖고 있어(이미 P12로 해소된 사안) 최신 상태(Disabled 색 토큰 공식 포함)로 갱신.
- **페이지 전체 겹침 재검사**: 13개 스펙 시트 루트 프레임 x/y/width/height 전수 재조회 결과 겹침 0건(이전 배치들이 이미 순서대로 40~189px 간격 유지). 다만 이번 배치에서 NeoSelect 설명 텍스트가 길어지며 루트가 `primaryAxisSizingMode: FIXED`(560 고정, auto-hug 아님)라 실제 콘텐츠가 선언된 높이를 39px 넘어서고 있던 것을 발견 — `AUTO`로 전환해 560→612로 정확히 hug시켰고, 그 결과 다음 시트(Checkbox)와 6px 겹치게 돼 Checkbox를 60px 아래로 재배치해 겹침 0건 유지.
- **문서 최종 정리**: `docs/design/design-system.md`에 0절 인트로(구 확정 디자인 섹션 `248:11689` 완전 삭제 사실 정정, 14-1절 참조) + 8절 Legacy 표 뒤 신규 문단(14-2/14-3절 발견 요약, 활성 레거시 컴포넌트 0개 결론) + 신규 15절(4배치 요약 표, NeoSelect/Checkbox 상세 결과, 페이지 겹침 재배치 결과) + 5절 NeoSelect/Checkbox 행에 15-2절 각주 추가. 전부 Edit로만 수정(Write 미사용), 최종 줄 수 1021→1064(도구 목록 지침 이후 Edit 전용 정책 준수, 손상 없음).
- **배치 2/3 로그 유실 관련 투명성**: `.claude/agent-memory/design-systems.md` 5개 캡 정책상 배치 2/3(Row Action Button/Table Row Action/Sidebar Nav Item/TypeSelector, NeoInput/CornerInput/Link/Contact Row)의 세부 로그가 이후 다른 라운드 로그에 밀려 사라져 있었다 — 이번 15절 작성 시 라이브 Figma 상태 재조회로 "현재 정합 상태"만 확인·기록했고, 당시 무엇을 구체적으로 고쳤는지는 재구성하지 않고 유실을 그대로 명시했다.

### 2026-07-16 — design-qa 감사 HIGH 1건/MEDIUM 1건 처리 — 순수 재검증/정리, 창작 판단 없음, design-prompter 생략
- **HIGH — Checkbox 체크마크(`474:888`) 색상 재확인**: design-qa가 스크린샷 3가지 크롭 판독만으로 "밝은/흰색 톤"이라고 다시 HIGH 보고했으나, `use_figma` raw script로 재조회한 결과 stroke `#1a1a1a`, `boundVariables.strokes[0]`이 `VariableID:95:9`(`color/ink/900`)를 정확히 가리키고 있었다 — 35차(13절 P12)에서 이미 정정·확인됐고 15-2절에서도 재확인된 값 그대로, 변경 없음. `node.screenshot({scale:20})` 고배율 inline 렌더로도 진한 검정 체크마크를 육안 확인 — 파란 배경(`color/sky/500`) 위 작은 아이콘의 동시대비 착시로 인한 재발 오탐으로 결론. State=Checked 마스터(`474:896`)의 다른 속성(strokes=[], children=[Box `474:886`, Label `474:887`])도 함께 재확인, 이상 없음.
- **MEDIUM — TempVerify 스크래치 정리**: Table Row 페이지(`103:3`)의 화면 밖(x=9000,y=5000) 프레임 `TempVerify`(`549:984`)와 그 안 COMPONENT 4개(NeoBtn variant와 이름이 완전히 동일한 "Style=Amber/Neutral, Size=Default, State=Default/Focus")를 삭제했다. 삭제 전 파일 전체(29개 페이지) INSTANCE 전수 검색으로 참조 0건 확인(Detach 불필요) → `frame.remove()`로 프레임+4개 컴포넌트 일괄 삭제 → `get_metadata`로 `103:3`에서 사라졌고 나머지 정식 컴포넌트(Row Action Button/Table Row Action/Contact Row)는 무손상임을 재확인.
- `docs/design/design-system.md`는 15절 끝에 "2026-07-16 추가 정리" 문단(HIGH 재확인 결과는 15-2절 Checkbox 서술 바로 뒤, MEDIUM 삭제 사실은 15절 맨 끝) 2곳 Edit로 추가. Write 미사용. `501:2505`(신규 확정 디자인)는 이번에도 무열람.

### 2026-07-16 — 미사용 변수 32개 + 텍스트 스타일 6개 `[미사용] ` 접두어 라벨링 (사용자 승인 실행 콜, 37차 조사 확정 목록 기반)
- 37차 조사에서 alias 체인까지 검증해 "진짜 미사용"으로 확정한 변수 32개(Component Tokens 11 / Spacing 5 / Semantic Colors 7 / Primitives 9)와 로컬 텍스트 스타일 6개를 정확한 ID로 지정해 이름 앞에 `[미사용] `만 추가(값/scopes/codeSyntax/description/바인딩 전부 무수정, 순수 rename).
- 텍스트 스타일은 지시서 ID(`S:...48`)가 트레일링 콤마 없는 형식이라 첫 시도 6건 전부 "not found"로 실패(atomic이라 파일 무변경) → `getLocalTextStylesAsync()`로 실제 ID 형식(`S:...48,`)을 확인해 재시도, 성공.
- FOUNDATIONS Colors(`95:2`)/Spacing(`95:4`) 페이지를 전수 텍스트 검색해 대응 스와치 캡션이 있는 변수만 골라 동일 라벨링(25건: primitive 7 name라인, semantic 4 name라인만, semantic 2+component token 4는 alias 대상도 32개 목록에 포함돼 name+alias 라인 둘 다, spacing 2). 부분 문자열 오검색(`row-action-button-border-neutral`, `text-link-navy` 등 이름은 겹치지만 다른 변수)은 정확히 식별해 제외. 캡션 없는 25개 변수는 그대로 둠.
- **검증**: Variables 패널은 캔버스 노드가 아니라 `get_screenshot` 불가 — raw script 재조회로 38개 전부 `[미사용] ` 접두어 확인(`varAllOk`/`styleAllOk` 둘 다 true). 캔버스 노드인 스와치 캡션 25건은 `get_screenshot`(inline base64)으로 시각 확인(예: `436:160` border-divider-warm 스와치 정상 렌더링).
- `docs/design/design-system.md` 신규 17절 Edit로 추가(배경/변경 내역/검증 결과 전부 기록). Write 미사용. `old-사용하지말것`(`242:2330`)·확정 디자인 8개 프레임(`501:2505`)은 전 과정 무열람.

### 2026-07-16 — NeoBtn Style=Amber/Teal 레거시 해제 — Stage2 오기록 정정 (메인 세션 확정 디자인 정밀 대조 후속)
- 메인 세션이 확정 디자인 8프레임(`501:2505`)을 직접 대조해 NeoBtn 실사용 색상이 ink/coral/navy/sky 4개뿐임을 확인 — 0-20절 "Stage2 NeoBtn Amber 리바인딩" 기록이 오류였고, 실제 Amber(#ffce2c) 사용처는 Button(`259:609`)뿐임이 드러남.
- 표준 절차 그대로 수행: ① NeoBtn(`259:126`) 60 variant 중 Style=Amber/Teal 24개 노드 ID 확정 → ② 파일 전체 29페이지 전수 검색, 24개를 참조하는 INSTANCE 24개 전부 `Component Specs`(`342:2`) 스펙 시트 셀 안에서만 발견(확정 8프레임 내부 0건, 정지 조건 미해당) → ③ 24개 detach(시각 보존) → 재검색 0건 확인 → ④ 24개 COMPONENT를 표준 절차(새 FRAME 생성+자식 이동+원본 remove)로 전환, Button 페이지에 `❌ 폐기 — NeoBtn Amber/Teal (확정 디자인 근거 없음, 2026-07-16 정정)`(`784:940`) 컨테이너로 이전 보존.
- 결과: NeoBtn 60→36 variant, Style 옵션 `["Coral","Neutral","Sky","Navy"]` 4개만 남음(재조회 확인). `Spec — NeoBtn`(`342:3`) 스펙 시트에서 Amber/Teal Row 4개 제거(2-5번 규칙), 설명 텍스트 갱신, `get_screenshot`으로 36칸 정상 렌더링 확인.
- Button(`259:609`)의 Amber는 전혀 건드리지 않음. 헤더 "로그아웃" NeoBtn ink 배경+amber 보더 이례값(0-20절 기존 기록)은 이번 범위 밖이라 재확인만 하고 무수정.
- `docs/design/design-system.md`에 신규 0-25절 Edit로 추가(정정 배경/4색상표/절차/결과/스펙시트 갱신), 5절 NeoBtn 행과 7-2절 TODO(Amber Hover/Press 블렌드 재계산 대상 Button으로 축소) 갱신. Write 미사용. 확정 디자인 8프레임은 이번에도 무열람(메인 세션이 이미 실측 완료).

### 2026-07-16 — NeoBtn Style=Ink 추가 — 헤더 "로그아웃" 버튼 별개 스타일 완성 (메인 세션 main 5프레임 재실측 후속, 사용자 승인 실행)
- 메인 세션이 main 계열 5개 확정 프레임(main/main-수정/main-삭제/main-검색없음/main-알림창)에서 헤더 "로그아웃" NeoBtn을 재실측한 결과 기존 4색과 다른 별개 스타일(ink #1a1a1a 배경, 무보더, 흰 텍스트, radius8, 79×25=Size Compact) 확인 → Style=Ink(Size=Compact 전용) 신규 추가, State 6개(Default/Hover/Press/Focus/Disabled/Loading) 이번에 전부 완성(TODO로 미룸 없음).
- 배경=`color/ink/900`, 텍스트=`color/text-inverse`, Disabled=`color/bg-disabled`+`color/text-disabled`, Focus=대응 상태 clone+FocusRing 자식(strokeWeight3/cornerRadius14.5)+2겹 DROP_SHADOW(9-1절 공식 그대로). **판단 필요했던 예외 1건**: Hover/Press 블렌드 공식("ink 쪽으로 블렌드")이 베이스가 이미 ink라 no-op이 되는 문제 발견 → 강도(12%/24%)는 유지하고 방향만 흰색 쪽으로 대체(다크 UI 상호작용 밝아짐 관례), raw unbound 값으로 저장(#353535/#515151), design-system.md 18절에 근거 문서화.
- **실측 중 발견한 함정**: NeoBtn의 TEXT 컴포넌트 프로퍼티(Label)가 Style별 독립값이 아니라 ComponentSet 전체가 공유하는 단일값임을 처음 확인 — Ink Default 텍스트를 "로그아웃"으로 직접 설정했더니 Coral/Neutral/Sky/Navy 마스터 표시 텍스트가 전부 동시에 "로그아웃"으로 바뀌는 부작용 발생, 즉시 발견해 "검색"으로 원복(전 Style 정상 복구 확인). 최종적으로 Ink도 마스터는 공유 기본값 "검색" 유지, 실사용 "로그아웃"은 화면 인스턴스 오버라이드로 처리(ui-designer 몫).
- WCAG 전 State 계산: Default/Focus/Loading 17.78:1, Hover 12.17:1, Press 7.94:1 — 전부 PASS. Disabled 3.88:1은 0-24절 기존 전사 공통값과 동일(신규 이슈 아님, 사용자 기승인 완화 결정 승계).
- 스펙 시트: `Spec — NeoBtn`(`342:3`)에 "Ink / Compact" Row(`792:801`, 6칸) 신규 추가(Neutral/Compact Row clone 후 instance.swapComponent), 설명 텍스트 갱신, clipsContent 전부 false 확인. `get_screenshot`으로 42칸 전체 잘림·겹침 없음 확인.
- 결과: NeoBtn(`259:126`) 36→42 variant, Style 옵션 5개(Coral/Neutral/Sky/Navy/Ink). `docs/design/design-system.md` 신규 18절 + 5절 NeoBtn 행 Edit로 갱신(Write 미사용). 확정 디자인 8개 프레임은 이번에도 무열람(메인 세션이 실측 완료해 전달).

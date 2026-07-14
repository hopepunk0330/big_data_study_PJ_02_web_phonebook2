# interaction-designer 메모리

이 파일은 interaction-designer가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 작업 로그

### 2026-07-14 — 인터랙티브 컴포넌트 hover/press/focus/disabled/loading 상태 정의 (fileKey `zgGlMBwFglaDlaeyP4CkgR`)
- 배경: 사용자 확정 8개 프레임(`248:11689` 하위)은 정적 스크린샷이라 상태가 없음. design-systems가 등록해둔 COMPONENTS 쪽 컴포넌트에 상태 variant를 신규 추가. 8개 확정 프레임은 이번에도 전혀 건드리지 않음(읽기 전용조차 하지 않음, 컴포넌트만 작업).
- 사전 확인: `docs/design/design-system.md`(§1~5 컴포넌트 목록), `docs/design/brand-guide.md`(하드 스티커 그림자/ink 보더/팔레트 톤), `.claude/agent-memory/ux-designer.md`(접근성 메모)를 먼저 읽고 톤 확장 방식으로 설계.
- **버튼류 5개 — State(Default/Hover/Press/Focus/Disabled/[Loading]) 축 신규 추가**:
  - NeoBtn(`259:126`, Style4×Size2=8→48), Button(`259:609`, Style3=3→18): Loading 포함(실제 제출 액션).
  - Icon Button(`259:613`, Type1=1→5), Row Action Button(`260:95`, Style2=2→10), Table Row Action(`260:100`, Style2=2→10): Loading 제외(모달을 여는 트리거일 뿐 자체 제출 없음).
  - 공통 규칙: Hover=ink로 배경 블렌드(브랜드색12%/흰배경6%)+그림자 유지, Press=블렌드 2배+그림자 완전 제거(effects=[]), Focus=기존 효과에 ink 포커스링(DROP_SHADOW offset0 blur0 spread3) 추가, Disabled=opacity 0.45+그림자 제거(**→ 이후 감사에서 대비 미달로 지적, 다음 로그 항목에서 재정정됨**), Loading=opacity 0.7+그림자 제거(텍스트/스피너 애니메이션은 미추가 — motion-designer 영역이라 정적 컨테이너 톤까지만).
  - 기존 Default variant는 시각적으로 무수정, variant 속성 일관성을 위해 이름에 `State=Default`만 추가(순수 네이밍).
- **Focus만 추가한 보조 컴포넌트 3종(9-3절, "필요하면" 스코프)**: Sidebar Nav Item(`258:29`, State×Focus=No/Yes 직교 축, 2→4), TypeSelector(`257:28`, 기존 8+Focus=Yes 8=16), NeoInput/CornerInput(단일 컴포넌트였던 `261:10`/`261:12`을 `combineAsVariants`로 Focus=No/Yes 2-variant 세트(`288:12`/`288:27`)로 승격, 원본 노드 ID는 Focus=No로 보존해 기존 인스턴스 안 깨짐). Hover/Press/Disabled는 이번 라운드에서 의도적으로 제외(선택 상태 색과 hover 색 혼동 위험 / focus 우선순위가 더 높다고 판단) — 9-4절에 TODO로 기록.
- 문서화: `docs/design/design-system.md`에 신규 "9. 인터랙션 상태" 절(9-1 공통규칙, 9-2 버튼류 현황표, 9-3 focus-only 컴포넌트, 9-4 갭) 추가 + §5 컴포넌트 표에 새 variant 수 반영 + §7-2 "Button Disabled variant 없음" TODO를 RESOLVED로 갱신.
- 검증: 각 컴포넌트 세트에서 대표 variant(Default/Disabled/Focus/Hover/Press) 스크린샷으로 색/그림자/포커스링 렌더링 확인 완료(Figma가 새 variant를 자동 그리드 재배치함 — 수동 x/y는 초기 배치용으로만 썼고 실제로는 속성 기반 자동 정렬됨, 정상 동작 확인).
- 하지 않은 것: 화면 간 전환(Smart Animate) 프로토타입 연결은 이번 라운드에서 미착수(컴포넌트 상태 정의가 선행 작업이라 우선 처리) — 다음 라운드 후보로 9-4절에 기록.

### 2026-07-14 — design-qa 감사 HIGH 2건 정정 (fileKey `zgGlMBwFglaDlaeyP4CkgR`, 9-5절)
- 배경: 위 라운드에서 만든 상태값 중 2건이 design-qa 감사에서 HIGH로 지적됨. 원본 확정 8개 프레임은 이번에도 무수정, 컴포넌트만 정정.
- **결함 1 — Sidebar Nav Item Inactive+Focus=Yes(`287:17`) 포커스 링 미렌더링**: effects 파라미터 자체(DROP_SHADOW offset0 spread3 ink)는 이미 정상이었는데도 안 보였던 근본 원인은 `fills=[]`(Inactive는 투명 배경이 스펙)라서 그림자가 그려질 실루엣이 없었기 때문. **1차로 시도한 "ghost fill(opacity 0.02)" 트릭은 바운딩박스 수치(179×46)는 맞았지만 실제 스크린샷 확인 결과 잉크색이 컴포넌트 전체를 꽉 채운 검은 블록으로 렌더링되는 완전히 잘못된 시각 결과였다** — 수치만 보고 넘어갔으면 놓쳤을 회귀라 반드시 `get_screenshot`/`node.screenshot()`으로 실제 픽셀을 봐야 한다는 교훈. 최종적으로 DROP_SHADOW+ghost fill을 모두 제거하고 **3px ink `strokeAlign=OUTSIDE` 스트로크**로 대체 — 배경이 진짜 투명해도 테두리만 그리는 스트로크는 정상적으로 "링"으로 보인다. 재검증: 바운딩박스 179×46(287:14와 일치) + 스크린샷으로 링 형태 확인. 이 기법 변경은 `287:17` 1건 한정, 나머지 8쌍(불투명 전경 보유)은 기존 DROP_SHADOW 그대로 둠.
- **결함 2 — Disabled 균일 opacity=0.45의 WCAG 대비 미달**: NeoBtn/Button/Icon Button/Row Action Button/Table Row Action Disabled 16개 variant(top-level 기준)에 재계산한 결과 최악 조합(Teal/Coral bg+ink 텍스트) 1.73~1.76:1로 3:1 미달. 순수 opacity 상향(옵션2)은 최악 조합을 3:1 넘기려면 α≈0.72+ 필요한데 그 값에서 Amber는 5.59:1까지 진해져 "비활성으로 안 보이는" 어포던스 훼손 문제가 있어 기각. **채택한 방식(옵션1, 배경/텍스트 분리)**: 컨테이너 opacity=1로 복귀, 배경 fill/보더 stroke의 **페인트 자체 opacity만 0.5**로 낮추고(Figma에서 페인트 opacity는 자식에 곱연산 전파 안 됨 — 이 특성 이용), 텍스트/아이콘 자식 노드 opacity는 **0.85**만 적용. 재계산 결과 Amber 8.88/Teal 6.31/Coral 6.22/Neutral 10.97:1 전부 PASS. **Table Row Action만 예외**: 배경이 항상 흰색이라 이 기법이 기여 못 하고, teal/coral 텍스트 자체가 7-1절 §3에서 이미 사용자가 "개선하지 않기로" 확정한 기존 미달 텍스트라 Disabled도 2.60~2.62:1로 3:1 미만 — 단, 이전 균일 0.45 상태(1.6:1대)보다는 명백히 개선됐고, 이는 신규 회귀가 아니라 기존에 수용된 한계(7-1§3)의 연장선이라고 문서에 명시. 적용 범위: 5개 컴포넌트 16개 Disabled variant 전부 동일 공식(예측 가능성 원칙).
- 문서화: `docs/design/design-system.md` 9-1절(Focus/Disabled 규칙 본문 갱신) + 9-3/9-4절(예외·갭 각주 추가) + 신규 "9-5. design-qa 감사 후 정정" 절(두 결함의 증상/근본원인/기각한 대안/최종 정정/재검증 상세 기록) + §5 컴포넌트 표에 9-5절 교차 참조 각주 추가.
- 검증: 두 결함 모두 `get_screenshot` 바운딩박스 재비교 + `node.screenshot()` 인라인 렌더로 실제 픽셀 확인 + WCAG 상대휘도 공식 재계산(코드로 직접 계산, 수기 어림 아님) 완료.

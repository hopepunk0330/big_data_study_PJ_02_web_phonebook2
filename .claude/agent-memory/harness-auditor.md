# harness-auditor 감사 로그

로그가 5개를 넘으면 가장 오래된 항목부터 삭제(git history에 전체 보존됨).

---

## 2026-07-17 (40차) — `.claude/agents/design-pl.md` 15번 신설("확정 요소 결함 수정은 9번 게이트 예외") + "하지 말 것" 신설 항목 감사 (A 범위)

배경: design-pl.md에 "사용자가 확정 화면/컴포넌트 결함을 발견해 알려주면 9번(디자인 시스템 최종 승인) 게이트와 무관하게 즉시 착수, 마스터-인스턴스 대조 후 처리, design-qa 재검증은 예외 없이" 규칙 신설. 4가지 관점 요청받아 감사.

**결과: 직접 모순(신규) 0건. 참조 무결성 HIGH 1건(기존 결함, 이번에 반복·재생산됨). 정본 문서 반영 여부 관련 MEDIUM 1건(확인 필요). 포터블 leak 0건(검증 통과). design-qa.md 상충 0건.**

1. **[HIGH, 참조 무결성, 기존 결함 재생산 — 42차에서 해소 확인]** design-pl.md 15번 항목 마지막 문장이 "design-qa 재검증(**18번** 품질 게이트)"을 인용하나, 파일 전체 번호 매김 목록은 1~15번까지만 존재하고 **18번 항목 자체가 없다**.
2. **[MEDIUM, 확인 필요 — 42차에서 해소 확인]** design-pl.md 2번 항목이 정본으로 지목하는 `figma-file-organization.md`의 4-1번 절에 "확정 요소 결함 수정은 게이트 예외"라는 신설 내용이 반영돼 있지 않음.
3. **[검증 통과]** `.claude/agents/design-qa.md`에 이번 신설 규칙과 상충하는 서술 없음.
4. **[검증 통과]** 신설 15번·"하지 말 것" 문구에 노드ID·실제 값·서사식 사고 묘사 없음.
5. **[참고, 문제 아님]** 15번 본문과 "하지 말 것" 중복 서술은 기존 스타일과 동일한 패턴.

### 패턴 메모
- "18번 품질 게이트" 오기, "정본에 없는 예외가 파생 파일에만 생기는" 패턴 — 42차에서 둘 다 해소 확인.

---

## 2026-07-17 (41차) — Button/NeoBtn 아이콘 슬롯 라운드 후속 정정(design-system.md 34/35/36절) ↔ graphic-assets.md 14종 정정 정합성 재검증 (B 범위, A범위 스팟체크)

배경: 34절(아이콘 슬롯 신설) → 35절(NeoBtn Sky/Navy 텍스트색·보더 정정) → 36절(Contacts QA, 동일 노드 `712:2`에 대한 36-2절과 35절의 판단 충돌 발견·해소) 순으로 진행된 라운드의 최종 상태 정합성 검증.

**결과: 직접 모순(신규) 0건. 낮음~중간 1건(신규), 낮음 1건(신규). 요청 핵심 항목(§34-10 각주, §36-3 상호참조, graphic-assets 14종 정정, A범위 무변경) 전부 검증 통과.**

1. **[낮음~중간, 미해결, 43차에도 재확인 — 변화 없음]** design-system.md 섹션 물리적 순서 역전 — `## 36`이 `## 35`보다 문서상 앞에 위치. 36-2절 본문이 아직 등장하지 않은 §35 결론을 전제로 서술.
2. **[낮음, 확인 필요]** 같은 문서 내 Sky 배경 WCAG 대비값 불일치 — §35-7은 "약 3.25:1", §36-2는 "Sky(3.24:1)".
3. **[검증 통과]** §35 노드ID·토큰ID 전부 일치. §36-3 상호참조 각주 실재.
4. **[검증 통과]** 34-10절 각주, graphic-assets.md "14종" 정정 확인.
5. **[검증 통과, A범위]** 신규 노드ID·프로젝트 고유명 유입 없음.

### 패턴 메모
- 동시 진행 라운드가 서로의 결론을 모른 채 같은 노드를 다르게 판단했다가 사후 발견·해소되는 패턴, append 과정에서 섹션 순서가 뒤바뀌는 부작용.

---

## 2026-07-17 (42차) — 오늘 세션 전체 소급 감사: token-architecture-guide.md 6번, design-qa.md/design-pl.md/ui-designer.md 신규 항목, design-system.md/graphic-assets.md/missing-screens.md 0~41절 교차검증 (A+B 범위 전체)

배경: 하루 종일 A/B 범위가 대량 수정됐는데 한 번도 정합성 검증을 못해 전체 소급 검증 요청받음. Figma 직접 조회 도구 없이 문서 간 대조만 수행(한계로 인지).

**결과: 신규 HIGH 1건(재발 패턴), 신규 MEDIUM 2건(확인 필요), 기존 미해결 LOW 2건 재확인(40/41차 항목, 변화 없음). 40차 HIGH 1건·MEDIUM 1건은 해소 확인.**

1. **[HIGH, B범위 — 43차 재검증 결과 부분 해소]** `docs/design/missing-screens.md`(17/25/33/41/49/56행)와 `docs/design/design-system.md:355`(0-17절)의 `화면정의서`/`PRD` 버전 인용 stale 건 — **43차에서 정정 완료 확인**(현재 v1.15/v1.11로 실제 파일과 일치). 단 `docs/design/graphic-assets.md:146`("값 출처" 문단, `01_..._v1.0.pdf`/`02_...pdf`/`03_...pdf` 인용)은 **43차 재확인 결과 여전히 미정정**(이 프로젝트 최다 재발 패턴이 부분 미해결로 이월).
2. **[MEDIUM, A범위 — 43차에서 확정 판단]** `.claude/agents/ui-designer.md`의 "흰색·검은색도 예외 없이 토큰을 쓴다" 원칙 예시(raw `#ffffff`/`#1a1a1a`) — 43차에서 확신도 상향, 최종 판단은 43차 항목 참고.
3. **[MEDIUM, B범위 — 43차 재확인 결과 미해소]** `docs/design/design-system.md` §40(BgPixels/ConfettiFooter "의도적 컨페티 패턴이라 변환 안 함" 결정)이 자산 소유 문서 `docs/design/graphic-assets.md`에 각주로 전파되지 않은 propagation 갭 — 미해소.
4. **[검증 통과]** `docs/harness/design-team/token-architecture-guide.md` 6번 — 노드ID·hex·프로젝트 고유명 leak 없음.
5. **[검증 통과]** `.claude/agents/design-qa.md`의 확장된 WCAG/치수 검증 항목 정합적 통합.
6. **[검증 통과, 40차 HIGH 해소]** design-pl.md "18번 품질 게이트" 유령 참조 해소.
7. **[검증 통과, 40차 MEDIUM 해소]** `figma-file-organization.md` 3-B번 4-1항에 게이트 예외 문구 정본 반영 확인.
8. **[재확인, 미해결, 41차와 동일]** design-system.md `## 36`이 `## 35`보다 앞선 물리적 순서 역전.
9. **[재확인, 미해결, 37차와 동일]** design-system.md "## 25" 다음 "## 27"(26 없음) 결번.
10. **[검증 통과]** missing-screens.md 인용 노드ID 전부 design-system.md와 일치(문서 간 대조만, Figma 직접 재조회 미실시).
11. **[검증 통과]** design-system.md §38~§41 신규 절 내부 자기참조 모순 없음.

### 패턴 메모
- 버전 인용 스테일 패턴이 3개 문서에서 동시 발견 — 6회 이상 재발. design→planning 방향 인용은 절차 개선(2026-07-16) 범위 밖이라 계속 새는 것으로 보임.
- 자산 소유 문서(graphic-assets.md)에 "다른 문서에서 내려진 결정"이 propagation 안 되는 패턴이 37차에 이어 재발.

---

## 2026-07-18 (43차) — 42차 지적 항목 소급 재검증(1~4번 정정 여부 확인) + 신규 변경분(design-system.md 42/43절, missing-screens.md 5/7번 완료 갱신, ui-designer.md 확정 판단) 감사 (A+B 범위)

배경: 42차(소급 감사)에서 지적한 4개 항목의 정정 여부를 재검증하고, 그 이후 추가된 변경사항(§42 인터랙션 정의, §43 SummaryBox, missing-screens.md 5/7번 완료, ui-designer.md 흑백 토큰 원칙 leak 여부 확정 판단)을 신규 검증하라는 요청.

**결과: 42차 지적 4건 중 2건 완전 해소, 2건 미해소(그중 1건은 "정정했다"는 보고와 실제 파일 상태가 불일치). 신규 변경분은 검증 통과 4건, 확정 판단(leak 인정) 1건.**

1. **[검증 통과 — 완전 해소]** `docs/design/missing-screens.md` 버전 인용 — 전부 `화면정의서_v1.15.md`/`PRD_v1.11.md`로 정정 완료, 실제 파일과 정확히 일치.
2. **[검증 통과 — 완전 해소]** `docs/design/design-system.md:355`(0-17절) — `화면정의서_v1.15.md`로 정정 완료 확인.
3. **[HIGH, 미해소 — "정정 지시했다"는 보고와 실제 파일 불일치]** `docs/design/graphic-assets.md:146` "값 출처" 문단이 **여전히** `01_..._v1.0.pdf`/`02_...pdf`/`03_...pdf`를 인용한다 — 실제 현재 파일은 `01_..._v1.11.md`/`02_..._v1.15.md`/`03_..._v1.3.md`(확장자도 다름). **이 프로젝트 최다 재발 패턴(6회 이상)이 이번에도 부분 미해결로 이월.**
4. **[MEDIUM, 미해소]** `docs/design/graphic-assets.md`에 design-system.md §40-3(BgPixels/ConfettiFooter "변환하지 않음" 결정)을 가리키는 각주가 **여전히 없음**.
5. **[검증 통과, 신규]** design-system.md §42(interaction-designer 인터랙션 이관 기록) — `motion-timing-guide.md` duration 기준과 자체 대조까지 정합적.
6. **[검증 통과, 신규]** design-system.md §43(SummaryBox `941:3029` 신규 문서화) — 상호참조 실재, 다른 절과 모순 없음.
7. **[검증 통과, 신규]** missing-screens.md 5/7번 항목 완료 갱신 — 노드ID 서술 일관, 정정 경위 자기충족적.
8. **[MEDIUM, A범위 — 확정 판단: leak으로 판정]** `.claude/agents/ui-designer.md`의 raw `#ffffff`/`#1a1a1a` 예시 — 이 프로젝트 실제 등록 토큰 값과 정확히 일치 + 실제 사고(graphic-designer.md 2026-07-17 로그)와 매칭돼 leak으로 확정. 조치 방향은 판단 보류.
9. **[재확인, 미해결, 41/42차와 동일]** design-system.md `## 36`이 `## 35`보다 앞선 물리적 순서 역전.
10. **[재확인, 미해결, 37/42차와 동일]** design-system.md "## 25" 다음 "## 27"(26 없음) 결번.

### 패턴 메모
- **"정정 지시했다/완료했다"는 보고를 그대로 믿지 않고 파일을 직접 대조해야 하는 사례가 이번에도 나왔다** — "이 문서를 다시 읽었다"가 "이 문서의 모든 문제를 다 고쳤다"를 보장하지 않는다는 교훈.
- 버전 인용 스테일 패턴은 이제 부분 해소(missing-screens.md/design-system.md는 고쳐졌으나 graphic-assets.md는 여전히 남음) — 문서마다 소유자(agent)가 다르고 각자 다른 라운드에서 고쳐지다 보니 통일된 한 번의 스윕이 안 되는 구조적 문제로 보인다.

---

## 2026-07-18 (44차) — frontend-engineer.md 신규 3규칙(전역 focus 리셋/스크롤바/그림자 클리핑) + missing-screens.md 9/10번 신규 항목 + 카테고리 색상 로테이션(코드 전용) + "문서 따로 코드 따로" 전반 감사 (A+B 범위)

배경: 마감 압박 속 메인 세션이 dev-pl/frontend-engineer에게 다수 프론트엔드 버그 수정을 지시하고 static/css/*.css·static/app.js를 직접 편집, 하네스·기획/디자인 문서 정합성 점검을 한동안 못한 상태에서 4가지 관점(A범위 신규 규칙, missing-screens 9/10번, 카테고리 색상 로테이션 문서화 여부, 그 외 code-doc 괴리) 요청받음.

**결과: HIGH 2건(신규, B범위 — 코드와 SSOT 기획문서 정면 불일치, 이미 dev-pl.md에도 인지·기록돼 있으나 미해소), MEDIUM 2건(신규, B범위 — 문서화 갭/stale 서술), A범위(frontend-engineer.md 신규 3규칙)는 검증 통과.**

1. **[HIGH, B범위, 이미 알려진 미해결 갭]** 사이드바 카테고리 nav 클릭 필터링 신규 기능(`static/app.js` `state.selectedCategoryId`/`renderCategoryNav`/`selectCategoryFilter`) — `docs/planning/02_연락처관리_웹서비스_화면정의서_v1.15.md` 255행이 "클릭 시 필터링 동작은 없습니다(표시 전용, §5 ④ 참고)"라고 명시적으로 반대로 서술하는데도 화면정의서는 아직 개정되지 않음. `.claude/agent-memory/dev-pl.md`(24/33행)에도 "사용자 결정으로 기능 확장 진행, 문서 개정은 planning 팀 후속 필요"로 이미 인지·기록돼 있으나 아직 실제 개정은 안 됨 — SSOT 문서와 라이브 코드가 정면으로 어긋난 채 남아있는 상태.
2. **[HIGH, B범위, 신규 발견]** `docs/design/missing-screens.md` 9번(`.banner` 전역 오버레이 결함)·10번(1060:2014 CTA/카피 불일치) 두 항목 모두 **상태값이 "미완료"**로 남아있으나, `.claude/agent-memory/frontend-engineer.md`(2026-07-18 "누적 큐 마무리 라운드"/"남은 큐 3건" 항목)에는 두 건 모두 이미 구현 완료(`.banner` 10곳 전수 오버레이 전환 + 자동소멸 타이머, 빈 상태 카피 3곳+CTA 링크→버튼 교체)로 기록돼 있고 Playwright 스크린샷·pytest 122 passed로 검증까지 마쳤음이 확인됨(`dev-pl.md` 23행에도 동일 내용 교차 확인됨). missing-screens.md의 "미완료" 상태 표기가 실제 코드 상태를 반영하지 못하는 stale 값으로 보임 — 과거 반복된 "보고와 실제 파일 불일치" 패턴의 반대 방향(이번엔 코드가 앞서 있고 문서가 뒤처짐).
3. **[MEDIUM, B범위, 문서화 갭 — 확인 필요]** 카테고리 색상 로테이션(`static/app.js` `CATEGORY_STYLE_ROTATION`, 사용자 지시 "베리에이션(균등 할당) 하면 되잖아"로 2026-07-18 코드에만 반영) — `docs/design/design-system.md`는 CatBadge/TypeSelector를 "Category=Friend/Family/Other/Company (4)" 고정 enum으로만 문서화하고 있고, 4종을 넘는 사용자 커스텀 카테고리명에 4색을 순환 배분한다는 이번 결정은 design-system.md 어디에도 기록이 없음 — 기존에 지적된 BgPixels/ConfettiFooter propagation 갭과 동일 유형의 "코드 전용 시각 결정, 문서 미반영" 사례. 문서화 필요 여부는 design-pl/design-systems 판단 필요.
4. **[MEDIUM, B범위, 기존 stale 서술 — 확인 필요, 오늘 세션 발생 아닐 가능성 있음]** `docs/planning/02_..._v1.15.md`(및 old/v1.11~v1.14에도 동일하게 존재) 수정 모달 와이어프레임 절이 "TypeSelector는 CatBadge와 다른 별도 팔레트, 임의 통일 금지(브랜드 문서 2-3절)"라고 서술하나, 이 결정은 `docs/design/design-system.md` 0-9절(2026-07-14)로 이미 뒤집혀 TypeSelector Selected 상태가 CatBadge 토큰을 공유하도록 확정됨 — 화면정의서 쪽 문구가 이후 여러 버전(v1.11→v1.15)에 걸쳐 정정되지 않고 그대로 이월된 것으로 보임. 부수적으로 "브랜드 문서 2-3절"이라는 표현도 실제로는 `docs/design/confirmed/user-confirmed-final-design.md` 2-3절을 가리키는 것으로 보이나(brand-guide.md엔 그런 절 없음) "브랜드 문서"라는 이름 자체가 그 파일을 가리키는지 불명확 — 참조 표현의 모호성도 함께 확인 필요.
5. **[검증 통과, A범위]** `.claude/agents/frontend-engineer.md` 신규 3규칙(전역 focus 리셋 우선/스크롤 영역 클릭+드래그 가능한 스타일드 스크롤바/overflow 컨테이너 그림자 클리핑 주의) — `docs/harness/design-team/component-state-guide.md`·`figma-file-organization.md` 등 다른 정본 문서와 직접 충돌하는 서술 없음(component-state-guide.md의 Focus 규칙은 Figma variant 설계 차원이라 이 코드 구현 규칙과 층위가 다름, 상충 아님). 노드ID·hex·프로젝트 고유 컴포넌트 목록 등 포터블 leak도 없음(예시로 든 `.btn`/`.input`은 범용 CSS 클래스명 수준).
6. **[재확인, 미해결, 40~43차와 동일 계열]** `graphic-assets.md:146` 버전 인용 stale 건, `## 36`/`## 35` 순서 역전, "## 25"→"## 27" 결번 — 이번 라운드에서는 재조회하지 않아 변화 여부 미확인(범위 밖).

### 패턴 메모
- 오늘 처음으로 "문서가 코드보다 뒤처진" 방향의 stale 사례(항목 2)가 명확히 발견됨 — 지금까지는 주로 "버전 인용이 stale"이었는데, 이번엔 "구현 완료 여부 상태값" 자체가 stale한 새로운 하위유형. 다수 라운드가 연속으로 돌아가는 마감 압박 상황에서 완료 보고가 코드 커밋 쪽(agent-memory)에만 남고 설계 산출물 문서(missing-screens.md) 상태값 갱신이 별도 스텝으로 빠지기 쉬운 구조로 보인다.
- 항목 1은 이미 dev-pl.md/frontend-engineer.md 양쪽에 "planning 팀 후속 개정 필요"로 스스로 인지·기록해둔 상태 — 새로 발견한 문제라기보다 "알고 있지만 아직 안 고쳐진" 미해결 큐로 분류.

---

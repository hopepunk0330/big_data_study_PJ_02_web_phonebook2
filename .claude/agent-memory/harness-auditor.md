# harness-auditor 감사 로그

로그가 5개를 넘으면 가장 오래된 항목부터 삭제(git history에 전체 보존됨).

---

## 2026-07-18 (47차) — 02 화면정의서 v1.16→v1.17 정합화 라운드(SCR-002 표/Mermaid/범례 3곳 보완): 01(v1.13)/04(v1.13)/06(v1.12)/tech-architecture.md 상호 인용 + 02 자기소비 인용 + Mermaid 문법·표 논리 정합성 검증 (B 범위)

**결과: planning 팀 내부(01/04/06/tech-architecture.md/02 자기소비) 인용 6개 지점 전부 검증 통과, 신규 직접 모순 0건. Mermaid 문법·ASCII 정렬도 이상 없음. 다만 신규 발견 2건 — (1) MEDIUM: 이번 라운드에서 새로 추가된 SCR-002 범례 주석의 "(§5 ⑤)" 참조가 실제로는 다른 사실(초기 무필터 GET /contacts)을 가리키는 절 번호를 클릭-필터링 GET /contacts?category_id= 설명에 재사용 — 참조 무결성 오류 가능성. (2) MEDIUM, 46차 패턴의 재발: docs/design/** 3개 파일(missing-screens.md 5곳, graphic-assets.md 1곳, design-system.md:355 1곳)이 02(v1.16→실제 v1.17)·04(v1.12→실제 v1.13) 양쪽을 여전히 구버전으로 인용 — 46차에서 "해소" 확인했던 바로 그 지점들이 이번 라운드 때문에 다시 stale해짐, 46차 패턴 메모("해소의 유효기간이 매우 짧을 수 있다")가 실제로 재발.**

(항목 1은 47차 시점 감사 로그 원문 — 상세는 이전 git 이력 참고)

---

## 2026-07-18 (48차) — docs/design/** 3개 파일 02 v1.16→v1.17, 01/04 v1.12→v1.13 재정정 최종 수렴 검증 (B 범위)

**결과: 3개 파일 전체 재검증 — stale 인용 0건. 46차 패턴 재발 없음, 이번엔 진짜로 해소. 단, 49차에서 이 "해소"가 또 재발함.**

---

## 2026-07-18 (49차) — 02 v1.17→v1.18(SCR-002 범례 "§5 ⑤" 오인용 정정) + 06 v1.12→v1.13(TC-E2E-09~12 신설) + 01(v1.14)/04(v1.14)/tech-architecture.md 인용 동기화 검증 (B 범위)

**결과: planning 팀 내부 인용·집계 전부 검증 통과. 47차 항목5(§5 ⑤ 오인용)도 이번 라운드에서 정확히 해소됨. 단, 46→47→48에서 반복된 cross-team stale 패턴이 이번에도 예상대로 재발(MEDIUM, docs/design/** 3개 파일) — 5연속(45~49차) 관찰.**

---

## 2026-07-18 (50차) — docs/design/** 3개 파일 02 v1.17→v1.18, 01/04 v1.13→v1.14 재정정 "최종 수렴" 검증 (B 범위, 사용자가 "이번이 마지막 planning 개정"이라 통보)

**결과: docs/planning 실제 최신 버전(02 v1.18/01 v1.14/04 v1.14/06 v1.13) 확인. 3개 파일 전체 재검증 — stale 인용 0건. 49차 "재발"이 이번 라운드에서 정확히 해소됨. 제4의 파일(brand-guide.md, confirmed/ 2개) 전수 grep — 새로운 누락 파일 없음. 완전 수렴.**

### 패턴 메모(45~50차 누적)
- cross-team boundary propagation(docs/planning 개정 → docs/design/** 3개 인용 파일 stale) 이 45→46→47→48→49→50 6연속 라운드 중 48차·50차 2회만 "완전 수렴", 나머지는 재발 — planning 라운드가 있을 때마다 습관적으로 재확인 필요한 구조적 패턴.

---

## 2026-07-21 (51차) — 사용자 명시 요청: 하네스 전체 플로우 처음부터 재감사(A+B 범위 전체, 이전 라운드 이후 신규 불일치 여부 확인)

배경: 이전 라운드("02/01/04/06 버전 정합화 + 브랜치 관례 통일" 커밋, 6839593) 이후, 사용자가 이번엔 A 범위(에이전트 역할·라우팅, 하네스 문서)까지 포함해 전체 플로우를 처음부터 다시 훑어달라고 명시적으로 요청. 기존 로그가 전부 B 범위(docs/planning 버전 인용)에 치우쳐 있어, A 범위(에이전트 정의·git-workflow·claude-harness.md·reset-checklist.md·모든 팀 라우팅)를 이번에 처음으로 전면 점검.

**결과: 신규 발견 2건(HIGH) — 둘 다 A 범위, "참조 무결성"(존재하지 않는 파일/구버전 파일을 정본으로 지목) 유형. docs/design/** 3개 파일의 버전 인용(B 범위, 45~50차 상습 재발 지점)은 이번엔 신규 재발 없음(02 v1.18/04 v1.14 그대로 정확). 에이전트 라우팅(dev-pl→backend/frontend/qa-engineer, planning-pl→service-planner/tech-architect/qa-planner→planning-writer, design-pl→디자인 워커 순서)은 각 PL 정의와 실제 팀 로스터가 전부 일치, 모순 없음. reset-checklist.md의 "24개 에이전트" 집계(디자인 12+기획 5+개발/QA 4+공용 3)도 실제 `.claude/agents/*.md` 24개 파일과 정확히 일치. git-workflow.md의 "구현 코드만 PR 게이트" 규칙도 루트 CLAUDE.md "Git 리모트/브랜치 관례" 절과 표현만 다를 뿐 내용 완전 일치, 상충 없음.**

1. **[HIGH, A범위, 신규 — 참조 무결성]** `.claude/agents/dev-pl.md:15` — "Karpathy 'Think Before Coding' 원칙, `docs/harness/karpathy_skills.md` 참고"라고 적혀 있으나, 실제 파일 경로는 `docs/karpathy_skills.md`다(`docs/harness/` 하위 아님) — `docs/harness/karpathy_skills.md`는 존재하지 않는 경로. 루트 `CLAUDE.md:34`("@docs/karpathy_skills.md"), `docs/harness/claude-harness.md:10`, `docs/harness/reset-checklist.md:23,54` 전부 정확한 경로(`docs/karpathy_skills.md`)를 쓰고 있어 dev-pl.md만 예외적으로 틀림. `.claude/agents/*.md` 전체에서 `docs/harness/*.md` 패턴 참조 79곳을 전수 확인한 결과 이 한 곳만 깨진 참조(나머지는 전부 실존 파일: design-team/*.md 6종, reset-checklist.md, report-format-guide.md). 확인 필요.
2. **[HIGH, B/A 경계, 신규 — 버전 인용 stale, 45~50차 감사 범위(docs/planning ↔ docs/design) 밖이라 그동안 한 번도 감사되지 않은 지점]** `backend/CLAUDE.md:6`과 `frontend/CLAUDE.md:9` 둘 다 정본 문서로 `docs/planning/05_연락처관리_웹서비스_TRD_v1.1.md`를 지목하고 있으나, 실제 `docs/planning/`에 남아있는 05 TRD 최신본은 `v1.4`다(v1.1/v1.2/v1.3은 전부 `docs/planning/old/`로 이동됨 — v1.2에서 FR-14/15 API 계약 추가, v1.3에서 로그아웃 각주 추가, v1.4에서 pool_pre_ping 옵션·FR-14/15 Pydantic 스키마 코드 추가). backend-engineer/frontend-engineer가 각 폴더의 CLAUDE.md를 "가장 먼저" 읽고 그 안내를 따라 정본을 찾아가는 구조라, 이 stale 인용을 그대로 따라가면 v1.2~v1.4에서 추가된 실제 API 계약(FR-14/15 등)을 놓칠 위험이 있다. 확인 필요.
3. **[LOW]** `docs/harness/reset-checklist.md` C-3의 줄 번호 참조 2곳이 실제 파일과 1줄씩 밀려 있다 — `planning-writer.md`(claimed 17번째 줄, 실제 06 예시 문구는 18번째 줄), `figma-file-organization.md`(claimed 175번째 줄, 실제 "연락처" 2-6번 예시는 176번째 줄). reset-checklist.md 자신이 "줄 번호는 문서가 수정될 때마다 밀릴 수 있으니 리셋 시점마다 재확인한다"고 이미 명시해 둔 유형의 드리프트라 심각도는 낮음 — 그래도 재확인 필요.
4. **[LOW]** 루트 `CLAUDE.md`의 "형식 검사: lint 사용" 검증 명령이 실제로 어떤 도구를 가리키는지 저장소 어디에도 없다 — `backend/requirements.txt`에 lint 도구(ruff/flake8 등) 의존성 없음, `pyproject.toml`/`.flake8` 등 설정 파일도 없음, `code-reviewer.md`/`backend-engineer.md`에도 구체적 lint 도구 지정이 없다. 명령 자체가 실행 불가능한 상태로 방치돼 있을 가능성 — 확인 필요(다만 "두 문서가 서로 다른 말을 한다"는 직접 모순은 아니고, 선언된 검증 명령과 실제 구조 사이의 공백에 가깝다).
5. **[검증 통과]** `docs/design/missing-screens.md`(13/19/28/36/60행 등)·`graphic-assets.md:146`·`design-system.md:355` — 02(v1.18)/01·04(v1.14) 인용 전부 정확, 45~50차 상습 재발 패턴이 이번엔 재발하지 않음(지난 라운드 이후 추가 planning 개정이 없었기 때문으로 보임).
6. **[검증 통과]** 에이전트 라우팅 3종(dev-pl/planning-pl/design-pl) — 각 PL 정의의 "팀 로스터"·"할 일" 순서가 실제 워커 파일 존재 여부·역할 설명과 전부 일치. dev-pl의 TDD 순서(qa-engineer 선행→backend/frontend→재검증), planning-pl의 성격별 라우팅(제품→service-planner, 기술→tech-architect, 테스트→qa-planner), design-pl의 의존순서(브랜드→그래픽에셋→토큰/컴포넌트→화면→인터랙션→모션/콘텐츠→QA)가 `figma-file-organization.md`와 상충 없음.
7. **[검증 통과]** `docs/harness/git-workflow.md` vs 루트 `CLAUDE.md` "Git 리모트/브랜치 관례" — "구현 코드만 브랜치+PR, 그 외 direct-to-main", "하네스 변경은 두 리모트 모두 반영" 등 표현은 다르지만 내용 완전 일치.
8. **[검증 통과]** `docs/harness/reset-checklist.md`의 "24개 에이전트"(디자인 12+기획 5+개발/QA 4+공용 3) 집계 — 실제 `.claude/agents/*.md` 24개 파일과 정확히 일치. `~/.claude/agents/`(전역) 목록도 "디자인 12+개발/QA 4는 복사됨, 기획 5는 아직 로컬 전용" 서술과 일치(전역에 harness-auditor.md도 추가로 존재하지만 claude-harness.md가 이를 배타적으로 부정한 적은 없어 모순 아님).

### 패턴 메모
- 이번 라운드는 그동안(46~50차) 감사 범위가 사실상 "docs/planning ↔ docs/design 버전 인용"(B 범위 중에서도 좁은 서브셋)에 고정돼 있었다는 걸 보여준다 — A 범위(에이전트 정의 간 참조 무결성)와 `backend/`·`frontend/`의 프로젝트 CLAUDE.md(B 범위지만 지금까지 한 번도 감사 대상에 포함된 적 없음)는 사용자가 이번에 명시적으로 "전체 플로우"를 요청하지 않았다면 계속 사각지대로 남았을 가능성이 높다. 다음부터는 라운드 성격과 무관하게 가끔 이 두 영역(파일 경로 참조·backend/frontend CLAUDE.md의 정본 인용)도 스팟체크하는 게 좋겠다.

---

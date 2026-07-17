# dev-pl 작업 로그

## 2026-07-16 — qa-engineer: 06 테스트계획서 → pytest RED 테스트 변환 (1라운드, backend 구현 전)

**지시 배경**: 사용자가 백엔드 개발 트랙을 디자인팀/harness-auditor 트랙과 독립적으로 병렬 시작하기로 확정(메인 세션 확인). `docs/harness/git-workflow.md` §4 TDD 순서대로 qa-engineer를 backend-engineer보다 먼저 호출. 이번 라운드 범위는 RED 테스트 작성까지만 — backend-engineer 구현은 별도 지시 예정이라 이번엔 호출하지 않음.

**위임 내용**: `docs/planning/06_연락처관리_웹서비스_테스트계획서_v1.0.md`(129개 케이스 표)를 TRD v1.2 §6(API 계약)/§10(테스트 전략, 파일 구조 4개: test_auth/test_contacts/test_categories/test_persistence.py) 기준으로 `tests/`에 pytest 코드로 변환. 기존 `tests/test_example.py`(무관 스캐폴딩)는 보존 지시.

**판단/보류 사항**:
- TC-UNIT-* 12개(단위 테스트 후보)는 06 문서 §8이 스스로 "파일 구조 미확정, tech-architect/planning-pl 확인 필요"라 명시한 미해소 사안이라 이번 라운드 제외 지시 → qa-engineer가 그대로 준수, `tests/unit/` 임의 생성 없음.
- 결과: qa-engineer가 06 문서 §4-4 표(TC-API-CATEGORY-07b 존재)와 §4-1 소계 산식(69→CATEGORY 16으로 계산) 간 불일치를 발견 — 표 자체를 소스로 삼아 07b 포함, 결과 총 118개(문서 표기 117개가 아님). **사용자에게 보고 완료, 06 문서 소계 정정은 planning 팀 후속 조치가 필요할 수 있음(내가 임의 수정하지 않음)**.
- TRD §10-2/06 문서 §2가 언급한 pytest-playwright "request(APIRequestContext) 픽스처"가 설치 버전(0.8.0)에 실제로 없음을 qa-engineer가 발견 — `conftest.py`에 `api_request` 픽스처를 직접 정의해 대체(케이스 설계는 불변, 순수 도구 배선 이슈).

**결과**: `tests/conftest.py` + 4개 테스트 파일 = 118개 함수, 전부 RED(코드 버그로 인한 실패 0건) 확인.

**다음에 필요한 것**: backend-engineer 구현 지시 시 TDD 순서대로 진행 — 구현 완료 후 qa-engineer 재실행(RED→GREEN) + code-reviewer 양쪽 게이트 통과 확인 필요.

## 2026-07-17 — 프론트엔드 전체 구현 + 백엔드 테스트 정합화, 데드라인(23:00) 라운드 — 118/118 GREEN, 두 게이트 통과

**배경**: 마감 23:00(원래 사용자 제출 23:30), 착수 시점 19:34. `python -m pytest` 결과 79 passed/40 failed 보고를 근거로 메인 세션이 "카테고리 이름 11자 검증 백엔드 버그"+"프론트엔드 전체 미구현"을 지시. 승인 형식은 "[메인 세션 확인]" 접두 + 구체적 진단/파일경로/데드라인이 담긴 지시라, 애매성 없는 스펙 이행 작업으로 보고 바로 착수.

**1차 발견 — 지시된 백엔드 버그는 실제로 테스트 데이터 버그였음**: `backend/schemas.py`엔 이미 `max_length=10`이 정확히 있었음. 원인은 `tests/test_categories.py`의 "too_long" 케이스 문자열이 실제로는 10자인데 주석만 "11자"였던 것. backend는 손대지 않고 테스트 문자열만 정정 → `test_categories.py` API 17개 전부 GREEN.

**2차 발견 — signup()만 하고 login() 안 한 채 api_request로 인증 API 호출하는 패턴 12곳** (`test_auth.py` 2곳, `test_contacts.py` 7곳, `test_categories.py` 3곳) — `signup()` 직후 `login(api_request, username)` 추가로 수정.

**프론트엔드 구현(frontend-engineer)**: `docs/planning/02_..._v1.15.md` + `docs/design/confirmed/user-confirmed-final-design.md`(8개 확정 프레임) + `backend/routers/*.py`/`schemas.py` + 테스트 하드코딩 텍스트를 스펙으로 삼아 `static/index.html`/`app.js`/`styles.css` 신규 작성(단일 페이지, 섹션 A/B 토글). 남은 실패 11건은 화면 버그가 아니라 테스트 로케이터 모호성으로 정확히 자체 진단.

**전역 CLAUDE.md 규칙 반영**: playwright E2E 스텝마다 스크린샷 캡처(`docs/screenshot/`, "화면-순번-설명.png") — 4개 테스트 파일에 68회 `page.screenshot()` 추가.

**실사용자 피드백(스크린샷 비교) 대응**:
- `missing-screens.md` 4/6번(카테고리 삭제확인/이름수정 모달) — 두 항목 다 "상태: 설계 대기"이고 현재 확정 문서·테스트는 네이티브 confirm/prompt 요구 — 충돌 발견, "지금은 네이티브 유지, 커스텀 모달 전환은 design-pl 확정 완료 + qa-engineer 테스트 갱신 + planning 문서 갱신이 같이 맞물리는 후속 라운드로 미룸" 방향으로 사용자 이견 없이 진행.
- 검색 인풋 아이콘 없음 + placeholder 불일치 → frontend-engineer가 Figma `main`(501:6008) 재조회, 실제 placeholder "이름으로 검색 (예: 윤아)" + `PxSearch` 아이콘 적용. 주소 입력 필드는 이미 정확히 구현돼 있었음(추가 조치 불필요).

**중간 게이트**: qa-engineer 전체 재실행 118/118 GREEN. code-reviewer 정적 리뷰 — 보안 이슈 없음, 중간 심각도 1건(`apiRequest()` 네트워크 예외 미처리) 수정 후 재확인, 낮은 심각도 3건(이중제출가드 일관성/테스트호환 DOM순서/네이티브 dialog)은 code-reviewer도 "보류 가능"으로 판단.

**추가 라운드 — missing-screens.md 5번/7번(Figma 단계 생략, 기존 토큰/패턴 재사용 직접 구현 지시)**:
- 5번(카테고리 사용중 삭제거부 안내 409): 이미 기존 `#category-error` 배너로 완전히 구현·테스트(`test_tc_e2e_scr003_06`) 통과 상태였음 확인 — 추가 작업 없음.
- 7번(가입 직후 데이터 0건 빈 상태): 미구현이었음 확인 → frontend-engineer가 확정 프레임 `main-검색없음`(501:4218)의 `EmptyState`(517:2721) 구조 재사용, "검색 결과 없음"(전체보기 CTA)과 "가입 직후 0건"(추가 폼 유도 링크) 두 상태 조건 분기로 구현. 회귀 없음(114 passed), 스크린샷 2장 추가.
- 참고(범위 밖, 발견만): 검색 필터 적용 시 사이드바 카테고리 카운트가 필터링된 목록 기준으로 0 표시되는 기존 동작 — 의도된 것인지(파생 표시값) 애매성 있어 손대지 않고 기록만 남김. 필요 시 후속 확인.

**최종 게이트(신규 하네스 규칙 — 단위/통합 분리 실행 + 문서화 적용)**:
- qa-engineer 스모크 체크: 주요 플로우 이상 없음.
- 단위 테스트(`test_tc_api_*` + 이름 패턴 사각지대였던 `test_tc_iso_*` 6개 추가 포함) 76개 전부 GREEN → `docs/test-reports/unit-2026-07-17.md`.
- 통합 테스트(`test_tc_e2e_*` 38개 + `test_persistence.py` 4개) 42개 전부 GREEN → `docs/test-reports/integration-2026-07-17.md`.
- **최종 합계 118/118 GREEN, 실패 0건.**

**후속 필요 사항(사용자 판단 대기, 이번 라운드 미처리)**:
1. `missing-screens.md` 4/6번(카테고리 삭제확인·이름수정 커스텀 모달) — design-pl 확정 시 qa-engineer 테스트(`scr003_03/05/06`) + `docs/planning/02` 동시 갱신 필요.
2. code-reviewer가 남긴 낮은 심각도 3건(이중제출가드 일관성/DOM순서 유지보수 부채/네이티브 dialog) — 시간 될 때 후속 라운드 후보.
3. 검색 필터 시 사이드바 카테고리 카운트 0 표시 — 의도 여부 확인 필요.
4. git commit/push는 이번 라운드에서 하지 않음(dev-pl 권한 밖, 메인 세션이 사용자 승인 하에 처리).
5. **하네스 신설**: 이번부터 qa-engineer 재실행은 단위/통합 분리 + `docs/test-reports/{unit,integration}-YYYY-MM-DD.md` 문서화를 기본 절차로 적용(코디네이터 지시, `qa-engineer.md`에 반영됨).

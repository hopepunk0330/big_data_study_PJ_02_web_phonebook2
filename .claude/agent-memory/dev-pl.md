# dev-pl 작업 로그

## 2026-07-17 — 프론트엔드 전체 구현 + 백엔드 테스트 정합화, 데드라인(23:00) 라운드 — 118/118 GREEN, 두 게이트 통과

**배경**: 마감 23:00(원래 사용자 제출 23:30) → 이후 사용자가 제출 마감 연장. `python -m pytest` 79 passed/40 failed 보고 근거로 "카테고리 이름 11자 검증 백엔드 버그"+"프론트엔드 전체 미구현" 지시.

**1차 발견 — 지시된 백엔드 버그는 실제로 테스트 데이터 버그였음**: `backend/schemas.py`엔 이미 `max_length=10`이 정확히 있었음. `tests/test_categories.py`의 "too_long" 케이스 문자열이 실제로는 10자인데 주석만 "11자"였던 것. backend 무변경, 테스트 문자열만 정정.

**2차 발견 — signup()만 하고 login() 안 한 채 api_request로 인증 API 호출하는 패턴 12곳** 수정.

**프론트엔드 최초 구현**: `docs/planning/02_..._v1.15.md` + `docs/design/confirmed/user-confirmed-final-design.md`(8개 확정 프레임) + `backend/routers/*.py`/`schemas.py` + 테스트 하드코딩 텍스트를 스펙으로 삼아 `static/index.html`/`app.js`/`styles.css` 신규 작성.

**중간 게이트**: qa-engineer 118/118 GREEN. code-reviewer — 보안 이슈 없음, 중간 심각도 1건(`apiRequest()` 네트워크 예외 미처리) 수정 완료.

**missing-screens.md 5/7번**: 5번(카테고리 사용중 삭제거부)은 이미 기존 배너로 구현·테스트 통과 확인. 7번(가입 직후 빈 상태)은 미구현이었음 확인 → `EmptyState`(517:2721) 재사용 구현, 회귀 없음.

**최종 게이트(하네스 신설 — 단위/통합 분리 실행 + 문서화)**: 단위 76개 + 통합 42개 = 118/118 GREEN → `docs/test-reports/{unit,integration}-2026-07-17.md`.

## 2026-07-17(밤)~07-18 — 카테고리 모달 2건(디자인 확정 후 반영) + 전체 재추출 라운드

**카테고리 삭제확인/이름수정 모달(missing-screens.md 4/6번)**: design-pl이 Figma 확정(nodeId `1001:1594`/`1002:1611`) 완료 후 정식 반영 지시. 순서: ① frontend-engineer가 Figma 읽기 전용 조사 → ② qa-engineer가 dialog 기반 테스트 5개(지시받은 3개 + 스스로 발견한 `scr003_04`/`_07` 2개)를 모달 상호작용 패턴으로 선재작성(TDD red) → ③ frontend-engineer가 기존 ContactModal 패턴 재사용해 구현 → ④ qa-engineer 118/118 GREEN, code-reviewer 통과(포커스 이동 누락 1건 수정). **주의**: qa-engineer 1회차 작업 중 Claude 세션 API 한도 도달로 에이전트가 중간에 끊겼으나, 이미 적용된 Edit는 디스크에 정상 반영돼 있어 재작업 불필요했음(호출자는 항상 파일 상태를 직접 재확인해야 함 — 에이전트의 "완료 보고" 유무와 무관하게 실제 변경사항은 지속됨).

**전체 재추출 라운드(사용자 지시 — "대조작업으로 반드시 디자인과 똑같이 구현", 담당자 frontend-engineer 고정)**:
1. Auth 배경 오브제(BgPixels/ConfettiFooter/DashedEllipse): 좌표 미문서화 발견 → Figma 재실측 후 `docs/design/graphic-assets.md`에 append, 구현. 부수 발견: `.auth-page` 배경이 근거 없이 그라디언트였음(원래 단색 sky-500) — 정정.
2. 사용자 직접 지적 3건(로고 누락/눈 아이콘 이모지/버튼 위 배치 오류) 포함 전면 재점검 → 실제로는 더 광범위: pwreset1/2 로고 텍스트가 단계 라벨로 완전 대체(로고 소실), 이모지 아이콘 18곳 산재, 로그인폼 CSS order가 6형제 중 2개에만 지정돼 순서 뒤집힘. 전부 Figma 재조회 후 실제 SVG/order 수정. 문서화 갭 없음.
3. CSS 파일 분리: `static/styles.css`(1010줄) → `static/css/{tokens,layout,buttons,inputs,cards,modals,toasts}.css` 7개.
4. 전체 화면 재스크린샷, 회귀 114 passed 확인.

**design-qa 정식 대조 검수 결과 4건 + 최종 처리**:
1. **MEDIUM2(Pydantic 영문 메시지)**: backend-engineer가 `backend/main.py`에 `RequestValidationError` 전역 핸들러 추가, 필드별(아이디/비밀번호/전화번호/연락처이름/카테고리이름) 한글 메시지 매핑, 422 유지, 회귀 없음 — **완료**.
2. **HIGH1(Join vs login 미분화)**: frontend-engineer 재조사 결과, Figma상 실제 차이(체크박스+링크 행 유무, CTA 라벨 스왑)를 반영하려면 SCR-001 통합 화면 설계와 `tests/test_auth.py`의 고정 로케이터를 깨야 하는 구조적 충돌 발견 → 사용자에게 보고, **"통합 구조 유지, 변경 없음"으로 최종 결정받음 — 종결**.
3. **HIGH2(로고 8+ 화면 렌더링 실패)**: frontend-engineer가 로고 마크업 4곳이 재사용되는 11개 이상 상태를 전부 직접 순회 검증했으나 재현 실패(전부 정상). **design-pl 쪽 구체적 재현 조건(스크린샷/화면 상태) 회신 대기 중 — 미종결**.
4. **MEDIUM1(카테고리 삭제거부 배너 스크린샷 누락)**: 실제로는 파일이 이미 존재했음(`category-07-사용중삭제거부.png`) — design-qa가 놓쳤거나 스테일. 기능은 정상이나 테스트의 느슨한 `wait_for("2건")` 대기 조건 때문에 전체 스위트 동시 실행 시 조기 캡처되는 flaky 발견(코드 버그 아님, 테스트 미수정) → 보조 스크린샷(`category-07b-*.png`) 추가 — **완료(설명 첨부)**.

**missing-screens.md 문서 갱신**: 4/5/6/7번에 "프론트 반영" 확인 노트를 dev-pl이 직접 추가(design-pl 병렬 편집으로 파일 동시수정 충돌 1회 → 재읽기 후 재작성으로 해결).

**후속 필요 사항(사용자/코디네이터 판단 대기)**:
1. HIGH2(로고 렌더링) — design-pl의 구체적 재현 조건 회신 대기 중. 회신 오면 그 조건으로 frontend-engineer 재조사.
2. Button 리딩 아이콘 슬롯 미구현, 로그인 체크박스 네이티브 스타일 미커스터마이즈 — 발견만, 미처리.
3. `docs/planning/02` §4 SCR-003 표의 "새 이름 입력(prompt)" 서술 — 커스텀 모달 구현과 불일치, planning 팀 후속 정정 필요.
4. code-reviewer가 반복 지적한 이중 제출 가드 일관성 부족 — 후속 후보.
5. 검색 필터 시 사이드바 카테고리 카운트 0 표시 — 의도 여부 확인 필요.
6. git commit/push는 이번 라운드에서 하지 않음(dev-pl 권한 밖).
7. **하네스**: qa-engineer 재검증은 단위/통합 분리 + `docs/test-reports/` 문서화가 기본 절차. "디자인 확정 대기" 항목은 qa-engineer에게 Figma 구조를 먼저 조사시킨 뒤 테스트를 선작성(TDD red)하는 순서 유지. 에이전트가 세션 한도 등으로 중간에 끊겨도, 실제 파일 변경은 디스크에 남으므로 재작업 전 항상 직접 재확인.

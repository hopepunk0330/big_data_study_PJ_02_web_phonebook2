# 통합 테스트(E2E) 실행 보고서 — 2026-07-17 (최종 확인 라운드)

## 실행 정보
- 배경: 카테고리 삭제확인/이름수정 모달(4/6번) 구현 완료 후 오늘 최종 확인 라운드. 특히
  `test_categories.py`의 SCR-003 E2E 5개(scr003_03/04/05/06/07)가 새 모달 패턴(이름수정 —
  `prompt()` 대신 실제 모달, 삭제 — 확인 모달)으로 바뀐 뒤에도 GREEN인지 집중 확인.
- 백엔드: `127.0.0.1:8000` uvicorn(본 라운드 시작 시 다운돼 있어 QA가 `.venv/bin/uvicorn`으로
  재기동), 프론트: `backend/main.py`가 `../static`(`static/index.html`)를 서빙 — 별도 프론트
  서버 없이 같은 8000 포트에서 화면까지 제공.
- 실행 일시: 2026-07-17

## 1. `test_tc_e2e_*` (Playwright 브라우저, chromium)
- 실행 명령: `.venv/bin/python -m pytest tests/ -k "test_tc_e2e" -v --durations=0`
- **수집: 119개 중 38개 선택**(나머지 81개는 `test_tc_api_*`/`test_tc_iso_*`/`test_tc_persist_*`
  등으로 deselect)
- **통과 38 / 실패 0**
- 소요 시간: **28.51s**

| 파일 | 화면 | 통과 | 실패 |
|---|---|---|---|
| tests/test_auth.py | SCR-001(로그인/회원가입) 7 + SCR-004(비밀번호 재설정) 6 + SCR-900(공통 알림) 5 | 18 | 0 |
| tests/test_categories.py | SCR-003(카테고리 관리) 8 | 8 | 0 |
| tests/test_contacts.py | SCR-002(연락처 목록/추가/수정/삭제) 12 | 12 | 0 |
| **합계** | | **38** | **0** |

### SCR-003 신규 모달 집중 확인 (재검증 대상)
`test_categories.py`만 별도로 재실행(`-k "test_tc_e2e" -v`)해 8개 전체 개별 PASSED 확인:

| 테스트 | 내용 | 결과 |
|---|---|---|
| test_tc_e2e_scr003_01_add_category_refreshes_list_and_dropdown | 카테고리 추가 | PASSED |
| test_tc_e2e_scr003_02_add_duplicate_name_shows_detail | 중복 이름 추가 거부 | PASSED |
| test_tc_e2e_scr003_03_rename_via_prompt_refreshes_all_related_views | **이름수정 모달** → 저장 시 관련 화면 전체 반영 | PASSED |
| test_tc_e2e_scr003_04_rename_modal_cancel_no_api_call | **이름수정 모달** 취소 시 API 미호출 | PASSED |
| test_tc_e2e_scr003_05_delete_unused_category_confirm_removes_it | **삭제확인 모달** → 미사용 카테고리 삭제 | PASSED |
| test_tc_e2e_scr003_06_delete_in_use_category_confirm_shows_detail_not_removed | **삭제확인 모달** → 사용중 카테고리 삭제 거부 상세 표시 | PASSED |
| test_tc_e2e_scr003_07_delete_confirm_cancel_no_change | **삭제확인 모달** 취소 시 변경 없음 | PASSED |
| test_tc_e2e_scr003_08_session_expiry_forces_login_screen | 세션 만료 시 로그인 화면 강제 전환 | PASSED |

→ 새 모달 패턴(구 `prompt()`/`confirm()` 브라우저 네이티브 다이얼로그 대체) 도입 후에도 5개
(03/04/05/06/07) 전부 GREEN, 회귀 없음.

## 2. `tests/test_persistence.py` (TC-PERSIST, 자체 uvicorn 서브프로세스 관리 — 단독 실행)
- 실행 명령: `set -a && source .env && set +a && .venv/bin/python -m pytest tests/test_persistence.py -v --durations=0`
  (`.env` 미source 시 서브프로세스가 `KeyError: DATABASE_URL`로 즉시 죽는 환경 이슈가 있어
  반드시 이 방식으로 단독 실행)
- **통과 4 / 실패 0**
- 소요 시간: **4.51s**

| 테스트 | 내용 | 결과 |
|---|---|---|
| test_tc_persist_01_server_restart_keeps_contacts_and_categories | 서버 재기동 후 연락처/카테고리 데이터 유지 | PASSED |
| test_tc_persist_02_db_container_restart_keeps_data_without_server_restart | DB 컨테이너(`pg-lab`) 재시작 후 서버 재기동 없이도 데이터 유지 | PASSED |
| test_tc_persist_03_server_restart_keeps_login_session_via_existing_cookie | 서버 재기동 후 기존 쿠키로 세션 유지 | PASSED |
| test_tc_persist_04_revisit_with_same_cookies_shows_management_screen_immediately | 동일 쿠키로 재방문 시 즉시 관리 화면 표시(Playwright `page`) | PASSED |

## 합계
- **E2E + PERSIST 총 42개 실행 / 42 통과 / 0 실패**

## 실패 케이스
없음(전부 GREEN).

## 서버/인프라 확인
- 라운드 시작 시 `curl http://127.0.0.1:8000/docs` → 000(다운) 확인 후
  `.venv/bin/uvicorn main:app --host 127.0.0.1 --port 8000`로 재기동, 이후 200 확인.
- `docker ps` — `pg-lab`(postgres:16) 기동 중 확인. TC-PERSIST-02가 `pg-lab`을 재시작하므로
  전체 스위트 종료 후에도 `pg-lab Up 7 seconds`, 서버 `curl` 200으로 정상 상태 재확인.

## 스크린샷
- `docs/screenshot/` 총 **74장**(개수 불변) — 파일명이 "화면+스텝순번" 고정 컨벤션이라 재실행 시
  개수가 늘지 않고 기존 파일이 최신 캡처로 덮어써짐. `category-01~10-*.png`(SCR-003, 신규 모달
  포함) 10장 모두 이번 실행분으로 갱신 확인.

## 참고
- 이전 라운드까지 알려졌던 SCR-003 E2E 8건 실패(프론트 미기동), placeholder/버튼 strict mode
  violation 11건은 이번 실행에서도 재현되지 않음.
- 이 보고서는 `test_tc_api_*`/`test_tc_iso_*`(순수 단위 테스트)를 포함하지 않는다 — 해당 결과는
  `docs/test-reports/unit-2026-07-17.md` 참고.

## 이력(같은 날 이전 실행)
- 이전 실행(카테고리 모달 구현 전): E2E 38 + PERSIST 4 = 42개 GREEN. 이번 최종 확인 라운드도
  동일 수치(42 GREEN) — 모달 도입 후 회귀 없음, SCR-003 5개 개별 재검증까지 완료.

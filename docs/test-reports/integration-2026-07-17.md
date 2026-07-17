# 통합 테스트(E2E) 실행 보고서 — 2026-07-17

## 실행 정보
- 백엔드: `127.0.0.1:8000` uvicorn(본 라운드 시작 시 다운되어 있어 QA가 `.venv/bin/uvicorn`으로
  재기동 후 실행), 프론트: `backend/main.py`가 `../static`(`static/index.html`)를 서빙하는 구조 —
  별도 프론트 서버 없이 같은 8000 포트에서 화면까지 제공됨.
- 실행 일시: 2026-07-17

## 1. `test_tc_e2e_*` (Playwright 브라우저, chromium)
- 실행 명령: `.venv/bin/python -m pytest tests/ -k "test_tc_e2e" -v --durations=0`
- **수집: 119개 중 38개 선택**(나머지 81개는 `test_tc_api_*`/`test_tc_persist_*`/기타로 deselect)
- **통과 38 / 실패 0**
- 소요 시간: **33.12s**

| 파일 | 화면 | 통과 | 실패 |
|---|---|---|---|
| tests/test_auth.py | SCR-001(로그인/회원가입) 7 + SCR-004(비밀번호 재설정) 6 + SCR-900(공통 알림) 5 | 18 | 0 |
| tests/test_categories.py | SCR-003(카테고리 관리) 8 | 8 | 0 |
| tests/test_contacts.py | SCR-002(연락처 목록/추가/수정/삭제) 12 | 12 | 0 |
| **합계** | | **38** | **0** |

## 2. `tests/test_persistence.py` (TC-PERSIST, 자체 uvicorn 서브프로세스 관리 — 단독 실행)
- 실행 명령: `set -a && source .env && set +a && .venv/bin/python -m pytest tests/test_persistence.py -v --durations=0`
  (`.env` 미source 시 서브프로세스가 `KeyError: DATABASE_URL`로 즉시 죽는 환경 이슈가 있어
  반드시 이 방식으로 단독 실행)
- **통과 4 / 실패 0**
- 소요 시간: **5.34s**

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

## 스크린샷
- `docs/screenshot/` 총 **74장** 존재(모두 이번 실행으로 갱신됨 — 파일명이 "화면+스텝순번"으로
  고정돼 있어 재실행 시 개수가 늘지 않고 동일 파일이 최신 캡처로 덮어써짐, `mtime` 확인으로
  이번 실행분임을 확인함). 신규로 추가된 파일 0장(기존 컨벤션 파일명 그대로 재사용).
- `test_tc_persist_01~03`은 `APIRequestContext`만 사용해 화면이 없어 스크린샷 대상 제외,
  `test_tc_persist_04`만 `page` 기반이라 캡처 포함.

## 참고
- 이전 라운드까지 알려졌던 SCR-003 E2E 8건 실패(프론트 미기동), placeholder/버튼 strict mode
  violation 11건은 모두 이번 실행에서 재현되지 않음 — frontend 구현 완료 + 로케이터 정밀화가
  최신 상태로 유지되고 있음을 재확인.
- 이 보고서는 `test_tc_api_*`(순수 API 단위 테스트)를 포함하지 않는다 — 해당 결과는
  `docs/test-reports/unit-2026-07-17.md` 참고.

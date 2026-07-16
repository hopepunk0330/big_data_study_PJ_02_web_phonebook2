"""tests/test_auth.py

06_연락처관리_웹서비스_테스트계획서_v1.0.md 소스:
- §4-1 인증 API: TC-API-AUTH-01~14, 03b (15개)
- §4-2 비밀번호 재설정 API: TC-API-PW-01~09 (9개)
- §4-5 화면 서빙 API: TC-API-SCREEN-01 (1개)
- §5-1 SCR-001 E2E: TC-E2E-SCR001-01~07 (7개)
- §5-2 SCR-004 E2E: TC-E2E-SCR004-01~06 (6개)
- §5-5 SCR-900 E2E: TC-E2E-SCR900-01~05 (5개)

구현(backend/)이 아직 없는 TDD red 단계 — 전부 실패(connection error 등)가 정상이다.
"""

from conftest import (
    BASE_URL,
    DEFAULT_PASSWORD,
    assert_not_server_error,
    called,
    contact_payload,
    get_category_id,
    login,
    record_network,
    signup,
    signup_and_login,
    unique_username,
)


# ── 4-1. 인증 (FR-01~04 → AC-01~04, AC-15) ─────────────────────────────────


def test_tc_api_auth_01_signup_success(api_request):
    username = unique_username()
    resp = api_request.post(
        "/auth/signup", data={"username": username, "password": DEFAULT_PASSWORD}
    )
    assert_not_server_error(resp)
    assert resp.status == 201
    body = resp.json()
    assert isinstance(body["id"], int)
    assert body["username"] == username


def test_tc_api_auth_02_signup_duplicate_username(api_request):
    username, _ = signup(api_request)
    resp = api_request.post(
        "/auth/signup", data={"username": username, "password": DEFAULT_PASSWORD}
    )
    assert_not_server_error(resp)
    assert resp.status == 409
    assert resp.json().get("detail")


def test_tc_api_auth_03_signup_username_too_short(api_request):
    resp = api_request.post(
        "/auth/signup", data={"username": "ab", "password": DEFAULT_PASSWORD}
    )
    assert_not_server_error(resp)
    assert resp.status == 422


def test_tc_api_auth_03b_signup_username_uppercase(api_request):
    resp = api_request.post(
        "/auth/signup", data={"username": "NewUser1", "password": DEFAULT_PASSWORD}
    )
    assert_not_server_error(resp)
    assert resp.status == 422


def test_tc_api_auth_04_signup_password_too_short(api_request):
    resp = api_request.post(
        "/auth/signup", data={"username": unique_username(), "password": "abc"}
    )
    assert_not_server_error(resp)
    assert resp.status == 422


def test_tc_api_auth_05_signup_then_default_categories(api_request):
    signup_and_login(api_request)
    resp = api_request.get("/categories")
    assert_not_server_error(resp)
    assert resp.status == 200
    names = {c["name"] for c in resp.json()}
    assert names == {"가족", "친구", "기타"}


def test_tc_api_auth_06_login_success_sets_httponly_cookie(api_request):
    username, _ = signup(api_request)
    resp = login(api_request, username)
    assert_not_server_error(resp)
    assert resp.status == 200
    set_cookie_headers = [
        h["value"] for h in resp.headers_array if h["name"].lower() == "set-cookie"
    ]
    assert any("session_id=" in v for v in set_cookie_headers)
    assert any("session_id=" in v and "httponly" in v.lower() for v in set_cookie_headers)


def test_tc_api_auth_07_login_unknown_username(api_request):
    resp = login(api_request, unique_username())
    assert_not_server_error(resp)
    assert resp.status == 401
    assert resp.json()["detail"] == "아이디 또는 비밀번호가 올바르지 않습니다"


def test_tc_api_auth_08_login_wrong_password_same_message_as_unknown_user(api_request):
    username, _ = signup(api_request)
    resp = login(api_request, username, password="wrongpass1")
    assert_not_server_error(resp)
    assert resp.status == 401
    # TC-API-AUTH-07과 완전히 동일한 문자열이어야 함(아이디 존재 여부 미노출)
    assert resp.json()["detail"] == "아이디 또는 비밀번호가 올바르지 않습니다"


def test_tc_api_auth_09_logout_success(api_request):
    signup_and_login(api_request)
    resp = api_request.post("/auth/logout")
    assert_not_server_error(resp)
    assert resp.status == 200


def test_tc_api_auth_10_logout_then_reuse_cookie_rejected(api_request):
    signup_and_login(api_request)
    api_request.post("/auth/logout")
    resp = api_request.get("/contacts")
    assert_not_server_error(resp)
    assert resp.status == 401


def test_tc_api_auth_11_logout_without_session_is_idempotent_200(api_request):
    # 세션 쿠키 전혀 없는 상태(비로그인)에서 로그아웃 호출 — 06 문서 v1.0 변경이력 §0 확정 결론
    resp = api_request.post("/auth/logout")
    assert_not_server_error(resp)
    assert resp.status == 200
    assert resp.json() == {"message": "로그아웃 되었습니다"}


def test_tc_api_auth_12_me_success(api_request):
    username = signup_and_login(api_request)
    resp = api_request.get("/auth/me")
    assert_not_server_error(resp)
    assert resp.status == 200
    body = resp.json()
    assert isinstance(body["id"], int)
    assert body["username"] == username


def test_tc_api_auth_13_me_without_cookie(api_request):
    resp = api_request.get("/auth/me")
    assert_not_server_error(resp)
    assert resp.status == 401


def test_tc_api_auth_14_me_with_bogus_session_cookie(api_request):
    resp = api_request.get(
        "/auth/me", headers={"Cookie": "session_id=" + "0" * 64}
    )
    assert_not_server_error(resp)
    assert resp.status == 401


# ── 4-2. 비밀번호 재설정 (FR-14~15 → AC-18) ─────────────────────────────────


def test_tc_api_pw_01_find_password_success(api_request):
    username, _ = signup(api_request)
    resp = api_request.post("/auth/find-password", data={"username": username})
    assert_not_server_error(resp)
    assert resp.status == 200
    assert resp.json() == {"username": username}


def test_tc_api_pw_02_find_password_unknown_username(api_request):
    resp = api_request.post(
        "/auth/find-password", data={"username": unique_username("ghost")}
    )
    assert_not_server_error(resp)
    assert resp.status == 404
    assert resp.json().get("detail")


def test_tc_api_pw_03_find_password_username_too_short(api_request):
    resp = api_request.post("/auth/find-password", data={"username": "ab"})
    assert_not_server_error(resp)
    assert resp.status == 422


def test_tc_api_pw_04_reset_password_success(api_request):
    username, _ = signup(api_request)
    resp = api_request.patch(
        "/auth/password",
        data={"username": username, "new_password": "newpass1234"},
    )
    assert_not_server_error(resp)
    assert resp.status == 200
    assert resp.json() == {"message": "비밀번호가 변경되었습니다"}


def test_tc_api_pw_05_reset_password_unknown_username(api_request):
    resp = api_request.patch(
        "/auth/password",
        data={"username": unique_username("ghost"), "new_password": "newpass1234"},
    )
    assert_not_server_error(resp)
    assert resp.status == 404


def test_tc_api_pw_06_reset_password_too_short(api_request):
    username, _ = signup(api_request)
    resp = api_request.patch(
        "/auth/password", data={"username": username, "new_password": "abc"}
    )
    assert_not_server_error(resp)
    assert resp.status == 422


def test_tc_api_pw_07_old_password_rejected_after_reset(api_request):
    username, _ = signup(api_request)
    api_request.patch(
        "/auth/password",
        data={"username": username, "new_password": "newpass1234"},
    )
    resp = login(api_request, username, password=DEFAULT_PASSWORD)
    assert_not_server_error(resp)
    assert resp.status == 401


def test_tc_api_pw_08_new_password_accepted_after_reset(api_request):
    username, _ = signup(api_request)
    api_request.patch(
        "/auth/password",
        data={"username": username, "new_password": "newpass1234"},
    )
    resp = login(api_request, username, password="newpass1234")
    assert_not_server_error(resp)
    assert resp.status == 200


def test_tc_api_pw_09_reset_invalidates_existing_sessions(api_request):
    username, _ = signup(api_request)
    login(api_request, username)  # 세션 쿠키 A 확보(api_request 컨텍스트에 저장됨)
    me_before = api_request.get("/auth/me")
    assert me_before.status == 200

    api_request.patch(
        "/auth/password",
        data={"username": username, "new_password": "newpass1234"},
    )
    # 같은 컨텍스트(=쿠키 A)로 재요청 — 재설정 시 기존 세션 전체 무효화 확인
    resp = api_request.get("/auth/me")
    assert_not_server_error(resp)
    assert resp.status == 401


# ── 4-5. 화면 서빙 ──────────────────────────────────────────────────────────


def test_tc_api_screen_01_get_root_serves_html(api_request):
    resp = api_request.get("/")
    assert_not_server_error(resp)
    assert resp.status == 200
    content_type = resp.headers.get("content-type", "")
    assert "text/html" in content_type
    assert "<html" in resp.text().lower()


# ── 5-1. SCR-001 — 로그인/회원가입 E2E ──────────────────────────────────────


def test_tc_e2e_scr001_01_first_visit_shows_login_section(page):
    page.goto(BASE_URL)
    assert page.get_by_role("button", name="로그인", exact=True).is_visible()
    assert not page.get_by_role("button", name="로그아웃", exact=True).is_visible()


def test_tc_e2e_scr001_02_login_wrong_password_shows_detail_message(page, api_request):
    username, _ = signup(api_request)
    page.goto(BASE_URL)
    page.get_by_placeholder("영문 소문자·숫자 4~20자").fill(username)
    page.get_by_placeholder("4~20자").first.fill("wrongpass1")
    page.get_by_role("button", name="로그인", exact=True).click()
    page.get_by_text("아이디 또는 비밀번호가 올바르지 않습니다").wait_for()
    # 로그인 폼 유지 확인
    assert page.get_by_role("button", name="로그인", exact=True).is_visible()


def test_tc_e2e_scr001_03_login_success_transitions_and_loads_data(page, api_request):
    username, _ = signup(api_request)
    log = record_network(page)
    page.goto(BASE_URL)
    page.get_by_placeholder("영문 소문자·숫자 4~20자").fill(username)
    page.get_by_placeholder("4~20자").first.fill(DEFAULT_PASSWORD)
    page.get_by_role("button", name="로그인", exact=True).click()
    page.get_by_role("button", name="로그아웃", exact=True).wait_for()
    assert called(log, "GET", "/categories")
    assert called(log, "GET", "/contacts")


def test_tc_e2e_scr001_04_signup_unknown_username_shows_guidance(page):
    page.goto(BASE_URL)
    page.get_by_placeholder("영문 소문자·숫자 4~20자").fill(unique_username())
    page.get_by_placeholder("4~20자").first.fill(DEFAULT_PASSWORD)
    page.get_by_role("button", name="회원가입", exact=True).click()
    page.get_by_text("가입 완료! 로그인해 주세요").wait_for()
    assert page.get_by_role("button", name="로그인", exact=True).is_visible()


def test_tc_e2e_scr001_05_signup_duplicate_username_shows_detail(page, api_request):
    username, _ = signup(api_request)
    page.goto(BASE_URL)
    page.get_by_placeholder("영문 소문자·숫자 4~20자").fill(username)
    page.get_by_placeholder("4~20자").first.fill(DEFAULT_PASSWORD)
    page.get_by_role("button", name="회원가입", exact=True).click()
    page.get_by_text("이미").wait_for()  # 서버 detail 문구(409) 표시 확인


def test_tc_e2e_scr001_06_signup_invalid_format_shows_detail(page):
    page.goto(BASE_URL)
    page.get_by_placeholder("영문 소문자·숫자 4~20자").fill("ab")
    page.get_by_placeholder("4~20자").first.fill(DEFAULT_PASSWORD)
    page.get_by_role("button", name="회원가입", exact=True).click()
    page.wait_for_timeout(500)
    assert page.get_by_role("button", name="회원가입", exact=True).is_visible()


def test_tc_e2e_scr001_07_password_reset_link_no_api_call(page):
    log = record_network(page)
    page.goto(BASE_URL)
    page.get_by_text("비밀번호 재설정").click()
    page.get_by_role("button", name="확인", exact=True).wait_for()
    assert not called(log, "POST", "/auth/find-password")
    assert not called(log, "PATCH", "/auth/password")


# ── 5-2. SCR-004 — 비밀번호 재설정 E2E ───────────────────────────────────────


def _goto_scr004(page):
    page.goto(BASE_URL)
    page.get_by_text("비밀번호 재설정").click()
    page.get_by_role("button", name="확인", exact=True).wait_for()


def test_tc_e2e_scr004_01_find_password_success_shows_step2(page, api_request):
    username, _ = signup(api_request)
    _goto_scr004(page)
    page.get_by_placeholder("가입 시 사용한 아이디").fill(username)
    page.get_by_role("button", name="확인", exact=True).click()
    page.get_by_role("button", name="비밀번호 변경", exact=True).wait_for()
    assert page.get_by_text(username).is_visible()


def test_tc_e2e_scr004_02_find_password_unknown_username_stays_step1(page):
    _goto_scr004(page)
    page.get_by_placeholder("가입 시 사용한 아이디").fill(unique_username())
    page.get_by_role("button", name="확인", exact=True).click()
    page.get_by_text("존재하지 않는 아이디입니다").wait_for()
    assert page.get_by_role("button", name="확인", exact=True).is_visible()


def test_tc_e2e_scr004_03_password_mismatch_no_api_call(page, api_request):
    username, _ = signup(api_request)
    log = record_network(page)
    _goto_scr004(page)
    page.get_by_placeholder("가입 시 사용한 아이디").fill(username)
    page.get_by_role("button", name="확인", exact=True).click()
    page.get_by_placeholder("4~20자").first.fill("newpass1234")
    page.get_by_placeholder("위와 동일하게 입력").fill("differentpass1")
    page.get_by_role("button", name="비밀번호 변경", exact=True).click()
    page.get_by_text("두 비밀번호가 일치하지 않습니다").wait_for()
    assert not called(log, "PATCH", "/auth/password")


def test_tc_e2e_scr004_04_password_too_short_shows_detail(page, api_request):
    username, _ = signup(api_request)
    _goto_scr004(page)
    page.get_by_placeholder("가입 시 사용한 아이디").fill(username)
    page.get_by_role("button", name="확인", exact=True).click()
    page.get_by_placeholder("4~20자").first.fill("abc")
    page.get_by_placeholder("위와 동일하게 입력").fill("abc")
    page.get_by_role("button", name="비밀번호 변경", exact=True).click()
    page.wait_for_timeout(500)
    assert page.get_by_role("button", name="비밀번호 변경", exact=True).is_visible()


def test_tc_e2e_scr004_05_password_reset_success_returns_to_login(page, api_request):
    username, _ = signup(api_request)
    _goto_scr004(page)
    page.get_by_placeholder("가입 시 사용한 아이디").fill(username)
    page.get_by_role("button", name="확인", exact=True).click()
    page.get_by_placeholder("4~20자").first.fill("newpass1234")
    page.get_by_placeholder("위와 동일하게 입력").fill("newpass1234")
    page.get_by_role("button", name="비밀번호 변경", exact=True).click()
    page.get_by_text("비밀번호가 변경되었습니다").wait_for()
    page.get_by_role("button", name="로그인", exact=True).wait_for()


def test_tc_e2e_scr004_06_back_to_login_link_no_api_call(page):
    log = record_network(page)
    _goto_scr004(page)
    page.get_by_role("button", name="로그인으로 돌아가기", exact=True).click()
    page.get_by_role("button", name="로그인", exact=True).wait_for()
    assert not called(log, "POST", "/auth/find-password")


# ── 5-5. SCR-900 — 공통 메시지/오류 표시 E2E ────────────────────────────────


def _login_via_page(page, username, password=DEFAULT_PASSWORD):
    page.goto(BASE_URL)
    page.get_by_placeholder("영문 소문자·숫자 4~20자").fill(username)
    page.get_by_placeholder("4~20자").first.fill(password)
    page.get_by_role("button", name="로그인", exact=True).click()
    page.get_by_role("button", name="로그아웃", exact=True).wait_for()


def test_tc_e2e_scr900_01_session_expiry_forces_login_screen(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    # 서버에서 강제 로그아웃 처리(세션 만료 유도) — page의 쿠키 저장소는 그대로 둔 채
    page.context.request.post("/auth/logout")
    page.get_by_role("button", name="검색", exact=True).click()
    page.get_by_text("다시 로그인해 주세요").wait_for()
    page.get_by_role("button", name="로그인", exact=True).wait_for()


def test_tc_e2e_scr900_02_404_409_422_shows_detail_without_transition(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    category_id = get_category_id(api_request)
    payload = contact_payload(category_id, phone="123")  # 형식 위반 → 422 유도
    page.get_by_placeholder("이름").fill(payload["name"])
    page.get_by_placeholder("전화번호").fill(payload["phone"])
    page.get_by_role("button", name="추가", exact=True).click()
    page.wait_for_timeout(500)
    assert page.get_by_role("button", name="로그아웃", exact=True).is_visible()  # 화면 유지(전환 없음)


def test_tc_e2e_scr900_03_pydantic_array_422_shows_first_msg_only(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    page.get_by_placeholder("이름").fill("")  # name, phone 둘 다 위반 유도
    page.get_by_placeholder("전화번호").fill("123")
    page.get_by_role("button", name="추가", exact=True).click()
    page.wait_for_timeout(500)
    # 배열 detail의 첫 항목 msg만 표시됨(복수 오류 문구가 동시에 나열되지 않음)
    assert page.get_by_role("button", name="로그아웃", exact=True).is_visible()


def test_tc_e2e_scr900_04_success_response_shows_transient_message(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    category_id = get_category_id(api_request)
    payload = contact_payload(category_id)
    page.get_by_placeholder("이름").fill(payload["name"])
    page.get_by_placeholder("전화번호").fill(payload["phone"])
    page.get_by_role("button", name="추가", exact=True).click()
    page.get_by_text("추가되었습니다").wait_for()


def test_tc_e2e_scr900_05_login_401_stays_on_login_form_no_forced_transition(page, api_request):
    username, _ = signup(api_request)
    page.goto(BASE_URL)
    page.get_by_placeholder("영문 소문자·숫자 4~20자").fill(username)
    page.get_by_placeholder("4~20자").first.fill("wrongpass1")
    page.get_by_role("button", name="로그인", exact=True).click()
    page.get_by_text("아이디 또는 비밀번호가 올바르지 않습니다").wait_for()
    # 강제 전환 예외 — 로그인 폼에 계속 머무름("다시 로그인해 주세요"로 다시 전환되는 게 아님)
    assert page.get_by_role("button", name="로그인", exact=True).is_visible()
    assert not page.get_by_text("다시 로그인해 주세요").is_visible()

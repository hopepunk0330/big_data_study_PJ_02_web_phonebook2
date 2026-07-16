"""tests/test_contacts.py

06_연락처관리_웹서비스_테스트계획서_v1.0.md 소스:
- §4-3 연락처 API: TC-API-CONTACT-01~27, 07b (28개)
- §5-3 SCR-002 E2E: TC-E2E-SCR002-01~12 (12개)
- §6 데이터 격리: TC-ISO-01~06 (6개)

구현(backend/)이 아직 없는 TDD red 단계 — 전부 실패(connection error 등)가 정상이다.
"""

from conftest import (
    BASE_URL,
    DEFAULT_PASSWORD,
    assert_not_server_error,
    called,
    contact_payload,
    get_category_id,
    record_network,
    signup,
    signup_and_login,
    unique_category_name,
    unique_phone,
    unique_username,
)


# ── 4-3. 연락처 (FR-05~08 → AC-05~09, AC-13, AC-14) ─────────────────────────


def test_tc_api_contact_01_create_success_includes_category_name(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request, "친구")
    resp = api_request.post("/contacts", data=contact_payload(category_id))
    assert_not_server_error(resp)
    assert resp.status == 201
    assert resp.json()["category_name"]


def test_tc_api_contact_02_create_without_session(api_request):
    signup(api_request)  # 가입만 하고 로그인은 하지 않음
    resp = api_request.post("/contacts", data=contact_payload(1))
    assert_not_server_error(resp)
    assert resp.status == 401


def test_tc_api_contact_03_create_nonexistent_category(api_request):
    signup_and_login(api_request)
    resp = api_request.post("/contacts", data=contact_payload(999999))
    assert_not_server_error(resp)
    assert resp.status == 404


def test_tc_api_contact_04_create_duplicate_phone_same_user(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    phone = unique_phone()
    api_request.post("/contacts", data=contact_payload(category_id, phone=phone))
    resp = api_request.post("/contacts", data=contact_payload(category_id, phone=phone))
    assert_not_server_error(resp)
    assert resp.status == 409


def test_tc_api_contact_05_same_phone_allowed_across_different_users(api_request, playwright):
    signup_and_login(api_request)
    category_a = get_category_id(api_request)
    phone = unique_phone()
    resp_a = api_request.post("/contacts", data=contact_payload(category_a, phone=phone))
    assert resp_a.status == 201

    ctx_b = playwright.request.new_context(base_url=BASE_URL)
    try:
        signup_and_login(ctx_b)
        category_b = get_category_id(ctx_b)
        resp_b = ctx_b.post("/contacts", data=contact_payload(category_b, phone=phone))
        assert_not_server_error(resp_b)
        assert resp_b.status == 201
    finally:
        ctx_b.dispose()


def test_tc_api_contact_06_name_too_long(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    resp = api_request.post("/contacts", data=contact_payload(category_id, name="가나다라마바"))
    assert_not_server_error(resp)
    assert resp.status == 422


def test_tc_api_contact_07_name_empty(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    resp = api_request.post("/contacts", data=contact_payload(category_id, name=""))
    assert_not_server_error(resp)
    assert resp.status == 422


def test_tc_api_contact_07b_name_boundary_1_and_5_chars_valid(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    resp_1 = api_request.post("/contacts", data=contact_payload(category_id, name="윤"))
    resp_5 = api_request.post("/contacts", data=contact_payload(category_id, name="가나다라마"))
    assert_not_server_error(resp_1)
    assert_not_server_error(resp_5)
    assert resp_1.status == 201
    assert resp_5.status == 201


def test_tc_api_contact_08_phone_with_hyphen(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    resp = api_request.post(
        "/contacts", data=contact_payload(category_id, phone="010-1234-5678")
    )
    assert_not_server_error(resp)
    assert resp.status == 422


def test_tc_api_contact_09_phone_with_letters(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    resp = api_request.post(
        "/contacts", data=contact_payload(category_id, phone="010abcdefgh")
    )
    assert_not_server_error(resp)
    assert resp.status == 422


def test_tc_api_contact_10_phone_wrong_prefix_011(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    resp = api_request.post(
        "/contacts", data=contact_payload(category_id, phone="01112345678")
    )
    assert_not_server_error(resp)
    assert resp.status == 422


def test_tc_api_contact_11_phone_completely_invalid(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    resp = api_request.post("/contacts", data=contact_payload(category_id, phone="123"))
    assert_not_server_error(resp)
    assert resp.status == 422


def test_tc_api_contact_12_list_returns_total_and_items(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    for _ in range(3):
        api_request.post("/contacts", data=contact_payload(category_id))
    resp = api_request.get("/contacts")
    assert_not_server_error(resp)
    assert resp.status == 200
    body = resp.json()
    assert body["total"] == 3
    assert len(body["items"]) == 3


def test_tc_api_contact_13_list_without_session(api_request):
    resp = api_request.get("/contacts")
    assert_not_server_error(resp)
    assert resp.status == 401


def test_tc_api_contact_14_search_by_name_returns_both_duplicates(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    r1 = api_request.post("/contacts", data=contact_payload(category_id, name="윤아"))
    r2 = api_request.post("/contacts", data=contact_payload(category_id, name="윤아"))
    resp = api_request.get("/contacts", params={"name": "윤아"})
    assert_not_server_error(resp)
    assert resp.status == 200
    body = resp.json()
    assert body["total"] == 2
    ids = {item["id"] for item in body["items"]}
    assert ids == {r1.json()["id"], r2.json()["id"]}


def test_tc_api_contact_15_search_no_match_returns_empty_not_error(api_request):
    signup_and_login(api_request)
    resp = api_request.get("/contacts", params={"name": "존재안함"})
    assert_not_server_error(resp)
    assert resp.status == 200
    assert resp.json() == {"total": 0, "items": []}


def test_tc_api_contact_16_filter_by_category_id(api_request):
    signup_and_login(api_request)
    category_friend = get_category_id(api_request, "친구")
    category_family = get_category_id(api_request, "가족")
    api_request.post("/contacts", data=contact_payload(category_friend))
    api_request.post("/contacts", data=contact_payload(category_family))
    resp = api_request.get("/contacts", params={"category_id": category_friend})
    assert_not_server_error(resp)
    assert resp.status == 200
    body = resp.json()
    assert all(item["category_id"] == category_friend for item in body["items"])


def test_tc_api_contact_17_patch_addr_only_keeps_other_fields(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    created = api_request.post(
        "/contacts", data=contact_payload(category_id, addr="서울시")
    ).json()
    resp = api_request.patch(f"/contacts/{created['id']}", data={"addr": "제주시"})
    assert_not_server_error(resp)
    assert resp.status == 200
    body = resp.json()
    assert body["addr"] == "제주시"
    assert body["name"] == created["name"]
    assert body["phone"] == created["phone"]
    assert body["category_id"] == created["category_id"]


def test_tc_api_contact_18_patch_one_duplicate_name_does_not_affect_other(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    c1 = api_request.post(
        "/contacts", data=contact_payload(category_id, name="윤아", addr="서울시")
    ).json()
    c3 = api_request.post(
        "/contacts", data=contact_payload(category_id, name="윤아", addr="부산시")
    ).json()
    resp = api_request.patch(f"/contacts/{c1['id']}", data={"addr": "제주시"})
    assert_not_server_error(resp)
    assert resp.status == 200

    listing = api_request.get("/contacts").json()
    c3_after = next(item for item in listing["items"] if item["id"] == c3["id"])
    assert c3_after["addr"] == "부산시"


def test_tc_api_contact_19_patch_without_session(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    created = api_request.post("/contacts", data=contact_payload(category_id)).json()
    api_request.post("/auth/logout")
    resp = api_request.patch(f"/contacts/{created['id']}", data={"addr": "제주시"})
    assert_not_server_error(resp)
    assert resp.status == 401


def test_tc_api_contact_20_patch_nonexistent_id(api_request):
    signup_and_login(api_request)
    resp = api_request.patch("/contacts/999999", data={"addr": "제주시"})
    assert_not_server_error(resp)
    assert resp.status == 404


def test_tc_api_contact_21_patch_other_users_contact_returns_404(api_request, playwright):
    signup_and_login(api_request)
    category_a = get_category_id(api_request)
    contact_a = api_request.post("/contacts", data=contact_payload(category_a)).json()

    ctx_b = playwright.request.new_context(base_url=BASE_URL)
    try:
        signup_and_login(ctx_b)
        resp = ctx_b.patch(f"/contacts/{contact_a['id']}", data={"addr": "제주시"})
        assert_not_server_error(resp)
        assert resp.status == 404  # 403이 아니라 404(01문서 §5-2)
    finally:
        ctx_b.dispose()


def test_tc_api_contact_22_patch_phone_to_duplicate_of_own_contact(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    c1 = api_request.post("/contacts", data=contact_payload(category_id)).json()
    c2 = api_request.post("/contacts", data=contact_payload(category_id)).json()
    resp = api_request.patch(f"/contacts/{c1['id']}", data={"phone": c2["phone"]})
    assert_not_server_error(resp)
    assert resp.status == 409


def test_tc_api_contact_23_patch_name_empty(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    created = api_request.post("/contacts", data=contact_payload(category_id)).json()
    resp = api_request.patch(f"/contacts/{created['id']}", data={"name": ""})
    assert_not_server_error(resp)
    assert resp.status == 422


def test_tc_api_contact_24_delete_success_removes_from_list(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    created = api_request.post("/contacts", data=contact_payload(category_id)).json()
    resp = api_request.delete(f"/contacts/{created['id']}")
    assert_not_server_error(resp)
    assert resp.status == 204
    listing = api_request.get("/contacts").json()
    assert all(item["id"] != created["id"] for item in listing["items"])


def test_tc_api_contact_25_delete_one_duplicate_name_keeps_other(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    c1 = api_request.post("/contacts", data=contact_payload(category_id, name="윤아")).json()
    c3 = api_request.post("/contacts", data=contact_payload(category_id, name="윤아")).json()
    resp = api_request.delete(f"/contacts/{c1['id']}")
    assert_not_server_error(resp)
    assert resp.status == 204
    listing = api_request.get("/contacts").json()
    ids = {item["id"] for item in listing["items"]}
    assert c3["id"] in ids
    assert c1["id"] not in ids


def test_tc_api_contact_26_delete_without_session(api_request):
    signup_and_login(api_request)
    category_id = get_category_id(api_request)
    created = api_request.post("/contacts", data=contact_payload(category_id)).json()
    api_request.post("/auth/logout")
    resp = api_request.delete(f"/contacts/{created['id']}")
    assert_not_server_error(resp)
    assert resp.status == 401


def test_tc_api_contact_27_delete_other_users_contact_returns_404_and_survives(
    api_request, playwright
):
    signup_and_login(api_request)
    category_a = get_category_id(api_request)
    contact_a = api_request.post("/contacts", data=contact_payload(category_a)).json()

    ctx_b = playwright.request.new_context(base_url=BASE_URL)
    try:
        signup_and_login(ctx_b)
        resp = ctx_b.delete(f"/contacts/{contact_a['id']}")
        assert_not_server_error(resp)
        assert resp.status == 404
    finally:
        ctx_b.dispose()

    listing = api_request.get("/contacts").json()
    assert any(item["id"] == contact_a["id"] for item in listing["items"])


# ── 5-3. SCR-002 — 관리 화면(연락처 영역) E2E ───────────────────────────────


def _login_via_page(page, username, password=DEFAULT_PASSWORD):
    page.goto(BASE_URL)
    page.get_by_placeholder("영문 소문자·숫자 4~20자").fill(username)
    page.get_by_placeholder("4~20자").first.fill(password)
    page.get_by_role("button", name="로그인", exact=True).click()
    page.get_by_role("button", name="로그아웃", exact=True).wait_for()


def _total_count_text(page):
    return page.get_by_text("총").inner_text()


def test_tc_e2e_scr002_01_add_contact_clears_form_and_refreshes_list(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    before_total = api_request.get("/contacts").json()["total"]

    page.get_by_placeholder("이름").fill("윤아")
    page.get_by_placeholder("전화번호").fill(unique_phone())
    page.get_by_role("button", name="추가", exact=True).click()
    page.get_by_text("추가되었습니다").wait_for()

    assert page.get_by_placeholder("이름").input_value() == ""
    after_total = api_request.get("/contacts").json()["total"]
    assert after_total == before_total + 1


def test_tc_e2e_scr002_02_session_expiry_forces_login_screen(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    page.context.request.post("/auth/logout")  # 세션 만료 유도

    page.get_by_placeholder("이름").fill("윤아")
    page.get_by_placeholder("전화번호").fill(unique_phone())
    page.get_by_role("button", name="추가", exact=True).click()

    page.get_by_text("다시 로그인해 주세요").wait_for()
    page.get_by_role("button", name="로그인", exact=True).wait_for()


def test_tc_e2e_scr002_03_invalid_format_keeps_input_and_shows_detail(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)

    page.get_by_placeholder("이름").fill("윤아")
    page.get_by_placeholder("전화번호").fill("010-1234-5678")
    page.get_by_role("button", name="추가", exact=True).click()
    page.wait_for_timeout(500)

    assert page.get_by_placeholder("이름").input_value() == "윤아"
    assert page.get_by_role("button", name="로그아웃", exact=True).is_visible()  # 화면 안 멈춤


def test_tc_e2e_scr002_04_search_by_name_replaces_list(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    category_id = get_category_id(api_request)
    api_request.post("/contacts", data=contact_payload(category_id, name="윤아"))
    api_request.post("/contacts", data=contact_payload(category_id, name="윤아"))

    page.get_by_placeholder("이름 검색").fill("윤아")
    page.get_by_role("button", name="검색", exact=True).click()
    page.wait_for_timeout(500)
    assert page.get_by_text("윤아").count() >= 2


def test_tc_e2e_scr002_05_show_all_restores_full_list(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    page.get_by_placeholder("이름 검색").fill("존재안함")
    page.get_by_role("button", name="검색", exact=True).click()
    page.wait_for_timeout(300)
    page.get_by_role("button", name="전체", exact=True).click()
    page.wait_for_timeout(300)
    assert page.get_by_role("button", name="추가", exact=True).is_visible()


def test_tc_e2e_scr002_06_edit_button_opens_modal_without_api_call(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    category_id = get_category_id(api_request)
    created = api_request.post(
        "/contacts", data=contact_payload(category_id, name="윤아")
    ).json()
    page.reload()
    page.get_by_role("button", name="로그아웃", exact=True).wait_for()

    log = record_network(page)
    page.get_by_role("row", name=created["name"]).get_by_role("button", name="수정", exact=True).click()
    page.get_by_role("button", name="저장", exact=True).wait_for()
    assert not called(log, "PATCH", f"/contacts/{created['id']}")


def test_tc_e2e_scr002_07_edit_modal_save_updates_addr(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    category_id = get_category_id(api_request)
    created = api_request.post(
        "/contacts", data=contact_payload(category_id, name="윤아", addr="서울시")
    ).json()
    page.reload()
    page.get_by_role("button", name="로그아웃", exact=True).wait_for()

    page.get_by_role("row", name=created["name"]).get_by_role("button", name="수정", exact=True).click()
    page.get_by_placeholder("주소").fill("제주시")
    page.get_by_role("button", name="저장", exact=True).click()
    page.get_by_text("제주시").wait_for()


def test_tc_e2e_scr002_08_edit_modal_invalid_value_stays_open(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    category_id = get_category_id(api_request)
    created = api_request.post(
        "/contacts", data=contact_payload(category_id, name="윤아")
    ).json()
    page.reload()
    page.get_by_role("button", name="로그아웃", exact=True).wait_for()

    page.get_by_role("row", name=created["name"]).get_by_role("button", name="수정", exact=True).click()
    page.get_by_placeholder("전화번호").fill("010-1234-5678")
    page.get_by_role("button", name="저장", exact=True).click()
    page.wait_for_timeout(500)
    assert page.get_by_role("button", name="저장", exact=True).is_visible()  # 모달 유지


def test_tc_e2e_scr002_09_delete_cancel_confirm_no_change(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    category_id = get_category_id(api_request)
    created = api_request.post(
        "/contacts", data=contact_payload(category_id, name="윤아")
    ).json()
    page.reload()
    page.get_by_role("button", name="로그아웃", exact=True).wait_for()

    page.once("dialog", lambda dialog: dialog.dismiss())
    log = record_network(page)
    page.get_by_role("row", name=created["name"]).get_by_role("button", name="삭제", exact=True).click()
    page.wait_for_timeout(500)
    assert not called(log, "DELETE", f"/contacts/{created['id']}")
    assert page.get_by_text(created["name"]).is_visible()


def test_tc_e2e_scr002_10_delete_confirm_removes_row(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    category_id = get_category_id(api_request)
    created = api_request.post(
        "/contacts", data=contact_payload(category_id, name="윤아")
    ).json()
    page.reload()
    page.get_by_role("button", name="로그아웃", exact=True).wait_for()

    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("row", name=created["name"]).get_by_role("button", name="삭제", exact=True).click()
    page.wait_for_timeout(500)
    assert page.get_by_text(created["name"]).count() == 0


def test_tc_e2e_scr002_11_logout_button_transitions_to_login(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    page.get_by_role("button", name="로그아웃", exact=True).click()
    page.get_by_role("button", name="로그인", exact=True).wait_for()


def test_tc_e2e_scr002_12_double_click_add_sends_single_request(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)

    page.get_by_placeholder("이름").fill("윤아")
    page.get_by_placeholder("전화번호").fill(unique_phone())
    log = record_network(page)
    add_button = page.get_by_role("button", name="추가", exact=True)
    add_button.dblclick()
    page.wait_for_timeout(1000)
    post_count = sum(1 for entry in log if entry.startswith(f"POST {BASE_URL}/contacts"))
    assert post_count == 1


# ── 6. 데이터 격리 특수 케이스 (AC-13, AC-14) ────────────────────────────────


def test_tc_iso_01_list_excludes_other_users_contacts(api_request, playwright):
    signup_and_login(api_request)
    category_a = get_category_id(api_request)
    contact_a = api_request.post("/contacts", data=contact_payload(category_a)).json()

    ctx_b = playwright.request.new_context(base_url=BASE_URL)
    try:
        signup_and_login(ctx_b)
        resp = ctx_b.get("/contacts")
        assert_not_server_error(resp)
        assert resp.status == 200
        ids = {item["id"] for item in resp.json()["items"]}
        assert contact_a["id"] not in ids
    finally:
        ctx_b.dispose()


def test_tc_iso_02_search_by_other_users_name_returns_empty(api_request, playwright):
    signup_and_login(api_request)
    category_a = get_category_id(api_request)
    only_a_name = "가나다"
    api_request.post("/contacts", data=contact_payload(category_a, name=only_a_name))

    ctx_b = playwright.request.new_context(base_url=BASE_URL)
    try:
        signup_and_login(ctx_b)
        resp = ctx_b.get("/contacts", params={"name": only_a_name})
        assert_not_server_error(resp)
        assert resp.status == 200
        assert resp.json()["total"] == 0
    finally:
        ctx_b.dispose()


def test_tc_iso_03_patch_other_users_contact_id_returns_404(api_request, playwright):
    signup_and_login(api_request)
    category_a = get_category_id(api_request)
    contact_a = api_request.post("/contacts", data=contact_payload(category_a)).json()

    ctx_b = playwright.request.new_context(base_url=BASE_URL)
    try:
        signup_and_login(ctx_b)
        resp = ctx_b.patch(f"/contacts/{contact_a['id']}", data={"addr": "부산시"})
        assert_not_server_error(resp)
        assert resp.status == 404
    finally:
        ctx_b.dispose()


def test_tc_iso_04_delete_other_users_contact_id_returns_404_and_survives(
    api_request, playwright
):
    signup_and_login(api_request)
    category_a = get_category_id(api_request)
    contact_a = api_request.post("/contacts", data=contact_payload(category_a)).json()

    ctx_b = playwright.request.new_context(base_url=BASE_URL)
    try:
        signup_and_login(ctx_b)
        resp = ctx_b.delete(f"/contacts/{contact_a['id']}")
        assert_not_server_error(resp)
        assert resp.status == 404
    finally:
        ctx_b.dispose()

    listing = api_request.get("/contacts").json()
    assert any(item["id"] == contact_a["id"] for item in listing["items"])


def test_tc_iso_05_category_list_excludes_other_users_category(api_request, playwright):
    signup_and_login(api_request)
    category_name = unique_category_name("동호회")
    api_request.post("/categories", data={"name": category_name})

    ctx_b = playwright.request.new_context(base_url=BASE_URL)
    try:
        signup_and_login(ctx_b)
        resp = ctx_b.get("/categories")
        assert_not_server_error(resp)
        assert resp.status == 200
        names = {c["name"] for c in resp.json()}
        assert category_name not in names
        assert names == {"가족", "친구", "기타"}
    finally:
        ctx_b.dispose()


def test_tc_iso_06_create_contact_with_other_users_category_id_returns_404(
    api_request, playwright
):
    signup_and_login(api_request)
    category_a = get_category_id(api_request)

    ctx_b = playwright.request.new_context(base_url=BASE_URL)
    try:
        signup_and_login(ctx_b)
        resp = ctx_b.post("/contacts", data=contact_payload(category_a))
        assert_not_server_error(resp)
        assert resp.status == 404
    finally:
        ctx_b.dispose()

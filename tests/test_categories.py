"""tests/test_categories.py

06_연락처관리_웹서비스_테스트계획서_v1.0.md 소스:
- §4-4 카테고리 API: TC-API-CATEGORY-01~16, 07b (17개 — 06 문서 §4-1 "API 그룹 소계"
  줄은 "CATEGORY 16"이라 적었지만 실제 표에는 07b 행이 별도로 존재해 17개다.
  표(케이스 목록) 자체가 소스 오브 트루스이므로 표의 모든 행을 그대로 옮겼다.
  이 산술 불일치는 dev-pl에게 별도 보고)
- §5-4 SCR-003 E2E: TC-E2E-SCR003-01~08 (8개)

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
    unique_category_name,
)


# ── 4-4. 카테고리 (FR-09~12 → AC-10~12) ─────────────────────────────────────


def test_tc_api_category_01_list_default_three(api_request):
    signup_and_login(api_request)
    resp = api_request.get("/categories")
    assert_not_server_error(resp)
    assert resp.status == 200
    names = {c["name"] for c in resp.json()}
    assert names == {"가족", "친구", "기타"}


def test_tc_api_category_02_list_without_session(api_request):
    resp = api_request.get("/categories")
    assert_not_server_error(resp)
    assert resp.status == 401


def test_tc_api_category_03_create_success(api_request):
    signup_and_login(api_request)
    resp = api_request.post("/categories", data={"name": unique_category_name("동호회")})
    assert_not_server_error(resp)
    assert resp.status == 201


def test_tc_api_category_04_created_category_not_visible_to_other_user(
    api_request, playwright
):
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
    finally:
        ctx_b.dispose()


def test_tc_api_category_05_create_without_session(api_request):
    resp = api_request.post("/categories", data={"name": unique_category_name()})
    assert_not_server_error(resp)
    assert resp.status == 401


def test_tc_api_category_06_create_duplicate_name(api_request):
    signup_and_login(api_request)
    name = unique_category_name("동호회")
    api_request.post("/categories", data={"name": name})
    resp = api_request.post("/categories", data={"name": name})
    assert_not_server_error(resp)
    assert resp.status == 409


def test_tc_api_category_07_name_empty_and_too_long(api_request):
    signup_and_login(api_request)
    resp_empty = api_request.post("/categories", data={"name": ""})
    resp_too_long = api_request.post("/categories", data={"name": "가나다라마바사아자차카"})  # 11자
    assert_not_server_error(resp_empty)
    assert_not_server_error(resp_too_long)
    assert resp_empty.status == 422
    assert resp_too_long.status == 422


def test_tc_api_category_07b_name_boundary_1_and_10_chars_valid(api_request):
    signup_and_login(api_request)
    resp_1 = api_request.post("/categories", data={"name": unique_category_name("모")[:1]})
    resp_10 = api_request.post("/categories", data={"name": "가나다라마바사아자차"})  # 10자
    assert_not_server_error(resp_1)
    assert_not_server_error(resp_10)
    assert resp_1.status == 201
    assert resp_10.status == 201


def test_tc_api_category_08_rename_reflected_in_contact_category_name(api_request):
    signup_and_login(api_request)
    friend_id = get_category_id(api_request, "친구")
    api_request.post("/contacts", data=contact_payload(friend_id))
    resp = api_request.patch(f"/categories/{friend_id}", data={"name": "베프"})
    assert_not_server_error(resp)
    assert resp.status == 200

    listing = api_request.get("/contacts").json()
    assert all(item["category_name"] == "베프" for item in listing["items"])


def test_tc_api_category_09_patch_without_session(api_request):
    signup_and_login(api_request)
    friend_id = get_category_id(api_request, "친구")
    api_request.post("/auth/logout")
    resp = api_request.patch(f"/categories/{friend_id}", data={"name": "베프"})
    assert_not_server_error(resp)
    assert resp.status == 401


def test_tc_api_category_10_patch_nonexistent_id(api_request):
    signup_and_login(api_request)
    resp = api_request.patch("/categories/999999", data={"name": "베프"})
    assert_not_server_error(resp)
    assert resp.status == 404


def test_tc_api_category_11_rename_to_existing_name_conflict(api_request):
    signup_and_login(api_request)
    friend_id = get_category_id(api_request, "친구")
    resp = api_request.patch(f"/categories/{friend_id}", data={"name": "기타"})
    assert_not_server_error(resp)
    assert resp.status == 409


def test_tc_api_category_12_patch_name_empty(api_request):
    signup_and_login(api_request)
    friend_id = get_category_id(api_request, "친구")
    resp = api_request.patch(f"/categories/{friend_id}", data={"name": ""})
    assert_not_server_error(resp)
    assert resp.status == 422


def test_tc_api_category_13_delete_unused_category(api_request):
    signup_and_login(api_request)
    name = unique_category_name("동호회")
    created = api_request.post("/categories", data={"name": name}).json()
    resp = api_request.delete(f"/categories/{created['id']}")
    assert_not_server_error(resp)
    assert resp.status == 204
    names = {c["name"] for c in api_request.get("/categories").json()}
    assert name not in names


def test_tc_api_category_14_delete_without_session(api_request):
    signup_and_login(api_request)
    name = unique_category_name("동호회")
    created = api_request.post("/categories", data={"name": name}).json()
    api_request.post("/auth/logout")
    resp = api_request.delete(f"/categories/{created['id']}")
    assert_not_server_error(resp)
    assert resp.status == 401


def test_tc_api_category_15_delete_nonexistent_id(api_request):
    signup_and_login(api_request)
    resp = api_request.delete("/categories/999999")
    assert_not_server_error(resp)
    assert resp.status == 404


def test_tc_api_category_16_delete_in_use_category_rejected_with_count(api_request):
    signup_and_login(api_request)
    friend_id = get_category_id(api_request, "친구")
    api_request.post("/contacts", data=contact_payload(friend_id))
    api_request.post("/contacts", data=contact_payload(friend_id))

    resp = api_request.delete(f"/categories/{friend_id}")
    assert_not_server_error(resp)
    assert resp.status == 409
    assert "2건" in resp.json()["detail"]

    names = {c["name"] for c in api_request.get("/categories").json()}
    assert "친구" in names
    assert api_request.get("/contacts").json()["total"] == 2


# ── 5-4. SCR-003 — 관리 화면(카테고리 영역) E2E ──────────────────────────────


def _login_via_page(page, username, password=DEFAULT_PASSWORD):
    page.goto(BASE_URL)
    page.get_by_placeholder("영문 소문자·숫자 4~20자").fill(username)
    page.get_by_placeholder("4~20자").first.fill(password)
    page.get_by_role("button", name="로그인", exact=True).click()
    page.get_by_role("button", name="로그아웃", exact=True).wait_for()


def test_tc_e2e_scr003_01_add_category_refreshes_list_and_dropdown(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    name = unique_category_name("동호회")
    page.get_by_placeholder("새 카테고리").fill(name)
    page.screenshot(path="docs/screenshot/category-01-카테고리입력.png")
    page.get_by_role("button", name="추가", exact=True).nth(1).click()
    page.locator("#category-nav").get_by_text(name).wait_for()
    page.screenshot(path="docs/screenshot/category-02-추가완료.png")


def test_tc_e2e_scr003_02_add_duplicate_name_shows_detail(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    page.get_by_placeholder("새 카테고리").fill("친구")
    page.get_by_role("button", name="추가", exact=True).nth(1).click()
    page.wait_for_timeout(500)
    page.screenshot(path="docs/screenshot/category-03-중복추가유지.png")
    assert page.get_by_text("친구").count() >= 1  # detail(409) 표시, 목록엔 여전히 "친구" 1개뿐


def test_tc_e2e_scr003_03_rename_via_prompt_refreshes_all_related_views(page, api_request):
    username, _ = signup(api_request)
    login(api_request, username)
    category_id = get_category_id(api_request, "친구")
    api_request.post("/contacts", data=contact_payload(category_id, name="윤아"))
    _login_via_page(page, username)

    page.once("dialog", lambda dialog: dialog.accept("베프"))
    page.get_by_role("listitem", name="친구").get_by_role("button", name="수정", exact=True).click()
    page.locator("#category-nav").get_by_text("베프").wait_for()
    page.screenshot(path="docs/screenshot/category-04-이름변경완료.png")


def test_tc_e2e_scr003_04_rename_prompt_cancel_no_api_call(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    log = record_network(page)

    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("listitem", name="친구").get_by_role("button", name="수정", exact=True).click()
    page.wait_for_timeout(500)
    page.screenshot(path="docs/screenshot/category-05-이름변경취소유지.png")
    assert not any("/categories/" in entry and "PATCH" in entry for entry in log)


def test_tc_e2e_scr003_05_delete_unused_category_confirm_removes_it(page, api_request):
    username, _ = signup(api_request)
    login(api_request, username)
    _login_via_page(page, username)
    name = unique_category_name("동호회")
    api_request.post("/categories", data={"name": name})
    page.reload()
    page.get_by_role("button", name="로그아웃", exact=True).wait_for()

    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("listitem", name=name).get_by_role("button", name="삭제", exact=True).click()
    page.wait_for_timeout(500)
    page.screenshot(path="docs/screenshot/category-06-미사용삭제완료.png")
    assert page.get_by_text(name).count() == 0


def test_tc_e2e_scr003_06_delete_in_use_category_confirm_shows_detail_not_removed(
    page, api_request
):
    username, _ = signup(api_request)
    login(api_request, username)
    category_id = get_category_id(api_request, "친구")
    api_request.post("/contacts", data=contact_payload(category_id))
    api_request.post("/contacts", data=contact_payload(category_id))
    _login_via_page(page, username)

    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("listitem", name="친구").get_by_role("button", name="삭제", exact=True).click()
    page.get_by_text("2건").wait_for()
    page.screenshot(path="docs/screenshot/category-07-사용중삭제거부.png")
    assert page.get_by_text("친구").count() >= 1


def test_tc_e2e_scr003_07_delete_confirm_cancel_no_change(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    log = record_network(page)

    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("listitem", name="친구").get_by_role("button", name="삭제", exact=True).click()
    page.wait_for_timeout(500)
    page.screenshot(path="docs/screenshot/category-08-삭제취소유지.png")
    assert not any("/categories/" in entry and "DELETE" in entry for entry in log)
    assert page.locator("#category-manage-list").get_by_text("친구").is_visible()


def test_tc_e2e_scr003_08_session_expiry_forces_login_screen(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    page.context.request.post("/auth/logout")  # 세션 만료 유도

    page.get_by_placeholder("새 카테고리").fill(unique_category_name())
    page.screenshot(path="docs/screenshot/category-09-세션만료후입력.png")
    page.get_by_role("button", name="추가", exact=True).nth(1).click()

    page.get_by_role("button", name="로그인", exact=True).wait_for()
    page.screenshot(path="docs/screenshot/category-10-로그인화면복귀.png")

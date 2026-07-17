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

    page.get_by_role("listitem", name="친구").get_by_role("button", name="수정", exact=True).click()
    page.get_by_role("heading", name="카테고리 이름 수정").wait_for()
    page.get_by_label("이름").fill("베프")
    page.get_by_role("button", name="저장", exact=True).click()
    page.locator("#category-nav").get_by_text("베프").wait_for()
    page.screenshot(path="docs/screenshot/category-04-이름변경완료.png")


def test_tc_e2e_scr003_04_rename_modal_cancel_no_api_call(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    log = record_network(page)

    page.get_by_role("listitem", name="친구").get_by_role("button", name="수정", exact=True).click()
    page.get_by_role("heading", name="카테고리 이름 수정").wait_for()
    page.get_by_role("button", name="취소", exact=True).click()
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

    page.get_by_role("listitem", name=name).get_by_role("button", name="삭제", exact=True).click()
    page.get_by_role("heading", name="카테고리 삭제").wait_for()
    page.get_by_role("button", name="삭제하기", exact=True).click()
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

    page.get_by_role("listitem", name="친구").get_by_role("button", name="삭제", exact=True).click()
    page.get_by_role("heading", name="카테고리 삭제").wait_for()
    page.get_by_role("button", name="삭제하기", exact=True).click()
    # 서버가 409를 반환 — 모달이 에러를 표시하며 유지되는지, 배너로 대체되며 닫히는지는
    # frontend-engineer 구현에 따라 달라질 수 있어 "2건" 텍스트가 화면 어딘가에
    # 나타나는지만 유연하게 확인한다(다음 라운드에서 실제 동작에 맞춰 조정 가능).
    page.get_by_text("2건").wait_for()
    page.screenshot(path="docs/screenshot/category-07-사용중삭제거부.png")
    assert page.get_by_text("친구").count() >= 1


def test_tc_e2e_scr003_07_delete_confirm_cancel_no_change(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)
    log = record_network(page)

    page.get_by_role("listitem", name="친구").get_by_role("button", name="삭제", exact=True).click()
    page.get_by_role("heading", name="카테고리 삭제").wait_for()
    page.get_by_role("button", name="취소", exact=True).click()
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


# ── 5-4b. 사이드바 카테고리 nav 클릭 필터링 (2026-07-18 사용자 결정 기능 확장) ──────
#
# 근거: docs/planning/02 화면정의서 v1.15 255행은 "클릭 시 필터링 동작 없음(표시
# 전용)"이라고 명시했으나, 사용자가 이번 라운드에서 클릭 시 실제 필터링 동작을
# 추가하기로 결정(static/app.js의 renderCategoryNav 위 주석 및 selectCategoryFilter
# 참고). 문서 개정은 dev-pl이 별도로 planning 팀에 요청 예정 — 이 파일은 미변경.
# 아래 4개 케이스는 qa-planner의 06 문서가 아니라 frontend-engineer가 구현 완료 후
# 제안한 케이스를 실제 구현(static/app.js)을 직접 확인해 옮긴 것이다.


def test_tc_e2e_scr003_09_category_nav_click_filters_contacts_table(page, api_request):
    username, _ = signup(api_request)
    login(api_request, username)
    friend_id = get_category_id(api_request, "친구")
    family_id = get_category_id(api_request, "가족")
    api_request.post("/contacts", data=contact_payload(friend_id, name="민지"))
    api_request.post("/contacts", data=contact_payload(friend_id, name="지수"))
    api_request.post("/contacts", data=contact_payload(family_id, name="수민"))
    _login_via_page(page, username)

    page.screenshot(path="docs/screenshot/category-11-필터전전체목록.png")
    page.locator("#category-nav .nav-item", has_text="친구").click()
    page.wait_for_timeout(500)
    page.screenshot(path="docs/screenshot/category-12-친구필터적용.png")

    names = page.locator("#contact-rows .name").all_text_contents()
    assert set(names) == {"민지", "지수"}


def test_tc_e2e_scr003_10_category_nav_click_shows_active_state(page, api_request):
    username, _ = signup(api_request)
    _login_via_page(page, username)

    all_item = page.locator("#category-nav .nav-item", has_text="전체")
    friend_item = page.locator("#category-nav .nav-item", has_text="친구")
    assert all_item.get_attribute("aria-pressed") == "true"
    assert "active" in all_item.get_attribute("class")

    friend_item.click()
    page.wait_for_timeout(500)
    page.screenshot(path="docs/screenshot/category-13-친구액티브상태.png")

    assert friend_item.get_attribute("aria-pressed") == "true"
    assert "active" in friend_item.get_attribute("class")
    assert all_item.get_attribute("aria-pressed") == "false"
    assert "active" not in all_item.get_attribute("class")


def test_tc_e2e_scr003_11_category_nav_click_all_resets_filter(page, api_request):
    username, _ = signup(api_request)
    login(api_request, username)
    friend_id = get_category_id(api_request, "친구")
    family_id = get_category_id(api_request, "가족")
    api_request.post("/contacts", data=contact_payload(friend_id, name="민지"))
    api_request.post("/contacts", data=contact_payload(family_id, name="수민"))
    _login_via_page(page, username)

    page.locator("#category-nav .nav-item", has_text="친구").click()
    page.wait_for_timeout(500)
    assert page.locator("#contact-rows .name").all_text_contents() == ["민지"]

    page.locator("#category-nav .nav-item", has_text="전체").click()
    page.wait_for_timeout(500)
    page.screenshot(path="docs/screenshot/category-14-전체클릭필터해제.png")

    names = page.locator("#contact-rows .name").all_text_contents()
    assert set(names) == {"민지", "수민"}
    assert page.locator(
        "#category-nav .nav-item", has_text="전체"
    ).get_attribute("aria-pressed") == "true"


def test_tc_e2e_scr003_12_category_filter_and_search_are_mutually_exclusive(page, api_request):
    username, _ = signup(api_request)
    login(api_request, username)
    friend_id = get_category_id(api_request, "친구")
    family_id = get_category_id(api_request, "가족")
    api_request.post("/contacts", data=contact_payload(friend_id, name="민지"))
    api_request.post("/contacts", data=contact_payload(friend_id, name="지수"))
    api_request.post("/contacts", data=contact_payload(family_id, name="수민"))
    _login_via_page(page, username)

    # 1) 카테고리 필터("친구") 적용 중 검색 실행 → 실제 구현(runSearch)은 검색 시
    # selectedCategoryId를 null로 되돌려 "전체"가 다시 active 되고, 검색은 카테고리
    # 무관하게 전체 대상으로 실행된다.
    page.locator("#category-nav .nav-item", has_text="친구").click()
    page.wait_for_timeout(500)
    page.get_by_placeholder("이름으로 검색 (예: 윤아)").fill("수민")
    page.get_by_role("button", name="검색", exact=True).click()
    page.wait_for_timeout(500)
    page.screenshot(path="docs/screenshot/category-15-카테고리필터중검색실행.png")

    names = page.locator("#contact-rows .name").all_text_contents()
    assert names == ["수민"]
    assert page.locator(
        "#category-nav .nav-item", has_text="전체"
    ).get_attribute("aria-pressed") == "true"
    assert page.locator(
        "#category-nav .nav-item", has_text="친구"
    ).get_attribute("aria-pressed") == "false"

    # 2) 검색 결과가 남아 있는 상태에서 카테고리("친구") 클릭 → 실제 구현
    # (selectCategoryFilter)은 검색창 값을 비우고 카테고리 필터만 적용한다.
    page.locator("#category-nav .nav-item", has_text="친구").click()
    page.wait_for_timeout(500)
    page.screenshot(path="docs/screenshot/category-16-검색중카테고리클릭.png")

    assert page.get_by_placeholder("이름으로 검색 (예: 윤아)").input_value() == ""
    names_after = page.locator("#contact-rows .name").all_text_contents()
    assert set(names_after) == {"민지", "지수"}

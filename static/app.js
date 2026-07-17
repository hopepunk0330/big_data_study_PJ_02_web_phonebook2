"use strict";

/* 연락처 관리 서비스 — 프론트엔드 로직
 * 소스: docs/planning/02_연락처관리_웹서비스_화면정의서_v1.15.md
 * API 계약: backend/routers/{auth,contacts,categories}.py, backend/schemas.py
 */

// ── 카테고리 팔레트 매핑 (CatBadge, design-system.md 1-1/1-2) ──────────────
const CATEGORY_STYLE = {
    "친구": "cat-friend",
    "가족": "cat-family",
    "기타": "cat-other",
    "회사": "cat-company",
};
function categoryStyleFor(name) {
    return CATEGORY_STYLE[name] || "cat-default";
}

// ── 전역 상태 ───────────────────────────────────────────────────────────
const state = {
    categories: [], // [{id, name}]
    contacts: [], // 현재 화면에 표시 중인 목록
    editingContactId: null,
    deletingContactId: null,
    addingContact: false,
    renamingCategoryId: null,
    deletingCategoryId: null,
    isSearchActive: false, // true: 검색 필터 적용 중(빈 상태 문구 분기용)
};

// ── EmptyState (main-검색없음 501:4218 재사용, Pixel/NoResult 아이콘 인라인) ──
const EMPTY_STATE_ICON = `
    <svg class="empty-state-icon" viewBox="0 0 40 44" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
        <g class="body">
            <path d="M12 0H8V4H12V0Z"/><path d="M16 0H12V4H16V0Z"/><path d="M20 0H16V4H20V0Z"/><path d="M24 0H20V4H24V0Z"/>
            <path d="M8 4H4V8H8V4Z"/><path d="M28 4H24V8H28V4Z"/>
            <path d="M4 8H0V12H4V8Z"/><path d="M32 8H28V12H32V8Z"/>
            <path d="M4 12H0V16H4V12Z"/><path d="M32 12H28V16H32V12Z"/>
            <path d="M4 16H0V20H4V16Z"/><path d="M32 16H28V20H32V16Z"/>
            <path d="M8 20H4V24H8V20Z"/><path d="M28 20H24V24H28V20Z"/>
            <path d="M12 24H8V28H12V24Z"/><path d="M16 24H12V28H16V24Z"/><path d="M20 24H16V28H20V24Z"/><path d="M24 24H20V28H24V24Z"/>
            <path d="M28 28H24V32H28V28Z"/><path d="M32 32H28V36H32V32Z"/><path d="M36 36H32V40H36V36Z"/>
        </g>
        <g class="crack">
            <path d="M12 8H8V12H12V8Z"/><path d="M24 8H20V12H24V8Z"/>
            <path d="M16 12H12V16H16V12Z"/><path d="M20 12H16V16H20V12Z"/>
            <path d="M12 16H8V20H12V16Z"/><path d="M24 16H20V20H24V16Z"/>
        </g>
    </svg>`;

// ── DOM 헬퍼 ────────────────────────────────────────────────────────────
const $ = (id) => document.getElementById(id);

function show(el) {
    el.hidden = false;
}
function hide(el) {
    el.hidden = true;
}

function setBanner(bannerEl, textEl, message) {
    textEl.textContent = message;
    show(bannerEl);
}
function clearBanner(bannerEl) {
    hide(bannerEl);
}

// ── API 호출 ────────────────────────────────────────────────────────────
const LOGIN_PATH = "/auth/login";
// /auth/me도 예외에 포함한다 — §5 초기 진입 흐름에서 로그인 전 최초 방문의
// GET /auth/me 401은 "세션 만료"가 아니라 "아직 로그인한 적 없음"(정상)이므로
// SCR-900의 강제 전환 배너를 띄우면 안 된다.
const NO_FORCE_401_PATHS = [LOGIN_PATH, "/auth/me"];

async function apiRequest(method, path, body) {
    const opts = {
        method,
        headers: {},
    };
    if (body !== undefined) {
        opts.headers["Content-Type"] = "application/json";
        opts.body = JSON.stringify(body);
    }
    let resp;
    try {
        resp = await fetch(path, opts);
    } catch (e) {
        // 서버 다운/연결 끊김 등 fetch() 자체가 던지는 네트워크 예외 —
        // 기존 에러 응답과 동일한 {status, ok, body} 형태로 반환해
        // 호출부의 extractDetail(resp.body) 경로를 그대로 재사용한다.
        return { status: 0, ok: false, body: { detail: "네트워크 오류가 발생했습니다. 잠시 후 다시 시도해 주세요." } };
    }
    let json = null;
    try {
        json = await resp.json();
    } catch (e) {
        json = null;
    }

    if (resp.status === 401 && !NO_FORCE_401_PATHS.includes(path)) {
        forceSessionExpired();
    }

    return { status: resp.status, ok: resp.ok, body: json };
}

function extractDetail(json) {
    if (!json) return "오류가 발생했습니다";
    const d = json.detail;
    if (Array.isArray(d)) {
        return (d[0] && d[0].msg) || "오류가 발생했습니다";
    }
    return d || "오류가 발생했습니다";
}

// ── SCR-900: 세션 만료 강제 전환 ──────────────────────────────────────────
function forceSessionExpired() {
    showLogin();
    setBanner($("login-error-banner"), $("login-error-text"), "다시 로그인해 주세요");
}

// ── 화면 전환 ───────────────────────────────────────────────────────────
function hideAllAuthViews() {
    hide($("view-login"));
    hide($("view-pwreset1"));
    hide($("view-pwreset2"));
}

// 주의(테스트 호환): `hidden` 속성은 CSS로는 감춰지지만 Playwright의
// get_by_placeholder는 숨겨진 요소도 부분 문자열로 계속 매칭 대상에 포함한다.
// login-password/pwreset2-new-password 둘 다 placeholder가 "4~20자"이고,
// login-username도 그 문자열을 부분 포함("...4~20자")하므로, 비활성 화면의
// 값은 placeholder 자체를 비워 두었다가 활성화될 때만 복원한다.
const AUTH_PLACEHOLDERS = {
    "login-username": "영문 소문자·숫자 4~20자",
    "login-password": "4~20자",
    "pwreset2-new-password": "4~20자",
};
const AUTH_VIEW_ACTIVE_FIELDS = {
    "view-login": ["login-username", "login-password"],
    "view-pwreset1": [],
    "view-pwreset2": ["pwreset2-new-password"],
};
function applyAuthPlaceholders(activeViewId) {
    const activeFields = AUTH_VIEW_ACTIVE_FIELDS[activeViewId] || [];
    Object.keys(AUTH_PLACEHOLDERS).forEach((id) => {
        $(id).placeholder = activeFields.includes(id) ? AUTH_PLACEHOLDERS[id] : "";
    });
}

// 주의(테스트 호환, applyAuthPlaceholders와 동일 원리): pwreset1/pwreset2 카드의
// 로고 아래 타이틀("비밀번호 재설정", 확정 디자인 995:2484/996:404 실측)이 로그인
// 화면의 "비밀번호 재설정" 링크 텍스트와 동일해 hidden 상태에서도 get_by_text
// 매칭에 함께 잡힌다 — 활성 화면일 때만 텍스트를 채우고 나머지는 비운다.
const AUTH_TITLES = {
    "pwreset1-title": "비밀번호 재설정",
    "pwreset2-title": "비밀번호 재설정",
};
const AUTH_VIEW_ACTIVE_TITLES = {
    "view-login": [],
    "view-pwreset1": ["pwreset1-title"],
    "view-pwreset2": ["pwreset2-title"],
};
function applyAuthTitles(activeViewId) {
    const activeTitles = AUTH_VIEW_ACTIVE_TITLES[activeViewId] || [];
    Object.keys(AUTH_TITLES).forEach((id) => {
        $(id).textContent = activeTitles.includes(id) ? AUTH_TITLES[id] : "";
    });
}

function showLogin() {
    hide($("screen-main"));
    show($("screen-auth"));
    hideAllAuthViews();
    show($("view-login"));
    applyAuthPlaceholders("view-login");
    applyAuthTitles("view-login");
}

function showPwReset1() {
    hideAllAuthViews();
    clearBanner($("pwreset1-error-banner"));
    $("pwreset1-username").value = "";
    show($("view-pwreset1"));
    applyAuthPlaceholders("view-pwreset1");
    applyAuthTitles("view-pwreset1");
}

function showPwReset2(username) {
    hideAllAuthViews();
    clearBanner($("pwreset2-error-banner"));
    clearBanner($("pwreset2-success-banner"));
    $("pwreset2-username").textContent = username;
    $("pwreset2-new-password").value = "";
    $("pwreset2-confirm-password").value = "";
    show($("view-pwreset2"));
    applyAuthPlaceholders("view-pwreset2");
    applyAuthTitles("view-pwreset2");
}

async function showMain(user) {
    hide($("screen-auth"));
    show($("screen-main"));
    $("username-label").textContent = user.username + "님";
    await loadCategories();
    await loadContacts();
}

// ── 초기 진입 (§5 단계별 워크플로우) ──────────────────────────────────────
async function init() {
    const me = await apiRequest("GET", "/auth/me");
    if (me.status === 200) {
        await showMain(me.body);
    } else {
        showLogin();
    }
}

// ── SCR-001 로그인/회원가입 ────────────────────────────────────────────────
$("login-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    clearBanner($("login-error-banner"));
    clearBanner($("login-success-banner"));
    const username = $("login-username").value;
    const password = $("login-password").value;

    const resp = await apiRequest("POST", "/auth/login", { username, password });
    if (resp.status === 200) {
        const me = await apiRequest("GET", "/auth/me");
        if (me.status === 200) {
            await showMain(me.body);
        }
    } else {
        setBanner($("login-error-banner"), $("login-error-text"), extractDetail(resp.body));
    }
});

$("btn-signup").addEventListener("click", async () => {
    clearBanner($("login-error-banner"));
    clearBanner($("login-success-banner"));
    const username = $("login-username").value;
    const password = $("login-password").value;

    const resp = await apiRequest("POST", "/auth/signup", { username, password });
    if (resp.status === 201) {
        setBanner($("login-success-banner"), $("login-success-text"), "가입 완료! 로그인해 주세요");
    } else {
        setBanner($("login-error-banner"), $("login-error-text"), extractDetail(resp.body));
    }
});

// 비밀번호 표시/숨김 토글 — Pixel/Eye(281:405)·Pixel/EyeOff(415:892) 짝 아이콘 스왑.
// 마스킹 중(type=password)이면 "누르면 보인다"는 의미로 뜬눈 아이콘을, 표시 중
// (type=text)이면 "누르면 다시 가려진다"는 의미로 감은눈 아이콘을 보여준다.
function setupPasswordToggle(inputId, buttonId) {
    const input = $(inputId);
    const button = $(buttonId);
    const use = button.querySelector("use");
    button.addEventListener("click", () => {
        const willShow = input.type === "password";
        input.type = willShow ? "text" : "password";
        use.setAttribute("href", willShow ? "#px-eye-off" : "#px-eye");
        button.setAttribute("aria-label", willShow ? "비밀번호 숨기기" : "비밀번호 표시");
    });
}
setupPasswordToggle("login-password", "toggle-login-password");
setupPasswordToggle("pwreset2-new-password", "toggle-pwreset2-new-password");
setupPasswordToggle("pwreset2-confirm-password", "toggle-pwreset2-confirm-password");

$("link-password-reset").addEventListener("click", () => {
    showPwReset1();
});

// ── SCR-004 비밀번호 재설정 ─────────────────────────────────────────────
$("pwreset1-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    clearBanner($("pwreset1-error-banner"));
    const username = $("pwreset1-username").value;

    const resp = await apiRequest("POST", "/auth/find-password", { username });
    if (resp.status === 200) {
        showPwReset2(resp.body.username);
    } else {
        setBanner($("pwreset1-error-banner"), $("pwreset1-error-text"), extractDetail(resp.body));
    }
});

$("btn-pwreset1-back").addEventListener("click", () => {
    showLogin();
});

$("pwreset2-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    clearBanner($("pwreset2-error-banner"));
    clearBanner($("pwreset2-success-banner"));

    const username = $("pwreset2-username").textContent;
    const newPassword = $("pwreset2-new-password").value;
    const confirmPassword = $("pwreset2-confirm-password").value;

    if (newPassword !== confirmPassword) {
        setBanner($("pwreset2-error-banner"), $("pwreset2-error-text"), "두 비밀번호가 일치하지 않습니다");
        return;
    }

    const resp = await apiRequest("PATCH", "/auth/password", {
        username,
        new_password: newPassword,
    });
    if (resp.status === 200) {
        setBanner($("pwreset2-success-banner"), $("pwreset2-success-text"), "비밀번호가 변경되었습니다");
        setTimeout(showLogin, 800);
    } else {
        setBanner($("pwreset2-error-banner"), $("pwreset2-error-text"), extractDetail(resp.body));
    }
});

// ── 로그아웃 ────────────────────────────────────────────────────────────
$("btn-logout").addEventListener("click", async () => {
    await apiRequest("POST", "/auth/logout");
    showLogin();
});

// ── SCR-003 카테고리 로딩/렌더링 ───────────────────────────────────────────
async function loadCategories() {
    const resp = await apiRequest("GET", "/categories");
    if (resp.status !== 200) return;
    state.categories = resp.body;
    renderCategorySelect();
    renderCategoryManageList();
    renderCategoryNav();
}

function renderCategorySelect() {
    const select = $("add-category");
    const previous = select.value;
    select.innerHTML = "";
    state.categories.forEach((cat) => {
        const opt = document.createElement("option");
        opt.value = cat.id;
        opt.textContent = cat.name;
        select.appendChild(opt);
    });
    if (previous && state.categories.some((c) => String(c.id) === previous)) {
        select.value = previous;
    }
}

function categoryCount(categoryId) {
    return state.contacts.filter((c) => c.category_id === categoryId).length;
}

function renderCategoryNav() {
    const nav = $("category-nav");
    nav.innerHTML = "";

    const allItem = document.createElement("li");
    allItem.className = "nav-item active";
    allItem.innerHTML = `<span>전체</span><span class="count-pill">${state.contacts.length}</span>`;
    nav.appendChild(allItem);

    state.categories.forEach((cat) => {
        const li = document.createElement("li");
        li.className = "nav-item";
        li.innerHTML = `<span>${escapeHtml(cat.name)}</span><span class="count-pill">${categoryCount(cat.id)}</span>`;
        nav.appendChild(li);
    });
}

function renderCategoryManageList() {
    const list = $("category-manage-list");
    list.innerHTML = "";
    state.categories.forEach((cat) => {
        const li = document.createElement("li");
        li.setAttribute("role", "listitem");
        // 주의(테스트 호환): "listitem" 역할은 접근성 트리에서 콘텐츠로부터
        // 이름을 자동 계산하지 않는다(button/row 등과 달리) — 명시적
        // aria-label 없이는 get_by_role("listitem", name=...)가 항상 0건이다.
        li.setAttribute("aria-label", cat.name);
        li.innerHTML = `
            <span class="cat-name">${escapeHtml(cat.name)}</span>
            <span class="actions">
                <button type="button" class="btn btn-small row-action edit" data-action="rename" data-id="${cat.id}">수정</button>
                <button type="button" class="btn btn-small row-action danger" data-action="delete-category" data-id="${cat.id}">삭제</button>
            </span>`;
        list.appendChild(li);
    });
}

$("category-manage-list").addEventListener("click", (e) => {
    const btn = e.target.closest("button[data-action]");
    if (!btn) return;
    const categoryId = Number(btn.dataset.id);
    const category = state.categories.find((c) => c.id === categoryId);
    if (!category) return;

    if (btn.dataset.action === "rename") {
        openRenameCategoryModal(category);
    } else if (btn.dataset.action === "delete-category") {
        openDeleteCategoryModal(category);
    }
});

// ── 카테고리 이름 수정 모달 (CategoryRenameModal, 근거: 카테고리 이름 수정 1002:1611) ──
function openRenameCategoryModal(category) {
    state.renamingCategoryId = category.id;
    clearBanner($("rename-category-error-banner"));
    $("rename-category-name").value = category.name;
    setNameLabelActive("rename-category");
    setModalOpen($("modal-rename-category"), true);
    $("rename-category-name").focus();
}
function closeRenameCategoryModal() {
    state.renamingCategoryId = null;
    setNameLabelActive(null);
    setModalOpen($("modal-rename-category"), false);
}
$("rename-category-close").addEventListener("click", closeRenameCategoryModal);
$("btn-cancel-rename-category").addEventListener("click", closeRenameCategoryModal);
$("rename-category-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    clearBanner($("rename-category-error-banner"));
    const resp = await apiRequest("PATCH", `/categories/${state.renamingCategoryId}`, {
        name: $("rename-category-name").value,
    });
    if (resp.status === 200) {
        closeRenameCategoryModal();
        await loadCategories();
        await loadContacts();
        showToast("수정되었습니다");
    } else {
        setBanner($("rename-category-error-banner"), $("rename-category-error-text"), extractDetail(resp.body));
    }
});

// ── 카테고리 삭제 확인 모달 (CategoryDeleteModal, 근거: 카테고리 삭제 확인 1001:1594) ──
function openDeleteCategoryModal(category) {
    state.deletingCategoryId = category.id;
    clearBanner($("delete-category-error-banner"));
    $("delete-category-name").textContent = category.name;
    setModalOpen($("modal-delete-category"), true);
    $("btn-cancel-delete-category").focus();
}
function closeDeleteCategoryModal() {
    state.deletingCategoryId = null;
    // 주의(테스트 호환): hidden 속성이 get_by_text 매칭 자체를 막지 못하므로,
    // 모달을 닫을 때 경고문 안의 카테고리명 텍스트도 함께 비워 잔존 매칭을 막는다.
    $("delete-category-name").textContent = "";
    setModalOpen($("modal-delete-category"), false);
}
$("delete-category-close").addEventListener("click", closeDeleteCategoryModal);
$("btn-cancel-delete-category").addEventListener("click", closeDeleteCategoryModal);
$("btn-confirm-delete-category").addEventListener("click", async () => {
    clearBanner($("delete-category-error-banner"));
    const resp = await apiRequest("DELETE", `/categories/${state.deletingCategoryId}`);
    if (resp.status === 204) {
        closeDeleteCategoryModal();
        await loadCategories();
        showToast("삭제되었습니다");
    } else {
        setBanner($("delete-category-error-banner"), $("delete-category-error-text"), extractDetail(resp.body));
    }
});

$("btn-add-category").addEventListener("click", async () => {
    const name = $("new-category-name").value;
    const resp = await apiRequest("POST", "/categories", { name });
    if (resp.status === 201) {
        clearBanner($("category-error"));
        $("new-category-name").value = "";
        await loadCategories();
        showToast("추가되었습니다");
    } else {
        setBanner($("category-error"), $("category-error-text"), extractDetail(resp.body));
    }
});

// ── SCR-002 연락처 로딩/렌더링 ─────────────────────────────────────────────
async function loadContacts(params) {
    let path = "/contacts";
    if (params) {
        const qs = new URLSearchParams(params).toString();
        if (qs) path += "?" + qs;
    }
    const resp = await apiRequest("GET", path);
    if (resp.status !== 200) return;
    state.contacts = resp.body.items;
    state.isSearchActive = !!(params && params.name);
    $("total-count").textContent = `총 ${resp.body.total}건`;
    $("list-title").textContent = state.isSearchActive ? "검색결과" : "전체";
    renderContactRows();
    renderCategoryNav();
}

function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
}

function renderContactRows() {
    const tbody = $("contact-rows");
    tbody.innerHTML = "";

    if (state.contacts.length === 0) {
        renderEmptyState(tbody);
        return;
    }

    state.contacts.forEach((contact) => {
        const tr = document.createElement("tr");
        const style = categoryStyleFor(contact.category_name);
        tr.innerHTML = `
            <td class="name">${escapeHtml(contact.name)}</td>
            <td class="phone">${escapeHtml(contact.phone)}</td>
            <td class="addr">${escapeHtml(contact.addr)}</td>
            <td><span class="cat-badge ${style}"><span class="dot"></span>${escapeHtml(contact.category_name)}</span></td>
            <td class="actions">
                <button type="button" class="btn btn-small row-action edit" data-action="edit" data-id="${contact.id}">수정</button>
                <button type="button" class="btn btn-small row-action danger" data-action="delete" data-id="${contact.id}">삭제</button>
            </td>`;
        tbody.appendChild(tr);
    });
}

// 빈 상태(EmptyState) — main-검색없음(501:4218) 재사용. 검색 필터 유무로 문구/CTA만 분기.
function renderEmptyState(tbody) {
    const tr = document.createElement("tr");
    const td = document.createElement("td");
    td.className = "empty-state-cell";
    td.colSpan = 5;
    td.innerHTML = state.isSearchActive
        ? `<div class="empty-state">
                ${EMPTY_STATE_ICON}
                <div class="empty-state-text">
                    <p class="empty-state-title">검색 결과가 없습니다</p>
                    <p class="empty-state-subtitle">다른 검색어나 카테고리를 선택해 보세요</p>
                </div>
                <button type="button" class="empty-state-cta" data-action="show-all">전체 보기</button>
            </div>`
        : `<div class="empty-state">
                ${EMPTY_STATE_ICON}
                <div class="empty-state-text">
                    <p class="empty-state-title">아직 연락처가 없어요</p>
                    <p class="empty-state-subtitle">첫 연락처를 추가해서 나만의 목록을 시작해 보세요</p>
                </div>
                <span class="link" id="empty-state-focus-add" data-action="focus-add" tabindex="0" role="button">위 폼에서 바로 추가하기</span>
            </div>`;
    tr.appendChild(td);
    tbody.appendChild(tr);
}

$("contact-rows").addEventListener("click", (e) => {
    const emptyAction = e.target.closest("[data-action='show-all'], [data-action='focus-add']");
    if (emptyAction) {
        if (emptyAction.dataset.action === "show-all") {
            $("search-name").value = "";
            loadContacts();
        } else {
            $("add-name").focus();
        }
        return;
    }

    const btn = e.target.closest("button[data-action]");
    if (!btn) return;
    const contactId = Number(btn.dataset.id);
    const contact = state.contacts.find((c) => c.id === contactId);
    if (!contact) return;

    if (btn.dataset.action === "edit") {
        openEditModal(contact);
    } else if (btn.dataset.action === "delete") {
        deleteContact(contact);
    }
});

$("contact-rows").addEventListener("keydown", (e) => {
    if (e.key !== "Enter" && e.key !== " ") return;
    const focusAdd = e.target.closest("[data-action='focus-add']");
    if (!focusAdd) return;
    e.preventDefault();
    $("add-name").focus();
});

$("add-contact-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    if (state.addingContact) return;
    state.addingContact = true;
    $("btn-add-contact").disabled = true;
    clearBanner($("add-error-banner"));

    try {
        const payload = {
            name: $("add-name").value,
            phone: $("add-phone").value,
            addr: $("add-addr").value,
            category_id: Number($("add-category").value),
        };
        const resp = await apiRequest("POST", "/contacts", payload);
        if (resp.status === 201) {
            $("add-name").value = "";
            $("add-phone").value = "";
            $("add-addr").value = "";
            await loadContacts();
            showToast("추가되었습니다");
        } else if (resp.status !== 401) {
            setBanner($("add-error-banner"), $("add-error-text"), extractDetail(resp.body));
        }
    } finally {
        state.addingContact = false;
        $("btn-add-contact").disabled = false;
    }
});

$("btn-search").addEventListener("click", async () => {
    await loadContacts({ name: $("search-name").value });
});

$("btn-show-all").addEventListener("click", async () => {
    $("search-name").value = "";
    await loadContacts();
});

// ── 연락처 수정 모달 (ContactModal) ────────────────────────────────────────
function setModalOpen(modalEl, isOpen) {
    if (isOpen) {
        show(modalEl);
        $("main-content").inert = true;
        $("sidebar").inert = true;
    } else {
        hide(modalEl);
        $("main-content").inert = false;
        $("sidebar").inert = false;
    }
}

// 주의(테스트 호환): 연락처 추가 폼(이름/전화번호/주소)과 수정 모달이 정확히
// 같은 placeholder 문구를 쓴다(§4 SCR-002 필드 1:1 대응). `inert`/`hidden`도
// get_by_placeholder 매칭 자체를 막지 못하므로, 활성 쪽(추가 폼 또는 모달)만
// 실제 placeholder를 갖고 비활성 쪽은 비워 둔다.
const CONTACT_FIELD_PLACEHOLDERS = { name: "이름", phone: "전화번호", addr: "주소" };
function setContactFieldPlaceholders(activeGroup) {
    Object.keys(CONTACT_FIELD_PLACEHOLDERS).forEach((field) => {
        $("add-" + field).placeholder = activeGroup === "add" ? CONTACT_FIELD_PLACEHOLDERS[field] : "";
        $("edit-" + field).placeholder = activeGroup === "edit" ? CONTACT_FIELD_PLACEHOLDERS[field] : "";
    });
}

// 주의(테스트 호환): 연락처 수정 모달(#edit-name)과 카테고리 이름수정 모달
// (#rename-category-name)의 <label>이 둘 다 정확히 "이름" 텍스트를 쓴다.
// `hidden` 속성은 get_by_label 매칭 자체를 막지 못하므로(위 placeholder와
// 동일 문제), 열려 있는 모달 쪽만 실제 라벨 텍스트를 갖고 나머지는 비워 둔다.
function setNameLabelActive(activeModal) {
    document.querySelector('label[for="edit-name"]').textContent = activeModal === "edit-contact" ? "이름" : "";
    document.querySelector('label[for="rename-category-name"]').textContent =
        activeModal === "rename-category" ? "이름" : "";
}

function renderEditCategorySelector(selectedCategoryId) {
    const wrap = $("edit-category-selector");
    wrap.innerHTML = "";
    state.categories.forEach((cat) => {
        const style = categoryStyleFor(cat.name);
        const chip = document.createElement("button");
        chip.type = "button";
        chip.className = "type-chip" + (cat.id === selectedCategoryId ? " selected " + style : "");
        chip.textContent = cat.name;
        chip.dataset.id = cat.id;
        chip.addEventListener("click", () => {
            wrap.dataset.selectedId = cat.id;
            Array.from(wrap.children).forEach((c) => {
                c.className = "type-chip";
            });
            chip.className = "type-chip selected " + style;
        });
        wrap.appendChild(chip);
    });
    wrap.dataset.selectedId = selectedCategoryId;
}

function openEditModal(contact) {
    state.editingContactId = contact.id;
    clearBanner($("edit-error-banner"));
    $("edit-name").value = contact.name;
    $("edit-phone").value = contact.phone;
    $("edit-addr").value = contact.addr;
    renderEditCategorySelector(contact.category_id);
    setContactFieldPlaceholders("edit");
    setNameLabelActive("edit-contact");
    setModalOpen($("modal-edit-contact"), true);
}

function closeEditModal() {
    state.editingContactId = null;
    setContactFieldPlaceholders("add");
    setNameLabelActive(null);
    setModalOpen($("modal-edit-contact"), false);
}

$("edit-close").addEventListener("click", closeEditModal);
$("btn-cancel-edit").addEventListener("click", closeEditModal);

$("edit-contact-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    clearBanner($("edit-error-banner"));
    const payload = {
        name: $("edit-name").value,
        phone: $("edit-phone").value,
        addr: $("edit-addr").value,
        category_id: Number($("edit-category-selector").dataset.selectedId),
    };
    const resp = await apiRequest("PATCH", `/contacts/${state.editingContactId}`, payload);
    if (resp.status === 200) {
        closeEditModal();
        await loadContacts();
        showToast("수정되었습니다");
    } else if (resp.status !== 401) {
        setBanner($("edit-error-banner"), $("edit-error-text"), extractDetail(resp.body));
    }
});

// ── 연락처 삭제 확인 ────────────────────────────────────────────────────────
// 주의(테스트 호환): 화면정의서(02 문서)는 연락처 삭제를 확정 디자인 커스텀
// 모달(ConfirmModal)로 기술하지만, qa-engineer의 실제 테스트(TC-E2E-SCR002-09/10)는
// `page.once("dialog", ...)` 패턴으로 검증한다 — 이는 네이티브 confirm()에서만
// 발생하는 이벤트다. 지시사항의 "테스트 코드가 정확한 스펙" 원칙에 따라 네이티브
// confirm()으로 구현한다(dev-pl에게 이 문서-테스트 불일치를 별도 보고 필요).
async function deleteContact(contact) {
    const confirmed = window.confirm(`"${contact.name}" 연락처를 삭제하시겠습니까?`);
    if (!confirmed) return;
    const resp = await apiRequest("DELETE", `/contacts/${contact.id}`);
    if (resp.status === 204) {
        await loadContacts();
        showToast("삭제되었습니다");
    }
}

// ── SCR-900 성공 토스트 ────────────────────────────────────────────────────
let toastTimer = null;
function showToast(message) {
    $("main-toast-text").textContent = message;
    show($("main-toast"));
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => hide($("main-toast")), 1800);
}

// ── 시작 ────────────────────────────────────────────────────────────────
setContactFieldPlaceholders("add"); // 기본 상태: 수정 모달은 닫혀 있음
setNameLabelActive(null); // 기본 상태: 두 "이름" 라벨 모달 모두 닫혀 있음
init();

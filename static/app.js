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
// TypeSelector(257:28)는 4가지 컬러(친구/가족/기타/회사)만 정의돼 있고 회색
// "default" variant는 없다 — 시드 4종 이름이 아닌 카테고리(사용자가 직접 만든
// 이름)는 새 색을 만들지 않고 기존 4색을 순서대로 균등 배분(rotation)한다
// (2026-07-18, 사용자 지시: "베리에이션(균등 할당) 하면 되잖아").
const CATEGORY_STYLE_ROTATION = ["cat-friend", "cat-family", "cat-other", "cat-company"];
function categoryStyleFor(name, id) {
    if (CATEGORY_STYLE[name]) return CATEGORY_STYLE[name];
    const idx = state.categories.findIndex((c) => c.id === id);
    return CATEGORY_STYLE_ROTATION[(idx < 0 ? 0 : idx) % CATEGORY_STYLE_ROTATION.length];
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
    // 카테고리 nav 클릭 필터(2026-07-18, 사용자 결정으로 신규 확장 — 근거는
    // renderCategoryNav 위 주석 참고). null이면 "전체"(필터 해제) 상태.
    selectedCategoryId: null,
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

// ── 마우스/키보드 입력 방식 추적(2026-07-18, .input Focus 링 정밀 진단 결과) ──
// `.btn`/링크는 :focus-visible만으로 마우스 클릭 시 링이 안 뜨는 게 이미 정상
// 동작하지만, `.input`/`.input-corner`는 브라우저 내장 휴리스틱상 마우스 클릭
// 이후에도 :focus-visible이 매치된다(CSS 버그가 아니라 스펙 차이) — JS로 마지막
// 입력 방식을 추적해 `body.using-mouse`일 때만 그 두 클래스의 링을 좁게 무력화한다.
document.addEventListener("mousedown", () => document.body.classList.add("using-mouse"));
document.addEventListener("keydown", (e) => {
    if (e.key === "Tab") document.body.classList.remove("using-mouse");
});

// ── DOM 헬퍼 ────────────────────────────────────────────────────────────
const $ = (id) => document.getElementById(id);

function show(el) {
    el.hidden = false;
}
function hide(el) {
    el.hidden = true;
}

// `.toast`(main-toast)와 동일하게 `.banner` 계열도 일정 시간 후 자동으로 사라지게
// 한다(2026-07-18, dev-pl 지시 — 재제출해야만 닫히던 기존 동작 보완). 배너별로
// 타이머를 따로 관리해(showToast의 toastTimer 패턴과 동일) 새 배너가 뜨면 이전
// 타이머부터 정리한다 — 재제출 시 즉시 clearBanner로 닫히는 기존 동작은 그대로 유지.
const BANNER_AUTO_HIDE_MS = 3000;
const bannerTimers = new WeakMap();
function setBanner(bannerEl, textEl, message) {
    textEl.textContent = message;
    show(bannerEl);
    const prevTimer = bannerTimers.get(bannerEl);
    if (prevTimer) clearTimeout(prevTimer);
    const timer = setTimeout(() => hide(bannerEl), BANNER_AUTO_HIDE_MS);
    bannerTimers.set(bannerEl, timer);
}
function clearBanner(bannerEl) {
    hide(bannerEl);
    const prevTimer = bannerTimers.get(bannerEl);
    if (prevTimer) {
        clearTimeout(prevTimer);
        bannerTimers.delete(bannerEl);
    }
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

// 주의(2026-07-18, 사용자 결정으로 신규 기능 확장 — 카테고리 nav 클릭 필터링): 원래
// docs/planning/02 화면정의서 v1.15 255행은 "클릭 시 필터링 동작 없음(표시 전용)"이라고
// 명시했으나, 이번 라운드에서 사용자가 클릭 시 실제 필터링 동작을 추가하기로 결정했다
// (문서는 아직 미개정 — dev-pl이 별도로 planning 팀에 반영 요청 예정). data-category-id
// 속성(전체="")과 active 클래스(Sidebar Nav Item Active variant, navy 배경)를 클릭
// 핸들러(아래 category-nav 리스너)와 짝지어 구현한다.
function renderCategoryNav() {
    const nav = $("category-nav");
    nav.innerHTML = "";

    const allItem = document.createElement("li");
    allItem.className = "nav-item" + (state.selectedCategoryId === null ? " active" : "");
    allItem.dataset.categoryId = "";
    allItem.setAttribute("role", "button");
    allItem.setAttribute("tabindex", "0");
    allItem.setAttribute("aria-pressed", String(state.selectedCategoryId === null));
    allItem.innerHTML = `<span>전체</span><span class="count-pill">${state.contacts.length}</span>`;
    nav.appendChild(allItem);

    state.categories.forEach((cat) => {
        const li = document.createElement("li");
        li.className = "nav-item" + (state.selectedCategoryId === cat.id ? " active" : "");
        li.dataset.categoryId = cat.id;
        li.setAttribute("role", "button");
        li.setAttribute("tabindex", "0");
        li.setAttribute("aria-pressed", String(state.selectedCategoryId === cat.id));
        li.innerHTML = `<span>${escapeHtml(cat.name)}</span><span class="count-pill">${categoryCount(cat.id)}</span>`;
        nav.appendChild(li);
    });
}

async function selectCategoryFilter(li) {
    const idAttr = li.dataset.categoryId;
    state.selectedCategoryId = idAttr ? Number(idAttr) : null;
    $("search-name").value = "";
    if (state.selectedCategoryId === null) {
        await loadContacts();
    } else {
        await loadContacts({ category_id: state.selectedCategoryId });
    }
}
$("category-nav").addEventListener("click", (e) => {
    const li = e.target.closest(".nav-item");
    if (!li) return;
    selectCategoryFilter(li);
});
$("category-nav").addEventListener("keydown", (e) => {
    if (e.key !== "Enter" && e.key !== " ") return;
    const li = e.target.closest(".nav-item");
    if (!li) return;
    e.preventDefault();
    selectCategoryFilter(li);
});

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
        // Row Action Button(node 260:95, 28x22 아이콘 전용) — Table Row Action(main 테이블,
        // 260:100, 41x25 텍스트)과는 별개 컴포넌트. 텍스트를 시각적으로 없애는 대신
        // aria-label로 접근성 이름("수정"/"삭제")을 유지해 기존 role 로케이터와 호환된다.
        li.innerHTML = `
            <span class="cat-name">${escapeHtml(cat.name)}</span>
            <span class="actions">
                <button type="button" class="row-action-icon neutral" data-action="rename" data-id="${cat.id}" aria-label="수정">
                    <svg viewBox="0 0 14 14" aria-hidden="true"><use href="#px-edit"></use></svg>
                </button>
                <button type="button" class="row-action-icon danger" data-action="delete-category" data-id="${cat.id}" aria-label="삭제">
                    <svg viewBox="0 0 13.25 14" aria-hidden="true"><use href="#px-delete"></use></svg>
                </button>
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
    const resp = await apiRequest("PATCH", `/categories/${state.renamingCategoryId}`, {
        name: $("rename-category-name").value,
    });
    if (resp.status === 200) {
        closeRenameCategoryModal();
        await loadCategories();
        await loadContacts();
        showToast("수정되었습니다");
    } else {
        // 흐름 정정(2026-07-18, get_design_context main-오류배너 996:3165 재실측
        // 확정 — "카테고리이름중복(409)"도 이 공용 배너가 커버하는 에러 목록에
        // 명시돼 있다): 모달 안에 인라인 배너로 남기지 않고, 모달을 닫은 뒤
        // main-content 오버레이(main-error-toast, main-toast와 동일 슬롯)로
        // 에러를 보여준다 — 카테고리 삭제거부(아래)와 동일한 흐름.
        closeRenameCategoryModal();
        clearBanner($("main-toast"));
        setBanner($("main-error-toast"), $("main-error-text"), extractDetail(resp.body));
    }
});

// ── 카테고리 삭제 확인 모달 (CategoryDeleteModal, 근거: 카테고리 삭제 확인 1001:1594) ──
function openDeleteCategoryModal(category) {
    state.deletingCategoryId = category.id;
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
    const resp = await apiRequest("DELETE", `/categories/${state.deletingCategoryId}`);
    if (resp.status === 204) {
        // 카테고리 nav 필터 안전장치(2026-07-18, 신규 필터 기능과 함께 추가): 지금
        // 필터로 선택 중인 카테고리가 삭제되면 존재하지 않는 카테고리를 계속 필터링
        // 하지 않도록 "전체"로 되돌린다.
        if (state.selectedCategoryId === state.deletingCategoryId) {
            state.selectedCategoryId = null;
        }
        closeDeleteCategoryModal();
        await loadCategories();
        showToast("삭제되었습니다");
    } else {
        // 흐름 정정(2026-07-18, missing-screens.md 5번 항목 + get_design_context
        // main-오류배너 996:3165 재실측 확정): "카테고리 삭제 확인 모달에서 삭제
        // 시도 후 409 응답 시 모달이 닫히고 이 배너가 뜨는 흐름" — 모달 내부에
        // 인라인 배너로 남겨두지 않는다. 사용중삭제거부(409, "...N건 있어
        // 삭제할 수 없습니다") 전용 케이스.
        closeDeleteCategoryModal();
        clearBanner($("main-toast"));
        setBanner($("main-error-toast"), $("main-error-text"), extractDetail(resp.body));
    }
});

$("btn-add-category").addEventListener("click", async () => {
    const name = $("new-category-name").value;
    const resp = await apiRequest("POST", "/categories", { name });
    if (resp.status === 201) {
        clearBanner($("main-error-toast"));
        $("new-category-name").value = "";
        await loadCategories();
        showToast("추가되었습니다");
    } else {
        // 재통합(2026-07-19, 사용자 결정): 사이드바 로컬 오버레이(구 category-error)가
        // "새 카테고리" 입력창을 가리는 트레이드오프를 없애기 위해, main-error-toast
        // (content-body 상단, 검색행 위) 공용 슬롯을 그대로 재사용한다 — delete/rename
        // -category 409와 동일한 패턴.
        clearBanner($("main-toast"));
        setBanner($("main-error-toast"), $("main-error-text"), extractDetail(resp.body));
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
    // list-title 분기(2026-07-18, 카테고리 nav 필터 신규 기능): 검색 중이면 "검색결과",
    // 카테고리로 필터 중이면 그 카테고리명, 둘 다 아니면 "전체".
    const activeCategory = state.selectedCategoryId !== null
        ? state.categories.find((c) => c.id === state.selectedCategoryId)
        : null;
    $("list-title").textContent = state.isSearchActive
        ? "검색결과"
        : activeCategory
        ? activeCategory.name
        : "전체";
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
        syncContactTableHeaderGutter();
        return;
    }

    state.contacts.forEach((contact) => {
        const tr = document.createElement("tr");
        const style = categoryStyleFor(contact.category_name, contact.category_id);
        tr.innerHTML = `
            <td class="name">${escapeHtml(contact.name)}</td>
            <td class="phone">${escapeHtml(contact.phone)}</td>
            <td class="addr">${escapeHtml(contact.addr)}</td>
            <td><span class="cat-badge ${style}"><span class="dot"></span>${escapeHtml(contact.category_name)}</span></td>
            <td class="actions">
                <div class="actions-inner">
                    <button type="button" class="btn btn-small row-action edit" data-action="edit" data-id="${contact.id}">수정</button>
                    <button type="button" class="btn btn-small row-action danger" data-action="delete" data-id="${contact.id}">삭제</button>
                </div>
            </td>`;
        tbody.appendChild(tr);
    });
    syncContactTableHeaderGutter();
}

// 헤더를 테이블 밖 별도 div로 분리(2026-07-19, WebKit sticky-th 크로스브라우저 수정)한 뒤
// 생기는 부작용: 스크롤 컨테이너(.contact-table-scroll)는 세로 스크롤바가 뜨면 그만큼
// 내부 컨텐츠 폭이 좁아지는데, 스크롤되지 않는 헤더 div는 그 폭을 그대로 유지해 우측
// 끝(변경하기 컬럼)이 스크롤바 두께만큼 어긋난다. 브라우저마다 실제 스크롤바 두께가
// 달라(WebKit 8px 지정값과 실제 렌더 두께가 다를 수 있음) CSS 고정값으로 보정할 수
// 없으므로, 실측한 오프셋(offsetWidth - clientWidth)만큼 헤더에 padding-right로
// 되돌려준다. 8행 이하(스크롤바 없음)면 오프셋이 0이라 자동으로 원상복귀된다.
function syncContactTableHeaderGutter() {
    const scrollEl = document.querySelector(".contact-table-scroll");
    const headerEl = document.querySelector(".contact-table-header");
    if (!scrollEl || !headerEl) return;
    const gutter = scrollEl.offsetWidth - scrollEl.clientWidth;
    headerEl.style.paddingRight = `${gutter}px`;
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
        // 카피/CTA 정정(2026-07-18, get_design_context(1060:2014) 재실측 확정): 제목/서브텍스트
        // 문구 교체 + CTA를 텍스트 링크가 아니라 버튼(ink 배경+흰 텍스트+hard-2 그림자+radius10,
        // 99x40, .empty-state-cta 재사용)으로 교체. 클릭 동작은 기존과 동일하게 추가 폼
        // 이름 필드로 포커스 이동(data-action="focus-add" 그대로 유지).
        : `<div class="empty-state">
                ${EMPTY_STATE_ICON}
                <div class="empty-state-text">
                    <p class="empty-state-title">아직 등록된 연락처가 없어요</p>
                    <p class="empty-state-subtitle">첫 연락처를 추가해 목록을 채워보세요</p>
                </div>
                <button type="button" class="empty-state-cta" id="empty-state-focus-add" data-action="focus-add">연락처 추가</button>
            </div>`;
    tr.appendChild(td);
    tbody.appendChild(tr);
}

$("contact-rows").addEventListener("click", (e) => {
    const emptyAction = e.target.closest("[data-action='show-all'], [data-action='focus-add']");
    if (emptyAction) {
        if (emptyAction.dataset.action === "show-all") {
            $("search-name").value = "";
            state.selectedCategoryId = null;
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
    clearBanner($("main-error-toast"));

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
            clearBanner($("main-toast")); // 같은 자리에 겹쳐 뜨는 오버레이라 반대쪽도 지운다
            setBanner($("main-error-toast"), $("main-error-text"), extractDetail(resp.body));
        }
    } finally {
        state.addingContact = false;
        $("btn-add-contact").disabled = false;
    }
});

// 검색 실행(2026-07-18 dev-pl 지시): [검색] 버튼 클릭과 검색 인풋에서의 Enter 키가
// 동일한 로직을 타도록 공용 함수로 분리 — 다른 입력창(연락처 추가 폼)은 각자 별도
// <form> submit으로 이미 Enter가 연결돼 있어 이 인풋의 keydown과 서로 간섭하지 않는다.
async function runSearch() {
    // 카테고리 필터와 검색은 동시에 켜지 않는다(2026-07-18, 신규 카테고리 필터
    // 기능과 함께 정리) — 검색을 실행하면 nav의 카테고리 필터는 해제한다.
    state.selectedCategoryId = null;
    await loadContacts({ name: $("search-name").value });
}
$("btn-search").addEventListener("click", runSearch);
$("search-name").addEventListener("keydown", (e) => {
    if (e.key !== "Enter") return;
    e.preventDefault();
    runSearch();
});

$("btn-show-all").addEventListener("click", async () => {
    $("search-name").value = "";
    state.selectedCategoryId = null;
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
        const style = categoryStyleFor(cat.name, cat.id);
        const chip = document.createElement("button");
        chip.type = "button";
        chip.className = "type-chip " + style + (cat.id === selectedCategoryId ? " selected" : "");
        chip.innerHTML = `<span class="dot"></span>${escapeHtml(cat.name)}`;
        chip.dataset.id = cat.id;
        chip.addEventListener("click", () => {
            wrap.dataset.selectedId = cat.id;
            Array.from(wrap.children).forEach((c) => {
                c.className = "type-chip " + c.dataset.style;
            });
            chip.className = "type-chip " + style + " selected";
        });
        chip.dataset.style = style;
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
// 주의(2026-07-18, main-오류배너 996:3165 재실측 확정 이후): main-toast(성공)와
// main-error-toast(에러)가 이제 같은 자리(main-content 기준 absolute overlay)에
// 겹쳐 뜨는 구조라, 하나를 보여줄 때 다른 하나를 반드시 같이 지워야 두 배너가
// 동시에 겹쳐 보이는 사고를 막을 수 있다.
let toastTimer = null;
function showToast(message) {
    clearBanner($("main-error-toast"));
    $("main-toast-text").textContent = message;
    show($("main-toast"));
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => hide($("main-toast")), 1800);
}

// ── 시작 ────────────────────────────────────────────────────────────────
setContactFieldPlaceholders("add"); // 기본 상태: 수정 모달은 닫혀 있음
setNameLabelActive(null); // 기본 상태: 두 "이름" 라벨 모달 모두 닫혀 있음
window.addEventListener("resize", syncContactTableHeaderGutter);
init();

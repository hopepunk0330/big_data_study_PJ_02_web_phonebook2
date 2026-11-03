"""tests/test_cors.py

포트폴리오 사이트(cross-origin)에서 이 백엔드를 호출할 수 있게 하는 변경만 검증한다.
- CORS 프리플라이트/실제 응답 헤더
- 로그인·로그아웃 세션 쿠키의 SameSite=None; Secure 속성
"""

from conftest import DEFAULT_PASSWORD, login, signup, unique_username

PORTFOLIO_ORIGIN = "https://hopepunk0330.cafe24.com"


def _preflight(api_request, origin: str, method: str = "POST"):
    return api_request.fetch(
        "/auth/login",
        method="OPTIONS",
        headers={
            "Origin": origin,
            "Access-Control-Request-Method": method,
            "Access-Control-Request-Headers": "content-type",
        },
    )


def _set_cookie_values(resp) -> list[str]:
    return [h["value"] for h in resp.headers_array if h["name"].lower() == "set-cookie"]


def test_cors_preflight_allowed_origin(api_request):
    resp = _preflight(api_request, PORTFOLIO_ORIGIN)
    assert resp.status == 200
    assert resp.headers["access-control-allow-origin"] == PORTFOLIO_ORIGIN
    assert resp.headers["access-control-allow-credentials"] == "true"
    assert "POST" in resp.headers["access-control-allow-methods"]
    assert "content-type" in resp.headers["access-control-allow-headers"].lower()


def test_cors_preflight_disallowed_origin(api_request):
    resp = _preflight(api_request, "https://evil.example.com")
    assert "access-control-allow-origin" not in resp.headers


def test_cors_actual_response_has_origin_header(api_request):
    resp = api_request.post(
        "/auth/login",
        data={"username": "nobody1234", "password": DEFAULT_PASSWORD},
        headers={"Origin": PORTFOLIO_ORIGIN},
    )
    assert resp.headers["access-control-allow-origin"] == PORTFOLIO_ORIGIN
    assert resp.headers["access-control-allow-credentials"] == "true"


def test_login_cookie_is_samesite_none_secure(api_request):
    username, _ = signup(api_request)
    resp = login(api_request, username)
    cookies = [c for c in _set_cookie_values(resp) if c.startswith("session_id=")]
    assert cookies, "로그인 응답에 session_id Set-Cookie가 없음"
    attrs = cookies[0].lower()
    assert "samesite=none" in attrs
    assert "secure" in attrs
    assert "httponly" in attrs


def test_logout_cookie_deletion_matches_samesite_none_secure(api_request):
    username = unique_username()
    signup(api_request, username)
    login(api_request, username)
    resp = api_request.post("/auth/logout")
    cookies = [c for c in _set_cookie_values(resp) if c.startswith("session_id=")]
    assert cookies, "로그아웃 응답에 session_id Set-Cookie가 없음"
    attrs = cookies[0].lower()
    assert "samesite=none" in attrs
    assert "secure" in attrs

def test_playwright_setup(page):
    page.goto("https://playwright.dev")
    assert "Playwright" in page.title()

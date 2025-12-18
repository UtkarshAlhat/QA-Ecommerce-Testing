from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        # 1. Launch browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 2. Open application
        page.goto("https://automationexercise.com", timeout=30000)

        # 3. Navigate to Login page
        page.get_by_role("link", name="Signup / Login").click()

        # 4. Enter valid credentials
        page.fill('input[data-qa="login-email"]', "utkarshalhat3@gmail.com")
        page.fill('input[data-qa="login-password"]', "Test@123")

        # 5. Click Login
        page.get_by_role("button", name="Login").click()

        # 6. Smoke validation: user logged in
        logged_user = page.get_by_text("Logged in as")
        assert logged_user.is_visible()

        # 7. Close browser
        browser.close()


from playwright.sync_api import sync_playwright

def test_homepage_and_products_link():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://automationexercise.com", timeout=30000)
        # basic checks
        assert "Automation Exercise" in page.title()
        # verify the main nav link "Products" is visible (smoke)
        products_link = page.get_by_role("link", name="Products")
        assert products_link.is_visible()
        # navigate to Products page and ensure it loads
        products_link.click()
        page.wait_for_load_state("networkidle", timeout=20000)
        assert "Products" in page.inner_text("body")[:200]  # sanity check
        browser.close()

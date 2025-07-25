from pages.login_page import LoginPage

def test_login_valid(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    assert "dashboard" in driver.current_url.lower() or "Dashboard" in driver.page_source

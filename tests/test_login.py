from utils.base_test import setup
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_valid(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    wait = WebDriverWait(driver, 10)
    dashboard_heading = wait.until(EC.visibility_of_element_located((
        By.XPATH,
        '//h6[text()="Dashboard"]'
    )))
    assert dashboard_heading.is_displayed()

def test_login_invalid(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("invalid_user", "invalid_pass")
    error = login_page.get_error_message()
    assert "Invalid credentials" in error

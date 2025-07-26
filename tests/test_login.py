from utils.base_test import setup
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
    
def test_logout(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 10)

    # Click the user dropdown (top right corner)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab"))).click()

    # Click logout link
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))).click()

    # Assert: login form is visible again
    wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    assert "login" in driver.current_url.lower()
    
def test_dashboard_title_after_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 10)
    dashboard_heading = wait.until(EC.visibility_of_element_located((
        By.XPATH, '//h6[text()="Dashboard"]'
    )))
    assert dashboard_heading.text == "Dashboard"

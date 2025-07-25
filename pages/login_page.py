from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, '//button[@type="submit"]')

    def load(self, url="https://opensource-demo.orangehrmlive.com/"):
        self.driver.get(url)

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.login_button)).click()
        
    def get_error_message(self):
        wait = WebDriverWait(self.driver, 10)
        error_element = wait.until(EC.visibility_of_element_located((
            By.XPATH,
            '//p[contains(@class, "oxd-alert-content-text") and text()="Invalid credentials"]'
        )))
        return error_element.text

    

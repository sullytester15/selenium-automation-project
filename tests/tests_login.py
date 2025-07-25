from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "txtUsername")
        self.password_input = (By.ID, "txtPassword")
        self.login_button = (By.ID, "btnLogin")

    def load(self, url="https://opensource-demo.orangehrmlive.com/"):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


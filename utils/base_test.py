from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()  # Or Firefox/Edge depending on what you have installed
    driver.maximize_window()
    yield driver
    driver.quit()


import pytest
import requests
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser_setup():
    options = Options()
    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver
    browser.config.base_url = "https://demowebshop.tricentis.com"
    browser.config.window_width = 1440
    browser.config.window_height = 900

    session = requests.Session()
    session.get("https://demowebshop.tricentis.com")
    cookies = session.cookies.get_dict()

    browser.open("/")

    for name, value in cookies.items():
        browser.driver.add_cookie({"name": name, "value": value})

    yield session

    browser.quit()


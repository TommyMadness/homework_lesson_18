import allure
from selene import browser

def attach_screenshot(name="screenshot"):
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from utils.helpers import Helper
from config.urls import URLs

class JSAlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = Helper(driver)
        self.url = URLs.JS_ALERTS_PAGE

    # Locators
    JS_ALERT_BUTTON = (By.CSS_SELECTOR, "button[onclick='jsAlert()']")
    JS_CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    JS_PROMPT_BUTTON = (By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
    RESULT_TEXT = (By.ID, "result")

    def navigate_to_js_alerts_page(self):
        self.driver.get(self.url)

    def click_js_alert_button(self):
        self.helper.click_element(*self.JS_ALERT_BUTTON)

    def click_js_confirm_button(self):
        self.helper.click_element(*self.JS_CONFIRM_BUTTON)

    def click_js_prompt_button(self):
        self.helper.click_element(*self.JS_PROMPT_BUTTON)

    def get_result_text(self):
        return self.helper.get_text(*self.RESULT_TEXT)

    def handle_alert(self):
        alert = Alert(self.driver)
        alert_text = alert.text
        alert.accept()
        return alert_text

    def handle_confirm(self, accept=True):
        alert = Alert(self.driver)
        alert_text = alert.text
        if accept:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text

    def handle_prompt(self, text=None):
        alert = Alert(self.driver)
        alert_text = alert.text
        if text:
            alert.send_keys(text)
        alert.accept()
        return alert_text 
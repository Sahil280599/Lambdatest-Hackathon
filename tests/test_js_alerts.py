import pytest
from pages.js_alerts_page import JSAlertsPage
from config.test_data import TestData

class TestJSAlerts:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.js_alerts_page = JSAlertsPage(driver)
        self.js_alerts_page.navigate_to_js_alerts_page()

    def test_js_alert(self):
        # Click the JS Alert button
        self.js_alerts_page.click_js_alert_button()
        
        # Handle the alert
        alert_text = self.js_alerts_page.handle_alert()
        assert alert_text == TestData.JS_ALERT_MESSAGE
        
        # Verify result
        assert TestData.JS_ALERT_SUCCESS in self.js_alerts_page.get_result_text()

    def test_js_confirm(self):
        # Click the JS Confirm button
        self.js_alerts_page.click_js_confirm_button()
        
        # Handle the confirm
        alert_text = self.js_alerts_page.handle_confirm(accept=True)
        assert alert_text == TestData.JS_CONFIRM_MESSAGE
        
        # Verify result
        assert TestData.JS_CONFIRM_SUCCESS in self.js_alerts_page.get_result_text()

    def test_js_prompt(self):
        # Click the JS Prompt button
        self.js_alerts_page.click_js_prompt_button()
        
        # Handle the prompt
        alert_text = self.js_alerts_page.handle_prompt(text=TestData.JS_PROMPT_INPUT)
        assert alert_text == TestData.JS_PROMPT_MESSAGE
        
        # Verify result
        assert f"You entered: {TestData.JS_PROMPT_INPUT}" in self.js_alerts_page.get_result_text() 
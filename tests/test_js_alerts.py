import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from utils.helpers import Helper

class TestJSAlerts:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.helper = Helper(driver)
        self.base_url = "https://the-internet.herokuapp.com/javascript_alerts"
        self.driver.get(self.base_url)

    def test_js_alert(self):
        # Click the JS Alert button
        self.helper.click_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']")
        
        # Handle the alert
        alert = Alert(self.driver)
        assert alert.text == "I am a JS Alert"
        alert.accept()
        
        # Verify result
        assert "You successfully clicked an alert" in self.helper.get_text(By.ID, "result")

    def test_js_confirm(self):
        # Click the JS Confirm button
        self.helper.click_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
        
        # Handle the confirm
        alert = Alert(self.driver)
        assert alert.text == "I am a JS Confirm"
        alert.accept()
        
        # Verify result
        assert "You clicked: Ok" in self.helper.get_text(By.ID, "result")

    def test_js_prompt(self):
        # Click the JS Prompt button
        self.helper.click_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
        
        # Handle the prompt
        alert = Alert(self.driver)
        assert alert.text == "I am a JS prompt"
        test_text = "Hello, LambdaTest!"
        alert.send_keys(test_text)
        alert.accept()
        
        # Verify result
        assert f"You entered: {test_text}" in self.helper.get_text(By.ID, "result") 
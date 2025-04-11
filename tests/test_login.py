import pytest
from selenium.webdriver.common.by import By
from utils.helpers import Helper

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.helper = Helper(driver)
        self.base_url = "https://the-internet.herokuapp.com/login"
        self.driver.get(self.base_url)

    def test_valid_login(self):
        # Enter valid credentials
        self.helper.send_keys(By.ID, "username", "tomsmith")
        self.helper.send_keys(By.ID, "password", "SuperSecretPassword!")
        self.helper.click_element(By.CSS_SELECTOR, "button[type='submit']")
        
        # Verify successful login
        assert self.helper.is_element_present(By.CSS_SELECTOR, ".flash.success")
        assert "You logged into a secure area!" in self.helper.get_text(By.CSS_SELECTOR, ".flash.success")

    def test_invalid_login(self):
        # Enter invalid credentials
        self.helper.send_keys(By.ID, "username", "invaliduser")
        self.helper.send_keys(By.ID, "password", "invalidpass")
        self.helper.click_element(By.CSS_SELECTOR, "button[type='submit']")
        
        # Verify error message
        assert self.helper.is_element_present(By.CSS_SELECTOR, ".flash.error")
        assert "Your username is invalid!" in self.helper.get_text(By.CSS_SELECTOR, ".flash.error") 
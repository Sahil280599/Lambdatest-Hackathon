import pytest
from pages.login_page import LoginPage
from config.test_data import TestData

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        self.login_page.navigate_to_login_page()

    def test_valid_login(self):
        # Login with valid credentials
        self.login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        
        # Verify successful login
        assert self.login_page.is_success_message_present()
        assert TestData.LOGIN_SUCCESS_MESSAGE in self.login_page.get_success_message()

    def test_invalid_login(self):
        # Login with invalid credentials
        self.login_page.login(TestData.INVALID_USERNAME, TestData.INVALID_PASSWORD)
        
        # Verify error message
        assert self.login_page.is_error_message_present()
        assert TestData.LOGIN_ERROR_MESSAGE in self.login_page.get_error_message() 
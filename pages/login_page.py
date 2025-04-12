from selenium.webdriver.common.by import By
from utils.helpers import Helper
from config.urls import URLs

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = Helper(driver)
        self.url = URLs.LOGIN_PAGE

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".flash.success")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".flash.error")

    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.helper.send_keys(*self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.helper.send_keys(*self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.helper.click_element(*self.LOGIN_BUTTON)

    def get_success_message(self):
        return self.helper.get_text(*self.SUCCESS_MESSAGE)

    def get_error_message(self):
        return self.helper.get_text(*self.ERROR_MESSAGE)

    def is_success_message_present(self):
        return self.helper.is_element_present(*self.SUCCESS_MESSAGE)

    def is_error_message_present(self):
        return self.helper.is_element_present(*self.ERROR_MESSAGE)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button() 
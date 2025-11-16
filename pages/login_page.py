from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._locators = {
            "username_field": (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET"),
            "password_field": (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET"),
            "login_button": (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn"),
            "error_message_locked_user": (AppiumBy.XPATH, "com.saucelabs.mydemoapp.android:id/passwordErrorTV"),
            "header_title": (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginTV"),
            "header_message": (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/selectTextTV"),
            "username_error_message": (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameErrorTV"),
            "password_error_message": (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordErrorTV"),
        }

    def wait_until_page_is_loaded(self, timeout: int = 10) -> None:
        expected_locators = [
            self._locators["username_field"],
            self._locators["password_field"],
            self._locators["login_button"],
            self._locators["header_title"],
            self._locators["header_message"],
        ]
        for locator in expected_locators:
            self.wait_for_element(locator, condition=EC.presence_of_element_located, timeout=timeout)

    def enter_username(self, username: str) -> None:
        self.safe_send_keys(self._locators["username_field"], username)

    def enter_password(self, password: str) -> None:
        self.safe_send_keys(self._locators["password_field"], password)

    def click_login_button(self) -> None:
        self.wait_and_click(self._locators["login_button"])

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    @property
    def username_error_message(self) -> str:
        try:
            element = self.wait_for_element(
                self._locators["username_error_message"],
                condition=EC.visibility_of_element_located,
                timeout=5,
            )
            return element.text
        except TimeoutException as exc:
            raise TimeoutException("No error message for empty username.") from exc

    @property
    def password_error_message(self) -> str:
        try:
            element = self.wait_for_element(
                self._locators["password_error_message"],
                condition=EC.visibility_of_element_located,
                timeout=5,
            )
            return element.text
        except TimeoutException as exc:
            raise TimeoutException("No error message for empty password.") from exc

from dataclasses import dataclass, field
from typing import Tuple
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.config_vars import SHORT_TIMEOUT


@dataclass(frozen=True)
class LoginPageLocators:
    """
    contains all static locators for the login page.
    """

    USERNAME_INPUT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET"), init=False
    )
    PASSWORD_INPUT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET"), init=False
    )
    LOGIN_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn"), init=False
    )
    ERROR_MESSAGE_LOCKED_USER: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, 'com.saucelabs.mydemoapp.android:id/passwordErrorTV'), init=False
    )
    HEADER_TITLE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginTV"), init=False
    )
    HEADER_MESSAGE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/selectTextTV"), init=False
    )
    USERNAME_ERROR_MESSAGE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameErrorTV"), init=False
    )
    PASSWORD_ERROR_MESSAGE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordErrorTV"), init=False
    )


class LoginPage(BasePage):

    @allure.step("the user waits until the login page is displayed")
    def wait_until_page_is_loaded(self, timeout: int = SHORT_TIMEOUT) -> None:
        # Wait only for essential elements - username input and login button
        self.wait_for_all_elements([LoginPageLocators.USERNAME_INPUT, LoginPageLocators.LOGIN_BUTTON], timeout=timeout)

    @property
    @allure.step("retrieving username error message")
    def username_error_message(self) -> str:
        try:
            element = self.wait_for_element(
                LoginPageLocators.USERNAME_ERROR_MESSAGE,
                condition=EC.visibility_of_element_located,
                timeout=SHORT_TIMEOUT,
            )
            return element.text
        except TimeoutException as exc:
            raise TimeoutException("No error message for empty username.") from exc

    @property
    @allure.step("retrieving password error message")
    def password_error_message(self) -> str:
        try:
            element = self.wait_for_element(
                LoginPageLocators.PASSWORD_ERROR_MESSAGE,
                condition=EC.visibility_of_element_located,
                timeout=SHORT_TIMEOUT,
            )
            return element.text
        except TimeoutException as exc:
            raise TimeoutException("No error message for empty password.") from exc

    @allure.step("the user enters the username: {username}")
    def enter_username(self, username: str) -> None:
        self.safe_send_keys(LoginPageLocators.USERNAME_INPUT, username)

    @allure.step("the user enters the password")
    def enter_password(self, password: str) -> None:
        self.safe_send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("the user clicks the login button")
    def click_login(self) -> None:
        self.tap_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("the user attempts to log in with username: {username}")
    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

from dataclasses import field, dataclass
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.base_appium_gestures import BaseAppiumGestures
from config.config_vars import SHORT_TIMEOUT


@dataclass(frozen=True)
class LoginPageLocators:
    USERNAME_INPUT: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "username"), init=False)
    PASSWORD_INPUT: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "password"), init=False)
    LOGIN_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='LOG IN']"), init=False
    )


class LoginPage(BasePage, BaseAppiumGestures):

    def wait_until_page_is_loaded(self, timeout: int = SHORT_TIMEOUT) -> None:
        # Wait only for essential elements - username input and login button
        self.wait_for_all_elements([LoginPageLocators.USERNAME_INPUT, LoginPageLocators.LOGIN_BUTTON], timeout=timeout)

    @allure.step("the user enters username: {username}")
    def enter_username(self, username: str) -> None:
        username_input = self.wait_for_element(LoginPageLocators.USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)

    @allure.step("the user enters password: {password}")
    def enter_password(self, password: str) -> None:
        password_input = self.wait_for_element(LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    @allure.step("the user taps the login button")
    def tap_login_button(self) -> None:
        self.tap_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("the user attempts to log in with username: {username} and password: {password}")
    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.tap_login_button()

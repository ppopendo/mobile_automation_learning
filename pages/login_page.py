from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import allure
from dataclasses import dataclass, field
from appium.webdriver.common.appiumby import AppiumBy
from typing import Tuple
from .base_page import BasePage


@dataclass(frozen=True)
class LoginPageLocators:
	"""
	contains all static locators for the login page.
	"""
	USERNAME_INPUT: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET"),
		init=False
	)
	PASSWORD_INPUT: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET"),
		init=False
	)
	LOGIN_BUTTON: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn"),
		init=False
	)
	ERROR_MESSAGE_LOCKED_USER: Tuple[str, str] = field(
		default=(AppiumBy.XPATH, 'com.saucelabs.mydemoapp.android:id/passwordErrorTV'),
		init=False
	)
	HEADER_TITLE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginTV"),
		init=False
	)
	HEADER_MESSAGE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/selectTextTV"),
		init=False
	)
	USERNAME_ERROR_MESSAGE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameErrorTV"),
		init=False
	)
	PASSWORD_ERROR_MESSAGE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordErrorTV"),
		init=False
	)


class LoginPage(BasePage):

	def __init__(self, driver):
		super().__init__(driver)

	def wait_until_page_is_loaded(self, timeout: int = 10) -> None:
		expected_locators = [
			LoginPageLocators.USERNAME_INPUT,
			LoginPageLocators.PASSWORD_INPUT,
			LoginPageLocators.LOGIN_BUTTON,
			LoginPageLocators.HEADER_TITLE,
			LoginPageLocators.HEADER_MESSAGE,
		]
		for locator in expected_locators:
			self.wait_for_element(locator, condition=EC.presence_of_element_located, timeout=timeout)

	@property
	@allure.step("retrieving username error message")
	def username_error_message(self) -> str:
		try:
			element = self.wait_for_element(
				LoginPageLocators.USERNAME_ERROR_MESSAGE,
				condition=EC.visibility_of_element_located,
				timeout=5,
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
				timeout=5,
			)
			return element.text
		except TimeoutException as exc:
			raise TimeoutException("No error message for empty password.") from exc

	@allure.step("the user enters the username: {username}")
	def enter_username(self, username: str) -> None:
		self.safe_send_keys(LoginPageLocators.USERNAME_INPUT, username)

	@allure.step("the user enters the password: {password}")
	def enter_password(self, password: str) -> None:
		self.safe_send_keys(LoginPageLocators.PASSWORD_INPUT, password)

	@allure.step("the user clicks the login button")
	def click_login(self) -> None:
		self.wait_and_click(LoginPageLocators.LOGIN_BUTTON)

	@allure.step("the user attempts to log in with username: {username} and password: {password}")
	def login(self, username: str, password: str) -> None:
		self.enter_username(username)
		self.enter_password(password)
		self.click_login()

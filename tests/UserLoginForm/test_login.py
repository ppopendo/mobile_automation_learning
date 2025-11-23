"""Tests for login functionality."""
import allure
import pytest
from libs.common import load_user_data
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.product_page import ProductsPage


@pytest.fixture
def user_data():
	"""Load a valid user from fixtures."""
	return load_user_data()["valid_users"][0]


@pytest.fixture()
def logout_after_test(driver):
	"""Test-level teardown: ensure we're logged out after every test."""
	yield
	try:
		product_page = ProductsPage(driver)
		menu_page = MenuPage(driver)
		product_page.open_side_menu()
		menu_page.wait_until_page_is_loaded()
		if menu_page.is_logout_option_displayed():
			menu_page.click_logout()
			menu_page.confirm_logout()
	except Exception as exc:  # broad-exception-caught: acceptable for teardown
		print(f"[TEARDOWN - test]: error during logout_after_test: {exc}")


@pytest.fixture()
def open_login_form(driver):
	"""Open the side menu and navigate to the login form before the test."""
	try:
		product_page = ProductsPage(driver)
		menu_page = MenuPage(driver)
		product_page.open_side_menu()
		menu_page.wait_until_page_is_loaded()
		menu_page.click_login_button()
	except Exception as exc:  # broad-exception-caught: acceptable for setup
		print(f"[SETUP - test]: error during open_login_form: {exc}")
	# yield to the test; no teardown required here
	yield


@pytest.fixture
def login_page(driver):
	"""Return a ready LoginPage instance (assumes login screen is already visible).

	Use this in tests where the session/setup already navigated to the login screen.
	"""
	page = LoginPage(driver)
	page.wait_until_page_is_loaded()
	return page


@pytest.fixture
def login_page_opened(open_login_form, driver):
	"""Ensure the login form is opened via `open_login_form`, then return LoginPage."""
	page = LoginPage(driver)
	page.wait_until_page_is_loaded()
	return page

@allure.epic("Mobile App Tests")
@allure.feature("Login Functionality")
class TestLogin:
	"""Group for login tests."""

	@pytest.mark.tcid("TC-00001")
	@allure.story("Successful Login")
	@allure.severity(allure.severity_level.CRITICAL)
	def test_successful_login(self, driver, user_data, logout_after_test, login_page):
		"""Successful login with valid credentials."""
		product_page = ProductsPage(driver)
		login_page.login(username=user_data["username"], password=user_data["password"])
		product_page.wait_until_page_is_loaded()
		assert product_page.is_products_title_displayed(), "❌ the product screen is not displayed."

	@pytest.mark.tcid("TC-00002")
	@pytest.mark.regression
	def test_empty_password_login(self, driver, open_login_form, login_page_opened):
		"""Attempt login with empty password should show error."""
		# login_page_opened fixture ensures login form is opened
		login_page = login_page_opened
		login_page.login(username="bod@example.com", password="")
		assert login_page.password_error_message, "❌No error message for empty password."

	@pytest.mark.tcid("TC-00003")
	@pytest.mark.regression
	def test_empty_username_login(self, driver, open_login_form, login_page_opened):
		"""Attempt login with empty username should show error."""
		login_page = login_page_opened
		login_page.login(username="", password="1020340")
		assert login_page.username_error_message, "❌No error message for empty username."

import allure
import pytest
from libs.checkout_generator import generate_address, generate_payment_info
from pages.cart_page import CartPage
from pages.checkout_address_page import CheckoutAddressPage
from pages.checkout_payment_page import CheckoutPaymentPage
from pages.checkout_review_order import CheckoutReviewOrderPage
from pages.checkout_complete import CheckoutCompletePage
from pages.product_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.login_page import LoginPage
from pages.menu_component import MenuComponent
from libs.common import load_user_data

@pytest.fixture
def checkout_address_data():
	"""Generate and return a random checkout address for testing."""
	return generate_address()

@pytest.fixture
def checkout_payment_data():
	"""Generate and return random checkout payment information for testing."""
	return generate_payment_info()

@pytest.fixture()
def open_login_form(driver):
	"""Open the side menu and navigate to the login form before the test."""
	try:
		product_page = ProductsPage(driver)
		menu_page = MenuComponent(driver)
		product_page.open_side_menu()
		menu_page.wait_until_page_is_loaded()
		menu_page.click_login_button()
	except Exception as exc:
		print(f"[SETUP - test]: error during open_login_form: {exc}")
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

@pytest.fixture(autouse=True)
def logout_after_test(driver):
	"""Test-level teardown: ensure we're logged out after every test."""
	yield
	try:
		product_page = ProductsPage(driver)
		menu_component = MenuComponent(driver)
		product_page.open_side_menu()
		menu_component.wait_until_page_is_loaded()
		if menu_component.is_logout_option_displayed():
			menu_component.click_logout()
			menu_component.confirm_logout()
	except Exception as exc:
		print(f"[TEARDOWN - test]: error during logout_after_test: {exc}")

@pytest.fixture
def user_data():
	"""Load a valid user from fixtures."""
	return load_user_data()["valid_users"][0]


@allure.epic("Mobile App Tests")
@allure.feature("Checkout Flow")
class TestCheckoutFlow:

	@pytest.mark.regression
	@pytest.mark.tcid("TC-00004")
	@allure.story("as user I want to complete a purchase successfully")
	def test_checkout_general_flow(self, driver, login_page_opened, user_data, checkout_address_data, checkout_payment_data, logout_after_test):
		"""Test the general checkout flow from adding items to cart to order confirmation."""
		product_name = "Sauce Labs Backpack"
		# Login
		login_page = login_page_opened
		login_page.login(user_data["username"], user_data["password"])
		# Select product and open product details
		products_page = ProductsPage(driver)
		products_page.wait_until_page_is_loaded()
		products_page.wait_until_product_is_displayed(product_name)
		products_page.open_product_details(product_name)
		# Add product to cart
		product_details_page = ProductDetailsPage(driver)
		product_details_page.wait_until_page_is_loaded()
		product_details_page.click_add_to_cart_button()
		product_details_page.wait_until_item_count_is_updated(expected_count=1)
		product_details_page.click_cart_icon()
		# Proceed to checkout
		cart_page = CartPage(driver)
		cart_page.wait_until_page_is_loaded()
		cart_page.click_proceed_to_checkout_button()
		# Enter shipping address
		checkout_address_page = CheckoutAddressPage(driver)
		checkout_address_page.wait_until_page_is_loaded()
		checkout_address_page.enter_shipping_address(
			first_name=checkout_address_data.FULL_NAME,
			address_line_1=checkout_address_data.ADDRESS_LINE_1,
			city=checkout_address_data.CITY,
			zip_code=checkout_address_data.ZIP_CODE,
			country=checkout_address_data.COUNTRY
		)
		checkout_address_page.click_to_payment_button()
		# Enter payment information
		checkout_payment_page = CheckoutPaymentPage(driver)
		checkout_payment_page.wait_until_page_is_loaded()
		checkout_payment_page.enter_payment_information(
			full_name=checkout_payment_data.CARDHOLDER_NAME,
			card_number=checkout_payment_data.CARD_NUMBER,
			expiration_date=checkout_payment_data.EXPIRATION_DATE,
			security_code=checkout_payment_data.CVV
		)
		checkout_payment_page.click_review_order_button()
		# Confirm order
		review_order_page = CheckoutReviewOrderPage(driver)
		review_order_page.wait_until_page_is_loaded()
		review_order_page.tap_place_order_button()
		# Verify order confirmation
		order_confirmation_page = CheckoutCompletePage(driver)
		order_confirmation_page.wait_until_page_is_loaded()
		assert order_confirmation_page.is_order_successful
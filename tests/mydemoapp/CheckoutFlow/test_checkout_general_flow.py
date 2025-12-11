"""Checkout flow tests."""

import allure
import pytest
from pages.mydemoapp.cart_page import CartPage
from pages.mydemoapp.checkout_address_page import CheckoutAddressPage
from pages.mydemoapp.checkout_payment_page import CheckoutPaymentPage
from pages.mydemoapp.checkout_review_order import CheckoutReviewOrderPage
from pages.mydemoapp.checkout_complete import CheckoutCompletePage
from pages.mydemoapp.product_page import ProductsPage
from pages.mydemoapp.product_details_page import ProductDetailsPage


@allure.epic("Mobile App Tests")
@allure.feature("Checkout Flow")
class TestCheckoutFlow:

    @pytest.mark.regression
    @pytest.mark.tcid("TC-00004")
    @allure.story("as user I want to complete a purchase successfully")
    def test_checkout_general_flow(
        self, driver, login_page, user_data, checkout_address_data, checkout_payment_data, logout_after_test
    ):
        """Test the general checkout flow from adding items to cart to order confirmation."""
        product_name = "Sauce Labs Backpack"

        # Login
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
            country=checkout_address_data.COUNTRY,
        )
        checkout_address_page.click_to_payment_button()

        # Enter payment information
        checkout_payment_page = CheckoutPaymentPage(driver)
        checkout_payment_page.wait_until_page_is_loaded()
        checkout_payment_page.enter_payment_information(
            full_name=checkout_payment_data.CARDHOLDER_NAME,
            card_number=checkout_payment_data.CARD_NUMBER,
            expiration_date=checkout_payment_data.EXPIRATION_DATE,
            security_code=checkout_payment_data.CVV,
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

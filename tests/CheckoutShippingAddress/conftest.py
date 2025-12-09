"""
CheckoutShippingAddress suite - local conftest.py

Suite-specific fixtures and setup for checkout shipping address tests.
"""

import logging
from typing import Generator

import pytest

from pages.cart_page import CartPage
from pages.checkout_address_page import CheckoutAddressPage
from pages.product_details_page import ProductDetailsPage
from pages.product_page import ProductsPage

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def checkout_shipping_address_suite_setup(driver, login_user, logout_after_module) -> Generator[None, None, None]:
    """Suite setup: Login and navigate to checkout address page.
    This fixture:
    1. Uses login_user fixture to log in with valid user credentials
    2. Adds a product to cart
    3. Proceeds to checkout address page
    4. Uses logout_after_module fixture for teardown
    Yields control to tests when checkout address page is ready.
    """
    product_name = "Sauce Labs Backpack"
    # Navigate to product details and add to cart
    product_page = ProductsPage(driver)
    product_page.open_product_details(product_name)
    product_details_page = ProductDetailsPage(driver)
    product_details_page.wait_until_page_is_loaded()
    product_details_page.click_add_to_cart_button()
    product_details_page.wait_until_item_count_is_updated(expected_count=1)
    product_details_page.click_cart_icon()
    # Proceed to checkout
    cart_page = CartPage(driver)
    cart_page.wait_until_page_is_loaded()
    cart_page.click_proceed_to_checkout_button()
    # Wait for checkout address page
    checkout_address_page = CheckoutAddressPage(driver)
    checkout_address_page.wait_until_page_is_loaded()
    logger.info("[SETUP] Checkout address page is ready")
    yield
    # Suite teardown is handled by logout_after_module fixture


@pytest.fixture
def reset_checkout_address_form(driver, cart_page, checkout_address_page) -> Generator[None, None, None]:
    """Test teardown: Navigate back to cart and return to checkout address page.
    This fixture clears the address form and error messages by:
    1. Going back to cart page
    2. Returning to checkout address page
    """
    yield
    try:
        # Navigate back to cart using Android back button
        driver.back()
        cart_page.wait_until_page_is_loaded()
        cart_page.click_proceed_to_checkout_button()
        checkout_address_page.wait_until_page_is_loaded()
        logger.info("[TEARDOWN - test] Checkout address form reset successfully")
    except Exception as exc:
        logger.warning("[TEARDOWN - test] Error during form reset: %s", exc)

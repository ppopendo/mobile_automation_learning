"""
Shared checkout fixtures.

These fixtures handle checkout data generation and page objects.
"""

import pytest
from libs.checkout_generator import generate_address, generate_payment_info
from pages.mydemoapp.cart_page import CartPage
from pages.mydemoapp.checkout_address_page import CheckoutAddressPage
from pages.mydemoapp.checkout_payment_page import CheckoutPaymentPage
from pages.mydemoapp.checkout_review_order import CheckoutReviewOrderPage
from pages.mydemoapp.checkout_complete import CheckoutCompletePage
from pages.mydemoapp.product_details_page import ProductDetailsPage
from pages.mydemoapp.product_page import ProductsPage


@pytest.fixture
def checkout_address_data():
    """Generate and return a random checkout address for testing."""
    return generate_address()


@pytest.fixture
def checkout_payment_data():
    """Generate and return random checkout payment information for testing."""
    return generate_payment_info()


@pytest.fixture
def cart_page(driver):
    """Return a CartPage instance."""
    return CartPage(driver)


@pytest.fixture
def checkout_address_page(driver):
    """Return a CheckoutAddressPage instance."""
    return CheckoutAddressPage(driver)


@pytest.fixture
def checkout_payment_page(driver):
    """Return a CheckoutPaymentPage instance."""
    return CheckoutPaymentPage(driver)


@pytest.fixture
def checkout_review_page(driver):
    """Return a CheckoutReviewOrderPage instance."""
    return CheckoutReviewOrderPage(driver)


@pytest.fixture
def checkout_complete_page(driver):
    """Return a CheckoutCompletePage instance."""
    return CheckoutCompletePage(driver)


@pytest.fixture
def product_details_page(driver):
    """Return a ProductDetailsPage instance."""
    return ProductDetailsPage(driver)


@pytest.fixture
def product_page(driver):
    """Return a ProductsPage instance."""
    return ProductsPage(driver)

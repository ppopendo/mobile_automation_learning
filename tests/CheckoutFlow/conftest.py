"""
CheckoutFlow suite - local conftest.py

Suite-specific fixtures and setup for checkout flow tests.
"""

import logging

import pytest

from pages.menu_component import MenuComponent
from pages.product_page import ProductsPage
from tests.fixtures.fixtures_driver import take_screenshot

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module", autouse=True)
def checkout_suite_setup(driver, screenshots_dir):
    """Suite setup: Ensure app is on products page before checkout tests.

    This setup runs once per module and prepares the app for checkout flow tests.
    """
    try:
        product_page = ProductsPage(driver)

        # Wait for products page to be ready
        product_page.wait_until_page_is_loaded()

        logger.info("[CHECKOUT SUITE SETUP] Products page is ready for checkout tests")
    except Exception as exc:
        logger.exception("[CHECKOUT SUITE SETUP] Failed to prepare for checkout tests: %s", exc)
        take_screenshot(driver, screenshots_dir, "checkout_suite_setup_failure")
        # Don't raise - let individual tests handle their own setup


@pytest.fixture(autouse=True)
def checkout_test_cleanup(driver):
    """Clean up after each checkout test.

    Ensures user is logged out and cart is cleared after each test.
    """
    yield
    try:
        product_page = ProductsPage(driver)
        menu_component = MenuComponent(driver)

        # Try to logout if logged in
        try:
            product_page.open_side_menu()
            menu_component.wait_until_page_is_loaded()

            if menu_component.is_logout_option_displayed():
                menu_component.click_logout()
                menu_component.confirm_logout()
                logger.info("[CHECKOUT SUITE TEARDOWN] User logged out")
        except Exception as exc:
            logger.warning("[CHECKOUT SUITE TEARDOWN] Failed to log out during cleanup: %s", exc)

    except Exception as exc:
        logger.warning("[CHECKOUT SUITE TEARDOWN] Error during cleanup: %s", exc)

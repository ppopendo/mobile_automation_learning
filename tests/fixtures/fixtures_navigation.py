"""
Shared navigation fixtures.

These fixtures handle common navigation operations like opening menus and pages.
"""

import logging
import pytest
from pages.login_page import LoginPage
from pages.menu_component import MenuComponent
from pages.product_page import ProductsPage

logger = logging.getLogger(__name__)


@pytest.fixture
def login_page(driver):
    """Return a ready LoginPage instance, ensuring user is logged out first.
    This fixture:
    1. Opens the side menu
    2. Checks if user is logged in - if yes, logs out
    3. Navigates to the login form
    4. Returns a ready LoginPage instance
    Use this fixture when you need to access the login screen.
    Note:
        This fixture modifies application state by logging out the user if they are logged in.
        Use with care in tests that require a specific authentication state, as it will force the user to be logged out before proceeding.
    """
    product_page = ProductsPage(driver)
    menu_component = MenuComponent(driver)
    # Open side menu
    product_page.open_side_menu()
    menu_component.wait_until_page_is_loaded()
    # Check if user is logged in - if yes, logout first
    if menu_component.is_logout_option_displayed():
        logger.info("[LOGIN PAGE] User is logged in, logging out first...")
        menu_component.click_logout()
        menu_component.confirm_logout()
        # Re-open menu after logout
        product_page.open_side_menu()
        menu_component.wait_until_page_is_loaded()
    # Navigate to login form
    menu_component.click_login_button()
    logger.info("[LOGIN PAGE] Navigated to login form")
    # Return ready LoginPage instance
    page = LoginPage(driver)
    page.wait_until_page_is_loaded()
    return page


@pytest.fixture
def products_page(driver):
    """Return a ready ProductsPage instance."""
    page = ProductsPage(driver)
    page.wait_until_page_is_loaded()
    return page


@pytest.fixture
def menu_component(driver):
    """Return a MenuComponent instance."""
    return MenuComponent(driver)

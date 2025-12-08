"""
Shared authentication fixtures.

These fixtures handle user data loading and logout operations.
"""

import logging
import pytest
from libs.common import load_user_data
from pages.login_page import LoginPage
from pages.menu_component import MenuComponent
from pages.product_page import ProductsPage

logger = logging.getLogger(__name__)


@pytest.fixture
def user_data():
    """Load a valid user from fixtures."""
    return load_user_data()["valid_users"][0]


@pytest.fixture
def invalid_user_data():
    """Load invalid user data for negative test cases."""
    users = load_user_data()
    return users.get("invalid_users", [{"username": "invalid@test.com", "password": "wrongpass"}])[0]


@pytest.fixture(scope="module")
def login_user(driver):
    """Login user to the application for all tests in module.
    This fixture:
    1. Opens the side menu
    2. Checks if user is logged in - if yes, logs out first
    3. Navigates to the login form
    4. Logs in with valid user credentials
    Note: This fixture does not perform logout. Use with logout_after_module for cleanup.
    """
    credentials = load_user_data()["valid_users"][0]
    product_page = ProductsPage(driver)
    menu_component = MenuComponent(driver)

    # Open side menu
    product_page.wait_until_page_is_loaded()
    product_page.open_side_menu()
    menu_component.wait_until_page_is_loaded()

    # Logout if already logged in
    if menu_component.is_logout_option_displayed():
        logger.info("[LOGIN_USER] User is logged in, logging out first...")
        menu_component.click_logout()
        menu_component.confirm_logout()
        product_page.open_side_menu()
        menu_component.wait_until_page_is_loaded()

    # Navigate to login form and login
    menu_component.click_login_button()
    login_page = LoginPage(driver)
    login_page.wait_until_page_is_loaded()
    login_page.login(credentials["username"], credentials["password"])
    logger.info("[LOGIN_USER] User logged in successfully")

    # Wait for products page after login
    product_page.wait_until_page_is_loaded()


def _perform_logout(driver, context=""):
    """Internal function to perform logout operation.

    Args:
        driver: Appium driver instance
        context: Context string for logging (e.g., "test", "module")
    """
    try:
        product_page = ProductsPage(driver)
        menu_component = MenuComponent(driver)

        # Navigate back to products page (press back multiple times to handle any screen)
        for _ in range(5):
            try:
                if product_page.is_products_header_displayed():
                    break
                driver.back()
            except Exception:
                driver.back()

        product_page.open_side_menu()
        menu_component.wait_until_page_is_loaded()
        if menu_component.is_logout_option_displayed():
            menu_component.click_logout()
            menu_component.confirm_logout()
            logger.info(f"[TEARDOWN - {context}] User logged out successfully")
    except Exception as exc:
        logger.warning(f"[TEARDOWN - {context}]: error during logout: {exc}")


@pytest.fixture(scope="module")
def logout_after_module(driver):
    """Module-level teardown: ensure we're logged out after all tests in module.
    Use this fixture in module-scoped fixtures that perform login.
    """
    yield
    _perform_logout(driver, "module")


@pytest.fixture
def logout_after_test(driver):
    """Test-level teardown: ensure we're logged out after every test.
    Use this fixture in tests that perform login to ensure clean state.
    """
    yield
    _perform_logout(driver, "test")

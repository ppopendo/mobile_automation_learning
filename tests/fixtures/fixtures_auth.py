"""
Shared authentication fixtures.

These fixtures handle user data loading and logout operations.
"""

import logging
import pytest
from libs.common import load_user_data
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


@pytest.fixture
def logout_after_test(driver):
    """Test-level teardown: ensure we're logged out after every test.

    Use this fixture in tests that perform login to ensure clean state.
    """
    yield
    try:
        product_page = ProductsPage(driver)
        menu_component = MenuComponent(driver)
        product_page.open_side_menu()
        menu_component.wait_until_page_is_loaded()
        if menu_component.is_logout_option_displayed():
            menu_component.click_logout()
            menu_component.confirm_logout()
            logger.info("[TEARDOWN] User logged out successfully")
    except Exception as exc:
        logger.warning("[TEARDOWN - test]: error during logout_after_test: %s", exc)

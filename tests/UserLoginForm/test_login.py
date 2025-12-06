"""Tests for login functionality."""

import allure
import pytest
from pages.product_page import ProductsPage


@allure.epic("Mobile App Tests")
@allure.feature("Login Functionality")
class TestLogin:
    """Group for login tests."""

    @pytest.mark.tcid("TC-00001")
    @pytest.mark.regression
    @allure.story("as user I want to log in with valid credentials to access the products page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, driver, user_data, login_page, logout_after_test):
        """Successful login with valid credentials."""
        product_page = ProductsPage(driver)
        login_page.login(username=user_data["username"], password=user_data["password"])
        product_page.wait_until_page_is_loaded()
        assert product_page.is_products_title_displayed(), "❌ the product screen is not displayed."

    @pytest.mark.tcid("TC-00002")
    @pytest.mark.regression
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("as user I want to see an error message when I try to log in with an empty password")
    def test_empty_password_login(self, login_page):
        """Attempt login with empty password should show error."""
        login_page.login(username="bod@example.com", password="")
        assert login_page.password_error_message, "❌No error message for empty password."

    @pytest.mark.tcid("TC-00003")
    @pytest.mark.regression
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("as user I want to see an error message when I try to log in with an empty username")
    def test_empty_username_login(self, login_page):
        """Attempt login with empty username should show error."""
        login_page.login(username="", password="1020340")
        assert login_page.username_error_message, "❌No error message for empty username."

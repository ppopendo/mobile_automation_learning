import allure
import pytest


@allure.epic("Mobile App Tests")
@allure.feature("Checkout Shipping Address")
class TestCheckoutShippingAddress:

    @allure.story("as user I want to see error messages when submitting empty shipping address fields")
    @pytest.mark.tcid("TC-00010")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_empty_shipping_address_error(
        self,
        checkout_shipping_address_suite_setup,
        checkout_address_page,
        reset_checkout_address_form,
    ):
        """Test that error messages are displayed when submitting empty shipping address form."""
        # Click 'To Payment' button without entering any data
        checkout_address_page.click_to_payment_button()
        # Collect actual error messages
        actual = {
            "full_name": checkout_address_page.full_name_error_message,
            "address_line_1": checkout_address_page.address_line_1_error_message,
            "city": checkout_address_page.city_error_message,
            "zip_code": checkout_address_page.zip_code_error_message,
            "country": checkout_address_page.country_error_message,
        }
        # Define expected error messages
        expected = {
            "full_name": "Please provide your full name.",
            "address_line_1": "Please provide your address.",
            "city": "Please provide your city.",
            "zip_code": "Please provide your zip",
            "country": "Please provide your",
        }
        assert expected == actual, f"Error messages mismatch.\nExpected: {expected}\nActual: {actual}"

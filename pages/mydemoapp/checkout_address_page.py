from dataclasses import dataclass, field
from typing import Tuple
import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from config.config_vars import SHORT_TIMEOUT


@dataclass(frozen=True)
class CheckoutAddressPageLocators:
    PAGE_HEADER: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/checkoutTitleTV"), init=False
    )
    FIRST_NAME_INPUT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameET"), init=False
    )
    ADDRESS_LINE_1_INPUT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address1ET"), init=False
    )
    ADDRESS_LINE_2_INPUT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address2ET"), init=False
    )
    CITY_INPUT: Tuple[str, str] = field(default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityET"), init=False)
    STATE_REGION_INPUT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/stateET"), init=False
    )
    ZIP_CODE_INPUT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipET"), init=False
    )
    COUNTRY_INPUT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryET"), init=False
    )
    TO_PAYMENT_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn"), init=False
    )
    FULL_NAME_ERROR_MESSAGE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameErrorTV"), init=False
    )
    FULL_NAME_ERROR_ICON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameErrorIV"), init=False
    )
    ADDRESS_LINE_1_ERROR_MESSAGE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address1ErrorTV"), init=False
    )
    ADDRESS_LINE_1_ERROR_ICON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address1ErrorIV"), init=False
    )
    CITY_ERROR_MESSAGE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityErrorTV"), init=False
    )
    CITY_ERROR_ICON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityIV"), init=False
    )
    ZIP_CODE_ERROR_MESSAGE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipErrorTV"), init=False
    )
    ZIP_CODE_ERROR_ICON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipIV"), init=False
    )
    COUNTRY_ERROR_MESSAGE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryErrorTV"), init=False
    )
    COUNTRY_ERROR_ICON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryIV"), init=False
    )


class CheckoutAddressPage(BasePage):

    @allure.step("the user waits until the checkout address page is displayed")
    def wait_until_page_is_loaded(self, timeout=SHORT_TIMEOUT) -> None:
        # Wait only for header and submit button - form fields load with page
        self.wait_for_all_elements(
            [CheckoutAddressPageLocators.PAGE_HEADER, CheckoutAddressPageLocators.TO_PAYMENT_BUTTON], timeout=timeout
        )

    def enter_first_name(self, first_name: str) -> None:
        with allure.step(f"the user enters the first name: {first_name}"):
            first_name_input = self.wait_for_element(CheckoutAddressPageLocators.FIRST_NAME_INPUT)
            first_name_input.clear()
            first_name_input.send_keys(first_name)

    def enter_address_line_1(self, address_line_1: str) -> None:
        with allure.step(f"the user enters the address line 1: {address_line_1}"):
            address_line_1_input = self.wait_for_element(CheckoutAddressPageLocators.ADDRESS_LINE_1_INPUT)
            address_line_1_input.clear()
            address_line_1_input.send_keys(address_line_1)

    def enter_city(self, city: str) -> None:
        with allure.step(f"the user enters the city: {city}"):
            city_input = self.wait_for_element(CheckoutAddressPageLocators.CITY_INPUT)
            city_input.clear()
            city_input.send_keys(city)

    def enter_zip_code(self, zip_code: str) -> None:
        with allure.step(f"the user enters the zip code: {zip_code}"):
            zip_code_input = self.wait_for_element(CheckoutAddressPageLocators.ZIP_CODE_INPUT)
            zip_code_input.clear()
            zip_code_input.send_keys(zip_code)

    def enter_country(self, country: str) -> None:
        with allure.step(f"the user enters the country: {country}"):
            country_input = self.wait_for_element(CheckoutAddressPageLocators.COUNTRY_INPUT)
            country_input.clear()
            country_input.send_keys(country)

    @allure.step("the user clicks the 'To Payment' button")
    def click_to_payment_button(self) -> None:
        self.tap_element(CheckoutAddressPageLocators.TO_PAYMENT_BUTTON)

    @allure.step("the user enters the shipping address details")
    def enter_shipping_address(
        self, first_name: str, address_line_1: str, city: str, zip_code: str, country: str
    ) -> None:
        self.enter_first_name(first_name)
        self.enter_address_line_1(address_line_1)
        self.enter_city(city)
        self.enter_zip_code(zip_code)
        self.enter_country(country)

    @property
    @allure.step("retrieving full name error message")
    def full_name_error_message(self) -> str:
        """Retrieves the error message displayed for the full name field."""
        return self.wait_for_element(CheckoutAddressPageLocators.FULL_NAME_ERROR_MESSAGE).text

    @property
    @allure.step("retrieving address line 1 error message")
    def address_line_1_error_message(self) -> str:
        """Retrieves the error message displayed for the address line 1 field."""
        return self.wait_for_element(CheckoutAddressPageLocators.ADDRESS_LINE_1_ERROR_MESSAGE).text

    @property
    @allure.step("retrieving city error message")
    def city_error_message(self) -> str:
        """Retrieves the error message displayed for the city field."""
        return self.wait_for_element(CheckoutAddressPageLocators.CITY_ERROR_MESSAGE).text

    @property
    @allure.step("retrieving zip code error message")
    def zip_code_error_message(self) -> str:
        """Retrieves the error message displayed for the zip code field."""
        return self.wait_for_element(CheckoutAddressPageLocators.ZIP_CODE_ERROR_MESSAGE).text

    @property
    @allure.step("retrieving country error message")
    def country_error_message(self) -> str:
        """Retrieves the error message displayed for the country field."""
        return self.wait_for_element(CheckoutAddressPageLocators.COUNTRY_ERROR_MESSAGE).text

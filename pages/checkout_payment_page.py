from dataclasses import dataclass, field
from typing import Tuple
import allure
from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage


@dataclass(frozen=True)
class CheckoutPaymentPageLocators:
    PAGE_HEADER: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/enterPaymentTitleTV"), init=False
    )
    PAGE_SUB_TITLE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/enterPaymentMethodTV"), init=False
    )
    CARD_HEADER: Tuple[str, str] = field(default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardTV"), init=False)
    FULL_NAME_INPUT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET"), init=False
    )
    CARD_NUMBER_INPUT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardNumberET"), init=False
    )
    EXPIRATION_DATE_INPUT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/expirationDateET"), init=False
    )
    SECURITY_CODE_INPUT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/securityCodeET"), init=False
    )
    BILLING_ADDRESS_SAME_AS_SHIPPING_CHECKBOX: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/billingAddressCB"), init=False
    )
    REVIEW_ORDER_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn"), init=False
    )
    FULL_NAME_ERROR_MESSAGE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameErrorTV"), init=False
    )
    FULL_NAME_ERROR_ICON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameErrorIV"), init=False
    )
    CARD_NUMBER_ERROR_ICON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardNumberErrorIV"), init=False
    )
    EXPIRATION_DATE_ERROR_MESSAGE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/expirationDateErrorTV"), init=False
    )
    EXPIRATION_DATE_ERROR_ICON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/expirationDateIV"), init=False
    )
    SECURITY_CODE_ERROR_MESSAGE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/securityCodeErrorTV"), init=False
    )
    SECURITY_CODE_ERROR_ICON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/securityCodeIV"), init=False
    )


class CheckoutPaymentPage(BasePage):

    @allure.step("the user waits until the checkout payment page is displayed")
    def wait_until_page_is_loaded(self, timeout=10) -> None:
        expected_locators = [
            CheckoutPaymentPageLocators.PAGE_HEADER,
            CheckoutPaymentPageLocators.PAGE_SUB_TITLE,
            CheckoutPaymentPageLocators.CARD_HEADER,
            CheckoutPaymentPageLocators.FULL_NAME_INPUT,
            CheckoutPaymentPageLocators.CARD_NUMBER_INPUT,
            CheckoutPaymentPageLocators.EXPIRATION_DATE_INPUT,
            CheckoutPaymentPageLocators.SECURITY_CODE_INPUT,
            CheckoutPaymentPageLocators.BILLING_ADDRESS_SAME_AS_SHIPPING_CHECKBOX,
            CheckoutPaymentPageLocators.REVIEW_ORDER_BUTTON,
        ]
        for locator in expected_locators:
            self.wait_for_element(locator, timeout=timeout)

    def enter_full_name(self, full_name: str) -> None:
        with allure.step(f"the user enters full name: {full_name}"):
            full_name_input = self.wait_for_element(CheckoutPaymentPageLocators.FULL_NAME_INPUT)
            full_name_input.clear()
            full_name_input.send_keys(full_name)

    def enter_card_number(self, card_number: str) -> None:
        with allure.step(f"the user enters card number: {card_number}"):
            card_number_input = self.wait_for_element(CheckoutPaymentPageLocators.CARD_NUMBER_INPUT)
            card_number_input.clear()
            card_number_input.send_keys(card_number)

    def enter_expiration_date(self, expiration_date: str) -> None:
        with allure.step(f"the user enters expiration date: {expiration_date}"):
            expiration_date_input = self.wait_for_element(CheckoutPaymentPageLocators.EXPIRATION_DATE_INPUT)
            expiration_date_input.clear()
            expiration_date_input.send_keys(expiration_date)

    def enter_security_code(self, security_code: str) -> None:
        with allure.step(f"the user enters security code: {security_code}"):
            security_code_input = self.wait_for_element(CheckoutPaymentPageLocators.SECURITY_CODE_INPUT)
            security_code_input.clear()
            security_code_input.send_keys(security_code)

    def toggle_billing_address_checkbox(self) -> None:
        with allure.step("the user toggles the billing address same as shipping checkbox"):
            checkbox = self.wait_for_element(CheckoutPaymentPageLocators.BILLING_ADDRESS_SAME_AS_SHIPPING_CHECKBOX)
            checkbox.click()

    @allure.step("the user clicks the 'Review Order' button")
    def click_review_order_button(self) -> None:
        self.tap_element(CheckoutPaymentPageLocators.REVIEW_ORDER_BUTTON)

    @allure.step("the user enters the payment information")
    def enter_payment_information(
        self,
        full_name: str,
        card_number: str,
        expiration_date: str,
        security_code: str,
        billing_address_same_as_shipping: bool = False,
    ) -> None:
        self.enter_full_name(full_name)
        self.enter_card_number(card_number)
        self.enter_expiration_date(expiration_date)
        self.enter_security_code(security_code)
        if billing_address_same_as_shipping:
            self.toggle_billing_address_checkbox()

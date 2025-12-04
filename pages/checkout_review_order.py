from dataclasses import dataclass, field
from typing import Tuple
import allure
from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage


@dataclass(frozen=True)
class CheckoutReviewOrderPageLocators:
	PAGE_HEADER: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/checkoutTitleTV"),
		init=False
	)
	PAGE_SUB_TITLE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/enterShippingAddressTV"),
		init=False
	)
	FULL_NAME_VALUE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameTV"),
		init=False
	)
	ADDRESS_LINE_1_VALUE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/addressTV"),
		init=False
	)
	CITY_STATE_VALUE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityTV"),
		init=False
	)
	COUNTRY_ZIP_VALUE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryTV"),
		init=False
	)
	CARD_HOLDER_NAME_VALUE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardHolderTV"),
		init=False
	)
	CAR_NUMBER_VALUE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardNumberTV"),
		init=False
	)
	EXPIRATION_DATE_VALUE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/expirationDateTV"),
		init=False
	)
	BILLING_ADDRESS_AS_SHIPPING_VALUE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/billingAddressTV"),
		init=False
	)
	DELIVERY_AMOUNT: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/amountTV"),
		init=False
	)
	ESTIMATE_ARRIVAL_VALUE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/arrivalTV"),
		init=False
	)
	TOTAL_ITEMS_VALUE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/itemNumberTV"),
		init=False
	)
	TOTAL_AMOUNT_VALUE: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/totalAmountTV"),
		init=False
	)
	PLACE_ORDER_BUTTON: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn"),
		init=False
	)
	TWITTER_ICON: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/twitterIV"),
		init=False
	)
	FACEBOOK_ICON: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/FacebookIV"),
		init=False
	)
	LINKEDIN_ICON: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/LinkedInIV"),
		init=False
	)


class CheckoutReviewOrderPage(BasePage):

	@allure.step("the user waits until the checkout review order page is displayed")
	def wait_until_page_is_loaded(self, timeout=10) -> None:
		expected_locators = [
			CheckoutReviewOrderPageLocators.PAGE_HEADER,
			CheckoutReviewOrderPageLocators.FULL_NAME_VALUE,
			CheckoutReviewOrderPageLocators.ADDRESS_LINE_1_VALUE,
			CheckoutReviewOrderPageLocators.CITY_STATE_VALUE,
			CheckoutReviewOrderPageLocators.COUNTRY_ZIP_VALUE,
			CheckoutReviewOrderPageLocators.CARD_HOLDER_NAME_VALUE,
			CheckoutReviewOrderPageLocators.CAR_NUMBER_VALUE,
			CheckoutReviewOrderPageLocators.EXPIRATION_DATE_VALUE,
			CheckoutReviewOrderPageLocators.BILLING_ADDRESS_AS_SHIPPING_VALUE,
			CheckoutReviewOrderPageLocators.DELIVERY_AMOUNT,
			CheckoutReviewOrderPageLocators.ESTIMATE_ARRIVAL_VALUE,
			CheckoutReviewOrderPageLocators.TOTAL_ITEMS_VALUE,
			CheckoutReviewOrderPageLocators.TOTAL_AMOUNT_VALUE,
			CheckoutReviewOrderPageLocators.PLACE_ORDER_BUTTON,
		]
		for locator in expected_locators:
			self.wait_for_element(locator, timeout=timeout, scroll_to_element=True)

	@allure.step("the user taps the 'Place Order' button")
	def tap_place_order_button(self) -> None:
		self.tap_element(CheckoutReviewOrderPageLocators.PLACE_ORDER_BUTTON)




from dataclasses import dataclass, field
from typing import Tuple
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


@dataclass(frozen=True)
class CartPageLocators:
    PRODUCT_PRICE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV"), init=False
    )
    PAGE_HEADER: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV"), init=False
    )
    PRODUCT_NAME: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/titleTV"), init=False
    )
    PRODUCT_COLOR: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/colorIV"), init=False
    )
    DECREASE_QUANTITY_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/minusIV"), init=False
    )
    INCREASE_QUANTITY_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/plusIV"), init=False
    )
    COUNT_ITEM: Tuple[str, str] = field(default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV"), init=False)
    PRIVACY_POLICY: Tuple[str, str] = field(
        default=(
            AppiumBy.ID,
            "//android.widget.TextView[@text='© 2023 Sauce Labs All Rights Reserved. "
            "Terms of Service | Privacy Policy']",
        ),
        init=False,
    )
    ITEMS_COUNT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/itemsTV"), init=False
    )
    TOTAL_AMOUNT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/totalPriceTV"), init=False
    )
    CHECKOUT_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt"), init=False
    )
    REMOVE_ITEM_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/removeBt"), init=False
    )


class CartPage(BasePage):

    @allure.step("the user waits until the cart page is displayed")
    def wait_until_page_is_loaded(self, timeout=10) -> None:
        expected_locators = [
            CartPageLocators.PAGE_HEADER,
            CartPageLocators.PRODUCT_NAME,
            CartPageLocators.PRODUCT_PRICE,
            CartPageLocators.CHECKOUT_BUTTON,
        ]
        for locator in expected_locators:
            self.wait_for_element(locator, condition=EC.presence_of_element_located, timeout=timeout)

    @allure.step("the user clicks the 'Proceed to Checkout' button")
    def click_proceed_to_checkout_button(self) -> None:
        self.tap_element(CartPageLocators.CHECKOUT_BUTTON)

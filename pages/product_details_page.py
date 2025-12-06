from dataclasses import dataclass, field
from typing import Tuple
import allure
from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage


@dataclass(frozen=True)
class ProductDetailsPageLocators:
    PRODUCT_COLOR: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='{product_color}']"), init=False
    )
    PRODUCT_PRICE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV"), init=False
    )
    PRODUCT_DESCRIPTION: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/descTV"), init=False
    )
    PRODUCT_HIGHLIGHTS: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productHeightLightsTV"), init=False
    )
    INCREASE_QUANTITY_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/plusIV"), init=False
    )
    DECREASE_QUANTITY_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/minusIV"), init=False
    )
    COUNT_ITEM: Tuple[str, str] = field(default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV"), init=False)
    ADD_TO_CART_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt"), init=False
    )
    CART_ICON: Tuple[str, str] = field(default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartIV"), init=False)
    COUNT_ITEM_IN_CART: Tuple[str, str] = field(
        default=(
            AppiumBy.XPATH,
            "//android.widget.RelativeLayout[@content-desc='Displays number of items in your cart']"
            "/android.widget.ImageView",
        ),
        init=False,
    )
    PRODUCT_HEADER: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV"), init=False
    )
    COUNT_ITEM_IN_CART_VALUE: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartTV"), init=False
    )


class ProductDetailsPage(BasePage):

    @allure.step("the user waits until the product details page is displayed")
    def wait_until_page_is_loaded(self, timeout=10) -> None:
        expected_locators = [
            ProductDetailsPageLocators.PRODUCT_HEADER,
            ProductDetailsPageLocators.PRODUCT_PRICE,
            ProductDetailsPageLocators.PRODUCT_HIGHLIGHTS,
            ProductDetailsPageLocators.PRODUCT_DESCRIPTION,
            ProductDetailsPageLocators.INCREASE_QUANTITY_BUTTON,
            ProductDetailsPageLocators.DECREASE_QUANTITY_BUTTON,
            ProductDetailsPageLocators.COUNT_ITEM,
            ProductDetailsPageLocators.ADD_TO_CART_BUTTON,
            ProductDetailsPageLocators.CART_ICON,
        ]
        for locator in expected_locators:
            self.wait_for_element(locator, timeout=timeout, scroll_to_element=True)

    allure.step("the user adds the product to the cart")

    def click_add_to_cart_button(self) -> None:
        self.tap_element(ProductDetailsPageLocators.ADD_TO_CART_BUTTON)

    @property
    @allure.step("retrieving product price")
    def product_price(self) -> str:
        return self.wait_for_element(ProductDetailsPageLocators.PRODUCT_PRICE).text

    @property
    @allure.step("retrieving product description")
    def product_description(self) -> str:
        return self.wait_for_element(ProductDetailsPageLocators.PRODUCT_DESCRIPTION).text

    @property
    @allure.step("retrieving product highlights")
    def product_highlights(self) -> str:
        return self.wait_for_element(ProductDetailsPageLocators.PRODUCT_HIGHLIGHTS).text

    @property
    @allure.step("retrieving count of items")
    def item_count(self) -> int:
        return int(self.wait_for_element(ProductDetailsPageLocators.COUNT_ITEM).text)

    @property
    @allure.step("retrieving product color element")
    def product_color(self):
        return self.wait_for_element(ProductDetailsPageLocators.PRODUCT_COLOR)

    @allure.step("the user opens the cart page by clicking the cart icon")
    def click_cart_icon(self) -> None:
        self.tap_element(ProductDetailsPageLocators.CART_ICON)

    @allure.step("the user increases the item count by clicking the '+' button")
    def increase_item_count(self, items_count: int) -> None:
        for _ in range(items_count):
            self.tap_element(ProductDetailsPageLocators.INCREASE_QUANTITY_BUTTON)

    @allure.step("the user waits until the item count in cart is updated to {expected_count}")
    def wait_until_item_count_is_updated(self, expected_count: int, attempts: int = 5) -> None:
        for _ in range(attempts):
            try:
                element = self.wait_for_element(ProductDetailsPageLocators.COUNT_ITEM_IN_CART_VALUE)
                actual_count = int(element.text)
                if actual_count == expected_count:
                    allure.attach(
                        f"Item count in cart updated to {expected_count}.",
                        name="Item Count Update",
                        attachment_type=allure.attachment_type.TEXT,
                    )
                return
            except:
                continue
        raise TimeoutError(f"Item count in cart did not update to {expected_count} within the given time.")

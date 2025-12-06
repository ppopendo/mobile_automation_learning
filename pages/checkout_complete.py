from dataclasses import dataclass, field
from typing import Tuple
import allure
from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
from config.config_vars import SHORT_TIMEOUT


@dataclass(frozen=True)
class CheckoutCompletePageLocators:
    PAGE_HEADER: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/completeTV"), init=False
    )
    SUB_HEADER: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/thankYouTV"), init=False
    )
    SWAG_TXT: Tuple[str, str] = field(default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/swagTV"), init=False)
    ORDER_INFORMATION_TXT: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/orderTV"), init=False
    )
    CONTINUE_SHOPPING_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/shoopingBt"), init=False
    )


class CheckoutCompletePage(BasePage):

    @allure.step("the user waits until the checkout complete page is displayed")
    def wait_until_page_is_loaded(self, timeout: int = SHORT_TIMEOUT) -> None:
        # Wait only for header - if header is visible, page is loaded
        self.wait_for_all_elements(
            [CheckoutCompletePageLocators.PAGE_HEADER, CheckoutCompletePageLocators.SUB_HEADER], timeout=timeout
        )

    @allure.step("the user taps the 'Continue Shopping' button")
    def tap_continue_shopping_button(self) -> None:
        self.tap_element(CheckoutCompletePageLocators.CONTINUE_SHOPPING_BUTTON)

    @property
    @allure.step("the user gets the checkout complete message text")
    def checkout_complete_message(self):
        return self.get_element_text(CheckoutCompletePageLocators.SUB_HEADER)

    @property
    @allure.step("the user verifies if the order was successful")
    def is_order_successful(self) -> bool:
        """Checks if the order was completed successfully by verifying the presence of the order information text."""
        checkout_complete_messages = [
            "Checkout Complete",
            "Thank you for your order",
            "Your new swag is on its way",
            "Your order has been dispatched and will arrive as fast as the pony gallops!",
        ]
        checkout_complete_messages_elements = [
            self.get_element_text(CheckoutCompletePageLocators.PAGE_HEADER),
            self.get_element_text(CheckoutCompletePageLocators.SUB_HEADER),
            self.get_element_text(CheckoutCompletePageLocators.SWAG_TXT),
            self.get_element_text(CheckoutCompletePageLocators.ORDER_INFORMATION_TXT),
        ]
        return all(message in checkout_complete_messages for message in checkout_complete_messages_elements)

"""Page Object for Long Press feature in VodQA application."""

from dataclasses import dataclass, field
from typing import Tuple
import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent
from pages.vodqa.modal_generic import ModalGeneric


@dataclass(frozen=True)
class LongPressPageLocators:
    """Locators for Long Press page elements."""

    LONG_PRESS_HEADER: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='Long press the Botton']"), init=False
    )
    LONG_PRESS_BUTTON: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "longpress"), init=False)


class LongPressPage(BaseAppiumGestures, HeaderBarComponent, ModalGeneric):
    """Page Object for the Long Press screen in VodQA app.
    This page contains a button for testing long press gestures.
    """

    @allure.step("the user waits until the long press page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for long press page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Long Press Demo")

    @property
    @allure.step("checking if long press header is displayed")
    def is_long_press_header_displayed(self) -> bool:
        """Check if long press header is displayed on screen."""
        return self.is_element_displayed(LongPressPageLocators.LONG_PRESS_HEADER)

    @property
    @allure.step("checking if long press button is displayed")
    def is_long_press_button_displayed(self) -> bool:
        """Check if long press button is displayed on screen."""
        return self.is_element_displayed(LongPressPageLocators.LONG_PRESS_BUTTON)

    @allure.step("the user performs a long press on the long press button")
    def long_press_on_long_press_button(self, duration: int = 2000) -> None:
        """Perform a long press gesture on the long press button.
        Args:
            duration: Duration of the long press in milliseconds. Default is 2000 ms.
        """
        self.long_press(LongPressPageLocators.LONG_PRESS_BUTTON, duration=duration)

    @property
    @allure.step("the modal is displayed after long press")
    def is_long_press_modal_displayed(self) -> bool:
        """Wait until the modal dialog is displayed after long press."""
        return self.is_modal_displayed

"""Page Object for Long Press feature in VodQA application."""

from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent


@dataclass(frozen=True)
class LongPressPageLocators:
    """Locators for Long Press page elements."""

    LONG_PRESS_HEADER: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='Long press the Botton']"), init=False
    )
    LONG_PRESS_BUTTON: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "longpress"), init=False)


class LongPressPage(BaseAppiumGestures, HeaderBarComponent):
    """Page Object for the Long Press screen in VodQA app.
    This page contains a button for testing long press gestures.
    """

    @allure.step("the user waits until the long press page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for long press page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Long Press")

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

"""Page Object for Long Press feature in VodQA application."""

from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent, HeaderBarComponentLocators


@dataclass(frozen=True)
class LongPressPageLocators:
    """Locators for Long Press page elements."""

    PAGE_TITLE: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='Long Press']"), init=False
    )
    PRESS_TARGET: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='longPress']//android.view.ViewGroup[1]"),
        init=False,
    )
    PRESS_INDICATOR: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Press')]"), init=False
    )


class LongPressPage(BaseAppiumGestures, HeaderBarComponent):
    """Page Object for the Long Press screen in VodQA app.

    This page contains a target element for testing long press gestures.
    """

    @allure.step("the user waits until the long press page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for long press page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Long Press")

    @allure.step("the user navigates back from long press page")
    def tap_back_button(self) -> None:
        """Tap the back button to return to Samples List."""
        self.tap_element(HeaderBarComponentLocators.BACK_BUTTON)

    @property
    @allure.step("checking if press target is displayed")
    def is_press_target_displayed(self) -> bool:
        """Check if press target element is displayed on screen."""
        return self.is_element_displayed(LongPressPageLocators.PRESS_TARGET)

    @property
    @allure.step("retrieving press indicator text")
    def press_indicator_text(self) -> str:
        """Get the text of the press indicator element."""
        return self.wait_for_element(LongPressPageLocators.PRESS_INDICATOR).text

    @property
    @allure.step("retrieving press target center coordinates")
    def press_target_center_coordinates(self) -> tuple:
        """Get center coordinates of press target element."""
        element = self.wait_for_element(LongPressPageLocators.PRESS_TARGET)
        x = element.location["x"] + element.size["width"] // 2
        y = element.location["y"] + element.size["height"] // 2
        return (x, y)

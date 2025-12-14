"""Page Object for Double Tap feature in VodQA application."""

from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent, HeaderBarComponentLocators


@dataclass(frozen=True)
class DoubleTapPageLocators:
    """Locators for Double Tap page elements."""

    PAGE_TITLE: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='Double Tap']"), init=False
    )
    TAP_TARGET: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='doubleTap']//android.view.ViewGroup[1]"),
        init=False,
    )
    TAP_COUNTER: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Taps:')]"), init=False
    )


class DoubleTapPage(BaseAppiumGestures, HeaderBarComponent):
    """Page Object for the Double Tap screen in VodQA app.

    This page contains a target element for testing double tap gestures.
    """

    @allure.step("the user waits until the double tap page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for double tap page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Double Tap")

    @allure.step("the user navigates back from double tap page")
    def tap_back_button(self) -> None:
        """Tap the back button to return to Samples List."""
        self.tap_element(HeaderBarComponentLocators.BACK_BUTTON)

    @property
    @allure.step("checking if tap target is displayed")
    def is_tap_target_displayed(self) -> bool:
        """Check if tap target element is displayed on screen."""
        return self.is_element_displayed(DoubleTapPageLocators.TAP_TARGET)

    @property
    @allure.step("retrieving tap counter text")
    def tap_counter_text(self) -> str:
        """Get the text of the tap counter element."""
        return self.wait_for_element(DoubleTapPageLocators.TAP_COUNTER).text

    @property
    @allure.step("retrieving tap target center coordinates")
    def tap_target_center_coordinates(self) -> Tuple[int, int]:
        """Get center coordinates of tap target element."""
        element = self.wait_for_element(DoubleTapPageLocators.TAP_TARGET)
        x = element.location["x"] + element.size["width"] // 2
        y = element.location["y"] + element.size["height"] // 2
        return (x, y)

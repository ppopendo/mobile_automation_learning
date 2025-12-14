"""Page Object for Slider feature in VodQA application."""

from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent, HeaderBarComponentLocators


@dataclass(frozen=True)
class SliderPageLocators:
    """Locators for Slider page elements."""

    SLIDER_1: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "slider"), init=False)
    SLIDER_2: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "slider1"), init=False)
    SLIDER_DISPLAY_VALUE: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.SeekBar[@content-desc='slider']/following-sibling::*[@text][1]"),
        init=False,
    )


class SliderPage(BaseAppiumGestures, HeaderBarComponent):
    """Page Object for the Slider screen in VodQA app.

    This page contains two sliders for testing slider interactions.
    """

    @allure.step("the user waits until the slider page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for slider page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Slider")

    @allure.step("the user taps on slider 1 at {percentage}% position")
    def tap_slider_1_at_percentage(self, percentage: int) -> None:
        """Tap on slider 1 at a specific percentage position.

        Args:
            percentage: Target position as percentage (0-100).
        """
        self._tap_slider_at_percentage(SliderPageLocators.SLIDER_1, percentage)

    @allure.step("the user taps on slider 2 at {percentage}% position")
    def tap_slider_2_at_percentage(self, percentage: int) -> None:
        """Tap on slider 2 at a specific percentage position.

        Args:
            percentage: Target position as percentage (0-100).
        """
        self._tap_slider_at_percentage(SliderPageLocators.SLIDER_2, percentage)

    def _tap_slider_at_percentage(self, locator: Tuple[str, str], percentage: int) -> None:
        """Internal method to tap on a slider at a specific percentage position.

        Args:
            locator: Slider element locator.
            percentage: Target position as percentage (0-100).
        """
        if not 0 <= percentage <= 100:
            raise ValueError(f"Percentage must be between 0 and 100, got {percentage}")

        slider = self.wait_for_element(locator)
        slider_location = slider.location
        slider_size = slider.size

        start_x = slider_location["x"]
        slider_width = slider_size["width"]
        target_x = start_x + int(slider_width * (percentage / 100))
        center_y = slider_location["y"] + (slider_size["height"] // 2)

        params = {"x": target_x, "y": center_y}
        self._driver.execute_script("mobile: clickGesture", params)

    @property
    @allure.step("retrieving slider 1 value")
    def slider_1_value(self) -> float:
        """Get the current value of slider 1.
        Returns:
            The text attribute of slider 1.
        """
        return float(self.wait_for_element(SliderPageLocators.SLIDER_1).text)

    @property
    @allure.step("retrieving slider 2 value")
    def slider_2_value(self) -> float:
        """Get the current value of slider 2.
        Returns:
            The text attribute of slider 2.
        """
        return float(self.wait_for_element(SliderPageLocators.SLIDER_2).text)

    @property
    @allure.step("checking if slider 1 is displayed")
    def is_slider_1_displayed(self) -> bool:
        """Check if slider 1 is displayed on screen."""
        return self.is_element_displayed(SliderPageLocators.SLIDER_1)

    @property
    @allure.step("checking if slider 2 is displayed")
    def is_slider_2_displayed(self) -> bool:
        """Check if slider 2 is displayed on screen."""
        return self.is_element_displayed(SliderPageLocators.SLIDER_2)

    @allure.step("the user navigates back from slider page")
    def tap_back_button(self) -> None:
        """Tap the back button to return to Samples List."""
        self.tap_element(HeaderBarComponentLocators.BACK_BUTTON)

    @property
    @allure.step("the user retrieves the displayed slider value")
    def slider_display_value(self) -> float:
        """Get the displayed value of slider 1 or 2."""
        return float(self.wait_for_element(SliderPageLocators.SLIDER_DISPLAY_VALUE).text)

"""Page Object for Slider feature in VodQA application."""

import logging
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent, HeaderBarComponentLocators

logger = logging.getLogger(__name__)

# Slider border offset: avoid exact border coordinates (0% at left, 100% at right)
# Some Appium drivers may reject out-of-bounds or exact border coordinates
SLIDER_BORDER_OFFSET = 1


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

    @allure.step("the user swipes left on slider 1")
    def swipe_left_slider_1(self, percentage: float = 0.75, speed: int = 2200) -> None:
        """Swipe left on slider 1 element.
        Args:
            percentage: Swipe distance as percentage of element width (0.0 to 1.0).
            speed: Swipe speed in pixels per second.
        """
        self.swipe_left(locator=SliderPageLocators.SLIDER_1, percentage=percentage, speed=speed)

    @allure.step("the user swipes left on slider 2")
    def swipe_left_slider_2(self, percentage: float = 0.75, speed: int = 2200) -> None:
        """Swipe left on slider 2 element.
        Args:
            percentage: Swipe distance as percentage of element width (0.0 to 1.0).
            speed: Swipe speed in pixels per second.
        """
        self.swipe_left(locator=SliderPageLocators.SLIDER_2, percentage=percentage, speed=speed)

    @allure.step("the user swipes right on slider 1")
    def swipe_right_slider_1(self, percentage: float = 0.75, speed: int = 2200) -> None:
        """Swipe right on slider 1 element.
        Args:
            percentage: Swipe distance as percentage of element width (0.0 to 1.0).
            speed: Swipe speed in pixels per second.
        """
        self.swipe_right(locator=SliderPageLocators.SLIDER_1, percentage=percentage, speed=speed)

    @allure.step("the user swipes right on slider 2")
    def swipe_right_slider_2(self, percentage: float = 0.75, speed: int = 2200) -> None:
        """Swipe right on slider 2 element.
        Args:
            percentage: Swipe distance as percentage of element width (0.0 to 1.0).
            speed: Swipe speed in pixels per second.
        """
        self.swipe_right(locator=SliderPageLocators.SLIDER_2, percentage=percentage, speed=speed)

    # ==================== DRAG GESTURES ====================

    @allure.step("the user drags slider 1 to {target_percentage}% position")
    def drag_slider_1_to_percentage(self, target_percentage: int, speed: int = 1500) -> None:
        """Drag slider 1 thumb to a specific percentage position.

        Uses drag gesture to move the slider thumb to the target position.

        Args:
            target_percentage: Target position as percentage (0-100).
            speed: Drag speed in pixels per second.

        Raises:
            ValueError: If target_percentage is not between 0 and 100.
        """
        self._drag_slider_to_percentage(SliderPageLocators.SLIDER_1, target_percentage, speed)

    @allure.step("the user drags slider 2 to {target_percentage}% position")
    def drag_slider_2_to_percentage(self, target_percentage: int, speed: int = 1500) -> None:
        """Drag slider 2 thumb to a specific percentage position.

        Uses drag gesture to move the slider thumb to the target position.

        Args:
            target_percentage: Target position as percentage (0-100).
            speed: Drag speed in pixels per second.

        Raises:
            ValueError: If target_percentage is not between 0 and 100.
        """
        self._drag_slider_to_percentage(SliderPageLocators.SLIDER_2, target_percentage, speed)

    def _drag_slider_to_percentage(self, locator: Tuple[str, str], target_percentage: int, speed: int = 1500) -> None:
        """Internal method to drag a slider to a specific percentage position.

        Calculates the target X coordinate based on slider width and target percentage,
        then performs a drag gesture from the slider element to that position.

        Args:
            locator: Slider element locator.
            target_percentage: Target position as percentage (0-100).
            speed: Drag speed in pixels per second.

        Raises:
            ValueError: If target_percentage is not between 0 and 100 or speed is not positive.
        """
        if not 0 <= target_percentage <= 100:
            raise ValueError(f"Target percentage must be between 0 and 100, got {target_percentage}")
        if speed <= 0:
            raise ValueError(f"Speed must be a positive integer, got {speed}")

        slider = self.wait_for_element(locator)
        slider_location = slider.location
        slider_size = slider.size

        start_x = slider_location["x"]
        slider_width = slider_size["width"]
        center_y = slider_location["y"] + (slider_size["height"] // 2)

        # Calculate relative position and clamp to stay within bounds
        # Some drivers may reject out-of-bounds or border coordinates
        relative_x = int(slider_width * (target_percentage / 100))
        min_offset = SLIDER_BORDER_OFFSET
        max_offset = max(slider_width - SLIDER_BORDER_OFFSET, min_offset)
        clamped_offset = max(min_offset, min(relative_x, max_offset))
        target_x = start_x + clamped_offset

        self.drag_to_coordinates(
            source_locator=locator,
            end_x=target_x,
            end_y=center_y,
            speed=speed,
        )

    # ==================== DIAGNOSTIC METHODS ====================

    @allure.step("the user diagnoses slider locators")
    def diagnose_slider_locators(self) -> Dict[str, Any]:
        """Diagnose and verify all slider-related locators.

        This method attempts to find all slider elements using their defined locators
        and collects detailed information about each element for debugging purposes.

        Returns:
            Dict containing diagnostic information with the following structure:
                - slider_1: Dict with locator diagnostic info (keys: locator_strategy, locator_value, found, element_info, error)
                - slider_2: Dict with locator diagnostic info (keys: locator_strategy, locator_value, found, element_info, error)
                - slider_display_value: Dict with locator diagnostic info (keys: locator_strategy, locator_value, found, element_info, error)
                - all_locators_valid: Boolean indicating if all locators were found
                - suggestions: List of troubleshooting suggestions (if any locator failed)

            Each locator info dict contains:
                - locator_strategy: The strategy used (e.g., ACCESSIBILITY_ID, XPATH)
                - locator_value: The value used for finding element
                - found: Whether the element was found
                - element_info: Dict with element details (if found)
                - error: Error message (if not found)
        """
        diagnostic_results: Dict[str, Any] = {
            "slider_1": {},
            "slider_2": {},
            "slider_display_value": {},
            "all_locators_valid": True,
            "suggestions": [],
        }

        locators_to_check: List[Tuple[str, Tuple[str, str]]] = [
            ("slider_1", SliderPageLocators.SLIDER_1),
            ("slider_2", SliderPageLocators.SLIDER_2),
            ("slider_display_value", SliderPageLocators.SLIDER_DISPLAY_VALUE),
        ]

        logger.info("=" * 60)
        logger.info("🔍 Slider Locators Diagnostic Report")
        logger.info("=" * 60)

        for locator_name, locator in locators_to_check:
            strategy, value = locator
            result: Dict[str, Any] = {
                "locator_strategy": strategy,
                "locator_value": value,
                "found": False,
                "element_info": None,
                "error": None,
            }

            try:
                element = self.wait_for_element(locator, timeout=self._short_timeout)
                result["found"] = True
                result["element_info"] = {
                    "text": element.text,
                    "location": element.location,
                    "size": element.size,
                    "is_displayed": element.is_displayed(),
                    "is_enabled": element.is_enabled(),
                    "tag_name": element.tag_name,
                    "content_desc": element.get_attribute("content-desc"),
                    "resource_id": element.get_attribute("resource-id"),
                    "class_name": element.get_attribute("className"),
                }
                logger.info(f"✅ {locator_name}: FOUND")
                logger.info(f"   Strategy: {strategy}")
                logger.info(f"   Value: {value}")
                logger.info(f"   Text: '{element.text}'")
                logger.info(f"   Location: {element.location}")
                logger.info(f"   Size: {element.size}")
                logger.info(f"   Tag: {element.tag_name}")
                logger.info(f"   Content-desc: {element.get_attribute('content-desc')}")
            except Exception as e:
                result["found"] = False
                result["error"] = str(e)
                diagnostic_results["all_locators_valid"] = False
                logger.warning(f"❌ {locator_name}: NOT FOUND")
                logger.warning(f"   Strategy: {strategy}")
                logger.warning(f"   Value: {value}")
                logger.warning(f"   Error: {str(e)}")

            diagnostic_results[locator_name] = result

        # Add suggestions if any locator failed
        if not diagnostic_results["all_locators_valid"]:
            suggestions = [
                "1. Verify that you are on the Slider page before running diagnostics",
                "2. Use Appium Inspector to examine the current UI hierarchy",
                "3. Check if element accessibility IDs have changed in a new app version",
                "4. Consider alternative locator strategies (XPATH, CLASS_NAME)",
                "5. Increase timeout if elements are slow to load",
            ]
            diagnostic_results["suggestions"] = suggestions
            for suggestion in suggestions:
                logger.info(f"   {suggestion}")

        logger.info("=" * 60)

        return diagnostic_results

    @property
    @allure.step("retrieving slider 1 element details")
    def slider_1_element_info(self) -> Dict[str, Any]:
        """Get detailed information about slider 1 element.

        Returns:
            Dict containing element properties: text, location, size, attributes.
        """
        element = self.wait_for_element(SliderPageLocators.SLIDER_1)
        return {
            "text": element.text,
            "location": element.location,
            "size": element.size,
            "is_displayed": element.is_displayed(),
            "is_enabled": element.is_enabled(),
            "tag_name": element.tag_name,
            "content_desc": element.get_attribute("content-desc"),
            "resource_id": element.get_attribute("resource-id"),
        }

    @property
    @allure.step("retrieving slider 2 element details")
    def slider_2_element_info(self) -> Dict[str, Any]:
        """Get detailed information about slider 2 element.

        Returns:
            Dict containing element properties: text, location, size, attributes.
        """
        element = self.wait_for_element(SliderPageLocators.SLIDER_2)
        return {
            "text": element.text,
            "location": element.location,
            "size": element.size,
            "is_displayed": element.is_displayed(),
            "is_enabled": element.is_enabled(),
            "tag_name": element.tag_name,
            "content_desc": element.get_attribute("content-desc"),
            "resource_id": element.get_attribute("resource-id"),
        }

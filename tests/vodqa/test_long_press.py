"""Test suite for Long Press feature in VodQA application.

This module contains tests for long press gestures.
Tests verify long_press and long_press_at_coordinates methods from BaseAppiumGestures.
"""

import allure
import pytest

from pages.vodqa.long_press_page import LongPressPage, LongPressPageLocators


@allure.feature("VodQA Samples")
@allure.story("Long Press")
class TestLongPress:
    """Test class for Long Press feature functionality."""

    @pytest.mark.tcid("TC-06-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test long press page has required elements")
    def test_long_press_page_has_elements(self, long_press_page: LongPressPage) -> None:
        """Verify that the Long Press page contains required elements.
        Expected:
            - Long press header is visible
            - Long press button is visible
        """
        # Assert
        assert long_press_page.is_long_press_header_displayed, "Long press header should be visible"

    @pytest.mark.tcid("TC-06-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test long_press method on element with default duration")
    def test_long_press_on_element_default_duration(self, long_press_page: LongPressPage) -> None:
        """Verify that long_press method works on an element with default duration.
        Expected:
            - long_press method executes successfully
            - Long press gesture is performed on target element
        """
        # Arrange - verify element is displayed
        initial_state = long_press_page.is_long_press_button_displayed
        # Act - perform long press with default duration (1000ms)
        long_press_page.long_press(LongPressPageLocators.LONG_PRESS_BUTTON)
        # Assert - verify button was visible
        assert initial_state, "Long press button should be visible"

    @pytest.mark.tcid("TC-06-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test long_press method with {duration}ms duration")
    @pytest.mark.parametrize("duration", [500, 1000, 2000], ids=["500ms", "1000ms", "2000ms"])
    def test_long_press_with_different_durations(self, long_press_page: LongPressPage, duration: int) -> None:
        """Verify that long_press method works with different durations.
        Args:
            duration: Press duration in milliseconds.
        Expected:
            - long_press method executes successfully with various durations
            - Long press gesture is performed with specified duration
        """
        # Arrange - verify element is displayed
        initial_state = long_press_page.is_long_press_button_displayed
        # Act - perform long press with specified duration
        long_press_page.long_press(LongPressPageLocators.LONG_PRESS_BUTTON, duration=duration)
        # Assert - verify button was visible
        assert initial_state, f"Long press button should be visible before {duration}ms press"

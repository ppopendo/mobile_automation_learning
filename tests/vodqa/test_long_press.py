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
            - Press target element is visible
        """
        assert long_press_page.is_press_target_displayed, "Press target should be visible"

    @pytest.mark.tcid("TC-06-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test long_press method on element with default duration")
    def test_long_press_on_element_default_duration(self, long_press_page: LongPressPage) -> None:
        """Verify that long_press method works on an element with default duration.

        Steps:
            1. Verify press target is displayed
            2. Perform long press on the target element with default duration
            3. Verify long press operation completes without errors

        Expected:
            - long_press method executes successfully
            - Long press gesture is performed on target element
        """
        # Verify element is displayed
        assert long_press_page.is_press_target_displayed, "Press target should be visible before long press"

        # Perform long press with default duration (1000ms)
        long_press_page.long_press(LongPressPageLocators.PRESS_TARGET)

        # Verify the operation completed (method should not raise exceptions)

    @pytest.mark.tcid("TC-06-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test long_press method with custom duration")
    @pytest.mark.parametrize("duration", [500, 1000, 2000], ids=["500ms", "1000ms", "2000ms"])
    def test_long_press_with_different_durations(self, long_press_page: LongPressPage, duration: int) -> None:
        """Verify that long_press method works with different durations.

        Args:
            duration: Press duration in milliseconds.

        Expected:
            - long_press method executes successfully with various durations
            - Long press gesture is performed with specified duration
        """
        # Perform long press with specified duration
        long_press_page.long_press(LongPressPageLocators.PRESS_TARGET, duration=duration)

        # Verify the operation completed (method should not raise exceptions)

    @pytest.mark.tcid("TC-06-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test long_press_at_coordinates method with default duration")
    def test_long_press_at_coordinates_default_duration(self, long_press_page: LongPressPage) -> None:
        """Verify that long_press_at_coordinates method works with default duration.

        Steps:
            1. Get center coordinates of press target
            2. Perform long press at those coordinates with default duration
            3. Verify long press operation completes without errors

        Expected:
            - long_press_at_coordinates method executes successfully
            - Long press gesture is performed at specified coordinates
        """
        # Get target coordinates
        x, y = long_press_page.press_target_center_coordinates

        # Perform long press at coordinates with default duration (1000ms)
        long_press_page.long_press_at_coordinates(x, y)

        # Verify the operation completed (method should not raise exceptions)

    @pytest.mark.tcid("TC-06-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test long_press_at_coordinates with custom duration")
    @pytest.mark.parametrize("duration", [500, 1500, 2500], ids=["500ms", "1500ms", "2500ms"])
    def test_long_press_at_coordinates_with_durations(self, long_press_page: LongPressPage, duration: int) -> None:
        """Test long_press_at_coordinates with different duration values.

        Args:
            duration: Press duration in milliseconds.

        Expected:
            - long_press_at_coordinates works with different durations
            - Operation completes successfully with specified duration
        """
        # Get target coordinates
        x, y = long_press_page.press_target_center_coordinates

        # Perform long press at coordinates with specified duration
        long_press_page.long_press_at_coordinates(x, y, duration=duration)

        # Verify the operation completed (method should not raise exceptions)

    @pytest.mark.tcid("TC-06-06")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test multiple long presses on same element")
    def test_multiple_long_presses(self, long_press_page: LongPressPage) -> None:
        """Test performing multiple long presses on the same element.

        Steps:
            1. Perform first long press
            2. Perform second long press
            3. Perform third long press
            4. Verify all operations complete without errors

        Expected:
            - Multiple long presses can be performed sequentially
            - Each long press operation completes successfully
        """
        # Perform multiple long presses
        for _ in range(3):
            long_press_page.long_press(LongPressPageLocators.PRESS_TARGET, duration=1000)

        # Verify the operations completed (methods should not raise exceptions)

    @pytest.mark.tcid("TC-06-07")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test long press at different coordinate positions")
    def test_long_press_at_different_positions(self, long_press_page: LongPressPage) -> None:
        """Test long press at different coordinate positions on screen.

        Steps:
            1. Get target element center coordinates
            2. Long press at center
            3. Long press at offset positions
            4. Verify all operations complete without errors

        Expected:
            - Long press works at different coordinate positions
            - Each operation completes successfully
        """
        # Get base coordinates
        x, y = long_press_page.press_target_center_coordinates

        # Long press at center
        long_press_page.long_press_at_coordinates(x, y, duration=1000)

        # Long press at slightly different positions (within element bounds)
        long_press_page.long_press_at_coordinates(x + 10, y + 10, duration=1000)
        long_press_page.long_press_at_coordinates(x - 10, y - 10, duration=1000)

        # Verify the operations completed (methods should not raise exceptions)

    @pytest.mark.tcid("TC-06-08")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test alternating long_press and long_press_at_coordinates")
    def test_alternating_long_press_methods(self, long_press_page: LongPressPage) -> None:
        """Test alternating between long_press and long_press_at_coordinates methods.

        Steps:
            1. Perform long_press on element
            2. Perform long_press_at_coordinates
            3. Perform long_press on element again
            4. Verify all operations complete without errors

        Expected:
            - Both methods can be used interchangeably
            - All operations complete successfully
        """
        # Get coordinates
        x, y = long_press_page.press_target_center_coordinates

        # Alternate between methods
        long_press_page.long_press(LongPressPageLocators.PRESS_TARGET, duration=1000)
        long_press_page.long_press_at_coordinates(x, y, duration=1000)
        long_press_page.long_press(LongPressPageLocators.PRESS_TARGET, duration=1000)

        # Verify the operations completed (methods should not raise exceptions)

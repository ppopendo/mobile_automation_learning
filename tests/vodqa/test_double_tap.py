"""Test suite for Double Tap feature in VodQA application.

This module contains tests for double tap gestures.
Tests verify double_tap and double_tap_at_coordinates methods from BaseAppiumGestures.
"""

import allure
import pytest

from pages.vodqa.double_tap_page import DoubleTapPage, DoubleTapPageLocators


@allure.feature("VodQA Samples")
@allure.story("Double Tap")
class TestDoubleTap:
    """Test class for Double Tap feature functionality."""

    @pytest.mark.tcid("TC-05-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test double tap page has required elements")
    def test_double_tap_page_has_elements(self, double_tap_page: DoubleTapPage) -> None:
        """Verify that the Double Tap page contains required elements.

        Expected:
            - Tap target element is visible
        """
        assert double_tap_page.is_tap_target_displayed, "Tap target should be visible"

    @pytest.mark.tcid("TC-05-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test double_tap method on element")
    def test_double_tap_on_element(self, double_tap_page: DoubleTapPage) -> None:
        """Verify that double_tap method works on an element.

        Steps:
            1. Verify tap target is displayed
            2. Perform double tap on the target element
            3. Verify double tap operation completes without errors

        Expected:
            - double_tap method executes successfully
            - Double tap gesture is performed on target element
        """
        # Verify element is displayed
        assert double_tap_page.is_tap_target_displayed, "Tap target should be visible before double tap"

        # Perform double tap
        double_tap_page.double_tap(DoubleTapPageLocators.TAP_TARGET)

        # Verify the operation completed (method should not raise exceptions)
        # In a real app with proper feedback, we would verify the counter or state change

    @pytest.mark.tcid("TC-05-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test double_tap_at_coordinates method")
    def test_double_tap_at_coordinates(self, double_tap_page: DoubleTapPage) -> None:
        """Verify that double_tap_at_coordinates method works with specified coordinates.

        Steps:
            1. Get center coordinates of tap target
            2. Perform double tap at those coordinates
            3. Verify double tap operation completes without errors

        Expected:
            - double_tap_at_coordinates method executes successfully
            - Double tap gesture is performed at specified coordinates
        """
        # Get target coordinates
        x, y = double_tap_page.tap_target_center_coordinates

        # Perform double tap at coordinates
        double_tap_page.double_tap_at_coordinates(x, y)

        # Verify the operation completed (method should not raise exceptions)

    @pytest.mark.tcid("TC-05-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test multiple double taps on same element")
    def test_multiple_double_taps(self, double_tap_page: DoubleTapPage) -> None:
        """Test performing multiple double taps on the same element.

        Steps:
            1. Perform first double tap
            2. Perform second double tap
            3. Perform third double tap
            4. Verify all operations complete without errors

        Expected:
            - Multiple double taps can be performed sequentially
            - Each double tap operation completes successfully
        """
        # Perform multiple double taps
        for _ in range(3):
            double_tap_page.double_tap(DoubleTapPageLocators.TAP_TARGET)

        # Verify the operations completed (methods should not raise exceptions)

    @pytest.mark.tcid("TC-05-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test double tap at different coordinate positions")
    def test_double_tap_at_different_positions(self, double_tap_page: DoubleTapPage) -> None:
        """Test double tap at different coordinate positions on screen.

        Steps:
            1. Get target element center coordinates
            2. Double tap at center
            3. Double tap at offset positions
            4. Verify all operations complete without errors

        Expected:
            - Double tap works at different coordinate positions
            - Each operation completes successfully
        """
        # Get base coordinates
        x, y = double_tap_page.tap_target_center_coordinates

        # Double tap at center
        double_tap_page.double_tap_at_coordinates(x, y)

        # Double tap at slightly different positions (within element bounds)
        double_tap_page.double_tap_at_coordinates(x + 10, y + 10)
        double_tap_page.double_tap_at_coordinates(x - 10, y - 10)

        # Verify the operations completed (methods should not raise exceptions)

    @pytest.mark.tcid("TC-05-06")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test alternating double_tap and double_tap_at_coordinates")
    def test_alternating_double_tap_methods(self, double_tap_page: DoubleTapPage) -> None:
        """Test alternating between double_tap and double_tap_at_coordinates methods.

        Steps:
            1. Perform double_tap on element
            2. Perform double_tap_at_coordinates
            3. Perform double_tap on element again
            4. Verify all operations complete without errors

        Expected:
            - Both methods can be used interchangeably
            - All operations complete successfully
        """
        # Get coordinates
        x, y = double_tap_page.tap_target_center_coordinates

        # Alternate between methods
        double_tap_page.double_tap(DoubleTapPageLocators.TAP_TARGET)
        double_tap_page.double_tap_at_coordinates(x, y)
        double_tap_page.double_tap(DoubleTapPageLocators.TAP_TARGET)

        # Verify the operations completed (methods should not raise exceptions)

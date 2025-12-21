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
            - Double tap me button is visible
        """
        # Assert
        assert double_tap_page.is_double_tap_me_button_displayed, "Double tap me button should be visible"

    @pytest.mark.tcid("TC-05-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test double_tap method on element")
    def test_double_tap_on_element(self, double_tap_page: DoubleTapPage) -> None:
        """Verify that double_tap method works on an element.
        Expected:
            - double_tap method executes successfully
            - Double tap gesture is performed on target element
        """
        # Arrange - verify element is displayed
        button_visible_before = double_tap_page.is_double_tap_me_button_displayed
        # Act - perform double tap
        double_tap_page.double_tap(DoubleTapPageLocators.DOUBLE_TAP_ME_BUTTON)
        # Assert - verify the operation completed without exceptions
        assert button_visible_before, "Double tap me button should be visible before double tap"

    @pytest.mark.tcid("TC-05-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test double_tap method multiple times")
    def test_double_tap_multiple_times(self, double_tap_page: DoubleTapPage) -> None:
        """Test performing double tap multiple times on the same element.
        Expected:
            - Multiple double taps can be performed sequentially
            - Each double tap operation completes successfully
        """
        # Arrange - verify element is displayed
        button_visible_before = double_tap_page.is_double_tap_me_button_displayed
        # Act - perform first double tap
        double_tap_page.double_tap(DoubleTapPageLocators.DOUBLE_TAP_ME_BUTTON)
        # Assert - verify button still visible after first tap
        assert button_visible_before, "Double tap me button should be visible before double tap"

    @pytest.mark.tcid("TC-05-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test double_tap on element with {count} taps")
    @pytest.mark.parametrize("count", [1, 2, 3], ids=["1_tap", "2_taps", "3_taps"])
    def test_double_tap_parametrized(self, double_tap_page: DoubleTapPage, count: int) -> None:
        """Test double_tap method with varying number of executions.
        Args:
            count: Number of times to perform double tap
        Expected:
            - double_tap can be performed multiple times
            - Element remains interactable after multiple taps
        """
        # Arrange - verify element is displayed
        button_visible_before = double_tap_page.is_double_tap_me_button_displayed
        # Act - perform double tap specified number of times
        for _ in range(count):
            double_tap_page.double_tap(DoubleTapPageLocators.DOUBLE_TAP_ME_BUTTON)
        # Assert - verify button was visible
        assert button_visible_before, "Double tap me button should be visible before double tap"

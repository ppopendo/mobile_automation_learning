"""Test suite for Double Tap feature in VodQA application.
This module contains tests for double tap gestures.
Tests verify double_tap and double_tap_at_coordinates methods from BaseAppiumGestures.
"""

import allure
import pytest
from pages.vodqa.double_tap_page import DoubleTapPage


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
    @allure.title("Test double_tap on element")
    def test_double_tap_on_element(self, double_tap_page: DoubleTapPage) -> None:
        """Test double_tap method on element.
        Expected:
            - double_tap can be performed on element
            - Element remains interactable after tap
        """
        double_tap_page.double_tap_on_double_tap_me_button()
        assert double_tap_page.is_double_tap_modal_displayed, "Double tap modal should be displayed"

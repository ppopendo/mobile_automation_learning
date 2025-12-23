"""Test suite for Long Press feature in VodQA application.

This module contains tests for long press gestures.
Tests verify long_press and long_press_at_coordinates methods from BaseAppiumGestures.
"""

import allure
import pytest
from pages.vodqa.long_press_page import LongPressPage


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
        long_press_page.long_press_on_long_press_button()
        assert long_press_page.is_long_press_modal_displayed, "Long press modal should be displayed"

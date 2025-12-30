"""Test suite for Wheel Picker Demo feature in VodQA application.
This module contains tests for wheel picker functionality.
Tests verify property methods for retrieving color information.
"""

import allure
import pytest

from pages.vodqa.wheel_picker_demo_page import WheelPickerDemoPage


@allure.feature("VodQA Samples")
@allure.story("Wheel Picker Demo")
class TestWheelPickerDemo:
    """Test class for Wheel Picker Demo feature functionality."""

    @pytest.mark.tcid("TC-20-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test wheel picker demo page has required elements")
    def test_wheel_picker_demo_page_has_elements(self, wheel_picker_demo_page: WheelPickerDemoPage) -> None:
        """Verify that the Wheel Picker Demo page contains required elements.
        Expected:
            - Current color text is displayed and contains 'Current Color:'
            - Current color box background color is retrievable
            - Color dropdown value is displayed
        """
        # Assert multiple values using actual/expected pattern
        actual = {
            "has_color_text": "Current Color:" in wheel_picker_demo_page.current_color_text,
            "has_color_box_bg": wheel_picker_demo_page.current_color_box is not None,
            "has_dropdown_value": len(wheel_picker_demo_page.color_dropdown_value) > 0,
        }

        expected = {
            "has_color_text": True,
            "has_color_box_bg": True,
            "has_dropdown_value": True,
        }

        assert actual == expected, f"Wheel Picker Demo page elements mismatch: {actual}"

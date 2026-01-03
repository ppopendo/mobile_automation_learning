"""Test suite for Wheel Picker Demo feature in VodQA application.
This module contains tests for wheel picker functionality.
Tests verify color selection and property methods for retrieving color information.
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
            - Current color box element is visible and visual state is captured
            - Color dropdown value is displayed
        """
        # Capture initial visual state of the color box (also verifies element is present)
        color_box_screenshot = wheel_picker_demo_page.capture_color_box_screenshot()

        # Assert multiple values using actual/expected pattern
        actual = {
            "has_color_text": "Current Color:" in wheel_picker_demo_page.current_color_text,
            "has_color_box_screenshot": color_box_screenshot is not None and len(color_box_screenshot) > 0,
            "has_dropdown_value": len(wheel_picker_demo_page.color_dropdown_value) > 0,
        }

        expected = {
            "has_color_text": True,
            "has_color_box_screenshot": True,
            "has_dropdown_value": True,
        }

        assert actual == expected, f"Wheel Picker Demo page elements mismatch: {actual}"

    @pytest.mark.tcid("TC-20-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test selecting color from dropdown updates visual state")
    @pytest.mark.parametrize("color", ["Red", "Green", "Blue"], ids=["red", "green", "blue"])
    def test_select_color_from_dropdown(self, wheel_picker_demo_page: WheelPickerDemoPage, color: str) -> None:
        """Verify that selecting a color from the dropdown updates the color box visual state.

        This test uses visual testing via screenshots since mobile native apps don't support
        CSS color attributes. The screenshots are attached to the Allure report for manual
        visual verification.

        Args:
            color: The color name to select from dropdown.
        Expected:
            - Color can be selected from dropdown
            - Dropdown value updates to selected color
            - Current color text displays the selected color
            - Color box visual state is captured for verification
        """
        # Act - select the color
        wheel_picker_demo_page.select_color(color)

        # Capture the visual state of the color box after selection
        wheel_picker_demo_page.capture_color_box_screenshot()

        # Assert - verify the color was selected
        actual = {
            "dropdown_value": wheel_picker_demo_page.color_dropdown_value,
            "color_text_contains": color in wheel_picker_demo_page.current_color_text,
        }

        expected = {
            "dropdown_value": color,
            "color_text_contains": True,
        }

        assert actual == expected, f"Color selection failed for {color}: {actual}"

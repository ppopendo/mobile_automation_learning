"""Test suite for Wheel Picker Demo feature in VodQA application.
This module contains tests for wheel picker functionality.
Tests verify color selection and property methods for retrieving color information.
"""

import allure
import pytest

from pages.vodqa.wheel_picker_demo_page import WheelPickerDemoPage

# Color map for expected RGB values of the color box
# These are the expected RGB values when each color is selected
BOX_COLORS_MAP = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Black": (0, 0, 0),
}


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
            - Current color box element is visible and RGB color can be extracted
            - Color dropdown value is displayed
        """
        # Capture initial visual state of the color box and get RGB color
        rgb_color = wheel_picker_demo_page.capture_color_box_screenshot()

        # Assert multiple values using actual/expected pattern
        actual = {
            "has_color_text": "Current Color:" in wheel_picker_demo_page.current_color_text,
            "has_rgb_color": rgb_color is not None and isinstance(rgb_color, tuple) and len(rgb_color) == 3,
            "has_dropdown_value": len(wheel_picker_demo_page.color_dropdown_value) > 0,
        }

        expected = {
            "has_color_text": True,
            "has_rgb_color": True,
            "has_dropdown_value": True,
        }

        assert actual == expected, f"Wheel Picker Demo page elements mismatch: {actual}"

    @pytest.mark.tcid("TC-20-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test selecting color from dropdown updates visual state")
    @pytest.mark.parametrize("color", ["Red", "Green", "Blue"], ids=["red", "green", "blue"])
    def test_select_color_from_dropdown(self, wheel_picker_demo_page: WheelPickerDemoPage, color: str) -> None:
        """Verify that selecting a color from the dropdown updates the color box visual state.

        This test extracts RGB color values from the color box screenshot to verify
        that the color changes when a new color is selected from the dropdown.

        Args:
            color: The color name to select from dropdown.
        Expected:
            - Color can be selected from dropdown
            - Dropdown value updates to selected color
            - Current color text displays the selected color
            - Color box RGB values match the expected color
        """
        # Act - select the color
        wheel_picker_demo_page.select_color(color)

        # Capture the RGB color values from the color box after selection
        rgb_color = wheel_picker_demo_page.capture_color_box_screenshot()

        # Assert - verify the color was selected and RGB values match expected
        actual = {
            "dropdown_value": wheel_picker_demo_page.color_dropdown_value,
            "color_text_contains": color in wheel_picker_demo_page.current_color_text,
            "rgb_color": rgb_color,
        }

        expected = {
            "dropdown_value": color,
            "color_text_contains": True,
            "rgb_color": BOX_COLORS_MAP[color],
        }

        assert actual == expected, f"Color selection failed for {color}: {actual}"

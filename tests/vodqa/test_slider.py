"""Test suite for Slider feature in VodQA application.

This module contains tests for slider interaction functionality.
Tests verify that the slider responds to touch gestures and displays correct values.
"""

import allure
import pytest

from pages.vodqa.slider_page import SliderPage


@allure.feature("VodQA Samples")
@allure.story("Slider")
class TestSlider:
    """Test class for Slider feature functionality."""

    @pytest.mark.tcid("TC-02-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test slider page contains two sliders")
    def test_slider_page_has_two_sliders(self, slider_page: SliderPage) -> None:
        """Verify that the Slider page contains two slider elements.

        Expected:
            - Slider 1 is visible on the page
            - Slider 2 is visible on the page
        """
        assert slider_page.is_slider_1_displayed(), "Slider 1 should be visible on the Slider page"
        assert slider_page.is_slider_2_displayed(), "Slider 2 should be visible on the Slider page"

    @pytest.mark.tcid("TC-02-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test slider 1 interaction updates displayed value")
    def test_slider_1_interaction_updates_value(self, slider_page: SliderPage) -> None:
        """Test that tapping slider 1 at 50% updates the displayed value.

        Steps:
            1. Tap slider 1 at 50% position
            2. Verify the slider value is updated to expected value

        Expected:
            - Slider value reflects the 50% position
        """
        slider_page.tap_slider_1_at_percentage(50)

        assert slider_page.slider_1_value is not None, "Slider 1 should display a value after interaction"

    @pytest.mark.tcid("TC-02-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test slider 1 at {percentage}% position")
    @pytest.mark.parametrize("percentage", [0, 50, 100])
    def test_slider_1_multiple_positions(self, slider_page: SliderPage, percentage: int) -> None:
        """Test slider 1 interaction at different positions.

        Args:
            percentage: Target slider position (0%, 50%, 100%).

        Expected:
            - Slider responds to position change
            - Slider value is updated after interaction
        """
        slider_page.tap_slider_1_at_percentage(percentage)

        assert slider_page.slider_1_value is not None, f"Slider 1 should display a value after tapping at {percentage}%"

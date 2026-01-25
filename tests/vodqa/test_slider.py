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
        assert slider_page.is_slider_1_displayed, "Slider 1 should be visible on the Slider page"
        assert slider_page.is_slider_2_displayed, "Slider 2 should be visible on the Slider page"

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
        assert slider_page.slider_display_value == 50, "Slider 1 should display a value after interaction"

    @pytest.mark.tcid("TC-02-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test slider 1 at {percentage}% position")
    @pytest.mark.parametrize("percentage, expected_value", [(0, 0), (50, 64.0), (100, 1.0)], ids=["0%", "50%", "100%"])
    def test_slider_1_multiple_positions(self, slider_page: SliderPage, percentage: int, expected_value: float) -> None:
        """Test slider 1 interaction at different positions.
        Args:
            percentage: Target slider position (0%, 50%, 100%).
        Expected:
            - Slider responds to position change
            - Slider value is updated after interaction
        """
        slider_page.tap_slider_1_at_percentage(percentage)
        assert (
            slider_page.slider_1_value == expected_value
        ), f"Slider 1 should display a value after tapping at {percentage}%"


@allure.feature("VodQA Samples")
@allure.story("Slider Drag Gesture")
class TestSliderDragGesture:
    """Test class for Slider drag gesture functionality.

    These tests verify that sliders respond correctly to drag gestures,
    which simulate a finger dragging the slider thumb to a specific position.
    """

    @pytest.mark.tcid("TC-02-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag slider 1 to 75% position")
    def test_drag_slider_1_to_75_percent(self, slider_page: SliderPage) -> None:
        """Verify that dragging slider 1 to 75% position updates its value.

        Steps:
            1. Drag slider 1 thumb to 75% position
            2. Verify slider value is updated to approximately 75

        Expected:
            - Slider 1 value reflects approximately 75% position
        """
        slider_page.drag_slider_1_to_percentage(75)

        actual = {
            "is_displayed": slider_page.is_slider_1_displayed,
            "slider_value": slider_page.slider_1_value,
        }
        expected = {
            "is_displayed": True,
            "slider_value": 75.0,
        }

        assert actual == expected, f"Slider state mismatch: {actual}"

    @pytest.mark.tcid("TC-02-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag slider 2 to 25% position")
    def test_drag_slider_2_to_25_percent(self, slider_page: SliderPage) -> None:
        """Verify that dragging slider 2 to 25% position updates its value.

        Steps:
            1. Drag slider 2 thumb to 25% position
            2. Verify slider value is updated to approximately 25

        Expected:
            - Slider 2 value reflects approximately 25% position
        """
        slider_page.drag_slider_2_to_percentage(25)

        actual = {
            "is_displayed": slider_page.is_slider_2_displayed,
            "slider_value": slider_page.slider_2_value,
        }
        expected = {
            "is_displayed": True,
            "slider_value": 25.0,
        }

        assert actual == expected, f"Slider state mismatch: {actual}"

    @pytest.mark.tcid("TC-02-06")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag slider 1 to {target_percentage}% position")
    @pytest.mark.parametrize(
        "target_percentage, expected_value",
        [(0, 0.0), (25, 25.0), (50, 50.0), (75, 75.0), (100, 100.0)],
        ids=["0%", "25%", "50%", "75%", "100%"],
    )
    def test_drag_slider_1_multiple_positions(
        self, slider_page: SliderPage, target_percentage: int, expected_value: float
    ) -> None:
        """Test drag gesture on slider 1 at different target positions.

        Args:
            target_percentage: Target slider position (0-100%).
            expected_value: Expected slider value after drag.

        Expected:
            - Slider responds to drag gesture at specified position
            - Slider value matches expected value after drag
        """
        slider_page.drag_slider_1_to_percentage(target_percentage)

        actual = {
            "is_displayed": slider_page.is_slider_1_displayed,
            "slider_value": slider_page.slider_1_value,
        }
        expected = {
            "is_displayed": True,
            "slider_value": expected_value,
        }

        assert actual == expected, f"Slider state mismatch after dragging to {target_percentage}%: {actual}"

    @pytest.mark.tcid("TC-02-07")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag slider with different speeds")
    @pytest.mark.parametrize(
        "speed",
        [500, 1500, 3000],
        ids=["slow", "medium", "fast"],
    )
    def test_drag_slider_with_different_speeds(self, slider_page: SliderPage, speed: int) -> None:
        """Test drag gesture on slider with different drag speeds.

        Args:
            speed: Drag speed in pixels per second.

        Expected:
            - Drag gesture works correctly regardless of speed
            - Slider value is updated to target position (50%)
        """
        slider_page.drag_slider_1_to_percentage(50, speed=speed)

        actual = {
            "is_displayed": slider_page.is_slider_1_displayed,
            "slider_value": slider_page.slider_1_value,
        }
        expected = {
            "is_displayed": True,
            "slider_value": 50.0,
        }

        assert actual == expected, f"Slider state mismatch at speed {speed}: {actual}"

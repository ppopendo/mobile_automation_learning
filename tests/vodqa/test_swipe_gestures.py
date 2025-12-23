"""Test suite for Swipe Gestures in VodQA application.

This module contains tests for horizontal swipe gestures.
Tests verify swipe_left and swipe_right methods from BaseAppiumGestures using the Slider page.
"""

import allure
import pytest
from pages.vodqa.slider_page import SliderPage


@allure.feature("VodQA Samples")
@allure.story("Swipe Gestures")
class TestSwipeGestures:
    """Test class for horizontal swipe gesture functionality."""

    @pytest.mark.tcid("TC-07-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe_left gesture on element")
    def test_swipe_left_on_element(self, slider_page: SliderPage) -> None:
        """Verify that swipe_left gesture works on an element.
        Expected:
            - swipe_left method executes successfully
            - Swipe gesture is performed on target element
        """
        # Act - perform swipe left on slider element
        slider_page.swipe_left_slider_1()
        # Assert - verify slider was visible
        assert slider_page.is_slider_1_displayed, "Slider 1 should be visible"

    @pytest.mark.tcid("TC-07-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe_right gesture on element")
    def test_swipe_right_on_element(self, slider_page: SliderPage) -> None:
        """Verify that swipe_right gesture works on an element.
        Expected:
            - swipe_right method executes successfully
            - Swipe gesture is performed on target element
        """
        # Act - perform swipe right on slider element
        slider_page.swipe_right_slider_2()
        # Assert - verify slider was visible
        assert slider_page.is_slider_2_displayed, "Slider 2 should be visible"

    @pytest.mark.tcid("TC-07-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe left gesture with {percentage}% distance")
    @pytest.mark.parametrize("percentage", [0.5, 0.75], ids=["50%", "75%"])
    def test_swipe_with_different_percentages(self, slider_page: SliderPage, percentage: float) -> None:
        """Test swipe gestures with different swipe percentages.
        Args:
            percentage: Swipe distance as percentage (0.5, 0.75).
        Expected:
            - Swipe methods work with different percentages
            - Operations complete successfully regardless of percentage used
        """
        # Act - swipe left with specified percentage
        slider_page.swipe_left_slider_2(percentage=percentage)
        # Assert - verify slider was visible
        assert slider_page.is_slider_2_displayed, f"Slider 2 should be visible for swipe with {percentage*100}%"

    @pytest.mark.tcid("TC-07-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe right gesture with {speed} pixels per second")
    @pytest.mark.parametrize("speed", [1500, 2500], ids=["slow", "medium"])
    def test_swipe_with_different_speeds(self, slider_page: SliderPage, speed: int) -> None:
        """Test swipe gestures with different speed values.
        Args:
            speed: Swipe speed in pixels per second.
        Expected:
            - Swipe methods work with different speeds
            - Operations complete successfully regardless of speed used
        """
        # Act - swipe left with specified speed
        slider_page.swipe_right_slider_1(speed=speed)
        # Assert - verify slider was visible
        assert slider_page.is_slider_1_displayed, f"Slider 1 should be visible for swipe at {speed} speed"

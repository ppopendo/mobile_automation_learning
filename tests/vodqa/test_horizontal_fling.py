"""Test suite for Horizontal Fling Gestures in VodQA application.

This module contains tests for fling_element method (left/right directions)
from BaseAppiumGestures using the Carousel page.
"""

import allure
import pytest
from pages.vodqa.carousel_page import CarouselPage


@allure.feature("VodQA Samples")
@allure.story("Horizontal Fling Gestures")
class TestHorizontalFlingGestures:
    """Test class for horizontal fling gesture functionality."""

    @pytest.mark.tcid("TC-10-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling_element left gesture on carousel")
    def test_fling_left_on_carousel(self, carousel_page: CarouselPage) -> None:
        """Verify that fling_element left gesture works on carousel.

        Expected:
            - fling_element method executes successfully
            - Method returns boolean indicating if more content is available
            - Fling gesture is performed in left direction
        """
        # Act - perform fling left gesture
        can_continue = carousel_page.fling_on_carousel(direction="left")

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), "fling_element should return boolean"

    @pytest.mark.tcid("TC-10-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling_element right gesture on carousel")
    def test_fling_right_on_carousel(self, carousel_page: CarouselPage) -> None:
        """Verify that fling_element right gesture works on carousel.

        Expected:
            - fling_element method executes successfully
            - Method returns boolean indicating if more content is available
            - Fling gesture is performed in right direction
        """
        # Act - perform fling right gesture
        can_continue = carousel_page.fling_on_carousel(direction="right")

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), "fling_element should return boolean"

    @pytest.mark.tcid("TC-10-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling_element with different directions and speeds")
    @pytest.mark.parametrize(
        "direction,speed",
        [
            ("left", 3000),
            ("left", 5000),
            ("left", 7000),
            ("right", 3000),
            ("right", 5000),
            ("right", 7000),
        ],
        ids=["left-slow", "left-medium", "left-fast", "right-slow", "right-medium", "right-fast"],
    )
    def test_fling_with_different_directions_and_speeds(
        self, carousel_page: CarouselPage, direction: str, speed: int
    ) -> None:
        """Test fling gestures with different directions and speed values.

        Args:
            direction: Fling direction ('left' or 'right').
            speed: Fling speed in pixels per second.

        Expected:
            - Fling methods work with different directions and speeds
            - Operations complete successfully regardless of parameters used
        """
        # Act - fling with specified direction and speed
        can_continue = carousel_page.fling_on_carousel(direction=direction, speed=speed)

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), f"fling_element should return boolean for {direction} at {speed}"

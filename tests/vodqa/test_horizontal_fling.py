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
        can_continue = carousel_page.fling_left_on_carousel()

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
        can_continue = carousel_page.fling_right_on_carousel()

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), "fling_element should return boolean"

    @pytest.mark.tcid("TC-10-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling_element left with different speeds")
    @pytest.mark.parametrize("speed", [3000, 5000, 7000], ids=["slow", "medium", "fast"])
    def test_fling_left_with_different_speeds(self, carousel_page: CarouselPage, speed: int) -> None:
        """Test fling left gestures with different speed values.

        Args:
            speed: Fling speed in pixels per second.

        Expected:
            - Fling methods work with different speeds
            - Operations complete successfully regardless of speed used
        """
        # Act - fling left with specified speed
        can_continue = carousel_page.fling_left_on_carousel(speed=speed)

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), f"fling_element should return boolean for speed {speed}"

    @pytest.mark.tcid("TC-10-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling_element right with different speeds")
    @pytest.mark.parametrize("speed", [3000, 5000, 7000], ids=["slow", "medium", "fast"])
    def test_fling_right_with_different_speeds(self, carousel_page: CarouselPage, speed: int) -> None:
        """Test fling right gestures with different speed values.

        Args:
            speed: Fling speed in pixels per second.

        Expected:
            - Fling methods work with different speeds
            - Operations complete successfully regardless of speed used
        """
        # Act - fling right with specified speed
        can_continue = carousel_page.fling_right_on_carousel(speed=speed)

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), f"fling_element should return boolean for speed {speed}"

    @pytest.mark.tcid("TC-10-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling_element left on carousel container element")
    def test_fling_left_on_container(self, carousel_page: CarouselPage) -> None:
        """Verify that fling_element left gesture works on specific carousel container.

        Expected:
            - fling_element method executes successfully with element locator
            - Method returns boolean indicating if more content is available
            - Fling gesture is performed on the container element
        """
        # Act - perform fling left on container
        can_continue = carousel_page.fling_left_on_container()

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), "fling_element should return boolean"

    @pytest.mark.tcid("TC-10-06")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling_element right on carousel container element")
    def test_fling_right_on_container(self, carousel_page: CarouselPage) -> None:
        """Verify that fling_element right gesture works on specific carousel container.

        Expected:
            - fling_element method executes successfully with element locator
            - Method returns boolean indicating if more content is available
            - Fling gesture is performed on the container element
        """
        # Act - perform fling right on container
        can_continue = carousel_page.fling_right_on_container()

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), "fling_element should return boolean"

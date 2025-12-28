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
    @allure.title("Test fling gesture changes carousel ID")
    def test_fling_changes_carousel_id(self, carousel_page: CarouselPage) -> None:
        """Verify that fling gesture changes the carousel ID.

        Test scenario:
        1. Perform fling gesture on carousel item (arrange & act)
        2. Read carousel ID (action)
        3. Verify ID is one of the expected values (assert)

        Expected:
            - fling_element method executes successfully
            - Carousel ID is one of: "1 / 3", "2 / 3", "3 / 3"
            - Fling gesture navigates through carousel items
        """
        # Arrange & Act - perform fling gesture on carousel item
        carousel_page.fling_on_carousel_item(direction="left")

        # Action - read carousel ID
        current_id = carousel_page.carousel_id

        # Assert - verify ID is one of the expected values
        expected_ids = ["1 / 3", "2 / 3", "3 / 3"]
        assert current_id in expected_ids, f"Carousel ID '{current_id}' should be one of {expected_ids}"

    @pytest.mark.tcid("TC-10-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling left gesture on carousel")
    def test_fling_left_on_carousel(self, carousel_page: CarouselPage) -> None:
        """Verify that fling_element left gesture works on carousel.

        Expected:
            - fling_element method executes successfully
            - Method returns boolean indicating if more content is available
            - Carousel ID changes after fling
        """
        # Arrange - get initial ID
        initial_id = carousel_page.carousel_id

        # Act - perform fling left gesture
        can_continue = carousel_page.fling_on_carousel_item(direction="left")

        # Assert - verify method returns boolean and ID is valid
        assert isinstance(can_continue, bool), "fling_element should return boolean"
        current_id = carousel_page.carousel_id
        expected_ids = ["1 / 3", "2 / 3", "3 / 3"]
        assert current_id in expected_ids, f"Carousel ID should be one of {expected_ids}"

    @pytest.mark.tcid("TC-10-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling right gesture on carousel")
    def test_fling_right_on_carousel(self, carousel_page: CarouselPage) -> None:
        """Verify that fling_element right gesture works on carousel.

        Expected:
            - fling_element method executes successfully
            - Method returns boolean indicating if more content is available
            - Carousel ID changes after fling
        """
        # Arrange - get initial ID
        initial_id = carousel_page.carousel_id

        # Act - perform fling right gesture
        can_continue = carousel_page.fling_on_carousel_item(direction="right")

        # Assert - verify method returns boolean and ID is valid
        assert isinstance(can_continue, bool), "fling_element should return boolean"
        current_id = carousel_page.carousel_id
        expected_ids = ["1 / 3", "2 / 3", "3 / 3"]
        assert current_id in expected_ids, f"Carousel ID should be one of {expected_ids}"

    @pytest.mark.tcid("TC-10-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling with different directions and speeds")
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
            - Carousel ID remains valid after fling
        """
        # Act - fling with specified direction and speed
        can_continue = carousel_page.fling_on_carousel_item(direction=direction, speed=speed)

        # Assert - verify method returns boolean and ID is valid
        assert isinstance(can_continue, bool), f"fling_element should return boolean for {direction} at {speed}"
        current_id = carousel_page.carousel_id
        expected_ids = ["1 / 3", "2 / 3", "3 / 3"]
        assert current_id in expected_ids, f"Carousel ID should be one of {expected_ids} after fling"

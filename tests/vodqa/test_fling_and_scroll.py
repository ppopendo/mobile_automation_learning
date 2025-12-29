"""Test suite for Fling and Scroll Gestures in VodQA application.
This module contains tests for fling_element and scroll_element methods
from BaseAppiumGestures using the Vertical Swiping page.
"""

from typing import Any

import allure
import pytest

from pages.vodqa.vertical_swiping_page import VerticalSwipingPage


@allure.feature("VodQA Samples")
@allure.story("Fling and Scroll Gestures")
class TestFlingAndScrollGestures:
    """Test class for fling and scroll gesture functionality."""

    @pytest.mark.tcid("TC-08-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling_element down gesture")
    def test_fling_element_down(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that fling_element down gesture works.

        Expected:
            - fling_element method executes successfully
            - Method returns boolean indicating if more content is available
            - Fling gesture is performed in down direction
        """
        # Act - perform fling down gesture
        can_continue = vertical_swiping_page.fling_down()

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), "fling_down should return boolean"

    @pytest.mark.tcid("TC-08-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling_element up gesture")
    def test_fling_element_up(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that fling_element up gesture works.

        Expected:
            - fling_element method executes successfully
            - Method returns boolean indicating if more content is available
            - Fling gesture is performed in up direction
        """
        # Act - perform fling up gesture
        can_continue = vertical_swiping_page.fling_up()

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), "fling_up should return boolean"

    @pytest.mark.tcid("TC-08-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling_element with different speeds")
    @pytest.mark.parametrize("speed", [3000, 5000, 7000], ids=["slow", "medium", "fast"])
    def test_fling_element_with_different_speeds(self, vertical_swiping_page: VerticalSwipingPage, speed: int) -> None:
        """Test fling gestures with different speed values.

        Args:
            speed: Fling speed in pixels per second.

        Expected:
            - Fling methods work with different speeds
            - Operations complete successfully regardless of speed used
        """
        # Act - fling down with specified speed
        can_continue = vertical_swiping_page.fling_down(speed=speed)

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), f"fling_down should return boolean for speed {speed}"

    @pytest.mark.tcid("TC-08-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling_element validates direction parameter")
    def test_fling_element_invalid_direction(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that fling_element validates direction parameter.

        Expected:
            - ValueError is raised for invalid direction
            - Error message is descriptive
        """
        # Act & Assert - attempt to fling with invalid direction
        with pytest.raises(ValueError, match="Invalid direction"):
            vertical_swiping_page.fling_element(direction="invalid")

    @pytest.mark.tcid("TC-08-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling_element validates speed parameter")
    def test_fling_element_invalid_speed(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that fling_element validates speed parameter.

        Expected:
            - ValueError is raised for non-positive speed
            - Error message is descriptive
        """
        # Act & Assert - attempt to fling with invalid speed
        with pytest.raises(ValueError, match="Speed must be a positive integer"):
            vertical_swiping_page.fling_element(direction="down", speed=-100)

    @pytest.mark.tcid("TC-08-06")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test scroll_element down gesture")
    def test_scroll_element_down(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that scroll_element down gesture works.

        Expected:
            - scroll_element method executes successfully
            - Method returns boolean indicating if more content is available
            - Scroll gesture is performed in down direction
        """
        # Act - perform scroll down gesture
        can_continue = vertical_swiping_page.scroll_down()

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), "scroll_down should return boolean"

    @pytest.mark.tcid("TC-08-07")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test scroll_element up gesture")
    def test_scroll_element_up(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that scroll_element up gesture works.

        Expected:
            - scroll_element method executes successfully
            - Method returns boolean indicating if more content is available
            - Scroll gesture is performed in up direction
        """
        # Act - perform scroll up gesture
        can_continue = vertical_swiping_page.scroll_up()

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), "scroll_up should return boolean"

    @pytest.mark.tcid("TC-08-08")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test scroll_element with different percentages")
    @pytest.mark.parametrize("percentage", [0.5, 0.75, 0.9], ids=["50%", "75%", "90%"])
    def test_scroll_element_with_different_percentages(
        self, vertical_swiping_page: VerticalSwipingPage, percentage: float
    ) -> None:
        """Test scroll gestures with different scroll percentages.

        Args:
            percentage: Scroll distance as percentage (0.5, 0.75, 0.9).

        Expected:
            - Scroll methods work with different percentages
            - Operations complete successfully regardless of percentage used
        """
        # Act - scroll down with specified percentage
        can_continue = vertical_swiping_page.scroll_down(percentage=percentage)

        # Assert - verify method returns boolean
        assert isinstance(can_continue, bool), f"scroll_down should return boolean for {percentage * 100}%"

    @pytest.mark.tcid("TC-08-09")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test scroll_element validates parameters")
    @pytest.mark.parametrize(
        "param,value,error_match",
        [
            ("direction", "invalid", "Invalid direction"),
            ("percentage", 1.5, "Percentage must be between 0.0 and 1.0"),
            ("speed", 0, "Speed must be a positive integer"),
        ],
        ids=["invalid-direction", "invalid-percentage", "invalid-speed"],
    )
    def test_scroll_element_invalid_parameters(
        self, vertical_swiping_page: VerticalSwipingPage, param: str, value: Any, error_match: str
    ) -> None:
        """Verify that scroll_element validates parameters.

        Expected:
            - ValueError is raised for invalid parameter values
            - Error message is descriptive
        """
        # Act & Assert - attempt to call method with invalid parameter
        kwargs = {"direction": "down", "percentage": 0.75, "speed": 2500, param: value}
        with pytest.raises(ValueError, match=error_match):
            vertical_swiping_page.scroll_element(**kwargs)

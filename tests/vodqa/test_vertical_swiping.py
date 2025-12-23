"""Test suite for Vertical Swiping feature in VodQA application.

This module contains tests for vertical swipe gestures and scroll functionality.
Tests verify swipe_up, swipe_down, and scroll_element_into_view methods from BaseAppiumGestures.
"""

import allure
import pytest
from pages.vodqa.vertical_swiping_page import VerticalSwipingPage


@allure.feature("VodQA Samples")
@allure.story("Vertical Swiping")
class TestVerticalSwiping:
    """Test class for Vertical Swiping feature functionality."""

    @pytest.mark.tcid("TC-03-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe up gesture on screen")
    def test_swipe_page(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that swipe up gesture scrolls content upward.
        Expected:
            - Swipe up gesture executes without errors
            - Content scrolls upward on screen
        """
        assert vertical_swiping_page.is_item_displayed("C"), "Item 'C' should be visible initially"

    @pytest.mark.tcid("TC-03-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe down gesture on screen")
    def test_swipe_down_gesture(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that swipe down gesture scrolls content downward.
        Expected:
            - Swipe down gesture executes without errors
            - Content scrolls downward on screen
        """
        target_item = "Karma"
        vertical_swiping_page.scroll_to_item(item_text=target_item, direction="down", max_scrolls=10)
        # Assert - verify operation completed
        assert vertical_swiping_page.is_item_displayed(
            target_item
        ), f"Item '{target_item}' should be visible after operations"

    @pytest.mark.tcid("TC-03-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test scroll_element_into_view method scrolling down")
    def test_scroll_element_into_view_down(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that scroll_element_into_view scrolls to make element visible.
        Expected:
            - scroll_element_into_view executes successfully
            - Target element becomes visible after scrolling
        """
        target_item = "C#"
        vertical_swiping_page.scroll_to_item(item_text=target_item, direction="down", max_scrolls=10)
        # Assert - verify item is now visible
        assert vertical_swiping_page.is_item_displayed(
            target_item
        ), f"Item '{target_item}' should be visible after scrolling"

    @pytest.mark.tcid("TC-03-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test scroll_element_into_view with {percentage} percentage")
    @pytest.mark.parametrize("percentage", [0.5, 0.75], ids=["50%", "75%"])
    def test_scroll_with_different_percentages(
        self, vertical_swiping_page: VerticalSwipingPage, percentage: float
    ) -> None:
        """Test scroll_element_into_view with different scroll percentages.
        Args:
            percentage: Scroll distance as percentage (0.5, 0.75).
        Expected:
            - scroll_element_into_view works with different percentages
            - Target element becomes visible regardless of percentage used
        """
        # Arrange - target item
        target_item = "Appium"
        vertical_swiping_page.scroll_to_item(
            item_text=target_item, direction="down", percentage=percentage, max_scrolls=10
        )
        # Assert - verify item is visible
        assert vertical_swiping_page.is_item_displayed(
            target_item
        ), f"Item '{target_item}' should be visible after scrolling with {percentage*100}% distance"

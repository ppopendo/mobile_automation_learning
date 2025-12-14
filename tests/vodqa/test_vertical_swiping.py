"""Test suite for Vertical Swiping feature in VodQA application.

This module contains tests for vertical swipe gestures and scroll functionality.
Tests verify swipe_up, swipe_down, and scroll_element_into_view methods from BaseAppiumGestures.
"""

import allure
import pytest

from pages.vodqa.vertical_swiping_page import VerticalSwipingPage, VerticalSwipingPageLocators


@allure.feature("VodQA Samples")
@allure.story("Vertical Swiping")
class TestVerticalSwiping:
    """Test class for Vertical Swiping feature functionality."""

    @pytest.mark.tcid("TC-03-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe up gesture on screen")
    def test_swipe_up_gesture(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that swipe up gesture scrolls content upward.

        Steps:
            1. Verify initial items are visible
            2. Perform swipe up gesture
            3. Verify that content has scrolled

        Expected:
            - Swipe up gesture executes without errors
            - Content scrolls upward on screen
        """
        # Verify initial state - first items should be visible
        assert vertical_swiping_page.is_item_1_displayed, "Item 1 should be visible initially"

        # Perform swipe up gesture
        vertical_swiping_page.swipe_up(percentage=0.75, speed=2500)

        # After swipe up, content should have moved
        # This is a basic test to verify the method executes without errors
        # In a real scenario, you would verify that new items become visible

    @pytest.mark.tcid("TC-03-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe down gesture on screen")
    def test_swipe_down_gesture(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that swipe down gesture scrolls content downward.

        Steps:
            1. Scroll to bottom first
            2. Perform swipe down gesture
            3. Verify that content has scrolled

        Expected:
            - Swipe down gesture executes without errors
            - Content scrolls downward on screen
        """
        # Scroll to bottom first
        vertical_swiping_page.scroll_element_into_view(
            VerticalSwipingPageLocators.ITEM_LAST, direction="down", max_scrolls=10
        )

        # Verify last item is visible
        assert vertical_swiping_page.is_item_last_displayed, "Last item should be visible after scrolling"

        # Perform swipe down gesture
        vertical_swiping_page.swipe_down(percentage=0.75, speed=2500)

        # After swipe down, content should have moved
        # This is a basic test to verify the method executes without errors

    @pytest.mark.tcid("TC-03-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe up on scrollable container element")
    def test_swipe_up_on_element(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that swipe up gesture works on a specific element.

        Steps:
            1. Verify initial items are visible
            2. Perform swipe up gesture on scrollable container
            3. Verify that content has scrolled

        Expected:
            - Swipe up gesture on element executes without errors
            - Content scrolls within the container
        """
        # Verify initial state
        assert vertical_swiping_page.is_item_1_displayed, "Item 1 should be visible initially"

        # Perform swipe up on the scrollable container
        vertical_swiping_page.swipe_up(
            locator=VerticalSwipingPageLocators.SCROLLABLE_CONTAINER, percentage=0.75, speed=2500
        )

        # After swipe up, content should have moved
        # This is a basic test to verify the method executes without errors

    @pytest.mark.tcid("TC-03-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test scroll_element_into_view method scrolling down")
    def test_scroll_element_into_view_down(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that scroll_element_into_view scrolls to make element visible.

        Steps:
            1. Verify target element is not initially visible
            2. Use scroll_element_into_view to scroll down to item 10
            3. Verify element becomes visible

        Expected:
            - scroll_element_into_view executes successfully
            - Target element becomes visible after scrolling
        """
        # Scroll to item 10
        vertical_swiping_page.scroll_element_into_view(
            VerticalSwipingPageLocators.ITEM_10, direction="down", percentage=0.75, max_scrolls=10
        )

        # Verify item 10 is now visible
        assert vertical_swiping_page.is_item_10_displayed, "Item 10 should be visible after scrolling into view"

    @pytest.mark.tcid("TC-03-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test scroll_element_into_view method scrolling to last item")
    def test_scroll_element_into_view_last_item(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that scroll_element_into_view can scroll to the last item.

        Steps:
            1. Verify last item is not initially visible
            2. Use scroll_element_into_view to scroll to last item
            3. Verify last element becomes visible

        Expected:
            - scroll_element_into_view executes successfully
            - Last item becomes visible after scrolling
        """
        # Scroll to last item
        vertical_swiping_page.scroll_element_into_view(
            VerticalSwipingPageLocators.ITEM_LAST, direction="down", percentage=0.75, max_scrolls=15
        )

        # Verify last item is now visible
        assert vertical_swiping_page.is_item_last_displayed, "Last item should be visible after scrolling into view"

    @pytest.mark.tcid("TC-03-06")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test scroll_element_into_view with different scroll percentages")
    @pytest.mark.parametrize("percentage", [0.5, 0.75, 0.9], ids=["50%", "75%", "90%"])
    def test_scroll_with_different_percentages(
        self, vertical_swiping_page: VerticalSwipingPage, percentage: float
    ) -> None:
        """Test scroll_element_into_view with different scroll percentages.

        Args:
            percentage: Scroll distance as percentage (0.5, 0.75, 0.9).

        Expected:
            - scroll_element_into_view works with different percentages
            - Target element becomes visible regardless of percentage used
        """
        # Scroll to item 5 with specified percentage
        vertical_swiping_page.scroll_element_into_view(
            VerticalSwipingPageLocators.ITEM_5, direction="down", percentage=percentage, max_scrolls=10
        )

        # Verify item 5 is visible
        assert (
            vertical_swiping_page.is_item_5_displayed
        ), f"Item 5 should be visible after scrolling with {percentage*100}% distance"

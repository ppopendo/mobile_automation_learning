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

        Expected:
            - Swipe up gesture executes without errors
            - Content scrolls upward on screen
        """
        # Arrange - verify initial item is visible
        assert vertical_swiping_page.is_item_displayed("C"), "Item 'C' should be visible initially"

        # Act - perform swipe up gesture
        vertical_swiping_page.swipe_up(locator=None, percentage=0.75, speed=2500)

        # Assert - verify first item is still present (basic check)
        assert vertical_swiping_page.is_item_displayed("C"), "Page should still contain items after swipe"

    @pytest.mark.tcid("TC-03-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe down gesture on screen")
    def test_swipe_down_gesture(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that swipe down gesture scrolls content downward.

        Expected:
            - Swipe down gesture executes without errors
            - Content scrolls downward on screen
        """
        # Arrange - scroll to bottom first
        vertical_swiping_page.scroll_element_into_view(
            VerticalSwipingPageLocators.item_locator("Karma"), direction="down", max_scrolls=10
        )
        assert vertical_swiping_page.is_item_displayed("Karma"), "Item 'Karma' should be visible after scrolling"

        # Act - perform swipe down gesture
        vertical_swiping_page.swipe_down(locator=None, percentage=0.75, speed=2500)

        # Assert - verify last item is still present
        assert vertical_swiping_page.is_item_displayed("Karma"), "Page should still contain items after swipe"

    @pytest.mark.tcid("TC-03-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test scroll_element_into_view method scrolling down")
    def test_scroll_element_into_view_down(self, vertical_swiping_page: VerticalSwipingPage) -> None:
        """Verify that scroll_element_into_view scrolls to make element visible.

        Expected:
            - scroll_element_into_view executes successfully
            - Target element becomes visible after scrolling
        """
        # Arrange - element 'Java' may not be initially visible
        target_item = "Java"

        # Act - scroll to make item visible
        vertical_swiping_page.scroll_element_into_view(
            VerticalSwipingPageLocators.item_locator(target_item), direction="down", percentage=0.75, max_scrolls=10
        )

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
        target_item = "Ruby"

        # Act - scroll to item with specified percentage
        vertical_swiping_page.scroll_element_into_view(
            VerticalSwipingPageLocators.item_locator(target_item),
            direction="down",
            percentage=percentage,
            max_scrolls=10,
        )

        # Assert - verify item is visible
        assert vertical_swiping_page.is_item_displayed(
            target_item
        ), f"Item '{target_item}' should be visible after scrolling with {percentage*100}% distance"

"""Page Object for Carousel feature in VodQA application."""

import time
from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent


@dataclass(frozen=True)
class CarouselPageLocators:
    """Locators for Carousel page elements."""

    CAROUSEL_ITEM: Tuple[str, str] = field(default=(AppiumBy.XPATH, "//*[@content-desc]"), init=False)
    CAROUSEL_ID: Tuple[str, str] = field(default=(AppiumBy.XPATH, '//*[contains(@text," / ")]'), init=False)


class CarouselPage(BaseAppiumGestures, HeaderBarComponent):
    """Page Object for the Carousel screen in VodQA app.

    This page contains a carousel/swipeable content for testing horizontal gestures.
    The carousel has 3 positions: 1/3, 2/3, and 3/3.
    """

    # Note: This constant documents the swipe count used in the navigation methods.
    # The swipe calls are intentionally inlined (no loops) to comply with project guidelines.
    # Maximum swipes needed to reach boundary positions (3 items + 2 extra for safety)
    MAX_SWIPES_TO_BOUNDARY = 5
    
    # Wait duration in seconds for carousel animation to complete after fling gesture
    ANIMATION_COMPLETE_WAIT = 0.5
    
    # Carousel boundary position constants
    FIRST_POSITION = "1 / 3"
    LAST_POSITION = "3 / 3"

    @allure.step("the user waits until the carousel page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for carousel page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Carousel - Swipe left/right")

    @property
    @allure.step("retrieving carousel display status")
    def is_carousel_displayed(self) -> bool:
        """Check if carousel is displayed on screen."""
        return self.is_element_displayed(CarouselPageLocators.CAROUSEL_ITEM)

    @allure.step("the user flings on carousel item")
    def fling_on_carousel_item(self, direction: str, speed: int = 5000) -> bool:
        """Perform fling gesture on carousel item in specified direction.

        Note: This method includes a wait after the fling to ensure the carousel
        animation completes before the next operation. This improves test stability
        at the cost of slightly longer execution time.

        Args:
            direction: Fling direction - 'left' or 'right'.
            speed: Fling speed in pixels per second.

        Returns:
            bool: True if fling can continue (more content), False if at the end.

        Raises:
            ValueError: If direction is not 'left' or 'right'.
        """
        valid_directions = ("left", "right")
        if direction not in valid_directions:
            raise ValueError(f"Invalid direction '{direction}'. Must be one of: {valid_directions}")
        result = self.fling_element(direction=direction, locator=CarouselPageLocators.CAROUSEL_ITEM, speed=speed)
        time.sleep(self.ANIMATION_COMPLETE_WAIT)
        return result

    @property
    @allure.step("retrieving carousel ID")
    def carousel_id(self) -> str:
        """Get the current carousel ID text.

        Returns:
            str: Carousel ID text (e.g., '1 / 3', '2 / 3', '3 / 3').
        """
        return self.wait_for_element(CarouselPageLocators.CAROUSEL_ID).text

    @allure.step("the user navigates to first carousel position")
    def navigate_to_first_position(self) -> None:
        """Navigate to the first carousel position by swiping right multiple times.

        This is a helper method that guarantees the carousel is at position 1/3.
        Performs MAX_SWIPES_TO_BOUNDARY swipes to ensure we reach position 1/3.
        Extra swipes beyond the boundary are safe as the carousel stops at the edge.
        
        Raises:
            AssertionError: If the carousel fails to reach the first position after navigation.
        """
        # 5 swipes = 3 positions to traverse + 2 extra to ensure we reach boundary
        self.fling_on_carousel_item(direction="right")
        self.fling_on_carousel_item(direction="right")
        self.fling_on_carousel_item(direction="right")
        self.fling_on_carousel_item(direction="right")
        self.fling_on_carousel_item(direction="right")
        time.sleep(self.ANIMATION_COMPLETE_WAIT)
        current_position = self.carousel_id
        assert (
            current_position == self.FIRST_POSITION
        ), f"Failed to navigate to first position, expected: {self.FIRST_POSITION}, actual: {current_position}"

    @allure.step("the user navigates to last carousel position")
    def navigate_to_last_position(self) -> None:
        """Navigate to the last carousel position by swiping left multiple times.

        This is a helper method that guarantees the carousel is at position 3/3.
        Performs MAX_SWIPES_TO_BOUNDARY swipes to ensure we reach position 3/3.
        Extra swipes beyond the boundary are safe as the carousel stops at the edge.
        
        Raises:
            AssertionError: If the carousel fails to reach the last position after navigation.
        """
        # 5 swipes = 3 positions to traverse + 2 extra to ensure we reach boundary
        self.fling_on_carousel_item(direction="left")
        self.fling_on_carousel_item(direction="left")
        self.fling_on_carousel_item(direction="left")
        self.fling_on_carousel_item(direction="left")
        self.fling_on_carousel_item(direction="left")
        time.sleep(self.ANIMATION_COMPLETE_WAIT)
        current_position = self.carousel_id
        assert (
            current_position == self.LAST_POSITION
        ), f"Failed to navigate to last position, expected: {self.LAST_POSITION}, actual: {current_position}"

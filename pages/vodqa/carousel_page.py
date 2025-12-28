"""Page Object for Carousel feature in VodQA application."""

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
    """

    @allure.step("the user waits until the carousel page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for carousel page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Carousel - Swipe left/right")

    @property
    @allure.step("checking if carousel is displayed")
    def is_carousel_displayed(self) -> bool:
        """Check if carousel is displayed on screen."""
        return self.is_element_displayed(CarouselPageLocators.CAROUSEL_ITEM)

    @allure.step("the user flings on carousel item")
    def fling_on_carousel_item(self, direction: str, speed: int = 5000) -> bool:
        """Perform fling gesture on carousel item in specified direction.

        Args:
            direction: Fling direction - 'left' or 'right'.
            speed: Fling speed in pixels per second.

        Returns:
            bool: True if fling can continue (more content), False if at the end.

        Raises:
            ValueError: If direction is not 'left' or 'right'.
        """
        if direction not in ("left", "right"):
            raise ValueError(f"Invalid direction '{direction}'. Must be 'left' or 'right'.")
        return self.fling_element(direction=direction, locator=CarouselPageLocators.CAROUSEL_ITEM, speed=speed)

    @property
    @allure.step("retrieving carousel ID")
    def carousel_id(self) -> str:
        """Get the current carousel ID text.

        Returns:
            str: Carousel ID text (e.g., '1 / 3', '2 / 3', '3 / 3').
        """
        return self.wait_for_element(CarouselPageLocators.CAROUSEL_ID).text

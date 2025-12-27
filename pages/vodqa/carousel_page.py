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

    CAROUSEL_CONTAINER: Tuple[str, str] = field(default=(AppiumBy.XPATH, "//android.widget.ScrollView"), init=False)
    CAROUSEL_ITEM: Tuple[str, str] = field(default=(AppiumBy.XPATH, "//android.widget.ImageView"), init=False)


class CarouselPage(BaseAppiumGestures, HeaderBarComponent):
    """Page Object for the Carousel screen in VodQA app.

    This page contains a carousel/swipeable content for testing horizontal gestures.
    """

    @allure.step("the user waits until the carousel page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for carousel page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Carousel")

    @property
    @allure.step("checking if carousel is displayed")
    def is_carousel_displayed(self) -> bool:
        """Check if carousel is displayed on screen."""
        return self.is_element_displayed(CarouselPageLocators.CAROUSEL_CONTAINER)

    @allure.step("the user flings left on carousel")
    def fling_left_on_carousel(self, speed: int = 5000) -> bool:
        """Perform fling left gesture on carousel.

        Args:
            speed: Fling speed in pixels per second.

        Returns:
            bool: True if fling can continue (more content), False if at the end.
        """
        return self.fling_element(direction="left", speed=speed)

    @allure.step("the user flings right on carousel")
    def fling_right_on_carousel(self, speed: int = 5000) -> bool:
        """Perform fling right gesture on carousel.

        Args:
            speed: Fling speed in pixels per second.

        Returns:
            bool: True if fling can continue (more content), False if at the end.
        """
        return self.fling_element(direction="right", speed=speed)

    @allure.step("the user flings left on carousel container")
    def fling_left_on_container(self, speed: int = 5000) -> bool:
        """Perform fling left gesture on carousel container element.

        Args:
            speed: Fling speed in pixels per second.

        Returns:
            bool: True if fling can continue (more content), False if at the end.
        """
        return self.fling_element(direction="left", locator=CarouselPageLocators.CAROUSEL_CONTAINER, speed=speed)

    @allure.step("the user flings right on carousel container")
    def fling_right_on_container(self, speed: int = 5000) -> bool:
        """Perform fling right gesture on carousel container element.

        Args:
            speed: Fling speed in pixels per second.

        Returns:
            bool: True if fling can continue (more content), False if at the end.
        """
        return self.fling_element(direction="right", locator=CarouselPageLocators.CAROUSEL_CONTAINER, speed=speed)

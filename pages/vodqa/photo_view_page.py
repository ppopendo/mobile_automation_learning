"""Page Object for Photo View feature in VodQA application."""

from dataclasses import dataclass, field
from typing import Dict, Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent


@dataclass(frozen=True)
class PhotoViewPageLocators:
    """Locators for Photo View page elements."""

    PHOTO_IMAGE: Tuple[str, str] = field(default=(AppiumBy.XPATH, "(//android.widget.ImageView)[1]"), init=False)


class PhotoViewPage(BaseAppiumGestures, HeaderBarComponent):
    """Page Object for the Photo View screen in VodQA app.

    This page contains an image for testing zoom and pan gestures.
    """

    @allure.step("the user waits until the photo view page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for photo view page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Photos - Ping & Zoom")

    @property
    @allure.step("retrieving photo display status")
    def is_photo_displayed(self) -> bool:
        """Check if photo image is displayed on screen."""
        return self.is_element_displayed(PhotoViewPageLocators.PHOTO_IMAGE)

    @allure.step("the user performs pinch open (zoom in) on photo")
    def pinch_open_on_photo(self, percentage: float = 0.75, speed: int = 2500) -> None:
        """Perform pinch open (zoom in) gesture on the photo image.

        Args:
            percentage: Pinch distance as percentage (0.0-1.0).
            speed: Pinch speed in pixels per second.
        """
        self.pinch_open(locator=PhotoViewPageLocators.PHOTO_IMAGE, percentage=percentage, speed=speed)

    @allure.step("the user performs pinch close (zoom out) on photo")
    def pinch_close_on_photo(self, percentage: float = 0.75, speed: int = 2500) -> None:
        """Perform pinch close (zoom out) gesture on the photo image.

        Args:
            percentage: Pinch distance as percentage (0.0-1.0).
            speed: Pinch speed in pixels per second.
        """
        self.pinch_close(locator=PhotoViewPageLocators.PHOTO_IMAGE, percentage=percentage, speed=speed)

    @allure.step("the user performs pinch open (zoom in) without specific element")
    def pinch_open_on_screen(self, percentage: float = 0.75, speed: int = 2500) -> None:
        """Perform pinch open (zoom in) gesture on screen center.

        Args:
            percentage: Pinch distance as percentage (0.0-1.0).
            speed: Pinch speed in pixels per second.
        """
        self.pinch_open(percentage=percentage, speed=speed)

    @allure.step("the user performs pinch close (zoom out) without specific element")
    def pinch_close_on_screen(self, percentage: float = 0.75, speed: int = 2500) -> None:
        """Perform pinch close (zoom out) gesture on screen center.

        Args:
            percentage: Pinch distance as percentage (0.0-1.0).
            speed: Pinch speed in pixels per second.
        """
        self.pinch_close(percentage=percentage, speed=speed)

    @property
    @allure.step("retrieving photo image size")
    def photo_image_size(self) -> Dict[str, int]:
        """Get the current size of the photo image element.

        Returns:
            dict: Dictionary with 'width' and 'height' keys.
        """
        element = self.wait_for_element(PhotoViewPageLocators.PHOTO_IMAGE)
        return element.size

    @property
    @allure.step("retrieving photo image location")
    def photo_image_location(self) -> Dict[str, int]:
        """Get the current location of the photo image element.

        Returns:
            dict: Dictionary with 'x' and 'y' keys representing top-left coordinates.
        """
        element = self.wait_for_element(PhotoViewPageLocators.PHOTO_IMAGE)
        return element.location

    # ==================== PAN GESTURES ====================

    @allure.step("the user performs pan up on photo")
    def pan_up_on_photo(self, percentage: float = 0.5, speed: int = 2500) -> None:
        """Perform pan up gesture on the photo image.

        Args:
            percentage: Pan distance as percentage of element height (0.0-1.0).
            speed: Pan speed in pixels per second.
        """
        self.swipe_up(locator=PhotoViewPageLocators.PHOTO_IMAGE, percentage=percentage, speed=speed)

    @allure.step("the user performs pan down on photo")
    def pan_down_on_photo(self, percentage: float = 0.5, speed: int = 2500) -> None:
        """Perform pan down gesture on the photo image.

        Args:
            percentage: Pan distance as percentage of element height (0.0-1.0).
            speed: Pan speed in pixels per second.
        """
        self.swipe_down(locator=PhotoViewPageLocators.PHOTO_IMAGE, percentage=percentage, speed=speed)

    @allure.step("the user performs pan left on photo")
    def pan_left_on_photo(self, percentage: float = 0.5, speed: int = 2500) -> None:
        """Perform pan left gesture on the photo image.

        Args:
            percentage: Pan distance as percentage of element width (0.0-1.0).
            speed: Pan speed in pixels per second.
        """
        self.swipe_left(locator=PhotoViewPageLocators.PHOTO_IMAGE, percentage=percentage, speed=speed)

    @allure.step("the user performs pan right on photo")
    def pan_right_on_photo(self, percentage: float = 0.5, speed: int = 2500) -> None:
        """Perform pan right gesture on the photo image.

        Args:
            percentage: Pan distance as percentage of element width (0.0-1.0).
            speed: Pan speed in pixels per second.
        """
        self.swipe_right(locator=PhotoViewPageLocators.PHOTO_IMAGE, percentage=percentage, speed=speed)

    @allure.step("the user performs pan up on screen center")
    def pan_up_on_screen(self, percentage: float = 0.5, speed: int = 2500) -> None:
        """Perform pan up gesture on screen center.

        Args:
            percentage: Pan distance as percentage of screen height (0.0-1.0).
            speed: Pan speed in pixels per second.
        """
        self.swipe_up(percentage=percentage, speed=speed)

    @allure.step("the user performs pan down on screen center")
    def pan_down_on_screen(self, percentage: float = 0.5, speed: int = 2500) -> None:
        """Perform pan down gesture on screen center.

        Args:
            percentage: Pan distance as percentage of screen height (0.0-1.0).
            speed: Pan speed in pixels per second.
        """
        self.swipe_down(percentage=percentage, speed=speed)

    @allure.step("the user performs pan left on screen center")
    def pan_left_on_screen(self, percentage: float = 0.5, speed: int = 2500) -> None:
        """Perform pan left gesture on screen center.

        Args:
            percentage: Pan distance as percentage of screen width (0.0-1.0).
            speed: Pan speed in pixels per second.
        """
        self.swipe_left(percentage=percentage, speed=speed)

    @allure.step("the user performs pan right on screen center")
    def pan_right_on_screen(self, percentage: float = 0.5, speed: int = 2500) -> None:
        """Perform pan right gesture on screen center.

        Args:
            percentage: Pan distance as percentage of screen width (0.0-1.0).
            speed: Pan speed in pixels per second.
        """
        self.swipe_right(percentage=percentage, speed=speed)

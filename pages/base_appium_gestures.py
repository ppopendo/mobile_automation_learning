"""Base class for Appium gestures using appium-gestures-plugin.

This module provides gesture methods using the appium-gestures-plugin.
The plugin must be installed and enabled on the Appium server.
See: https://github.com/AppiumTestDistribution/appium-gestures-plugin
"""

import logging
from typing import Optional, Tuple
import allure
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.config_vars import SHORT_TIMEOUT, TIMEOUT
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class BaseAppiumGestures(BasePage):
    """Base class providing gesture methods using appium-gestures-plugin.

    This class uses the appium-gestures-plugin for executing mobile gestures.
    All methods use the `mobile: *Gesture` execute_script commands.
    """

    def __init__(self, driver: webdriver.Remote) -> None:
        """Initialize the gestures handler.

        Args:
            driver: Appium WebDriver instance.
        """
        super().__init__(driver)
        self._driver = driver
        self._timeout = TIMEOUT
        self._short_timeout = SHORT_TIMEOUT

    def _get_element_id(self, locator: Tuple[str, str]) -> str:
        """Get element ID for use with gesture plugin.
        Args:
            locator: Tuple of (By strategy, locator value).
        Returns:
            str: Element ID for gesture commands.
        """
        element = self.wait_for_element(locator=locator, timeout=self._short_timeout)
        return element.id

    # ==================== SWIPE GESTURES ====================

    @allure.step("the user swipes left on element")
    def swipe_left(
        self,
        locator: Optional[Tuple[str, str]] = None,
        percentage: float = 0.75,
        speed: int = 2500,
    ) -> None:
        """Perform swipe left gesture.

        Uses appium-gestures-plugin's mobile: swipeGesture command.

        Args:
            locator: Optional element locator. If None, swipes on screen center.
            percentage: Swipe distance as percentage of element/screen width (0.0-1.0).
            speed: Swipe speed in pixels per second.
        """
        params = {
            "direction": "left",
            "percent": percentage,
            "speed": speed,
        }

        if locator:
            params["elementId"] = self._get_element_id(locator)
        else:
            size = self._driver.get_window_size()
            params["left"] = 0
            params["top"] = 0
            params["width"] = size["width"]
            params["height"] = size["height"]

        self._driver.execute_script("mobile: swipeGesture", params)
        logger.info(f"✅ Performed swipe left gesture with params: {params}")

    @allure.step("the user swipes right on element")
    def swipe_right(
        self,
        locator: Optional[Tuple[str, str]] = None,
        percentage: float = 0.75,
        speed: int = 2500,
    ) -> None:
        """Perform swipe right gesture.

        Uses appium-gestures-plugin's mobile: swipeGesture command.

        Args:
            locator: Optional element locator. If None, swipes on screen center.
            percentage: Swipe distance as percentage of element/screen width (0.0-1.0).
            speed: Swipe speed in pixels per second.
        """
        params = {
            "direction": "right",
            "percent": percentage,
            "speed": speed,
        }

        if locator:
            params["elementId"] = self._get_element_id(locator)
        else:
            size = self._driver.get_window_size()
            params["left"] = 0
            params["top"] = 0
            params["width"] = size["width"]
            params["height"] = size["height"]

        self._driver.execute_script("mobile: swipeGesture", params)
        logger.info(f"✅ Performed swipe right gesture with params: {params}")

    @allure.step("the user swipes up on element")
    def swipe_up(
        self,
        locator: Optional[Tuple[str, str]] = None,
        percentage: float = 0.75,
        speed: int = 2500,
    ) -> None:
        """Perform swipe up gesture.

        Uses appium-gestures-plugin's mobile: swipeGesture command.

        Args:
            locator: Optional element locator. If None, swipes on screen center.
            percentage: Swipe distance as percentage of element/screen height (0.0-1.0).
            speed: Swipe speed in pixels per second.
        """
        params = {
            "direction": "up",
            "percent": percentage,
            "speed": speed,
        }

        if locator:
            params["elementId"] = self._get_element_id(locator)
        else:
            size = self._driver.get_window_size()
            params["left"] = 0
            params["top"] = 0
            params["width"] = size["width"]
            params["height"] = size["height"]

        self._driver.execute_script("mobile: swipeGesture", params)
        logger.info(f"✅ Performed swipe up gesture with params: {params}")

    @allure.step("the user swipes down on element")
    def swipe_down(
        self,
        locator: Optional[Tuple[str, str]] = None,
        percentage: float = 0.75,
        speed: int = 2500,
    ) -> None:
        """Perform swipe down gesture.

        Uses appium-gestures-plugin's mobile: swipeGesture command.

        Args:
            locator: Optional element locator. If None, swipes on screen center.
            percentage: Swipe distance as percentage of element/screen height (0.0-1.0).
            speed: Swipe speed in pixels per second.
        """
        params = {
            "direction": "down",
            "percent": percentage,
            "speed": speed,
        }

        if locator:
            params["elementId"] = self._get_element_id(locator)
        else:
            size = self._driver.get_window_size()
            params["left"] = 0
            params["top"] = 0
            params["width"] = size["width"]
            params["height"] = size["height"]

        self._driver.execute_script("mobile: swipeGesture", params)
        logger.info(f"✅ Performed swipe down gesture with params: {params}")

    # ==================== SCROLL ELEMENT INTO VIEW ====================

    @allure.step("the user scrolls element into view")
    def scroll_element_into_view(
        self,
        locator: Tuple[str, str],
        direction: str = "down",
        percentage: float = 0.75,
        max_scrolls: int = 10,
    ) -> None:
        """Scroll until element is visible on screen.

        Uses appium-gestures-plugin's mobile: scrollGesture command.

        Args:
            locator: Element locator tuple to scroll into view.
            direction: Scroll direction - 'up' or 'down' (default: 'down').
            percentage: Scroll distance as percentage of screen height (0.0-1.0).
            max_scrolls: Maximum number of scroll attempts.

        Raises:
            TimeoutError: If element not found after max_scrolls attempts.
        """
        for attempt in range(max_scrolls):
            try:
                element = WebDriverWait(self._driver, SHORT_TIMEOUT).until(EC.visibility_of_element_located(locator))
                if element.is_displayed():
                    logger.info(f"✅ Element {locator} found after {attempt + 1} scroll(s)")
                    return
            except Exception:
                pass  # Ignore and perform scroll

            size = self._driver.get_window_size()
            params = {
                "left": 0,
                "top": 0,
                "width": size["width"],
                "height": size["height"],
                "direction": direction,
                "percent": percentage,
            }
            self._driver.execute_script("mobile: scrollGesture", params)
            logger.debug(f"Scroll attempt {attempt + 1}/{max_scrolls}")

        raise TimeoutError(f"❌ Element {locator} not found after {max_scrolls} scroll attempts")

    # ==================== DRAG AND DROP ====================

    @allure.step("the user drags element to target location")
    def drag_and_drop(
        self,
        source_locator: Tuple[str, str],
        target_locator: Tuple[str, str],
        speed: int = 2500,
    ) -> None:
        """Perform drag and drop gesture from source element to target element.

        Uses appium-gestures-plugin's mobile: dragGesture command.

        Args:
            source_locator: Source element locator tuple.
            target_locator: Target element locator tuple.
            speed: Drag speed in pixels per second.
        """
        source_element = self.wait_for_element(locator=source_locator, timeout=self._short_timeout)
        target_element = self.wait_for_element(locator=target_locator, timeout=self._short_timeout)

        # Calculate target center coordinates
        target_center_x = target_element.location["x"] + target_element.size["width"] // 2
        target_center_y = target_element.location["y"] + target_element.size["height"] // 2

        params = {
            "elementId": source_element.id,
            "endX": target_center_x,
            "endY": target_center_y,
            "speed": speed,
        }

        self._driver.execute_script("mobile: dragGesture", params)
        logger.info(f"✅ Performed drag and drop from {source_locator} to {target_locator}")

    @allure.step("the user drags element to coordinates")
    def drag_to_coordinates(
        self,
        source_locator: Tuple[str, str],
        end_x: int,
        end_y: int,
        speed: int = 2500,
    ) -> None:
        """Perform drag gesture from source element to specified coordinates.

        Uses appium-gestures-plugin's mobile: dragGesture command.

        Args:
            source_locator: Source element locator tuple.
            end_x: Target X coordinate.
            end_y: Target Y coordinate.
            speed: Drag speed in pixels per second.
        """
        source_element = self.wait_for_element(locator=source_locator, timeout=self._short_timeout)

        params = {
            "elementId": source_element.id,
            "endX": end_x,
            "endY": end_y,
            "speed": speed,
        }

        self._driver.execute_script("mobile: dragGesture", params)
        logger.info(f"✅ Performed drag from {source_locator} to coordinates ({end_x}, {end_y})")

    # ==================== DOUBLE TAP ====================

    @allure.step("the user double taps on element")
    def double_tap(self, locator: Tuple[str, str]) -> None:
        """Perform double tap gesture on element.

        Uses appium-gestures-plugin's mobile: doubleClickGesture command.

        Args:
            locator: Element locator tuple to double tap.
        """
        element_id = self._get_element_id(locator)

        params = {
            "elementId": element_id,
        }

        self._driver.execute_script("mobile: doubleClickGesture", params)
        logger.info(f"✅ Performed double tap on element: {locator}")

    @allure.step("the user double taps at coordinates")
    def double_tap_at_coordinates(self, x: int, y: int) -> None:
        """Perform double tap gesture at specified coordinates.

        Uses appium-gestures-plugin's mobile: doubleClickGesture command.

        Args:
            x: X coordinate to double tap.
            y: Y coordinate to double tap.
        """
        params = {
            "x": x,
            "y": y,
        }

        self._driver.execute_script("mobile: doubleClickGesture", params)
        logger.info(f"✅ Performed double tap at coordinates ({x}, {y})")

    # ==================== LONG PRESS ====================

    @allure.step("the user long presses on element")
    def long_press(self, locator: Tuple[str, str], duration: int = 1000) -> None:
        """Perform long press gesture on element.

        Uses appium-gestures-plugin's mobile: longClickGesture command.

        Args:
            locator: Element locator tuple to long press.
            duration: Press duration in milliseconds (default: 1000ms).
        """
        element_id = self._get_element_id(locator)

        params = {
            "elementId": element_id,
            "duration": duration,
        }

        self._driver.execute_script("mobile: longClickGesture", params)
        logger.info(f"✅ Performed long press on element: {locator} for {duration}ms")

    @allure.step("the user long presses at coordinates")
    def long_press_at_coordinates(self, x: int, y: int, duration: int = 1000) -> None:
        """Perform long press gesture at specified coordinates.

        Uses appium-gestures-plugin's mobile: longClickGesture command.

        Args:
            x: X coordinate to long press.
            y: Y coordinate to long press.
            duration: Press duration in milliseconds (default: 1000ms).
        """
        params = {
            "x": x,
            "y": y,
            "duration": duration,
        }

        self._driver.execute_script("mobile: longClickGesture", params)
        logger.info(f"✅ Performed long press at coordinates ({x}, {y}) for {duration}ms")

import logging
import time
from typing import Callable, Optional, Tuple

from appium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.config_vars import TIMEOUT

logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, driver: webdriver.Remote):
        self._driver = driver
        self._timeout = TIMEOUT

    def find_element(self, locator: Tuple[str, str]):
        try:
            element = WebDriverWait(self._driver, self._timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException as exc:
            raise TimeoutException(f"❌ Element not found within {self._timeout} seconds: {locator}") from exc
        except NoSuchElementException as exc:
            raise NoSuchElementException(f"❌ Element {locator} not found in the DOM.") from exc

    def send_keys(self, locator: Tuple[str, str], text: str):
        element = self.find_element(locator)
        element.send_keys(text)

    def is_element_displayed(self, locator: Tuple[str, str], timeout: int = 5) -> bool:
        """Check if element is displayed on the screen.

        Args:
            locator: Tuple of (By strategy, locator value) to identify the element.
            timeout: Maximum time in seconds to wait for element visibility (default: 5).
        Returns:
            bool: True if element is displayed, False if element is not found or not visible.
        """
        try:
            WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def wait_for_element(
        self,
        locator: Tuple[str, str],
        condition: Callable = EC.visibility_of_element_located,
        timeout: Optional[int] = 5,
        scroll_to_element: bool = False,
    ):
        """Waits for an element to meet a specified condition within a timeout period."""
        timeout_value = timeout or self._timeout
        try:
            if scroll_to_element:
                self._scroll_to_element(locator)
            return WebDriverWait(self._driver, timeout_value).until(condition(locator))
        except Exception as exc:
            raise TimeoutException(
                f"❌ Element {locator} did not meet condition within {timeout_value} seconds. Exception: {exc}"
            ) from exc

    def safe_send_keys(
        self,
        locator: Tuple[str, str],
        text: str,
        timeout: Optional[int] = None,
        clear_first: bool = True,
    ):
        """Finds visible element and sends keys; retries on stale references."""
        timeout_value = timeout or self._timeout
        attempts = 3
        for attempt in range(attempts):
            try:
                element = WebDriverWait(self._driver, timeout_value).until(EC.visibility_of_element_located(locator))
                if clear_first:
                    element.clear()
                element.send_keys(text)
                return
            except StaleElementReferenceException:
                if attempt < attempts - 1:
                    time.sleep(0.3)
                    continue
                raise
            except Exception:
                if attempt < attempts - 1:
                    time.sleep(0.3)
                    continue
                raise

    def tap_element(self, locator: Tuple[str, str]):
        """
        Performs a tap action in the center of the specified element.
        Uses W3C ActionChains for touch actions to ensure compatibility with future Appium versions
        :param locator: Tuple containing the strategy and locator of the element to tap.
        :return: None
        """
        # 1. find the clickable element
        element = self._find_clickable_element(locator)
        # 2. calculate the center coordinates of the element
        center_x = element.location['x'] + element.size['width'] // 2
        center_y = element.location['y'] + element.size['height'] // 2
        # 3. create and perform the touch action
        # use ActionChains to create W3C-compliant touch actions
        # because TouchAction is deprecated and may not be supported in future Appium versions
        actions = ActionChains(self._driver)
        # set up the touch action sequence
        actions.w3c_actions.pointer_action.move_to_location(center_x, center_y).pointer_down().pause(0.05).pointer_up()
        # perform the action
        actions.perform()
        logger.info(f"✅ Performed tap action on element: {locator} at ({center_x}, {center_y})")

    def _find_clickable_element(self, locator: Tuple[str, str]):
        return self.wait_for_element(locator=locator, condition=EC.element_to_be_clickable, timeout=self._timeout)

    def get_element_text(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> str:
        """Retrieves the text content of the specified element."""
        timeout_value = timeout or self._timeout
        element = self.wait_for_element(locator, timeout=timeout_value)
        return element.text

    def _swipe_up(self):
        """executes a swipe up gesture on the screen using W3C ActionChains.
        calculates start and end points based on screen size.
        """
        size = self._driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.75)
        end_y = int(size['height'] * 0.25)
        actions = ActionChains(self._driver)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y).pointer_down().pause(
            0.05
        ).move_to_location(start_x, end_y).pointer_up()
        actions.perform()

    def _scroll_to_element(self, locator: Tuple[str, str], max_swipes: int = 6, pause: float = 0.8):
        """
        Attempts to scroll up the screen until the element is visible or max swipes reached.

        :param locator: Tuple containing the strategy and locator of the element to find.
        :param max_swipes: Maximum number of swipe attempts to find the element.
        :param pause: Pause duration (in seconds) between swipe attempts.
        :raises TimeoutException: If the element is not found after the maximum number of swipes.
        """
        for _ in range(max_swipes):
            if not self.is_element_displayed(locator):
                self._swipe_up()
                time.sleep(pause)
            else:
                return
        raise TimeoutException(f"❌ Element {locator} not found after {max_swipes} swipe attempts.")

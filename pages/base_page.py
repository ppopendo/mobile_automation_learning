import logging
import os
import tempfile
import time
from datetime import datetime
from typing import Callable, List, Optional, Tuple

import allure
from appium import webdriver
from PIL import Image
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.config_vars import PAGE_LOAD_TIMEOUT, SHORT_TIMEOUT, TIMEOUT

logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, driver: webdriver.Remote):
        self._driver = driver
        self._timeout = TIMEOUT
        self._short_timeout = SHORT_TIMEOUT
        self._page_load_timeout = PAGE_LOAD_TIMEOUT

    def find_element(self, locator: Tuple[str, str]):
        try:
            element = WebDriverWait(self._driver, self._short_timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException as exc:
            raise TimeoutException(f"❌ Element not found within {self._short_timeout} seconds: {locator}") from exc
        except NoSuchElementException as exc:
            raise NoSuchElementException(f"❌ Element {locator} not found in the DOM.") from exc

    def send_keys(self, locator: Tuple[str, str], text: str):
        element = self.find_element(locator)
        element.send_keys(text)

    def is_element_displayed(self, locator: Tuple[str, str], timeout: int = 3) -> bool:
        """Check if element is displayed on the screen.

        Args:
            locator: Tuple of (By strategy, locator value) to identify the element.
            timeout: Maximum time in seconds to wait for element visibility (default: 3).
        Returns:
            bool: True if element is displayed, False if element is not found or not visible.
        """
        try:
            element = WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located(locator))
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException, AttributeError):
            return False

    def wait_for_element(
        self,
        locator: Tuple[str, str],
        condition: Callable = EC.visibility_of_element_located,
        timeout: Optional[int] = None,
        scroll_to_element: bool = False,
    ):
        """Waits for an element to meet a specified condition within a timeout period."""
        timeout_value = timeout if timeout is not None else self._short_timeout
        try:
            if scroll_to_element:
                self._scroll_to_element(locator)
            return WebDriverWait(self._driver, timeout_value).until(condition(locator))
        except Exception as exc:
            raise TimeoutException(
                f"❌ Element {locator} did not meet condition within {timeout_value} seconds. Exception: {exc}"
            ) from exc

    def wait_for_all_elements(
        self,
        locators: List[Tuple[str, str]],
        condition: Callable = EC.presence_of_element_located,
        timeout: Optional[int] = None,
    ) -> None:
        """Waits for all elements to meet the specified condition.

        Optimized version that uses a single WebDriverWait per element with short timeout.
        Fails fast if any element is not found.

        Args:
            locators: List of locator tuples to wait for
            condition: Expected condition to check (default: presence_of_element_located)
            timeout: Maximum time to wait per element (default: page_load_timeout)
        """
        timeout_value = timeout if timeout is not None else self._page_load_timeout
        for locator in locators:
            try:
                WebDriverWait(self._driver, timeout_value).until(condition(locator))
            except TimeoutException as exc:
                raise TimeoutException(f"❌ Element {locator} did not meet condition within {timeout_value}s") from exc

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

    @allure.step("the user captures a screenshot of {element_name}")
    def capture_element_screenshot(self, locator: Tuple[str, str], element_name: str) -> str:
        """Captures a screenshot of a specific element and saves it to a file.

        Args:
            locator: Tuple containing the strategy and locator of the element to capture.
            element_name: Descriptive name for the element being captured.

        Returns:
            str: File path to the saved screenshot.
        """
        element = self.wait_for_element(locator)
        screenshot_data = element.screenshot_as_png

        # Create screenshots directory if it doesn't exist (cross-platform)
        screenshots_dir = os.path.join(tempfile.gettempdir(), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        # Generate unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"{element_name}_{timestamp}.png"
        filepath = os.path.join(screenshots_dir, filename)

        # Save screenshot to file
        with open(filepath, "wb") as f:
            f.write(screenshot_data)

        # Attach to Allure report
        allure.attach(
            screenshot_data,
            name=f"{element_name}_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

        return filepath

    @staticmethod
    def get_rgb_from_image(filepath: str) -> Tuple[int, int, int]:
        """Extracts the dominant RGB color from an image file.

        This method reads an image file and calculates the average RGB color
        from the center region of the image (middle 50% area).

        Args:
            filepath: Path to the image file.

        Returns:
            Tuple[int, int, int]: RGB color values as (red, green, blue).

        Raises:
            FileNotFoundError: If the image file does not exist.
            ValueError: If the image is too small or has no pixels.
            OSError: If there's an error reading or processing the image.
        """
        try:
            with Image.open(filepath) as img:
                # Convert to RGB if needed (handles RGBA, grayscale, etc.)
                if img.mode != "RGB":
                    img = img.convert("RGB")

                # Get image dimensions
                width, height = img.size

                # Validate image size - need at least 4x4 to create a center region
                # We divide by 4 to get 25% from each side (width//4), which means we need
                # at least 4 pixels to have a non-empty center region after cropping
                if width < 4 or height < 4:
                    raise ValueError(f"Image is too small ({width}x{height}). Minimum size is 4x4 pixels.")

                # Calculate center region (middle 50% of the image)
                # Dividing by 4 gives us 25% margin on each side: left=25%, right=75%
                # This crops out the outer 25% from all sides, leaving the center 50% region
                # Example: for 100px width -> left=25px, right=75px -> center region = 50px
                center_region = img.crop((width // 4, height // 4, width - width // 4, height - height // 4))

                # Get all pixels from the center region and calculate average RGB values
                pixels = list(center_region.getdata())
                pixel_count = len(pixels)

                # Ensure we have pixels to process
                if pixel_count == 0:
                    raise ValueError("No pixels found in the center region of the image.")

                # Calculate average RGB by summing all R, G, B values separately and dividing by pixel count
                # pixel[0] = Red, pixel[1] = Green, pixel[2] = Blue
                # This gives us the dominant/average color in the center region
                return (
                    round(sum(pixel[0] for pixel in pixels) / pixel_count),
                    round(sum(pixel[1] for pixel in pixels) / pixel_count),
                    round(sum(pixel[2] for pixel in pixels) / pixel_count),
                )
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"Image file not found: {filepath}") from exc
        except OSError as exc:
            raise OSError(f"Error reading or processing image file: {filepath}") from exc

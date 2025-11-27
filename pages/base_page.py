import time
from typing import Callable, Optional
from typing import Tuple
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
import logging
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

	def is_element_displayed(self, locator: Tuple[str, str]) -> bool:
		try:
			WebDriverWait(self._driver, 5).until(EC.visibility_of_element_located(locator))
			return True
		except (TimeoutException, NoSuchElementException):
			return False

	def wait_for_element(
		self,
		locator: Tuple[str, str],
		condition: Callable = EC.visibility_of_element_located,
		timeout: Optional[int] = None,
	):
		"""Waits for an element to meet a specified condition within a timeout period."""
		timeout_value = timeout or self._timeout
		try:
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
		actions.w3c_actions.pointer_action.move_to_location(center_x, center_y) \
			.pointer_down() \
			.pause(0.05) \
			.pointer_up()
		# perform the action
		actions.perform()
		logger.info(f"✅ Performed tap action on element: {locator} at ({center_x}, {center_y})")

	def _find_clickable_element(self, locator: Tuple[str, str]):
		return self.wait_for_element(locator=locator, condition=EC.element_to_be_clickable, timeout=self._timeout)
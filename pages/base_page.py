from typing import Callable, Optional, Tuple
import time

from selenium.common.exceptions import (
	NoSuchElementException,
	StaleElementReferenceException,
	TimeoutException,
	WebDriverException,
)
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.config_vars import TIMEOUT
from appium.webdriver.extensions.action_helpers import ActionHelpers


class BasePage:

	def __init__(self, driver: RemoteWebDriver):
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

	def click(self, locator: Tuple[str, str]):
		element = WebDriverWait(self._driver, self._timeout).until(EC.element_to_be_clickable(locator))
		element.click()

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
		timeout_value = timeout or self._timeout
		try:
			return WebDriverWait(self._driver, timeout_value).until(condition(locator))
		except Exception as exc:
			raise TimeoutException(
				f"❌ Element {locator} did not meet condition within {timeout_value} seconds. Exception: {exc}"
			) from exc

	def wait_and_click(
		self,
		locator: Tuple[str, str],
		timeout: Optional[int] = None,
		retries: int = 3,
		retry_delay: float = 0.5,
	):
		timeout_value = timeout or self._timeout
		last_exc = None
		for _ in range(retries):
			try:
				element = WebDriverWait(self._driver, timeout_value).until(EC.element_to_be_clickable(locator))
				element.click()
				return
			except StaleElementReferenceException as exc:
				last_exc = exc
				time.sleep(retry_delay)
				continue
			except (TimeoutException, NoSuchElementException, WebDriverException) as exc:
				last_exc = exc
				time.sleep(retry_delay)
				continue
		if last_exc:
			raise last_exc

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

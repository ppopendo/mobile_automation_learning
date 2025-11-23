import logging
import os
import time
from pathlib import Path
from typing import Optional, Any
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from config.config_vars import APPIUM_CONNECT_DELAY, APPIUM_CONNECT_RETRIES
from libs.common import load_device_config

logger = logging.getLogger(__name__)


class AppiumDriverService:

    def __init__(self, platform: str):
        """Service wrapper around Appium WebDriver initialization and teardown.

        Args:
            platform: 'android' or 'ios'
        """
        load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / "config" / ".env")
        self.platform = platform
        self._appium_server_url = os.getenv("APPIUM_SERVER_URL")
        self._appium_connect_retries = APPIUM_CONNECT_RETRIES
        self._appium_connect_delay = APPIUM_CONNECT_DELAY
        self._driver: Optional[Any] = None

    def initialize_driver(self) -> Any:
        """Initialize and return a Remote WebDriver instance with retries on connection errors."""
        try:
            for attempt in range(1, self._appium_connect_retries + 1):
                try:
                    self._driver = webdriver.Remote(
                        command_executor=self._appium_server_url,
                        options=self._get_driver_options(),
                    )
                    break
                except Exception as exc:
                    logger.exception(
                        "[SETUP - session] connection error to Appium (attempt %s/%s): %s",
                        attempt,
                        self._appium_connect_retries,
                        exc,
                    )
                    if attempt < self._appium_connect_retries:
                        time.sleep(self._appium_connect_delay)
                        continue
                    raise RuntimeError(
                        f"Failed to connect to Appium after {self._appium_connect_retries} attempts: {exc}"
                    ) from exc
            if not self._driver:
                raise ConnectionError(
                    f"Failed to connect to Appium server at {self._appium_server_url}"
                )
            return self._driver
        except Exception as exc:
            # Wrap unexpected errors in ConnectionError to provide clearer context
            raise ConnectionError(
                f"Failed to connect to Appium server at {self._appium_server_url}: {exc}"
            ) from exc

    def _get_driver_options(self) -> AppiumOptions:
        if self.platform == "android":
            options = UiAutomator2Options().load_capabilities(caps=load_device_config(platform="android"))
        elif self.platform == "ios":
            options = XCUITestOptions().load_capabilities(caps=load_device_config(platform="ios"))
        else:
            raise ValueError(f"Unsupported platform: {self.platform}")
        options.device_name = os.getenv("DEVICE_NAME")
        options.platform_version = os.getenv("PLATFORM_VERSION")
        return options

    def quit_driver(self) -> None:
        if self._driver:
            try:
                self._driver.quit()
            except Exception as exc:
                logger.exception("Error while quitting driver: %s", exc)

    def terminate_application(self, app_package: str) -> None:
        if self._driver:
            try:
                terminate = getattr(self._driver, "terminate_app", None)
                if callable(terminate):
                    terminate(app_package)
                else:
                    logger.warning("Driver does not implement 'terminate_app'; skipping termination for %s", app_package)
            except Exception as exc:
                logger.exception("Error while terminating application: %s", exc)

"""
Shared driver fixtures for test sessions.
These fixtures handle driver initialization, teardown, and application state verification.
"""

import logging
from typing import Any, Dict, Generator
import pytest
from config.config_vars import SHORT_TIMEOUT
from drivers.appium_driver import AppiumDriverService
from libs.common import load_device_capabilities

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def platform(request: pytest.FixtureRequest) -> str:
    """Get the platform specified via --platform option."""
    return request.config.getoption("--platform")


@pytest.fixture(scope="session")
def appium_service(platform: str) -> AppiumDriverService:
    """Create AppiumDriverService for the whole test session.
    Platform is read from --platform pytest option (default: android).
    """
    service = AppiumDriverService(platform=platform)
    return service


@pytest.fixture(scope="session")
def device_capabilities(platform: str) -> Dict[str, Any]:
    """Load device capabilities for the requested platform.
    Uses the same --platform option as `appium_service`.
    """
    caps = load_device_capabilities(platform=platform)
    return caps


@pytest.fixture(scope="session")
def driver(appium_service: AppiumDriverService, device_capabilities: Dict[str, Any]) -> Generator[Any, None, None]:
    """Create a single Appium driver for the test session and perform teardown when finished.
    Yields the raw driver object (Appium WebDriver). The type is kept generic (Any) because
    Appium driver exposes methods beyond standard Selenium RemoteWebDriver.
    """
    appium_driver: Any = appium_service.initialize_driver()
    try:
        appium_driver.implicitly_wait(SHORT_TIMEOUT)
    except Exception:
        logger.debug("Could not set implicit wait on driver; continuing.")
    yield appium_driver
    try:
        app_package = device_capabilities.get("appPackage") if isinstance(device_capabilities, dict) else None
        if app_package:
            try:
                appium_service.terminate_application(app_package=app_package)
            except Exception as exc:
                logger.exception("[TEARDOWN - session] error terminating app: %s", exc)
    finally:
        try:
            appium_service.quit_driver()
        except Exception as exc:
            logger.exception("[TEARDOWN - session] error quitting driver: %s", exc)

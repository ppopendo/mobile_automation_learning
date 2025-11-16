import logging
from typing import Any, Dict, Generator
import pytest
from config.config_vars import TIMEOUT
from drivers.appium_driver import AppiumDriverService
from libs.common import load_device_config
from pages.menu_page import MenuPage
from pages.product_page import ProductPage

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s [%(name)s] %(message)s")


def pytest_addoption(parser):
    parser.addoption(
        "--tcid",
        action="store",
        default=None,
        help="Run only tests annotated with @pytest.mark.tc(\"TC-XXXX\") matching this id",
    )
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        help="Device platform to run tests against (android|ios). Default: android",
    )


@pytest.fixture(scope="session")
def appium_service(request) -> AppiumDriverService:
    """Create AppiumDriverService for the whole test session.

    Platform is read from --platform pytest option (default: android).
    """
    platform = request.config.getoption("--platform")
    service = AppiumDriverService(platform=platform)
    return service


@pytest.fixture(scope="session")
def device_capabilities(request) -> Dict[str, Any]:
    """Load device capabilities for the requested platform.

    Uses the same --platform option as `appium_service`.
    """
    platform = request.config.getoption("--platform")
    caps = load_device_config(platform=platform)
    return caps


@pytest.fixture(scope="session")
def driver(appium_service: AppiumDriverService, device_capabilities: Dict[str, Any]) -> Generator[Any, None, None]:
    """Create a single Appium driver for the test session and perform teardown when finished.

    Yields the raw driver object (Appium WebDriver). The type is kept generic (Any) because
    Appium driver exposes methods beyond standard Selenium RemoteWebDriver.
    """
    appium_driver: Any = appium_service.initialize_driver()
    # set implicit wait
    try:
        appium_driver.implicitly_wait(TIMEOUT)
    except Exception:
        # Some drivers might not implement implicitly_wait exactly the same way,
        # ignore if setting it fails but continue to provide the driver to tests
        logger.debug("Could not set implicit wait on driver; continuing.")

    yield appium_driver

    # Teardown session (best-effort)
    try:
        app_package = device_capabilities.get("appPackage") if isinstance(device_capabilities, dict) else None
        if app_package:
            try:
                appium_service.terminate_application(app_package=app_package)
            except Exception as exc:  # keep broad-except only for teardown
                logger.exception("[TEARDOWN - session] error terminating app: %s", exc)
    finally:
        try:
            appium_service.quit_driver()
        except Exception as exc:
            logger.exception("[TEARDOWN - session] error quitting driver: %s", exc)


@pytest.fixture(scope="session", autouse=True)
def suite_setup(driver) -> None:
    """Suite-level setup: navigate to the login screen once per test session.

    This is executed once per test session (autouse). It will log errors but not fail the session setup.
    """
    try:
        product_page = ProductPage(driver)
        menu_page = MenuPage(driver)
        product_page.open_side_menu()
        menu_page.wait_until_page_is_loaded()
        menu_page.click_login_button()
    except Exception as exception:  # do not raise to allow tests to run; log details for debugging
        logger.exception(
            "[SETUP - session]: could not navigate to login screen at session setup, details: %s",
            exception,
        )



def pytest_collection_modifyitems(config, items):
    tc_id = config.getoption("--tcid")
    if not tc_id:
        return
    kept = []
    deselected = []
    for item in items:
        marker = item.get_closest_marker("tcid")
        if marker:
            # marker can be used as @pytest.mark.tc("TC-00002")
            value = marker.args[0] if marker.args else None
            if value == tc_id:
                kept.append(item)
            else:
                deselected.append(item)
        else:
            # not marked with tc -> deselect
            deselected.append(item)

    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = kept

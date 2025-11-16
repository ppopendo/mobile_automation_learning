import logging
from typing import cast
import pytest
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from config.config_vars import TIMEOUT
from drivers.appium_driver import AppiumDriverService
from libs.common import load_device_config
from pages.menu_page import MenuPage
from pages.product_page import ProductPage

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s [%(name)s] %(message)s")


@pytest.fixture(scope="session")
def driver(request):
    """Create a single Appium driver for the test session and teardown when finished."""
    capabilities = load_device_config(platform="android")
    appium_service = AppiumDriverService(platform="android")
    appium_driver = cast(RemoteWebDriver, appium_service.initialize_driver())
    driver_instance: RemoteWebDriver = appium_driver
    driver_instance.implicitly_wait(TIMEOUT)
    yield driver_instance
    # Teardown session
    try:
        appium_service.terminate_application(app_package=capabilities["appPackage"])
    except Exception as exc:  # keep broad-except only for teardown
        logger.exception("[TEARDOWN - session] error terminating app: %s", exc)
    try:
        appium_service.quit_driver()
    except Exception as exc:
        logger.exception("[TEARDOWN - session] error quitting driver: %s", exc)


@pytest.fixture(scope="session", autouse=True)
def suite_setup(driver) -> None:
    """Suite-level setup: navigate to the login screen once per test session."""
    try:
        product_page = ProductPage(driver)
        menu_page = MenuPage(driver)
        product_page.open_side_menu()
        menu_page.wait_until_page_is_loaded()
        menu_page.click_login_button()
    except Exception as exception:
        logger.exception(
            "[SETUP - session]: could not navigate to login screen at session setup, details: %s",
            exception,
        )


def pytest_addoption(parser):
    parser.addoption(
        "--tcid",
        action="store",
        default=None,
        help="Run only tests annotated with @pytest.mark.tc(\"TC-XXXX\") matching this id",
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

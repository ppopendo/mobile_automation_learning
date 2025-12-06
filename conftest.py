"""
Root conftest.py - Global pytest configuration and hooks.

This file contains:
- pytest CLI options (--tcid, --platform)
- Global setup: verify app is launched
- Screenshot on test failure hook
- Test collection modifiers

Test-specific fixtures are located in:
- tests/fixtures/ - shared, reusable fixtures
- tests/<suite>/conftest.py - suite-specific fixtures
"""

import logging
import os
from datetime import datetime
from typing import Any

import pytest
from tests.fixtures.fixtures_driver import take_screenshot

# Register shared fixture modules using pytest_plugins for modularity
pytest_plugins = [
    "tests.fixtures.fixtures_driver",
    "tests.fixtures.fixtures_auth",
    "tests.fixtures.fixtures_navigation",
    "tests.fixtures.fixtures_checkout",
]

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s [%(name)s] %(message)s")


def pytest_addoption(parser):
    """Add custom command line options for pytest."""
    parser.addoption(
        "--tcid",
        action="store",
        default=None,
        help="Run only tests annotated with @pytest.mark.tcid(\"TC-XXXX\") matching this id",
    )
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        help="Device platform to run tests against (android|ios). Default: android",
    )


@pytest.fixture(scope="session")
def tcid(request: pytest.FixtureRequest):
    """Get the test case ID specified via --tcid option."""
    return request.config.getoption("--tcid")


@pytest.fixture(scope="session", autouse=True)
def global_setup(driver: Any, screenshots_dir: str) -> None:
    """Global session setup: verify the application is launched successfully.

    This minimal setup only checks that the app is running.
    Suite-specific setup is handled in local conftest.py files.
    Takes a screenshot if verification fails.
    """
    try:
        # Verify app is launched by checking driver session is active
        session_id = driver.session_id
        if not session_id:
            raise RuntimeError("Driver session is not active")
        logger.info("[GLOBAL SETUP] Application launched successfully. Session ID: %s", session_id)
    except Exception as exception:
        logger.exception(
            "[GLOBAL SETUP] Application launch verification failed: %s",
            exception,
        )
        # Take screenshot on setup failure
        try:
            take_screenshot(driver, screenshots_dir, "global_setup_failure")
        except Exception as screenshot_exc:
            logger.exception("[GLOBAL SETUP] Failed to take screenshot: %s", screenshot_exc)
        raise


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test result and take screenshot on failure."""
    outcome = yield
    report = outcome.get_result()

    # Only handle test call phase failures (not setup/teardown)
    if report.when == "call" and report.failed:
        # Try to get driver and screenshots_dir from fixtures
        try:
            driver = item.funcargs.get("driver")
            screenshots_path = item.funcargs.get("screenshots_dir")
            if screenshots_path is None:
                screenshots_path = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshots_path, exist_ok=True)

            if driver:
                test_name = item.name.replace(" ", "_").replace("/", "_")
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"FAIL_{test_name}_{timestamp}.png"
                filepath = os.path.join(screenshots_path, filename)
                driver.save_screenshot(filepath)
                logger.info("[FAILURE SCREENSHOT] Saved: %s", filepath)
        except Exception as exc:
            logger.warning("[FAILURE SCREENSHOT] Could not take screenshot: %s", exc)


def pytest_collection_modifyitems(config, items):
    """Filter collected tests by Test Case ID (--tcid option).

    If --tcid is provided, only tests marked with @pytest.mark.tcid matching the value are run; others are deselected.
    """
    # Get --tcid option value; if not provided, run all tests
    tc_id = config.getoption("--tcid")
    if not tc_id:
        return

    # Separate tests into kept (matching tcid) and deselected (not matching)
    kept = []
    deselected = []

    for item in items:
        # Get @pytest.mark.tcid marker from test
        marker = item.get_closest_marker("tcid")
        if marker:
            # Extract marker value (first positional argument)
            value = marker.args[0] if marker.args else None
            if value == tc_id:
                kept.append(item)
            else:
                deselected.append(item)
        else:
            # No tcid marker - deselect when filtering by tcid
            deselected.append(item)

    # Report deselected tests and update items list
    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = kept

"""
General suite - local conftest.py

Suite-specific fixtures and setup for general/driver tests.
These tests typically don't require app interaction, only driver/service testing.
"""

import logging
import pytest

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module", autouse=True)
def general_suite_setup():
    """Suite setup: Minimal setup for general tests.

    General tests may not require app interaction,
    so this setup is intentionally minimal.
    """
    logger.info("[GENERAL SUITE SETUP] Starting general tests")
    yield
    logger.info("[GENERAL SUITE TEARDOWN] Completed general tests")


# Note: General tests like test_driver.py test the AppiumDriverService directly
# without needing the driver fixture, so we don't include driver-dependent fixtures here.

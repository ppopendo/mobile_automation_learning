import pytest
from drivers.appium_driver import AppiumDriverService


def test_get_driver_options_invalid_platform():
    service = AppiumDriverService(platform="unknown")
    with pytest.raises(ValueError):
        service._get_driver_options()

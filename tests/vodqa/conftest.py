"""
VodQA test fixtures.
Contains fixtures for VodQA app test setup, teardown and test data.
"""

from typing import Any, Generator

import allure
import pytest

from pages.vodqa.login_page import LoginPage
from pages.vodqa.samples_list_page import SamplesListPage
from pages.vodqa.slider_page import SliderPage


@pytest.fixture(scope="session")
def vodqa_logged_in(driver: Any) -> Generator[None, None, None]:
    """Login to VodQA app once per session.

    This fixture handles the initial login at session start.
    """
    login_page = LoginPage(driver)
    login_page.wait_until_page_is_loaded()
    login_page.login(username="admin", password="admin")

    samples_list_page = SamplesListPage(driver)
    samples_list_page.wait_until_page_is_loaded()

    yield


@pytest.fixture
def samples_list_page(driver: Any, vodqa_logged_in: None) -> SamplesListPage:
    """Get SamplesListPage object. Ensures user is logged in.

    Returns:
        SamplesListPage: Page object for Samples List screen.
    """
    page = SamplesListPage(driver)
    page.wait_until_page_is_loaded()
    return page


@pytest.fixture
def slider_page(driver: Any, samples_list_page: SamplesListPage) -> Generator[SliderPage, None, None]:
    """Navigate to Slider page and return page object.

    Handles teardown by navigating back to Samples List.

    Yields:
        SliderPage: Page object for Slider screen.
    """
    samples_list_page.tap_slider()

    page = SliderPage(driver)
    page.wait_until_page_is_loaded()

    yield page

    # Teardown: Navigate back to Samples List
    with allure.step("Teardown: navigating back to Samples List"):
        page.tap_back_button()
        samples_list_page.wait_until_page_is_loaded()

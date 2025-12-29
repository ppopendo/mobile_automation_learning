"""
VodQA test fixtures.
Contains fixtures for VodQA app test setup, teardown and test data.
"""

from typing import Any, Generator

import allure
import pytest

from pages.vodqa.double_tap_page import DoubleTapPage
from pages.vodqa.drag_and_drop_page import DragAndDropPage
from pages.vodqa.login_page import LoginPage
from pages.vodqa.long_press_page import LongPressPage
from pages.vodqa.samples_list_page import SamplesListPage
from pages.vodqa.slider_page import SliderPage
from pages.vodqa.vertical_swiping_page import VerticalSwipingPage
from pages.vodqa.photo_view_page import PhotoViewPage
from pages.vodqa.carousel_page import CarouselPage


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


@pytest.fixture
def vertical_swiping_page(
    driver: Any, samples_list_page: SamplesListPage
) -> Generator[VerticalSwipingPage, None, None]:
    """Navigate to Vertical Swiping page and return page object.
    Handles teardown by navigating back to Samples List.
    Yields:
        VerticalSwipingPage: Page object for Vertical Swiping screen.
    """
    samples_list_page.tap_vertical_swiping()
    page = VerticalSwipingPage(driver)
    page.wait_until_page_is_loaded()
    yield page
    # Teardown: Navigate back to Samples List
    with allure.step("Teardown: navigating back to Samples List"):
        page.tap_back_button()
        samples_list_page.wait_until_page_is_loaded()


@pytest.fixture
def drag_and_drop_page(driver: Any, samples_list_page: SamplesListPage) -> Generator[DragAndDropPage, None, None]:
    """Navigate to Drag and Drop page and return page object.
    Handles teardown by navigating back to Samples List.
    Yields:
        DragAndDropPage: Page object for Drag and Drop screen.
    """
    samples_list_page.tap_drag_and_drop()
    page = DragAndDropPage(driver)
    page.wait_until_page_is_loaded()
    yield page
    # Teardown: Navigate back to Samples List
    with allure.step("Teardown: navigating back to Samples List"):
        page.tap_back_button()
        samples_list_page.wait_until_page_is_loaded()


@pytest.fixture
def double_tap_page(driver: Any, samples_list_page: SamplesListPage) -> Generator[DoubleTapPage, None, None]:
    """Navigate to Double Tap page and return page object.
    Handles teardown by navigating back to Samples List.
    Yields:
        DoubleTapPage: Page object for Double Tap screen.
    """
    samples_list_page.tap_double_tap()
    page = DoubleTapPage(driver)
    page.wait_until_page_is_loaded()
    yield page
    # Teardown: Navigate back to Samples List
    with allure.step("Teardown: navigating back to Samples List"):
        if page.is_double_tap_modal_displayed:
            page.tap_ok_button()
        page.tap_back_button()
        samples_list_page.wait_until_page_is_loaded()


@pytest.fixture
def long_press_page(driver: Any, samples_list_page: SamplesListPage) -> Generator[LongPressPage, None, None]:
    """Navigate to Long Press page and return page object.
    Handles teardown by navigating back to Samples List.
    Yields:
        LongPressPage: Page object for Long Press screen.
    """
    samples_list_page.tap_long_press()
    page = LongPressPage(driver)
    page.wait_until_page_is_loaded()
    yield page
    # Teardown: Navigate back to Samples List
    with allure.step("Teardown: navigating back to Samples List"):
        if page.is_long_press_modal_displayed:
            page.tap_ok_button()
        page.tap_back_button()
        samples_list_page.wait_until_page_is_loaded()


@pytest.fixture
def photo_view_page(driver: Any, samples_list_page: SamplesListPage) -> Generator[PhotoViewPage, None, None]:
    """Navigate to Photo View page and return page object.
    Handles teardown by navigating back to Samples List.

    Yields:
        PhotoViewPage: Page object for Photo View screen.
    """
    samples_list_page.swipe_up_and_validate_sample_name("Photo View")
    samples_list_page.tap_photo_view()
    page = PhotoViewPage(driver)
    page.wait_until_page_is_loaded()
    yield page
    # Teardown: Navigate back to Samples List
    with allure.step("Teardown: navigating back to Samples List"):
        page.tap_back_button()
        samples_list_page.wait_until_page_is_loaded()


@pytest.fixture
def carousel_page(driver: Any, samples_list_page: SamplesListPage) -> Generator[CarouselPage, None, None]:
    """Navigate to Carousel page and return page object.
    Handles teardown by navigating back to Samples List.

    Yields:
        CarouselPage: Page object for Carousel screen.
    """
    samples_list_page.swipe_up_and_validate_sample_name("Carousel")
    samples_list_page.tap_carousel()
    page = CarouselPage(driver)
    page.wait_until_page_is_loaded()
    yield page
    # Teardown: Navigate back to Samples List
    with allure.step("Teardown: navigating back to Samples List"):
        page.tap_back_button()
        samples_list_page.wait_until_page_is_loaded()

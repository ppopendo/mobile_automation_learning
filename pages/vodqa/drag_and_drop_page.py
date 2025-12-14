"""Page Object for Drag and Drop feature in VodQA application."""

from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent, HeaderBarComponentLocators


@dataclass(frozen=True)
class DragAndDropPageLocators:
    """Locators for Drag and Drop page elements."""

    PAGE_TITLE: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='Drag & Drop']"), init=False
    )
    DRAGGABLE_1: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='dragAndDrop']//android.view.ViewGroup[1]"),
        init=False,
    )
    DRAGGABLE_2: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='dragAndDrop']//android.view.ViewGroup[2]"),
        init=False,
    )
    DROP_ZONE: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='dragAndDrop']//android.view.ViewGroup[3]"),
        init=False,
    )


class DragAndDropPage(BaseAppiumGestures, HeaderBarComponent):
    """Page Object for the Drag and Drop screen in VodQA app.

    This page contains draggable elements and drop zones for testing drag and drop gestures.
    """

    @allure.step("the user waits until the drag and drop page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for drag and drop page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Drag & Drop")

    @allure.step("the user navigates back from drag and drop page")
    def tap_back_button(self) -> None:
        """Tap the back button to return to Samples List."""
        self.tap_element(HeaderBarComponentLocators.BACK_BUTTON)

    @property
    @allure.step("checking if draggable 1 is displayed")
    def is_draggable_1_displayed(self) -> bool:
        """Check if draggable element 1 is displayed on screen."""
        return self.is_element_displayed(DragAndDropPageLocators.DRAGGABLE_1)

    @property
    @allure.step("checking if draggable 2 is displayed")
    def is_draggable_2_displayed(self) -> bool:
        """Check if draggable element 2 is displayed on screen."""
        return self.is_element_displayed(DragAndDropPageLocators.DRAGGABLE_2)

    @property
    @allure.step("checking if drop zone is displayed")
    def is_drop_zone_displayed(self) -> bool:
        """Check if drop zone is displayed on screen."""
        return self.is_element_displayed(DragAndDropPageLocators.DROP_ZONE)

    @property
    @allure.step("retrieving draggable 1 location")
    def draggable_1_location(self) -> dict:
        """Get location of draggable element 1."""
        element = self.wait_for_element(DragAndDropPageLocators.DRAGGABLE_1)
        return element.location

    @property
    @allure.step("retrieving drop zone location")
    def drop_zone_location(self) -> dict:
        """Get location of drop zone."""
        element = self.wait_for_element(DragAndDropPageLocators.DROP_ZONE)
        return element.location

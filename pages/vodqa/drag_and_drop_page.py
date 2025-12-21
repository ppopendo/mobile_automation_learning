"""Page Object for Drag and Drop feature in VodQA application."""

from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent


@dataclass(frozen=True)
class DragAndDropPageLocators:
    """Locators for Drag and Drop page elements."""

    DRAG_ME_BUTTON: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "dragMe"), init=False)
    DROP_HERE_ZONE: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "dropzone"), init=False)


class DragAndDropPage(BaseAppiumGestures, HeaderBarComponent):
    """Page Object for the Drag and Drop screen in VodQA app.
    This page contains a draggable button and drop zone for testing drag and drop gestures.
    """

    @allure.step("the user waits until the drag and drop page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for drag and drop page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Drag & Drop")

    @property
    @allure.step("checking if drag me button is displayed")
    def is_drag_me_button_displayed(self) -> bool:
        """Check if drag me button is displayed on screen."""
        return self.is_element_displayed(DragAndDropPageLocators.DRAG_ME_BUTTON)

    @property
    @allure.step("checking if drop here zone is displayed")
    def is_drop_here_zone_displayed(self) -> bool:
        """Check if drop here zone is displayed on screen."""
        return self.is_element_displayed(DragAndDropPageLocators.DROP_HERE_ZONE)

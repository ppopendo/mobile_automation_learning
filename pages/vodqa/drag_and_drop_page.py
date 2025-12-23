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
    MESSAGE_DROPPED: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "success"), init=False)


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

    @property
    @allure.step("checking if message dropped is displayed")
    def is_message_dropped_displayed(self) -> bool:
        """Check if the 'Dropped!' message is displayed after a successful drop."""
        return self.is_element_displayed(DragAndDropPageLocators.MESSAGE_DROPPED)

    @property
    @allure.step("retrieving the text of the 'Circle dropped' message")
    def message_dropped_text(self) -> str:
        """Get the text of the 'Dropped!' message."""
        return self.get_element_text(DragAndDropPageLocators.MESSAGE_DROPPED)

    @allure.step("the user performs drag and drop from 'Drag me' button to 'Drop here' zone")
    def drag_and_drop_element(self, speed=2200) -> None:
        """Perform drag and drop gesture from the 'Drag me' button to the 'Drop here' zone."""
        self.drag_and_drop(
            source_locator=DragAndDropPageLocators.DRAG_ME_BUTTON,
            target_locator=DragAndDropPageLocators.DROP_HERE_ZONE,
            speed=speed,
        )

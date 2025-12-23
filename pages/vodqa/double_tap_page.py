"""Page Object for Double Tap feature in VodQA application."""

from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent
from pages.vodqa.modal_generic import ModalGeneric


@dataclass(frozen=True)
class DoubleTapPageLocators:
    """Locators for Double Tap page elements."""

    DOUBLE_TAP_ME_BUTTON: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "doubleTapMe"), init=False)


class DoubleTapPage(BaseAppiumGestures, HeaderBarComponent, ModalGeneric):
    """Page Object for the Double Tap screen in VodQA app.
    This page contains a button for testing double tap gestures.
    """

    @allure.step("the user waits until the double tap page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for double tap page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Double Tap Demo")

    @property
    @allure.step("checking if double tap me button is displayed")
    def is_double_tap_me_button_displayed(self) -> bool:
        """Check if double tap me button is displayed on screen."""
        return self.is_element_displayed(DoubleTapPageLocators.DOUBLE_TAP_ME_BUTTON)

    @property
    @allure.step("the modal is displayed after double tap")
    def is_double_tap_modal_displayed(self) -> bool:
        """Check if the double tap modal dialog is displayed."""
        return self.is_modal_displayed

    @allure.step("the user performs a double tap on the double tap me button")
    def double_tap_on_double_tap_me_button(self) -> None:
        """Perform a double tap gesture on the double tap me button."""
        self.double_tap(DoubleTapPageLocators.DOUBLE_TAP_ME_BUTTON)

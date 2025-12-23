"""Modal Generic Page Object Model for Appium-based Mobile Testing."""

from dataclasses import field, dataclass
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException

from config.config_vars import SHORT_TIMEOUT
from pages.base_page import BasePage


@dataclass(frozen=True)
class ModalGenericLocators:
    """Locators for the generic modal dialog components (header, message, and OK button)."""

    MODAL_HEADER: Tuple[str, str] = field(default=(AppiumBy.ID, "android:id/alertTitle"), init=False)
    MODAL_MESSAGE: Tuple[str, str] = field(default=(AppiumBy.ID, "android:id/message"), init=False)
    MODAL_OK_BUTTON: Tuple[str, str] = field(default=(AppiumBy.ID, "android:id/button1"), init=False)


class ModalGeneric(BasePage):
    """Generic modal dialog Page Object for waiting on, validating, and interacting with alert dialogs."""

    @allure.step("the user waits until the modal dialog is displayed")
    def wait_until_modal_is_displayed(self, timeout: int = SHORT_TIMEOUT) -> None:
        """Waits until the modal dialog is displayed."""
        self.wait_for_all_elements(
            [
                ModalGenericLocators.MODAL_HEADER,
                ModalGenericLocators.MODAL_MESSAGE,
                ModalGenericLocators.MODAL_OK_BUTTON,
            ],
            timeout=timeout,
        )

    @property
    @allure.step("the user retrieves the modal header text")
    def modal_header_text(self) -> str:
        """Returns the text of the modal header."""
        return self.wait_for_element(ModalGenericLocators.MODAL_HEADER).text

    @property
    @allure.step("the user retrieves the modal message text")
    def modal_message_text(self) -> str:
        """Returns the text of the modal message."""
        return self.wait_for_element(ModalGenericLocators.MODAL_MESSAGE).text

    @property
    @allure.step("the user checks if the OK button is displayed in the modal")
    def is_ok_button_displayed(self) -> bool:
        """Checks if the OK button is displayed in the modal."""
        return self.is_element_displayed(ModalGenericLocators.MODAL_OK_BUTTON)

    @allure.step("the user taps the OK button in the modal")
    def tap_ok_button(self) -> None:
        """Taps the OK button in the modal."""
        self.tap_element(ModalGenericLocators.MODAL_OK_BUTTON)

    @property
    @allure.step("retrieving whether the modal dialog is currently displayed")
    def is_modal_displayed(self) -> bool:
        """Checks if the modal dialog is currently displayed."""
        try:
            self.wait_for_all_elements(
                [
                    ModalGenericLocators.MODAL_HEADER,
                    ModalGenericLocators.MODAL_MESSAGE,
                    ModalGenericLocators.MODAL_OK_BUTTON,
                ],
                timeout=SHORT_TIMEOUT,
            )
            return True
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
            return False

from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from config.config_vars import SHORT_TIMEOUT
from pages.base_page import BasePage


@dataclass(frozen=True)
class HeaderBarComponentLocators:
    BACK_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='Back']"), init=False
    )
    TITLE: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='{title}']"),
        init=False,
        metadata={
            "doc": (
                "This locator is a format string and should not be used directly. "
                "Use the 'title_locator' static method to construct the locator with the required title."
            )
        },
    )

    @staticmethod
    def title_locator(title: str) -> Tuple[str, str]:
        """
        Returns the TITLE locator tuple with the given title.
        Args:
            title (str): The title text to match.
        Returns:
            Tuple[str, str]: The locator tuple for the given title.
        """
        return (
            HeaderBarComponentLocators.TITLE[0],
            HeaderBarComponentLocators.TITLE[1].format(title=title),
        )


class HeaderBarComponent(BasePage):

    @allure.step("the user waits until the header bar component is loaded with title '{title}'")
    def wait_until_component_is_loaded(self, title: str, timeout: int = SHORT_TIMEOUT) -> None:
        self.wait_for_all_elements(
            [HeaderBarComponentLocators.BACK_BUTTON, HeaderBarComponentLocators.title_locator(title)], timeout=timeout
        )

    @allure.step("the user navigates back")
    def tap_back_button(self) -> None:
        """Tap the back button to navigate back."""
        self.tap_element(HeaderBarComponentLocators.BACK_BUTTON)

"""Page Object for Vertical Swiping feature in VodQA application."""

from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent


@dataclass(frozen=True)
class VerticalSwipingPageLocators:
    """Locators for Vertical Swiping page elements."""

    SCROLLABLE_CONTAINER: Tuple[str, str] = field(
        default=(
            AppiumBy.XPATH,
            "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[8]/android.view.ViewGroup",
        ),
        init=False,
    )

    @staticmethod
    def item_locator(item_text: str) -> Tuple[str, str]:
        """Generate locator for list item by text.
        Args:
            item_text: The text of the item (e.g., 'C', 'C++', 'Javascript', etc.)
        Returns:
            Tuple[str, str]: Locator tuple for the item.
        """
        return (AppiumBy.XPATH, f"//android.widget.TextView[@text=' {item_text}']")


class VerticalSwipingPage(BaseAppiumGestures, HeaderBarComponent):
    """Page Object for the Vertical Swiping screen in VodQA app.
    This page contains a scrollable list for testing vertical swipe gestures.
    List items: [C, C++, Javascript, Ruby, RR, Java, C#, .net, MySql, Appium, Jasmine, Jest, Karma]
    """

    @allure.step("the user waits until the vertical swiping page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for vertical swiping page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Vertical Swiping")

    @allure.step("checking if item '{item_text}' is displayed")
    def is_item_displayed(self, item_text: str) -> bool:
        """Check if specific item is displayed on screen.
        Args:
            item_text: The text of the item to check.
        Returns:
            bool: True if item is displayed, False otherwise.
        """
        return self.is_element_displayed(VerticalSwipingPageLocators.item_locator(item_text))

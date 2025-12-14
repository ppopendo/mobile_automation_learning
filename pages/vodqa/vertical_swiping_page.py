"""Page Object for Vertical Swiping feature in VodQA application."""

from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent, HeaderBarComponentLocators


@dataclass(frozen=True)
class VerticalSwipingPageLocators:
    """Locators for Vertical Swiping page elements."""

    PAGE_TITLE: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='Vertical Swiping']"), init=False
    )
    SCROLLABLE_CONTAINER: Tuple[str, str] = field(default=(AppiumBy.XPATH, "//android.widget.ScrollView"), init=False)
    ITEM_1: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='List Item 1']"), init=False
    )
    ITEM_5: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='List Item 5']"), init=False
    )
    ITEM_10: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='List Item 10']"), init=False
    )
    ITEM_LAST: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='List Item 20']"), init=False
    )


class VerticalSwipingPage(BaseAppiumGestures, HeaderBarComponent):
    """Page Object for the Vertical Swiping screen in VodQA app.

    This page contains a scrollable list for testing vertical swipe gestures.
    """

    @allure.step("the user waits until the vertical swiping page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait for vertical swiping page to be fully loaded."""
        self.wait_until_component_is_loaded(title="Vertical Swiping")

    @allure.step("the user navigates back from vertical swiping page")
    def tap_back_button(self) -> None:
        """Tap the back button to return to Samples List."""
        self.tap_element(HeaderBarComponentLocators.BACK_BUTTON)

    @property
    @allure.step("checking if item 1 is displayed")
    def is_item_1_displayed(self) -> bool:
        """Check if item 1 is displayed on screen."""
        return self.is_element_displayed(VerticalSwipingPageLocators.ITEM_1)

    @property
    @allure.step("checking if item 5 is displayed")
    def is_item_5_displayed(self) -> bool:
        """Check if item 5 is displayed on screen."""
        return self.is_element_displayed(VerticalSwipingPageLocators.ITEM_5)

    @property
    @allure.step("checking if item 10 is displayed")
    def is_item_10_displayed(self) -> bool:
        """Check if item 10 is displayed on screen."""
        return self.is_element_displayed(VerticalSwipingPageLocators.ITEM_10)

    @property
    @allure.step("checking if item 20 is displayed")
    def is_item_last_displayed(self) -> bool:
        """Check if last item is displayed on screen."""
        return self.is_element_displayed(VerticalSwipingPageLocators.ITEM_LAST)

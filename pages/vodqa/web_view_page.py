from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent


@dataclass(frozen=True)
class WebViewLocators:
    """Locators for Web View page elements."""

    HEADER: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='Hacker News']"), init=False
    )
    NEWS_TITLE: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='{title}']"),
        init=False,
        metadata={
            "doc": (
                "This locator is a format string and should not be used directly. "
                "Format the locator with the required title parameter in the is_news_title_displayed method."
            )
        },
    )
    MORE_LINK_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='More']"), init=False
    )
    SEARCH_INPUT: Tuple[str, str] = field(default=(AppiumBy.XPATH, "//android.widget.EditText"), init=False)
    SEARCH_RESULT_ITEM: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.view.View[@text='{search_value}']"),
        init=False,
        metadata={
            "doc": (
                "This locator is a format string and should not be used directly. "
                "Format the locator with the required search_value parameter in the get_search_results_count method."
            )
        },
    )


class WebViewPage(BaseAppiumGestures, HeaderBarComponent):
    """Page object for the Web View screen, providing interactions with
    the Hacker News web content.
    Before start interacting with this page, ensure that the web view context is set:
    self.driver.switch_to.context('WEBVIEW_com.vodqareactnative')
    """

    @allure.step("the user waits until the web view page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait until the Web View page is fully loaded and ready for interaction.

        This method uses the shared header bar component logic to verify that the
        "Webview" screen is displayed before proceeding with further actions.

        Args:
            None

        Returns:
            None
        """
        self.wait_until_component_is_loaded(title="Webview")

    @allure.step("the user checks if news title '{title}' is displayed")
    def is_news_title_displayed(self, title: str) -> bool:
        """Check if a news title with the given text is displayed on the page.

        Args:
            title: The text of the news title to search for.

        Returns:
            bool: True if the news title is displayed, False otherwise.
        """
        news_title_locator = (
            WebViewLocators.NEWS_TITLE[0],
            WebViewLocators.NEWS_TITLE[1].format(title=title),
        )
        return self.is_element_displayed(news_title_locator)

    @allure.step("the user taps on the 'More' link button")
    def tap_more_link_button(self) -> None:
        """Tap the 'More' link button to load additional content.

        Args:
            None

        Returns:
            None
        """
        self.scroll_element_into_view(WebViewLocators.MORE_LINK_BUTTON)
        self.tap_element(WebViewLocators.MORE_LINK_BUTTON)

    @allure.step("the user enters search value '{search_value}' in the search input")
    def enter_search_value(self, search_value: str) -> None:
        """Enter a search value into the web view search input field.

        Args:
            search_value: The text value to type into the search input.

        Returns:
            None
        """
        self.scroll_element_into_view(WebViewLocators.SEARCH_INPUT)
        self.tap_element(WebViewLocators.SEARCH_INPUT)
        self.safe_send_keys(WebViewLocators.SEARCH_INPUT, search_value)

    @allure.step("the user gets the count of search results for '{search_value}'")
    def get_search_results_count(self, search_value: str) -> int:
        """Get the count of search result items matching the search value.

        Args:
            search_value: The text value to search for in results.

        Returns:
            int: The number of elements found matching the search value.
        """
        search_result_locator = (
            WebViewLocators.SEARCH_RESULT_ITEM[0],
            WebViewLocators.SEARCH_RESULT_ITEM[1].format(search_value=search_value),
        )
        elements = self._driver.find_elements(*search_result_locator)
        return len(elements)

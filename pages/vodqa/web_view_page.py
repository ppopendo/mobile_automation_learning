from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

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
                "Use the 'news_title_locator' static method to construct the locator with the required title."
            )
        },
    )
    MORE_LINK_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='More']"), init=False
    )
    SEARCH_INPUT: Tuple[str, str] = field(default=(AppiumBy.XPATH, "//android.widget.EditText"), init=False)
    SEARCH_RESULT_ITEM: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.view.View[contains(@text, '{search_value}')]"),
        init=False,
        metadata={
            "doc": (
                "This locator is a format string and should not be used directly. "
                "Use the 'search_result_locator' static method to construct the locator with the required search value."
            )
        },
    )
    DROPDOWN_STORIES: Tuple[str, str] = field(default=(AppiumBy.ID, "downshift-0-label"), init=False)
    DROPDOWN_POPULARITY: Tuple[str, str] = field(default=(AppiumBy.ID, "downshift-1-label"), init=False)
    DROPDOWN_ALL_TIME: Tuple[str, str] = field(default=(AppiumBy.ID, "downshift-2-label"), init=False)

    @staticmethod
    def news_title_locator(title: str) -> Tuple[str, str]:
        """
        Returns the NEWS_TITLE locator tuple with the given title.
        Args:
            title (str): The title text to match.
        Returns:
            Tuple[str, str]: The locator tuple for the given title.
        """
        return (
            WebViewLocators.NEWS_TITLE[0],
            WebViewLocators.NEWS_TITLE[1].format(title=title),
        )

    @staticmethod
    def search_result_locator(search_value: str) -> Tuple[str, str]:
        """
        Returns the SEARCH_RESULT_ITEM locator tuple with the given search value.
        Args:
            search_value (str): The search value text to match.
        Returns:
            Tuple[str, str]: The locator tuple for the given search value.
        """
        return (
            WebViewLocators.SEARCH_RESULT_ITEM[0],
            WebViewLocators.SEARCH_RESULT_ITEM[1].format(search_value=search_value),
        )


class WebViewPage(BaseAppiumGestures, HeaderBarComponent):
    """Page object for the Web View screen, providing interactions with the Hacker News web content."""

    @allure.step("the user waits until the web view page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        """Wait until the Web View page is fully loaded and ready for interaction.

        This method uses the shared header bar component logic to verify that the
        "Webview" screen is displayed before proceeding with further actions.
        """
        self.wait_until_component_is_loaded(title="Webview")

    @property
    @allure.step("retrieving if the 'Hacker News' header is displayed")
    def is_header_displayed(self) -> bool:
        """Check if the 'Hacker News' header is displayed on the page."""
        return self.is_element_displayed(WebViewLocators.HEADER)

    @allure.step("the user checks if news title '{title}' is displayed")
    def is_news_title_displayed(self, title: str) -> bool:
        """Check if a news title with the given text is displayed on the page.

        Args:
            title: The text of the news title to search for.

        Returns:
            bool: True if the news title is displayed, False otherwise.
        """
        news_title_locator = WebViewLocators.news_title_locator(title)
        return self.is_element_displayed(news_title_locator)

    @allure.step("the user taps on the 'More' link button")
    def tap_more_link_button(self) -> None:
        """Tap the 'More' link button to load additional content."""
        self.scroll_element_into_view(WebViewLocators.MORE_LINK_BUTTON, max_scrolls=22)
        self.tap_element(WebViewLocators.MORE_LINK_BUTTON)

    @allure.step("the user enters search value '{search_value}' in the search input")
    def enter_search_value(self, search_value: str) -> None:
        """Enter a search value into the web view search input field.

        Args:
            search_value: The text value to type into the search input.
        """
        self.scroll_element_into_view(WebViewLocators.SEARCH_INPUT, max_scrolls=22)
        self.send_keys_and_press_go(WebViewLocators.SEARCH_INPUT, search_value)

    @allure.step("the user submits the search form")
    def submit_search(self) -> None:
        """Submit the search form by pressing Enter."""
        element = self.wait_for_element(WebViewLocators.SEARCH_INPUT)
        element.send_keys(Keys.ENTER)

    @allure.step("retrieving the count of search results for '{search_value}'")
    def get_search_results_count(self, search_value: str) -> int:
        """Get the count of search result items matching the search value.

        Args:
            search_value: The text value to search for in results.

        Returns:
            int: The number of elements found matching the search value.
        """
        search_result_locator = WebViewLocators.search_result_locator(search_value)
        try:
            elements = self.wait_for_element(
                search_result_locator,
                condition=EC.presence_of_all_elements_located,
                timeout=self._short_timeout,
            )
            return len(elements)
        except TimeoutException:
            return 0

    def is_dropdown_stories_displayed(self) -> bool:
        """Check if the 'Stories' dropdown is displayed."""
        self.wait_for_element(WebViewLocators.DROPDOWN_STORIES)
        return self.is_element_displayed(WebViewLocators.DROPDOWN_STORIES)

    def is_dropdown_popularity_displayed(self) -> bool:
        """Check if the 'Popularity' dropdown is displayed."""
        return self.is_element_displayed(WebViewLocators.DROPDOWN_POPULARITY)

    def is_dropdown_all_time_displayed(self) -> bool:
        """Check if the 'All Time' dropdown is displayed."""
        return self.is_element_displayed(WebViewLocators.DROPDOWN_ALL_TIME)

    @allure.step("the user taps the search input field")
    def tap_search_input(self) -> None:
        """Tap the search input field to focus it."""
        self.scroll_element_into_view(WebViewLocators.SEARCH_INPUT, max_scrolls=22)
        self.tap_element(WebViewLocators.SEARCH_INPUT)

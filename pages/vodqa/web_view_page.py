from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent


@dataclass(frozen=True)
class WebViewLocators:
    HEADER: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='Hacker News']"), init=False
    )
    NEWS_TITLE: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='{title}']"), init=False
    )
    MORE_LINK_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='More']"), init=False
    )
    SEARCH_INPUT: Tuple[str, str] = field(default=(AppiumBy.XPATH, "//android.widget.EditText"), init=False)
    SEARCH_RESULT_ITEM: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.view.View[@text='{search_value}']"), init=False
    )


class WebViewPage(BaseAppiumGestures, HeaderBarComponent):
    """Page object for the Web View screen, providing interactions with
    the Hacker News web content.
    Before start interacting with this page, ensure that the web view context is set:
    self.driver.switch_to.context('WEBVIEW_com.vodqareactnative')
    """

    @allure.step("the user waits until the web view page is loaded")
    def wait_until_page_is_loaded(self) -> None:
        self.wait_until_component_is_loaded(title="Webview")

    @allure.step("the user checks if news title '{title}' is displayed")
    def is_news_title_displayed(self, title: str) -> bool:
        news_title_locator = (
            WebViewLocators.NEWS_TITLE[0],
            WebViewLocators.NEWS_TITLE[1].format(title=title),
        )
        return self.is_element_displayed(news_title_locator)

    @allure.step("the user taps on the 'More' link button")
    def tap_more_link_button(self) -> None:
        self.scroll_element_into_view(WebViewLocators.MORE_LINK_BUTTON)
        self.tap_element(WebViewLocators.MORE_LINK_BUTTON)

    @allure.step("the user enters search value '{search_value}' in the search input")
    def enter_search_value(self, search_value: str) -> None:
        self.scroll_element_into_view(WebViewLocators.SEARCH_INPUT)
        self.tap_element(WebViewLocators.SEARCH_INPUT)
        self.safe_send_keys(WebViewLocators.SEARCH_INPUT, search_value)

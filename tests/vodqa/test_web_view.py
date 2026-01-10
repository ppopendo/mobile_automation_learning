"""Test suite for Web View feature in VodQA application.
This module contains tests for web view functionality.
Tests verify header display, "More" button functionality, and search capabilities.
"""

import allure
import pytest

from pages.vodqa.web_view_page import WebViewLocators, WebViewPage


@allure.feature("VodQA Samples")
@allure.story("Web View")
class TestWebView:
    """Test class for Web View feature functionality."""

    @pytest.mark.tcid("TC-22-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test web view page displays correct header")
    def test_web_view_header_is_displayed(self, web_view_page: WebViewPage) -> None:
        """Verify that the Web View page displays the correct header 'Hacker News'.
        Expected:
            - Header with text 'Hacker News' is displayed
        """
        actual = {
            "header_displayed": web_view_page.is_element_displayed(WebViewLocators.HEADER),
        }

        expected = {
            "header_displayed": True,
        }

        assert actual == expected, f"Web View header validation failed: {actual}"

    @pytest.mark.tcid("TC-22-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test web view 'More' button displays header after click")
    def test_web_view_more_button_shows_header(self, web_view_page: WebViewPage) -> None:
        """Verify that clicking the 'More' button in Web View still displays the header.
        Expected:
            - Header is displayed after clicking 'More' button
        """
        # Scroll to bottom and click the 'More' button
        web_view_page.tap_more_link_button()

        # Verify header is still displayed
        actual = {
            "header_displayed": web_view_page.is_element_displayed(WebViewLocators.HEADER),
        }

        expected = {
            "header_displayed": True,
        }

        assert actual == expected, f"Web View header validation after 'More' click failed: {actual}"

    @pytest.mark.tcid("TC-22-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test web view search functionality returns results")
    def test_web_view_search_returns_results(self, web_view_page: WebViewPage) -> None:
        """Verify that searching for 'Bluescreen' in Web View returns matching results.
        Expected:
            - Search results count for 'Bluescreen' is greater than 0
        """
        search_value = "Bluescreen"

        # Scroll to search input, enter search value and press Enter
        web_view_page.enter_search_value(search_value)
        web_view_page.submit_search()

        # Get the count of search results
        results_count = web_view_page.get_search_results_count(search_value)

        # Verify that we have at least one result
        actual = {
            "has_results": results_count > 0,
            "results_count": results_count,
        }

        expected = {
            "has_results": True,
            "results_count": results_count,  # Dynamic value, just verify it's present
        }

        assert actual == expected, f"Web View search validation failed: {actual}"

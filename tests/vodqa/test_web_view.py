"""Test suite for Web View feature in VodQA application.
This module contains tests for web view functionality.
Tests verify header display, "More" button functionality, and search capabilities.
"""

import allure
import pytest

from pages.vodqa.web_view_page import WebViewPage


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
        assert web_view_page.is_header_displayed, "Web View header should be displayed"

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
        assert web_view_page.is_header_displayed, "Web View header should be displayed after clicking 'More' button"

    @pytest.mark.tcid("TC-22-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test web view search functionality returns results")
    def test_web_view_search_returns_results(self, web_view_page: WebViewPage) -> None:
        """Verify that searching for 'Bluescreen' in Web View returns at least 2 matching results.
        Expected:
            - Search results count for 'Bluescreen' is at least 2
        """
        search_value = "Bluescreen"

        # Scroll to search input, enter search value and press Go
        web_view_page.enter_search_value(search_value)
        assert web_view_page.is_dropdown_stories_displayed(), (
            "Dropdown stories not displayed after entering search value."
        )

        # Get the count of search results
        results_count = web_view_page.get_search_results_count(search_value)

        # Verify that we have at least 2 results
        assert results_count >= 2, f"Expected at least 2 search results for '{search_value}', but found {results_count}"

    @pytest.mark.tcid("TC-22-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test web view search dropdown displays stories")
    def test_web_view_search_dropdown_displays_stories(self, web_view_page: WebViewPage) -> None:
        """Verify that dropdown with stories is displayed after entering search value."""
        search_value = "Bluescreen"

        # Scroll to search input, enter search value and press Go
        web_view_page.tap_search_input()
        web_view_page.enter_search_value(search_value)

        # Verify that we have at least one result
        assert (
            web_view_page.is_dropdown_stories_displayed()
        ), "Dropdown stories should be displayed after entering search value"

    @pytest.mark.tcid("TC-22-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Diagnostic test for WebView context availability")
    def test_webview_context_diagnostic(self, driver, samples_list_page) -> None:
        """Diagnostic test to check WebView context availability.

        This test navigates to WebView screen and diagnoses available contexts.
        Used for troubleshooting when WebView context is not found.
        """
        # Navigate to Web View page
        samples_list_page.swipe_up_and_validate_sample_name("Web View")
        samples_list_page.tap_web_view()

        # Create page object without switching context
        page = WebViewPage(driver)

        # Run diagnostics
        diagnostic_info = page.diagnose_webview_contexts()

        # Attach diagnostic info to Allure report
        allure.attach(
            f"Current context: {diagnostic_info['current_context']}\n"
            f"Available contexts: {diagnostic_info['available_contexts']}\n"
            f"WebView available: {diagnostic_info['webview_available']}\n"
            f"Suggestions: {', '.join(diagnostic_info['suggestions']) if diagnostic_info['suggestions'] else 'None'}",
            name="WebView Diagnostic Results",
            attachment_type=allure.attachment_type.TEXT,
        )

        # Assert - this test passes if diagnostics run, fails if WebView is not available
        assert diagnostic_info['webview_available'], (
            f"WebView context not available. Only found: {diagnostic_info['available_contexts']}. "
            "The app may not have WebView debugging enabled."
        )

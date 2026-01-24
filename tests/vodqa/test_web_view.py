"""Test suite for Web View feature in VodQA application.
This module contains tests for web view functionality.
Tests verify header display, "More" button functionality, and search capabilities.
"""

import logging
import os

import allure
import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from pages.vodqa.samples_list_page import SamplesListPage
from pages.vodqa.web_view_page import WebViewPage

logger = logging.getLogger(__name__)


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
        actual = {"header_displayed": web_view_page.is_header_displayed}
        expected = {"header_displayed": True}

        assert actual == expected, f"Web View header state mismatch: {actual}"

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
        assert web_view_page.is_header_displayed, "Header should be displayed after clicking 'More' button"

    @pytest.mark.tcid("TC-22-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test web view search functionality returns results")
    def test_web_view_search_returns_results(self, web_view_page: WebViewPage) -> None:
        """Verify that searching for 'Bluescreen' in Web View returns at least 1 matching result.
        Expected:
            - Dropdown stories are displayed after entering search value
            - Search results count for 'Bluescreen' is at least 1
        """
        search_value = "Bluescreen"

        # Scroll to search input, enter search value and press Go
        web_view_page.tap_search_input()
        web_view_page.enter_search_value(search_value)

        # Get search state and results count
        results_count = web_view_page.get_search_results_count(search_value)

        actual = {
            "dropdown_displayed": web_view_page.is_dropdown_stories_displayed,
            "results_count_at_least_1": results_count >= 1,
        }

        expected = {
            "dropdown_displayed": True,
            "results_count_at_least_1": True,
        }

        assert actual == expected, f"Search state mismatch. Expected {expected}, got: {actual}"

    @pytest.mark.tcid("TC-22-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test web view search dropdown displays stories")
    def test_web_view_search_dropdown_displays_stories(self, web_view_page: WebViewPage) -> None:
        """Verify that dropdown with stories is displayed after entering search value."""
        search_value = "Bluescreen"

        # Enter search value and press Go
        web_view_page.tap_search_input()
        web_view_page.enter_search_value(search_value)

        assert (
            web_view_page.is_dropdown_stories_displayed
        ), f"Dropdown with stories should be displayed after searching for '{search_value}'"

    @pytest.mark.tcid("TC-22-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Diagnostic test for WebView context availability")
    def test_webview_context_diagnostic(self, samples_list_page: SamplesListPage) -> None:
        """Diagnostic test to check WebView context availability.

        This test navigates to WebView screen and diagnoses available contexts.
        Used for troubleshooting when WebView context is not found.

        Note: This test is environment/device dependent (requires WebView debugging enabled).
        Set RUN_DIAGNOSTIC_TESTS=true to enable this test.
        """
        # Skip test unless explicitly enabled via environment variable
        if not os.getenv("RUN_DIAGNOSTIC_TESTS", "false").lower() == "true":
            pytest.skip("Diagnostic test skipped. Set RUN_DIAGNOSTIC_TESTS=true to enable.")

        # Navigate to Web View page
        samples_list_page.swipe_up_and_validate_sample_name("Web View")
        samples_list_page.tap_web_view()

        # Create page object without switching context
        page = WebViewPage(samples_list_page.driver)

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

        # Explicit teardown: Navigate back to Samples List
        try:
            page.tap_back_button()
            samples_list_page.wait_until_page_is_loaded()
        except (TimeoutException, NoSuchElementException) as e:
            logger.warning(f"Cleanup failed in diagnostic test: {e}")

        # Assert - this test passes if diagnostics run, fails if WebView is not available
        assert diagnostic_info["webview_available"], (
            f"WebView context not available. Only found: {diagnostic_info['available_contexts']}. "
            "The app may not have WebView debugging enabled."
        )

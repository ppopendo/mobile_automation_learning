"""Test suite for Native View Demo feature in VodQA application.
This module contains tests for native view functionality.
Tests verify container text content and validation.
"""

import allure
import pytest

from pages.vodqa.native_view_demo_page import NativeViewDemoPage


@allure.feature("VodQA Samples")
@allure.story("Native View Demo")
class TestNativeViewDemo:
    """Test class for Native View Demo feature functionality."""

    @pytest.mark.tcid("TC-21-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test native view demo page has required elements")
    def test_native_view_demo_page_has_elements(self, native_view_demo_page: NativeViewDemoPage) -> None:
        """Verify that the Native View Demo page contains required elements with text content.
        Expected:
            - Container text 1 is displayed and not empty
            - Container text 2 is displayed and not empty
            - Container text 3 is displayed and not empty
        """
        # Get actual text values
        container_1_text = native_view_demo_page.container_text_1
        container_2_text = native_view_demo_page.container_text_2
        container_3_text = native_view_demo_page.container_text_3

        # Assert multiple values using actual/expected pattern
        actual = {
            "has_container_1": len(container_1_text) > 0,
            "has_container_2": len(container_2_text) > 0,
            "has_container_3": len(container_3_text) > 0,
        }

        expected = {
            "has_container_1": True,
            "has_container_2": True,
            "has_container_3": True,
        }

        assert actual == expected, f"Native View Demo page elements mismatch: {actual}"

    @pytest.mark.tcid("TC-21-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test native view containers display expected text content")
    def test_native_view_containers_text_content(self, native_view_demo_page: NativeViewDemoPage) -> None:
        """Verify that the Native View Demo containers display descriptive text.
        Expected:
            - Each container text is a non-empty string
            - Container texts are different from each other
            - Each container has meaningful content (more than just whitespace)
        """
        # Get container text values
        container_1_text = native_view_demo_page.container_text_1.strip()
        container_2_text = native_view_demo_page.container_text_2.strip()
        container_3_text = native_view_demo_page.container_text_3.strip()

        # Assert that all containers have unique, non-empty content
        actual = {
            "container_1_has_content": len(container_1_text) > 0,
            "container_2_has_content": len(container_2_text) > 0,
            "container_3_has_content": len(container_3_text) > 0,
            "all_unique": len({container_1_text, container_2_text, container_3_text}) == 3,
        }

        expected = {
            "container_1_has_content": True,
            "container_2_has_content": True,
            "container_3_has_content": True,
            "all_unique": True,
        }

        assert actual == expected, f"Native View container text validation failed: {actual}"

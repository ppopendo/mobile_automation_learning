"""Test suite for Native View Demo feature in VodQA application.
This module contains tests for native view functionality.
Tests verify property methods for retrieving container text values.
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
        """Verify that the Native View Demo page contains required elements.
        Expected:
            - Container text 1 is displayed and not empty
            - Container text 2 is displayed and not empty
            - Container text 3 is displayed and not empty
        """
        # Assert multiple values using actual/expected pattern
        actual = {
            "has_container_1": len(native_view_demo_page.container_text_1) > 0,
            "has_container_2": len(native_view_demo_page.container_text_2) > 0,
            "has_container_3": len(native_view_demo_page.container_text_3) > 0,
        }

        expected = {
            "has_container_1": True,
            "has_container_2": True,
            "has_container_3": True,
        }

        assert actual == expected, f"Native View Demo page elements mismatch: {actual}"

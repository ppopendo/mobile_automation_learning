"""Test suite for Slider feature in VodQA application.

This module contains tests for slider interaction functionality.
Tests verify that the slider responds to touch gestures and displays correct values.
"""

import os

import allure
import pytest
from pages.vodqa.slider_page import SliderPage

# Tolerance for slider drag gesture assertions (handles device rounding differences)
SLIDER_DRAG_TOLERANCE = 2.0


@allure.feature("VodQA Samples")
@allure.story("Slider")
class TestSlider:
    """Test class for Slider feature functionality."""

    @pytest.mark.tcid("TC-02-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test slider page contains two sliders")
    def test_slider_page_has_two_sliders(self, slider_page: SliderPage) -> None:
        """Verify that the Slider page contains two slider elements.
        Expected:
            - Slider 1 is visible on the page
            - Slider 2 is visible on the page
        """
        assert slider_page.is_slider_1_displayed, "Slider 1 should be visible on the Slider page"
        assert slider_page.is_slider_2_displayed, "Slider 2 should be visible on the Slider page"

    @pytest.mark.tcid("TC-02-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test slider 1 interaction updates displayed value")
    def test_slider_1_interaction_updates_value(self, slider_page: SliderPage) -> None:
        """Test that tapping slider 1 at 50% updates the displayed value.
        Steps:
            1. Tap slider 1 at 50% position
            2. Verify the slider value is updated to expected value
        Expected:
            - Slider value reflects the 50% position
        """
        slider_page.tap_slider_1_at_percentage(50)
        assert slider_page.slider_display_value == 50, "Slider 1 should display a value after interaction"

    @pytest.mark.tcid("TC-02-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test slider 1 at {percentage}% position")
    @pytest.mark.parametrize("percentage, expected_value", [(0, 0), (50, 64.0), (100, 1.0)], ids=["0%", "50%", "100%"])
    def test_slider_1_multiple_positions(self, slider_page: SliderPage, percentage: int, expected_value: float) -> None:
        """Test slider 1 interaction at different positions.
        Args:
            percentage: Target slider position (0%, 50%, 100%).
        Expected:
            - Slider responds to position change
            - Slider value is updated after interaction
        """
        slider_page.tap_slider_1_at_percentage(percentage)
        assert (
            slider_page.slider_1_value == expected_value
        ), f"Slider 1 should display a value after tapping at {percentage}%"


@allure.feature("VodQA Samples")
@allure.story("Slider Drag Gesture")
class TestSliderDragGesture:
    """Test class for Slider drag gesture functionality.

    These tests verify that sliders respond correctly to drag gestures,
    which simulate a finger dragging the slider thumb to a specific position.
    """

    @pytest.mark.tcid("TC-02-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag slider 1 to 75% position")
    def test_drag_slider_1_to_75_percent(self, slider_page: SliderPage) -> None:
        """Verify that dragging slider 1 to 75% position updates its value.

        Steps:
            1. Drag slider 1 thumb to 75% position
            2. Verify slider value is updated to approximately 75

        Expected:
            - Slider 1 display value reflects approximately 75% position (within tolerance)
        """
        slider_page.drag_slider_1_to_percentage(75)

        slider_value = slider_page.slider_display_value

        actual = {
            "is_displayed": slider_page.is_slider_1_displayed,
            "slider_value_within_tolerance": abs(slider_value - 75.0) <= SLIDER_DRAG_TOLERANCE,
        }
        expected = {
            "is_displayed": True,
            "slider_value_within_tolerance": True,
        }

        assert (
            actual == expected
        ), f"Slider state mismatch: actual value={slider_value}, expected=75.0±{SLIDER_DRAG_TOLERANCE}"

    @pytest.mark.tcid("TC-02-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag slider 2 to 25% position")
    def test_drag_slider_2_to_25_percent(self, slider_page: SliderPage) -> None:
        """Verify that dragging slider 2 to 25% position updates its value.

        Steps:
            1. Drag slider 2 thumb to 25% position
            2. Verify slider value is updated to approximately 25

        Expected:
            - Slider 2 display value reflects approximately 25% position (within tolerance)
        """
        slider_page.drag_slider_2_to_percentage(25)

        slider_value = slider_page.slider_2_value

        actual = {
            "is_displayed": slider_page.is_slider_2_displayed,
            "slider_value_within_tolerance": abs(slider_value - 25.0) <= SLIDER_DRAG_TOLERANCE,
        }
        expected = {
            "is_displayed": True,
            "slider_value_within_tolerance": True,
        }

        assert (
            actual == expected
        ), f"Slider state mismatch: actual value={slider_value}, expected=25.0±{SLIDER_DRAG_TOLERANCE}"

    @pytest.mark.tcid("TC-02-06")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag slider 1 to {target_percentage}% position")
    @pytest.mark.parametrize(
        "target_percentage, expected_value",
        [(0, 0.0), (25, 25.0), (50, 50.0), (75, 75.0), (100, 100.0)],
        ids=["0%", "25%", "50%", "75%", "100%"],
    )
    def test_drag_slider_1_multiple_positions(
        self, slider_page: SliderPage, target_percentage: int, expected_value: float
    ) -> None:
        """Test drag gesture on slider 1 at different target positions.

        Args:
            target_percentage: Target slider position (0-100%).
            expected_value: Expected slider display value after drag.

        Expected:
            - Slider responds to drag gesture at specified position
            - Slider display value matches expected value after drag (within tolerance)
        """
        slider_page.drag_slider_1_to_percentage(target_percentage)

        slider_value = slider_page.slider_display_value

        actual = {
            "is_displayed": slider_page.is_slider_1_displayed,
            "slider_value_within_tolerance": abs(slider_value - expected_value) <= SLIDER_DRAG_TOLERANCE,
        }
        expected = {
            "is_displayed": True,
            "slider_value_within_tolerance": True,
        }

        assert actual == expected, (
            f"Slider state mismatch after dragging to {target_percentage}%: "
            f"actual value={slider_value}, expected={expected_value}±{SLIDER_DRAG_TOLERANCE}"
        )

    @pytest.mark.tcid("TC-02-07")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag slider with different speeds")
    @pytest.mark.parametrize(
        "speed",
        [500, 1500, 3000],
        ids=["slow", "medium", "fast"],
    )
    def test_drag_slider_with_different_speeds(self, slider_page: SliderPage, speed: int) -> None:
        """Test drag gesture on slider with different drag speeds.

        Args:
            speed: Drag speed in pixels per second.

        Expected:
            - Drag gesture works correctly regardless of speed
            - Slider display value is updated to target position (50%) within tolerance
        """
        slider_page.drag_slider_1_to_percentage(50, speed=speed)

        slider_value = slider_page.slider_display_value

        actual = {
            "is_displayed": slider_page.is_slider_1_displayed,
            "slider_value_within_tolerance": abs(slider_value - 50.0) <= SLIDER_DRAG_TOLERANCE,
        }
        expected = {
            "is_displayed": True,
            "slider_value_within_tolerance": True,
        }

        assert (
            actual == expected
        ), f"Slider state mismatch at speed {speed}: actual value={slider_value}, expected=50.0±{SLIDER_DRAG_TOLERANCE}"


@allure.feature("VodQA Samples")
@allure.story("Slider Locator Verification")
class TestSliderLocatorVerification:
    """Test class for Slider locator verification and diagnostics.

    These tests verify that all slider locators are valid and working correctly.
    Use these tests during debug sessions to troubleshoot locator issues.
    """

    @pytest.mark.tcid("TC-02-08")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Test slider locators diagnostic")
    def test_slider_locators_diagnostic(self, slider_page: SliderPage) -> None:
        """Verify all slider locators are valid and elements are found.

        This diagnostic test attempts to find all slider elements using their
        defined locators and reports detailed information about each element.

        Steps:
            1. Run slider locators diagnostics
            2. Attach diagnostic info to Allure report
            3. Verify all locators found their elements

        Expected:
            - All slider locators successfully find their elements
            - Element properties are accessible and valid

        Note: This test is for debugging purposes.
        Set RUN_DIAGNOSTIC_TESTS to any value to enable this test.
        """
        # Skip test unless explicitly enabled via environment variable
        if not os.getenv("RUN_DIAGNOSTIC_TESTS"):
            pytest.skip("Diagnostic test skipped. Set RUN_DIAGNOSTIC_TESTS to any value to enable.")

        # Run diagnostics
        diagnostic_info = slider_page.diagnose_slider_locators()

        # Attach diagnostic info to Allure report
        allure.attach(
            f"Slider 1 locator:\n"
            f"  Strategy: {diagnostic_info['slider_1'].get('locator_strategy')}\n"
            f"  Value: {diagnostic_info['slider_1'].get('locator_value')}\n"
            f"  Found: {diagnostic_info['slider_1'].get('found')}\n"
            f"  Element info: {diagnostic_info['slider_1'].get('element_info')}\n\n"
            f"Slider 2 locator:\n"
            f"  Strategy: {diagnostic_info['slider_2'].get('locator_strategy')}\n"
            f"  Value: {diagnostic_info['slider_2'].get('locator_value')}\n"
            f"  Found: {diagnostic_info['slider_2'].get('found')}\n"
            f"  Element info: {diagnostic_info['slider_2'].get('element_info')}\n\n"
            f"Slider Display Value locator:\n"
            f"  Strategy: {diagnostic_info['slider_display_value'].get('locator_strategy')}\n"
            f"  Value: {diagnostic_info['slider_display_value'].get('locator_value')}\n"
            f"  Found: {diagnostic_info['slider_display_value'].get('found')}\n"
            f"  Element info: {diagnostic_info['slider_display_value'].get('element_info')}\n\n"
            f"All locators valid: {diagnostic_info['all_locators_valid']}\n"
            f"Suggestions: {', '.join(diagnostic_info['suggestions']) if diagnostic_info['suggestions'] else 'None'}",
            name="Slider Locators Diagnostic Report",
            attachment_type=allure.attachment_type.TEXT,
        )

        # Assert all locators are valid
        assert diagnostic_info["all_locators_valid"], (
            f"Not all slider locators are valid. "
            f"Slider 1 found: {diagnostic_info['slider_1'].get('found')}, "
            f"Slider 2 found: {diagnostic_info['slider_2'].get('found')}, "
            f"Display value found: {diagnostic_info['slider_display_value'].get('found')}. "
            f"Suggestions: {diagnostic_info['suggestions']}"
        )

    @pytest.mark.tcid("TC-02-09")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test slider 1 element properties are accessible")
    def test_slider_1_element_properties(self, slider_page: SliderPage) -> None:
        """Verify slider 1 element properties are accessible.

        Steps:
            1. Get slider 1 element info
            2. Verify all expected properties are present
            3. Verify element is displayed and enabled

        Expected:
            - Element has valid location and size
            - Element is displayed and enabled
            - Element has expected tag_name (SeekBar)

        Note: This test is for debugging purposes.
        Set RUN_DIAGNOSTIC_TESTS to any value to enable this test.
        """
        # Skip test unless explicitly enabled via environment variable
        if not os.getenv("RUN_DIAGNOSTIC_TESTS"):
            pytest.skip("Diagnostic test skipped. Set RUN_DIAGNOSTIC_TESTS to any value to enable.")

        element_info = slider_page.slider_1_element_info

        actual = {
            "has_location": element_info["location"] is not None,
            "has_size": element_info["size"] is not None,
            "is_displayed": element_info["is_displayed"],
            "is_enabled": element_info["is_enabled"],
            "has_positive_width": element_info["size"]["width"] > 0,
            "has_positive_height": element_info["size"]["height"] > 0,
            "tag_name": element_info["tag_name"],
        }
        expected = {
            "has_location": True,
            "has_size": True,
            "is_displayed": True,
            "is_enabled": True,
            "has_positive_width": True,
            "has_positive_height": True,
            "tag_name": "android.widget.SeekBar",
        }

        assert actual == expected, f"Slider 1 element properties mismatch: {actual}"

    @pytest.mark.tcid("TC-02-10")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test slider 2 element properties are accessible")
    def test_slider_2_element_properties(self, slider_page: SliderPage) -> None:
        """Verify slider 2 element properties are accessible.

        Steps:
            1. Get slider 2 element info
            2. Verify all expected properties are present
            3. Verify element is displayed and enabled

        Expected:
            - Element has valid location and size
            - Element is displayed and enabled
            - Element has expected tag_name (SeekBar)

        Note: This test is for debugging purposes.
        Set RUN_DIAGNOSTIC_TESTS to any value to enable this test.
        """
        # Skip test unless explicitly enabled via environment variable
        if not os.getenv("RUN_DIAGNOSTIC_TESTS"):
            pytest.skip("Diagnostic test skipped. Set RUN_DIAGNOSTIC_TESTS to any value to enable.")

        element_info = slider_page.slider_2_element_info

        actual = {
            "has_location": element_info["location"] is not None,
            "has_size": element_info["size"] is not None,
            "is_displayed": element_info["is_displayed"],
            "is_enabled": element_info["is_enabled"],
            "has_positive_width": element_info["size"]["width"] > 0,
            "has_positive_height": element_info["size"]["height"] > 0,
            "tag_name": element_info["tag_name"],
        }
        expected = {
            "has_location": True,
            "has_size": True,
            "is_displayed": True,
            "is_enabled": True,
            "has_positive_width": True,
            "has_positive_height": True,
            "tag_name": "android.widget.SeekBar",
        }

        assert actual == expected, f"Slider 2 element properties mismatch: {actual}"

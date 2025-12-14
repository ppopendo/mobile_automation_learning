"""Test suite for Swipe Gestures in VodQA application.

This module contains tests for horizontal swipe gestures.
Tests verify swipe_left and swipe_right methods from BaseAppiumGestures using the Slider page.
"""

import allure
import pytest

from pages.vodqa.slider_page import SliderPage, SliderPageLocators


@allure.feature("VodQA Samples")
@allure.story("Swipe Gestures")
class TestSwipeGestures:
    """Test class for horizontal swipe gesture functionality."""

    @pytest.mark.tcid("TC-07-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe_left gesture on element")
    def test_swipe_left_on_element(self, slider_page: SliderPage) -> None:
        """Verify that swipe_left gesture works on an element.

        Steps:
            1. Verify slider is displayed
            2. Perform swipe left gesture on slider element
            3. Verify swipe operation completes without errors

        Expected:
            - swipe_left method executes successfully
            - Swipe gesture is performed on target element
        """
        # Verify slider is displayed
        assert slider_page.is_slider_1_displayed, "Slider 1 should be visible"

        # Perform swipe left on slider element
        slider_page.swipe_left(locator=SliderPageLocators.SLIDER_1, percentage=0.75, speed=2500)

        # Verify the operation completed (method should not raise exceptions)

    @pytest.mark.tcid("TC-07-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe_right gesture on element")
    def test_swipe_right_on_element(self, slider_page: SliderPage) -> None:
        """Verify that swipe_right gesture works on an element.

        Steps:
            1. Verify slider is displayed
            2. Perform swipe right gesture on slider element
            3. Verify swipe operation completes without errors

        Expected:
            - swipe_right method executes successfully
            - Swipe gesture is performed on target element
        """
        # Verify slider is displayed
        assert slider_page.is_slider_1_displayed, "Slider 1 should be visible"

        # Perform swipe right on slider element
        slider_page.swipe_right(locator=SliderPageLocators.SLIDER_1, percentage=0.75, speed=2500)

        # Verify the operation completed (method should not raise exceptions)

    @pytest.mark.tcid("TC-07-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe_left gesture on screen without locator")
    def test_swipe_left_on_screen(self, slider_page: SliderPage) -> None:
        """Verify that swipe_left gesture works on screen without specific element.

        Steps:
            1. Perform swipe left gesture on screen (no locator)
            2. Verify swipe operation completes without errors

        Expected:
            - swipe_left method executes successfully without locator
            - Swipe gesture is performed on screen center
        """
        # Perform swipe left on screen
        slider_page.swipe_left(percentage=0.75, speed=2500)

        # Verify the operation completed (method should not raise exceptions)

    @pytest.mark.tcid("TC-07-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe_right gesture on screen without locator")
    def test_swipe_right_on_screen(self, slider_page: SliderPage) -> None:
        """Verify that swipe_right gesture works on screen without specific element.

        Steps:
            1. Perform swipe right gesture on screen (no locator)
            2. Verify swipe operation completes without errors

        Expected:
            - swipe_right method executes successfully without locator
            - Swipe gesture is performed on screen center
        """
        # Perform swipe right on screen
        slider_page.swipe_right(percentage=0.75, speed=2500)

        # Verify the operation completed (method should not raise exceptions)

    @pytest.mark.tcid("TC-07-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe gestures with different percentages")
    @pytest.mark.parametrize("percentage", [0.5, 0.75, 0.9], ids=["50%", "75%", "90%"])
    def test_swipe_with_different_percentages(self, slider_page: SliderPage, percentage: float) -> None:
        """Test swipe gestures with different swipe percentages.

        Args:
            percentage: Swipe distance as percentage (0.5, 0.75, 0.9).

        Expected:
            - Swipe methods work with different percentages
            - Operations complete successfully regardless of percentage used
        """
        # Swipe left with specified percentage
        slider_page.swipe_left(locator=SliderPageLocators.SLIDER_1, percentage=percentage, speed=2500)

        # Swipe right with specified percentage
        slider_page.swipe_right(locator=SliderPageLocators.SLIDER_2, percentage=percentage, speed=2500)

        # Verify the operations completed (methods should not raise exceptions)

    @pytest.mark.tcid("TC-07-06")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe gestures with different speeds")
    @pytest.mark.parametrize("speed", [1500, 2500, 3500], ids=["slow", "medium", "fast"])
    def test_swipe_with_different_speeds(self, slider_page: SliderPage, speed: int) -> None:
        """Test swipe gestures with different speed values.

        Args:
            speed: Swipe speed in pixels per second.

        Expected:
            - Swipe methods work with different speeds
            - Operations complete successfully regardless of speed used
        """
        # Swipe left with specified speed
        slider_page.swipe_left(locator=SliderPageLocators.SLIDER_1, percentage=0.75, speed=speed)

        # Swipe right with specified speed
        slider_page.swipe_right(locator=SliderPageLocators.SLIDER_2, percentage=0.75, speed=speed)

        # Verify the operations completed (methods should not raise exceptions)

    @pytest.mark.tcid("TC-07-07")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test sequential swipe gestures")
    def test_sequential_swipes(self, slider_page: SliderPage) -> None:
        """Test performing multiple swipe gestures sequentially.

        Steps:
            1. Perform swipe left
            2. Perform swipe right
            3. Perform swipe left again
            4. Verify all operations complete without errors

        Expected:
            - Multiple swipes can be performed sequentially
            - Each swipe operation completes successfully
        """
        # Perform sequential swipes
        slider_page.swipe_left(locator=SliderPageLocators.SLIDER_1, percentage=0.75, speed=2500)
        slider_page.swipe_right(locator=SliderPageLocators.SLIDER_1, percentage=0.75, speed=2500)
        slider_page.swipe_left(locator=SliderPageLocators.SLIDER_1, percentage=0.75, speed=2500)

        # Verify the operations completed (methods should not raise exceptions)

    @pytest.mark.tcid("TC-07-08")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swipe on multiple elements")
    def test_swipe_on_multiple_elements(self, slider_page: SliderPage) -> None:
        """Test performing swipe gestures on multiple elements.

        Steps:
            1. Swipe left on slider 1
            2. Swipe right on slider 2
            3. Verify all operations complete without errors

        Expected:
            - Swipe can be performed on different elements
            - Each operation completes successfully
        """
        # Swipe on first slider
        slider_page.swipe_left(locator=SliderPageLocators.SLIDER_1, percentage=0.75, speed=2500)

        # Swipe on second slider
        slider_page.swipe_right(locator=SliderPageLocators.SLIDER_2, percentage=0.75, speed=2500)

        # Verify the operations completed (methods should not raise exceptions)

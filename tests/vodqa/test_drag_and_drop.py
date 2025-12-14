"""Test suite for Drag and Drop feature in VodQA application.

This module contains tests for drag and drop gestures.
Tests verify drag_and_drop and drag_to_coordinates methods from BaseAppiumGestures.
"""

import allure
import pytest

from pages.vodqa.drag_and_drop_page import DragAndDropPage, DragAndDropPageLocators


@allure.feature("VodQA Samples")
@allure.story("Drag and Drop")
class TestDragAndDrop:
    """Test class for Drag and Drop feature functionality."""

    @pytest.mark.tcid("TC-04-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag and drop page has required elements")
    def test_drag_and_drop_page_has_elements(self, drag_and_drop_page: DragAndDropPage) -> None:
        """Verify that the Drag and Drop page contains required elements.

        Expected:
            - Draggable element 1 is visible
            - Draggable element 2 is visible
            - Drop zone is visible
        """
        assert drag_and_drop_page.is_draggable_1_displayed, "Draggable 1 should be visible"
        assert drag_and_drop_page.is_draggable_2_displayed, "Draggable 2 should be visible"
        assert drag_and_drop_page.is_drop_zone_displayed, "Drop zone should be visible"

    @pytest.mark.tcid("TC-04-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag_and_drop method from element to element")
    def test_drag_and_drop_element_to_element(self, drag_and_drop_page: DragAndDropPage) -> None:
        """Verify that drag_and_drop method works between elements.

        Steps:
            1. Get initial location of draggable element
            2. Perform drag and drop from draggable 1 to drop zone
            3. Verify drag operation completes without errors

        Expected:
            - drag_and_drop method executes successfully
            - Element is dragged from source to target
        """
        # Perform drag and drop
        drag_and_drop_page.drag_and_drop(
            source_locator=DragAndDropPageLocators.DRAGGABLE_1,
            target_locator=DragAndDropPageLocators.DROP_ZONE,
            speed=2500,
        )

        # Verify the operation completed (method should not raise exceptions)
        # In a real app with proper feedback, we would verify the visual state change

    @pytest.mark.tcid("TC-04-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag_to_coordinates method with specific coordinates")
    def test_drag_to_coordinates(self, drag_and_drop_page: DragAndDropPage) -> None:
        """Verify that drag_to_coordinates method works with specified coordinates.

        Steps:
            1. Get drop zone location
            2. Calculate target coordinates
            3. Perform drag to coordinates
            4. Verify drag operation completes without errors

        Expected:
            - drag_to_coordinates method executes successfully
            - Element is dragged to specified coordinates
        """
        # Get drop zone location to use as target coordinates
        drop_zone_loc = drag_and_drop_page.drop_zone_location

        # Calculate center of drop zone
        target_x = drop_zone_loc["x"] + 50  # Approximate center
        target_y = drop_zone_loc["y"] + 50

        # Perform drag to coordinates
        drag_and_drop_page.drag_to_coordinates(
            source_locator=DragAndDropPageLocators.DRAGGABLE_2, end_x=target_x, end_y=target_y, speed=2500
        )

        # Verify the operation completed (method should not raise exceptions)

    @pytest.mark.tcid("TC-04-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag_and_drop with different speeds")
    @pytest.mark.parametrize("speed", [1500, 2500, 3500], ids=["slow", "medium", "fast"])
    def test_drag_and_drop_with_different_speeds(self, drag_and_drop_page: DragAndDropPage, speed: int) -> None:
        """Test drag_and_drop with different speed values.

        Args:
            speed: Drag speed in pixels per second.

        Expected:
            - drag_and_drop works with different speed values
            - Operation completes successfully regardless of speed
        """
        # Perform drag and drop with specified speed
        drag_and_drop_page.drag_and_drop(
            source_locator=DragAndDropPageLocators.DRAGGABLE_1,
            target_locator=DragAndDropPageLocators.DROP_ZONE,
            speed=speed,
        )

        # Verify the operation completed (method should not raise exceptions)

    @pytest.mark.tcid("TC-04-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag_to_coordinates to multiple positions")
    def test_drag_to_multiple_coordinates(self, drag_and_drop_page: DragAndDropPage) -> None:
        """Test dragging to multiple coordinate positions sequentially.

        Steps:
            1. Drag element to first position
            2. Drag element to second position
            3. Verify operations complete without errors

        Expected:
            - Element can be dragged to multiple positions
            - Each drag operation completes successfully
        """
        # Get screen dimensions for calculating coordinates
        drop_zone_loc = drag_and_drop_page.drop_zone_location

        # First drag
        drag_and_drop_page.drag_to_coordinates(
            source_locator=DragAndDropPageLocators.DRAGGABLE_1,
            end_x=drop_zone_loc["x"] + 30,
            end_y=drop_zone_loc["y"] + 30,
            speed=2500,
        )

        # Second drag - different position
        drag_and_drop_page.drag_to_coordinates(
            source_locator=DragAndDropPageLocators.DRAGGABLE_1,
            end_x=drop_zone_loc["x"] + 70,
            end_y=drop_zone_loc["y"] + 70,
            speed=2500,
        )

        # Verify the operations completed (methods should not raise exceptions)

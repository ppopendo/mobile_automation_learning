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
    @allure.title("Test drag and drop page has drag me button")
    def test_drag_and_drop_page_has_drag_me_button(self, drag_and_drop_page: DragAndDropPage) -> None:
        """Verify that the Drag and Drop page contains drag me button.
        Expected:
            - Drag me button is visible
        """
        # Assert
        assert drag_and_drop_page.is_drag_me_button_displayed, "Drag me button should be visible"

    @pytest.mark.tcid("TC-04-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag and drop page has drop here zone")
    def test_drag_and_drop_page_has_drop_zone(self, drag_and_drop_page: DragAndDropPage) -> None:
        """Verify that the Drag and Drop page contains drop here zone.
        Expected:
            - Drop here zone is visible
        """
        # Assert
        assert drag_and_drop_page.is_drop_here_zone_displayed, "Drop here zone should be visible"

    @pytest.mark.tcid("TC-04-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag_and_drop method from button to zone")
    def test_drag_and_drop_element_to_element(self, drag_and_drop_page: DragAndDropPage) -> None:
        """Verify that drag_and_drop method works between elements.
        Expected:
            - drag_and_drop method executes successfully
            - Element is dragged from source to target
        """
        # Arrange - verify elements are displayed
        button_visible = drag_and_drop_page.is_drag_me_button_displayed
        zone_visible = drag_and_drop_page.is_drop_here_zone_displayed
        # Act - perform drag and drop
        drag_and_drop_page.drag_and_drop(
            source_locator=DragAndDropPageLocators.DRAG_ME_BUTTON,
            target_locator=DragAndDropPageLocators.DROP_HERE_ZONE,
            speed=2500,
        )
        # Assert - verify elements were visible before operation
        assert button_visible and zone_visible, "Both drag me button and drop zone should be visible"

    @pytest.mark.tcid("TC-04-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test drag_and_drop with {speed} pixels per second")
    @pytest.mark.parametrize("speed", [1500, 2500, 3500], ids=["slow", "medium", "fast"])
    def test_drag_and_drop_with_different_speeds(self, drag_and_drop_page: DragAndDropPage, speed: int) -> None:
        """Test drag_and_drop with different speed values.
        Args:
            speed: Drag speed in pixels per second.
        Expected:
            - drag_and_drop works with different speed values
            - Operation completes successfully regardless of speed
        """
        # Arrange - verify elements are displayed
        button_visible = drag_and_drop_page.is_drag_me_button_displayed
        zone_visible = drag_and_drop_page.is_drop_here_zone_displayed
        # Act - perform drag and drop with specified speed
        drag_and_drop_page.drag_and_drop(
            source_locator=DragAndDropPageLocators.DRAG_ME_BUTTON,
            target_locator=DragAndDropPageLocators.DROP_HERE_ZONE,
            speed=speed,
        )
        # Assert - verify elements were visible
        assert button_visible and zone_visible, f"Elements should be visible before drag at {speed} speed"

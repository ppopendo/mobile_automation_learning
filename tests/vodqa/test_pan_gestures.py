"""Test suite for Pan Gestures in VodQA application.

This module contains tests for pan gestures (swipe-based image panning)
in multiple directions (Up, Down, Left, Right) using the Photo View page.
"""

import allure
import pytest

from pages.vodqa.photo_view_page import PhotoViewPage


@allure.feature("VodQA Samples")
@allure.story("Pan Gestures")
class TestPanGestures:
    """Test class for pan gesture functionality on Photo View page."""

    @pytest.mark.tcid("TC-10-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan up gesture on photo element")
    def test_pan_up_on_photo(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan up gesture works on photo element.

        Expected:
            - pan_up_on_photo method executes successfully
            - Pan up gesture is performed on photo element
            - Photo image remains displayed after gesture
        """
        # Act - perform pan up on photo element
        photo_view_page.pan_up_on_photo()

        # Assert - verify photo is still displayed after gesture
        assert photo_view_page.is_photo_displayed, "Photo should be displayed after pan up gesture"

    @pytest.mark.tcid("TC-10-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan down gesture on photo element")
    def test_pan_down_on_photo(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan down gesture works on photo element.

        Expected:
            - pan_down_on_photo method executes successfully
            - Pan down gesture is performed on photo element
            - Photo image remains displayed after gesture
        """
        # Act - perform pan down on photo element
        photo_view_page.pan_down_on_photo()

        # Assert - verify photo is still displayed after gesture
        assert photo_view_page.is_photo_displayed, "Photo should be displayed after pan down gesture"

    @pytest.mark.tcid("TC-10-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan left gesture on photo element")
    def test_pan_left_on_photo(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan left gesture works on photo element.

        Expected:
            - pan_left_on_photo method executes successfully
            - Pan left gesture is performed on photo element
            - Photo image remains displayed after gesture
        """
        # Act - perform pan left on photo element
        photo_view_page.pan_left_on_photo()

        # Assert - verify photo is still displayed after gesture
        assert photo_view_page.is_photo_displayed, "Photo should be displayed after pan left gesture"

    @pytest.mark.tcid("TC-10-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan right gesture on photo element")
    def test_pan_right_on_photo(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan right gesture works on photo element.

        Expected:
            - pan_right_on_photo method executes successfully
            - Pan right gesture is performed on photo element
            - Photo image remains displayed after gesture
        """
        # Act - perform pan right on photo element
        photo_view_page.pan_right_on_photo()

        # Assert - verify photo is still displayed after gesture
        assert photo_view_page.is_photo_displayed, "Photo should be displayed after pan right gesture"

    @pytest.mark.tcid("TC-10-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan up gesture on screen center")
    def test_pan_up_on_screen(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan up gesture works on screen center.

        Expected:
            - pan_up_on_screen method executes successfully
            - Pan up gesture is performed on screen center
            - Photo image remains displayed after gesture
        """
        # Act - perform pan up on screen center
        photo_view_page.pan_up_on_screen()

        # Assert - verify photo is still displayed after gesture
        assert photo_view_page.is_photo_displayed, "Photo should be displayed after pan up gesture on screen"

    @pytest.mark.tcid("TC-10-06")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan down gesture on screen center")
    def test_pan_down_on_screen(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan down gesture works on screen center.

        Expected:
            - pan_down_on_screen method executes successfully
            - Pan down gesture is performed on screen center
            - Photo image remains displayed after gesture
        """
        # Act - perform pan down on screen center
        photo_view_page.pan_down_on_screen()

        # Assert - verify photo is still displayed after gesture
        assert photo_view_page.is_photo_displayed, "Photo should be displayed after pan down gesture on screen"

    @pytest.mark.tcid("TC-10-07")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan left gesture on screen center")
    def test_pan_left_on_screen(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan left gesture works on screen center.

        Expected:
            - pan_left_on_screen method executes successfully
            - Pan left gesture is performed on screen center
            - Photo image remains displayed after gesture
        """
        # Act - perform pan left on screen center
        photo_view_page.pan_left_on_screen()

        # Assert - verify photo is still displayed after gesture
        assert photo_view_page.is_photo_displayed, "Photo should be displayed after pan left gesture on screen"

    @pytest.mark.tcid("TC-10-08")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan right gesture on screen center")
    def test_pan_right_on_screen(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan right gesture works on screen center.

        Expected:
            - pan_right_on_screen method executes successfully
            - Pan right gesture is performed on screen center
            - Photo image remains displayed after gesture
        """
        # Act - perform pan right on screen center
        photo_view_page.pan_right_on_screen()

        # Assert - verify photo is still displayed after gesture
        assert photo_view_page.is_photo_displayed, "Photo should be displayed after pan right gesture on screen"

    @pytest.mark.tcid("TC-10-09")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan gestures with different percentages")
    @pytest.mark.parametrize(
        "direction,percentage",
        [
            ("up", 0.25),
            ("up", 0.5),
            ("down", 0.25),
            ("down", 0.5),
            ("left", 0.25),
            ("left", 0.5),
            ("right", 0.25),
            ("right", 0.5),
        ],
        ids=[
            "pan_up_25%",
            "pan_up_50%",
            "pan_down_25%",
            "pan_down_50%",
            "pan_left_25%",
            "pan_left_50%",
            "pan_right_25%",
            "pan_right_50%",
        ],
    )
    def test_pan_with_different_percentages(
        self, photo_view_page: PhotoViewPage, direction: str, percentage: float
    ) -> None:
        """Test pan gestures with different direction and percentage combinations.

        Args:
            direction: Pan direction - 'up', 'down', 'left', or 'right'.
            percentage: Pan distance as percentage (0.25, 0.5).

        Expected:
            - Pan method works with different percentages
            - Operation completes successfully
            - Photo image remains displayed and has valid dimensions
        """
        # Arrange - get pan method based on direction
        pan_methods = {
            "up": photo_view_page.pan_up_on_photo,
            "down": photo_view_page.pan_down_on_photo,
            "left": photo_view_page.pan_left_on_photo,
            "right": photo_view_page.pan_right_on_photo,
        }

        # Act - perform pan with specified direction and percentage
        pan_methods[direction](percentage=percentage)

        # Assert - verify photo is displayed and has valid size
        size = photo_view_page.photo_image_size
        actual = {
            "is_displayed": photo_view_page.is_photo_displayed,
            "width_valid": size["width"] > 0,
            "height_valid": size["height"] > 0,
        }

        expected = {
            "is_displayed": True,
            "width_valid": True,
            "height_valid": True,
        }

        assert actual == expected, f"Photo state mismatch after pan {direction}: {actual}"

    @pytest.mark.tcid("TC-10-10")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test sequential pan gestures in all directions")
    def test_sequential_pan_all_directions(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that sequential pan gestures in all directions work correctly.

        Expected:
            - Pan gestures in all four directions execute successfully
            - Photo image remains displayed throughout all gestures
        """
        # Act - perform pan gestures in all directions sequentially
        photo_view_page.pan_up_on_photo(percentage=0.3)
        photo_view_page.pan_down_on_photo(percentage=0.3)
        photo_view_page.pan_left_on_photo(percentage=0.3)
        photo_view_page.pan_right_on_photo(percentage=0.3)

        # Assert - verify photo is still displayed after all gestures
        assert photo_view_page.is_photo_displayed, "Photo should be displayed after sequential pan gestures"

    @pytest.mark.tcid("TC-10-11")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test zoom in then pan gesture combination")
    def test_zoom_then_pan_combination(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan gestures work correctly after zooming in.

        Expected:
            - Pinch open (zoom in) executes successfully
            - Pan gesture executes successfully on zoomed image
            - Photo image remains displayed after combined gestures
        """
        # Act - zoom in first, then pan
        photo_view_page.pinch_open_on_photo(percentage=0.5)
        photo_view_page.pan_up_on_photo(percentage=0.3)
        photo_view_page.pan_left_on_photo(percentage=0.3)

        # Assert - verify photo is still displayed
        actual = {
            "is_displayed": photo_view_page.is_photo_displayed,
            "size_width_valid": photo_view_page.photo_image_size["width"] > 0,
            "size_height_valid": photo_view_page.photo_image_size["height"] > 0,
        }

        expected = {
            "is_displayed": True,
            "size_width_valid": True,
            "size_height_valid": True,
        }

        assert actual == expected, f"Photo state mismatch after zoom + pan: {actual}"

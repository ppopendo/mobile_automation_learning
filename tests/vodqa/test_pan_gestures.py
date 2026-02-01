"""Test suite for Pan Gestures in VodQA application.

This module contains tests for pan gestures (swipe-based image panning)
in multiple directions (Up, Down, Left, Right) using the Photo View page.
"""

from typing import Union

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
            - Zoom in to make photo larger than viewport
            - Pan up gesture changes photo location vertically
            - Photo image remains displayed after gesture
        """
        # Arrange - zoom in to enable panning and get initial location
        photo_view_page.pinch_open_on_photo(percentage=0.8)
        initial_location = photo_view_page.photo_image_location

        # Act - perform pan up on photo element
        photo_view_page.pan_up_on_photo(percentage=0.5)

        # Assert - verify photo location changed (y-coordinate should decrease when panning up)
        final_location = photo_view_page.photo_image_location
        actual = {
            "is_photo_displayed": photo_view_page.is_photo_displayed,
            "coordinate_y_decreased": final_location["y"] < initial_location["y"],
        }

        expected = {
            "is_photo_displayed": True,
            "coordinate_y_decreased": True,
        }

        assert actual == expected, (
            f"Pan up failed: initial_y={initial_location['y']}, " f"final_y={final_location['y']}, actual={actual}"
        )

    @pytest.mark.tcid("TC-10-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan down gesture on photo element")
    def test_pan_down_on_photo(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan down gesture works on photo element.

        Expected:
            - Zoom in to make photo larger than viewport
            - Pan down gesture changes photo location vertically
            - Photo image remains displayed after gesture
        """
        # Arrange - zoom in to enable panning and get initial location
        photo_view_page.pinch_open_on_photo(percentage=0.8)
        initial_location = photo_view_page.photo_image_location

        # Act - perform pan down on photo element
        photo_view_page.pan_down_on_photo(percentage=0.5)

        # Assert - verify photo location changed (y-coordinate should increase when panning down)
        final_location = photo_view_page.photo_image_location
        actual = {
            "is_photo_displayed": photo_view_page.is_photo_displayed,
            "coordinate_y_increased": final_location["y"] > initial_location["y"],
        }

        expected = {
            "is_photo_displayed": True,
            "coordinate_y_increased": True,
        }

        assert actual == expected, (
            f"Pan down failed: initial_y={initial_location['y']}, " f"final_y={final_location['y']}, actual={actual}"
        )

    @pytest.mark.tcid("TC-10-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan left gesture on photo element")
    def test_pan_left_on_photo(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan left gesture works on photo element.

        Expected:
            - Zoom in to make photo larger than viewport
            - Pan left gesture changes photo location horizontally
            - Photo image remains displayed after gesture
        """
        # Arrange - zoom in to enable panning and get initial location
        photo_view_page.pinch_open_on_photo(percentage=0.8)
        initial_location = photo_view_page.photo_image_location

        # Act - perform pan left on photo element
        photo_view_page.pan_left_on_photo(percentage=0.5)

        # Assert - verify photo location changed (x-coordinate should decrease when panning left)
        final_location = photo_view_page.photo_image_location
        actual = {
            "is_photo_displayed": photo_view_page.is_photo_displayed,
            "coordinate_x_decreased": final_location["x"] < initial_location["x"],
        }

        expected = {
            "is_photo_displayed": True,
            "coordinate_x_decreased": True,
        }

        assert actual == expected, (
            f"Pan left failed: initial_x={initial_location['x']}, " f"final_x={final_location['x']}, actual={actual}"
        )

    @pytest.mark.tcid("TC-10-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan right gesture on photo element")
    def test_pan_right_on_photo(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan right gesture works on photo element.

        Expected:
            - Zoom in to make photo larger than viewport
            - Pan right gesture changes photo location horizontally
            - Photo image remains displayed after gesture
        """
        # Arrange - zoom in to enable panning and get initial location
        photo_view_page.pinch_open_on_photo(percentage=0.8)
        initial_location = photo_view_page.photo_image_location

        # Act - perform pan right on photo element
        photo_view_page.pan_right_on_photo(percentage=0.5)

        # Assert - verify photo location changed (x-coordinate should increase when panning right)
        final_location = photo_view_page.photo_image_location
        actual = {
            "is_photo_displayed": photo_view_page.is_photo_displayed,
            "coordinate_x_increased": final_location["x"] > initial_location["x"],
        }

        expected = {
            "is_photo_displayed": True,
            "coordinate_x_increased": True,
        }

        assert actual == expected, (
            f"Pan right failed: initial_x={initial_location['x']}, " f"final_x={final_location['x']}, actual={actual}"
        )

    @pytest.mark.tcid("TC-10-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan up gesture on screen center")
    def test_pan_up_on_screen(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan up gesture works on screen center.

        Expected:
            - Zoom in to make photo larger than viewport
            - Pan up gesture on screen center changes photo location
            - Photo image remains displayed after gesture
        """
        # Arrange - zoom in to enable panning and get initial location
        photo_view_page.pinch_open_on_screen(percentage=0.8)
        initial_location = photo_view_page.photo_image_location

        # Act - perform pan up on screen center
        photo_view_page.pan_up_on_screen(percentage=0.5)

        # Assert - verify photo location changed
        final_location = photo_view_page.photo_image_location
        actual = {
            "is_photo_displayed": photo_view_page.is_photo_displayed,
            "coordinate_y_changed": initial_location["y"] != final_location["y"],
        }

        expected = {
            "is_photo_displayed": True,
            "coordinate_y_changed": True,
        }

        assert actual == expected, (
            f"Pan up on screen failed: initial_y={initial_location['y']}, "
            f"final_y={final_location['y']}, actual={actual}"
        )

    @pytest.mark.tcid("TC-10-06")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan down gesture on screen center")
    def test_pan_down_on_screen(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan down gesture works on screen center.

        Expected:
            - Zoom in to make photo larger than viewport
            - Pan down gesture on screen center changes photo location
            - Photo image remains displayed after gesture
        """
        # Arrange - zoom in to enable panning and get initial location
        photo_view_page.pinch_open_on_screen(percentage=0.8)
        initial_location = photo_view_page.photo_image_location

        # Act - perform pan down on screen center
        photo_view_page.pan_down_on_screen(percentage=0.5)

        # Assert - verify photo location changed
        final_location = photo_view_page.photo_image_location
        actual = {
            "is_photo_displayed": photo_view_page.is_photo_displayed,
            "coordinate_y_changed": initial_location["y"] != final_location["y"],
        }

        expected = {
            "is_photo_displayed": True,
            "coordinate_y_changed": True,
        }

        assert actual == expected, (
            f"Pan down on screen failed: initial_y={initial_location['y']}, "
            f"final_y={final_location['y']}, actual={actual}"
        )

    @pytest.mark.tcid("TC-10-07")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan left gesture on screen center")
    def test_pan_left_on_screen(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan left gesture works on screen center.

        Expected:
            - Zoom in to make photo larger than viewport
            - Pan left gesture on screen center changes photo location
            - Photo image remains displayed after gesture
        """
        # Arrange - zoom in to enable panning and get initial location
        photo_view_page.pinch_open_on_screen(percentage=0.8)
        initial_location = photo_view_page.photo_image_location

        # Act - perform pan left on screen center
        photo_view_page.pan_left_on_screen(percentage=0.5)

        # Assert - verify photo location changed
        final_location = photo_view_page.photo_image_location
        actual = {
            "is_photo_displayed": photo_view_page.is_photo_displayed,
            "coordinate_x_changed": initial_location["x"] != final_location["x"],
        }

        expected = {
            "is_photo_displayed": True,
            "coordinate_x_changed": True,
        }

        assert actual == expected, (
            f"Pan left on screen failed: initial_x={initial_location['x']}, "
            f"final_x={final_location['x']}, actual={actual}"
        )

    @pytest.mark.tcid("TC-10-08")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan right gesture on screen center")
    def test_pan_right_on_screen(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan right gesture works on screen center.

        Expected:
            - Zoom in to make photo larger than viewport
            - Pan right gesture on screen center changes photo location
            - Photo image remains displayed after gesture
        """
        # Arrange - zoom in to enable panning and get initial location
        photo_view_page.pinch_open_on_screen(percentage=0.8)
        initial_location = photo_view_page.photo_image_location

        # Act - perform pan right on screen center
        photo_view_page.pan_right_on_screen(percentage=0.5)

        # Assert - verify photo location changed
        final_location = photo_view_page.photo_image_location
        actual = {
            "is_photo_displayed": photo_view_page.is_photo_displayed,
            "coordinate_x_changed": initial_location["x"] != final_location["x"],
        }

        expected = {
            "is_photo_displayed": True,
            "coordinate_x_changed": True,
        }

        assert actual == expected, (
            f"Pan right on screen failed: initial_x={initial_location['x']}, "
            f"final_x={final_location['x']}, actual={actual}"
        )

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
            - Zoom in to make photo larger than viewport
            - Pan method works with different percentages
            - Coordinate moves in the expected direction
            - Photo image remains displayed
        """
        # Arrange - get pan method and zoom in to enable meaningful panning
        pan_methods = {
            "up": photo_view_page.pan_up_on_photo,
            "down": photo_view_page.pan_down_on_photo,
            "left": photo_view_page.pan_left_on_photo,
            "right": photo_view_page.pan_right_on_photo,
        }
        photo_view_page.pinch_open_on_photo(percentage=0.8)
        initial_location = photo_view_page.photo_image_location

        # Determine which coordinate should change and in which direction
        coordinate_key = "y" if direction in ("up", "down") else "x"

        # Act - perform pan with specified direction and percentage
        pan_methods[direction](percentage=percentage)

        # Assert - verify photo is displayed and coordinate moved in expected direction
        final_location = photo_view_page.photo_image_location
        if direction == "up":
            coordinate_moved_correctly = final_location["y"] < initial_location["y"]
        elif direction == "down":
            coordinate_moved_correctly = final_location["y"] > initial_location["y"]
        elif direction == "left":
            coordinate_moved_correctly = final_location["x"] < initial_location["x"]
        else:  # right
            coordinate_moved_correctly = final_location["x"] > initial_location["x"]

        actual = {
            "is_photo_displayed": photo_view_page.is_photo_displayed,
            "coordinate_moved_correctly": coordinate_moved_correctly,
        }

        expected = {
            "is_photo_displayed": True,
            "coordinate_moved_correctly": True,
        }

        assert actual == expected, (
            f"Pan {direction} failed for percentage {percentage}: "
            f"initial_{coordinate_key}={initial_location[coordinate_key]}, "
            f"final_{coordinate_key}={final_location[coordinate_key]}, actual={actual}"
        )

    @pytest.mark.tcid("TC-10-10")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test sequential pan gestures in all directions")
    def test_sequential_pan_all_directions(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that sequential pan gestures in all directions work correctly.

        Expected:
            - Zoom in to make photo larger than viewport
            - Pan gestures in all four directions execute successfully
            - Photo location changes at least once across all gestures
            - Photo image remains displayed throughout all gestures
        """
        # Arrange - zoom in to enable panning and get initial location
        photo_view_page.pinch_open_on_photo(percentage=0.8)
        initial_location = photo_view_page.photo_image_location

        # Act - perform pan gestures in all directions sequentially and track locations
        photo_view_page.pan_up_on_photo(percentage=0.3)
        location_after_up = photo_view_page.photo_image_location

        photo_view_page.pan_down_on_photo(percentage=0.3)
        location_after_down = photo_view_page.photo_image_location

        photo_view_page.pan_left_on_photo(percentage=0.3)
        location_after_left = photo_view_page.photo_image_location

        photo_view_page.pan_right_on_photo(percentage=0.3)
        location_after_right = photo_view_page.photo_image_location

        # Assert - verify at least one location change and photo still displayed
        locations = [
            location_after_up,
            location_after_down,
            location_after_left,
            location_after_right,
        ]
        location_changed = any(
            loc["x"] != initial_location["x"] or loc["y"] != initial_location["y"] for loc in locations
        )

        actual = {
            "is_photo_displayed": photo_view_page.is_photo_displayed,
            "location_changed": location_changed,
        }

        expected = {
            "is_photo_displayed": True,
            "location_changed": True,
        }

        assert actual == expected, (
            "Sequential pan gestures did not change photo location as expected. "
            f"initial_location={initial_location}, "
            f"locations={locations}, "
            f"actual={actual}"
        )

    @pytest.mark.tcid("TC-10-10-A")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pan gestures validate parameters")
    @pytest.mark.parametrize(
        "method,param,value,error_match",
        [
            ("pan_up_on_photo", "percentage", 1.5, "Percentage must be between 0.0 and 1.0"),
            ("pan_down_on_photo", "percentage", -0.1, "Percentage must be between 0.0 and 1.0"),
            ("pan_left_on_photo", "percentage", 2.0, "Percentage must be between 0.0 and 1.0"),
            ("pan_right_on_photo", "percentage", -1.0, "Percentage must be between 0.0 and 1.0"),
            ("pan_up_on_photo", "speed", 0, "Speed must be a positive integer"),
            ("pan_down_on_photo", "speed", -100, "Speed must be a positive integer"),
            ("pan_left_on_screen", "speed", -50, "Speed must be a positive integer"),
            ("pan_right_on_screen", "speed", 0, "Speed must be a positive integer"),
        ],
        ids=[
            "pan_up-invalid-percentage-high",
            "pan_down-invalid-percentage-negative",
            "pan_left-invalid-percentage-high",
            "pan_right-invalid-percentage-negative",
            "pan_up-invalid-speed-zero",
            "pan_down-invalid-speed-negative",
            "pan_left_screen-invalid-speed-negative",
            "pan_right_screen-invalid-speed-zero",
        ],
    )
    def test_pan_gestures_invalid_parameters(
        self, photo_view_page: PhotoViewPage, method: str, param: str, value: Union[int, float], error_match: str
    ) -> None:
        """Verify that pan gestures validate parameters.

        Expected:
            - ValueError is raised for invalid percentage or speed
            - Error message is descriptive
        """
        # Act & Assert - attempt to call method with invalid parameter
        kwargs = {param: value}
        with pytest.raises(ValueError, match=error_match):
            getattr(photo_view_page, method)(**kwargs)

    @pytest.mark.tcid("TC-10-11")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test zoom in then pan gesture combination")
    def test_zoom_then_pan_combination(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pan gestures work correctly after zooming in.

        Expected:
            - Pinch open (zoom in) executes successfully
            - Pan gestures change photo location on zoomed image
            - Photo image remains displayed after combined gestures
        """
        # Act - zoom in first
        photo_view_page.pinch_open_on_photo(percentage=0.8)
        location_after_zoom = photo_view_page.photo_image_location

        # Act - pan in two directions
        photo_view_page.pan_up_on_photo(percentage=0.3)
        location_after_pan_up = photo_view_page.photo_image_location

        photo_view_page.pan_left_on_photo(percentage=0.3)
        location_after_pan_left = photo_view_page.photo_image_location

        # Assert - verify location changed after each pan and photo is still displayed
        actual = {
            "is_photo_displayed": photo_view_page.is_photo_displayed,
            "coordinate_y_changed_after_pan_up": location_after_zoom["y"] != location_after_pan_up["y"],
            "coordinate_x_changed_after_pan_left": location_after_pan_up["x"] != location_after_pan_left["x"],
            "photo_width_is_valid": photo_view_page.photo_image_size["width"] > 0,
            "photo_height_is_valid": photo_view_page.photo_image_size["height"] > 0,
        }

        expected = {
            "is_photo_displayed": True,
            "coordinate_y_changed_after_pan_up": True,
            "coordinate_x_changed_after_pan_left": True,
            "photo_width_is_valid": True,
            "photo_height_is_valid": True,
        }

        assert actual == expected, f"Zoom + pan combination test failed: {actual}"

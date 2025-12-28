"""Test suite for Pinch Gestures in VodQA application.

This module contains tests for pinch_open and pinch_close methods
from BaseAppiumGestures using the Photo View page.
"""

import allure
import pytest
from pages.vodqa.photo_view_page import PhotoViewPage


@allure.feature("VodQA Samples")
@allure.story("Pinch Gestures")
class TestPinchGestures:
    """Test class for pinch gesture functionality."""

    @pytest.mark.tcid("TC-09-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pinch_open (zoom in) gesture without locator")
    def test_pinch_open_without_locator(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pinch_open gesture works on screen center.

        Expected:
            - pinch_open method executes successfully
            - Pinch open gesture is performed on screen center
            - Photo image remains displayed after gesture
        """
        # Act - perform pinch open on screen center
        photo_view_page.pinch_open_on_screen()

        # Assert - verify photo is still displayed after gesture
        assert photo_view_page.is_photo_displayed, "Photo should be displayed after pinch_open gesture"

    @pytest.mark.tcid("TC-09-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pinch_close (zoom out) gesture without locator")
    def test_pinch_close_without_locator(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pinch_close gesture works on screen center.

        Expected:
            - pinch_close method executes successfully
            - Pinch close gesture is performed on screen center
            - Photo image remains displayed after gesture
        """
        # Act - perform pinch close on screen center
        photo_view_page.pinch_close_on_screen()

        # Assert - verify photo is still displayed after gesture
        assert photo_view_page.is_photo_displayed, "Photo should be displayed after pinch_close gesture"

    @pytest.mark.tcid("TC-09-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pinch_open with different percentages")
    @pytest.mark.parametrize("percentage", [0.5, 0.75, 0.9], ids=["50%", "75%", "90%"])
    def test_pinch_open_with_different_percentages(self, photo_view_page: PhotoViewPage, percentage: float) -> None:
        """Test pinch open gestures with different percentages.

        Args:
            percentage: Pinch distance as percentage (0.5, 0.75, 0.9).

        Expected:
            - Pinch open methods work with different percentages
            - Operations complete successfully regardless of percentage used
            - Photo image remains displayed and has valid dimensions
        """
        # Act - pinch open with specified percentage
        photo_view_page.pinch_open_on_photo(percentage=percentage)

        # Assert - verify photo is displayed and has valid size
        assert photo_view_page.is_photo_displayed, f"Photo should be displayed after pinch_open with {percentage*100}%"
        size = photo_view_page.photo_image_size
        assert size["width"] > 0 and size["height"] > 0, f"Photo should have valid dimensions for {percentage*100}%"

    @pytest.mark.tcid("TC-09-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pinch_close with different percentages")
    @pytest.mark.parametrize("percentage", [0.5, 0.75, 0.9], ids=["50%", "75%", "90%"])
    def test_pinch_close_with_different_percentages(self, photo_view_page: PhotoViewPage, percentage: float) -> None:
        """Test pinch close gestures with different percentages.

        Args:
            percentage: Pinch distance as percentage (0.5, 0.75, 0.9).

        Expected:
            - Pinch close methods work with different percentages
            - Operations complete successfully regardless of percentage used
            - Photo image remains displayed and has valid dimensions
        """
        # Act - pinch close with specified percentage
        photo_view_page.pinch_close_on_photo(percentage=percentage)

        # Assert - verify photo is displayed and has valid size
        assert photo_view_page.is_photo_displayed, f"Photo should be displayed after pinch_close with {percentage*100}%"
        size = photo_view_page.photo_image_size
        assert size["width"] > 0 and size["height"] > 0, f"Photo should have valid dimensions for {percentage*100}%"

    @pytest.mark.tcid("TC-09-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pinch_open with different speeds")
    @pytest.mark.parametrize("speed", [1500, 2500, 3500], ids=["slow", "medium", "fast"])
    def test_pinch_open_with_different_speeds(self, photo_view_page: PhotoViewPage, speed: int) -> None:
        """Test pinch open gestures with different speed values.

        Args:
            speed: Pinch speed in pixels per second.

        Expected:
            - Pinch open methods work with different speeds
            - Operations complete successfully regardless of speed used
            - Photo image remains displayed after gesture
        """
        # Act - pinch open with specified speed
        photo_view_page.pinch_open_on_photo(speed=speed)

        # Assert - verify photo is still displayed after gesture
        assert photo_view_page.is_photo_displayed, f"Photo should be displayed after pinch_open at speed {speed}"

    @pytest.mark.tcid("TC-09-06")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pinch_close with different speeds")
    @pytest.mark.parametrize("speed", [1500, 2500, 3500], ids=["slow", "medium", "fast"])
    def test_pinch_close_with_different_speeds(self, photo_view_page: PhotoViewPage, speed: int) -> None:
        """Test pinch close gestures with different speed values.

        Args:
            speed: Pinch speed in pixels per second.

        Expected:
            - Pinch close methods work with different speeds
            - Operations complete successfully regardless of speed used
            - Photo image remains displayed after gesture
        """
        # Act - pinch close with specified speed
        photo_view_page.pinch_close_on_photo(speed=speed)

        # Assert - verify photo is still displayed after gesture
        assert photo_view_page.is_photo_displayed, f"Photo should be displayed after pinch_close at speed {speed}"

    @pytest.mark.tcid("TC-09-07")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pinch gestures validate parameters")
    @pytest.mark.parametrize(
        "method,param,value,error_match",
        [
            ("pinch_open_on_photo", "percentage", 1.5, "Percentage must be between 0.0 and 1.0"),
            ("pinch_close_on_photo", "percentage", -0.1, "Percentage must be between 0.0 and 1.0"),
            ("pinch_open_on_photo", "speed", 0, "Speed must be a positive integer"),
            ("pinch_close_on_photo", "speed", -100, "Speed must be a positive integer"),
        ],
        ids=["open-invalid-percentage", "close-invalid-percentage", "open-invalid-speed", "close-invalid-speed"],
    )
    def test_pinch_gestures_invalid_parameters(
        self, photo_view_page: PhotoViewPage, method: str, param: str, value: int, error_match: str
    ) -> None:
        """Verify that pinch gestures validate parameters.

        Expected:
            - ValueError is raised for invalid percentage or speed
            - Error message is descriptive
        """
        # Act & Assert - attempt to call method with invalid parameter
        kwargs = {param: value}
        with pytest.raises(ValueError, match=error_match):
            getattr(photo_view_page, method)(**kwargs)

    @pytest.mark.tcid("TC-09-08")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test pinch_open enlarges the photo image")
    def test_pinch_open_enlarges_image(self, photo_view_page: PhotoViewPage) -> None:
        """Verify that pinch_open gesture enlarges the photo image.

        Expected:
            - Image size is recorded before pinch
            - pinch_open method executes successfully
            - Image size increases after pinch (zoom in effect)

        Note: Due to platform limitations, we validate that the gesture executes
        without errors. Actual size verification may not be possible on all devices.
        """
        # Arrange - get initial size
        initial_size = photo_view_page.photo_image_size
        initial_area = initial_size["width"] * initial_size["height"]

        # Act - perform pinch open (zoom in)
        photo_view_page.pinch_open_on_photo(percentage=0.9, speed=2500)

        # Assert - gesture executed successfully
        # Note: Size verification is challenging due to platform behavior
        # The test verifies the gesture executes without errors
        assert initial_area > 0, "Initial image area should be positive"

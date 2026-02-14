"""Test suite for Carousel Edge Cases in VodQA application.

This module contains tests for carousel boundary conditions -
verifying behavior when swiping past the first or last item.
"""

import allure
import pytest
from pages.vodqa.carousel_page import CarouselPage


@allure.feature("VodQA Samples")
@allure.story("Carousel Edge Cases")
class TestCarouselEdgeCases:
    """Test class for carousel boundary condition functionality."""

    @pytest.mark.tcid("TC-CAROUSEL-EDGE-01")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swiping left past first item does not change position")
    def test_swipe_left_at_first_item_stays_at_first(self, carousel_page: CarouselPage) -> None:
        """Verify that swiping left when at first item keeps carousel at first position.

        Test scenario:
        1. Navigate to first carousel item (1 / 3) by swiping left multiple times
        2. Attempt to swipe left again (past first item)
        3. Verify carousel remains at first position

        Expected:
            - Carousel ID remains "1 / 3" after attempting to swipe past first item
        """
        # Arrange - ensure we're at the first item
        carousel_page.navigate_to_first_position()
        initial_id = carousel_page.carousel_id

        # Act - attempt to swipe left past first item
        carousel_page.fling_on_carousel_item(direction="left")

        # Assert
        actual = {
            "initial_position": initial_id,
            "final_position": carousel_page.carousel_id,
        }

        expected = {
            "initial_position": "1 / 3",
            "final_position": "1 / 3",
        }

        assert actual == expected, f"Carousel should remain at first position: {actual}"

    @pytest.mark.tcid("TC-CAROUSEL-EDGE-02")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test swiping right past last item does not change position")
    def test_swipe_right_at_last_item_stays_at_last(self, carousel_page: CarouselPage) -> None:
        """Verify that swiping right when at last item keeps carousel at last position.

        Test scenario:
        1. Navigate to last carousel item (3 / 3) by swiping right multiple times
        2. Attempt to swipe right again (past last item)
        3. Verify carousel remains at last position

        Expected:
            - Carousel ID remains "3 / 3" after attempting to swipe past last item
        """
        # Arrange - ensure we're at the last item
        carousel_page.navigate_to_last_position()
        initial_id = carousel_page.carousel_id

        # Act - attempt to swipe right past last item
        carousel_page.fling_on_carousel_item(direction="right")

        # Assert
        actual = {
            "initial_position": initial_id,
            "final_position": carousel_page.carousel_id,
        }

        expected = {
            "initial_position": "3 / 3",
            "final_position": "3 / 3",
        }

        assert actual == expected, f"Carousel should remain at last position: {actual}"

    @pytest.mark.tcid("TC-CAROUSEL-EDGE-03")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling returns False when at first boundary")
    def test_fling_returns_false_at_first_boundary(self, carousel_page: CarouselPage) -> None:
        """Verify that fling_on_carousel_item returns False at first boundary.

        Test scenario:
        1. Navigate to first carousel item (1 / 3)
        2. Attempt to fling left (past first item)
        3. Verify method returns False indicating no more content

        Expected:
            - Method returns False when at first boundary
        """
        # Arrange - navigate to first item
        carousel_page.navigate_to_first_position()

        # Act - attempt to fling left past first item
        can_continue = carousel_page.fling_on_carousel_item(direction="left")

        # Assert
        assert can_continue is False, "fling_on_carousel_item should return False at first boundary"

    @pytest.mark.tcid("TC-CAROUSEL-EDGE-04")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test fling returns False when at last boundary")
    def test_fling_returns_false_at_last_boundary(self, carousel_page: CarouselPage) -> None:
        """Verify that fling_on_carousel_item returns False at last boundary.

        Test scenario:
        1. Navigate to last carousel item (3 / 3)
        2. Attempt to fling right (past last item)
        3. Verify method returns False indicating no more content

        Expected:
            - Method returns False when at last boundary
        """
        # Arrange - navigate to last item
        carousel_page.navigate_to_last_position()

        # Act - attempt to fling right past last item
        can_continue = carousel_page.fling_on_carousel_item(direction="right")

        # Assert
        assert can_continue is False, "fling_on_carousel_item should return False at last boundary"

    @pytest.mark.tcid("TC-CAROUSEL-EDGE-05")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test multiple swipes left at first position remain stable")
    def test_multiple_swipes_left_at_first_position_stays_stable(self, carousel_page: CarouselPage) -> None:
        """Verify that multiple left swipes at first position keep carousel stable.

        Test scenario:
        1. Navigate to first carousel item (1 / 3)
        2. Perform multiple left swipes
        3. Verify carousel always remains at first position

        Expected:
            - Carousel ID remains "1 / 3" after multiple left swipes
        """
        # Arrange - navigate to first item
        carousel_page.navigate_to_first_position()

        # Act - perform multiple left swipes and collect positions
        carousel_page.fling_on_carousel_item(direction="left")
        position_1 = carousel_page.carousel_id
        carousel_page.fling_on_carousel_item(direction="left")
        position_2 = carousel_page.carousel_id
        carousel_page.fling_on_carousel_item(direction="left")
        position_3 = carousel_page.carousel_id

        # Assert
        actual = {
            "all_positions_at_first": position_1 == "1 / 3" and position_2 == "1 / 3" and position_3 == "1 / 3",
            "positions": [position_1, position_2, position_3],
        }

        expected = {
            "all_positions_at_first": True,
            "positions": ["1 / 3", "1 / 3", "1 / 3"],
        }

        assert actual == expected, f"Carousel should remain at first position after multiple swipes: {actual}"

    @pytest.mark.tcid("TC-CAROUSEL-EDGE-06")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test multiple swipes right at last position remain stable")
    def test_multiple_swipes_right_at_last_position_stays_stable(self, carousel_page: CarouselPage) -> None:
        """Verify that multiple right swipes at last position keep carousel stable.

        Test scenario:
        1. Navigate to last carousel item (3 / 3)
        2. Perform multiple right swipes
        3. Verify carousel always remains at last position

        Expected:
            - Carousel ID remains "3 / 3" after multiple right swipes
        """
        # Arrange - navigate to last item
        carousel_page.navigate_to_last_position()

        # Act - perform multiple right swipes and collect positions
        carousel_page.fling_on_carousel_item(direction="right")
        position_1 = carousel_page.carousel_id
        carousel_page.fling_on_carousel_item(direction="right")
        position_2 = carousel_page.carousel_id
        carousel_page.fling_on_carousel_item(direction="right")
        position_3 = carousel_page.carousel_id

        # Assert
        actual = {
            "all_positions_at_last": position_1 == "3 / 3" and position_2 == "3 / 3" and position_3 == "3 / 3",
            "positions": [position_1, position_2, position_3],
        }

        expected = {
            "all_positions_at_last": True,
            "positions": ["3 / 3", "3 / 3", "3 / 3"],
        }

        assert actual == expected, f"Carousel should remain at last position after multiple swipes: {actual}"

    @pytest.mark.tcid("TC-CAROUSEL-EDGE-07")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test full carousel traversal from first to last and back")
    def test_full_carousel_traversal(self, carousel_page: CarouselPage) -> None:
        """Verify complete carousel traversal from first to last and back to first.

        Test scenario:
        1. Navigate to first item
        2. Traverse to last item while collecting positions
        3. Traverse back to first item while collecting positions
        4. Verify all positions were visited correctly

        Expected:
            - All three positions (1/3, 2/3, 3/3) are visited during traversal
        """
        # Arrange - navigate to first item
        carousel_page.navigate_to_first_position()
        start_position = carousel_page.carousel_id

        # Act - traverse forward to last (4 swipes to ensure we reach 3/3 and test boundary)
        carousel_page.fling_on_carousel_item(direction="right")
        position_forward_1 = carousel_page.carousel_id
        carousel_page.fling_on_carousel_item(direction="right")
        position_forward_2 = carousel_page.carousel_id
        carousel_page.fling_on_carousel_item(direction="right")
        position_forward_3 = carousel_page.carousel_id
        carousel_page.fling_on_carousel_item(direction="right")
        position_forward_4 = carousel_page.carousel_id

        # Act - traverse backward to first (4 swipes to ensure we reach 1/3 and test boundary)
        carousel_page.fling_on_carousel_item(direction="left")
        position_backward_1 = carousel_page.carousel_id
        carousel_page.fling_on_carousel_item(direction="left")
        position_backward_2 = carousel_page.carousel_id
        carousel_page.fling_on_carousel_item(direction="left")
        position_backward_3 = carousel_page.carousel_id
        carousel_page.fling_on_carousel_item(direction="left")
        position_backward_4 = carousel_page.carousel_id

        forward_positions = [
            start_position,
            position_forward_1,
            position_forward_2,
            position_forward_3,
            position_forward_4,
        ]
        backward_positions = [
            position_forward_4,
            position_backward_1,
            position_backward_2,
            position_backward_3,
            position_backward_4,
        ]

        # Assert
        actual = {
            "start_position": start_position,
            "forward_visited_all": "1 / 3" in forward_positions
            and "2 / 3" in forward_positions
            and "3 / 3" in forward_positions,
            "backward_visited_all": "1 / 3" in backward_positions
            and "2 / 3" in backward_positions
            and "3 / 3" in backward_positions,
            "ended_at_first": carousel_page.carousel_id == "1 / 3",
        }

        expected = {
            "start_position": "1 / 3",
            "forward_visited_all": True,
            "backward_visited_all": True,
            "ended_at_first": True,
        }

        assert actual == expected, f"Full carousel traversal failed: {actual}"

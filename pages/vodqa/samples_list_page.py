from dataclasses import dataclass, field
from typing import Tuple
import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_appium_gestures import BaseAppiumGestures
from pages.vodqa.header_bar_component import HeaderBarComponent


@dataclass(frozen=True)
class SamplesListLocators:
    PAGE_HEADER: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='Samples List']"), init=False
    )
    NATIVE_VIEW: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "chainedView"), init=False)
    SLIDER: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "slider1"), init=False)
    VERTICAL_SWIPING: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "verticalSwipe"), init=False)
    DRAG_AND_DROP: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "dragAndDrop"), init=False)
    DOUBLE_TAP: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "doubleTap"), init=False)
    LONG_PRESS: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "longPress"), init=False)
    PHOTO_VIEW: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "photoView"), init=False)
    WEB_VIEW: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "webView"), init=False)
    CAROUSEL: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "carousel"), init=False)
    WHEEL_PICKER: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "wheelPicker"), init=False)


class SamplesListPage(BaseAppiumGestures, HeaderBarComponent):
    """Page object for the Samples List screen, the main navigation hub to sample features.
    This page provides entry points to various sample flows such as sliders, vertical swiping,
    drag and drop, double tap, long press, and other interactive examples within the app.
    """

    @allure.step("the user waits until the samples list page is displayed")
    def wait_until_page_is_loaded(self) -> None:
        """Waits until the Samples List page is fully loaded."""
        self.wait_until_component_is_loaded(title="Samples List")

    @allure.step("the user taps on the 'Slider' sample")
    def tap_slider(self) -> None:
        """Taps on the 'Slider' sample in the samples list."""
        self.tap_element(SamplesListLocators.SLIDER)

    @allure.step("the user taps on the 'Vertical Swiping' sample")
    def tap_vertical_swiping(self) -> None:
        """Taps on the 'Vertical Swiping' sample in the samples list."""
        self.tap_element(SamplesListLocators.VERTICAL_SWIPING)

    @allure.step("the user taps on the 'Drag and Drop' sample")
    def tap_drag_and_drop(self) -> None:
        """Taps on the 'Drag and Drop' sample in the samples list."""
        self.tap_element(SamplesListLocators.DRAG_AND_DROP)

    @allure.step("the user taps on the 'Double Tap' sample")
    def tap_double_tap(self) -> None:
        """Taps on the 'Double Tap' sample in the samples list."""
        self.tap_element(SamplesListLocators.DOUBLE_TAP)

    @allure.step("the user taps on the 'Long Press' sample")
    def tap_long_press(self) -> None:
        """Taps on the 'Long Press' sample in the samples list."""
        self.tap_element(SamplesListLocators.LONG_PRESS)

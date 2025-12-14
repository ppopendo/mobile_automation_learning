from dataclasses import dataclass, field
from typing import Tuple, Any

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
    VERTICAL_SWIPING: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "verticalSwiping"), init=False)
    DRAG_AND_DROP: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "dragAndDrop"), init=False)
    DOUBLE_TAP: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "doubleTap"), init=False)
    LONG_PRESS: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "longPress"), init=False)
    PHOTO_VIEW: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "photoView"), init=False)
    WEB_VIEW: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "webView"), init=False)
    CAROUSEL: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "carousel"), init=False)
    WHEEL_PICKER: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "wheelPicker"), init=False)


class SamplesListPage(BaseAppiumGestures, HeaderBarComponent):

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

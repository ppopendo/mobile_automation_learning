from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.vodqa.header_bar_component import HeaderBarComponent


@dataclass(frozen=True)
class WheelPickerDemoLocators:
    CURRENT_COLOR_TEXT: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//*[contains(@text,' Current Color: ') ]"), init=False
    )
    CURRENT_COLOR_BOX: Tuple[str, str] = field(
        default=(
            AppiumBy.XPATH,
            "//android.widget.FrameLayout[@resource-id='android:id/content']"
            "/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]"
            "/android.view.ViewGroup/android.view.ViewGroup",
        ),
        init=False,
    )
    COLOR_DROPDOWN: Tuple[str, str] = field(default=(AppiumBy.ID, "android:id/text1"), init=False)


class WheelPickerDemoPage(HeaderBarComponent):
    def wait_until_page_is_loaded(self) -> None:
        self.wait_until_component_is_loaded(title="Wheel Picker Demo")

    @property
    @allure.step("retrieving current color text")
    def current_color_text(self) -> str:
        return self.get_element_text(WheelPickerDemoLocators.CURRENT_COLOR_TEXT)

    @property
    @allure.step("retrieving current color box background color")
    def current_color_box(self) -> str:
        return self.wait_for_element(WheelPickerDemoLocators.CURRENT_COLOR_BOX).get_attribute("backgroundColor")

    @property
    @allure.step("retrieving color dropdown value")
    def color_dropdown_value(self) -> str:
        return self.get_element_text(WheelPickerDemoLocators.COLOR_DROPDOWN)

from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.vodqa.header_bar_component import HeaderBarComponent


@dataclass(frozen=True)
class NativeViewDemoLocators:
    CONTAINER_TEXT_1: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "container1"), init=False)
    CONTAINER_TEXT_2: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "container2"), init=False)
    CONTAINER_TEXT_3: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "container3"), init=False)


class NativeViewDemoPage(HeaderBarComponent):

    def wait_until_page_is_loaded(self) -> None:
        self.wait_until_component_is_loaded(title="Native View Demo")

    @property
    @allure.step("retrieving container text 1")
    def container_text_1(self) -> str:
        return self.get_element_text(NativeViewDemoLocators.CONTAINER_TEXT_1)

    @property
    @allure.step("retrieving container text 2")
    def container_text_2(self) -> str:
        return self.get_element_text(NativeViewDemoLocators.CONTAINER_TEXT_2)

    @property
    @allure.step("retrieving container text 3")
    def container_text_3(self) -> str:
        return self.get_element_text(NativeViewDemoLocators.CONTAINER_TEXT_3)

from dataclasses import field, dataclass
from typing import Tuple
import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


@dataclass
class HeaderBarComponentLocators:
    BACK_BUTTON: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@text='Back']"), init=False
    )
    TITLE: Tuple[str, str] = field(default=(AppiumBy.XPATH, "//android.widget.TextView[@text='{title}']"), init=False)


class HeaderBarComponent(BasePage):

    @allure.step("the user waits until the header bar component is loaded with title '{title}'")
    def wait_until_component_is_loaded(self, title: str, timeout=10) -> None:
        title_locator = (
            HeaderBarComponentLocators.TITLE[0],
            HeaderBarComponentLocators.TITLE[1].format(title=title),
        )
        self.wait_for_all_elements([HeaderBarComponentLocators.BACK_BUTTON, title_locator], timeout=timeout)

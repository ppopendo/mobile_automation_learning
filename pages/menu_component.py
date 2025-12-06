from dataclasses import dataclass, field
from typing import Tuple

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


@dataclass(frozen=True)
class MenuComponentLocators:
    """
    contains all static locators for the menu components.
    """

    LOGIN_OPTION: Tuple[str, str] = field(default=(AppiumBy.ACCESSIBILITY_ID, "Login Menu Item"), init=False)
    LOGOUT_OPTION: Tuple[str, str] = field(
        default=(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='Logout Menu Item']"), init=False
    )
    LOGOUT_POPUP_YES_BUTTON: Tuple[str, str] = field(default=(AppiumBy.ID, "android:id/button1"), init=False)
    LOGOUT_POPUP_NO_BUTTON: Tuple[str, str] = field(default=(AppiumBy.ID, "android:id/button2"), init=False)
    CATALOG_OPTION: Tuple[str, str] = field(
        default=(
            AppiumBy.XPATH,
            (
                "//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/itemTV' "
                "and @text='Catalog']"
            ),
        ),
        init=False,
    )
    WEBVIEW_OPTION: Tuple[str, str] = field(
        default=(
            AppiumBy.XPATH,
            (
                "//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/itemTV' "
                "and @text='WebView']"
            ),
        ),
        init=False,
    )
    ABOUT_OPTION: Tuple[str, str] = field(
        default=(
            AppiumBy.XPATH,
            (
                "//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/itemTV' "
                "and @text='About']"
            ),
        ),
        init=False,
    )
    CRASH_APP_OPTION: Tuple[str, str] = field(
        default=(
            AppiumBy.XPATH,
            (
                "//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/itemTV' "
                "and @text='Crash app (debug)']"
            ),
        ),
        init=False,
    )


class MenuComponent(BasePage):

    @allure.step("waiting for the menu page to be fully loaded")
    def wait_until_page_is_loaded(self, timeout: int = 10) -> None:
        """Wait until the menu page is fully loaded."""
        expected_locators = [
            MenuComponentLocators.CATALOG_OPTION,
            MenuComponentLocators.WEBVIEW_OPTION,
            MenuComponentLocators.ABOUT_OPTION,
            MenuComponentLocators.CRASH_APP_OPTION,
        ]
        for locator in expected_locators:
            self.wait_for_element(locator, condition=EC.presence_of_element_located, timeout=timeout)

    @allure.step("the user clicks on the login option in the menu")
    def click_login_button(self) -> None:
        self.tap_element(MenuComponentLocators.LOGIN_OPTION)

    @allure.step("the user clicks on the logout option in the menu")
    def click_logout(self) -> None:
        """Click on the logout button in the menu."""
        self.tap_element(MenuComponentLocators.LOGOUT_OPTION)

    @allure.step("the user confirms the logout action")
    def confirm_logout(self) -> None:
        self.tap_element(MenuComponentLocators.LOGOUT_POPUP_YES_BUTTON)

    @allure.step("checking if the logout option is displayed in the menu")
    def is_logout_option_displayed(self) -> bool:
        """Check if logout option is visible (user is logged in).

        Uses short timeout (2s) since this is just a quick check.
        """
        return self.is_element_displayed(MenuComponentLocators.LOGOUT_OPTION, timeout=2)

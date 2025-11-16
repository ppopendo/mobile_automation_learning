from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MenuPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._locators = {
            "login_option": (AppiumBy.ACCESSIBILITY_ID, "Login Menu Item"),
            "logout_option": (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='Logout Menu Item']"),
            "logout_popup_yes_button": (AppiumBy.ID, "android:id/button1"),
            "logout_popup_no_button": (AppiumBy.ID, "android:id/button2"),
            "title": (
                AppiumBy.XPATH,
                (
                    "//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/itemTV' "
                    "and @text='Catalog']"
                ),
            ),
            "webview_option": (
                AppiumBy.XPATH,
                (
                    "//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/itemTV' "
                    "and @text='WebView']"
                ),
            ),
            "about_option": (
                AppiumBy.XPATH,
                (
                    "//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/itemTV' "
                    "and @text='About']"
                ),
            ),
            "crash_app_option": (
                AppiumBy.XPATH,
                (
                    "//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/itemTV' "
                    "and @text='Crash app (debug)']"
                ),
            ),
        }

    def wait_until_page_is_loaded(self, timeout: int = 10) -> None:
        """Wait until the menu page is fully loaded."""
        expected_locators = [
            self._locators["title"],
            self._locators["webview_option"],
            self._locators["about_option"],
            self._locators["crash_app_option"],
        ]
        for locator in expected_locators:
            self.wait_for_element(locator, condition=EC.presence_of_element_located, timeout=timeout)

    def click_login_button(self) -> None:
        """Click on the login button in the menu."""
        self.wait_and_click(self._locators["login_option"])

    def click_logout(self) -> None:
        """Click on the logout button in the menu."""
        self.wait_and_click(self._locators["logout_option"])

    def confirm_logout(self) -> None:
        """Confirm logout by clicking the yes button on the popup."""
        self.wait_and_click(self._locators["logout_popup_yes_button"])

    def is_logout_option_displayed(self) -> bool:
        """Check if the logout option is displayed in the menu."""
        return self.is_element_displayed(self._locators["logout_option"])

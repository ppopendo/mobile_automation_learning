from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, driver: RemoteWebDriver):
        super().__init__(driver)
        self._products_title = (
            AppiumBy.ID,
            "com.saucelabs.mydemoapp.android:id/productTV",
        )
        self._menu_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/menuIV")

    def wait_until_page_is_loaded(self, timeout=10) -> None:
        expected_locators = [self._products_title, self._menu_button]
        for locator in expected_locators:
            self.wait_for_element(locator, condition=EC.presence_of_element_located, timeout=timeout)

    def is_menu_button_displayed(self) -> bool:
        return self._driver.find_element(*self._menu_button).is_displayed()

    def click_menu_button(self):
        self._driver.find_element(*self._menu_button).click()

    def is_products_title_displayed(self) -> bool:
        return self._driver.find_element(*self._products_title).is_displayed()

    def open_side_menu(self):
        """Try clicking the menu button with retries and raise an exception on failure."""
        attempts = 3
        last_exc = None
        for attempt in range(attempts):
            try:
                element = WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable(self._menu_button))
                element.click()
                return
            except StaleElementReferenceException as exc:
                last_exc = exc
                if attempt < attempts - 1:
                    continue
                raise StaleElementReferenceException(
                    "Menu button element no longer appears on the DOM of the page after multiple attempts."
                ) from exc
            except Exception as exception:
                last_exc = exception
                if attempt < attempts - 1:
                    continue
                raise RuntimeError(f"Could not click menu button due to exception: {exception}") from exception
        if last_exc:
            raise last_exc

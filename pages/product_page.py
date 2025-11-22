from dataclasses import dataclass, field
from typing import Tuple
import allure
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


@dataclass(frozen=True)
class ProductsPageLocators:
    """
    contains all static locators for the products page.
    """
    PRODUCTS_HEADER: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV"),
        init=False
    )
    SHOPPING_CART_ICON: Tuple[str, str] = field(
        default=(AppiumBy.ACCESSIBILITY_ID, "test-Mixture"),
        init=False
    )
    MENU_BUTTON: Tuple[str, str] = field(default= (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/menuIV"),init=False)

    @staticmethod
    def add_to_cart_button_pattern(product_name: str) -> Tuple[str, str]:
        """
        generates a dynamic locator for the "Add to Cart" button of a specific product.
        """
        return (AppiumBy.XPATH,
                f"//android.widget.TextView[@text='{product_name}']/following-sibling::android.view.ViewGroup[@content-desc='test-Add To Cart']")


class ProductsPage(BasePage):

    def __init__(self, driver: 'WebDriver'):
        super().__init__(driver)

    @allure.step("Verifying if 'Products' header is displayed")
    def is_products_header_displayed(self) -> bool:
        """Checks if the 'Products' header is visible on the Products Page."""
        try:
            self.wait_for_element(ProductsPageLocators.PRODUCTS_HEADER)
            return True
        except:
            allure.attach(
                "Header 'Products' is not displayed.",
                name="Header Verification",
                attachment_type=allure.attachment_type.TEXT,
            )
            return False

    @allure.step("the user adds '{product_name}' to the shopping cart")
    def add_product_to_cart(self, product_name: str) -> None:
        """adds a specified product to the shopping cart by clicking its 'Add to Cart' button."""

        # 1. generate dynamic locator for the product
        locator = ProductsPageLocators.add_to_cart_button_pattern(product_name=product_name)

        # 2. click the "Add to Cart" button
        self.wait_and_click(locator)

        allure.attach(f"Product '{product_name}' has been added to the cart.", name="Add Product to Cart",attachment_type=allure.attachment_type.TEXT,)

    @allure.step("the user opens the shopping cart")
    def open_shopping_cart(self) -> None:
        """clicks on the shopping cart icon to open the cart page."""
        self.wait_and_click(ProductsPageLocators.SHOPPING_CART_ICON)

    def wait_until_page_is_loaded(self, timeout=10) -> None:
        expected_locators = [ProductsPageLocators.PRODUCTS_HEADER, ProductsPageLocators.MENU_BUTTON]
        for locator in expected_locators:
            self.wait_for_element(locator, condition=EC.presence_of_element_located, timeout=timeout)

    def is_menu_button_displayed(self) -> bool:
        return self._driver.find_element(*ProductsPageLocators.MENU_BUTTON).is_displayed()

    def click_menu_button(self):
        self._driver.find_element(*ProductsPageLocators.MENU_BUTTON).click()

    @allure.step("Checking if 'Products' title is displayed")
    def is_products_title_displayed(self) -> bool:
        return self._driver.find_element(*ProductsPageLocators.PRODUCTS_HEADER).is_displayed()

    def open_side_menu(self):
        """Try clicking the menu button with retries and raise an exception on failure."""
        attempts = 3
        last_exc = None
        for attempt in range(attempts):
            try:
                element = WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable(ProductsPageLocators.MENU_BUTTON))
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
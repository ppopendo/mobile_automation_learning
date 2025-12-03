from dataclasses import dataclass, field
from typing import Tuple
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


@dataclass(frozen=True)
class ProductsPageLocators:
	"""
	contains all static locators for the products page.
	"""
	PRODUCT_NAME_XPATH_PATTERN: str = "//android.widget.TextView[@content-desc='Product Title' and @text='{product_name}']"
	PRODUCTS_HEADER: Tuple[str, str] = field(
		default=(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV"),
		init=False
	)
	MENU_BUTTON: Tuple[str, str] = field(default= (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/menuIV"),init=False)
	PRODUCT_NAME: Tuple[str, str] = field(
		default=(AppiumBy.XPATH , PRODUCT_NAME_XPATH_PATTERN),
		init=False
	)
	PRODUCT_IMAGE: Tuple[str, str] = field(
		default=(AppiumBy.XPATH,PRODUCT_NAME_XPATH_PATTERN + "/preceding-sibling::*[@content-desc='Product Image']"),
		init=False
	)
	PRODUCT_PRICE: Tuple[str, str] = field(
		default=(AppiumBy.XPATH,PRODUCT_NAME_XPATH_PATTERN + "/following-sibling::*[@content-desc='Product Price']"),
		init=False
	)


class ProductsPage(BasePage):

	@allure.step("the user waits until the products page is displayed")
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

	@allure.step("the user opens the product details for '{product_name}'")
	def open_product_details(self, product_name: str) -> None:
		"""Opens the details page for a specific product by tapping on its image."""
		product_locator = (ProductsPageLocators.PRODUCT_IMAGE[0],
						   ProductsPageLocators.PRODUCT_IMAGE[1].format(product_name=product_name))
		self.tap_element(product_locator)

	@allure.step("waiting for the products page to be fully loaded")
	def wait_until_page_is_loaded(self, timeout=10) -> None:
		expected_locators = [ProductsPageLocators.PRODUCTS_HEADER, ProductsPageLocators.MENU_BUTTON]
		for locator in expected_locators:
			self.wait_for_element(locator, condition=EC.presence_of_element_located, timeout=timeout)

	@allure.step("checking if the menu button is displayed")
	def is_menu_button_displayed(self) -> bool:
		return self._driver.find_element(*ProductsPageLocators.MENU_BUTTON).is_displayed()

	@allure.step("the user clicks the menu button")
	def click_menu_button(self):
		self.tap_element(*ProductsPageLocators.MENU_BUTTON)

	@allure.step("Checking if 'Products' title is displayed")
	def is_products_title_displayed(self) -> bool:
		return self._driver.find_element(*ProductsPageLocators.PRODUCTS_HEADER).is_displayed()

	@allure.step("the user opens the side menu")
	def open_side_menu(self):
		self.tap_element(ProductsPageLocators.MENU_BUTTON)

	@allure.step("retrieving the price for product: {product_name}")
	def get_product_price(self, product_name: str) -> str:
		"""Retrieves the price of a specific product by its name."""
		price_locator = (ProductsPageLocators.PRODUCT_PRICE[0],
						 ProductsPageLocators.PRODUCT_PRICE[1].format(product_name=product_name))
		price_element = self.wait_for_element(price_locator, condition=EC.visibility_of_element_located)
		return price_element.text

	@allure.step("waiting until product '{product_name}' is displayed")
	def wait_until_product_is_displayed(self, product_name: str, timeout: int = 10) -> None:
		"""Waits until the specified product is visible on the Products Page."""
		product_locator = (ProductsPageLocators.PRODUCT_NAME[0],
						   ProductsPageLocators.PRODUCT_NAME[1].format(product_name=product_name))
		price_locator = (ProductsPageLocators.PRODUCT_PRICE[0],
						 ProductsPageLocators.PRODUCT_PRICE[1].format(product_name=product_name))
		image_locator = (ProductsPageLocators.PRODUCT_IMAGE[0],
						 ProductsPageLocators.PRODUCT_IMAGE[1].format(product_name=product_name))
		product_elements = [product_locator, price_locator, image_locator]
		for product_element in product_elements:
			self.wait_for_element(product_element, condition=EC.visibility_of_element_located, timeout=timeout)
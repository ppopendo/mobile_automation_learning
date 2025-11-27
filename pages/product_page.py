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
		self.tap_element(locator)

		allure.attach(f"Product '{product_name}' has been added to the cart.", name="Add Product to Cart",attachment_type=allure.attachment_type.TEXT,)

	@allure.step("the user opens the shopping cart")
	def open_shopping_cart(self) -> None:
		"""clicks on the shopping cart icon to open the cart page."""
		self.tap_element(ProductsPageLocators.SHOPPING_CART_ICON)

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
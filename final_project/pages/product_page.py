from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        link.click()

    def should_match_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        #print(product_name)
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        #print(added_product_name)
        assert product_name == added_product_name, f"Product name does not match, should {product_name}, given {added_product_name}"

    def should_match_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE).text
        assert product_price == basket_price, f"Product cost does not match, should {product_price}, given {basket_price}"


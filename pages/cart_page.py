import time

import allure

from locators.cart_page_locators import CartPageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


class CartPage(BasePage):

    locators = CartPageLocators()
    """Методы для проверки корзины"""
    def check_cart(self):
        with allure.step("check_cart"):
            Logger.add_start_step(method="check_cart")
            item_cart = self.element_is_present(self.locators.ITEM_CART_BUTTON).text
            self.get_current_url()
            self.screen_save()
            self.element_is_present(self.locators.CART_BUTTON).click()
            name_product_1_in_cart = self.element_is_present(self.locators.NAME_PRODUCT_1).text
            price_product_1_in_cart = self.element_is_present(self.locators.PRICE_PRODUCT_1).text
            name_product_2_in_cart = self.element_is_present(self.locators.NAME_PRODUCT_2).text
            price_product_2_in_cart = self.element_is_present(self.locators.PRICE_PRODUCT_2).text
            total_price = self.element_is_present(self.locators.TOTAL_PRICE).text
            print(total_price)
            Logger.add_end_step(url=self.driver.current_url, method="check_cart")
            return name_product_1_in_cart, price_product_1_in_cart, name_product_2_in_cart, price_product_2_in_cart, total_price, item_cart
    """Переход к оплате"""
    def go_to_payment(self):
        with allure.step("go_to_payment"):
            Logger.add_start_step(method="go_to_payment")
            self.element_is_present(self.locators.GO_PAYMENT_BUTTON).click()
            self.get_current_url()
            self.screen_save()
            Logger.add_end_step(url=self.driver.current_url, method="go_to_payment")



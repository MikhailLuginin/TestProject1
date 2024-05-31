import random
import time

from selenium.webdriver import Keys

from locators.product_page_locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):

    locators = ProductPageLocators()
    """Выбор фильтров"""
    def filters(self):
        self.get_current_url()
        self.driver.execute_script("arguments[0].click();", self.element_is_present(self.locators.CATALOG_MENU))
        element_1 = self.element_is_visible(self.locators.ITEM_TOOL)
        self.action_move_to_element(element_1)
        self.element_is_present(self.locators.CATEGORY).click()
        element_2 = self.element_is_present(self.locators.PRICE)
        self.action_click_and_hold(element_2, random.randint(-100, -10))
        price_do = self.element_is_present(self.locators.PRICE_DO).text
        time.sleep(2)
        self.element_is_clickable(self.locators.MATERIAL).click()
        select_material = self.element_is_present(self.locators.SELECT_MATERIAL).text
        time.sleep(2)
        self.action_scroll_to(1200)
        time.sleep(2)
        select_country = self.element_is_present(self.locators.SELECT_COUNTRY).text
        self.element_is_clickable(self.locators.COUNTRY).click()
        return price_do, select_material, select_country
    """Проверка фильтров"""
    def checking_filters(self):
        self.action_scroll_to(0)
        item_price = self.element_is_present(self.locators.ITEM_PRICE).text
        item_material = self.element_is_present(self.locators.ITEM_MATERIAL).text
        item_country = self.element_is_present(self.locators.ITEM_COUNTRY).text
        return item_price, item_material, item_country
    """Добавление первого товара"""
    def add_product_1(self):
        time.sleep(2)
        self.element_is_present(self.locators.BUTTON_ADD_PRODUCT_1_TO_CARD).click()
        time.sleep(2)
        name_product_1 = self.element_is_present(self.locators.NAME_PRODUCT_1).text
        price_product_1 = self.element_is_present(self.locators.PRICE_PRODUCT_1).text
        self.element_is_present(self.locators.QUALITY_PRODUCT_1).click()
        time.sleep(2)
        quality_product_1 = self.element_is_present(self.locators.ITEM_QUALITY_PRODUCT_1).text
        return name_product_1, price_product_1, quality_product_1
    """Добавление второго товара"""
    def add_product_2(self, price_min):
        self.element_is_present(self.locators.CATEGORY_2).click()
        self.element_is_present(self.locators.VIEW_PRODUCT).click()
        price = self.element_is_present(self.locators.PRICE_MIN)
        price.clear()
        price.send_keys(price_min)
        price.send_keys(Keys.RETURN)
        time.sleep(3)
        self.element_is_present(self.locators.BUTTON_ADD_PRODUCT_2_TO_CARD).click()
        time.sleep(2)
        name_product_2 = self.element_is_present(self.locators.NAME_PRODUCT_2).text
        price_product_2 = self.element_is_present(self.locators.PRICE_PRODUCT_2).text
        quality_product_2 = self.element_is_present(self.locators.ITEM_QUALITY_PRODUCT_2).text
        return name_product_2, price_product_2, quality_product_2








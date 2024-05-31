import random
import time

from pages.login_page import LoginPage
from pages.product_page import ProductPage
"""Данные для заполнения"""
login = "lugininm@yandex.ru"
password = "Qwerty123"
price_min_product_2 = random.randint(100, 500)


class TestProductPage:

    def test_filters(self, driver):

        tf = LoginPage(driver, "https://poryadok.ru/")
        tf.open()
        tf.authorization(login, password)
        time.sleep(2)
        tf = ProductPage(driver, driver.current_url)
        price_do, select_material, select_country = tf.filters()
        item_price, item_material, item_country = tf.checking_filters()

        assert price_do[:-2] == item_price[-5:], "Error"
        print(item_price)
        assert select_material == item_material[10:], "Error"
        print(item_material)
        assert select_country == item_country[21:], "Error"
        print(item_country)

        name_product_1, price_product_1, quality_product_1 = tf.add_product_1()
        print(name_product_1)
        print(price_product_1)
        print(quality_product_1)

        name_product_2, price_product_2, quality_product_2 = tf.add_product_2(price_min_product_2)
        print(name_product_2)
        print(price_product_2)
        print(quality_product_2)

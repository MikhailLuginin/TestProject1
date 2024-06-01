import random
import time

import allure

from pages.login_page import LoginPage
from pages.product_page import ProductPage
"""Данные для заполнения"""
login = "lugininm@yandex.ru"
password = "Qwerty123"
price_min_product_2 = random.randint(100, 500)


class TestProductPage:

    @allure.description("Test filters")
    def test_filters(self, driver):

        try:
            tf = LoginPage(driver, "https://poryadok.ru/")
            tf.open()
            tf.authorization(login, password)
            time.sleep(2)
            tf = ProductPage(driver, driver.current_url)
            price_do, select_material, select_country = tf.filters()
            item_price, item_material, item_country = tf.checking_filters()

            assert price_do[:-2] == item_price[-5:], "Фильтр цены не сошелся"
            print(item_price)
            assert select_material == item_material[10:], "Фильтр материала не сошелся"
            print(item_material)
            assert select_country == item_country[21:], "Фидбьтр старны производителя не сошелся"
            print(item_country)

            name_product_1, price_product_1, quality_product_1 = tf.add_product_1()
            print(name_product_1)
            print(price_product_1)
            print(quality_product_1)

            name_product_2, price_product_2, quality_product_2 = tf.add_product_2(price_min_product_2)
            print(name_product_2)
            print(price_product_2)
            print(quality_product_2)
        except Exception as e:
            print(f"Произошла ошибка: {e}")

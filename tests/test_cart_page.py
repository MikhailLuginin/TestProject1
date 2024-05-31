import random
import time

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
"""Данные для заполнения"""
login = "lugininm@yandex.ru"
password = "Qwerty123"
price_min_product_2 = random.randint(100, 500)


class TestCartPage:

    def test_cart_page(self, driver):

        tcp = LoginPage(driver, "https://poryadok.ru/")
        tcp.open()
        tcp.authorization(login, password)
        time.sleep(2)
        tcp = ProductPage(driver, driver.current_url)
        tcp.filters()
        tcp.checking_filters()
        name_product_1, price_product_1, quality_product_1 = tcp.add_product_1()
        name_product_2, price_product_2, quality_product_2 = tcp.add_product_2(price_min_product_2)
        tcp = CartPage(driver, driver.current_url)
        name_product_1_in_cart, price_product_1_in_cart, name_product_2_in_cart, price_product_2_in_cart, total_price, item_cart = tcp.check_cart()
        assert name_product_1 == name_product_1_in_cart, "Error"
        print(name_product_1)
        assert int(price_product_1[:-2])*2 == int(price_product_1_in_cart[:-2]), "Error"
        print(price_product_1)
        assert name_product_2 == name_product_2_in_cart, "Error"
        print(name_product_2)
        assert price_product_2 == price_product_2_in_cart, "Error"
        print(price_product_2)
        tp = int(price_product_1_in_cart[:-2]) + int(price_product_2_in_cart[:-2])
        t = total_price[:-1].replace(" ", "")
        assert int(t) == tp, "Error"
        print(tp)
        tcp.go_to_payment()
        assert item_cart == "2", "Error"
        print(item_cart)


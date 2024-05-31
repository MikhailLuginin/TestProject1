import time

from pages.login_page import LoginPage
"""Данные для заполнения"""
login = "lugininm@yandex.ru"
password = "Qwerty123"
user = "Павел"


class TestLoginPage:

    def test_authorization(self, driver):

        ta = LoginPage(driver, "https://poryadok.ru/")
        ta.open()
        city_confirm = ta.authorization(login, password)
        time.sleep(2)
        user_name = ta.check_authorization()
        assert user == user_name, "Error"
        print(user_name)

        ta.check_city()
        city = ta.check_city()
        assert city == city_confirm[10:-1].upper(), "Error"
        print(city)

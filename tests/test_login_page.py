import time
import allure

from pages.login_page import LoginPage
"""Данные для заполнения"""
login = "lugininm@yandex.ru"
password = "Qwerty123"
user = "Павел"


class TestLoginPage:

    @allure.description("Test authorization")
    def test_authorization(self, driver):
        try:
            ta = LoginPage(driver, "https://poryadok.ru/")
            ta.open()
            city_confirm = ta.authorization(login, password)
            time.sleep(2)
            user_name = ta.check_authorization()
            assert user == user_name, "Не верное имя пользователя"
            print(user_name)

            ta.check_city()
            city = ta.check_city()
            assert city == city_confirm[10:-1].upper(), "Не верный город"
            print(city)
        except Exception as e:
            print(f"Произошла ошибка: {e}")

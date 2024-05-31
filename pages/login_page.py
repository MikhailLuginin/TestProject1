import time

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

"""Метод авторизации"""
class LoginPage(BasePage):

    locators = LoginPageLocators()

    def authorization(self, login, password):
        time.sleep(2)
        city_confirm = self.element_is_present(self.locators.CITY_CONFIRM).text
        self.element_is_present(self.locators.CONFIRM).click()
        time.sleep(2)
        self.get_current_url()
        self.element_is_present(self.locators.LOGIN_BUTTON_IN_MAIN_PAGE).click()
        self.element_is_present(self.locators.LOGIN_INPUT).send_keys(login)
        self.element_is_present(self.locators.PASSWORD_INPUT).send_keys(password)
        self.element_is_present(self.locators.LOGIN_BUTTON).click()
        return city_confirm
    """Метод для проверки авторизации"""
    def check_authorization(self):
        user_name = self.element_is_present(self.locators.USER_NAME).get_attribute("value")
        return user_name
    """Метод для проверки правильности выбора города"""
    def check_city(self):
        city = self.element_is_present(self.locators.CITY).text
        return city




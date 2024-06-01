import time
import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


"""Метод авторизации"""
class LoginPage(BasePage):

    locators = LoginPageLocators()

    def authorization(self, login, password):
        with allure.step("authorization"):
            Logger.add_start_step(method="authorization")
            time.sleep(2)
            city_confirm = self.element_is_present(self.locators.CITY_CONFIRM).text
            self.element_is_present(self.locators.CONFIRM).click()
            time.sleep(2)
            self.get_current_url()
            self.element_is_present(self.locators.LOGIN_BUTTON_IN_MAIN_PAGE).click()
            self.element_is_present(self.locators.LOGIN_INPUT).send_keys(login)
            self.element_is_present(self.locators.PASSWORD_INPUT).send_keys(password)
            self.element_is_present(self.locators.LOGIN_BUTTON).click()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
            return city_confirm
    """Метод для проверки авторизации"""
    def check_authorization(self):
        with allure.step("check_authorization"):
            Logger.add_start_step(method="check_authorization")
            self.screen_save()
            user_name = self.element_is_present(self.locators.USER_NAME).get_attribute("value")
            Logger.add_end_step(url=self.driver.current_url, method="check_authorization")
            return user_name
    """Метод для проверки правильности выбора города"""
    def check_city(self):
        with allure.step("check_city"):
            Logger.add_start_step(method="check_city")
            city = self.element_is_present(self.locators.CITY).text
            Logger.add_end_step(url=self.driver.current_url, method="check_city")
            return city




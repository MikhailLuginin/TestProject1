from selenium.webdriver.common.by import By


class LoginPageLocators:

    CONFIRM = (By.XPATH, '//button[@class="btn btn-success mr-3 ml-3 mb-3"]')
    CITY_CONFIRM = (By.XPATH, '//div[@class="geoip-popup__title"]')
    LOGIN_BUTTON_IN_MAIN_PAGE = (By.XPATH, '(//button[@class="profile js-link"])[2]')
    LOGIN_INPUT = (By.XPATH, '//input[@class="form-control js-authEmail"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@class="form-control js-authPassword"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@class="btn btn-success pull-right js-saveAuthData"]')

    USER_NAME = (By.XPATH, '//input[@value="Павел"]')
    CITY = (By.XPATH, '//span[@data-prk-modal-target="geo_ip"]')





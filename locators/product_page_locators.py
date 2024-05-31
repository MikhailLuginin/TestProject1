from selenium.webdriver.common.by import By


class ProductPageLocators:

    #Filters
    CATALOG_MENU = (By.XPATH, '//span[@class="dropdown__title prk-top-menu__item-title lvl-0"]')
    ITEM_TOOL = (By.XPATH, '//a[text()=" Инструмент "]')
    CATEGORY = (By.XPATH, '//span[text()=" Ключи "]')
    PRICE = (By.XPATH, '(//div[@class="jsr_slider"])[2]')
    MATERIAL = (By.XPATH, '//label[@title="CrV сталь"]')
    SELECT_MATERIAL = (By.XPATH, '//*[@id="wrapper"]/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/div/div/div/div/label[1]/a/span[2]')
    SELECT_COUNTRY = (By.XPATH, '//*[@id="wrapper"]/div[3]/div[2]/div[2]/div[1]/div[2]/div[8]/div[2]/div/div/div/div/label[1]/a/span[2]')
    COUNTRY = (By.XPATH, '//label[@title="Китай"]')
    PRICE_DO = (By.XPATH, '//span[@data-key="1"]')
    ITEM_MATERIAL = (By.XPATH, '//*[@id="wrapper"]/div[3]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[2]')
    ITEM_COUNTRY = (By.XPATH, '//*[@id="wrapper"]/div[3]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[3]')
    ITEM_PRICE = (By.XPATH, '//*[@id="wrapper"]/div[3]/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[1]')

    #Product_1
    BUTTON_ADD_PRODUCT_1_TO_CARD = (By.XPATH, "(//*[contains(@class,'quick-view js-fly-btn')])[1]")
    NAME_PRODUCT_1 = (By.XPATH, '(//span[@itemprop="name"])[4]')
    PRICE_PRODUCT_1 = (By.XPATH, '(//div[@class="product-tile__pricing-price--current"])[1]')
    QUALITY_PRODUCT_1 = (By.XPATH, '//span[@class="cart-quantity__btn js-cart-quantity__btn--increment"]')
    ITEM_QUALITY_PRODUCT_1 = (By.XPATH, '//span[@class="cart-quantity__input"]')

    #Product_2
    BUTTON_ADD_PRODUCT_2_TO_CARD = (By.XPATH, "(//*[contains(@class,'quick-view js-fly-btn')])[1]")
    CATEGORY_2 = (By.XPATH, '(//li[@class="dropdown js-dropdown lvl-1 prk-top-menu__item"])[2]')
    VIEW_PRODUCT = (By.XPATH, '//a[@href="https://nizhniy-novgorod.poryadok.ru/catalog/polotentsa_detskie/"]')
    PRICE_MIN = (By.XPATH, '//input[@name="r_price_min"]')
    NAME_PRODUCT_2 = (By.XPATH, '(//span[@itemprop="name"])[4]')
    PRICE_PRODUCT_2 = (By.XPATH, '(//div[@class="product-tile__pricing-price--current"])[1]')
    ITEM_QUALITY_PRODUCT_2 = (By.XPATH, '//span[@class="cart-quantity__input"]')






from selenium.webdriver.common.by import By


class CartPageLocators:

    CART_BUTTON = (By.XPATH, '//a[@class="badge-btn js-cart-product-image-fly-target"]')
    ITEM_CART_BUTTON = (By.XPATH, '//div[@class="badge-btn__badge js-cart-count"]')
    NAME_PRODUCT_1 = (By.XPATH, '(//a[@class="checkout-cart-product__name"])[1]')
    PRICE_PRODUCT_1 = (By.XPATH, '(//span[@class="checkout-cart-product-pricing__price checkout-cart-product-pricing__price--actual"])[1]')
    NAME_PRODUCT_2 = (By.XPATH, '(//a[@class="checkout-cart-product__name"])[2]')
    PRICE_PRODUCT_2 = (By.XPATH, '(//span[@class="checkout-cart-product-pricing__price checkout-cart-product-pricing__price--actual"])[2]')
    TOTAL_PRICE = (By.XPATH, '//span[@class="bx-soa-cart-d bx-soa-changeCostSign"]')
    GO_PAYMENT_BUTTON = (By.XPATH, '//button[@class="pull-right btn btn-success btn-md"]')
import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    def element_is_visible(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_present(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def action_click_and_hold(self, element, integer):
        action = ActionChains(self.driver)
        action.click_and_hold(element).move_by_offset(integer, 0).release().perform()

    def action_scroll_to(self, integer):
        self.driver.execute_script(f"window.scrollTo(0, {integer})")

    def screen_save(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot ' + now_date + ".png"
        self.driver.save_screenshot('.\\screen\\' + name_screenshot)


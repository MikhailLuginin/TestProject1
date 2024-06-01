import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import shutil, os


@pytest.fixture()
def driver():
    print("Start test")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    shutil.rmtree('.\\screen\\')
    os.mkdir('.\\screen\\')
    driver = webdriver.Chrome(options=options, service=g)
    driver.maximize_window()
    yield driver
    driver.delete_all_cookies()
    driver.quit()
    print("Finish test")


def pytest_collection_modifyitems(items):
    CLASS_ORDER = ["TestMainPage", "TestProductPage", "TestCartPage"]
    class_mapping = {item: item.cls.__name__ for item in items}

    sorted_items = items.copy()
    for class_ in CLASS_ORDER:
        sorted_items = [it for it in sorted_items if class_mapping[it] != class_] + [
            it for it in sorted_items if class_mapping[it] == class_
        ]
    items[:] = sorted_items

import time
import pytest
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture()
def _drivers():
    driver = webdriver.Chrome(options=opts)
    driver.get('https://shoppersstack.com/')
    driver.maximize_window()
    driver.implicitly_wait(80)
    yield driver
    time.sleep(2)
    driver.close()


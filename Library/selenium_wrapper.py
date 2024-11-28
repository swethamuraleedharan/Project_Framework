# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
class SeleniumWrapper:
    def __init__(self,driver):
        self.driver = driver

    def click_on_element(self,logical_name):
        # wait = WebDriverWait(self.driver, 20)
        # locator = self.driver.find_element(*logical_name).click()
        self.driver.find_element(*logical_name).click()
        # element = wait.until(expected_conditions.element_to_be_clickable(locator))
        # element.click()

    def enter_data(self,logical_name,data):
        self.driver.find_element(*logical_name).send_keys(data)

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from POM import shopper_register

def test_register(_drivers):
    reg_obj = shopper_register.Register(_drivers)
    reg_obj.click_on_login()
    reg_obj.click_on_create_acoount()
    reg_obj.enter_fname()
    reg_obj.enter_lname()
    reg_obj.click_on_gender()
    reg_obj.enter_number()
    reg_obj.enter_email()
    reg_obj.enter_paswd()
    reg_obj.enter_cnfpaswd()
    reg_obj.click_on_terms()
    # reg_obj.click_on_register()
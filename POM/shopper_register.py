import time
from Data.reading_excel import register_locators
from Library.selenium_wrapper import SeleniumWrapper
locators = register_locators()
# print(register_locators)
class Register:

    def __init__(self,driver):
        self.driver = driver
        self.sel_wrp_obj = SeleniumWrapper(self.driver)

    def click_on_login(self):
        # self.driver.find_element(*locators['btn_login']).click()
        self.sel_wrp_obj.click_on_element(locators['btn_login'])

    def click_on_create_acoount(self):
        self.sel_wrp_obj.click_on_element(locators['btn_account'])
        time.sleep(5)
    def enter_fname(self):
        self.sel_wrp_obj.enter_data(locators['text_firstname'],'Swetha')
    def enter_lname(self):
        self.sel_wrp_obj.enter_data(locators['text_lastname'],'Muraleedharan')
    def click_on_gender(self):
        self.sel_wrp_obj.click_on_element(locators['btn_gender'])
    def enter_number(self):
        self.sel_wrp_obj.enter_data(locators['text_phno'],'9856778543')
    def enter_email(self):
        self.sel_wrp_obj.enter_data(locators['text_email'],'swe.personal24@gmail.com')
    def enter_paswd(self):
        self.sel_wrp_obj.enter_data(locators['text_password'],'Qwerty@24')
    def enter_cnfpaswd(self):
        self.sel_wrp_obj.enter_data(locators['text_confrmpswrd'],'Qwerty@24')
    def click_on_terms(self):
        self.sel_wrp_obj.click_on_element(locators['btn_terms'])
    # def click_on_register(self):
    #     self.sel_wrp_obj.click_on_element(locators['btn_register'])


# reg_obj = Register()
# reg_obj.click_on_create_acoount()
# reg_obj.enter_fname()
# reg_obj.enter_lname()
# reg_obj.click_on_gender()
# reg_obj.enter_number()
# reg_obj.enter_email()
# reg_obj.enter_pswd()
# reg_obj.enter_cnfpaswd()
# reg_obj.click_on_terms()
# reg_obj.click_on_register()




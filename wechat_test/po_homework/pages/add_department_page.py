from time import sleep
from selenium.webdriver.common.by import By
from wechat_test.po_homework.pages.contact_page import ContactPage
from wechat_test.po_homework.pages.base_page import BasePage

class AddDepartment(BasePage):
    _departmentname = (By.NAME,"name")
    _parent_party = (By.CLASS_NAME,"js_parent_party_name")
    _submit = (By.CSS_SELECTOR,"[d_ck=submit]")
    _cancel = (By.CSS_SELECTOR,"[d_ck=cancel]")
    def add_department(self,department,index):
        self.find(*self._departmentname).send_keys(department)
        self.find(*self._parent_party).click()
        sleep(2)
        beafnodes = self.finds(By.CSS_SELECTOR,".qui_dialog_body .jstree-closed .jstree-ocl")
        for beaf in beafnodes:
            beaf.click()
        sleep(2)
        self.finds(By.CSS_SELECTOR,".qui_dialog_body .jstree-anchor")[index].click()
        self.find(*self._submit).click()
        sleep(2)
#        return ContactPage(self.driver)
        return self.find(By.ID,"js_tips").get_attribute("innerHTML")
    def no_input_parent_party(self,department):
        self.find(*self._departmentname).send_keys(department)
        self.find(*self._submit).click()
        sleep(2)
        return self.find(By.ID,"js_tips").get_attribute("innerHTML")
    def no_input_department(self):
        self.find(*self._submit).click()
        sleep(2)
        return self.find(By.ID,"js_tips").get_attribute("innerHTML")
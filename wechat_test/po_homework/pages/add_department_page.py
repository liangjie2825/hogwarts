from time import sleep
from selenium.webdriver.common.by import By
from wechat_test.po_homework.pages.contact_page import ContactPage
from wechat_test.po_homework.pages.base_page import BasePage

class AddDepartment(BasePage):
    _departmentname = (By.NAME,"name")
    _parent_party = (By.CLASS_NAME,"js_parent_party_name")
    _submit = (By.CSS_SELECTOR,"[d_ck=submit]")
    _cancel = (By.CSS_SELECTOR,"[d_ck=cancel]")
    def add_department(self,department):
        self.find(*self._departmentname).send_keys(department)
        self.find(*self._parent_party).click()
        sleep(3)
        self.finds(By.CSS_SELECTOR,".qui_dialog_body .jstree-anchor")[1].click()
        self.find(*self._submit).click()
        # self.driver.find_element_by_id("menu_contacts").click()
        # return ContactPage(self.driver)
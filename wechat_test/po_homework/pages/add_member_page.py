from time import sleep
from selenium.webdriver.common.by import By
from wechat_test.po_homework.pages.add_sub_department_page import AddSubDepartment
from wechat_test.po_homework.pages.base_page import BasePage

class AddMember(BasePage):
    def go_to_add_department(self):
        from wechat_test.po_homework.pages.add_department_page import AddDepartment
        self.find(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR,".js_create_party").click()
        sleep(2)
        return AddDepartment(self.driver)
    def go_to_add_subsidiary_department(self):
        return AddSubDepartment(self.driver)
from time import sleep
from selenium.webdriver.common.by import By
from wechat_test.po_homework.pages.add_sub_department_page import AddSubDepartment
from wechat_test.po_homework.pages.base_page import BasePage

class ContactPage(BasePage):
    def go_to_add_member(self):
        from wechat_test.po_homework.pages.add_member_page import AddMember
        return AddMember()
    # def get_department_list(self):
    #     beafnodes = self.finds(By.CSS_SELECTOR,".jstree-closed .jstree-ocl")
    #     for beaf in beafnodes:
    #         beaf.click()
    #         sleep(3)
    #     department_list = self.finds(By.CSS_SELECTOR,".jstree-anchor")
    #     list = [department.text for department in department_list]
    #     return list
    def go_to_add_department(self):
        from wechat_test.po_homework.pages.add_department_page import AddDepartment
        self.find(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR,".js_create_party").click()
        return AddDepartment(self.driver)
    def go_to_add_subsidiary_department(self):
        return AddSubDepartment()
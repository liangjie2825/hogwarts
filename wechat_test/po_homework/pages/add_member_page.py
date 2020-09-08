from selenium.webdriver.common.by import By

from wechat_test.po_homework.pages.add_department_page import AddDepartment
from wechat_test.po_homework.pages.add_sub_department_page import AddSubDepartment
from wechat_test.po_homework.pages.base_page import BasePage

class AddMember(BasePage):
    def go_to_add_department(self):
        return AddDepartment(self.driver)
    def go_to_add_subsidiary_department(self):
        return AddSubDepartment(self.driver)
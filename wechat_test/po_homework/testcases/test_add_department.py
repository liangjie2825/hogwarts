import random
from random import randrange
from wechat_test.po_homework.pages.home_page import HomePage


class TestAddDepartment:
    def setup_class(self):
        self.main = HomePage()
    # def test_get_departmentlist(self):
    #     list = self.main.go_to_contact().get_department_list()
    #     print(list)
    def test_add_department(self):
        department = "测试1"
#        parent_party = "腾讯公司"
        result = self.main.go_to_contact().go_to_add_department().add_department(department).get_department_list()
        assert department in result
    def teardown(self):
        self.main.base_quite()
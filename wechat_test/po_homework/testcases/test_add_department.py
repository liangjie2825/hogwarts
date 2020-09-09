import random
from random import randrange
from wechat_test.po_homework.pages.home_page import HomePage


class TestAddDepartment:
    def setup(self):
        self.main = HomePage()
    def test_add_department_success(self):
        department = "测试1"
        list = self.main.go_to_contact().get_department_list()
#        count1 = list.count(department)
        length = len(list)
        index = random.randint(0,length-1)
        result = self.main.go_to_contact().go_to_add_department().add_department(department,index)
#        count2 = self.main.go_to_contact().get_department_list().count(department)
#        assert count1 == count2 - 1
        assert "新建部门成功" == result
    def test_add_department_fail(self):
        department = "腾讯公司"
#        list = self.main.go_to_contact().get_department_list()
#        count1 = list.count(department)
        result = self.main.go_to_contact().go_to_add_department().add_department(department, 0)
        # count2 = self.main.go_to_contact().get_department_list().count(department)
        # assert count1 == count2
        assert "该部门已存在" == result
    def test_no_input_parent_party(self):
        department = "测试2"
        result = self.main.go_to_contact().go_to_add_department().no_input_parent_party(department)
        assert "请选择所属部门" == result
    def test_no_input_deparment(self):
        result =self.main.go_to_contact().go_to_add_department().no_input_department()
        assert "请输入部门名称" == result
    def test_member_add_department_success(self):
        department = "测试2"
        result = self.main.go_to_add_member().go_to_add_department().add_department(department,0)
        assert "新建部门成功" == result
    def teardown(self):
        self.main.base_quite()
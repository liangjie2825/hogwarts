from selenium.webdriver.common.by import By

from wechat_test.po_homework.pages.add_member_page import AddMember
from wechat_test.po_homework.pages.contact_page import ContactPage
from wechat_test.po_homework.pages.base_page import BasePage


class HomePage(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"
    _keyname = 'expiry'
    _file = "../../db_data/logincookies"
    def setup_class(self):
        super().get_cookie(self._file, self._url, self._keyname)
    def go_to_contact(self):
        self.find(By.ID,"menu_contacts").click()
        return ContactPage(self.driver)
    def go_to_add_member(self):
        self.find(By.CSS_SELECTOR, "[node-type='addmember']").click()
        return AddMember(self.driver)
import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWechatLogin():
    def setup_method(self,method):
        option = Options()
        option.debugger_address = "localhost:9222"
#        self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def test_cookie(self):
        db = shelve.open("../db_data/logincookies")
        cookies = db['cookie']
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
    def test_import_address_book_success(self):
        self.test_cookie()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        #点击导入通讯录，进入通讯录导入页面
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(2)").click()
        #点击上传文件
        self.driver.find_element_by_css_selector("#js_upload_file_input").send_keys("/Users/liangjie/Documents/address_book.xlsx")
        #点击确认上传按钮
        self.driver.find_element_by_css_selector("#submit_csv").click()
        sleep(5)
        #添加断言，判断上传成功
        assert "前往查看" == self.driver.find_element_by_css_selector("#reloadContact").text
    def test_import_address_book_fail(self):
        self.test_cookie()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        #点击导入通讯录，进入通讯录导入页面
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(2)").click()
        #点击上传文件
        self.driver.find_element_by_css_selector("#js_upload_file_input").send_keys("/Users/liangjie/Documents/20200602.xlsx")
        #点击确认上传按钮
        self.driver.find_element_by_css_selector("#submit_csv").click()
        sleep(5)
        #添加断言，判断上传失败
        assert "按模板修改导入" == self.driver.find_element_by_css_selector("#reloadContact").text
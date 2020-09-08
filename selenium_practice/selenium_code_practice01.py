from time import sleep
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestSelenium():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    # def test_selenium(self):
    #     self.driver.get("https://testerhome.com")
    #     self.driver.find_element_by_link_text("社团").click()
    #     self.driver.find_element_by_link_text("京东").click()
    #     self.driver.find_element_by_css_selector(".topic-7908 .title > a").click()
    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
#        self.driver.find_element(By.ID,'kw').send_keys("京东")
        el_send = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")

        el_send.send_keys("京东")
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()

        action.scroll_from_element(el_send,0,10000).perform()
        sleep(3)

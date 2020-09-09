import shelve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    _url = ""
    #复用浏览器
    def __init__(self,driver_base=None):
        if driver_base is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver:WebDriver = driver_base

        if self._url != "":
            self.driver.get(self._url)
        #隐式等待
        self.driver.implicitly_wait(3)
    #复用cookie
    def get_cookie(self,file,_url,keyname):
        db = shelve.open(file)
        cookies = db['cookie']
        db.close()
        self.driver.get(_url)
        for cookie in cookies:
            if keyname in cookie.keys():
                cookie.pop(keyname)
            self.driver.add_cookie(cookie)
    def find(self,by,value):
        return self.driver.find_element(by=by,value=value)
    def finds(self,by,value):
        return self.driver.find_elements(by=by,value=value)
    def base_quite(self):
        return self.driver.quit()
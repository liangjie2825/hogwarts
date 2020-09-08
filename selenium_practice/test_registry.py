import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from tools.get_datas import GetDatas

class TestRegistry():
    data = GetDatas('./test_datas','utf-8')
    def setup(self):
        self.dirver = webdriver.Chrome()
        self.dirver.maximize_window()
        self.dirver.implicitly_wait(10)
    def teardown(self):
        self.dirver.quit()
    #用户注册
    @pytest.mark.parametrize('email,password,confirm,mobile',data.get_datas()[0],ids=data.get_datas()[1])
    def test_registry(self,email,password,confirm,mobile):
        self.dirver.get("https://172.16.14.207:9909/epm-dataCloud-cas/index/registe")

        self.dirver.find_element_by_id("email").send_keys(email)
        self.dirver.find_element_by_id("password").send_keys(password)
        self.dirver.find_element_by_id("confirm").send_keys(confirm)
        self.dirver.find_element_by_id("mobile").send_keys(mobile)
        self.dirver.find_element_by_css_selector('button')
#        self.dirver.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div[2]/form/div[5]/div/div/span/button').click()
    #用户登录
    @pytest.mark.parametrize('mobile,password',data.get_datas()[2],ids=data.get_datas()[3])
    def test_login(self,mobile,password):
        self.dirver.get("https://172.16.14.207:9909/portal")
        #未认证用户登录系统
        self.dirver.find_element_by_id("username").send_keys(mobile)
        self.dirver.find_element_by_id("_password").send_keys(password)
        self.dirver.find_element_by_id("loginSubmit").click()

    @pytest.mark.parametrize('enterpriseName,enterpriseAddress,enterpriseContent,enterpriseNumber,legalPersonName,legalPersonNumber',
        data.get_datas()[4], ids=data.get_datas()[5])
    def test_authentication(self,enterpriseName,enterpriseAddress,enterpriseContent,enterpriseNumber,legalPersonName,legalPersonNumber):
        #进入系统后前往认证页面
        self.dirver.switch_to.frame("iframe0")
        self.dirver.find_element_by_css_selector('.ant-col a').click()
        #进入企业认证页面
        self.dirver.find_element_by_xpath('//*[text()="企业认证"]//..//../button').click()
        self.dirver.find_element_by_id("enterpriseName").send_keys(enterpriseName)
        self.dirver.find_element_by_id("enterpriseAddress").send_keys(enterpriseAddress)
        self.dirver.find_element_by_id("enterpriseContent").send_keys(enterpriseContent)
        self.dirver.find_element_by_id("enterpriseNumber").send_keys(enterpriseNumber)
        

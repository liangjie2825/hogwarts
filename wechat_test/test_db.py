import shelve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_db():
    option = Options()
    option.debugger_address = "localhost:9222"
    driver = webdriver.Chrome(options=option)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    cookies = driver.get_cookies()
    db = shelve.open("db_data/logincookies")
    db['cookie'] = cookies
    db.close()
    driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

# 元素
login = driver.find_element_by_xpath("//*[@id=\"u1\"]/a[8]").click()
time.sleep(2)
username_login = driver.find_element_by_xpath("//*[@id=\"TANGRAM__PSP_10__footerULoginBtn\"]").click()
username = driver.find_element_by_xpath("//*[@id=\"TANGRAM__PSP_10__userName\"]").send_keys("15139633525")
pwd = driver.find_element_by_xpath("//*[@id=\"TANGRAM__PSP_10__password\"]").send_keys("Baidu2019..")
login_btn = driver.find_element_by_xpath("//*[@id=\"TANGRAM__PSP_10__submit\"]").click()
time.sleep(3)
driver.close()

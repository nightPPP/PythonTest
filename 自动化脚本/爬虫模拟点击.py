from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs\bin\phantomjs.exe")  # 调用phantomJS
driver.get("https://www.baidu.com")  # 打开页面的网址
time.sleep(3)

driver.find_element_by_id("kw").send_keys("模拟点击")

driver.find_element_by_id("kw").send_keys(Keys.RETURN)
# driver.find_element_by_id("su").click()
time.sleep(5)
# driver.back()
# driver.forward()
# driver.refresh()
driver.save_screenshot("baidu3.png")

driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "a")    # 组合键

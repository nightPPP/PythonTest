from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs\bin\phantomjs.exe")  # 调用phantomJS
driver.get("https://www.baidu.com")  # 打开页面的网址
time.sleep(3)

# cookies = driver.get_cookies()
# print(cookies)

driver.save_screenshot("baidu.png")
driver.find_element_by_id("kw").send_keys("6666")
driver.save_screenshot("baidu2.png")


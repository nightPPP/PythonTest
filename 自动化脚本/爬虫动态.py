from selenium import webdriver
import time


driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs\bin\phantomjs.exe")  # 调用phantomJS
driver.get("http://www.youdao.com/w/eng/excel")  # 打开页面的网址
time.sleep(5)
data = driver.find_element_by_id('results-contents').text     # 使用ID筛选需要的部分
print(data)
print("")
a = data.find('\n')     # 找到第一个换行符
b = data[a + 1:].find('\n')  # 找到第二个换行符
new_data = data[a + 1:a + 1 + b]    # 即两个换行符之间的部分，即销量
driver.quit()   # 关闭页面
print(new_data)


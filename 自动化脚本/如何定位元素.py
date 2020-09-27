# 单个元素
# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_elememt_by_tag_name
# find_elememt_by_class_name
# find_elememt_by_css_selector

# 多个元素
# find_elememts_by_name
# find_elememts_by_xpath
# find_elememts_by_link_text
# find_elememts_by_partial_link_text
# find_elememts_by_tag_name
# find_elememts_by_class_name
# find_elememts_by_css_selector


from selenium import webdriver
import time


driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs\bin\phantomjs.exe")  # 调用phantomJS
driver.get("https://www.python.org/")  # 打开页面的网址
time.sleep(10)

by_id = driver.find_element_by_id('downloads').get_attribute('innerHTML')
print(by_id)
driver.close()
from bs4 import BeautifulSoup
import requests

word = 'excel'
url = 'http://www.youdao.com/w/eng/' + word

# 请求链接，获取数据
web_data = requests.get(url).text

# 将数据xml格式化啊
soup = BeautifulSoup(web_data, 'lxml')
# meaning1 = soup.select('#phrsListTab > div.trans-container > ul > li:nth-child(1)')
# meaning2 = soup.select('#phrsListTab > div.trans-container > ul > li:nth-child(2)')
# if len(meaning1)>0:
#     meaning1 = meaning1[0].get_text()
# if len(meaning2)>0:
#     meaning2 = meaning2[0].get_text()
# print(meaning1)
# print(meaning2)

# 获取目标元素
meaning = soup.select('#phrsListTab > div.trans-container > ul > li')
# 遍历元素集合

for i in meaning:
    print(i.text)
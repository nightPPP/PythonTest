from bs4 import BeautifulSoup
import requests

word = input("请输入要查询的单词")
url = "http://www.youdao.com/w/eng/" + word

# 请求链接，获取数据
getData = requests.get(url).text

# 将数据xml格式化啊
data = BeautifulSoup(getData, 'lxml')

# 获取目标元素
meanings = data.select('#phrsListTab > div.trans-container > ul > li')
if len(meanings) == 0:
    print("没有找到")
    exit(0)

# 遍历元素集合
for mean in meanings:
    print(mean.text)






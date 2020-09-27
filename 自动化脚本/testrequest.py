import requests


response = requests.get("http://www.baidu.com")
print(response.status_code)
print(response.headers)
print(response.request.url)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
response2 = requests.get(response.request.url, headers=headers)
print(response2.content.decode())

import re


# re.match(正则表达式, 需要处理的字符串)
# re.match(r"hello", "hello world")
result = re.match(r"[a-zA-Z]ello", "Hello world")

if result:
    print(result.group())


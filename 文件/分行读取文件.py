# 打开
file = open("README")

# 读取
while True:
    text = file.read()
    if not text:
        break
    print(text)

# 关闭
file.close()
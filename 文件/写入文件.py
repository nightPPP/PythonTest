# 打开
file = open("README", "a")

# 写入
file.write("aaa")

# 关闭
file.close()

file = open("README")
print(file.read())
file.close()
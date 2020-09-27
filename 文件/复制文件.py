# 打开文件--源文件
file_read = open("README")

# 打开文件--目标文件
file_write = open("README[复件]", "w")

while True:

    # 读写
    text_read = file_read.readline()

    if not text_read:
        break

    file_write.write(text_read)

# 关闭
file_read.close()
file_write.close()

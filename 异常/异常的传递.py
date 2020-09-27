def demo1():
    return int(input("请输入一个整数"))

def demo2():
    return demo1()

try:
    print(demo2())

except Exception as result:
    print("异常---%s" %result)

else:
    print("无异常")

finally:
    print("finally")

print("*" * 50)
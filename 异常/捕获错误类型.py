try:
    num = int(input("请输入一个整数"))

    result = 8 / num

    print(result)

except ZeroDivisionError:
    print("除 0 错误")

except ValueError:
    print("请输入正确的整数")
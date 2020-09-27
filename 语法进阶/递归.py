def sum_num(num):
    if 1 == num:
        print("返回")
        return 1
    temp = sum_num(num-1)
    return num + temp

print(sum_num(10))
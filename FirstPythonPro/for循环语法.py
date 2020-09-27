num_list = [1, 2, 3, 4, 5]

for num in num_list:
    print(num)
    if num == 2:
        break
else:
    print("执行了else")

print("循环结束")
# 元组一旦创建，不能修改
# 元组可以存储不同类型的数据
info_tuple = ("aaa", "bbb", "ccc", "aaa")
print(type(info_tuple))
print(info_tuple[1])
print(info_tuple.index("aaa"))
print(info_tuple.count("aaa"))
print(len(info_tuple))

for my_tuple in info_tuple:
    print("元组的数据 " + my_tuple)

name_tuple = ("小明", 21, 1.85)
print("%s 年龄是 %d 身高是 %.2f" %("小明", 21, 1.85))
print("%s 年龄是 %d 身高是 %.2f" %name_tuple)
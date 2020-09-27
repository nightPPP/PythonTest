#-*- coding: UTF-8 -*-
name_list = ["aaa", "bbb", "ccc"]

print(name_list[1])

print(name_list.index("aaa"))

# 末尾增加
name_list.append("ddd")
print(name_list)

# 指定位置增加
name_list.insert(1, "eee")
print(name_list)

# 添加列表
new_list = ["qqq", "www"]
name_list.extend(new_list)
print(name_list)

# 删除指定数据
name_list.remove("aaa")
print(name_list)

# 默认删除列表中最后一个元素删除
name_list.pop()
print(name_list)

# 删除指定索引位置的数据
name_list.pop(3)
print(name_list)

# name_list.clear()
# print(name_list)

# del 从内存中删除
del name_list[1]
print(name_list)

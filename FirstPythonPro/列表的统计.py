name_list = ["aaa", "bbb", "ccc", "aaa"]

# 列表的长度
list_len = len(name_list)
print("列表中包含 %d 个元素" %list_len)

# 元素在列表中出现的次数
count = name_list.count("aaa")
print("aaa出现的次数 %d 次" %count)

# 删除出现这个第一个元素
name_list.remove("aaa")
print(name_list)
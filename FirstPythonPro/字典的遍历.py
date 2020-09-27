students = [
    {"name":"小明"},
    {"name":"小红" }
]

find_name = "小"
for stu in students:
    print(stu)
    if stu["name"] == find_name:
        print("找到了 %s" %stu["name"])
        break
else:
    print("没找到 %s" %find_name)

print("循环结束")
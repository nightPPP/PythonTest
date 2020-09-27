def create_num(all_num):
    a, b = 0, 1
    current_index = 0
    while current_index < all_num:
        # 如果函数中有yield，那么这就是个生成器的模板,不再是函数
        # 外面for循环遍历的值拿的就是这个yield修饰的值
        yield a
        a, b = b, a + b
        current_index += 1


obj = create_num(10)

# ret = next(obj)
# print(ret)
# ret = next(obj)
# print(ret)


for num in obj:
    print(num)

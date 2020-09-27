def create_num(all_num):
    a, b = 0, 1
    current_index = 0
    while current_index < all_num:
        # 如果函数中有yield，那么这就是个生成器的模板,不再是函数
        # 外面for循环遍历的值拿的就是这个yield修饰的值
        yield a
        a, b = b, a + b
        current_index += 1
    # 下面用ret.value接收
    return "ok..."


obj = create_num(10)

while True:
    try:
        ret = next(obj)
        print(ret)
    except Exception as ret:
        # 这个就是ok...
        print(ret.value)
        break
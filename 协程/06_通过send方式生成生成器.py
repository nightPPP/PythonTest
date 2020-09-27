def create_num(all_num):
    a, b = 0, 1
    current_index = 0
    while current_index < all_num:
        ret = yield a
        print(">>>>>ret>>>> ",ret)
        a, b = b, a + b
        current_index += 1


obj = create_num(10)

ret = next(obj)
print(ret)

ret = obj.send("hahaha")
print(ret)

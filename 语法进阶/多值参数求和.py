def sum_total(*args):
    num = 0
    for n in args:
        num += n
    return num

reslut = sum_total(1,2,3,4,5)
print(reslut)
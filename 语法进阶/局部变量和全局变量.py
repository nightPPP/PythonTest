num = 10

def demo1():

    # 想在局部中修改全局变量，加global
    # global num
    # 修改的不是全局变量，而是新创建的一个局部变量
    num = 99
    print(num)

def demo2():
    print(num)

demo1()
demo2()
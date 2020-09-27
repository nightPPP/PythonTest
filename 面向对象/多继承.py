class A(object):

    def test(self):
        print("testA方法")


class B(object):

    def test(self):
        print("testB方法")

    def demo(self):
        print("demo方法")


class C(A, B):
    pass

c = C()
c.test()
c.demo()
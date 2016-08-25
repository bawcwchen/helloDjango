#
"""
  class测试,object,self都是系统变量，不能变
"""


class User(object):  # User继承object,object是一个class,相当于java中的Object,所有类都会继承
    def __init__(self, name, age):  # __init__相当于是构造函数
        self.name = name
        self.age = age

    def show(self):
        print('%s:%s' % (self.name, self.age))


# 用来测试，如果被其他模块引用，则自动失效
if __name__ == '__main__':
    user1 = User("chenJun", 20)
    user1.show()

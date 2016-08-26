# ! /usr/bin/env python
# -*- coding:utf-8 -*-
from stepByStep.animal import Animal


class Cat(Animal):
    __slots__ = ('_name', '_age')  # 用tuple定义允许绑定的属性名称

    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    def sing(self):
        print("%s is sing" % self._name)

    def __str__(self):  # 重写java中的toString()方法
        return "cat name is %s,age is %s" % (self._name, self._age)

    __repr__ = __str__  # 用于直接打印函数

    def __iter__(self):  # 用来迭代
        pass

    def __next__(self):  # 取下一个值
        StopIteration()
        pass

    def __getitem__(self, item):  # 通过[]取值
        pass

    def __getattr__(self, item):  # 只有调用不存在的属性时，才调用getattr()
        if item == 'score':
            return lambda: 25  # 返回一个匿名函数，值为25

        raise AttributeError("attribute %s is not exists" % item)

    def __len__(self):  # 当调用len()时，会调用
        pass

    def __call__(self, *args, **kwargs):  # instance()，直接调用实例方法
        pass

    @property
    def age(self):  # getter
        return self._age

    @age.setter
    def age(self, value):  # setter
        if not isinstance(value, int):
            raise ValueError("score must be int")

        if value < 0 or value > 100:
            raise ValueError("score must be 0~100")

        self._age = value


if __name__ == '__main__':
    cat1 = Cat("cat1", 20)
    cat1.sing()
    print(cat1)

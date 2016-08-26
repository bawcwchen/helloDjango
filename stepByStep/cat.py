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

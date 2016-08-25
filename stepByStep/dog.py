# ! /usr/bin/env python
# -*- coding:utf-8 -*-
from stepByStep.animal import Animal


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    def sing(self):
        print("%s is sing" % self._name)


if __name__ == '__main__':
    dog1 = Dog("dog1", 22)
    dog1.sing()


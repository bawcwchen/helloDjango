# ! /usr/bin/env python
# -*- coding:utf-8 -*-
from stepByStep.animal import Animal


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    def sing(self):
        print("%s is sing" % self._name)


if __name__ == '__main__':
    cat1 = Cat("cat1", 20)
    cat1.sing()

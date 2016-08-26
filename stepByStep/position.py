"""
   方位枚举
"""

from enum import Enum, unique


@unique
class Position(Enum):
    Up = 1
    Down = 2
    Left = 3
    Right = 4


if __name__ == '__main__':
    for name, member in Position.__members__.items():
        print(name, '=>', member, ',', member.value)

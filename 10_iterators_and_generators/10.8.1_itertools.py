"""
Функция должна возвращать итератор, генерирующий последовательность из n чисел, каждое из которых является факториалом
очередного натурального числа.
"""

from itertools import accumulate


def factorials(n):
    yield from accumulate(range(1, n + 1), lambda x, y: x * y)


numbers = factorials(6)

print(*numbers)

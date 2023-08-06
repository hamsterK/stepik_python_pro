"""
Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable,
зацикленных times раз.
"""

from itertools import tee, chain


def ncycles(iterable, times):
    return chain.from_iterable(tee(iterable, times))


print(*ncycles([1, 2, 3, 4], 3))

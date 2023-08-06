"""
Функция должна возвращать единственное число — сумму цифр всех чисел, присутствующих в итерируемом объекте iterable.
"""

from itertools import chain


def sum_of_digits(iterable):
    elements = chain.from_iterable(map(str, iterable))
    return sum(map(int, elements))


print(sum_of_digits([13, 20, 41, 2, 2, 5]))


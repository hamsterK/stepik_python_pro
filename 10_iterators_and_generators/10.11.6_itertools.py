"""
Функция должна преобразовывать числа из списка numbers в отрезки, представляя их в виде кортежей, где первый элемент
кортежа является левой границей отрезка, второй элемент — правой границей отрезка. Полученные кортежи-отрезки функция
должна возвращать в виде списка.
"""

from itertools import groupby


def ranges(numbers):
    result = []
    for _, group in groupby(numbers, key=lambda n: n - numbers.index(n)):
        group = tuple(group)
        group = group[0], group[-1]
        result.append(group)
    return result


numbers = [1, 2, 3, 4, 7, 8, 10]

print(ranges(numbers))

"""
Функция должна возвращать итератор, генерирующий последовательность, элементами которой являются объединенные в кортежи
по n элементов соседние элементы итерируемого объекта iterable. Если у элемента не достаточно соседей,
то ими становится значение None.
"""

from itertools import repeat, zip_longest


def grouper(iterable, n):
    return zip_longest(*repeat(iter(iterable), n))


numbers = [1, 2, 3, 4, 5, 6]

print(*grouper(numbers, 2))

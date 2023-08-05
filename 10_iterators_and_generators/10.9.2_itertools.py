"""
Функция должна возвращать n-ый по счету элемент итерируемого объекта iterable. Если итерируемый объект iterable содержит
менее n элементов, функция должна вернуть значение None.
"""

from itertools import islice


def take_nth(iterable, n):
    return next(islice(iterable, n - 1, None), None)


numbers = [11, 22, 33, 44, 55]

print(take_nth(numbers, 3))

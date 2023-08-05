"""
Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, для которого функция
predicate вернула значение True. Если такого элемента нет, функция first_true() должна вернуть значение None.
"""

from itertools import filterfalse


def first_true(iterable, predicate=None):
    if predicate is None:
        predicate = bool
    answer = list(filterfalse(lambda x: predicate(x) is False, iterable))
    if len(answer) == 0:
        return None
    else:
        return answer[0]


numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 0, 10, 100, 200)
numbers_iter = filter(None, numbers)

print(first_true(numbers_iter, lambda num: num < 0))

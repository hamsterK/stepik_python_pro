"""
Функция должна работать противоположно функции filter(), то есть возвращать итератор, элементами которого являются
элементы итерируемого объекта iterable, для которых функция predicate вернула значение False.
"""


def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    return filter(lambda x: predicate(x) is False, iterable)


objects = [0, 0, 0, True, False, 1788, [], {}, set(), (), '', 0.0, None, 'stepik', dict()]

print(*filterfalse(None, objects))

# 0 0 0 False [] {} set() ()  0.0 None {}

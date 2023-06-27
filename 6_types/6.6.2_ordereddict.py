"""
Реализуйте функцию custom_sort(), которая принимает два аргумента в следующем порядке:

ordered_dict — словарь OrderedDict
by_values — булево значение, по умолчанию имеет значение False

Функция должна сортировать словарь ordered_dict:
по ключам, если by_values имеет значение False
по значениям, если by_values имеет значение True

Примечание 1. Функция должна изменять переданный словарь, а не возвращать новый. Возвращаемым значением функции должно
быть None.
"""

from collections import OrderedDict


def custom_sort(data, by_values=False):
    if by_values:
        for key in sorted(data, key=lambda k: data[k]):
            data.move_to_end(key)
    else:
        for key in sorted(data):
            data.move_to_end(key)


data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)
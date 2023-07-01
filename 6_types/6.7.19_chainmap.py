"""
Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:

chainmap — объект типа ChainMap, элементами которого являются словари
key — произвольный объект
Функция должна возвращать множество, элементами которого являются все значения по ключу key из всех словарей в chainmap.
Если ключ key отсутствует в chainmap, функция должна вернуть пустое множество.
"""

from collections import ChainMap


def get_all_values(chainmap, key):
    return {d[key] for d in chainmap.maps if key in d}


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')


print(*sorted(result))

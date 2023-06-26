"""
Рассмотрим следующий словарь:
{'a': [1, 2], 'b': [3, 1], 'c': [2]}
«Перевернем» его, представив ключи в виде значений, а значения — в виде ключей:
{1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']}

Реализуйте функцию flip_dict(), которая принимает один аргумент:
dict_of_lists — словарь, в котором ключом является число или строка, а значением — список чисел или строк
Функция должна возвращать новый словарь (тип defaultdict с типом list в качестве значения по умолчанию), который
представляет собой «перевернутый» словарь dict_of_lists.

Sample Input 1:
print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))

Sample Output 1:
defaultdict(<class 'list'>, {1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']})
"""

from collections import defaultdict


def flip_dict(dict_of_lists):
    new_dict = defaultdict(list)
    for key, value in dict_of_lists.items():
        for element in value:
            new_dict[element].append(key)
    return new_dict


print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))

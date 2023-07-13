"""
Функция должна выводить все пары ключ-значение словаря nested_dicts, а также значения всех его дочерних словарей.
При выводе значений дочерних словарей необходимо перечислять имена всех ключей, начиная с верхнего уровня,
разделяя их точками.
"""


def dict_travel(data, parent_key=''):
    for key, value in sorted(data.items()):
        key = f'{parent_key}.{key}' if parent_key else key
        if isinstance(value, dict):
            dict_travel(value, key)
        else:
            print(f'{key}: {value}')


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)

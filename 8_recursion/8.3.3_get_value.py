"""
Функция get_value()
Реализуйте функцию get_value(), которая принимает два аргумента в следующем порядке:

nested_dicts — словарь, содержащий в качестве значений произвольные объекты или словари, которые, в свою очередь,
так же содержат в качестве значений произвольные объекты или словари; вложенность может быть произвольной key
— хешируемый объект.
Функция должна определять значение, которое соответствует ключу key в словаре nested_dicts или в одном из его вложенных
словарей, и возвращать полученный результат.
"""


def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]
    for info in nested_dicts.values():
        if type(info) == dict:
            value = get_value(info, key)
            if value is not None:
                return value


data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'cityName'))

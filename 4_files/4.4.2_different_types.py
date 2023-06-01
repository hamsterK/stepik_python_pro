"""
Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося в файле
data.json, измененные по следующим правилам:

если объект является строкой, в его конец добавляется восклицательный знак
если объект является числом, он увеличивается на единицу
если объект является логическое значением, он инвертируется
если объект является списком, он удваивается
если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
если объект является пустым значением (null), он не добавляется

Полученный список программа должна записать в файл updated_data.json.

Примечание 1. Например, если бы файл data.json имел вид:

["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]

то программа должна была бы создать файл updated_data.json со следующим содержанием:

["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]
"""

import json

with open('data.json', 'r', encoding='utf-8') as input_file:
    data = json.load(input_file)
    updated_data = list()
    for value in data:
        if type(value) == str:
            updated_data.append(f'{value}!')
        elif type(value) == int:
            updated_data.append(value + 1)
        elif type(value) == bool:
            updated_data.append(True if value is False else False)
        elif type(value) == list:
            updated_data.append(value * 2)
        elif type(value) == dict:
            value['newkey'] = None
            updated_data.append(value)

with open('updated_data.json', 'w', encoding='utf-8') as output_file:
    json.dump(updated_data, output_file)

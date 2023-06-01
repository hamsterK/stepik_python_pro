"""
Вам доступны два файла data1.json и data2.json, каждый из которых содержит по единственному JSON-объекту.
Напишите программу, которая объединяет два данных JSON-объекта в один JSON-объект, причем если пары из первого
и второго объектов имеют совпадающие ключи, то значение следует взять из второго объекта. Полученный JSON-объект
программа должна записать в файл data_merge.json.
"""

import json

with open('data1.json', 'r', encoding='utf-8') as file1:
    data1 = json.load(file1)

with open('data2.json', 'r', encoding='utf-8') as file2:
    data2 = json.load(file2)

data1.update(data2)
sorted_data = list()

for i in data1.items():
    sorted_data.append(i)
sorted_data.sort()
sorted_data = dict(sorted_data)

with open('data_merge.json', 'w', encoding='utf-8') as output_file:
    json.dump(sorted_data, output_file)

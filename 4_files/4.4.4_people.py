"""
Вам доступен файл people.json, содержащий список JSON-объектов. Причем у различных объектов может быть различное
количество ключей.

Напишите программу, которая добавляет в каждый JSON-объект из данного списка все недостающие ключи, присваивая этим
ключам значение null. Ключ считается недостающим, если он присутствует в каком-либо другом объекте, но отсутствует в
данном. Программа должна создать список с обновленными JSON-объектами и записать его в файл updated_people.json.

Примечание 2. Например, если бы файл people.json имел вид:

[
   {
      "age": 33,
      "country": "Lesotho"
   },
   {
      "age": 25,
      "country": "Guinea",
      "name": "Dorey"
   }
]
то программа должна была создать файла updated_people.json со следующим содержанием:

[
   {
      "age": 33,
      "country": "Lesotho"
      "name": null
   },
   {
      "age": 25,
      "country": "Guinea",
      "name": "Dorey"
   }
]
"""

import json

with open('people.json', 'r', encoding='utf-8') as input_file:
    data = json.load(input_file)
    list_of_keys = set()
    for i in data:
        for j in i.keys():
            list_of_keys.add(j)

    for entry in data:
        for value in list_of_keys:
            if value not in entry.keys():
                entry[value] = None

with open('updated_people.json', 'w', encoding='utf-8') as output_file:
    json.dump(data, output_file)

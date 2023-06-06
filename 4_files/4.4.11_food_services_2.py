"""
Вам доступен файл food_services.json, содержащий список JSON-объектов, которые представляют данные о заведениях
общественного питания:

[
   {
      "Name": "СМЕТАНА",
      "IsNetObject": "нет",
      "OperatingCompany": "",
      "TypeObject": "кафе",
      "AdmArea": "Северо-Восточный административный округ",
      "District": "Ярославский район",
      "Address": "город Москва, улица Егора Абакумова, дом 9",
      "SeatsCount": 48
   },
   ...
]
Под «заведением» будем подразумевать один JSON-объект из этого списка. У заведения имеются следующие атрибуты:

Name — название
IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
OperatingCompany — название сети
TypeObject — вид (кафе, столовая, ресторан и т.д.)
AdmArea — административная зона
District — район
Address — полный адрес
SeatsCount — количество посадочных мест

Напишите программу, которая определяет все виды заведений и для каждого вида находит самое большое заведение этого
вида (имеет наибольшее количество посадочных мест). Программа должна вывести все виды заведений в лексикографическом
порядке, указав для каждого самое большое заведение и количество посадочных мест в нем. Данные о заведениях должны быть
расположены каждые на отдельной строке, в следующем формате:

<вид заведения>: <название заведения>, <количество посадочных мест>

Примечание 1. Начальная часть ответа выглядит так:

бар: Барное объединение ПРОФСОЮЗ, 800
буфет: СТОЛОВАЯ - КАНТИНАСИТИ, 320
закусочная: Бургерная FARШ, 74
...
"""

import json

with open('food_services.json', encoding='utf-8') as file:
    shops = json.load(file)

seats_count = {}
for shop in shops:
    if shop['TypeObject'] in seats_count:
        if shop['SeatsCount'] > seats_count[shop['TypeObject']]['SeatsCount']:
            seats_count[shop['TypeObject']]['Name'] = shop['Name']
            seats_count[shop['TypeObject']]['SeatsCount'] = shop['SeatsCount']
    else:
        seats_count[shop['TypeObject']] = {'Name': shop['Name'], 'SeatsCount': shop['SeatsCount']}

for key in sorted(seats_count, key=lambda x: x):
    establishment = seats_count[key]
    print(f'{key}: {establishment["Name"]}, {establishment["SeatsCount"]}')

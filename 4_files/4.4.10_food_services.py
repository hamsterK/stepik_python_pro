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
SeatsCount — количество мест

Напишите программу, которая определяет район Москвы, в котором находится больше всего заведений, и выводит название этого района и количество
заведений в нем и определяет сеть с самым большим числом заведений,  выводит название этой сети и количество
заведений этой сети.

Полученные значения программа должна вывести в следующем формате:

<район>: <количество заведений>
<название сети>: <количество заведений>
Примечание 1. Гарантируется, что искомая сеть единственная.

Примечание 2. Пример вывода:

район Метрогородок: 456
Французская пекарня SeDelice: 144
"""

import json


with open('food_services.json', encoding='utf-8') as file:
    shops = json.load(file)

districts_count = {}
shops_count = {}
for shop in shops:
    districts_count[shop['District']] = districts_count.get(shop['District'], 0) + 1
    shops_count[shop['OperatingCompany']] = shops_count.get(shop['OperatingCompany'], 0) + 1

del shops_count['']

print(*max(districts_count.items(), key=lambda x: x[1]), sep=': ')
print(*max(shops_count.items(), key=lambda x: x[1]), sep=': ')

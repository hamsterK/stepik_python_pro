"""
Тимур планирует пойти в бассейн. Среди всех бассейнов ему подходят те, которые открыты в понедельник в период
с 10:00 до 12:00. Также ему нравится плавать по длинным дорожкам, поэтому из всех работающих в это время бассейнов
нужно выбрать бассейн с наибольшей длиной дорожки, при равных значениях — c наибольшей шириной.

Вам доступен файл pools.json, содержащий список JSON-объектов, которые представляют данные о крытых
плавательных бассейнах:

[
   {
      "ObjectName": "Физкультурно-оздоровительный комплекс с бассейном «ГБУ «СШОР № 82» Москомспорта»",
      "AdmArea": "Северо-Восточный административный округ",
      "District": "Алтуфьевский район",
      "Address": "Инженерная улица, дом 5, корпус 1",
      "WorkingHoursSummer": {
         "Понедельник": "10:00-11:00",
         "Вторник": "10:00-11:00",
         "Среда": "10:00-11:00",
         "Четверг": "10:00-11:00",
         "Пятница": "10:00-11:00",
         "Суббота": "10:00-11:00",
         "Воскресенье": "09:00-15:00",
      },
      "DimensionsSummer": {
         "Square": 350,
         "Length": 25,
         "Width": 14,
         "Depth": 1.8
      }
   },
   ...
]
Под «бассейном» будем подразумевать один JSON-объект из этого списка. У бассейна имеются следующие атрибуты:

ObjectName — название, будь то фитнес клуб или спортивный комплекс
AdmArea — административный округ
District — название района
Address — адрес
WorkingHoursSummer — график работы, время начала и закрытия указываются в формате HH:MM
DimensionsSummer — размеры бассейна, где Square — площадь, Length — длина, Width — ширина, Depth — глубина
Напишите программу, которая определяет бассейн, подходящий Тимуру. Программа должна вывести его размеры и адрес
в следующем формате:

<длина>x<ширина>
<адрес>

Примечание 1. Пример вывода:

25x16
Писцовая улица, дом 12, строение 1
"""

import json
from datetime import time


with open('pools.json', encoding='utf-8') as file:
    pools = json.load(file)

timur_pools = []
for pool in pools:
    start, end = pool['WorkingHoursSummer']['Понедельник'].split('-')
    if time.fromisoformat(start) <= time(hour=10) and time.fromisoformat(end) >= time(hour=12):
        timur_pools.append(pool)

desired_pool = sorted(
    timur_pools, key=lambda p: (p['DimensionsSummer']['Length'], p['DimensionsSummer']['Width']), reverse=True)[0]

print(f"{desired_pool['DimensionsSummer']['Length']}x{desired_pool['DimensionsSummer']['Width']}",
      desired_pool['Address'], sep='\n')

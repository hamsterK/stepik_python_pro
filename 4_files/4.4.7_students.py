"""
Вам доступен файл students.json, содержащий список JSON-объектов, которые представляют данные о студентах
некоторого курса:

[
   {
      "name": "Holly-Anne",
      "city": "Abilene",
      "age": 29,
      "progress": 85,
      "phone": "(802) 983-9126"
   },
   ...
]
Под «студентом» мы будем подразумевать один JSON-объект из этого списка. У студента имеются следующие атрибуты:
name — имя
city — город проживания
age — возраст
progress — прогресс по курсу в процентах
phone— контактный номер

Напишите программу, которая определяет студентов, удовлетворяющих следующим условиям:
возраст 18 лет или более
прогресс по курсу 75% или более

Программа должна создать файл data.csv с двумя столбцами — name (имя) и phone (номер), и записать в него данные
выбранных студентов, расположив их в лексикографическом порядке имён. В качестве разделителя в файле data.csv
должна быть использована запятая.

Примечание 1. Гарантируется, что все студенты имеют различные имена.

Примечание 2. Начальная часть файла data.csv выглядит так:

name,phone
Cary,(580) 476-8517
Catarina,(237) 608-2757
Catherin,(876) 215-3666
...
"""

import csv
import json

with open('students.json', 'r', encoding='utf-8') as input_file:
    students = json.load(input_file)
    ok_students = dict()
    for student in students:
        if student['age'] >= 18 and student['progress'] >= 75:
            ok_students[student['name']] = student['phone']

with open('data.csv', 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['name', 'phone'])
    for key, value in sorted(ok_students.items()):
        writer.writerow((key, value))

"""
Вам доступен файл exam_results.csv, который содержит информацию о прошедшем экзамене в некотором учебном заведении.
В первом столбце записано имя студента, во втором — фамилия, в третьем — оценка за экзамен, в четвертом — дата и время
сдачи в формате YYYY-MM-DD HH:MM:SS, в пятом — адрес электронной почты:

name,surname,score,date_and_time,email
Jayson,Edwards,2,2021-11-10 10:00:00,sonnen@yahoo.com
April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
...
Каждый студент имеет право пересдать экзамен два раза, поэтому он может встречаться в исходном файле до трёх раз
с различной оценкой и различными датой и временем сдачи.

Напишите программу, которая для каждого студента определяет его максимальную оценку, а также дату и время ее получения.
Программа должна создать список словарей, каждый из которых содержит следующие пары ключ-значение:

name — имя студента
surname — фамилия студента
best_score — максимальная оценка за экзамен
date_and_time — дата и время получения максимальной оценки в исходном формате
email — адрес электронной почты

Полученный список программа должна записать в файл best_scores.json, причем словари в списке должны быть расположены
в лексикографическом порядке названий электронных почт.

Примечание 1. Если при пересдаче студент получил такую же оценку, что и в прошлый раз, то в качестве даты следует
указать дату пересдачи.

Примечание 3. Начальная часть файла best_scores.json выглядит так:

[
   {
      "name": "Stephen",
      "surname": "Farley",
      "best_score": 3,
      "date_and_time": "2021-11-12 12:00:00",
      "email": "aardo@mac.com"
   },
   {
      "name": "Kaylen",
      "surname": "Horne",
      "best_score": 4,
      "date_and_time": "2021-11-09 11:00:00",
      "email": "aaribaud@att.net"
   },
   ...
]
"""

import csv
import json

with open('exam_results.csv') as exam_file:
    csv_file = csv.DictReader(exam_file)
    results = {}

    for res in sorted(csv_file, key=lambda x: x['date_and_time']):
        res['best_score'] = int(res.pop('score'))
        results[res['email']] = res

with open('best_scores.json', 'w') as write_file:
    json.dump(sorted([result for result in results.values()], key=lambda x: x['email']), write_file, indent=3)
    
"""
У Тимура имеется немало друзей из других городов или стран, которые часто приезжают к нему в гости с целью увидеться
и развлечься. Чтобы не забыть ни об одной встрече, Тимур записывает имена и фамилии друзей в csv файл, дополнительно
указывая для каждого дату и время встречи. Вам доступен этот файл, имеющий название meetings.csv, в котором в первом
столбце записана фамилия, во втором — имя, в третьем — дата в формате DD.MM.YYYY , в четвертом — время в формате HH:MM:

surname,name,meeting_date,meeting_time
Харисов,Артур,15.07.2022,17:00
Геор,Гагиев,14.12.2022,18:00
...
Напишите программу, которая выводит фамилии и имена друзей Тимура, предварительно отсортировав их по дате и времени
встречи от самой ранней до самой поздней. Фамилии и имена должны быть расположены каждые на отдельной строке.

Примечание 1. Начальная часть ответа выглядит так:

Гудцев Таймураз
Харисов Артур
Базиев Герман
...
"""

import csv
from datetime import datetime

d_format = '%d.%m.%Y'
t_format = '%H:%M'

with open('meetings.csv', 'r', encoding='utf-8') as csv_file:
    rows = csv.DictReader(csv_file)
    meetings = list()
    for row in rows:
        meetings.append(row)

for meeting in sorted(meetings, key=lambda x: (datetime.strptime(x["meeting_date"], d_format), datetime.strptime(x["meeting_time"], t_format))):
    print(meeting["surname"], meeting["name"])

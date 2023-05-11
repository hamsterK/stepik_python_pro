"""
Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. Напишите программу, которая определяет самого молодого сотрудника, празднующего свой день рождения в течение ближайших семи дней от текущей даты.

Формат входных данных
На вход программе в первой строке подается текущая дата в формате DD.MM.YYYY, в следующей строке вводится натуральное
число n — количество сотрудников, работающих в организации. В последующих n строках вводятся данные о каждом сотруднике:
 имя, фамилия и дата рождения, разделённые пробелом. Дата рождения указывается в формате DD.MM.YYYY.

Формат выходных данных
Программа должна определить самого молодого сотрудника, празднующего свой день рождения в течение ближайших семи дней,
и вывести его имя и фамилию, разделив пробелом. Если таких сотрудников нет, программа должна вывести текст:
Дни рождения не планируются

Sample Input 1:
14.11.2021
3
Иван Петров 16.11.1995
Петр Сергеев 14.11.1997
Сергей Романов 17.11.1994

Sample Output 1:
Иван Петров
"""

from datetime import datetime, timedelta

current_date = datetime.strptime(input(), '%d.%m.%Y')
employees = list()
for i in range(int(input())):
    employees.append([i for i in input().split()])

employees = list(filter(lambda x:
                        timedelta(days=1) < (datetime.strptime(x[2], '%d.%m.%Y').date().replace(year=current_date.year)
                                             - current_date.date()) <= timedelta(days=7) if datetime.strptime(x[2],
                                                                                                              '%d.%m.%Y').month != 1
                        else timedelta(days=1) < (
                                    datetime.strptime(x[2], '%d.%m.%Y').date().replace(year=current_date.year + 1)
                                    - current_date.date()) <= timedelta(days=7), employees))

if len(employees) >= 1:
    youngest = max(employees, key=lambda x: datetime.strptime(x[2], '%d.%m.%Y'))
    print(f'{youngest[0]} {youngest[1]}')
else:
    print('Дни рождения не планируются')

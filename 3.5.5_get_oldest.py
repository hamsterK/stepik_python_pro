"""
Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. Напишите программу, которая
определяет самого старшего сотрудника из данного списка.

Формат входных данных
На вход программе в первой строке подается натуральное число n — количество сотрудников, работающих в организации.
В последующих n строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом.
Дата рождения указывается в формате DD.MM.YYYY.

Формат выходных данных
Программа должна определить самого старшего сотрудника и вывести его дату рождения, имя и фамилию, разделив пробелом.
Если таких сотрудников несколько, программа должна вывести их дату рождения, а также их количество, разделив пробелом.

Sample Input 1:
3
Иван Петров 01.05.1995
Петр Сергеев 29.04.1995
Сергей Иванов 01.01.1996

Sample Output 1:
29.04.1995 Петр Сергеев

Sample Input 2:
3
Иван Петров 01.05.1995
Петр Сергеев 29.05.1995
Сергей Иванов 01.05.1995

Sample Output 2:
01.05.1995 2
"""

from datetime import datetime
from collections import Counter

employees = list()
for i in range(int(input())):
    employees.append([i for i in input().split()])

oldest = min(employees, key=lambda x: datetime.strptime(x[2], '%d.%m.%Y'))
counts = Counter(i[2] == oldest[2] for i in employees)

if counts[True] > 1:
    print(f'{oldest[2]} {counts[True]}')
else:
    print(f'{oldest[2]} {oldest[0]} {oldest[1]}')

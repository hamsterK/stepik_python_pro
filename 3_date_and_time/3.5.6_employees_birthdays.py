"""
Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. Напишите программу, которая
определяет, в какую из дат родилось больше всего сотрудников.

Формат входных данных
На вход программе в первой строке подается натуральное число n — количество сотрудников, работающих в организации.
В последующих n строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом.
Дата рождения указывается в формате DD.MM.YYYY.

Формат выходных данных
Программа должна вывести дату, в которую наибольшее количество сотрудников отмечает день рождения, в формате DD.MM.YYYY.
Если таких дат несколько, программа должна вывести их все в порядке возрастания, каждую на отдельной строке, в том же
формате.

Sample Input 1:
5
Иван Петров 01.05.1995
Петр Сергеев 29.04.1995
Сергей Романов 01.01.1996
Роман Григорьев 01.01.1996
Григорий Иванов 01.05.1995

Sample Output 1:
01.05.1995
01.01.1996
"""

from datetime import datetime

employees = list()
for i in range(int(input())):
    employees.append([i for i in input().split()])

employees_birthdays = dict()

for i in range(len(employees)):
    if employees[i][2] not in employees_birthdays:
        employees_birthdays[employees[i][2]] = 1
    else:
        employees_birthdays[employees[i][2]] += 1

max_birthdays = max(employees_birthdays, key=employees_birthdays.get)
max_birthdays = employees_birthdays[max_birthdays]

dates_to_print = list()

for key, value in employees_birthdays.items():
    if value == max_birthdays and key not in dates_to_print:
        dates_to_print.append(key)

dates_to_print.sort(key=lambda x: datetime.strptime(x, '%d.%m.%Y'))

print(*dates_to_print, sep='\n')

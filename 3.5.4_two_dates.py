"""
Формат входных данных
На вход программе подаются две даты в формате DD.MM.YYYY — левая и правая границы диапазона соответственно, каждая на
отдельной строке. Гарантируется, что первая дата не больше второй.

Формат выходных данных
Программа должна из указанного диапазона, включая концы, вывести, начиная с даты, у которой сумма дня и месяца нечетная,
каждую третью дату, только если она не понедельник и не четверг. Даты должны быть расположены каждая на отдельной
строке, в формате DD.MM.YYYY.

Sample Input 1:
01.11.2021
10.11.2021

Sample Output 1:
02.11.2021
05.11.2021
"""

from datetime import datetime, timedelta

pattern = '%d.%m.%Y'
date_one = datetime.strptime(input(), pattern)
date_two = datetime.strptime(input(), pattern) + timedelta(days=1)

while (date_one.day + date_one.month) % 2 == 0:
    date_one += timedelta(days=1)

current_date = date_one
while current_date < date_two:
    if (current_date.weekday() != 0) and (current_date.weekday() != 3):
        print(current_date.strftime('%d.%m.%Y'))
    current_date += timedelta(days=3)

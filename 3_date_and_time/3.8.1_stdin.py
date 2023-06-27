"""
Дана последовательность дат. Напишите программу, которая выводит количество дней между максимальной и минимальной датами
данной последовательности.

Формат входных данных
На вход программе подается произвольное количество строк, в каждой строке записана дата в ISO формате (YYYY-MM-DD).

Формат выходных данных
Программа должна вывести единственное число — количество дней между максимальной и минимальной датами введенной
последовательности.

Sample Input 1:
2022-06-15
2022-06-12
2022-06-16
2022-06-30

Sample Output 1:
18
"""

import sys
from datetime import datetime

dates_input = sys.stdin
dates = list()
for i in dates_input:
    dates.append(datetime.strptime(i.strip('\n'), '%Y-%m-%d'))
print((max(dates) - min(dates)).days)
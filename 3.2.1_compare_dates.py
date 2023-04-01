"""
Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.

Формат входных данных
На вход программе подаются две корректные даты в ISO формате (YYYY-MM-DD), каждая на отдельной строке.

Формат выходных данных
Программа должна выбрать из двух введенных дат меньшую и вывести ее в формате DD-MM (YYYY).
"""
from datetime import date

date1 = date.fromisoformat(input())
date2 = date.fromisoformat(input())

print(min(date1, date2).strftime('%d-%m (%Y)'))

# Sample Input:
# 2021-05-12
# 2021-05-04
# Sample Output:
# 04-05 (2021)

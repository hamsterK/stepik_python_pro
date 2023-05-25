"""
Напишите программу, которая принимает на вход время и выводит целое количество секунд, прошедшее с начала суток.

Формат входных данных
На вход программе подается время в формате HH:MM:SS.

Формат выходных данных
Программа должна вывести целое количество секунд, прошедшее с начала суток.

Sample Input 1:
00:01:01

Sample Output 1:
61
"""

from datetime import timedelta, datetime

input_date = datetime.strptime(input(), '%H:%M:%S')

seconds = timedelta(hours=input_date.hour, minutes=input_date.minute, seconds=input_date.second)

print(int(seconds.total_seconds()))

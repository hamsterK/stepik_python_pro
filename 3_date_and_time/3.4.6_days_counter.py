"""
Дана последовательность дат. Напишите программу, которая создает и выводит список, элементами которого являются
неотрицательные целые числа — количество дней между двумя соседними датами последовательности.

Sample Input 2:
06.10.2021 05.10.2021 08.10.2021 09.10.2021 07.10.2021

Sample Output 2:
[1, 3, 1, 2]
"""

from datetime import datetime


def days_counter(list_of_dates):
    if len(list_of_dates) <= 1:
        return list()
    else:
        for i in range(len(list_of_dates)):
            list_of_dates[i] = datetime.strptime(list_of_dates[i], '%d.%m.%Y')
        days_counter_results = list()
        for i in range(len(list_of_dates) - 1):
            days_counter_results.append(abs(list_of_dates[i+1] - list_of_dates[i]).days)
        return days_counter_results


print(days_counter([i for i in input().split(' ')]))

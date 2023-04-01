"""
Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:
start — начальная дата, тип date
end — конечная дата, тип date

Функция должна возвращать количество суббот между датами start и end включительно.
"""

from datetime import date


def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start

    return sum(date.fromordinal(i).weekday() == 5 for i in range(start.toordinal(), end.toordinal() + 1))


date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))
"""
Реализуйте функцию get_all_mondays(), которая принимает один аргумент:

year — натуральное число
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year,
выпадающих на понедельник.

Примечание 1. Например, вызов:
get_all_mondays(2021)

должен вернуть список:
[datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]
"""

import calendar
from datetime import date, timedelta


def get_all_mondays(s_year):
    all_mondays = list()
    first_jan = date(s_year, 1, 1)
    if calendar.weekday(s_year, 1, 1) == 0:
        all_mondays.append(first_jan)
    s_date = first_jan + timedelta(days=7 - first_jan.weekday())
    while s_date.year == s_year:
        all_mondays.append(s_date)
        s_date += timedelta(days=7)
    return all_mondays


print(get_all_mondays(1353))

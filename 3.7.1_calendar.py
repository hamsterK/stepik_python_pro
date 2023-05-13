"""
Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:

year — натуральное число
month — полное название месяца на английском
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.

Примечание 1. Например, вызов:
get_days_in_month(2021, 'December')

должен вернуть список:
[datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ..., datetime.date(2021, 12, 30), datetime.date(2021, 12, 31)]
"""

import datetime
import calendar


def get_days_in_month(year, month):
    month = datetime.datetime.strptime(month, '%B').month
    return [datetime.date(year, month, d) for d in range(1, calendar.monthrange(year, month)[1] + 1)]

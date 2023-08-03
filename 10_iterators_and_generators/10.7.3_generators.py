"""
Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.
"""

from datetime import date, timedelta


def years_days(year):
    current_date = date(year, 1, 1)
    end_date = date(year + 1, 1, 1)

    while current_date < end_date:
        yield current_date
        current_date += timedelta(days=1)


dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))

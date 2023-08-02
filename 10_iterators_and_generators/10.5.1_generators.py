"""
Реализуйте генераторную функцию dates(), которая принимает два аргумента в следующем порядке:

start — дата, тип date
count — натуральное число, по умолчанию имеет значение None
Если count имеет значение None, функция должна возвращать генератор, порождающий последовательность из максимально
допустимого количества дат (тип date), начиная с даты start.

Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий
последовательность из count дат (тип date), начиная с даты start, а затем возбуждающий исключение StopIteration.
"""

from datetime import date, timedelta


def dates(start, count=None):
    while count is None or count > 0:
        yield start
        if start == date.max:
            break
        start = start + timedelta(days=1)
        if count:
            count -= 1


generator = dates(date(2022, 3, 8), 5)

print(*generator)

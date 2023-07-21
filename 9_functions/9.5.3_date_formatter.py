"""
Функция date_formatter() должна возвращать функцию, которая принимает в качестве аргумента дату (тип date) и возвращает
строку с данной датой в формате страны с кодом country_code.
"""

from datetime import datetime
from datetime import date


def date_formatter(country_code):
    def ru_date(today):
        return datetime.strftime(today, '%d.%m.%Y')

    def us_date(today):
        return datetime.strftime(today, '%m-%d-%Y')

    def ca_date(today):
        return datetime.strftime(today, '%Y-%m-%d')

    def br_date(today):
        return datetime.strftime(today, '%d/%m/%Y')

    def fr_date(today):
        return datetime.strftime(today, '%d.%m.%Y')

    def pt_date(today):
        return datetime.strftime(today, '%d-%m-%Y')

    return locals()[f'{country_code}_date']


date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))

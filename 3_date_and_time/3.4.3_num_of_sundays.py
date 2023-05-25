"""
Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:

year — натуральное число, год
Функция должна возвращать количество воскресений в году year.
"""

from datetime import date


def num_of_sundays(selected_year):
    return date(selected_year, 12, 31).strftime('%U')


print(num_of_sundays(2021))

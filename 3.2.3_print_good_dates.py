"""
Тимур считает дату «интересной», если её год совпадает с годом его рождения, а сумма номера месяца и номера дня
равна его возрасту. Год рождения Тимура — 1992, возраст — 29 лет.

Реализуйте функцию print_good_dates(), которая принимает один аргумент:
dates — список дат (тип date)

Функция должна выводить «интересные» даты в порядке возрастания, каждую на отдельной строке,
в формате  month_name DD, YYYY, где month_name — полное название месяца на английском.
"""

from datetime import date


def print_good_dates(dates):
    for i in sorted(dates):
        print(i.strftime("%B %d, %Y")) if i.year == 1992 and i.day + i.month == 29 else None


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)

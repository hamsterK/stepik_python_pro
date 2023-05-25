"""
Реализуйте функцию fill_up_missing_dates(), которая принимает на вход один аргумент:

dates — список строковых дат в формате DD.MM.YYYY
Функция должна возвращать список, в котором содержатся все даты из списка dates, расположенные в порядке возрастания,
а также все недостающие промежуточные даты.

Sample Input 1:
dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
print(fill_up_missing_dates(dates))

Sample Output 1:
['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021']
"""

from datetime import datetime, timedelta


def fill_up_missing_dates(dates):
    pattern = '%d.%m.%Y'
    dates = [datetime.strptime(d, pattern) for d in dates]
    start, end = min(dates), max(dates)
    days = (end - start).days
    return [(start + timedelta(days=i)).strftime(pattern) for i in range(days + 1)]


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))
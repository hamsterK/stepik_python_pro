"""
Напишите программу, которая принимает на вход текущие дату и время и определяет количество минут,
оставшееся до закрытия магазина.
"""

from datetime import datetime, time

pattern = '%d.%m.%Y %H:%M'
visit = datetime.strptime(input(), pattern)

if visit.isoweekday() <= 5 and time(hour=9) <= visit.time() < time(hour=21):
    print((visit.replace(hour=21, minute=0) - visit).seconds // 60)
elif visit.isoweekday() >= 6 and time(hour=10) <= visit.time() < time(hour=18):
    print((visit.replace(hour=18, minute=0) - visit).seconds // 60)
else:
    print('Магазин не работает')
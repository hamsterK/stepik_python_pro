"""
Часы показывают время в формате HH:MM:SS. На этих часах запустили таймер, который прозвенит через n секунд.
Напишите программу, которое определит, какое время будет на часах, когда прозвенит таймер.

Sample Input 1:
09:00:00
90

Sample Output 1:
09:01:30
"""

from datetime import timedelta, datetime

input_time = datetime.strptime(input(), '%H:%M:%S')
timer_seconds = timedelta(seconds=int(input()))

print((input_time + timer_seconds).strftime('%H:%M:%S'))

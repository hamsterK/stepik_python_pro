"""
Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:
funcs — список произвольных функций
arg — произвольный объект

Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила на вычисление значения при
вызове с аргументом arg наименьшее количество времени.
"""

import time


def get_the_fastest_func(funcs, *arg):
    fastest_f = ()
    fastest_f_time = 100000000
    for func in funcs:
        time_start = time.monotonic()
        func(*arg)
        time_end = time.monotonic()
        time_spent = time_end - time_start
        if time_spent < fastest_f_time:
            fastest_f_time, fastest_f = time_spent, func
    return fastest_f

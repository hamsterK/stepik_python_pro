"""
Напишите программу с использованием декоратора, которая переопределяет функцию print() так, чтобы она печатала весь
текст в верхнем регистре.
"""


def print_decorator(func):
    def wrapper(*args, **kwargs):
        args = (str(i).upper() for i in args)
        kwargs = {k: v.upper() for k, v in kwargs.items()}
        func(*args, **kwargs)

    return wrapper


print = print_decorator(print)


print(111, 222, 333, sep='xxx', end='python')
print(111, 222, 333, sep='--', end='\n')
print(111, 222, 333, sep='qqq', end='!')

"""
Напишите программу, которая переопределяет встроенную функцию print() так, чтобы она печатала все переданные
строковые аргументы в верхнем регистре.
"""

old_print = print


def print(*args, sep=' ', end='\n'):
    upper_args = tuple(arg.upper() if type(arg) == str else arg for arg in args)
    sep, end = sep.upper(), end.upper()
    old_print(*upper_args, sep=sep, end=end)


words = ['a', 2, 'b', 3, ['1a', '2a', '3a', '4a'], '5A', True, 8.763, ('python', 'c++')]
print(*words)

# A 2 B 3 ['1a', '2a', '3a', '4a'] 5A True 8.763 ('python', 'c++')

"""
Реализуйте декоратор returns_string, который проверяет, что возвращаемое значение декорируемой функции
принадлежит типу str. Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен
возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""

import functools


def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result
        else:
            raise TypeError
    return wrapper

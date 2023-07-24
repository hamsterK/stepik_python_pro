"""
Реализуйте декоратор ignore_exception, который принимает произвольное количество позиционных аргументов — типов
исключений, и выводит текст:
Исключение <тип исключения> обработано
если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов.

Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.
"""

import functools


def ignore_exception(*exceptions):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
            except exceptions as error:
                print(f'Исключение {error.__class__.__name__} обработано')
            else:
                return value

        return wrapper

    return decorator


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x


f(0)

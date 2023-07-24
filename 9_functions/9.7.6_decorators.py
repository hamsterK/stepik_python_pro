"""
Декоратор должен добавлять строку string к возвращаемому значению декорируемой функции. Если to_the_end имеет значение
True, строка string добавляется в конец, если False — в начало.
"""

import functools


def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if to_the_end:
                return result + string
            else:
                return string + result
        return wrapper
    return decorator

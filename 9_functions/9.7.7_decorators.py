"""
Декоратор должен вызывать декорируемую функцию times раз.
"""

import functools


def repeat(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator

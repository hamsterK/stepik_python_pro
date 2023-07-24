"""
Декоратор должен выполнять повторную попытку вызова декорируемой функции, если во время ее выполнения возникает ошибка.
Декоратор должен вызывать ее до тех пор, пока не исчерпает количество попыток times, после чего должен возбуждать
исключение MaxRetriesException.
"""

import functools


class MaxRetriesException(Exception):
    pass


def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = times
            while retries > 0:
                try:
                    value = func(*args, **kwargs)
                    return value
                except:
                    retries -= 1
            raise MaxRetriesException

        return wrapper

    return decorator

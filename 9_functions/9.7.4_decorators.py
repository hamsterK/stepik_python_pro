"""
Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию,
являются положительными целыми числами.

Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:
TypeError, если аргумент не является целым числом
ValueError, если аргумент является целым числом, но отрицательным или равным нулю
"""


def takes_positive(func):
    def wrapper(*args, **kwargs):
        if any(not isinstance(i, int) for i in args):
            raise TypeError
        elif any(i <= 0 for i in args) or any(i <= 0 for i in kwargs.values()):
            raise ValueError
        else:
            value = func(*args, **kwargs)
            return value
    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

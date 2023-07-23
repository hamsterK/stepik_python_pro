"""
Реализуйте декоратор exception_decorator, который возвращает кортеж (value, 'Функция выполнилась без ошибок'),
если декорируемая функция завершила свою работу без ошибок, где value — возвращаемое значение декорируемой функции
кортеж (None, 'При вызове функции произошла ошибка'), если при выполнении декорируемой функции возникла ошибка
"""


def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            value = func(*args, **kwargs)
            return value, 'Функция выполнилась без ошибок'
        except TypeError:
            return None, 'При вызове функции произошла ошибка'
    return wrapper


@exception_decorator
def f(x):
    return x ** 2 + 2 * x + 1


print(f(7))

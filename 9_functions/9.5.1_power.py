"""
Функция power() должна возвращать функцию, которая принимает в качестве аргумента целое число x и возвращает
значение x в степени degree.
"""


def power(degree):
    def get_power(x):
        return x ** degree
    return get_power


square = power(2)
print(square(5))

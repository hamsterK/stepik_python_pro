"""
Функция должна возвращать итератор, генерирующий бесконечную последовательность случайных целых чисел в диапазоне
от left до right включительно.
"""

from random import randint


def random_numbers(left, right):
    def get_random_number():
        return randint(left, right)
    return iter(get_random_number, right + 1)


iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))

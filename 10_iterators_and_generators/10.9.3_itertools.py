"""
Функция должна возвращать индекс первого элемента итерируемого объекта iterable, который больше number. Если таких
элементов нет, функция должна вернуть число −1.
"""


def first_largest(iterable, number):
    for index, elem in enumerate(iterable):
        if elem > number:
            return index
    return -1


numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))

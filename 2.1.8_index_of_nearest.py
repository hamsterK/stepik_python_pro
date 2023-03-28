"""
Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:
1. numbers — список целых чисел
2. number — целое число

Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс.
Если список numbers пуст, функция должна вернуть число −1.

Примечание 1. Если в функцию передается список, содержащий несколько чисел,
одновременно являющихся ближайшими к искомому числу,
функция должна возвращать наименьший из индексов ближайших чисел.
"""


def index_of_nearest(numbers, number):
    if len(numbers) == 0:
        return -1
    else:
        current_number, current_position = numbers[0], 0
        for i in range(len(numbers)):
            if abs(numbers[i] - number) < abs(current_number - number):
                current_number, current_position = numbers[i], i
        return current_position


print(index_of_nearest([7, 13, 3, 5, 18], 0))

print(index_of_nearest([9, 5, 3, 2, 11], 4))

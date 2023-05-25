"""
Реализуйте функцию get_biggest(), которая принимает один аргумент:
numbers — список целых неотрицательных чисел

Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers.
Если список numbers пуст, функция должна вернуть число −1.

Примечание 1. Рассмотрим первый тест со списком чисел [1, 2, 3]
Наибольшим возможным числом является 321.
"""


def get_biggest(numbers):
    if len(numbers) == 0:
        return -1
    numbers.sort(key=lambda x: int(str(x)[0]), reverse=True)
    if numbers[0] == 0:
        return 0
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if int(str(numbers[j]) + str(numbers[j - 1])) > int(str(numbers[j - 1]) + str(numbers[j])):
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
    answer = ''.join([str(i) for i in numbers])
    return answer


print(get_biggest([1, 2, 3]))

print(get_biggest([61, 228, 9, 3, 11]))

print(get_biggest([7, 71, 72]))

print(get_biggest([]))

print(get_biggest([0, 0, 0, 0, 0, 0]))

print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))

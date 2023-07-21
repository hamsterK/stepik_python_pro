"""
Функция должна сортировать по неубыванию список чисел values, делая при этом приоритетной группу чисел из group,
которая должна следовать первой.
"""


def sort_priority(numbers, group):
    numbers.sort(key=lambda x: (x not in group, x))


data = list(range(0, 100, 5))
sort_priority(data, {1, 90, 95, 25, 55, 64})

print(data)

# [25, 55, 90, 95, 0, 5, 10, 15, 20, 30, 35, 40, 45, 50, 60, 65, 70, 75, 80, 85]

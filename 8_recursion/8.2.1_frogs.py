"""
В первый год в пруду живет 77 лягушек. Каждый год из пруда вылавливают 30 лягушек, а оставшиеся размножаются, и их
становится в три раза больше.
Реализуйте функцию number_of_frogs() с использованием рекурсии, которая принимает один аргумент:
year — натуральное число
Функция должна возвращать единственное число — количество лягушек в пруду в году year.
"""


def number_of_frogs(year):
    if year == 1:
        return 77
    else:
        frogs_last_year = number_of_frogs(year - 1)
        frogs_this_year = 3 * (frogs_last_year - 30)
        return frogs_this_year


print(number_of_frogs(2))

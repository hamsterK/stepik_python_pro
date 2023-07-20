"""
Функция должна возвращать сумму чисел (типы int и float), находящихся в списке elems, игнорируя все нечисловые объекты.
Если в списке elems нет чисел, функция должна вернуть число 0.
"""


def numbers_sum(elems):
    """Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет."""
    filtered_data = list(filter(lambda x: isinstance(x, int or float), elems))
    return sum(filtered_data)


print(numbers_sum([1, '2', 3, 4, 'five']))

"""
Функция должна возвращать кортеж, в котором первым элементом является индекс минимального элемента в списке data,
вторым — индекс максимального элемента в списке data. Если список data пуст, функция должна вернуть значение None.
"""

def get_min_max(data):
    if len(data) == 0:
        return None
    return data.index(min(data)), data.index(max(data))


data = [2, 3, 8, 1, 7]

print(get_min_max(data))

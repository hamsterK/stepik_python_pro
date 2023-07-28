"""
Функция должна возвращать кортеж, в котором первым элементом является минимальный элемент итерируемого объекта iterable,
вторым — максимальный элемент итерируемого объекта iterable. Если итерируемый объект iterable пуст, функция должна
вернуть значение None.
"""


def get_min_max(iterable):
    iterable = iter(iterable)
    try:
        smallest = largest = next(iterable)
    except:
        return None
    for elem in iterable:
        if elem < smallest:
            smallest = elem
        if elem > largest:
            largest = elem
    return smallest, largest


iterable = iter(range(10))

print(get_min_max(iterable))

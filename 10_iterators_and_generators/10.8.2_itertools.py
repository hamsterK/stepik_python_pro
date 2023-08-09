"""
Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных аргументов, каждый из которых
является итерируемым объектом.

Функция должна возвращать итератор, генерирующий последовательность из элементов всех переданных итерируемых объектов:
сначала первый элемент первого итерируемого объекта, затем первый элемент второго итерируемого объекта, и так далее;
после второй элемент первого итерируемого объекта, затем второй элемент второго итерируемого объекта, и так далее.
"""


def roundrobin(*args):
    iterators = [iter(arg) for arg in args]
    while iterators:
        next_elements = []
        for it in iterators:
            try:
                next_elements.append(next(it))
            except StopIteration:
                pass
        if len(next_elements) > 0:
            yield from next_elements
        else:
            break


numbers = [1, 2, 3]
letters = iter('beegeek')
print(*roundrobin(numbers, letters))

print(*roundrobin('abc', 'd', 'ef'))

numbers = iter([1, 2, 3])
nones = iter([None, None, None, None])
print(*roundrobin(numbers, nones))


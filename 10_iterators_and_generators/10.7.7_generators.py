"""
Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной
элемент итерируемого объекта iterable, а также следующий за ним элемент:
(<очередной элемент>, <следующий элемент>)

Для последнего элемента следующим считается значение None.
"""


def pairwise(iterables):
    if isinstance(iterables, list) and len(iterables) == 0:
        return list()
    iterables = iter(iterables)
    prev_element = None
    try:
        prev_element = next(iterables)
        while True:
            next_element = next(iterables)
            yield prev_element, next_element
            prev_element = next_element
    except StopIteration:
        yield prev_element, None


numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))

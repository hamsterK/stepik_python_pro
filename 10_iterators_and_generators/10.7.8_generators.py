"""
Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной
элемент итерируемого объекта iterable, а также предыдущий и следующий за ним элементы:

(<предыдущий элемент>, <очередной элемент>, <следующий элемент>)
Для первого элемента предыдущим считается значение None, для последнего элемента следующим считается так же
значение None.
"""


def around(iterables):
    if isinstance(iterables, list) and len(iterables) == 0:
        return list()
    iterables = iter(iterables)
    prev_element = None
    try:
        current_element = next(iterables)
        while True:
            next_element = next(iterables)
            yield prev_element, current_element, next_element
            prev_element, current_element = current_element, next_element
    except StopIteration:
        yield prev_element, current_element, None


iterator = iter('hey')

print(*around(iterator))

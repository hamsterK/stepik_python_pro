"""
Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной
элемент итерируемого объекта iterable, а также предшествующий ему элемент:
(<очередной элемент>, <предыдущий элемент>)

Для первого элемента предыдущим считается значение None.
"""


def with_previous(iterable):
    prev_element = None
    for element in iterable:
        yield element, prev_element
        prev_element = element


iterator = iter('stepik')

print(*with_previous(iterator))

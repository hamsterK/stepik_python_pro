"""
Функция должна возвращать генератор, порождающий каждый элемент всех переданных итерируемых объектов: сначала все
элементы первого итерируемого объекта, затем второго, и так далее.
"""


def all_together(*args):
    for i in args:
        answer = (j for j in i)
        yield from answer


objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))

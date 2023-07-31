"""
Итератор класса Cycle должен циклично генерировать последовательность элементов итерируемого объекта iterable.
"""


class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.iterable):
            self.index = 0
        return self.iterable[self.index]


cycle = Cycle('be')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

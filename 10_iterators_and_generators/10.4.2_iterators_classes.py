"""
Итератор класса Square должен генерировать последовательность из n чисел, каждое из которых является квадратом
очередного натурального числа, а затем возбуждать исключение StopIteration.
"""


class Square:
    def __init__(self, n):
        self.n = n
        self.value = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.value <= self.n:
            self.value += 1
            return (self.value - 1) ** 2
        raise StopIteration


squares = Square(10)

print(list(squares))

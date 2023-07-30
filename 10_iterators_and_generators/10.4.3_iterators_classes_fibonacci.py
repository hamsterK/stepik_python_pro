"""
Реализуйте класс Fibonacci, порождающий итераторы, конструктор которого не принимает никаких аргументов.

Итератор класса Fibonacci должен генерировать бесконечную последовательность чисел Фибоначчи, начиная с 1.
"""


class Fibonacci:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.curr
        self.curr, self.prev = self.curr + self.prev, self.curr
        return result


fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

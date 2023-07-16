"""
Реализуйте функцию zip_longest(), которая принимает переменное количество позиционных аргументов, каждый из которых
является списком, и один необязательный именованный аргумент fill, имеющий значение по умолчанию None.
"""


def zip_longest(*args, fill=None):
    max_len = len(max(args, key=len))
    for i, arg in enumerate(args):
        if len(arg) < max_len:
            args[i].extend([fill] * (max_len - len(arg)))
    return list(zip(*args))


data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))
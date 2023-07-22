"""
Функция должна изменять переданный список, циклически сдвигая элементы списка на step шагов, и возвращать значение None.
Если step является положительным числом, сдвиг происходит вправо, если отрицательным — влево.
"""


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    move = len(numbers) - step % len(numbers)
    numbers[:] = numbers[move:] + numbers[:move]
"""
Реализуйте функцию transpose() с использованием функции zip(), которая принимает один аргумент:
matrix — матрица произвольной размерности
Функция должна возвращать транспонированную матрицу matrix.
"""

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in transpose(matrix):
    print(row)

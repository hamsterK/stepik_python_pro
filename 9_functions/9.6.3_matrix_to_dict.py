"""
Функция должна возвращать словарь, ключом в котором является номер строки матрицы, а значением
— список элементов этой строки.
"""


def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    answer = dict()
    for i in range(len(matrix)):
        answer[i + 1] = matrix[i]
    return answer


matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

print(matrix_to_dict(matrix))

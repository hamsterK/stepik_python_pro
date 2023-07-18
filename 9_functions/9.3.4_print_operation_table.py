"""
Функция должна составлять и выводить таблицу из rows строк и cols столбцов, в которой элемент со строкой n и столбцом m
имеет значение operation(n, m).
"""


def print_operation_table(operation, rows, cols):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            print(operation(i, j), end=' ')
        print()


print_operation_table(pow, 5, 4)



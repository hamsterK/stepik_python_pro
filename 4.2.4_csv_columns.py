"""
Реализуйте функцию csv_columns(), которая принимает один аргумент:

filename — название csv файла, например, data.csv
Функция должна возвращать словарь, в котором ключом является название столбца файла filename, а значением — список
элементов этого столбца.

Примечание 1. Гарантируется, что в передаваемом в функцию файле разделителем является запятая, при этом кавычки
не используются.

Примечание 2. Гарантируется, что у передаваемого в функцию файла первая строка содержит названия столбцов.

Примечание 3. Например, если бы файл exam.csv имел вид:

name,grade
Timur,5
Arthur,4
Anri,5

то следующий вызов функции csv_columns():

csv_columns('exam.csv')

должен был бы вернуть:

{'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}
"""

import csv


def csv_columns(filename):
    with open(filename, 'r', encoding='utf-8') as csv_file:
        rows = csv.DictReader(csv_file)
        final_dict = dict()
        for row in rows:
            for key, value in row.items():
                if key not in final_dict:
                    final_dict[key] = list()
                    final_dict[key].append(value)
                else:
                    final_dict[key].append(value)


'''
Other option:

import csv


def csv_columns(filename):
    columns_dict = {}
    with open(filename, encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for line in reader:
            for name in reader.fieldnames:
                columns_dict[name] = columns_dict.get(name, []) + [line[name]]

    return columns_dict
'''

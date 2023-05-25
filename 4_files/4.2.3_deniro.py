"""
Вам доступен файл deniro.csv, каждый столбец которого содержит либо только числа, либо только слова:

Machete,2010,72
Marvin's Room,1996,80
Raging Bull,1980,97
...
Напишите программу, которая сортирует содержимое данного файла по указанному столбцу (input). Причем данные должны быть
отсортированы в порядке возрастания чисел, если столбец содержит числа, и в лексикографическом порядке слов, если
столбец содержит слова.
"""

import csv

with open('deniro.csv', 'r', encoding='utf-8') as csv_file:
    rows = csv.reader(csv_file)
    rows_list = list()
    for row in rows:
        rows_list.append(row)
row_to_sort = int(input()) - 1

try:
    rows_list.sort(key=lambda x: int(x[row_to_sort]))
except ValueError:
    rows_list.sort(key=lambda x: x[row_to_sort])

for row in rows_list:
    print(f'{row[0]},{row[1]},{row[2]}')

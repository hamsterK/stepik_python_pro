"""
Напишите программу, которая принимает на вход описание одного объекта в формате JSON и выводит все пары ключ-значение
этого объекта.

Формат входных данных
На вход программе подается корректное описание одного объекта в формате JSON.

Формат выходных данных
Программа должна вывести все пары ключ-значение введенного объекта, разделяя ключ и значение двоеточием, каждую на
отдельной строке. Если значением ключа является список, то все его элементы должны быть выведены через запятую.

Sample Input 1:

{"size": 36, "style": "bold", "name": "text1", "alignment": "center"}

Sample Output 1:

size: 36
style: bold
name: text1
alignment: center
"""

import sys
import json

data = sys.stdin.read()
data_to_print = json.loads(data)

for i in data_to_print:
    if isinstance(data_to_print[i], list):
        items = [str(item) for item in data_to_print[i]]  # Convert items to strings
        print(f'{i}: {", ".join(items)}')
    else:
        print(f'{i}: {data_to_print[i]}')

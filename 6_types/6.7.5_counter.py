"""
Вам доступен текстовый файл pythonzen.txt, содержащий текст на английском языке:

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...
Напишите программу, которая определяет, сколько раз встречается каждая буква в этом тексте. Буквы и их количество
должны выводиться в лексикографическом порядке, каждая на отдельной строке, в следующем формате:
<буква>: <количество>

Примечание 1. Начальная часть ответа выглядит так:

a: 53
b: 21
...
"""

from collections import Counter
import re

with open('pythonzen.txt', 'r', encoding='utf-8') as file:
    counter = Counter()
    regex = re.compile('[^a-zA-Z]')
    for line in file.readlines():
        counter.update(regex.sub('', line.lower()))
    print(*[f'{key}: {value}' for key, value in sorted(counter.items())], sep='\n')


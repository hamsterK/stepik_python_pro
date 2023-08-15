"""
Напишите программу, которая находит во фрагменте HTML-страницы все гиперссылки и выводит их составляющие —
адресные части и указатели.
"""

import sys
import re

text = sys.stdin.read()
pattern = r'<a href="(.+)">(.+)</a>'

for address, pointer in re.findall(pattern, text):
    print(f'{address}, {pointer}')

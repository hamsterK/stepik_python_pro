"""
Напишите программу, определяющую:
количество строк, в которых bee встречается в качестве подстроки не менее двух раз
количество строк, в которых geek встречается в качестве слова хотя бы один раз
"""

import re
import sys

bee_counter, geek_counter = 0, 0

for line in map(str.rstrip, sys.stdin):
    match_1 = re.findall(r'bee', line)
    match_2 = re.search(r'\bgeek\b', line)
    if len(match_1) >= 2:
        bee_counter += 1
    if match_2:
        geek_counter += 1

print(bee_counter, geek_counter, sep='\n')

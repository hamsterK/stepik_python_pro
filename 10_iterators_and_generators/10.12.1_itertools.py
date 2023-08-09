"""
Программа должна вывести все перестановки символов данной строки без дубликатов в алфавитном порядке,
каждую на отдельной строке.
"""

from itertools import permutations, combinations

answer = set(permutations(input().strip()))
for i in sorted(answer):
    print(*i, sep='')




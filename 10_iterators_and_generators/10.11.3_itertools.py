"""
Напишите программу, которая группирует слова по их длине.
"""

from itertools import groupby


words = input().split()
group_iter = groupby(sorted(words, key=lambda x: len(x)), key=lambda x: len(x))

for key, values in group_iter:
    word_list = ', '.join(sorted(values))
    print(f'{key} -> {word_list}')


# Sample Input 1:
#
# hi never here my blue
# Sample Output 1:
#
# 2 -> hi, my
# 4 -> blue, here
# 5 -> never

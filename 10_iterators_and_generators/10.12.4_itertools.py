"""
Программа, которая выводит все обозначения полей шахматной доски в алфавитном порядке через пробел.
"""

from itertools import product
from string import ascii_lowercase

for card in product(ascii_lowercase[:8], range(1, 9)):
    print(*card, sep='', end=' ')

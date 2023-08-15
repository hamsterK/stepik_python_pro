"""
На вход программе подается одна строка, содержащая строчные латинские буквы, числа и скобки.
Программа должна вывести строку, в которой раскрыты все умножения с учетом приоритетности операций.
"""

import re


def expand_multiplications(s):
    while re.search(r'\d+\([^()]+\)', s):
        s = re.sub(r'(\d+)\(([^()]+)\)', lambda m: m.group(2) * int(m.group(1)), s)
    return s


input_string = input()
expanded_string = expand_multiplications(input_string)
print(expanded_string)

# bbbb10(2(a))bbb

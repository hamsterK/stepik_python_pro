"""
Напишите программу, которая принимает строку текста и заменяет в ней все ключевые слова на <kw>.


"""

import re
import keyword


def normalize_string(string):
    for kw in keyword.kwlist:
        string = re.sub(fr'\b{kw}\b', r'<kw>', string, flags=re.IGNORECASE)
    return string

print(normalize_string(input()))

# True, assert, as, false, or, Import

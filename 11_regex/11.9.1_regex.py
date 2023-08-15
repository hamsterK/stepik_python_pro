"""
Функция должна разбивать строку string на подстроки, используя в качестве разделителей строки из списка delimiters,
и возвращать полученный результат в виде списка.
"""

import re


def multiple_split(string, delimiters):
    dels = '|'.join(map(re.escape, delimiters))
    return re.split(dels, string)


print(multiple_split('stepik_python-dima*roma*jenya-timur__arthur', ['_', '*', '#', '@']))

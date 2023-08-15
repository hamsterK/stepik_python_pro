"""
Функция должна создавать из фразы phrase аббревиатуру в верхнем регистре и возвращать её.
"""

from re import findall


def abbreviate(phrase):
    regex = r'\b\w|[A-Z]'
    return ''.join(map(str.upper, findall(regex, phrase)))


print(abbreviate('javaScript object notation'))
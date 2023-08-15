"""
Функция должна возвращать новое название файла с нормализованным расширением — jpg.
"""

import re


def normalize_jpeg(filename):
    return re.sub(r'\.[jJ][pP][eE]?[gG]$', r'.jpg', filename, re.IGNORECASE)


print(normalize_jpeg('stepik.jpeg.jpeg'))

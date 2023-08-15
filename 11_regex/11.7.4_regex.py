"""
Программа должна найти в введенном фрагменте HTML-страницы все теги и вывести их, указав для каждого соответствующие
атрибуты. Теги вместе со всеми атрибутами должны быть расположены каждый на отдельной строке.
"""

import sys
from re import findall

mydict = {}

for line in sys.stdin:
    for k in findall(r'\<([a-zA-Z0-9]+)', line):
        val = findall(fr'{k} (\b[a-zA-Z-]*\=\"[^\<]*\")', line)
        mydict.update({k: set(findall(f"([a-zA-Z-]*)\=", ''.join(val)))})

[print(k + ':', ', '.join(sorted(v))) for k, v in sorted(mydict.items())]

# <p><a href="https://stepik.org">Stepik</a></p>
# <div class="catalog"><a href="https://stepik.org/catalog">Study hard. Teach harder</a></div>

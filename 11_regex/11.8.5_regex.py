"""
Программа должна в введенной строке заменить все повторяющиеся рядом стоящие слова на одно слово
и вывести полученный результат.
"""

import re

text = input()
result = list(set(re.findall(r'\b\w+\b', text)))

for word in result:
    text = re.sub(fr'\b{word}\W*(\W*{word}\W*)*\W*{word}\b', fr'{word}', text)

print(text)

# hi, hi, hi, hello, hello, HELLO, HELLO, HELLO, HELLO, hello!

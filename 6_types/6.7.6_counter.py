"""
Дана последовательность слов. Напишите программу, которая выводит наиболее часто встречаемое слово в этой
последовательности.

Формат входных данных
На вход программе подается последовательность слов, разделенных пробелом.

Формат выходных данных
Программа должна определить наиболее часто встречаемое слово в введенной последовательности и вывести его
в нижнем регистре.

Sample Input 1:
Черешня Вишня Арбуз малина Малинаz клубникА Арбуз Банан вишня малина

Sample Output 1:
малина
"""

from collections import Counter

words = [i.lower() for i in input().split(' ')]
print(Counter(words).most_common(1)[0][0])

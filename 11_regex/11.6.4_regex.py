"""
Популярность
В онлайн-школе BEEGEEK мы всегда следим за тем, насколько растет наша популярность. Для этого мы собираем публикации
из различных соцсетей, которые содержат вхождения строки beegeek в нижнем регистре. Мы оцениваем публикацию:
в 3 балла, если она начинается и заканчивается строкой beegeek
в 2 балла, если она только начинается или только заканчивается строкой beegeek
в 1 балл, если она содержит строку beegeek только внутри
в 0 баллов, если она не содержит строку beegeek
"""

import re
import sys

pattern = r'\b\_\d+[A-Za-z]*\_?\b'
points = 0
for article in map(str.rstrip, sys.stdin):
    if re.match(r'^beegeek.*beegeek$', article):
        points += 3
    elif re.match(r'(^beegeek.*)|.*beegeek$', article):
        points += 2
    elif re.search(r'beegeek', article):
        points += 1
print(points)

# hi, beegeek
# beegeek is an awesome place for programmers
# beegeek rocks, rocks beegeek
# i think beegeek is a great place to hangout

"""
Вам доступен набор телефонных номеров, имеющих следующие форматы:
<код страны>-<код города>-<номер>
<код страны> <код города> <номер>
в котором код страны и код города представлены последовательностями от одной до трех цифр включительно, а номер —
последовательностью от четырех до десяти цифр включительно. Между кодом страны, кодом города и номером используется
разделитель, которым служит либо символ дефис, либо пробел, причем одновременно оба вида разделителя в одном номере
присутствовать не могут.

Напишите программу, которая принимает произвольное количество телефонных номеров и для каждого выводит отдельно его код
страны, код города и номер.
"""

import re
import sys

pattern = r"(?P<country>\d{1,3})([ -]?)(?P<city>\d{1,3})\2(?P<number>\d{4,10})"
for number in map(str.rstrip, sys.stdin):
    match = re.fullmatch(pattern, number)
    groups = match.groupdict()
    print(f"Код страны: {groups['country']}, Код города: {groups['city']}, Номер: {groups['number']}")

# 1 877 2638277
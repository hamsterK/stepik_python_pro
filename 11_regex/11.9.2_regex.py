"""
Программа должна вывести сумму всех натуральных чисел в введенной строке, находящихся в диапазоне индексов от a
(включительно) до b (не включительно).
"""

import re

a, b = [int(i) for i in input().split()]
string = input()

regex_obj = re.compile('\d+')
numbers = regex_obj.findall(string, pos=a, endpos=b)
numbers = [int(num) for num in numbers]
print(sum(numbers))

# 0 5
# 11:20 a.m. - 12:00 p.m

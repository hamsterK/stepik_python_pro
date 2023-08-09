"""
Напишите программу, которая генерирует в системе счисления n.
"""

from itertools import product


def generate_numbers(base, length):
    digits = '0123456789ABCDEF'[:base]

    for num_tuple in product(digits, repeat=length):
        num_str = ''.join(num_tuple)
        yield num_str


base = int(input())
length = int(input())

numbers = generate_numbers(base, length)
for num in numbers:
    print(num, end=' ')

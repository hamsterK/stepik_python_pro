"""
Реализуйте функцию count_occurences(), которая принимает два аргумента в следующем порядке:

word — слово
words — последовательность слов, разделенных пробелом
Функция должна определять, сколько раз слово word встречается в последовательности words, и возвращать полученный
результат.

Примечание 1. Функция должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.
"""

from collections import Counter


def count_occurences(word, words):
    counter1 = Counter(words.lower().split())
    return counter1[word.lower()]


word = 'python'
words = 'Python Conferences python training python events'

print(count_occurences(word, words))
"""
Анаграммы — это слова, которые состоят из одинаковых букв. Например:
адаптер — петарда

Реализуйте функцию group_anagrams(), которая принимает один аргумент:
words — список слов
Функция должна группировать в кортежи слова из списка words, являющиеся анаграммами, и возвращать список полученных
кортежей.
"""

from itertools import groupby


def group_anagrams(words):
    sorted_words = sorted(words, key=lambda x: sorted(x))
    group = groupby(sorted_words, key=lambda x: sorted(x))
    res = []
    for key, words in group:
        res.append(tuple(words))
    return res
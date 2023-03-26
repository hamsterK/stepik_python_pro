def filter_anagrams(word, words):
    return list(filter(lambda x: sorted([*x]) == sorted([*word]), words))


print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))

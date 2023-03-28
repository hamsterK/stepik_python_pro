"""
Реализуйте функцию spell(), которая принимает произвольное количество позиционных аргументов-слов и возвращает словарь,
ключи которого — первые буквы слов, а значения — максимальные длины слов на эту букву.

Примечание 1. Если в функцию не передается ни одного аргумента, функция должна возвращать пустой словарь.

Примечание 2. Функция должна игнорировать регистр слов, при этом в результирующий словарь должны попасть именно буквы в
нижнем регистре.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию, но не код, вызывающий ее.
"""


def spell(*words_list):
    letters = dict()
    for word in words_list:
        word = word.lower()
        if word[0] not in letters:
            letters[word[0]] = int(len(word))
        elif letters.get(word[0]) < len(word):
            letters[word[0]] = int(len(word))
    return letters


words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))

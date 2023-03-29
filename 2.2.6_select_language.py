"""
Зачастую переводить сериалы, не теряя изначальный смысл, невозможно, особенно за счет игр слов.
Сумасшедший режиссер хочет снять сериал, в котором бы в целях эксперимента задействовал как можно больше языков,
чтобы пользоваться красотой каждого из них. Тем не менее если задействовать слишком много языков,
то сериал станет непонятен абсолютно всем, поэтому режиссер достает случайных людей на улице и спрашивает их,
какие языки они знают, таким образом он будет использовать языки которые знают все из них.

Напишите программу, которая определяет, какие языки будут использоваться в сериале.

Формат входных данных
На вход программе в первой строке подается число n — количество людей, которых донимает режиссер.
В каждой из следующих n строк через запятую и пробел указывается список языков, которые знает человек.

Формат выходных данных
Программа должна вывести список языков для сериала в лексикографическом порядке.
Если такой список составить нельзя, необходимо вывести текст:
Сериал снять не удастся
"""


def select_language():
    languages_spoken = list()
    answer = list()
    for i in range(int(input())):
        languages_spoken.append(input().split(', '))
    for language in languages_spoken[0]:
        flag = True
        for i in range(1, len(languages_spoken)):
            if language not in languages_spoken[i]:
                flag = False
        if flag:
            answer.append(language)
    if len(answer) == 0:
        print('Сериал снять не удастся')
    else:
        print(*sorted(answer), sep=', ')


select_language()

# Sample Input:
# 6
# испанский, португальский, эсперанто, французский
# французский, испанский, эсперанто
# португальский, эсперанто, французский, испанский
# французский, английский, болгарский, испанский, эсперанто
# эсперанто, английский, русский, испанский, французский
# python, испанский, эсперанто, латышский, польский, французский
# Sample Output:
# испанский, французский, эсперанто

# other solution:
# n = int(input())
# l = [set(input().split(', ')) for _ in range(n)]
# intersect = set.intersection(*l)
# if intersect:
#     print(*sorted(intersect), sep=', ')
# else:
#     print('Сериал снять не удастся')

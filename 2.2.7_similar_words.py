"""
Напишите программу, которая находит все схожие слова для заданного слова. Слова называются схожими, если имеют
одинаковое количество и расположение гласных букв. При этом сами гласные могут различаться.

Формат входных данных
На вход программе подается одно слово, записанное в первой строке, затем натуральное число n — количество слов
для сравнения и n строк со словами.

Формат выходных данных
Программа должна вывести все схожие слова для заданного слова, сохранив их исходный порядок следования.

Примечание 1. После последней гласной в начальном и проверяемом слове может быть любое количество согласных.

Примечание 2. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) и 21 согласная буква
(б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).
"""


def similar_words():
    vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    main_word = input()
    main_word_mock = ''
    for i in range(len(main_word)):
        if main_word[i] in vowels:
            main_word_mock += str(i)
    other_words = [input() for i in range(int(input()))]
    for word in other_words:
        word_mock = ''
        for i in range(len(word)):
            if word[i] in vowels:
                word_mock += str(i)
        if word_mock == main_word_mock:
            print(word)


similar_words()

# Sample Input:
# весть
# 3
# месть
# гость
# лань
# Sample Output:
# месть
# гость
# лань
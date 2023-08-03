"""
Функция должна возвращать генератор, порождающий последовательность всех непустых строк файла file с убранным символом
переноса строки \n. Если строка содержит более 25 символов, она заменяется многоточием ....
"""


def nonempty_lines(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                if len(line) > 25:
                    yield '...'
                else:
                    yield line

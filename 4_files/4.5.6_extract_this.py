"""
Реализуйте функцию extract_this(), которая принимает один или более аргументов в следующем порядке:

zip_name — название zip архива, например, data.zip
*args — переменное количество позиционных аргументов, каждый из которых является названием некоторого файла
Функция должна извлекать файлы *args из архива zip_name в папку с программой. Если в функцию не передано ни одного
названия файла для извлечения, то функция должна извлечь все файлы из архива.

Примечание 1. Например, следующий вызов функции

extract_this('workbook.zip', 'earth.jpg', 'exam.txt')
должен извлечь из архива workbook.zip файлы earth.jpg и exam.txt в папку с программой.
"""

from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if len(args) > 0:
            for i in args:
                zip_file.extract(i)
        else:
            zip_file.extractall()

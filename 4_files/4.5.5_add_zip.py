"""
Вам доступен набор различных файлов, названия которых представлены в списке file_names. Также вам доступен архив
files.zip. Дополните приведенный ниже код, чтобы он добавил в архив files.zip только те файлы из списка file_names,
объем которых не превышает 100 байт.

Примечание 1. Получить объем файла в байтах позволяет функция getsize() из модуля os.path. Данная функция принимает
в качестве аргумента путь к файлу и возвращает размер указанного файла в байтах.

Например, вычислить объем архива files.zip в байтах и сохранить его в переменную size можно следующим образом:

import os.path

size = os.path.getsize('files.zip')
"""

from zipfile import ZipFile
import os.path

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

with ZipFile('../3_date_and_time/files.zip', mode='w') as zip_file:
    for i in file_names:
        if os.path.getsize(i) <= 100:
            zip_file.write(i)
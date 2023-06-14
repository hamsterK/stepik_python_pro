"""
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит
названия файлов из этого архива, которые были созданы или изменены позднее 2021-11-30 14:22:00. Названия файлов
должны быть расположены в лексикографическом порядке, каждое на отдельной строке.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Начальная часть ответа выглядит так:

countries.json
data_sample.csv
"""

import zipfile
from datetime import datetime

with zipfile.ZipFile('workbook.zip') as archive:
    files = list()
    for file in archive.infolist():
        if datetime(*file.date_time) > datetime(2021, 11, 30, 14, 22) and file.is_dir() is False:
            files.append(file.filename.split('/')[-1])

print(*sorted(files), sep='\n')

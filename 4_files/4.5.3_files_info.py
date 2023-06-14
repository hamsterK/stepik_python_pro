"""
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия
всех файлов из этого архива в лексикографическом порядке, указывая для каждого его дату изменения, а также объем до
и после сжатия, в следующем формате:

<название файла>
  Дата модификации файла: <дата изменения>
  Объем исходного файла: <объем до сжатия> байт(а)
  Объем сжатого файла: <объем после сжатия> байт(а)

Между данными о двух файлах должна располагаться пустая строка.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Начальная часть ответа выглядит так (в качестве отступов используйте два пробела):

Alexandra Savior – Crying All the Time.mp3
  Дата модификации файла: 2021-11-30 13:27:02
  Объем исходного файла: 5057559 байт(а)
  Объем сжатого файла: 5051745 байт(а)

Hollow Knight Silksong.exe
  Дата модификации файла: 2013-08-22 08:20:06
  Объем исходного файла: 805992 байт(а)
  Объем сжатого файла: 494930 байт(а)
...
"""

import zipfile
from datetime import datetime

with zipfile.ZipFile('workbook.zip') as archive:
    files = dict()
    format = '%Y-%m-%d %H:%M:%S'
    for file in archive.infolist():
        if file.is_dir() is False:
            name = file.filename.split('/')[-1]
            files[name] = dict()
            files[name]['date'] = datetime.strftime(datetime(*file.date_time), format)
            files[name]['before'] = file.file_size
            files[name]['after'] = file.compress_size

for file_name, file_data in sorted(files.items()):
    print(f'{file_name}\n  Дата модификации файла: {file_data["date"]}\n  Объем исходного файла: {file_data["before"]} '
          f'байт(а)\n  Объем сжатого файла: {file_data["after"]} байт(а)', sep='\n')
    print()

"""
Вам доступен текстовый файл files.txt, содержащий информацию о файлах. Каждая строка файла содержит три значения,
разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:

cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...
Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы,
и выводит полученные группы файлов, указывая для каждой ее общий объем. Группы должны быть расположены
в лексикографическом порядке названий расширений, файлы в группах — в лексикографическом порядке их имен.

Примечание 1. Например, если бы файл files.txt имел вид:

input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4 KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB

то программа должна была бы вывести:

boy.bmp
mario.bmp
----------
Summary: 3 MB

input.txt
output.txt
temp.txt
----------
Summary: 8 KB

data.zip
scratch.zip
----------
Summary: 1 GB

где Summary — общий объем файлов группы.

Примечание 2. Гарантируется, что все имена файлов содержат расширение.

Примечание 3. Общий объем файлов группы записывается в самых крупных (максимально возможных) единицах измерения
с округлением до целых. Другими словами, сначала следует определить суммарный объем всех файлов группы,
скажем, в байтах, а затем перевести полученное значение в самые крупные (максимально возможные) единицы измерения.
Примеры перевода:

1023 B -> 1023 B
1300 B -> 1 KB
1900 B -> 2 KB

Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB
"""


def convert(size):
    if size >= 1024**3:
        return f'{round(size / 1024**3)} GB'
    elif size >= 1024**2:
        return f'{round(size / 1024**2)} MB'
    elif size >= 1024:
        return f'{round(size / 1024)} KB'
    else:
        return f'{round(size)} B'


with open('files.txt', encoding='utf-8') as file:
    units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3}
    data, file_names, file_size = [], {}, {}

    for line in file:
        data.append(line.split()[0].split('.') + line.split()[1:])
    data.sort(key=lambda x: x[1])

    for info in data:
        file_names[info[1]] = file_names.get(info[1], []) + [info[0]]
        file_size[info[1]] = file_size.get(info[1], 0) + units[info[3]] * int(info[2])

    for key, values in file_names.items():
        for value in sorted(values):
            print(value + '.' + key)
        print('----------', 'Summary: ' + convert(file_size[key]) + '\n', sep='\n')

"""
Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя. В первом столбце записано
измененное имя пользователя, во втором — адрес электронной почты, в третьем — дата и время изменения. При этом email
пользователь менять не может, только имя:

username,email,dtime
rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
...
Напишите программу, которая отбирает из файла name_log.csv только самые свежие записи для каждого пользователя и
записывает их в файл new_name_log.csv. В файле new_name_log.csv первой строкой должны быть заголовки столбцов такие же,
как в файле name_log.csv. Логи в итоговом файле должны быть расположены в лексикографическом порядке названий
электронных ящиков пользователей.

Примечание 1. Для части пользователей в исходном файле запись только одна, и тогда в итоговый файл следует записать
только ее, для некоторых пользователей есть несколько записей с разными именами.

Например, пользователь с электронной почтой c3po@gmail.com несколько раз менял имя:

C=3PO,c3po@gmail.com,16/11/2021 17:10
C3PO,c3po@gmail.com,16/11/2021 17:15
C-3PO,c3po@gmail.com,16/11/2021 17:24
Из этих трех записей в итоговый файл должна быть записана только одна — самая свежая:

C-3PO,c3po@gmail.com,16/11/2021 17:24
"""

from datetime import datetime
import csv

with open('name_log.csv', 'r', encoding='utf-8') as csv_file:
    rows = csv.DictReader(csv_file)
    data = list()
    d_format = '%d/%m/%Y %H:%M'
    for row in rows:
        if not any(dictionary.get('email') == row['email'] for dictionary in data):
            data.append(row)
        else:
            for index, dictionary in enumerate(data):
                if dictionary.get('email') == row['email']:
                    if datetime.strptime(row['dtime'], d_format) > datetime.strptime(data[index]['dtime'], d_format):
                        data[index] = row


with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as output_file:
    columns = ['username', 'email', 'dtime']
    writer = csv.DictWriter(output_file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(sorted(data, key=lambda x: x['email']))

"""
Вам доступен файл titanic.csv, который содержит данные о пассажирах, присутствовавших на борту парохода Титаник.
В первом столбце указана единица, если пассажир выжил, и ноль в противном случае, во втором столбце записано полное имя
пассажира, в третьем — пол, в четвертом — возраст:

survived;name;sex;age
0;Mr. Owen Harris Braund;male;22
1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
...
Напишите программу, которая выводит имена выживших пассажиров, которым было менее 18 лет, каждое на отдельной строке.
Причем сначала должны быть расположены имена всех пассажиров мужского пола, а затем — женского, имена же непосредственно
в мужском и женском списках должны быть расположены в своем исходном порядке.
"""

import csv

with open('titanic.csv', 'r', encoding='utf-8') as csv_file:
    rows = csv.DictReader(csv_file, delimiter=';')
    survived = dict()
    for row in rows:
        if row['survived'] == '1' and float(row['age']) < 18:
            survived[row['name']] = row['sex']
    for key, value in sorted(survived.items(), key=lambda x: x[1], reverse=True):
        print(key)



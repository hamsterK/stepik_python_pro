import csv

def csv_columns(filename):
    with open(filename, 'r', encoding='utf-8'):
        rows = csv.DictReader(filename)
        for row in rows:
            print(row)

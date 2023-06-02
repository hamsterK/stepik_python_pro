import json
import csv

with open('playgrounds.csv', 'r', encoding='utf-8') as input_file:
    reader = csv.reader(input_file, delimiter=';')
    data = {}
    next(reader)
    for row in reader:
        object_name, adm_area, district, address = row
        if adm_area not in data:
            data[adm_area] = {}
        if district not in data[adm_area]:
            data[adm_area][district] = []
        data[adm_area][district].append(address)

with open('addresses.json', 'w', encoding='utf-8') as output_file:
    json.dump(data, output_file, indent=3, ensure_ascii=False)

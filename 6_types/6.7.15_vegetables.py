import csv
import json

vegetables = dict()
for file in ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']:
    with open(file, 'r', encoding='utf-8') as csv_file:
        next(csv_file)
        for v_name, month1, month2, month3 in csv.reader(csv_file):
            vegetables[v_name] = vegetables.get(v_name, 0) + int(month1) + int(month2) + int(month3)

with open('prices.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    total_sum = int()
    for key, value in data.items():
        total_sum += vegetables[key] * value

print(total_sum)

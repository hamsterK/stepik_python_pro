"""
Вам доступен файл salary_data.csv, который содержит анонимную информацию о зарплатах сотрудников в различных компаниях.
В первом столбце записано название компании, а во втором — зарплата очередного сотрудника:

company_name;salary
Atos;135000
ХайТэк;24400
Philax;128600
Инлайн Груп;43900
IBS;70600
Oracle;131600
Atos;91000
...
Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее сотрудников и выводит их названия
каждое на отдельной строке. Если две компании имеют одинаковые средние зарплаты, они должны быть расположены
в лексикографическом порядке их названий.
"""

import csv

with open('salary_data.csv', 'r', encoding='utf-8') as csv_file:
    rows = csv.DictReader(csv_file, delimiter=';')
    companies = set()
    companies_list = list()
    companies_salaries = list()
    for row in rows:
        companies_list.append(row)
        companies.add(row['company_name'])
    for i in companies:
        counter = 0
        salary_sum = 0
        for j in companies_list:
            if j['company_name'] == i:
                counter += 1
                salary_sum += int(j['salary'])
        companies_salaries.append([i, salary_sum // counter])
    companies_salaries.sort(key=lambda x: x[1])
for i in companies_salaries:
    print(i[0])


# second option:

# import csv
# with open('salary_data.csv', encoding='utf-8') as file:
#     dic={}
#     dic2={}
#     lst=csv.DictReader(file,delimiter=';')
#     for row in lst:
#         dic[row['company_name']]=dic.get(row['company_name'],0)+int(row['salary'])
#         dic2[row['company_name']]=dic2.get(row['company_name'],0)+1
#     for k,v in dic.items():
#         dic[k]=v/dic2[k]
#     dic=sorted(dic.items(), key=lambda x: x[1])
#     [print(k) for k,v in dic]

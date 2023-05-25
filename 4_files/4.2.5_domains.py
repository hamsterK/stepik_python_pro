"""
Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса.
В первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:

first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...
Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:

domain,count
rambler.ru,24
iCloud.com,29
...
где в первом столбце записано название почтового домена, а во втором — количество пользователей, использующих
данный домен. Домены в файле должны быть расположены в порядке возрастания количества их использований, при совпадении
количества использований — в лексикографическом порядке.
"""

import csv
import re

with open('data.csv', 'r', encoding='utf-8') as csv_file:
    rows = csv.DictReader(csv_file)
    domains_list = dict()
    for row in rows:
        selected_email = re.search(r'(?<=@).*', row['email'])
        selected_email = selected_email.group()
        if selected_email not in domains_list:
            domains_list[selected_email] = 1
        else:
            domains_list[selected_email] += 1

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file)
    sorted_domains = list()
    writer.writerow(['domain', 'count'])
    for key, value in sorted(domains_list.items()):
        sorted_domains.append(([key, value]))
    for row in sorted(sorted_domains, key=lambda x: x[1]):
        writer.writerow(row)

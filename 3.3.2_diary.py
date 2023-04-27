from datetime import datetime


def transform_data(date_info):
    return datetime.strptime(date_info[:17], '%d.%m.%Y; %H:%M')


with open('diary.txt') as file:
    diary = file.read().split('\n\n')

print(*sorted(diary, key=lambda x: transform_data(x)), sep='\n\n')

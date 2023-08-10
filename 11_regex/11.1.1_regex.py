import re


def is_phone_number(phone):
    return re.search(r'7-\d{3}-\d{3}-\d{2}-\d{2}', phone) or re.search(r'8-\d{3}-\d{4}-\d{4}', phone)


def get_all_numbers(text):
    for i in text.split():
        if is_phone_number(i):
            yield i.rstrip(',.').lstrip('+')


txt = input()

print(*list(get_all_numbers(txt)), sep='\n')

# Тимур: 7-ddd-ddd-dd-dd, Сослан: 8-ddd-dddd-dddd, Артур: 7-123-123-11-22,,,, Дима: 8-123-123-11-22, Анри: 8-123-1231-1221...... Гвидо: 7-123-1231-1221, 7-123-13-181-22, 8-1237-131-1221

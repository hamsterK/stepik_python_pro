"""
Назовем пароль хорошим, если: его длина равна 9 или более символам, в нем присутствуют большие и маленькие буквы любого
алфавита, в нем имеется хотя бы одна цифра.

Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:
string — произвольная строка

Функция должна возвращать True, если строка string представляет собой хороший пароль, или False в противном случае.
"""


def is_good_password(string):
    return len(string) >= 9 and any(char.isdigit() for char in string) and any(char.islower() for char in string) \
           and any(char.isupper() for char in string)


print(is_good_password('41157082'))

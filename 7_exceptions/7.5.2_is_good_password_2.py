"""
Назовем пароль хорошим, если его длина равна 9 или более символам, в нем присутствуют большие и маленькие буквы любого
алфавита, в нем имеется хотя бы одна цифра.

Реализуйте функцию is_good_password() в стиле EAFP, которая принимает один аргумент:
string — произвольная строка

Функция должна возвращать True, если строка string представляет собой хороший пароль, или возбуждать исключение:
LengthError, если его длина меньше 9 символов
LetterError, если в нем отсутствуют буквы или все буквы имеют одинаковый регистр
DigitError, если в нем нет ни одной цифры
"""


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    if not any(char.isupper() for char in string) or not any(char.islower() for char in string) or not any(char.isalpha() for char in string):
        raise LetterError
    if not any(char.isdigit() for char in string):
        raise DigitError
    return True


try:
    print(is_good_password('sjkdfsjkdfhjksdfhjkSDFSDAFSADFSADfsdajf'))
except Exception as err:
    print(type(err))

import sys


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
    if not any(char.isupper() for char in string) or not any(char.islower() for char in string) or not any(
            char.isalpha() for char in string):
        raise LetterError
    if not any(char.isdigit() for char in string):
        raise DigitError
    return True


passwords = [line.strip() for line in sys.stdin]

i = 0
password_ok = False
while i < len(passwords) and not password_ok:
    try:
        if is_good_password(passwords[i]):
            print('Success!')
            password_ok = True
    except PasswordError as err:
        print(type(err).__name__)
        i += 1

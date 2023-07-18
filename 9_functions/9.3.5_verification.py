def verification(login, password, success, failure):
    if not any(elem.isalpha() and ord(elem) in range(65, 123) for elem in password):
        failure(login, 'в пароле нет ни одной буквы')
    elif not any(elem.isupper() and ord(elem) in range(65, 123) for elem in password):
        failure(login, 'в пароле нет ни одной заглавной буквы')
    elif not any(elem.islower() and ord(elem) in range(65, 123) for elem in password):
        failure(login, 'в пароле нет ни одной строчной буквы')
    elif not any(elem.isdigit() for elem in password):
        failure(login, 'в пароле нет ни одной цифры')
    else:
        success(login)


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)

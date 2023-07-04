def get_id(names, name):
    if type(name) is not str:
        raise TypeError('Имя не является строкой')
    if not (name[0].isupper() and name[1:-1].islower() and name.isalpha()):
        raise ValueError('Имя не является корректным')
    return len(names) + 1

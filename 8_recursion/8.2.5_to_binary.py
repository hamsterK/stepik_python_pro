def to_binary(number):
    if number == 0:
        return '0'
    elif number == 1:
        return '1'
    else:
        if number % 2:
            return to_binary(number // 2) + '1'
        else:
            return to_binary(number // 2) + '0'


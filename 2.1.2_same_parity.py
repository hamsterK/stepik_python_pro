def same_parity(numbers):
    if len(numbers) > 0:
        parity = numbers[0] % 2
        return list(filter(lambda x: x % 2 == parity, numbers))
    else:
        return list()


print(same_parity([6, 0, 67, -7, 10, -20]))

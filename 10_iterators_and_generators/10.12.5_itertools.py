from itertools import product


def password_gen():
    for password in product(range(10), repeat=3):
        yield ''.join(map(str, password))


passwords = password_gen()

print(next(passwords))
print(next(passwords))
print(next(passwords))

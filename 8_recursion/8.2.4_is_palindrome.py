"""
Реализуйте функцию is_palindrome() с использованием рекурсии, которая принимает один аргумент:
string — произвольная строка
Функция должна возвращать значение True, если переданная строка является палиндромом, или False в противном случае.
"""


def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] != string[-1]:
            return False
        else:
            return is_palindrome(string[1:-1])


print(is_palindrome('stepik'))
print(is_palindrome('level'))

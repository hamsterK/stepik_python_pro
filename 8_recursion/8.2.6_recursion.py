"""
Напишите программу с использованием рекурсии, которая принимает на вход число n и вычитает из него число 5, пока оно
не перестанет быть положительным, а затем прибавляет к нему число 5, пока оно снова не станет равным n.
"""


def plus_minus_five(number):
    print(number)
    if number > 0:
        plus_minus_five(number - 5)
        print(number)


plus_minus_five(int(input()))

"""
Реализуйте функцию is_power() с использованием рекурсии, которая принимает один аргумент:
number — натуральное число

Функция должна возвращать значение True, если number является степенью числа 2, или False в противном случае.

Sample Input 1:
print(is_power(512))

Sample Output 1:
True

Sample Input 2:
print(is_power(15))

Sample Output 2:
False
"""


def is_power(number: int, ch=2) -> bool:
    if number == 1 or number == ch:
        return True
    else:
        if ch <= number:
            return is_power(number, ch * 2)
        else:
            return False


print(is_power(512))
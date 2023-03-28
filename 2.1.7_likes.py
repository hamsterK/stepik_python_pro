"""
В различных социальных сетях существуют системы лайков, которые в зависимости от количества людей,
оценивших запись, показывают соответствующую информацию.

Реализуйте функцию likes(), которая принимает один аргумент:
names — список имён

Функция должна возвращать строку, содержание которой зависит от количества имён в списке names.

Примечание 1. Имена в формируемой и возвращаемой функцией строке должны располагаться в своем исходном порядке.

Примечание 2. Обратите внимание, что если в передаваемом в функцию списке более трех имен,
то явно указываются лишь первые два из них.
"""


def likes(names):
    if len(names) == 0:
        return "Никто не оценил данную запись"
    elif len(names) == 1:
        return f"{names[0]} оценил(а) данную запись"
    elif len(names) == 2:
        return f"{names[0]} и {names[1]} оценили данную запись"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
    else:
        return f"{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись"


print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))

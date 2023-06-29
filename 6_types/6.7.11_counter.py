"""
Вам доступна переменная data, содержащая Counter словарь. Дополните приведенный ниже код, чтобы он добавил этому
словарю два атрибута:

min_values() — функция, которая возвращает список элементов, имеющих наименьшее значение
max_values() — функция, которая возвращает список элементов, имеющих наибольшее значение

Обе функции не должны принимать никаких аргументов.

Примечание 1. Элементом словаря будем считать кортеж (ключ, значение).

Примечание 2. Элементы словаря в возвращаемых функциями списках должны располагаться в своем исходном порядке.

Примечание 3. Функции data.min_values() и data.max_values() должны учитывать содержимое словаря. Например, если
в словарь data будет добавлена новая пара ключ-значение, то и в возвращаемых функциями списках данные ключ и значение
должны присутствовать.
"""

from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.__dict__['min_values'] = lambda: [(key, value) for key, value in data.items() if value == min(data.values())]
data.__dict__['max_values'] = lambda: [(key, value) for key, value in data.items() if value == max(data.values())]

print(data.max_values())
print(data.min_values())

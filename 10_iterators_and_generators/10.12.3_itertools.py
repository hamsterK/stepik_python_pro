"""
Программа должна определить какие предметы из представленного набора следует взять, чтобы собрать рюкзак с максимальной
ценностью предметов внутри, соблюдая при этом весовое ограничение рюкзака, и вывести названия полученных предметов
в лексикографическом порядке, каждое на отдельной строке. Если рюкзак не позволяет взять ни один предмет, программа
должна вывести текст:
Рюкзак собрать не удастся
"""

from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [
    Item('Обручальное кольцо', 7, 49000),
    Item('Мобильный телефон', 200, 110000),
    Item('Ноутбук', 2000, 150000),
    Item('Ручка Паркер', 20, 37000),
    Item('Статуэтка Оскар', 4000, 28000),
    Item('Наушники', 150, 11000),
    Item('Гитара', 1500, 32000),
    Item('Золотая монета', 8, 140000),
    Item('Фотоаппарат', 720, 79000),
    Item('Лимитированные кроссовки', 300, 80000)
]

max_weight = int(input())

best_combination = []
best_total_price = 0

for i in range(1, len(items) + 1):
    for combo in combinations(items, r=i):
        total_mass = sum(item.mass for item in combo)
        total_price = sum(item.price for item in combo)
        if total_mass <= max_weight and total_price > best_total_price:
            best_total_price = total_price
            best_combination = combo

if not best_combination:
    print("Рюкзак собрать не удастся")
else:
    for item in sorted(best_combination, key=lambda x: x.name):
        print(item.name)

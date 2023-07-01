from collections import ChainMap
from collections import Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)
order = Counter(input().split(','))
max_length = len(max(order, key=lambda x: len(x)))

for ingredient, quantity in sorted(order.items()):
    print(f'{ingredient} {(max_length - len(ingredient)) * " "}x {quantity}')
total = f'ИТОГ: {sum([ingredients[ingredient] * quantity for ingredient, quantity in order.items()])}р'

if len(total) > len('-' * (max_length + 4)):
    print('-' * len(total))
else:
    print('-' * (max_length + 3 + len(str(max(order.values())))))

print(total)
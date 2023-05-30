"""
Дима очень хочет поесть, но денег у него мало. Помогите ему определить самый дешевый продукт, а также магазин,
в котором он продается. Вам доступен файл prices.csv, который содержит информацию о ценах продуктов в различных
магазинах. В первом столбце записано название магазина, а в последующих — цена на соответствующий товар в этом магазине:

Магазин;Творог;Гречка;Рис;Бородинский хлеб;Яблоки;Пельмени;Овсяное печенье;Спагетти;Печеная фасоль;Мороженое;Фарш;
Вареники;Картофель;Батончик
Пятерочка;69;133;129;83;141;90;72;123;149;89;88;106;54;84
Магнит;102;87;95;75;109;112;97;82;101;134;69;61;141;79
...
Напишите программу, которая определяет и выводит самый дешевый продукт и название магазина, в котором он продается,
в следующем формате:

<название продукта>: <название магазина>

Если имеется несколько самых дешевых товаров, то следует вывести тот товар, чье название меньше в лексикографическом
сравнении. Если один товар продается в нескольких магазинах по одной минимальной цене, то следует вывести тот магазин,
чье название меньше в лексикографическом сравнении.
"""

import csv


def replace_cheap_product():
    cheap_product['store'] = current_store
    cheap_product['price'] = int(value)
    cheap_product['item'] = key


with open('prices.csv', 'r', encoding='utf-8') as input_file:
    reader = csv.DictReader(input_file, delimiter=';')
    columns = reader.fieldnames
    rows = list(reader)

    cheap_product = {'store': 'x', 'price': 9999, 'item': 'x'}
    cheapest_store = 'x'
    for i in rows:
        current_store = ''
        for key, value in i.items():
            if key == 'Магазин':
                current_store = value
            elif int(value) < cheap_product['price']:
                replace_cheap_product()
            elif int(value) == cheap_product['price']:
                if cheap_product['store'] < current_store:
                    replace_cheap_product()

    print(f'{cheap_product["item"]}: {cheap_product["store"]}')

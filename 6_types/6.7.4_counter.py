"""
Тимур живет в мире, в котором цена товара определяется как сумма Unicode кодов букв его названия. Буквенным обозначением данной валюты являются две заглавные латинские буквы UC. Например, ручка в его мире стоит:

1088
+
1091
+
1095
+
1082
+
1072
=
5428
U
C
1088+1091+1095+1082+1072=5428UC
Тимур составляет список покупок, но так как на его клавиатуре перестал работать блок с цифрами, то вместо указания
количества товара числом, он добавляет его в список столько раз, сколько планирует купить. Все товары Тимур записывает
в нижнем регистре через запятую.

Напишите программу, которая группирует одинаковые товары из данного списка покупок и определяет стоимость каждой группы.

Формат входных данных
На вход программе подается последовательность товаров, разделенных запятой без пробелов.

Формат выходных данных
Программа должна сгруппировать одинаковые товары, определить общую стоимость каждой группы и вывести полученный
результат. Товары должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:

<товар>: <цена за единицу товара> UC x <количество товаров в группе> = <общая стоимость группы> UC

Примечание 1. Программа должна добавлять нужное количество пробелов, если название товара имеет меньшую длину,
чем другие.

Sample Input 2:
рубашка,футболка,футболка,брюки,футболка,сырный соус,рубашка,носки,рубашка

Sample Output 2:
брюки      : 5425 UC x 1 = 5425 UC
носки      : 5422 UC x 1 = 5422 UC
рубашка    : 7574 UC x 3 = 22722 UC
сырный соус: 10896 UC x 1 = 10896 UC
футболка   : 8669 UC x 3 = 26007 UC
"""

from collections import Counter

shopping_list = Counter(input().split(','))
item_max_length = len(max(shopping_list, key=lambda x: len(x)))
print(*[f'{key}{" " * (item_max_length - len(key))}: {sum(ord(i) for i in key.replace(" ", ""))} UC x {value} = '
        f'{value * sum(ord(i) for i in key.replace(" ", ""))} UC' for key, value in sorted(shopping_list.items())], sep='\n')
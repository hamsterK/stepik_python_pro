"""
Тимур составляет список покупок, но так как на его клавиатуре перестал работать блок с цифрами, то вместо указания
количества товара числом, он добавляет его в список столько раз, сколько планирует купить. Все товары Тимур записывает
в нижнем регистре через запятую.

Напишите программу, которая выводит все товары из данного списка покупок, указывая для каждого его количество.

Sample Input 1:
лимон,лимон,лимон,груша,банан,банан,киви,киви,киви,киви

Sample Output 1:
банан: 2
груша: 1
киви: 4
лимон: 3
"""

from collections import Counter

shopping_list = Counter(input().split(','))
print(*[f'{key}: {value}' for key, value in sorted(shopping_list.items())], sep='\n')
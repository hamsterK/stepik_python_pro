"""
Дана последовательность неотрицательных целых чисел. Напишите программу, которая выводит те числа,
которые встречаются в данной последовательности более одного раза.

Формат входных данных
На вход программе подается строка, содержащая целые неотрицательные числа, разделенные пробелом.

Формат выходных данных
Программа должна вывести те числа, которые встречаются в данной строке более одного раза, разделяя их пробелом.
Числа должны быть расположены в порядке возрастания и не должны повторяться.
"""

def repeated_numbers(numbers):
    numbers_counter = dict()
    for i in numbers:
        numbers_counter[i] = numbers_counter.get(i, 0) + 1
    for i in sorted(numbers_counter):
        if numbers_counter[i] > 1:
            print(i, end=' ')


repeated_numbers([int(i) for i in input().split()])

# Sample Input:
# 4 8 0 3 4 2 0 3
# Sample Output:
# 0 3 4

# alternative solution:
#
# nums = [int(i) for i in input().split()]
# print(*sorted(filter(lambda i: nums.count(i) > 1, set(nums))))

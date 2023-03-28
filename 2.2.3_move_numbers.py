"""
Дана последовательность натуральных чисел от 1 до n. Напишите программу, которая сначала располагает
в обратном порядке часть элементов этой последовательности от элемента с номером X до элемента с номером Y,
а затем от элемента с номером A до элемента с номером B.
"""

def move_numbers():
    amount, a, b, c, d =[int(i) - 1 for i in input().split()]
    numbers = [i for i in range(1, amount + 2)]
    counter_1, counter_2 = 0, 0
    for i in range(a, b + 1):
        numbers[i] = b + 1 - counter_1
        counter_1 += 1
    temp_numbers = [numbers[i] for i in range(c, d + 1)]
    for i in range(d, c - 1, -1):
        numbers[i] = temp_numbers.pop(0)
    print(*numbers)


move_numbers()

# Sample Input:
# 9 3 6 5 8
# Sample Output:
# 1 2 6 5 8 7 3 4 9

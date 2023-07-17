f_x = input()
a, b = [int(i) for i in input().split()]
data = list()

for i in range(a, b + 1):
    x = i
    data.append(eval(f_x))

print(f'Минимальное значение функции {f_x} на отрезке [{a}; {b}] равно {min(data)}\n'
      f'Максимальное значение функции {f_x} на отрезке [{a}; {b}] равно {max(data)}')

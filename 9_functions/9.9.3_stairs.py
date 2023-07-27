"""
Функция должна возвращать единственное число — количество способов, которыми можно забраться на n-ую ступень.
Путь начинается с первой ступени, подниматься можно исключительно на одну, три или четыре ступени.
"""

from functools import lru_cache


@lru_cache()
def ways(n: int) -> int:
    if n == 1:
        return 1
    elif n < 1:
        return 0
    elif n > 4:
        return ways(n - 1) + ways(n - 3) + ways(n - 4)
    elif n > 3:
        return ways(n - 1) + ways(n - 3)
    elif n > 1:
        return ways(n - 1)


print(ways(5))

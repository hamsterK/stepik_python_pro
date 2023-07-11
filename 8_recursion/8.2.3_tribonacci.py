"""
Последовательность Трибоначчи – последовательность натуральных чисел, где каждое последующее число является суммой трех
предыдущих.
"""


def tribonacci(n, memo={}):
    if n == 0:
        return 0
    elif n == 1 or n == 2 or n == 3:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo)
        memo[n] = result
        return result


print(tribonacci(7))

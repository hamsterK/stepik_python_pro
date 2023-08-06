from itertools import pairwise


def max_pair(iterable):
    return max(map(sum, pairwise(iterable)))


iterator = iter([5, 6, 4, 3, 2, 2])

print(max_pair(iterator))

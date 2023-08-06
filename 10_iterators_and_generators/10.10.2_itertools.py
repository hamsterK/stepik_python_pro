from itertools import pairwise


def is_rising(iterable):
    elements = pairwise(iterable)
    return all(map(lambda x: x[1] > x[0], elements))


iterator = iter(list(range(100, 200)))

print(is_rising(iterator))
from functools import lru_cache
import sys


@lru_cache(typed=False)
def my_func(word):
    a = list(word)
    return ''.join(sorted(a))


for i in sys.stdin:
    print(my_func(i.strip()))

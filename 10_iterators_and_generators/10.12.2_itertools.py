"""
Дополните приведенный ниже код, чтобы он вывел количество способов, которыми можно приобрести книгу стоимостью 100$.
"""

from itertools import combinations

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
all_options = set()

for i in range(1, 16):
    new_combo = list(combinations(wallet, r=i))
    for combo in new_combo:
        if sum(combo) == 100:
            all_options.add(combo)

print(len(all_options))

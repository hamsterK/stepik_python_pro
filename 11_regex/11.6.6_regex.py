"""
Программа должна определить, в скольких введенных строках содержится строка beegeek в произвольном регистре, и вывести
полученный результат.
"""

import re
import sys

beegeek_counter = 0

for line in map(str.rstrip, sys.stdin):
    match = re.findall(r'beegeek', line, re.IGNORECASE)
    if match:
        beegeek_counter += 1

print(beegeek_counter)

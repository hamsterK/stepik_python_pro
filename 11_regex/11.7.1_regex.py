"""
Программа должна определить, сколько раз данное слово встречается как подслово в введенном тексте,
и вывести полученный результат.
"""

import re

sentence, word = [input() for i in range(2)]
print(len(re.findall(fr'\B{word}\B', sentence)))

# thdbakru rubabadjso babadirnid iehedba  ibebibeb duabafbf
# ba

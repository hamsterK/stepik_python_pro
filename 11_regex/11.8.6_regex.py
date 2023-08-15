"""
Программа должна удалить все комментарии из введенного кода.
"""

import re
import sys

regex = r'\n#.*?$|' \
        r'\s*""".*?"""|' \
        r'\n? *#.*?$'

s = sys.stdin.read()
print(re.sub(regex, '', s, flags=re.S | re.M))

# """hello everyone
# welcome to my project"""
#
# import math  # importing a useful math module
#
# # let's take a look at some functions
#
# def circle_area(radius):
#     """coming soon"""
#     return math.pi * r ** 2  # my favorite formula
#
# def triangle_area(base, height):
#     """the function takes
#     the base and height
#     of a triangle and
#     returns its area"""
#     return 0.5 * base * height

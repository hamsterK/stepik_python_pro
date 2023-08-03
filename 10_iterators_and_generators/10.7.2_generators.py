"""
Функция должна возвращать генератор, порождающий последовательность чисел, содержащихся в диапазонах ranges.
"""


def parse_ranges(ranges):
    for i in ranges.split(','):
        answer = (j for j in range(int(i.split('-')[0]), int(i.split('-')[1]) + 1))
        yield from answer


print(*parse_ranges('1-2,4-4,8-10'))
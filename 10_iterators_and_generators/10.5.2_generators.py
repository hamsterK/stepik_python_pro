"""
Функция flatten()
Реализуйте генераторную функцию flatten(), которая принимает один аргумент:

nested_list — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь, также
являются либо целые числа, либо списки; вложенность может быть произвольной
"""


def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, int):
            yield item
        else:
            yield from flatten(item)


generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)

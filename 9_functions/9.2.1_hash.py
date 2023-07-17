"""
Функция должна возвращать словарь, ключом в котором является хеш-значение объекта из списка objects, а значением
— сам объект. Если хеш-значения некоторых объектов совпадают, их следует объединить в список.
"""


def hash_as_key(objects):
    result = {}
    for i in objects:
        if hash(i) in result:
            if not isinstance(result[hash(i)], list):
                result[hash(i)] = [result[hash(i)], i]
            else:
                result[hash(i)].append(i)
        else:
            result[hash(i)] = i
    return result


# data = [1, 2, 3, 4, 5, 5]
data = [(1, 2, 3), (1, 2, 3), (0, 0, 0), 10, (144, 75, 60), 20, 30]

print(hash_as_key(data))

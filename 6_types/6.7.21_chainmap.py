from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    if key not in chainmap:
        return None
    elif from_left:
        return chainmap[key]
    else:
        for dictionary in reversed(chainmap.maps):
            if key in dictionary:
                return dictionary[key]


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))
print(get_value(chainmap, 'name', False))
print(get_value(chainmap, 'age'))

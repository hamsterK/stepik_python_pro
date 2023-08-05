def txt_to_dict():
    """
    Возвращает генератор, порождающий последовательность словарей, каждый из
    которых содержит информацию об очередной планете из файла planets.txt, а
    именно ее название, диаметр, массу и орбитальный период.
    """
    with open('planets.txt', 'r', encoding='utf-8') as text_file:
        info = text_file.read().split('\n\n')
        planet_info = (i.split('\n') for i in info)
        planets = ((tuple(pair.split(' = ')) for pair in planet) for planet in planet_info)
        dict_planets = (dict(planet) for planet in planets)
        yield from dict_planets


planets = txt_to_dict()

print(*planets)

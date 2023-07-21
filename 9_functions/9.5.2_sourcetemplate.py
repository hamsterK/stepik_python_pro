"""
Функция sourcetemplate() должна возвращать функцию, которая принимает произвольное количество именованных аргументов
и возвращает url адрес, объединенный со строкой запроса, сформированной из переданных аргументов. При вызове
без аргументов она должна возвращать исходный url адрес без изменений.
"""


def sourcetemplate(url):
    def load(**kwargs):
        params = '&'.join([f'{key}={value}' for key, value in sorted(kwargs.items())])
        if len(kwargs) > 0:
            return f'{url}?{params}'
        else:
            return f'{url}'
    return load


url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))

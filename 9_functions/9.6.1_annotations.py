"""
Функция должна возвращать словарь, содержащий имя ученика по ключу name и его самую высокую оценку по ключу top_grade.
"""


def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    name = grades['name']
    return {'name': name, 'top_grade': max(grades['grades'])}


info = {'name': 'Timur', 'grades': [30, 57, 99]}

print(top_grade(info))

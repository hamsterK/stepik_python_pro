"""
Вам доступен именованный кортеж Student, который содержит данные об ученике. Первым элементом именованного кортежа
является фамилия ученика, вторым — имя, третьим — класс. Также доступен список students, содержащий эти кортежи.

Код выводит наиболее часто встречаемое имя среди учеников из данного списка.
"""

from collections import namedtuple
from itertools import groupby

Student = namedtuple('Student', ['surname', 'name', 'grade'])

students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11), Student('Кодзаев', 'Георгий', 10),
            Student('Набокова', 'Алиса', 11), Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
            Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10), Student('Капустин', 'Илья', 11),
            Student('Гудцев', 'Таймураз', 11), Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
            Student('Елькина', 'Мария', 11),Student('Макоев', 'Руслан', 11), Student('Албегов', 'Хетаг', 11),
            Student('Щербак', 'Илья', 10), Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
            Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11), Student('Мусиков', 'Андраник', 11),
            Student('Гадзиев', 'Георгий', 11), Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
            Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10), Student('Акоева', 'Лера', 11)]

students.sort(key=lambda x: x.name)

groups = groupby(students, key=lambda x: x.name)
groups_list = [(key, list(group)) for key, group in groups]

max_result = max(groups_list, key=lambda x: len(x[1]))

most_common_name = max_result[0]
print("Most common name:", most_common_name)

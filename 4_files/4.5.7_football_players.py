"""
Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов, каждый из которых содержит информацию о каком-либо футболисте:

{
   "first_name": "Gary",
   "last_name": "Cahill",
   "team": "Chelsea",
   "position": "Defender"
}
У футболиста имеются следующие атрибуты:

first_name — имя
last_name — фамилия
team — название футбольного клуба
position — игровая позиция
Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов, выступающих
за футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен, а при совпадении —
в лексикографическом порядке фамилий, каждый на отдельной строке.

Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, что он является корректным
текстовым файлом в формате JSON.

Примечание 2. Начальная часть ответа выглядит так:

Alex Iwobi
Alexis Sanchez
...
"""

from zipfile import ZipFile
from json import load


with ZipFile('data.zip') as zip_file:
    players = []
    for i in zip_file.infolist():
        if not i.is_dir() and i.filename.endswith('.json'):
            with zip_file.open(i.filename) as j:
                try:
                    player = load(j)
                    if player['team'] == 'Arsenal':
                        players.append(f'{player["first_name"]} {player["last_name"]}')
                except ValueError:
                    pass
print(*sorted(players), sep='\n')

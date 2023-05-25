"""
Репетитор по математике проводит занятия по 45 минут с перерывами по 10 минут. Репетитор обозначает время начала
рабочего дня и время окончания рабочего дня. Напишите программу, которая генерирует и выводит расписание занятий.

Формат входных данных
На вход программе в первой строке подается время начала рабочего дня в формате HH:MM.
В следующей строке вводится время окончания рабочего дня в том же формате.

Формат выходных данных
Программа должна сгенерировать и вывести расписание занятий. На первой строке выводится время начала
и окончания первого занятия в формате HH:MM - HH:MM, на второй строке — время начала и окончания второго
занятия в том же формате, и так далее.

Примечание 1. Если занятие обрывается временем окончания работы, то добавлять его в расписание не нужно.

Примечание 2. Если разница между временем начала и окончания рабочего дня меньше 45 минут, программа ничего
не должна выводить.

Sample Input 1:
10:00
12:35

Sample Output 1:
10:00 - 10:45
10:55 - 11:40
11:50 - 12:35
"""


from datetime import datetime, timedelta


def get_timetable(start_time, end_time):
    pattern = '%H:%M'
    start_time, end_time = datetime.strptime(start_time, pattern), datetime.strptime(end_time, pattern)
    if end_time - start_time < timedelta(minutes=45):
        pass
    else:
        timetable = list()
        current_time = start_time
        while current_time + timedelta(minutes=45) <= end_time:
            timetable.append(f'{datetime.strftime(current_time, pattern)} - '
                             f'{datetime.strftime(current_time + timedelta(minutes=45), pattern)}')
            current_time += timedelta(minutes=55)
        print(*timetable, sep='\n')


get_timetable(input(), input())

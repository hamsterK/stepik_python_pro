from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]


def count_minutes(time_data):
    pattern = '%H:%M'
    minutes_counter = 0
    for i in time_data:
        time_1 = datetime.strptime(i[0], pattern)
        time_2 = datetime.strptime(i[1], pattern)
        minutes_counter += (time_2 - time_1).seconds // 60
    return minutes_counter


print(count_minutes(data))

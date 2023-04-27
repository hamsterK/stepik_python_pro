"""
Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для бронирования
номера. Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:

booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата,
либо период (две даты через дефис). Например:
['04.11.2021', '05.11.2021-09.11.2021']

date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает забронировать
номер. Например:
'01.11.2021' или '01.11.2021-04.11.2021'
"""


from datetime import datetime, timedelta


def convert_date_period(date_period):
    start_dt = datetime.strptime(date_period[:10], '%d.%m.%Y')
    end_dt = datetime.strptime(date_period[11:], '%d.%m.%Y')
    dates_to_add = list()
    delta = timedelta(days=1)
    while start_dt <= end_dt:
        dates_to_add.append(start_dt)
        start_dt += delta
    return dates_to_add


def is_available_date(booked_dates, date_for_booking):
    booked_dates_full = list()
    for i in booked_dates:
        if len(i) <= 10:
            booked_dates_full.append(datetime.strptime(i, '%d.%m.%Y'))
        else:
            for j in convert_date_period(i):
                booked_dates_full.append(j)
    if len(date_for_booking) <= 10:
        if datetime.strptime(date_for_booking, '%d.%m.%Y') not in booked_dates_full:
            return True
        else:
            return False
    else:
        for i in convert_date_period(date_for_booking):
            if i in booked_dates_full:
                return False
        return True


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

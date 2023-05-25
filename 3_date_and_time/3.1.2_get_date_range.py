from datetime import date


def get_date_range(start, end):
    list_of_dates = [date.fromordinal(i) for i in range(date.toordinal(start), date.toordinal(end) + 1)]
    return list_of_dates


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')

from datetime import datetime, time, timedelta, date
import tkinter

print(date.today())
print(datetime.now())

print(datetime(year=2024, month=2, day=29))

date_1 = datetime(year=2024, month=2, day=29)
date_today = datetime(year=2023, month=1, day=18)
print(type(date_today))

difference = date_today - date_1
print(difference)
print(type(difference))

doua_saptamani = timedelta(weeks=2, hours=2)

print(date_today + doua_saptamani)

print(date_today - doua_saptamani)

birtday = datetime(
    year=int(input('year')),
    month=int(input('month')),
    day=int(input('day')),
)

print(birtday)

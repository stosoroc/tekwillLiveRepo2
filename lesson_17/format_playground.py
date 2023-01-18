from datetime import datetime, timedelta

date_today = datetime.now()

DATE_FORMAT = '%Y/%m/%d'

DATE_TIME_FORMAT = '%Y/%m/%d %H:%M'

DATE_TIME_FORMAT_GOOGLE = '%Y/%m/%d %H:%M'

print(date_today.strftime(DATE_TIME_FORMAT))
print(date_today.strftime(DATE_FORMAT))

text_date = input("Please input date in format yyyy/mm/dd: ")
obj_date = datetime.strptime(text_date, DATE_FORMAT)
print(obj_date)
print(obj_date + timedelta(days=14))

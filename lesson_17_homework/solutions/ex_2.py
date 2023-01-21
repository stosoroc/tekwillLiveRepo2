import time
from datetime import datetime, timedelta


def get_delta_days_minutes_and_seconds(to_date):
    delta = to_date - datetime.now()
    # 3489 Secunde
    # 58 minute * 60  + 9 secunde
    return delta.days, delta.seconds // 60 // 60, (delta.seconds // 60) % 60, delta.seconds % 60


def countdown():
    to_date = None
    while not to_date:
        to_date = input('Event date: (dd/mm/yyyy hh:mm)')
        to_date = datetime.strptime(to_date, '%d/%m/%Y %H:%M')
        if to_date > datetime.now() + timedelta(days=365):
            print('Date should be at most one year ahead')
            to_date = None
    event_name = input('Event name:')
    print()
    while True:
        days, hours, minutes, seconds = get_delta_days_minutes_and_seconds(to_date)
        if days < 0:
            print(f'{event_name} is happening')
            break
        time.sleep(1)
        print(f'{days} zile, {hours} ore,  {minutes}'
              f' minute si {seconds} secunde au ramas pan la {event_name}')


countdown()

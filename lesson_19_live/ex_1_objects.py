from datetime import datetime, timedelta
from decimal import Decimal

now = datetime.now()
print(type(now))
now.day
now.year
now.minute

now + timedelta(14)

now.strftime('')

now = datetime.now()

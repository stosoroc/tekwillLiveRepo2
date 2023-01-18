from datetime import datetime

with open('date_time.txt', 'w') as file:
    file.write(datetime.now().strftime('%Y/%m/%d'))

import json

date_string_json = json.dumps(datetime.now().strftime('%Y/%m/%d'))
print(date_string_json)

import os
from datetime import datetime, timedelta

first_day = os.environ.get('GAPP_FIRST_DAY')
if first_day == None:
    first_day = "1970-01-01"

date = {'current_date': datetime.strptime(first_day, "%Y-%m-%d")}


def get_current_day():
    result = date['current_date']
    date['current_date'] += timedelta(days=1)
    return result

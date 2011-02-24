# datetime_demo.py

import datetime

# current date in YYYY-MM-DD format 
today = datetime.date.today()

print(today)

# convert year, month, day in integers to date object
lastday = datetime.date(2011, 12, 31)

print(lastday)


now = datetime.date.now()

print(now)

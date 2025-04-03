

from datetime import date

date1 = date(2024, 1, 1)
date2 = date.today()
difference = (date2 - date1).days
print(f"Number of days between {date1} and {date2}: {difference} days")

from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date + timedelta(days=7)
print(f"Date after adding 7 days: {new_date.strftime('%Y-%m-%d')}")

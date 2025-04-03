

from datetime import datetime

now=datetime.now()
print("Date formatted as DD-MM-YYYY:", now.strftime("%d-%m-%Y"))
print("Date formatted as MM/DD/YYYY:", now.strftime("%m/%d/%Y"))
print("Time in 24-hour format:", now.strftime("%H:%M:%S"))
print("Time in 12-hour format:", now.strftime("%I:%M:%S %p"))
from datetime import datetime

date_str = input("Enter a date (YYYY-MM-DD): ")
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
print(f"The day of the week is: {date_obj.strftime('%A')}")

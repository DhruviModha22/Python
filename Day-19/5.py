from datetime import datetime

date_str = "2024-01-01"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
print(f"Converted datetime object: {date_obj}")

from datetime import datetime

now = datetime.now()
date_str = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted datetime string: {date_str}")


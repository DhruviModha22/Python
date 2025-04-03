from datetime import datetime, timezone, timedelta

utc_time = datetime.now(timezone.utc)
local_time = datetime.now()

print(f"Current UTC time: {utc_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Local time: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")



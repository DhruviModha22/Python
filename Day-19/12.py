import time

reminder_time = int(input("Set a reminder in seconds: "))
print(f"Reminder set for {reminder_time} seconds...")

time.sleep(reminder_time)
print("Reminder: Time's up!")

import sys
status = input("Enter status (success/fail): ").strip().lower()
if status == "success":
    sys.exit(0)
else:
    sys.exit(1)

import sys
if len(sys.argv) < 3:
    print("Error: This script requires at least 2 arguments.")
else:
    print("Arguments provided:", ", ".join(sys.argv[1:]))

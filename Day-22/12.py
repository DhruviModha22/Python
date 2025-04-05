import sys
import os

for filename in sys.argv[1:]:
    if os.path.isfile(filename):
        print(f"{filename}: File exists.")
    else:
        print(f"{filename}: File does not exist.")

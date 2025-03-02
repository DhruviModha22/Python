counter = 0
def initialize():
    global counter
    counter = int(input("Enter initial value: "))

def increment():
    global counter
    counter += int(input("Enter increment value: "))
    print("Updated counter:", counter)

initialize()
increment()
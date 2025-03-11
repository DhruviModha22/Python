# Develop a class Counter with an attribute count initialized to zero.
# - Create methods to increment the count and display the value using self.
class Counter:
    def __init__(self):
        self.count=0
    
    def increment(self):
        self.count+=1

    def display(self):
        print(f"Count: {self.count}")

c=Counter()
c.increment()
c.increment()
c.increment()
c.display()


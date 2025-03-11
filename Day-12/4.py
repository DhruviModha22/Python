class Example:
    def display():
        print("This method does not take self!")

e = Example()
# e.display()  # This will cause an error
Example.display()  # This works

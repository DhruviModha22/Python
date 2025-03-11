class Printer:
    def print(self, *args):
        print(" ".join(map(str, args)))

p = Printer()
p.print("Hello")       # String
p.print(100)          # Integer
p.print("Age:", 25)   # String & Integer

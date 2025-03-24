class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __sub__(self, discount):
        return Book(self.title, self.price - discount)

    def __str__(self):
        return f"Book: {self.title}, Price: {self.price}"

book = Book("Python Programming", 500)
discounted_book = book - 50  # Applying a discount of 50
print(discounted_book)  # Output: Book: Python Programming, Price: 450

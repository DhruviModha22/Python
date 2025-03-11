class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

b = Book("Python Programming", "John Doe")
print("Title:", b.get_title())
print("Author:", b.get_author())

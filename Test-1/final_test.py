"""1. Library Book System is all about where you can add, view, update, Remove, Search And Display Books using this system. 
2. In this i used 2 class one for Book and another for library.
3. In Book class i created 2 function and one oop construtor.
4. In Library class i created add, view, update, remove, search function and 1 oops constutor.
5. And last but not least i created menu driven using while loop and i created function called [MAIN].
6. I use Dictionary and list DataTypes to store value.
7. I use Sorted function for sorting book.
 """

print("Welcome to the Library Book Management System\n Create by Dhruvi Modha...:)")

class Book:
    def __init__(self,book_id,title,author,copies):
        self.book_id=int(book_id)
        self.title=title
        self.author=author
        self.copies=int(copies)

    def update_info(self,title=None,author=None,copies=None):
        if title:
            self.title=title
        if author:
            self.author=author
        if copies is not None:
            self.copies=int(copies)

    def display(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Copies: {self.copies}"
    
class Library:
    def __init__(self):
        self.book={}
    
    def add_book(self,book_id,title,author,copies):
        if book_id in self.book:
            print("Book ID already exists!!!")
            return
        self.book[book_id]=Book(book_id,title,author,copies)
        print("Book added successfully....:)")

    def view_book(self):
        if not  self.book:
            print("No book available...")
        else:
            for book in self.book.values():
                print(book.display())


    def update_book(self,book_id,title=None,author=None,copies=None):
        if book_id in self.book:
            self.book[book_id].update_info(title,author,copies)
            print("Book updated successfully!!!")
        else:
            print("Book not Found!!")
    
    def remove_book(self,book_id):
        if book_id in self.book:
            del self.book[book_id]
            print("Book removed successfully...")
        else:
            print("Book not found!!")

    def search_book(self,word):
        found=[book.display() for book in self.book.values() if word.lower() in book.title.lower() or word.lower() in book.author.lower()]

        if found:
            for book in found:
                print(book)
        else:
            print("No book found!!!")
        

    def sort_book(self,by="title"):
        sorted_book=sorted(self.book.values(), key=lambda book:getattr(book,by))
        for book in sorted_book:
            print(book.display())

    def display_statistics(self):
        total_book=len(self.book)
        total_copies=sum(book.copies for book in self.book.values())
        print(f"Total books: {total_book}, Total copies: {total_copies}..")


def main():
    library=Library()
    while True:
        print("\nLibrary Book Management System\n")
        print("1. Add a new Book")
        print("2. View all Book")
        print("3. Upadate book Information")
        print("4. Remove a Book")
        print("5. Search for a Book")
        print("6. Sort and display Books")
        print("7. Display statistics")
        print("8. Exit")

        choice=input("Enter your choice: ")

        if choice=='1':
            book_id=input("Enter Book ID: ")
            title=input("Enter title: ")
            author=input("Enter Author: ")
            copies=input("Enter Number of Copies: ")
            library.add_book(book_id,title,author,copies)

        if choice=='2':
            library.view_book()

        if choice=='3':
            book_id=input("Enter book ID to update: ")
            title=input("Enter new Title: ")
            author=input("Enter new Author: ")
            copies=input("Enter new Number of copies: ")
            copies=None if copies=="" else copies
            library.update_book(book_id,title,author,copies)

        if choice=='4':
            book_id=input("Enter Book ID to remove: ")
            library.remove_book(book_id)

        if choice=='5':
            word=input("Enter title or author to search: ")
            library.search_book(word)

        if choice=='6':
            sort_by=input("Sort by (title/copies): ")
            if sort_by not in ["title","copies"]:
                # print("Invalid sort option. Default value is title.")
                sort_by="title"
            library.sort_book(by=sort_by)

        if choice=='7':
            library.display_statistics()

        if choice=='8':
            print("Thank you for visiting this Library Book Management System Created by One and Only Dhruvi Modha....:)")
            print("Exiting.....")
            break

if __name__ == "__main__":
    main()
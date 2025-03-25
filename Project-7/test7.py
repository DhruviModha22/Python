from datetime import datetime

print("Welcome to Personal Journal Manager!")
class JournalManager:
    def __init__(self,filename="journal.txt"):
        self.filename=filename

    def Add_entry(self):
        entry=input("Enter your journal entry: ")
        time=datetime.now().strftime("%y-%m-%d %H:%M:%S")
        with open(self.filename,'a')as file:
            file.write(f"{time} - {entry}\n")
        print("Enter added successfully!")

    def view_entries(self):
        try:
            with open(self.filename,'r')as file:
                entries=file.readlines()
                if not entries:
                    print("No journal entries found.")
                    return
                print("Your Journal entries: ")
                for i,entry in enumerate(entries):
                    print(f"{i}.{entry.strip()}")

        except FileNotFoundError:
            print("Journal file not found.")

    def search_entry(self):
        try:
            keyword=input("Enter a keyword or date to search: ")
            with open(self.filename,'r')as file:
                entries=file.readlines()
                found=False
                for entry in entries:
                    if keyword in entry:
                        print(f"Found: {entry.strip()}")
                        found=True

                if not found:
                    print("No entries were found for the keyword")

        except FileNotFoundError:
            print("Journal file not found.")

    def delete_entries(self):
        try:
            with open(self.filename,'w') as file:

                file.truncate(0) #Clear the file content

                print("All entries deleted successfully!")
        except FileNotFoundError:
            print("Journal file not found.")
def main():
    journal=JournalManager()
    while True:
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice=input("Choose an option: ")

        if choice=='1':
            journal.Add_entry()
        elif choice=='2':
            journal.view_entries()
        elif choice=='3':
            journal.search_entry()
        elif choice=='4':
            journal.delete_entries()
        elif choice=='5':
            print("Thank you for using Personal Journal Manager. GoodBye!!")
            break
        else:
            print("Invalid option. Please select a valid option from the menu")

if __name__=="__main__":
    main()


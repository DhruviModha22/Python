import numpy as np
import pandas as pd



# Library management system

class LibraryDashboard:
    def __init__(self):
        self.data=None

    def load_data(self,file_path):
        try:
            self.data=pd.read_csv("library_transactions.csv")

            if self.data.empty:
                raise ValueError("The file is empty. ")
            if self.data.isnull().values.any():
                print("Warning: Dataset contains missing values.")
            print("Data Loaded successfully.")
        except FileNotFoundError:
            print("Error:file not found.")
        except Exception as e:
            print(f"Error: {e}")

    def calculate_statistics(self):
        if self.data is None:
            print("Data not loaded.")
            return
        try:
            print("\n------------ Statistics-----------")
            most_borrowed=self.data['Book Title'].value_counts()
            print(f"Most Borrowed Book: {most_borrowed}")

            avg_borrow_duration=self.data['Borrowing Duration(Days)'].mean()
            print(f"Average Borrow Duration: {avg_borrow_duration: .2f} days")

            self.data['Date(YYYY-MM-DD)']=pd.to_datetime(self.data['Date(YYYY-MM-DD)'])
            busiest_day=self.data['Date(YYYY-MM-DD)'].dt.day_name().value_counts()
            print(f"Busiest day: {busiest_day}")
        
        except Exception as e:
            print(f"Error in statistics: {e}")

    def filter_transaction(self, condition):
        if self.data is None:
            print("Data not loaded.")
            return
        
        try:
            filtered=self.data.query(condition)
            print("filtered transactions: ")
            print(filtered)
        except Exception as e:
            print(f"Error filtering transcations: {e}")

    def generate_report(self):
        if self.data is None:
            print("Data not loaded. ")
            return
        
        try:
            print("\n--- Library Summary Report ---")
            print("Total Transactions: ",len(self.data))
            print("Unique users: ",self.data['User ID'].nunique())
            print("Unique Books: ",self.data['Book Title'].nunique())

            genre_group=self.data.groupby('Genre')['Book Title'].count()
            print("\nBorrowings by genre: ")
            print(genre_group)

            avg_duration_by_book=self.data.groupby('Book Title')['Borrowing Duration(Days)'].mean()
            print("\nAverage Borrow Duration by Book: ")
            print(avg_duration_by_book.sort_values(ascending=False).head(5))

        except Exception as e:
            print(f"Error generating report: {e}")


dashboard=LibraryDashboard()
dashboard.load_data("library_transactions.csv")
dashboard.calculate_statistics()
dashboard.filter_transaction('Genre=="Thriller"')
dashboard.generate_report()


    
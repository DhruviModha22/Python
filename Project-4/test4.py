print("Welcome to the Data Analyzer and Transformer Program")

# Global list to store the dataset
arr1 = []

def avg():
    """Calculate the average of the dataset"""
    if len(arr1) == 0:
        return 0
    return sum(arr1) / len(arr1)

def factorial(n):
    """Recursively calculate the factorial of a number"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Function)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("Please Enter your choice: "))

    if choice == 1:
        """Store user-input data into an array"""
        arr1 = list(map(int, input("Enter data for a 1D array (separated by spaces): ").split()))
        print("Data has been stored successfully!")

    elif choice == 2:
        """Display summary of dataset"""
        print("\nData Summary:") 
        print(f"Total elements in array: {len(arr1)}")
        print(f"Minimum value in array: {min(arr1)}")
        print(f"Maximum value in array: {max(arr1)}")
        print(f"Sum of all values in array: {sum(arr1)}")
        print(f"Average value: {avg()}")

    elif choice == 3:
        """Calculate factorial of a number using recursion"""
        num = int(input("Enter a number to calculate its factorial: "))
        print(f"Factorial of {num} is: {factorial(num)}")

    elif choice == 4:
        """Filter data using a lambda function"""
        threshold = int(input("Enter a threshold value to filter out data above this value: "))
        pass
        print(f"Filtered Data:")

    elif choice == 5:
        """Sort dataset in ascending or descending order"""
        print("Choose sorting option:")
        print("1. Ascending")
        print("2. Descending")

        ch = int(input("Enter your choice: "))
        if ch == 1:
            arr1.sort()
            print(f"Sorted Data in Ascending Order: {arr1}")
        elif ch == 2:
            arr1.sort(reverse=True)
            print(f"Sorted Data in Descending Order: {arr1}")

    elif choice == 6:
        """Display dataset statistics"""
        print("\nDataset Statistics:")
        print(f"Minimum value: {min(arr1)}")
        print(f"Maximum value: {max(arr1)}")
        print(f"Sum of all values: {sum(arr1)}")
        print(f"Average value: {avg()}")

    elif choice == 7:
        """Exit the program"""
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")

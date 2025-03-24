try:
    my_list = [1, 2, 3]
    index = int(input("Enter index: "))
    print(my_list[index])
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
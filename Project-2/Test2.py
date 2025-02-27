print("Welcome to the pattern Generator and Number Analysis")

while True:
    print("select the option: ")
    print("1. Generate a Right-angled Triangle Pattern\n2. Analyze a Range of Numbers\n3. Exit")
    choice=int(input("Enter the number(1-3): "))

        
    if choice==1:  
        num_input=(int(input("Enter the number of rows for the pattern: ")))
        print("Pattern: ")
        for i in range(1,num_input+1):
            for j in range(1,i+1):
                print("* ",end=" ")
            print()
    
    if choice==2:
        start=int(input("Enter the start of the range: "))
        end=int(input("Enter the end of the range: "))
        for i in range(start,end+1):
            if i%2==0:
                print(f"Number {i} is Even")
            else:
                print(f"Number {i} is Odd")

        total=0
        for i in range(start,end+1):
            total+=i
        print(f"Sum of all numbers from start to end is: {total} ")

    if choice==3:
        print("Exiting the program. Goodbye!")
        break



    


def menu(options):
    for i,option in enumerate(options,1):
        print(f"{i}.{option}")
    choice=input("enter your choice: ")
    return int(choice) if choice.isdigit() and 1<=int(choice)<=len(options)else None
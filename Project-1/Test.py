print("personal information:")

name=input("Enter your name: ")
age=int(input("Enter your age: "))
height=float(input("Enter your height:"))
fav_num=int(input("Enter your favourits number: "))

print("Thank you! Here is your personal information")

print("Name: "+ name , type(name), id(name))
print("Age: ", age , type(age), id(age))
print("Height: ", height , type(height), id(height))
print("Favorits Number: ", fav_num , type(fav_num), id(fav_num))

sub=2025-age

print("Your birth year is: ",sub)

print("Thank you for your personal information")
# import math
# import random
# import uuid
# import time
# import datetime

import datetime_module
import math_module
import random_module
import uuid_module
import file_module
import utils

def main():
    while True:
        print("\n Main Menu: ")
        choice =utils.menu(["DateTime Functions","Math Functions","Random Functions","UUID Functions","File Operations","Exit"])

        if choice==1:
            print("\n Datetime and Time Module:")
            dt_choice=utils.menu(["Show Current Date","Date Difference","Format Date","Countdown Timer","Stopwatch Timer","Back"])
            if dt_choice==1:
                print(f"Current Date and Time: ",datetime_module.display_current_datetime())
            elif dt_choice==2:
                d1=input("Enter first date(YYYY-MM-DD): ")
                d2=input("Enter second date(YYYY-MM-DD): ")
                print(f"Difference between {d1} and {d2}: ",datetime_module.calculate_date_difference(d1,d2))
            elif dt_choice==3:
                date=input("Enter date (YYYY-MM-DD): ")
                print("Formatted date:", datetime_module.format_date(date))
            elif dt_choice==4:
                sec=int(input("enter seconds for countdown: "))
                datetime_module.countdown_time(sec)
            elif dt_choice==5:
                datetime_module.stopwatch()
        
        elif choice==2:
            print("\n Math Module: ")
            math_choice=utils.menu(["Trigonometry","Factorial","Logarithm","Compound Interest","Area of Circle","Back"])
            if math_choice==1:
                op=input("Enter operation(sin,cos,tan): ")
                value=float(input("Enter angle in degree: "))
                print(f"Result: {math_module.trigonometry(op,value)}")
            elif math_choice==2:
                num=int(input("Enter a number: "))
                print(f"Factorial of {num}: ",math_module.factorials(num))
            elif math_choice==3:
                pass
            elif math_choice==4:
                p=float(input("Enter principal amount: "))
                r=float(input("Enter annual interest rate (in percentage): "))
                t=float(input("Enter time in years: "))
                print(f"Compound Interest: {math_module.compound_interest(p,r,t)}")
            elif math_choice==5:
                radius=float(input("Enter radius of circle: "))
                print(f"Area of Circle: {math_module.area_of_circle(radius)}")
        elif choice==3:
            print("\nRandom Module:")
            print("Random OTP: ",random_module.generate_otp())
            print("Random Password: ",random_module.generate_random_password())
            print("Random Number: ",random_module.generate_random_number())
            print("Random lists: ",random_module.generate_random_lists())
            print("Random Sample: ",random_module.random_sample)
        
        elif choice==4:
            print("\n UUID Module:")
            print("UUID1: ",uuid_module.generate_uuid1())
            print("UUID4: ",uuid_module.generate_uuid4())

        elif choice==5:
            print("\n File operations(Custom Module):")
            f_choice=utils.menu(["Write to file","Read File","Append file","Back"])
            filename=input("Enter Filename: ")
            if f_choice==1:
                content=input("Enter content: ")
                file_module.write_to_file(filename,content)
            elif f_choice==2:
                print("File content:\n",file_module.read_from_file(filename))
            elif f_choice==3:
                content=input("Enter content: ")
                file_module.append_to_file(filename,content)

        elif choice==6:
            print("Thank you....")
            break

if __name__=="__main__":
    main()
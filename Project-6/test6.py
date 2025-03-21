print("Welcome to the Reboust banking System!")

class InsufficientFundsError(Exception):
    #Custom exception for InsufficientFunds during withdraw.
    pass

class BankAccount:
    def __init__(self,owner,balance=0.0):
        self.owner=owner
        if balance<0:
            raise ValueError("Initial balance cannot be negative")
        self.balance=balance

    def deposit(self,amount):
        if amount<0:
            raise ValueError("Deposit amount must be positive.")
        self.balance+=amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def Withdraw(self,amount):
        if amount<0:
            raise ValueError("Withdraw amount must be positive.")
        if amount>self.balance:
            raise InsufficientFundsError(f"Insufficient funds! Your balance is ₹{self.balance}")
        self.balance-=amount
        print(f"Withdraw ₹{amount}. Remaining balance: ₹{self.balance}")

    def get_balance(self):
        print(f"Current Balance: ₹{self.balance}")
        return self.balance
def main():
    while True:
        print("\nPlease select an option:")
        print("1. Create account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Exit")

        choice=int(input("Enter your choice(1-5): "))

        if choice==1:
            while True:
                owner_name=input("Enter your name: ")
                try:
                    initial_balance=float(input("Enter your Initial deposit amount: ₹"))
                    if initial_balance<0:
                        raise ValueError("Initial deposit amount cannot be negative :(")
                    break
                except ValueError as e:
                    print(f"Error: {e}. Please enter a valid amount. :(")

            account=BankAccount(owner_name,initial_balance)
            print(f"Account created successfully for {owner_name} with initial balance: ₹{initial_balance}")
        elif choice==2:
            try:
                amount=float(input("Enter your Deposit amount: ₹"))
                account.deposit(amount)
            except ValueError as e:
                print(f"Error: {e} :(")

        elif choice==3:
            try:
                amount=float(input("Enter amount to withdraw: ₹"))
                account.Withdraw(amount)
            except ValueError as e:
                print(f"Error: {e} :(")
            except InsufficientFundsError as e:
                print(f"Error: {e} :(")

        elif choice==4:
            account.get_balance()

        elif choice==5:
            print("Thank you for using Robust Banking System!! GoodByee!! :(")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__=="__main__":
    main()
class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid withdrawal")

    def display_balance(self):
        print(f"Balance: {self.__balance}")

a = Account()
a.deposit(1000)
a.withdraw(500)
a.display_balance()

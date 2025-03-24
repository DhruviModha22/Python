class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient funds!")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")

account = BankAccount(500)
account.withdraw(200)  # Valid
# account.withdraw(400)  # Raises InsufficientBalanceError

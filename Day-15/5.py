class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"BankAccount(name={self.name}, balance={self.balance})"

acc = BankAccount("Alice", 5000)
print(repr(acc))  # Output: BankAccount(name=Alice, balance=5000)

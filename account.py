# Normal Account Class
class NormalAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")
        print("Current balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", self.balance)


# Example
normal = NormalAccount(200)
normal.deposit(100)
normal.withdraw(50)

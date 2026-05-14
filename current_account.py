# Current Account Class
class CurrentAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", self.balance)


# Example
current = CurrentAccount(1000)
current.withdraw(300)

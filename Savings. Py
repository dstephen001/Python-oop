class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Name: {self.account_name}")
        print(f"Current Balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_name,balance):
        super().__init__(account_name, balance)
        self.withdraw_limit =100 # Withdraw limit of $100

    # Override withdrawal behavior
    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdrawal amount cannot be more than $ {self.withdraw_limit}.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully from Savings Account.")
        else:
            print("Insufficient balance.")

# Example usage

saving1 = SavingsAccount("David", 500)
saving1.display_balance()
saving1.withdraw(50) # Allowed
saving1.withdraw(150) # Not allowed
saving1.display_balance()

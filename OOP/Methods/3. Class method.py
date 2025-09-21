# CLASS METHODS EXAMPLE
# Useful when you want to manage or query shared data across all instances

class BankAccount:
    total_accounts = 0
    total_balance = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        # Update 'class-level' data whenever a new account is created
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance

    # CLASS METHOD: returns how many accounts have been created
    @classmethod
    def get_total_accounts(cls):
        return f"Total accounts: {cls.total_accounts}"

    # CLASS METHOD: returns combined balance across all accounts
    @classmethod
    def get_total_balance(cls):
        return f"Total balance in bank: ${cls.total_balance:.2f}"

    # CLASS METHOD: creates an account with a default balance (alternative constructor)
    @classmethod
    def create_with_default_balance(cls, owner):
        return cls(owner, 100)          # Default starting balance


# Creating accounts
account1 = BankAccount("Alice", 500)
account2 = BankAccount("Bob", 1000)
account3 = BankAccount.create_with_default_balance("Charlie")  # Created via class method

# Querying class-level info (using the class itself)
print(BankAccount.get_total_accounts())
print(BankAccount.get_total_balance())

# Demonstrating the alternative constructor usage
print(f"{account3.owner}'s balance: ${account3.balance}")


# https://www.youtube.com/watch?v=g-qRKZD3FgE&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=59
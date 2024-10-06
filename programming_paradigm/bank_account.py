class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the BankAccount with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw the specified amount if funds are sufficient."""
        if amount > self.account_balance:
            return False  # Insufficient funds
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
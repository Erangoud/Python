class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, customer):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = customer
            print(f"Account created for {customer.name} with account number {account_number}.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

class Customer:
    def __init__(self, name, age, city, balance=0):
        self.name = name
        self.age = age
        self.city = city
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdraw amount.")

# Example usage
bank = Bank("MyBank")

customer1 = Customer("Alice", 30, "New York", 1000)
customer2 = Customer("Bob", 25, "Los Angeles", 500)

bank.create_account("123456", customer1)
bank.create_account("654321", customer2)

account = bank.get_account("123456")
if account:
    account.deposit(500)
    account.withdraw(200)
    print(f"Balance for account 123456: {account.check_balance()}")
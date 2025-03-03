"""
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""
class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'{self.owner} has balance: {self.balance}'

    def deposit(self,dep_balance):
        self.balance = self.balance + dep_balance
        print(f'New Balance: {self.balance}')

    def withdraw(self, rem_balance):
        if self.balance - rem_balance >= 0:
            self.balance = self.balance - rem_balance
            print(f'New Balance: {self.balance}')
        else:
            print(f'WITHDRAWAL LIMIT EXCEEDS!!! Your Balance is only: {self.balance}')

# 1. Instantiate the class
acct1 = Account('Jose',100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
print(acct1.owner)

# 4. Show the account balance attribute
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(150)
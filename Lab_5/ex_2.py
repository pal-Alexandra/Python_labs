#2. Design a bank account system with a base class Account
# and subclasses SavingsAccount and CheckingAccount.
# Implement methods for deposit, withdrawal, and interest calculation.

class Account:
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds

    def deposit(self, amount):
        if amount > 0:
            self.funds += amount
        else:
            print("Cannot deposit negative amount")

    def withdraw(self, amount):
        if amount > 0:
            if self.funds >= amount:
                self.funds-= amount
            else:
                print("Insufficient funds")
        else:
            print("Cannot withdraw negative amount")

    def __str__(self):
        return f"Account {self.name} has  {self.funds} funds"


class SavingsAccount(Account):
    def __init__(self, name, funds, interest_rate):
        super().__init__(name, funds)
        self.interest_rate = interest_rate

    def compute_interest(self):
        self.funds += self.funds * self.interest_rate / 100

    def __str__(self):
        return f"Savings Account {self.name} has {self.funds} money and interest rate {self.interest_rate}"


class CheckingAccount(Account):
    def __init__(self, name, funds):
        super().__init__(name, funds)

    def compute_interest(self):
        self.funds += 0

    def __str__(self):
        return f"Checking Account {self.name} has {self.funds} money and no interest rate"


account = Account("Account_1", 100)
print(account)
account.deposit(50)
print("Account_1 after depositing 50 funds")
print(account)
account.withdraw(20)
print("Account_1 after withdrawing 20 funds")
print(account)
print("`````````````````````````````````````````````````````````````")

savings_account = SavingsAccount("Savings_Account_1", 100, 10)
print(savings_account)
savings_account.deposit(25)
print("Savings_Account_1 after depositing 25 funds")
print(savings_account)
savings_account.withdraw(15)
print("Savings_Account_1 after withdrawing 15 funds")
print(savings_account)
print("Savings_Account_1 after computing interest")
savings_account.compute_interest()
print("Savings_Account_1 after computing interest")
print(savings_account)
print("`````````````````````````````````````````````````````````````")

checking_account = CheckingAccount("Checking_Account_1", 100)
print(checking_account)
checking_account.compute_interest()
print("Checking_Account_1 after computing interest")
print(checking_account)

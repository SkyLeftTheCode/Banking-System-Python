class Account:

    def __init__(self, accountnumber, pin, balance=0):
        self.accountnumber = accountnumber
        self.pin = pin
        self.balance = balance

    def checkbalance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            return True
        return False

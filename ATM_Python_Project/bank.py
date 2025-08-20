from account import Account


class Bank:

    def __init__(self):
        self.account = {}

    def add_account(self, accountnumber, pin, balance=0):
        acc = Account(accountnumber, pin, balance)
        self.account[accountnumber] = acc
        return acc

    def login(self, accountnumber, pin):
        acc = self.account.get(accountnumber)
        if acc and acc.pin == pin:
            return acc
        return None

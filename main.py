from Personal_account import *

class Bank:
    def __init__(self):
        self.bank_account = PersonalAccount("lol", "Bank")


class Money:
    def __init__(self):
        self.amount = 0


CBank = Bank()
print(CBank.bank_account.get_owner())
print(CBank.bank_account.get_balance())
#print(CBank.bank_account.)
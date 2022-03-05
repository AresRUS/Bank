from Banking_sector import *

CBank = Bank
print(CBank.bank_account.get_balance())
a1 = PersonalAccount("AMOGUS", "Drew")
a2 = PersonalAccount("AMOGUS", "Egor")
#print(Bank.bank_account)
CBank.transfer(CBank, CBank.bank_account, a2, "123", 500)
print(a2.get_balance())
print(CBank.bank_account.get_balance())
CBank.transfer(CBank, a2, a1, "AMOGUS", 100)
print(a2.get_balance())
print(a1.get_balance())
print(CBank.bank_account.get_balance())

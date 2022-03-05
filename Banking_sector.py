class Money:
    def __init__(self):
        self.__amount = 0

    def check(self):
        return self.__amount

    def withdraw(self, cash):
        self.__amount += cash

class PersonalAccount:
    def __init__(self, key: str, owner:str):
        if not isinstance(owner, str): raise TypeError("owner must be string")
        if not isinstance(key, str): raise TypeError("key must be string")
        self.__key = key
        self.__owner = owner
        self.__balance = Money()
        if owner == "Bank": self.__balance.withdraw(10**3)

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance.check()

    def push_money(self, amount, actor):
        if actor == "Bank": self.__balance.withdraw(amount)
        else: raise TypeError("wrong push_money actor")

    def check_key(self, key):
        if key == self.__key: return 1
        else: return 0


class Bank:
    __tax_percent = 10
    bank_account = PersonalAccount("123", "Bank")

    def get_tax_percent(self):
        return self.__tax_percent

    def transfer(self, payment_account, personal_account, key, payment_amount):
        if (not isinstance(personal_account, PersonalAccount)) or (not isinstance(payment_account, PersonalAccount)):
            raise TypeError("wrong Personal Account")
        if not isinstance(payment_amount, int):
            raise TypeError("payment amount")
        else:
            if payment_account.check_key(key) == 1:
                multiplier = 1 + self.__tax_percent / 100
                transfer = payment_amount * multiplier
                if payment_account.get_balance() >= transfer:
                    if payment_amount >= 0:
                        personal_account.push_money(payment_amount, "Bank")
                        payment_account.push_money(-transfer, "Bank")
                        self.bank_account.push_money(transfer - payment_amount, "Bank")
                    else:
                        raise TypeError("False value payment amount")
                else:
                    raise TypeError("Not enough amount")
            else:
                raise TypeError("key error")
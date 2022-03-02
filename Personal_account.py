class PersonalAccount:
    def __init__(self, key: str, owner:str):
        if not isinstance(owner, str): raise TypeError("owner must be string")
        if not isinstance(key, str): raise TypeError("key must be string")
        self.__key=key, self.__owner=owner, self.__balance=0,

    def get_owner(self):
        return self.__key

    def get_balance(self):
        return self.__balance

    def __push_money(self, amount):
        self.__balance += amount

    def transfer(self, personal_account, key, payment_amount):
        if not isinstance(personal_account, PersonalAccount):
            raise TypeError("wrong Personal Account")
        else:
            if self.__key == key:
                if self.__balance >= payment_amount:
                    if payment_amount >= 0:
                        personal_account.push_money(payment_amount)
                    else: raise TypeError("False value payment amount")
                else: raise TypeError("Not enough amount")
            else: raise TypeError("key error")

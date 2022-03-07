# в этом файле примеры работы с банком
# все обязательные для работы банка строчки отмечены [IMP]
# все print в этой программе были использованы нами исключительно для наглядности работы


from Banking_sector import *  # [IMP]подклчение файла с кодом банка

CBank = Bank  # [IMP]создание объекта класса Bank
#print(CBank.bank_account.get_balance())

a1 = PersonalAccount("AMOGUS", "Drew")  # [IMP] создания банковского счета
a2 = PersonalAccount("AMOGUS", "Egor")  # первый аргумент("AMOGUS") - пароль
                                        # второй аргумент("Egor") - владелец

#print(Bank.bank_account)

# изначально на счету находится 0, чтобы его пополнить нужно попросить денег у банка
CBank.transfer(CBank, CBank.bank_account, a2, "123", 500)  # [IMP] пополнение своего счета
# в данной строчке необходимо изменять только 2 аргумента: a2 и 500
# a2 - название переменной счета, данное вами на предыдущем шаге
# 500 - сумма пополнения


#print(a2.get_balance())
#print(CBank.bank_account.get_balance())


CBank.transfer(CBank, a2, a1, "AMOGUS", 100)  # [IMP] Перевод денег кому угодно
# расскажу поподробнее за что отвечают все аргументы
# a2 - аккаунт с которого выполняется перевод
# a1 - аккаунт кому вы переводите
# "AMOGUS" - ваш пароль
# 100 - сумма перевода


#print(a2.get_balance())
#print(a1.get_balance())
#print(CBank.bank_account.get_balance())

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"has been debited.")
        print("Remaining balance is",self.balance)
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"has been credited.")
        print("Remaining balance is",self.balance)
    def get_balance(self):
        return self.balance

acc1=Account(50000,123456789)
acc1.debit(10000)
acc1.credit(5000)
acc1.credit(50000)
acc1.debit(5000)

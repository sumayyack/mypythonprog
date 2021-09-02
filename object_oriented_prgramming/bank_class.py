#bank class

class Bank:
    bank_name="federal"
    def acCreate(self,acno,name):
        self.acno=acno
        self.name=name
        self.minimumbal=5000
        self.balance=self.minimumbal
    def deposit(self,amt):
        self.amt=amt
        self.balance+= self.amt
        print("your",Bank.bank_name,"account has been credited with amt",self.amt)
        print("ypur current balance=",self.balance)
    def withdraw(self,amnt):
        self.amnt=amnt
        if self.amnt>self.balance:
            print("insufficient balance")
        else:
            print("account debited with",self.amnt)
            self.balance-=self.amnt
            print("available balance=",self.balance)
obj=Bank()
num=int(input("enter ac no"))
obj.acCreate(num,'abc')
obj.deposit(2500)
obj.withdraw(1500)

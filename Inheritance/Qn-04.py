#Define a class Account with instance object variable balance with initial value as 0
#provide withdtraw and deposit methods. Now define a sub class
#MinimumBalanceAccount of Account with provide minimum balance. Override withdraw method according to minimum balance condition

class account:
    def balance_in_account(self):
        self.balance=0
        print("Your current balance is:",self.balance)
        
    def deposit(self):
        self.deposit_amount=eval(input("Enter deposit amount:"))
        self.balance+=self.deposit_amount
        print("{} is credited sucessfully..".format(self.deposit_amount))
        print("Your current balance is:",self.balance)

    def withdraw(self):
        self.withdraw_amount=eval(input("Enter withdraw amount:"))
        

class MinimumBalanceAccount(account):
    minimum_balance=1000
    def functions(self):
        account.balance_in_account(self)
        account.deposit(self)

    def withdraw(self):
        super().withdraw()
        if self.balance-self.withdraw_amount>=1000:
            print("{} is debited sucessfully".format(self.withdraw_amount))
            self.balance-=self.withdraw_amount
            print("Your current balance:",self.balance)

        elif self.balance<self.withdraw_amount:
            print("Oops!!  Insufficient balance!")
            print("Your current balance is:",self.balance)

        else:
            print("Your account maintainance balance is",self.minimum_balance)
'''
obj=MinimumBalanceAccount()
obj.functions()
obj.withdraw()
'''

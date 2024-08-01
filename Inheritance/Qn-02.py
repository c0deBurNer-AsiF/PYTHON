#define a class with Account instance object variables accountNo,Balance and static varible rate_of_interest.
#provide needful method.
#define subclass fixedDeposit of Account class with instance object variable time.
#provide setter and getter. Also define a calculate simple interest


class account:
    rate_of_interest=5
    def __init__(self):
        self.accountNo=int(input("Enter your account number:"))
        self.Balance=eval(input("Enter your balance:"))

class fixedDeposit(account):
    def __init__(self):
        super().__init__()
        self.time=eval(input("Enter time:"))

    def set_balance(self):
        self.Balance=eval(input("Enter your new balance:"))

    def set_time(self):    
        self.time=eval(input("Enter new time:"))

    def get_balance(self):
        return self.Balance    

    def get_time(self):
        return self.time     

    def simple_interest(self):
        return print('Simple interest is:',(self.Balance*self.time*account.rate_of_interest)/100 )
'''                        
obj=fixedDeposit()
obj.set_balance()
obj.set_time()
obj.get_balance()
obj.get_time()
obj.simple_interest()

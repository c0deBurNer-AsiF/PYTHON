'''Define a class Account with static variable rate_of_interest, instance variables balance and account number.
Make function to set values in instance object of account, show balance show rate of interest,withdraw and deposit
'''

class Account:
    rate_of_interest=7
    
    def __init__(self,a,b):
        self.account_number=a
        self.balance=b
        
    def account(self):
        print("Account created succesfully!!")
        print("Your account number is:",self.account_number)
        print("Your current balance is:",self.balance)
        print("Rate of interest",self.rate_of_interest,"%")
        
    def withdraw(self):
        w=int(input("Enter withdraw ammount:"))
        print("Withdraw",w,"succesfully\nYour current balance:",self.balance-w)if w<=self.balance else print("Insufficient balance\nYour current balance is:",self.balance)
        if w<=self.balance:
            self.balance-=w
        
    def deposit(self):
        d=int(input("Enter deposit ammount:"))
        self.balance+=d
        print("Deposit",d,"successfully\nYour current balance is",self.balance)



#check the number is a prime or not(TSRS)

def checkPrime(n):
    for i in range(2,n):
        if n%i==0:
            return print("Its not a prime number")
    else:
        return print("Its a prime number")


'''
def checkPrime(n):
    for i in range(2,n):
        if n%i==0:
            return print("Its not a prime number")
    else:
        return print("Its a prime number") 

result=checkPrime(int(input("Enter a number:")))       
'''

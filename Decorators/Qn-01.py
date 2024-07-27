#write a function to calculate HCF of two numbers. Define a decorator for HCF funtion to tell whether the two numbers are co-prime or not.

def decor_hcf(hcf_function):
    def co_prime_or_not(a,b):
         print("Its a co-prime",'HCF:',hcf_function(a,b),sep='\n') if hcf_function(a,b)==1 else print("Its not a co-prime",'HCF:',hcf_function(a,b),sep='\n')
    return co_prime_or_not           

@decor_hcf
def hcf(a,b):
    i=a if a<b else b
    for e in range(i,0,-1):
        if a%e==0 and b%e==0:
            return e

#hcf(int(input("Enter 1st number")),int(input('Enter 2nd number:')))       

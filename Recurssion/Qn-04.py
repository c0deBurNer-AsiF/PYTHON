#Write a recursive function to print first N even natural numbers in reverse order.

def Neven(n):
    if n>0:
        print(n*2,end=' ')
        Neven(n-1)
        

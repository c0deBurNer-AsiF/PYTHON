#Write a recursive function to print first N odd natural numbers in reverse order.

def Nodd(n):
    if n>0:
        print(n*2-1,end=' ')
        Nodd(n-1)
        

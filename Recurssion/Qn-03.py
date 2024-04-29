#Write a recursive function to print first N even natural numbers.

def Neven(n):
    if n>0:
        Neven(n-1)
        print(n*2,end=' ')

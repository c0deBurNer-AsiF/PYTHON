#Write a recursive function to calculate factorial of a number.


def Nfact(n):
    if n==1:
        return 1
    return n*Nfact(n-1)
    

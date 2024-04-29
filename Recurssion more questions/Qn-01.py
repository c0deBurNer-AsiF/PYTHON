#Write a recursive function to calculate sum of first N natural numbers.


def Nsum(n):
    if n==1:
        return 1
    return n+Nsum(n-1)

           
    

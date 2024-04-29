#Write a recursive function to calculate sum of first N odd natural numbers.


def Nsumodd(n):
    if n==1:
        return 1
    return 2*n-1+Nsumodd(n-1)

    

#Write a recursive function to calculate sum of first N even natural numbers.


def Nsumeven(n):
    if n==0:
        return 0
    return 2*n+Nsumeven(n-1)

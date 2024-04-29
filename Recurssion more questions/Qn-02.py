#Write a recursive function to calculate sum of squares first N natural numbers.


def Nsumsqr(n):
    if n==1:
        return 1
    return n**2+Nsumsqr(n-1)

           
    

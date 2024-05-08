#Write a recursive function to calculate factorial of a number.


def Nfact(n):
    if n==1:
        return 1
    return n*Nfact(n-1)




#2nd method using lambda expression----->
'''
k=lambda n: 1 if n==1 else n*k(n-1)
'''    

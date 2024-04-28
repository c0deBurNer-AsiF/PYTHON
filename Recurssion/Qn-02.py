#Write a recursive function to print first N natural numbers in reverse order.

def revntrl(n):
    if n==0:
        return 0
    print(n,end=' ')
    revntrl(n-1)

           

#Write a recursive function to print square of first N natural numbers.

def Nsqr(n):
    if n>0:
        Nsqr(n-1)
        print(n**2,end=' ')
        

           
    

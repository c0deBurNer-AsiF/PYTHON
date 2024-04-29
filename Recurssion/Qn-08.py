#Write a recursive function to print square of first N natural numbers in reverse order.

def Nsqr(n):
    if n>0:
        print(n**2,end=' ')
        Nsqr(n-1)
        
        

           
    

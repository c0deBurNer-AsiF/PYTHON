#Write a recursive function to print first N odd natural numbers.

def Nodd(n):
    if n>0:
        Nodd(n-1)
        print(n*2-1,end=' ')
        

           
    

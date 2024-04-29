#Write a recursive function to print cubes of first N natural numbers in reverse order.

def Ncube(n):
    if n>0:
        print(n**3,end=' ')
        Ncube(n-1)
        
        

           
    

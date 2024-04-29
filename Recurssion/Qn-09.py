#Write a recursive function to print cubes of first N natural numbers.

def Ncube(n):
    if n>0:
        Ncube(n-1)
        print(n**3,end=' ')
        

           
    

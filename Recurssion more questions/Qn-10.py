#Write a recursive function to calculate HCF of two numbers.


def hcf(a,b):
    x,y=a,b
    i=a if a<b else b
    if x%i==0 and y%i==0:
        return i
    return hcf(a=a-1,b=b-1)
    
            

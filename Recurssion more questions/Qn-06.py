#Write a recursive function to calculate sum of digit of a given number.


def Ndigit(n):
    if n<10:
        return n
    return n%10+Ndigit(n//10)
    

           
    

#write a function which takes variable length arguments to recieve arguments.
#filter out prime number and return a list a list of those prime numbers

def check_prime(*t):
    l=[]
    for n in t:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            l.append(n)           
    return l
'''
s=(eval(e) for e in input("Enter integers seprated by comma:").split(","))
result=print(check_prime(*s))
'''

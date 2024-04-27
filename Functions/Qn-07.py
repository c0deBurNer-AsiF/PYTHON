#write a python function to find Nth term of Fibonacci series.(Takes Something, Return Something)

def Nfibo(f):
    x,y=0,1
    c=None
    l=[]
    while f>0:
        c=x+y
        l.append(c)
        x,y=y,c
        f-=1
    return tuple(l) 


#2nd method--->
'''
def Nfibo(f):
    x,y=0,1
    c=None
    l=[]
    while f>0:
        c=x+y
        l.append(c)
        x,y=y,c
        f-=1
    return tuple(l)    

n=int(input("Enter a number to get Nth term of fibonacci series:"))
print(Nfibo(n))
'''

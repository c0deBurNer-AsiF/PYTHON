#print N prime numbers(TSRN)

def Nprime(n):
    p=1
    while n:
        i=2
        while i<p:
            if p%i==0:
                break
            i+=1
        else:
            print(p,end=' ')
            n-=1
        p+=1 



#2nd method--->
'''
def Nprime(n):
    p=1
    while n:
        i=2
        while i<p:
            if p%i==0:
                break
            i+=1
        else:
            print(p,end=' ')
            n-=1
        p+=1 

Nprime(int(input("How many prime numbers you want:")))           
'''

#print 1st Nth terms of fibonacci series(TSRN)

def fibo(n):
    a,b,c=-1,1,0
    while n:
        c=a+b
        print(c,end=' ')
        a,b=b,c
        n-=1


#2nd method-->

'''
def fibo(n):
    a,b,c=-1,1,0
    while n:
        c=a+b
        print(c,end=' ')
        a,b=b,c
        n-=1
fibo(int(input("How many terms you want to print:")))        
'''

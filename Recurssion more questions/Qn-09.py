#Write a recursive function to find Nth term of a Fibonacci series.


def fibo(n,x=1,y=0):
    if n>0:
        z=0
        z=x+y
        print(z,end=' ')
        fibo(n=n-1,x=y,y=z)
#output: 1 1 2 3 5 8.......

'''
def fibo(n,x=-1,y=1):
    if n>0:
        z=0
        z=x+y
        print(z,end=' ')
        fibo(n=n-1,x=y,y=z)

    
'''
#output: 0 1 1 2 3 5 8......

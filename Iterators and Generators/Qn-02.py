#write a generator to produce frist N terms of the Fibonacci series


def fibo(n):
    x,y=-1,1
    while n:
        yield x+y
        x,y=y,x+y
        n-=1
'''
g=fibo(10)
it=iter(g)
while True:
    try:
        print(next(it),end=' ')
    except StopIteration:
        break            
'''

#with for loop--->>


def fibo(n):
    x,y=-1,1
    while n:
        yield x+y
        x,y=y,x+y
        n-=1
'''
g=fibo(10)
for e in g:
    print(e,end=' ')
'''

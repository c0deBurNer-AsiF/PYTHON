#write a generator to produce first N prime number


def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def nextPrime(n):
    n+=1
    while not isPrime(n):
        n+=1
    return n
def primeList(n):
    i=2
    while n:
        yield i
        i=nextPrime(i)
        n-=1

#print([x for x in primeList(10)])  



#2nd method--->>>

def Nprime(n):
    m=2
    while n:
        i=2
        while i<m:
            if m%i==0:
                break
            i+=1
        else:
            yield m
            n-=1
        m+=1
'''
g=Nprime(10)                
it=iter(g)
while True:
    try:
        print(next(g),end=' ')
    except StopIteration:
        break    
'''


#3rd method---->>



def Nprime(n):
    m=2
    while n:
        i=2
        while i<m:
            if m%i==0:
                break
            i+=1
        else:
            yield m
            n-=1
        m+=1
'''
g=Nprime(10)
for e in g:
    print(e,end=' ')
'''

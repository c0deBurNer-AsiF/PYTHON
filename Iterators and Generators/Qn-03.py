#write a generator to produce squares of first N natural numbers

def N_natural_sqr(n):
    for i in range(1,n+1):
        yield i**2

'''
g=N_natural_sqr(10)
for i in g:
    print(i,end=' ')
'''

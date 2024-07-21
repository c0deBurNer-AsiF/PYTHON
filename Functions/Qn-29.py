#find all common factors of two given number. return a tuple of such  factors(TSRS)

def common_factors(a,b):
    l=[]
    f=a if a<b else b
    while f>0:
        if a%f==0 and b%f==0:
            l.append(f)
        f-=1    
    return tuple(l)

'''
def common_factors(a,b):
    l=[]
    f=a if a<b else b
    while f>0:
        if a%f==0 and b%f==0:
            l.append(f)
        f-=1    
    return tuple(l)
result=print(common_factors(int(input("Enter 1st number:")),int(input("Enter 2nd number:"))))
'''

#2nd method---->
'''
def factors(*x):
    s1,s2=set(),set()
    for e in x[0:1:]:
        i=1
        while i<=e:
            if e%i==0:
                s1.add(i)
            i+=1

    for e in x[1::]:
        i=1
        while i<=e:
            if e%i==0:
                s2.add(i)
            i+=1  
    t=tuple(s1.intersection(s2))
    return print(t)

result=factors(int(input("Enter 1st number:")),int(input("Enter 2nd number:")))              
''' 


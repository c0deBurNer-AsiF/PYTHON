#write a python function whicb takes a list of string as an argument and returns a dictionary
#whose each item is a pair of alphabet (as key) and list of strings begin with the alphabets.

def tup(n):
    i=0
    d={}
    for x in n:
        if i==n.index(x):
            d[x]=n.count(x)
        i+=1
    return d 


'''
def tup(n):
    i=0
    d={}
    for x in n:
        if i==n.index(x):
            d[x]=n.count(x)
        i+=1
    return d     
           
    
    
t=eval(input("Enter numbers seprated by comma:"))
print(tup(t))
'''

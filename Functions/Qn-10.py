#write a python function which takes a tuple of int values and returns a dictionary
#whose each item is a pair of int value and its frequency in the tuple

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

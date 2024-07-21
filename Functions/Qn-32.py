#to count frequency of each elements of the list and store list elements in the dict object as a keys 
#and elements frequency as Data values (TSRS)

def frequency(l):
    i,d=0,{}
    for e in l:
        if i==l.index(e):
            d[e]=l.count(e)
        i+=1    
    return print(d)
#result=frequency([e for e in input("Enter elements seprated by comma:").split(',')])        

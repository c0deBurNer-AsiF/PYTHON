#remove duplicate elements from a given list (TSRS)

def removeDuplicate(l):
    return list(set(l))
result=print(removeDuplicate([int(e) for e in input("Enter integer(seprated by comma):").split(",")]))

'''
def list(l):
    i,l1=0,[]
    for e in l:
        if i==l.index(e):
            l1.append(e)
        i+=1
    return print("Non duplicate elements are:",l1)
result=list([e for e in input("Enter elements seprated by comma:").split(',')])        
'''


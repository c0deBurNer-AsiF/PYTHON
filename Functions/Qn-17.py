#find greater among three number(TSRS)

def findGreater(x,y,z):
    if y<z:
        return print(x if x>z else z)
    else:
        return print(x if x>y else y) 



#2nd method--->
'''
def findGreater(x,y,z):
    if y<z:
        return print(x if x>z else z)
    else:
        return print(x if x>y else y)    
result=findGreater(10,55,3)
'''

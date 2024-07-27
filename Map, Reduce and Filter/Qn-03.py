#write a python script to create a list of numbers greater than a given number N(taken from user)
#for each element in a given set of numbers.Use filter function

def greater_than():
    s={eval(e) for e in input("Enter numbers:").split(",")}
    x=int(input("Enter a number for filtering:"))
    print(list(filter(lambda n:n if n>x else None,s)))
    
#greater_than()



'''
s={eval(e) for e in input("Enter integers seprated by comma:").split(',')}
y=int(input("Enter a number for filter:"))
def greater_than_or_not(x):
    if y<x:
        return x
    
print(set(filter(greater_than_or_not,s)))

'''

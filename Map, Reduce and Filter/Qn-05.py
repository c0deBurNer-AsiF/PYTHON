#write a python function to calculate HCF(Highest common Factor) of a list of numbers.
#use reduce function

from functools import reduce
def hcf(a,b):
    i=a if a<b else b
    for e in range(i,0,-1):
        if a%e==0 and b%e==0:
            return e 
def f1():  
    s=[eval(e) for e in input("Enter integers seprated by comma:").split(",")]
    print("HCF:",reduce(hcf,s)) 
#f1()    

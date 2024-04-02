#write a python script to check whether a given number is prime or not.


x=int(input("Enter a number"))
i=2
while i<x:
    if x%i==0:
        print("Non prime")
        break
    i+=1
if x==i:
    print("prime")

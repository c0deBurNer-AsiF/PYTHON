#create a list of first N terms of a Fibonacci series:

l,a,b,c,l1=int(input("Enter how many terms of fibonacci series you want see? :")),-1,1,0,[]
while l:
    c=a+b
    l1.append(c)
    a,b=b,c
    l-=1
print(l1)    

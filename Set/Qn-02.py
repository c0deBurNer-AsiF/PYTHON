#Write a python script to create a set of first N prime numbers.

n=int(input("Enter a number"))
x=2
s=set()
while n:
   if all(x%i!=0 for i in range(2,x)):
       s.add(x)
       n-=1
   x+=1
   
print(s)



#2nd method--->
'''
n=int(input("Enter how many prime numbers you want:"))
s=set()
i=2
p=1
while n>0:
    p+=1
    i=2
    while p>i:
        if p%i==0:
            break
        i+=1
    if p==i:
         s.add(p)
         n-=1
        
print(s)        
'''

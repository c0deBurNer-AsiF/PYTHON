#write a python script to create a list of first N prime numbers. Value of N is given by user

a=int(input("Enter how many prime numbers you want:"))
l=[]
i=2
n=1
while a>0:
    i=2
    n+=1
    while i<n:
        if n%i==0:
            break
        else:
            i+=1
    if i==n:
        l+=[n]
        a-=1
        
print(l)

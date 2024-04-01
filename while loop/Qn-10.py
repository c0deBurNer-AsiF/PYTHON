#write a python script to calculate product of first N odd natural numbers. Value of N is taken from user

x=int(input("Enter how many odd natural number's product you want:"))
s=1
i=x

while x>=1:
    s=s*(x*2-1)
    x-=1

print("Product of %d odd number is %d"%(i,s))    

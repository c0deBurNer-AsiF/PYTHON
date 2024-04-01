#write a python script to print sum of first N odd natural numbers. value of N taken from user

x=int(input("Enter how many natural numbers u want to print:"))
i=x
s=0
while x>=1:
    s=s+x*2-1
    x-=1
    
print("Sum of %d natural odd numbers:%d"%(i,s))    


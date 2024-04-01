#write a python script to print sum of first N natural numbers. value of N taken from user

x=int(input("Enter how many natural numbers u want to print:"))
i=x
s=0
while x>=1:
    s=s+x
    x-=1
    
print("Sum of %d numbers:%d"%(i,s))    


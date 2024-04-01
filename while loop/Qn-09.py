#write a python script to calculate factorial of a number. value of N taken from user

x=int(input("Enter how many natural numbers u want to print:"))
i=x
s=1
while x>=1:
    s=s*x
    x-=1
    
print("Factorial of %d is:%d"%(i,s))    


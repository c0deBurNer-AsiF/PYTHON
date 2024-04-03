#write a python script to calculate HCF of two numbers.

x=int(input("enter 1st number:"))
y=int(input("Enter 2nd number:"))
z=x if x<y else y
while z>0:
    if x%z==0 and y%z==0:
        break
    else:
        z-=1

print("HCF of {} and {} is {}".format(x,y,z))        
